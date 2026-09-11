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


from xivscraper.sheet import LanguageSheet, CsvSheet, extract_array1d, extract_script, extract_dict
from xivscraper.yaml_helpers import dump_indented_yaml
from xivscraper.coord_helpers import readable_coords, readable_contenttype, pixel_coords



def scrub_boolstr(s):
    s = s.lower()
    if s in [True,1,'1','true']:
        return True
    if s in [False,0,'0','false']:
        return False
    return s


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
            'JournalSection': CsvSheet(self._path_for_sheet("JournalSection")),
            'JournalCategory': CsvSheet(self._path_for_sheet("JournalCategory")),
            'Level': CsvSheet(self._path_for_sheet("Level")),
            'Map': CsvSheet(self._path_for_sheet("Map")),
            'ENpcResident': CsvSheet(self._path_for_sheet("ENpcResident")),
            'ENpcBase': CsvSheet(self._path_for_sheet("ENpcBase")),
            'PlaceName': CsvSheet(self._path_for_sheet("PlaceName")),
            'Quest': CsvSheet(self._path_for_sheet("Quest")),
            'TerritoryType': CsvSheet(self._path_for_sheet("TerritoryType")),
            'Action': CsvSheet(self._path_for_sheet("Action")),
            'AetherCurrent': CsvSheet(self._path_for_sheet("AetherCurrent")),
            'AetherCurrentCompFlgSet': CsvSheet(self._path_for_sheet("AetherCurrentCompFlgSet")),
            'MountSpeed': CsvSheet(self._path_for_sheet("MountSpeed")),
            'Achievement': CsvSheet(self._path_for_sheet("Achievement")),
            'Emote': CsvSheet(self._path_for_sheet("Emote")),
            'EObjName': CsvSheet(self._path_for_sheet("EObjName")),
            'EObj': CsvSheet(self._path_for_sheet("EObj")),
            'QuestRedo': CsvSheet(self._path_for_sheet("QuestRedo")),
            'QuestRedoChapterUI': CsvSheet(self._path_for_sheet("QuestRedoChapterUI")),
            'QuestRedoChapterUITab': CsvSheet(self._path_for_sheet("QuestRedoChapterUITab")),
            'QuestRedoChapterUICategory': CsvSheet(self._path_for_sheet("QuestRedoChapterUICategory")),
            'CustomTalk': CsvSheet(self._path_for_sheet("CustomTalk")),
            'Item': CsvSheet(self._path_for_sheet("Item")),
            'SpecialShop': CsvSheet(self._path_for_sheet("SpecialShop")),
            'ItemUICategory': CsvSheet(self._path_for_sheet("ItemUICategory")),
            'FateShop': CsvSheet(self._path_for_sheet("FateShop")),
            'ExVersion': CsvSheet(self._path_for_sheet("ExVersion")),
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

    def format_battle(self, quest, battle_id):
        battle = self.sheets['QuestBattle'].byId(battle_id)
        if battle is not None:
            return {
                'levelSync': int(battle['LevelSync']),
                'timeLimit': int(battle['TimeLimit']),
                'id': battle_id
            }
        return {
            'levelSync': int(quest['ClassJobLevel[0]']),
            'id': battle_id,
        }

    def format_contentfindercondition(self, cfc):
        return {
            'name': cfc['Name'],
            'type': readable_contenttype(cfc['ContentType']),
            'levelRequired': int(cfc['ClassJobLevelRequired']),
            'levelSync': int(cfc['ClassJobLevelSync']),
            'ilevelRequired': int(cfc['ItemLevelRequired']),
            'ilevelSync': int(cfc['ItemLevelSync']),
            # 'raw': cfc
        }

    def parse_unlocks(self, quest, script):
        unlocks = []
        content_idx = 0
        while 'INSTANCEDUNGEON{}'.format(content_idx) in script:
            icId = script.get('INSTANCEDUNGEON{}'.format(content_idx), None)
            if icId is None: 
                break

            cfc = self.sheets['ContentFinderCondition'].find(lambda it: it["Content"] == icId and it["ContentLinkType"] == '1')
            if cfc:
                unlocks.append(self.format_contentfindercondition(cfc))
            content_idx += 1


        # action reward
        actionId = quest['ActionReward']
        if actionId != "0":
            action = self.sheets['Action'].byId(actionId)
            unlocks.append({
                'id': action['#'],
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
                'id': current['#'],
                'name': 'Aether Current',
                'type': "aethercurrent"
            })

        # emote
        if quest['EmoteReward'] != "0":
            emote = self.sheets['Emote'].byId(quest['EmoteReward'])
            unlocks.append({
                'id': emote['#'],
                'name': emote['Name'],
                'type': 'emote',
            })

        # achievements
        achievements = self.sheets['Achievement'].findMatches(
            lambda it: it['Key'] == quest['#'])
        for it in achievements:
            unlocks.append({
                'id': int(it['#']),
                'name': it['Name'],
                'type': 'achievement'
            })

        return unlocks

    def parse_requirements(self, row, script, previousId=None):
        requirements = []

        i = 1
        prefixes = ['QST_CHECK_{:02d}', 'QST_COMP_CHK{:01d}']
        quest_ids = []
        while i < 9: # TODO: better determine when to finish?
            for prefix in prefixes:
                key = prefix.format(i)
                value = script.get(key, None)
                if value is not None:
                    quest_ids.append(script[key])
            i += 1

        for j in range(0,3):
            pid = row['PreviousQuest[{}]'.format(j)]
            if pid == "0": 
                continue
            if previousId is None or pid != previousId:
                quest_ids.append(pid)

        if len(quest_ids) > 0:
            requirements = list(map(lambda it: self.generate_questListItem(it), quest_ids))

        # import pdb; pdb.set_trace()
        content_idx = 0
        while 'CHECK_CONTENT{}'.format(content_idx) in script:
            icId = script.get('CHECK_CONTENT{}'.format(content_idx), None)
            if icId is None: 
                break

            cfc = self.sheets['ContentFinderCondition'].find(
                lambda it: it["Content"] == icId and it["ContentLinkType"] == '1')
            # ic = self.sheets['InstanceContent'].byId(icId)
            # cfc = self.sheets['ContentFinderCondition'].byId(ic['ContentFinderCondition'])
            if cfc:
                requirements.append(self.format_contentfindercondition(cfc))
            content_idx += 1
        return requirements

    def location_coords_from_level(self, levelId, detailed = False):
        level = self.sheets['Level'].byId(levelId)
        if level is None:
            return {}
        map_row = self.sheets['Map'].byId(level['Map'])
        territory = self.sheets['TerritoryType'].byId(level["Territory"])
        placename = self.sheets['PlaceName'].byId(territory["PlaceName"])
        coords = readable_coords(level, map_row)
        out = {
            'location': placename['Name'],
            'coords': "({x}, {y})".format(**coords),
            #'levelType': int(level['Type']),
            #'territoryIntendedUse': int(territory['TerritoryIntendedUse']),
            # 'raw': {
            #     'territory': territory,
            #     'level': level,
            #     'map': map_row
            # }
        }
        if detailed:
            out.update({
                'coords': "({x}, {y}) z:{z}".format(**coords),
                'map': map_row['Id'],
                'pixel': pixel_coords(level, map_row),
                'territory': level["Territory"],
                'exversion': territory['ExVersion']
            })
        return out

    def parse_issuer(self, quest):
        issuer = self.location_coords_from_level(quest["IssuerLocation"])
        issuer_npc = self.sheets['ENpcResident'].byId(quest["IssuerStart"])
        issuer['name'] = issuer_npc['Singular']
        return issuer

    def parse_steps(self, quest):
        lang_sheet_name = "quest/{section}/{questId}".format(
            section=quest["Id"].split("_", 1)[1][:3], 
            questId=quest["Id"])
        self.fetch_sheet(lang_sheet_name)

        lang_sheet_path = self._path_for_sheet(lang_sheet_name)
        lang_sheet = LanguageSheet(lang_sheet_path)
        steps = []

        for todo_idx in range(0, 24):
            # todo_qty = int(quest["TodoParams[{}].ToDoQty".format(todo_idx)])
            # if todo_qty == 255 or todo_qty == 0: 
            #     continue

            locationId = quest["TodoParams[{}].ToDoLocation[0]".format(todo_idx)]
            if locationId == "0":
                break
            step = self.location_coords_from_level(locationId)
            todoId = "TEXT_{}_TODO_{:02d}".format(quest["Id"].upper(), todo_idx)
            step["name"] = lang_sheet.byId(todoId)
            if not step["name"]:
                break

            steps.append(step)
        return steps

    def generate_questListItem(self, rowId):
        quest = self.sheets['Quest'].byId(rowId)
        if quest is None:
            return None
        genre = self.sheets['JournalGenre'].byId(quest['JournalGenre'])
        icon_type = self.sheets['EventIconType'].byId(quest['EventIconType'])
        return {
            'name': quest['Name'],
            'level': int(quest['ClassJobLevel[0]']),
            'rowId': int(quest['#']),
            'questId': quest['Id'],
            'genre': genre['Name'],
            'icon': icon_type['MapIconAvailable'],
        }

    def quest_list_entry(self, row, previousId=None):
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
            'genre': {
                'id': genre['#'],
                'name': genre['Name'],
            },
            'icon': icon_type['MapIconAvailable'],
            'issuer': issuer,
            'steps': steps,
        }

        # has solo duty?        
        battle_id = script.get('QUESTBATTLE0', None)
        if battle_id is not None:
            out_row['soloDuty'] = self.format_battle(row, battle_id)

        # unlocks?
        unlocks = self.parse_unlocks(row, script)
        if len(unlocks):
            out_row['unlocks'] = unlocks

        # requires?
        requires = self.parse_requirements(row, script, previousId=previousId)
        if len(requires) > 0:
            out_row['requires'] = requires


        return out_row

    def cmd_quests(self):
        self.argparser.add_argument("rowIds", nargs="+")
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--icon", type=str, default="0")
        self.argparser.add_argument("--require-previous", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        output = []
        partQuestNo = 1 
        previousId = None
        for rowId in self.args.rowIds:
            row = self.sheets['Quest'].byId(rowId)
            out_row = self.quest_list_entry(row, previousId=previousId)
            out_row.update({
                'partQuestNo': partQuestNo
            })
            if out_row['icon'] == "0":
                out_row['icon'] = self.args.icon
            partQuestNo += 1
            if not self.args.require_previous:
                previousId = rowId
            output.append(out_row)

        if self.args.yaml:
            print(dump_indented_yaml({"quests": output}))
        else:
            print(json.dumps(output))

    def cmd_questChain(self):
        self.argparser.add_argument("--count", type=int, default=99)
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--partQuestNo", type=int, default=1)
        self.argparser.add_argument("--previousId", nargs="?")
        self.argparser.add_argument("--startingId", nargs="?")
        self.args = self.argparser.parse_args()
        self.init_sheets()
        # pprint.pprint(vars(self.args))

        if self.args.startingId:
            cur_quest = self.sheets['Quest'].byId(self.args.startingId)
        elif self.args.previousId:
            cur_quest = self.sheets['Quest'].findBy('PreviousQuest[0]', self.args.previousId)

        genre = cur_quest['JournalGenre']

        count = 1
        output = []
        previousId = None
        while cur_quest and count <= self.args.count:
            out_row = self.quest_list_entry(cur_quest, previousId=previousId)
            output.append(out_row)

            count += 1
            next_matches = list(self.sheets['Quest'].findAll('PreviousQuest[0]', cur_quest['#']))
            previousId = cur_quest['#']
            cur_quest = None
            for m in next_matches:
                if m['JournalGenre'] == genre:
                    cur_quest = m
                    break

        ordered = list(output)
        numbered = []
        for i in range(0,len(ordered)):
            row = ordered[i]
            row.update({
                'partQuestNo': i+self.args.partQuestNo,
            })
            numbered.append(row)
        print(dump_indented_yaml({"quests": list(numbered)}))


    def cmd_questList(self):
        self.argparser.add_argument("--count", type=int, default=10)
        self.argparser.add_argument("lastRowId")
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--partQuestNo", type=int, default=1)
        self.argparser.add_argument("--firstRowId", nargs="?")
        self.args = self.argparser.parse_args()
        self.init_sheets()

        output = []
        count = self.args.count
        rowId = self.args.lastRowId
        while count > 0:
            row = self.sheets['Quest'].byId(rowId)
            out_row = self.quest_list_entry(row)
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
        self.argparser.add_argument("--types", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        sheet_name = self.args.sheetName

        self.init_sheets()
        self.sheets[sheet_name] = CsvSheet(self._path_for_sheet(sheet_name))
        self.sheets[sheet_name].buildIndex()

        output = []
        if self.args.types:
            output.append(self.sheets[sheet_name].types)
        keys = self.args.rowIds if len(self.args.rowIds) > 0 else self.sheets[sheet_name].rows.keys()
        for rowId in keys:
            output.append(self.sheets[sheet_name].byId(rowId))

        if self.args.json: 
            print(json.dumps(output))
        else:
            pprint.pprint(output)

    def cmd_aethercurrents(self):
        self.argparser.add_argument("--yaml", action="store_true", default=False)
        self.argparser.add_argument("--json", action="store_true", default=True)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        currents = {}
        enames = self.sheets['EObjName'].findAll('Singular', "aether current")
        for ename in enames:
            eobj = self.sheets['EObj'].byId(ename['#'])
            level = self.sheets['Level'].findBy('Object', ename['#'])
            if level is not None:
                pos = self.location_coords_from_level(level['#'], detailed=True)
                pos.update({
                    'id': eobj['Data'],
                    'name': ename['Singular'],
                })
                row = currents.get(pos['map'], [])
                row.append(pos)
                currents[pos['map']] = row

        map_names = {}
        compflgset = {}
        quests = {}
        for row in currents.values():
            for c in row:
                map_names[c['map']] = {
                    'name': c['location'],
                    'exversion': c['exversion'],
                    'map': c['map']
                }
                flgset = self.sheets['AetherCurrentCompFlgSet'].findBy('Territory', c['territory'])

                current_seq = extract_array1d(flgset, "AetherCurrents")
                compflgset[c['map']] = current_seq

                for current_id in current_seq:
                    current = self.sheets['AetherCurrent'].byId(current_id)
                    if current and current['Quest'] != "0":
                        if c['map'] not in quests:
                            quests[c['map']] = {}
                        quests[c['map']][current_id] = {
                            'quest': current['Quest'],
                            'aethercurrent': current_id,
                        }


        output = {
            'aethercurrents': currents,
            'maps': map_names,
            'compflgset': compflgset,
            'quests': quests,
        }

        if self.args.yaml:
            print(dump_indented_yaml(output))
        else:
            print(json.dumps(output))

    def cmd_listContent(self):
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.argparser.add_argument("contentFinderConditionIds", nargs="+")
        self.args = self.argparser.parse_args()
        self.init_sheets()

        output = []
        for id in self.args.contentFinderConditionIds:
            cfc = self.sheets['ContentFinderCondition'].byId(id)
            output.append(self.format_contentfindercondition(cfc))

        if self.args.yaml:
            print(dump_indented_yaml(output))
        else:
            print(json.dumps(output))

    def cmd_findContent(self):
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.argparser.add_argument("query")
        self.args = self.argparser.parse_args()
        self.init_sheets()

        q = self.args.query.lower()

        rows = self.sheets['ContentFinderCondition'].findMatches(lambda it: q in it['Name'].lower())
        output = []
        for cfc in rows:
            output.append(self.format_contentfindercondition(cfc))

        if self.args.yaml:
            print(dump_indented_yaml(output))
        else:
            print(json.dumps(output))

    def cmd_newgame(self):
        # QuestRedoChapterUITab > QuestRedoChapterUICategory > QuestRedoChapterUI
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        tabs = {}
        for chapter_row in self.sheets['QuestRedoChapterUI'].all():
            tab_row = self.sheets['QuestRedoChapterUITab'].byId(chapter_row['UITab'])
            category_row = self.sheets['QuestRedoChapterUICategory'].byId(chapter_row['Category'])
            t = tabs.get(tab_row['#'], {})
            c = t.get(category_row['#'], [])
            c.append(chapter_row)
            t[category_row['#']] = c
            tabs[tab_row['#']] = t

        output = {
            'tabs': list(tabs.values())
        }
        if self.args.json:
            print(json.dumps(output))
        else:
            print(dump_indented_yaml(output))

    def cmd_newgameQuests(self):
        self.argparser.add_argument("chapterName")
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        query = self.args.chapterName.lower()
        chapter = self.sheets['QuestRedoChapterUI'].find(lambda it: query in it['ChapterName'].lower())
        redos = self.sheets['QuestRedo'].findAll('Chapter', chapter['#'])
        quests = []

        partQuestNo = 1
        for redo in redos:
            questIds = extract_array1d(redo, "Quest")
            for questId in questIds:
                if questId == "0":
                    continue
                quest = self.sheets['Quest'].byId(questId)
                row = self.quest_list_entry(quest)
                row.update({
                    'partQuestNo': partQuestNo
                })
                partQuestNo += 1
                quests.append(row)

        output = {
            'quests': quests
        }
        if self.args.json:
            print(json.dumps(output))
        else:
            print(dump_indented_yaml(output))



    def cmd_journal(self):
        # JournalSection [tabs] > JournalCategory [dropdown] > JournalGenre [section]
        # e.g.:  Sidequest > Chronicles of Light > Tales of the Dragonsong War
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        sections = []
        for section_row in self.sheets['JournalSection'].all():
            category_rows = self.sheets['JournalCategory'].findAll('JournalSection', section_row['#'])

            categories = []
            for category_row in category_rows:
                genre_rows = self.sheets['JournalGenre'].findAll('JournalCategory', category_row['#'])
                categories.append({
                    'id': category_row['#'],
                    'name': category_row['Name'],
                    'genres': list(map(lambda it: {
                        'id': it['#'],
                        'name': it['Name'],
                        'icon': it['Icon'],
                        'visible': scrub_boolstr(it['col2']),
                    }, genre_rows))
                })

            sections.append({
                'id': section_row['#'],
                'name': section_row['Name'],
                'categories': categories,
                'visible': scrub_boolstr(section_row['col1']),
                'col2': scrub_boolstr(section_row['col2']),
            })

        output = {
            'sections': sections
        }
        if self.args.json:
            print(json.dumps(output))
        else:
            print(dump_indented_yaml(output))

    def cmd_genreQuests(self):
        self.argparser.add_argument("genreName")
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.argparser.add_argument("--brief", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        match = self.args.genreName.lower()
        genre = None
        try:
            genre_id = int(match)
            genre = self.sheets['JournalGenre'].byId(match)
        except ValueError:
            genre = next(self.sheets['JournalGenre'].findMatches(lambda it: match in it['Name'].lower()))

        quests = self.sheets['Quest'].findAll('JournalGenre', genre['#'])
        sortedQuests = sorted(quests, key=lambda it: int(it['SortKey']))

        out_rows = []
        partQuestNo = 1
        previousId = None
        for quest in sortedQuests:
            row = self.quest_list_entry(quest, previousId=previousId)
            row.update({
                'partQuestNo': partQuestNo
            })
            partQuestNo += 1
            previousId = quest['#']
            out_rows.append(row)

        output = {
            "quests": out_rows,
            "genre": {
                'genreId': genre['#'],
                'name': genre['Name']
            }
        }
        if self.args.json:
            print(json.dumps(output))
        else:
            print(dump_indented_yaml(output))

    def cmd_uiItemCategories(self):
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()
        output = {}

        for cat in self.sheets['ItemUICategory'].all():
            if not cat['Name']:
                continue
            output[cat['#']] = {
                'name': cat['Name'],
                'icon': cat['Icon']
            }

        if self.args.json:
            print(json.dumps(output))
        else:
            print(dump_indented_yaml(output))

    def shadowbringer_gemstoneShops(self):
        # shadowbringers gemstone shops differ from endwalker and dawntrail 
        # afaict the references are housed on a specific CustomTalk record, id=721479
        # have not found how they are tied to a SpecialShop, but they can be inferred
        # from ENpcBase.ENpcData[1] for the FATESHOP_ENPCID_*
        shbCustomTalkId = '721479'
        ct = self.sheets['CustomTalk'].byId(shbCustomTalkId)
        script = extract_script(ct, prefix='Script')

        city_script = extract_script(self.sheets['CustomTalk'].byId('721480'), prefix='Script')

        shbShopInfos = [
            {
                'eNpcResidentId': script['FATESHOP_ENPCID_LAKERAND'],  # 1769627
                'rank2': script['FATESHOP_REWARD_LAKELAND1'],  # 80
                'rank3': script['FATESHOP_REWARD_LAKELAND2'],  # 81
                'specialShopId': '1769959'
            },
            {
                'eNpcResidentId': script['FATESHOP_ENPCID_KHOLUSIA'],
                'rank2': script['FATESHOP_REWARD_KHOLUSIA1'],
                'rank3': script['FATESHOP_REWARD_KHOLUSIA2'],
                'specialShopId': '1769960'
            },
            {
                'eNpcResidentId': script['FATESHOP_ENPCID_AMHARAENG'],
                'rank2': script['FATESHOP_REWARD_AMHARAENG1'],
                'rank3': script['FATESHOP_REWARD_AMHARAENG2'],
                'specialShopId': '1769961'
            },
            {
                'eNpcResidentId': script['FATESHOP_ENPCID_ILMHEG'],
                'rank2': script['FATESHOP_REWARD_ILMHEG1'],
                'rank3': script['FATESHOP_REWARD_ILMHEG2'],
                'specialShopId': '1769962'
            },
            {
                'eNpcResidentId': script['FATESHOP_ENPCID_RAKTIKA'],
                'rank2': script['FATESHOP_REWARD_RAKTIKA1'],
                'rank3': script['FATESHOP_REWARD_RAKTIKA2'],
                'specialShopId': '1769963'
            },
            {
                'eNpcResidentId': script['FATESHOP_ENPCID_THETEMPEST'],
                'rank2': script['FATESHOP_REWARD_THETEMPEST1'],
                'rank3': script['FATESHOP_REWARD_THETEMPEST2'],
                'specialShopId': '1769964'
            },

            {
                'eNpcResidentId': city_script['FATESHOP_ENPCID_THECRYSTARIUM'],
                'rank2': "0",
                'rank3': "0",
                'specialShopId': '1769957'
            },
            {
                'eNpcResidentId': city_script['FATESHOP_ENPCID_EULMORE'],
                'rank2': "0",
                'rank3': "0",
                'specialShopId': '1769958'
            },
        ]
        def _rank_from_quest(qid, shbInfo):
            if shbInfo['rank2'] == '0':
                return -1
            if qid == shbInfo['rank3']:
                return 3
            if qid == shbInfo['rank2']:
                return 2
            return 1

        output = []
        for shopInfo in shbShopInfos:
            npc = self.sheets['ENpcResident'].byId(shopInfo['eNpcResidentId'])
            loc = self.sheets['Level'].findBy('Object', npc['#'])
            coords = self.location_coords_from_level(loc['#'])
            coords.update({'name': npc['Singular']})

            specialShop = self.sheets['SpecialShop'].byId(shopInfo['specialShopId'])
            shop = self.parse_specialshop(specialShop)

            # update inventory with ranks
            for inv in shop['inventory']:
                if 'questId' in inv:
                    inv['rank'] = _rank_from_quest(inv['questId'], shopInfo)
                else:
                    inv['rank'] = 1

            shop.update({
                'npcs': [coords],
                'map': {
                  'id': loc['Map'],
                  'name': coords['location'],
                },
                'version': {
                    'id': "3",
                    'name': 'Shadowbringers'
                },
            })

            output.append(shop)

        return output


    def other_gemstoneShops(self):

        def _extract_itemids(specialShopId):
            shop = self.sheets['SpecialShop'].byId(specialShopId)
            for i in range(0,60):
                for j in range(0,2):
                    k = 'Item[{}].Item[{}]'.format(i,j)
                    if shop[k] != "0":
                        yield shop[k]

        output = []

        for fateshop in self.sheets['FateShop'].all():
            npc = self.sheets['ENpcResident'].byId(fateshop['#'])
            if not npc:
                continue
            loc = self.sheets['Level'].findBy('Object', npc['#'])
            tt = self.sheets['TerritoryType'].byId(loc['Territory'])
            version = self.sheets['ExVersion'].byId(tt['ExVersion'])
            coords = self.location_coords_from_level(loc['#'])
            coords.update({'name': npc['Singular']})

            rank1ShopId = fateshop['SpecialShop[0]']
            rank2ShopId = fateshop['SpecialShop[1]']
            rank3ShopId = fateshop['SpecialShop[2]']

            rank1_itemids = set(_extract_itemids(rank1ShopId))
            if rank2ShopId != "0":
                rank2_itemids = set(_extract_itemids(rank2ShopId)) - rank1_itemids
                specialShop = self.sheets['SpecialShop'].byId(rank3ShopId)
            else:
                specialShop = self.sheets['SpecialShop'].byId(rank1ShopId)

            def _rank_for_itemid(itemid, achievementid):
                if rank2ShopId == "0":
                    # mak rank FATE shop
                    return -1

                if itemid in rank1_itemids:
                    return 1
                if itemid in rank2_itemids:
                    if rank2ShopId == rank3ShopId:  # Endwalker
                        return 3 if achievementid != '0' else 2
                    return 2
                return 4 if achievementid != '0' else 3

            shop = self.parse_specialshop(specialShop)

            # update inventory with ranks
            for inv in shop['inventory']:
                itemId = inv['items'][0]['item']['id']
                achievementId = inv.get('achievementId', '0')
                inv['rank'] = _rank_for_itemid(itemId, achievementId)

            shop.update({
                'npcs': [coords],
                'map': {
                    'id': loc['Map'],
                    'name': coords['location'],
                },
                'version': {
                    'id': version['#'],
                    'name': version['Name']
                },
                'fateShopId': fateshop['#']
            })
            output.append(shop)
        return output

    def cmd_gemstoneShops(self):
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        shops = self.shadowbringer_gemstoneShops()
        shops.extend(self.other_gemstoneShops())

        output = self.indexed_shops(shops)

        if self.args.json:
            print(json.dumps(output))
        else:
            print(dump_indented_yaml(output))

    def npc_for_resident(self, npcId):
        resident = self.sheets['ENpcResident'].byId(npcId)
        loc = self.sheets['Level'].findBy('Object', npcId)
        npc = {
            'name': resident['Singular']
        }
        if loc:
            npc.update(self.location_coords_from_level(loc['#']))
        return npc

    def parse_specialshop(self, specialShop):
        inventory = []
        for i in range(0, 60):
            invrow = extract_dict(specialShop, 'Item[{}].'.format(i))

            if invrow['Item[0]'] == "0":
                continue

            inv = {
                'items': [],
                'costs': [],
                'order': int(invrow['Order']),
            }

            # up to two different items can be received
            for j in range(0,2):
                reward_id = invrow['Item[{}]'.format(j)]
                if reward_id == "0":
                    continue
                reward_item = self.sheets['Item'].byId(reward_id) 
                category = self.sheets['ItemUICategory'].byId(reward_item['ItemUICategory'])
                inv['items'].append({
                    'quantity': invrow['ReceiveCount[{}]'.format(j)],
                    'item': {
                        'name': reward_item['Name'],
                        'id': reward_item['#'],
                        'category': {
                            'id': category['#'],
                            'name': category['Name'],
                            'icon': category['Icon']
                        }
                    }
                })

            # may require up to 3 different currency types to purchase
            for k in range(0,3):
                currency_id = invrow['ItemCost[{}]'.format(k)]
                if currency_id == "0":
                    continue
                currency_item = self.sheets['Item'].byId(currency_id)
                inv['costs'].append({
                    'quantity': invrow['CurrencyCost[{}]'.format(k)],
                    'currency': {
                        'id': currency_item['#'],
                        'name': currency_item['Name'],
                        'plural': currency_item['Plural'],
                        'icon': currency_item['Icon'],
                    },
                })

            if invrow['Quest'] != '0':
                inv['questId'] = invrow['Quest']
                quest = self.generate_questListItem(invrow['Quest'])
                if quest:
                    inv['quest'] = quest

            if invrow['AchievementUnlock'] != '0':
                inv['achievementId'] = invrow['AchievementUnlock']

            inventory.append(inv)

        shop = {
            'id': specialShop['#'],
            'name': specialShop['Name'],
            'inventory': inventory,
        }
        if specialShop['Quest'] != '0':
            shop['requires'] = self.generate_questListItem(specialShop['Quest'])
        return shop

    def cmd_alliedShops(self):
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        specialShopRefs = [
            # realm reborn
            {"#": "1769627", "Name": "Steel Amalj'ok Exchange"}, # amalj'aa
            {"#": "1769628", "Name": "Sylphic Goldleaf Exchange"}, # sylph
            {"#": "1769629", "Name": "Titan Cobaltpiece Exchange"}, # kobold
            {"#": "1769630", "Name": "Rainbowtide Psashp Exchange"}, # sahagin
            {"#": "1769525", "Name": "Ixali Oaknot Exchange"}, # ixali

            # heavensward
            {"#": "1769631", "Name": "Vanu Whitebone Exchange"},    # vanu vanu
            {"#": "1769665", "Name": "Black Copper Gil Exchange"},  # vath
            {"#": "1769685", "Name": "Carved Kupo Nut Exchange"},   # moogle society

            # stormblood
            {"#": "1769818", "Name": "Kojin Sango Exchange"},        # kojin
            {"#": "1769847", "Name": "Ananta Dreamstaff Exchange"},  # ananta
            {"#": "1769868", "Name": "Namazu Koban Exchange"},       # namazu

            # shadowbringers
            {"#": "1770040", "Name": "Fae Fancies"},                  # pixie
            {"#": "1770046", "Name": "Qitari Compliment Exchange"},   # qitari
            {"#": "1770285", "Name": "Hammered Frogments Exchange"},  # dwarf

            # endwalker
            {"#": "1770550", "Name": "Arkasodara Pana Exchange"},    # arkasodara
            {"#": "1770605", "Name": "Omicron Omnitoken Exchange"},  # omicron
            {"#": "1770647", "Name": "Loporrit Carat Exchange"},     # loporrit

            # dawntrail
            {"#": "1770890", "Name": "Pelu Pelplume Exchange"},     # pelupelu
            {"#": "1770924", "Name": "Mamool Ja Nanook Exchange"},  # mamool ja
        ]

        gilShopRefs = [
            # realm reborn
            {"#": "262692"},  # amalj'aa
            {"#": "262693"},  # sylph
            {"#": "262694"},  # kobold
            {"#": "262695"},  # sahagin
            {"#": "262696"},  # ixali

            # heavensward
            {"#": "262697"},  # vanu vanu
            {"#": "262698"},  # vath
            {"#": "262699"},  # moogle society

            # stormblood
            {"#": "262917"}, # namazu
        ]
 
        output = self.scrape_specialShops(specialShopRefs)

        if self.args.json:
            print(json.dumps(output))
        else:
            print(dump_indented_yaml(output))

    def cmd_huntShops(self):
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        specialShopRefs = [
            # allied seals
            {"#": "1769811", "Name": "Allied Seals (Other)"},  # Hunt billmaster (realm reborn)
            {"#": "1770032", "Name": "Exchange Allied Seals"},  # maudlin latool ja (blue mage)

            # centurio seals
            {"#": "1769577", "Name": "", "npcIds": ["1012225"]},   # ardolain (heavensward)
            {"#": "1769578", "Name": "", "npcIds": ["1012225"]},   # clan mark logs
            {"#": "1769782", "Name": "Centurio Seal Exchange I"},  # leuekin/estrild (stormblood)
            {"#": "1769783", "Name": "Centurio Seal Exchange II"}, # billebaut/satsuya (shadowbringers)

            # sack of nuts
            {"#": "1769987", "Name": "Sacks of Nuts Exchange"},  # xylle/ilfroy (shadowbringers)
            {"#": "1770476", "Name": "Sacks of Nuts Exchange"},  # j'lakshai/wilmetta (endwalker)
            {"#": "1770761", "Name": "Sacks of Nuts Exchange"},  # rubool ja (dawntrail)

            # clan mark logs, fate tokens, mount tokens
            {"#": "1769728", "Name": "Uncanny Knickknacks"}, # aelina (realm reborn)
            {"#": "1769511", "Name": "Uncanny Knickknacks"}, # bertana (heavensward)
            {"#": "1769807", "Name": "Wondrous Sundries"},  # eschina (stormblood)
            {"#": "1770015", "Name": "Glorious Gewgaws"}, # fathard (shadowbringers)
            {"#": "1770456", "Name": "Out-of-this-world Oddities"}, # nesvaaz (endwalker)
            {"#": "1770885", "Name": "Sublime Curiosities"}, # uah'shepya (dawntrail)
        ]
        output = self.scrape_specialShops(specialShopRefs)
        if self.args.json:
            print(json.dumps(output))
        else:
            print(dump_indented_yaml(output))

    def indexed_shops(self, shops):
        categories = {}
        currencies = {}
        for shop in shops: 
            for inv in shop["inventory"]:
                for item in inv['items']:
                    cat = item['item']['category']
                    categories[cat['id']] = cat
                for cost in inv['costs']:
                    currencies[cost['currency']['id']] = cost['currency']
        return {
            'shops': shops,
            'categories': list(categories.values()),
            'currencies': list(currencies.values()),
        }

    def scrape_specialShops(self, specialShopRefs):
        shops = {}
        for ref in specialShopRefs:
            shop = self.sheets['SpecialShop'].byId(ref['#'])
            parsed = self.parse_specialshop(shop)
            parsed['npcs'] = list(self.npc_for_resident(it) for it in ref.get('npcIds',[]))
            shops[shop['#']] = parsed

        # find all npcs with shops 
        shopIds = list(map(lambda it: it['id'], shops.values()))
        for base in self.sheets['ENpcBase'].all():
            data = extract_array1d(base, 'ENpcData')
            for shopId in data:
                if shopId in shopIds:
                    shops[shopId]['npcs'].append(self.npc_for_resident(base['#']))

        flattened = list(shops.values())
        return self.indexed_shops(flattened)


if __name__ == "__main__":
    app = XivQuestScraper()
    app.main()


