#!/usr/bin/env python3


import argparse
import os
import os.path
import requests
import time
import sys
import json
import yaml

import pprint
import pdb

from xivscraper.sheet import CsvSheet, extract_array2d
from xivscraper.yaml_helpers import dump_indented_yaml


class XivQuestScraper:
    def __init__(self):
        self.argparser = argparse.ArgumentParser(description="scrape ffxiv datamined quest info")
        self.argparser.add_argument("command", nargs=1)
        self.argparser.add_argument("--cache-dir", nargs="?", default="./.xiv-cache")
        self.argparser.add_argument("--datamining-commit", nargs="?", default="master")
        self.argparser.add_argument("-v", "--verbose", action="store_true")
        pass
 
    def main(self):
        (args, unknown) = self.argparser.parse_known_args()
        meth = getattr(self, "cmd_{}".format(args.command[0]), None)
        if meth is not None:
            meth()
        else:
            print("Unknown command '{}'\n".format(args.command))
            self.argparser.print_help()
            self.argparser.exit()


    def download_file(self, url, path, chunk_size=8192):
        if self.args.verbose:
            print("fetching {} <- {}".format(path, url))
        with requests.get(url, stream=True) as reader:
            reader.raise_for_status()
            with open(path, 'wb') as writer:
                for chunk in reader.iter_content(chunk_size=chunk_size):
                    writer.write(chunk)

    def fetch_sheet(self, sheet):
        url_format = "https://github.com/{repo}/raw/refs/heads/{commit}/csv/{sheet}.csv"

        url = url_format.format(
            repo=self.args.datamining_repo,
            commit=self.args.datamining_commit,
            sheet=sheet)

        path = self._path_for_sheet(sheet)

        if not os.path.exists(path):
            parent_path = os.path.dirname(path)
            if not os.path.exists(parent_path):
                os.makedirs(parent_path)

            self.download_file(url, path)

            if self.args.verbose:
                print("sleeping {}s...".format(self.args.datamining_delay))
            time.sleep(self.args.datamining_delay)
        else:
            if self.args.verbose:
                print("Skipping {}".format(path))

    def cmd_fetch(self):
        self.argparser.add_argument("sheets", nargs="*")
        self.argparser.add_argument("--datamining-repo", nargs="?", default="xivapi/ffxiv-datamining")
        self.argparser.add_argument("--datamining-delay", nargs="?", type=float, default=1.0)
        self.args = self.argparser.parse_args()

        default_sheets = [
            'ENpcResident',
            'EventIconType',
            'Level',
            'Map',
            'PlaceName',
            'Quest',
            'QuestChapter',
            'Town',
        ]
        pprint.pprint(vars(self.args))

        sheet_names = self.args.sheets if len(self.args.sheets) else default_sheets 
        print("Okay fetching {}".format(sheet_names))
        for sheet in sheet_names:
            self.fetch_sheet(sheet)

    def _path_for_sheet(self, sheet):
        return "{}.csv".format(
            os.path.join(self.args.cache_dir, self.args.datamining_commit, sheet))


    def cmd_questList(self):
        self.argparser.add_argument("--count", type=int, default=10)
        self.argparser.add_argument("lastRowId")
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--partQuestNo", type=int, default=1)
        self.args = self.argparser.parse_args()
        # pprint.pprint(vars(self.args))

        quest_sheet = CsvSheet(self._path_for_sheet("Quest"))

        output = []
        count = self.args.count
        rowId = self.args.lastRowId
        while count > 0:
            row = quest_sheet.byId(rowId)
            out_row = {
                'name': row['Name'],
                'level': int(row['ClassJobLevel[0]']),
                'rowId': int(row['#']),
                'questId': row['Id'],
                'type': "msq",
            }
            output.append(out_row)
            rowId = row['PreviousQuest[0]']
            count -= 1

        ordered = list(reversed(output))
        numbered = []
        for i in range(0,len(ordered)):
            row = ordered[i]
            row.update({
                'partQuestNo': i+self.args.partQuestNo,
            })
            numbered.append(row)

        if self.args.yaml:
            print(dump_indented_yaml({"quests": list(numbered)}))
        else:
            pprint.pprint(ordered)


    def cmd_findQuest(self):
        self.argparser.add_argument("questId", nargs="*")
        self.argparser.add_argument("--name", default=None)
        self.argparser.add_argument("--json", action="store_true", default=True)
        self.args = self.argparser.parse_args()

        # pprint.pprint(vars(self.args))
        #print("Okay looking for {}".format(self.args.questId))
        if self.args.name is None and len(self.args.questId) < 1:
            print("Must specify questId or --name", file=sys.stderr)
            return

        quest_sheet = CsvSheet(self._path_for_sheet("Quest"))
        output = []
        if self.args.name is not None:
            match = self.args.name.lower()
            for row in quest_sheet.rows.values():
                if match in row['Name'].lower():
                    output.append(row)
        else:
            for questId in self.args.questId:
                row = quest_sheet.byId(questId)
                output.append(row)

        # d = {
        #     'ToDoCompleteSeq': extract_array2d(row, "ToDoCompleteSeq"),
        #     'ToDoQty': extract_array2d(row, "ToDoQty")
        # }
        # for i in range(0,23):
        #     k = "ToDoLocation[{}]".format(i)
        #     d[k] = extract_array2d(row, k)

        # pprint.pprint(d)

        if self.args.json: 
            print(json.dumps(output))
        else:
            pprint.pprint(output)



def main():
    app = XivQuestScraper()
    app.main()


if __name__ == "__main__":
    main()