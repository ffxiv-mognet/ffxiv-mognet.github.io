#!/usr/bin/env python3

import csv
import pprint


QUESTS_CSV_PATH = ".xiv-cache/master/Quest.csv"




class QuestIndex:
    def __init__(self, csv_path=QUESTS_CSV_PATH):
        self.csv_path = csv_path
        self.quests = {}
        self.buildQuestIndex()

    def buildQuestIndex(self):
        self.quests = {}
        with open(self.csv_path, 'r') as csvfh:
            csvfh.readline()  # skip first line
            reader = csv.DictReader(csvfh)
            for row in reader:
                rowId = row["#"]
                self.quests[rowId] = row

    def find(self, rowId, default=None):
        return self.quests.get(rowId, default)

    def findParents(self, rowId, howMany=45):
        parents = []
        while howMany > 0:
            q = self.find(rowId)

            parents.append([
                rowId,
                q['Name'],
                (q['PreviousQuest[0]'], q['PreviousQuest[1]'], q['PreviousQuest[2]'], q['PreviousQuest[3]']),
                q['PreviousQuestJoin']
            ])

            rowId = q['PreviousQuest[0]']
            howMany -= 1
        return parents


def main():
    quests = QuestIndex()
    # parents = quests.findParents("70415", howMany=10)
    # pprint.pprint(list(reversed(parents)))
    q = quests.find("65781")
    import json
    print(json.dumps(q))

if __name__ == "__main__":
    main()


