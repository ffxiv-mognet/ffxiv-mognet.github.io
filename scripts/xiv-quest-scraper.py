#!/usr/bin/env python3


import argparse
import os
import os.path
import requests
import time

import pprint
import pdb


class XivQuestScraper:
    def __init__(self):
        self.argparser = argparse.ArgumentParser(
            description="scrape ffxiv datamined quest info")
        self.argparser.add_argument("command", nargs="?", default="fetch")
        self.argparser.add_argument("sheets", nargs="*")
        self.argparser.add_argument("--datamining-commit", nargs="?", default="master")
        self.argparser.add_argument("--datamining-repo", nargs="?", default="xivapi/ffxiv-datamining")
        self.argparser.add_argument("--datamining-delay", nargs="?", type=float, default=1.0)
        self.argparser.add_argument("--cache-dir", nargs="?", default="./.xiv-cache")
        self.argparser.add_argument("-v", "--verbose", action="store_true")
 
    def main(self):
        self.args = self.argparser.parse_args()
        meth = getattr(self, "cmd_{}".format(self.args.command), None)
        if meth is not None:
            meth()
        else:
            print("Unknown command '{}'\n".format(self.args.command))
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

        path = "{}.csv".format(
            os.path.join(self.args.cache_dir, self.args.datamining_commit, sheet))

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




def main():
    app = XivQuestScraper()
    app.main()


if __name__ == "__main__":
    main()