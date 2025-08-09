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


from xivscraper.sheet import LanguageSheet, CsvSheet, extract_array1d, extract_script
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
            'levelRequired': int(cfc['ClassJobLevel{Required}']),
            'levelSync': int(cfc['ClassJobLevel{Sync}']),
            'ilevelRequired': int(cfc['ItemLevel{Required}']),
            'ilevelSync': int(cfc['ItemLevel{Sync}']),
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
        actionId = quest['Action{Reward}']
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
        if quest['Emote{Reward}'] != "0":
            emote = self.sheets['Emote'].byId(quest['Emote{Reward}'])
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

    def parse_requirements(self, script):
        prefixes = ['QST_CHECK_{:02d}', 'QST_COMP_CHK{:01d}']
        i = 1
        running = True
        requirements = []
        while i < 9: # TODO: better determine when to finish?
            for prefix in prefixes:
                key = prefix.format(i)
                value = script.get(key, None)
                if value is not None:
                    requirements.append(script[key])
            i += 1
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
        todo_seq = extract_array1d(quest, "ToDoCompleteSeq")
        has_todos = True
        while has_todos and todo_idx < 24:
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

    def quest_list_entry(self, row):
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
            'icon': icon_type['MapIcon{Available}'],
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
        requires = self.parse_requirements(script)
        if len(requires) > 0:
            out_row['requires'] = list(map(lambda it: self.generate_questListItem(it), requires))

        return out_row

    def cmd_quests(self):
        self.argparser.add_argument("rowIds", nargs="+")
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        output = []
        partQuestNo = 1 
        for rowId in self.args.rowIds:
            row = self.sheets['Quest'].byId(rowId)
            out_row = self.quest_list_entry(row)
            out_row.update({
                'partQuestNo': partQuestNo
            })
            partQuestNo += 1
            output.append(out_row)

        if self.args.yaml:
            print(dump_indented_yaml({"quests": output}))
        else:
            print(json.dumps(output))


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
        for row in currents.values():
            for c in row:
                map_names[c['map']] = {
                    'name': c['location'],
                    'exversion': c['exversion'],
                    'map': c['map']
                }


                flgset = self.sheets['AetherCurrentCompFlgSet'].findBy('Territory', c['territory'])

                current_seq = extract_array1d(flgset, "AetherCurrent")
                compflgset[c['map']] = current_seq


        output = {
            'aethercurrents': currents,
            'maps': map_names,
            'compflgset': compflgset
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
        for quest in sortedQuests:
            row = self.quest_list_entry(quest)
            row.update({
                'partQuestNo': partQuestNo
            })
            partQuestNo += 1
            out_rows.append(row)

        # import pdb; pdb.set_trace()
        # first = sortedQuests[0]
        # prereqId = first.get('PreviousQuest[0]', None)
        # if prereqId and prereqId != "0":
        #     req = self.sheets['Quest'].byId(prereqId)
        #     first['requires'] = self.generate_questListItem(req)

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


    def shadowbringer_gemstoneShops(self):
        # shadowbringers gemstone shops differ from endwalker and dawntrail 
        # afaict the references are housed on a specific CustomTalk record, id=721479
        # have not found how they are tied to a SpecialShop, but they can be inferred
        shbCustomTalkId = '721479'
        ct = self.sheets['CustomTalk'].byId(shbCustomTalkId)
        script = extract_script(ct)
        shbShopInfos = [
            {
                'eNpcResidentId': script['FATESHOP_ENPCID_LAKERAND'],
                'rank2': script['FATESHOP_REWARD_LAKELAND1'],
                'rank3': script['FATESHOP_REWARD_LAKELAND2'],
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
        ]
        def rank_from_questreq(qr, info):
            if qr == info['rank3']:
                return 3
            if qr == info['rank2']:
                return 2
            if qr == "0":
                return 1
            return None

        def _item_category(id):
            category = self.sheets['ItemUICategory'].byId(id)
            return {
                'id': category['#'],
                'name': category['Name'],
                'icon': category['Icon']
            }

        output = []
        for shopInfo in shbShopInfos:
            npc = self.sheets['ENpcResident'].byId(shopInfo['eNpcResidentId'])
            loc = self.sheets['Level'].findBy('Object', npc['#'])
            coords = self.location_coords_from_level(loc['#'])
            coords.update({'name': npc['Singular']})
            specialShop = self.sheets['SpecialShop'].byId(shopInfo['specialShopId'])

            items = extract_array1d(specialShop, 'Item{Receive}', suffix='[0]')
            costs = extract_array1d(specialShop, 'Count{Cost}', suffix='[0]')
            questReqs = extract_array1d(specialShop, 'Quest{Item}')

            count = len(list(filter(lambda it: it != "0", items)))
            inventory = []
            for i in range(0,count):
                reward_item = self.sheets['Item'].byId(items[i]) 
                rank = rank_from_questreq(questReqs[i], shopInfo)
                row = {
                    'item': {
                        'name': reward_item['Name'],
                        'id': reward_item['#'],
                        'ItemUiCategoryId': reward_item['ItemUICategory']
                    },
                    'cost': int(costs[i]),
                }
                if rank is not None:
                    row['sharedFateRank'] = rank
                else:
                    row['quest'] = questReqs[i]
                inventory.append(row)
            row = {
                'inventory': inventory,
                'npc': coords,
            }
            output.append(row)
        return output


    def other_gemstoneShops(self):

        def _extract_itemids(specialShopId):
            shop = self.sheets['SpecialShop'].byId(specialShopId)
            return list(filter(lambda it: it != '0', extract_array1d(shop, 'Item{Receive}', suffix='[0]')))

        output = []

        for fateshop in self.sheets['FateShop'].all():
            npc = self.sheets['ENpcResident'].byId(fateshop['#'])
            if not npc:
                continue
            loc = self.sheets['Level'].findBy('Object', npc['#'])
            coords = self.location_coords_from_level(loc['#'])
            coords.update({'name': npc['Singular']})

            rank1ShopId = fateshop['SpecialShop[0]']
            rank2ShopId = fateshop['SpecialShop[1]']
            rank3ShopId = fateshop['SpecialShop[2]']
            if rank2ShopId == "0":
                continue

            rank1_itemids = set(_extract_itemids(rank1ShopId))
            rank2_itemids = set(_extract_itemids(rank2ShopId)) - rank1_itemids

            specialShop = self.sheets['SpecialShop'].byId(rank3ShopId)

            items = extract_array1d(specialShop, 'Item{Receive}', suffix='[0]')
            counts = extract_array1d(specialShop, 'Count{Receive}', suffix='[0]')
            costs = extract_array1d(specialShop, 'Count{Cost}', suffix='[0]')
            achievements = extract_array1d(specialShop, 'AchievementUnlock')
            def rank_for_itemid(itemid):
                if itemid in rank1_itemids:
                    return 1
                if itemid in rank2_itemids:
                    return 2

            count = len(list(filter(lambda it: it != "0", items)))
            inventory = []
            for i in range(0,count):
                reward_item = self.sheets['Item'].byId(items[i]) 
                rank = rank_for_itemid(reward_item['#'])
                row = {
                    'item': {
                        'name': reward_item['Name'],
                        'id': reward_item['#'],
                        'ItemUiCategoryId': reward_item['ItemUICategory']
                    },
                    'cost': int(costs[i]),
                }
                if rank is not None:
                    row['sharedFateRank'] = rank
                elif achievements[i] != '0':
                    row['sharedFateRank'] = 4
                else:
                    row['sharedFateRank'] = 3
                inventory.append(row)

            row = {
                'inventory': inventory,
                'npc': coords,
            }
            output.append(row)
        return output


    def cmd_gemstoneShops(self):
        self.argparser.add_argument("--yaml", action="store_true", default=True)
        self.argparser.add_argument("--json", action="store_true", default=False)
        self.args = self.argparser.parse_args()
        self.init_sheets()

        # shbCustomTalkId = '721479'
        # ct = self.sheets['CustomTalk'].byId(shbCustomTalkId)
        # script = extract_script(ct)
        # output = script

        output = self.shadowbringer_gemstoneShops()
        output.extend(self.other_gemstoneShops())

        if self.args.json:
            print(json.dumps(output))
        else:
            print(dump_indented_yaml(output))


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
                'PreviousQuest': extract_array1d(quest, "PreviousQuest"),
                'PreviousQuestJoin': quest['PreviousQuestJoin'],
                'QuestLock': extract_array1d(quest, "QuestLock"),
                'QuestLockJoin': quest['QuestLockJoin'],
            }

        # has solo duty?        
        battle_id = script.get('QUESTBATTLE0', None)
        if battle_id is not None:
            front_matter['soloDuty'] = self.format_battle(quest, battle_id)

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


