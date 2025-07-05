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


from xivscraper.sheet import LanguageSheet, CsvSheet, extract_array2d, extract_script
from xivscraper.yaml_helpers import dump_indented_yaml
from xivscraper.coord_helpers import readable_coords


class XivQuestScraper:
    def __init__(self):
        self.argparser = argparse.ArgumentParser(description="scrape ffxiv datamined quest info")
        self.argparser.add_argument("command", nargs=1)
        self.argparser.add_argument("--cache-dir", nargs="?", default="./.xiv-cache")
        self.argparser.add_argument("--datamining-repo", nargs="?", default="xivapi/ffxiv-datamining")
        self.argparser.add_argument("--datamining-delay", nargs="?", type=float, default=1.0)
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
        self.args = self.argparser.parse_args()

        default_sheets = [
            'ENpcResident',
            # 'EventIconType',
            'Level',
            # 'Map',
            'PlaceName',
            'Quest',
            'QuestBattle',
            'TerritoryType',
            # 'QuestChapter',
            # 'Town',
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
        battle_sheet = CsvSheet(self._path_for_sheet("QuestBattle"))

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
            battle = battle_sheet.findBy("Quest", row['#'])
            if battle is not None:
                out_row['questBattle'] = {
                    'levelSync': int(battle['LevelSync']),
                    'timeLimit': int(battle['TimeLimit'])
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

        if self.args.json: 
            print(json.dumps(output))
        else:
            pprint.pprint(output)


    def cmd_dumpQuest(self):
        self.argparser.add_argument("questId")
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.args = self.argparser.parse_args()

        level_sheet = CsvSheet(self._path_for_sheet("Level"))
        npc_sheet = CsvSheet(self._path_for_sheet("ENpcResident"))
        quest_sheet = CsvSheet(self._path_for_sheet("Quest"))
        battle_sheet = CsvSheet(self._path_for_sheet("QuestBattle"))
        territorytype_sheet = CsvSheet(self._path_for_sheet("TerritoryType"))
        placename_sheet = CsvSheet(self._path_for_sheet("PlaceName"))
        map_sheet = CsvSheet(self._path_for_sheet("Map"))

        ic_sheet = CsvSheet(self._path_for_sheet("InstanceContent"))

        quest = quest_sheet.byId(self.args.questId)

        def location_coords_from_level(levelId):
            level = level_sheet.byId(levelId)
            if level is None:
                return {}
            map_row = map_sheet.byId(level['Map'])
            territory = territorytype_sheet.byId(level["Territory"])
            placename = placename_sheet.byId(territory["PlaceName"])
            coords = readable_coords(level, map_row)
            return {
                'location': placename['Name'],
                'coords': "({x}, {y})".format(**coords),
                'levelType': int(level['Type']),
                'territoryIntendedUse': int(territory['TerritoryIntendedUse'])
            }

        issuer = location_coords_from_level(quest["Issuer{Location}"])
        issuer_npc = npc_sheet.byId(quest["Issuer{Start}"])
        issuer['name'] = issuer_npc['Singular']

        lang_sheet_name = "quest/{section}/{questId}".format(
            section=quest["Id"].split("_", 1)[1][:3], 
            questId=quest["Id"])
        self.fetch_sheet(lang_sheet_name)
        lang_sheet = LanguageSheet(self._path_for_sheet(lang_sheet_name))
        steps = []
        todo_idx = 0
        todo_seq = extract_array2d(quest, "ToDoCompleteSeq")
        while todo_idx != 255:
            locationId = quest["ToDoLocation[{}][0]".format(todo_idx)]
            step = location_coords_from_level(locationId)

            todoId = "TEXT_{}_TODO_{:02d}".format(quest["Id"].upper(), todo_idx)
            step["name"] = lang_sheet.byId(todoId)

            steps.append(step)
            todo_idx = int(todo_seq.pop(0))

        script = extract_script(quest)

        front_matter = {
            'output': False,
            "layout": "quest",
            "type": "msq",
            "steps": steps,
            "rowId": int(quest["#"]),
            "questId": quest["Id"],
            "name": quest["Name"],
            "level": int(quest["ClassJobLevel[0]"]),
            "issuer": issuer,
            #'script': script
        }

        # has solo duty?        
        battle_id = script.get('QUESTBATTLE0', None)
        if battle_id is not None:
            battle = battle_sheet.byId(battle_id)
            front_matter['questBattle'] = {
                'levelSync': int(battle['LevelSync']),
                'timeLimit': int(battle['TimeLimit'])
            }

        # unlocks content?
        unlocks = []
        content_idx = 0
        while 'INSTANCEDUNGEON{}'.format(content_idx) in script:
            icId = script.get('INSTANCEDUNGEON{}'.format(content_idx), None)
            if icId is None: 
                break
            ic = ic_sheet.byId(icId) 
            unlocks.append(ic)
            content_idx += 1
        # if len(unlocks) > 0:
            # front_matter['unlocks'] = unlocks

        if self.args.yaml:
            print("---\n{}\n---".format(dump_indented_yaml(front_matter)))
        else:
            pprint.pprint(ordered)


if __name__ == "__main__":
    app = XivQuestScraper()
    app.main()


