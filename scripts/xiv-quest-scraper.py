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
from xivscraper.coord_helpers import readable_coords, readable_contenttype



class XivQuestScraper:
    def __init__(self):
        self.argparser = argparse.ArgumentParser(description="scrape ffxiv datamined quest info")
        self.argparser.add_argument("command", nargs=1)
        self.argparser.add_argument("--cache-dir", nargs="?", default="./.xiv-cache")
        self.argparser.add_argument("--datamining-repo", nargs="?", default="xivapi/ffxiv-datamining")
        self.argparser.add_argument("--datamining-delay", nargs="?", type=float, default=1.0)
        self.argparser.add_argument("--datamining-commit", nargs="?", default="master")
        self.argparser.add_argument("-v", "--verbose", action="store_true")
 
    def main(self):
        (args, unknown) = self.argparser.parse_known_args()
        meth = getattr(self, "cmd_{}".format(args.command[0]), None)
        if meth is not None:
            meth()
        else:
            print("Unknown command '{}'\n".format(args.command))
            self.argparser.print_help()
            self.argparser.exit()

    def init_sheets(self):
        self.sheets = {
            'QuestBattle': CsvSheet(self._path_for_sheet("QuestBattle")),
            'ContentFinderCondition': CsvSheet(self._path_for_sheet("ContentFinderCondition")),
            'EventIconType': CsvSheet(self._path_for_sheet("EventIconType")),
            'JournalGenre': CsvSheet(self._path_for_sheet("JournalGenre")),
            'Level': CsvSheet(self._path_for_sheet("Level")),
            'Map': CsvSheet(self._path_for_sheet("Map")),
            'ENpcResident': CsvSheet(self._path_for_sheet("ENpcResident")),
            'PlaceName': CsvSheet(self._path_for_sheet("PlaceName")),
            'Quest': CsvSheet(self._path_for_sheet("Quest")),
            'TerritoryType': CsvSheet(self._path_for_sheet("TerritoryType")),
            'Action': CsvSheet(self._path_for_sheet("Action")),
            'AetherCurrent': CsvSheet(self._path_for_sheet("AetherCurrent")),
            'MountSpeed': CsvSheet(self._path_for_sheet("MountSpeed")),
        }


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
        self.init_sheets()

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

    def format_battle(self, battle_id):
        battle = self.sheets['QuestBattle'].byId(battle_id)
        if battle is not None:
            return {
                'levelSync': int(battle['LevelSync']),
                'timeLimit': int(battle['TimeLimit'])
            }

    def parse_unlocks(self, quest, script):
        unlocks = []
        content_idx = 0
        while 'INSTANCEDUNGEON{}'.format(content_idx) in script:
            icId = script.get('INSTANCEDUNGEON{}'.format(content_idx), None)
            if icId is None: 
                break

            cfc = self.sheets['ContentFinderCondition'].find(lambda it: it["Content"] == icId and it["ContentLinkType"] == '1')
            unlocks.append({
                'name': cfc['Name'],
                'type': readable_contenttype(cfc['ContentType']),
                'levelRequired': int(cfc['ClassJobLevel{Required}']),
                'levelSync': int(cfc['ClassJobLevel{Sync}']),
                # 'raw': cfc
            })
            content_idx += 1


        # action reward
        actionId = quest['Action{Reward}']
        if actionId != "0":
            action = self.sheets['Action'].byId(actionId)
            unlocks.append({
                'name': action['Name'],
                'icon': action['Icon'],
                'type': "action"
            })

        # mount speed increase
        mountspeeds = self.sheets['MountSpeed'].findAll('Quest', quest['#'])
        for it in mountspeeds:
            tt = self.sheets['TerritoryType'].findBy('MountSpeed', it['#'])
            pn = self.sheets['PlaceName'].byId(tt['PlaceName'])
            unlocks.append({
                'name': pn['Name'],
                'type': 'mountspeed',
            })

        # aethercurrents
        current = self.sheets['AetherCurrent'].findBy('Quest', quest['#'])
        if current:
            unlocks.append({
                'name': 'Aether Current',
                'type': "aethercurrent"
            })

        return unlocks

    def parse_requirements(self, script):
        i = 1
        key = 'QST_CHECK_{:02d}'.format(i)
        requirements = []
        while key in script:
            requirements.append(script[key])
            i += 1
            key = 'QST_CHECK_{:02d}'.format(i)
        return requirements


    def location_coords_from_level(self, levelId):
        level = self.sheets['Level'].byId(levelId)
        if level is None:
            return {}
        map_row = self.sheets['Map'].byId(level['Map'])
        territory = self.sheets['TerritoryType'].byId(level["Territory"])
        placename = self.sheets['PlaceName'].byId(territory["PlaceName"])
        coords = readable_coords(level, map_row)
        return {
            'location': placename['Name'],
            'coords': "({x}, {y})".format(**coords),
            #'levelType': int(level['Type']),
            #'territoryIntendedUse': int(territory['TerritoryIntendedUse']),
            # 'raw': {
            #     'territory': territory
            # }
        }

    def parse_issuer(self, quest):
        issuer = self.location_coords_from_level(quest["Issuer{Location}"])
        issuer_npc = self.sheets['ENpcResident'].byId(quest["Issuer{Start}"])
        issuer['name'] = issuer_npc['Singular']
        return issuer

    def parse_steps(self, quest):
        lang_sheet_name = "quest/{section}/{questId}".format(
            section=quest["Id"].split("_", 1)[1][:3], 
            questId=quest["Id"])
        self.fetch_sheet(lang_sheet_name)
        lang_sheet = LanguageSheet(self._path_for_sheet(lang_sheet_name))
        steps = []
        todo_idx = 0
        todo_seq = extract_array2d(quest, "ToDoCompleteSeq")
        has_todos = True
        while has_todos:
            locationId = quest["ToDoLocation[{}][0]".format(todo_idx)]
            step = self.location_coords_from_level(locationId)

            todoId = "TEXT_{}_TODO_{:02d}".format(quest["Id"].upper(), todo_idx)
            step["name"] = lang_sheet.byId(todoId)

            steps.append(step)
            seq = int(todo_seq.pop(0))
            if seq == 255:
                has_todos = False
                break
            todo_idx += 1

        return steps

    def generate_questListItem(self, rowId):
        quest = self.sheets['Quest'].byId(rowId)
        genre = self.sheets['JournalGenre'].byId(quest['JournalGenre'])
        icon_type = self.sheets['EventIconType'].byId(quest['EventIconType'])
        return {
            'name': quest['Name'],
            'level': int(quest['ClassJobLevel[0]']),
            'rowId': int(quest['#']),
            'questId': quest['Id'],
            'genre': genre['Name'],
            'icon': icon_type['MapIcon{Available}'],
        }

    def cmd_questList(self):
        self.argparser.add_argument("--count", type=int, default=10)
        self.argparser.add_argument("lastRowId")
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--partQuestNo", type=int, default=1)
        self.argparser.add_argument("--firstRowId", nargs="?")
        self.args = self.argparser.parse_args()
        self.init_sheets()
        # pprint.pprint(vars(self.args))

        output = []
        count = self.args.count
        rowId = self.args.lastRowId
        while count > 0:
            row = self.sheets['Quest'].byId(rowId)
            script = extract_script(row)
            genre = self.sheets['JournalGenre'].byId(row['JournalGenre'])
            icon_type = self.sheets['EventIconType'].byId(row['EventIconType'])

            issuer = self.parse_issuer(row)
            steps = self.parse_steps(row)

            out_row = {
                'name': row['Name'],
                'level': int(row['ClassJobLevel[0]']),
                'rowId': int(row['#']),
                'questId': row['Id'],
                'genre': genre['Name'],
                'icon': icon_type['MapIcon{Available}'],
                'issuer': issuer,
                'steps': steps,
            }

            # has solo duty?        
            battle_id = script.get('QUESTBATTLE0', None)
            if battle_id is not None:
                out_row['soloDuty'] = self.format_battle(battle_id)

            # unlocks?
            unlocks = self.parse_unlocks(row, script)
            if len(unlocks):
                out_row['unlocks'] = unlocks

            # requires?
            requires = self.parse_requirements(script)
            if len(requires) > 0:
                out_row['requires'] = list(map(lambda it: self.generate_questListItem(it), requires))

            output.append(out_row)

            if self.args.firstRowId and rowId == self.args.firstRowId:
                break
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
        self.init_sheets()

        # pprint.pprint(vars(self.args))
        #print("Okay looking for {}".format(self.args.questId))
        if self.args.name is None and len(self.args.questId) < 1:
            print("Must specify questId or --name", file=sys.stderr)
            return

        self.sheets['Quest'].buildIndex()
        output = []
        if self.args.name is not None:
            match = self.args.name.lower()
            for row in self.sheets['Quest'].rows.values():
                if match in row['Name'].lower():
                    output.append(row)
        else:
            for questId in self.args.questId:
                row = self.sheets['Quest'].byId(questId)
                output.append(row)

        if self.args.json: 
            print(json.dumps(output))
        else:
            pprint.pprint(output)

    def cmd_sheet(self):
        self.argparser.add_argument("sheetName")
        self.argparser.add_argument("rowIds", nargs='*')
        self.argparser.add_argument("--json", action="store_true", default=True)
        self.args = self.argparser.parse_args()
        sheet_name = self.args.sheetName

        self.init_sheets()
        self.sheets[sheet_name] = CsvSheet(self._path_for_sheet(sheet_name))
        self.sheets[sheet_name].buildIndex()

        output = []
        keys = self.args.rowIds if len(self.args.rowIds) > 0 else self.sheets[sheet_name].rows.keys()
        #import pdb; pdb.set_trace()
        for rowId in keys:
            output.append(self.sheets[sheet_name].byId(rowId))

        if self.args.json: 
            print(json.dumps(output))
        else:
            pprint.pprint(output)

    def cmd_dumpQuest(self):
        self.argparser.add_argument("questId")
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--raw", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        quest = self.sheets['Quest'].byId(self.args.questId)


        issuer = self.parse_issuer(quest)
        steps = self.parse_steps(quest)

        script = extract_script(quest)
        genre = self.sheets['JournalGenre'].byId(quest['JournalGenre'])
        icon_type = self.sheets['EventIconType'].byId(quest['EventIconType'])

        front_matter = {
            'output': False,
            "layout": "quest",
            "steps": steps,
            "rowId": int(quest["#"]),
            "questId": quest["Id"],
            "name": quest["Name"],
            "level": int(quest["ClassJobLevel[0]"]),
            "issuer": issuer,
            'genre': genre['Name'],
            'icon': icon_type['MapIcon{Available}'],
            'action': quest["Action{Reward}"],
        }
        if self.args.raw:
            front_matter['raw'] = {
                'script': script,
            }

        # has solo duty?        
        battle_id = script.get('QUESTBATTLE0', None)
        if battle_id is not None:
            front_matter['soloDuty'] = self.format_battle(battle_id)

        unlocks = self.parse_unlocks(quest, script)
        if len(unlocks) > 0:
            front_matter['unlocks'] = unlocks

        requires = self.parse_requirements(script)
        if len(requires) > 0:
            front_matter['requires'] = list(map(lambda it: self.generate_questListItem(it), requires))

        if self.args.yaml:
            print("---\n{}\n---".format(dump_indented_yaml(front_matter)))
        else:
            pprint.pprint(ordered)


if __name__ == "__main__":
    app = XivQuestScraper()
    app.main()


