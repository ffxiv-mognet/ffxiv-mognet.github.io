import csv

class CsvSheet:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.rows = {}
        self.buildIndex()

    def buildIndex(self):
        self.rows = {}
        with open(self.csv_path, 'r') as csvfh:
            csvfh.readline()  # skip first line
            reader = csv.DictReader(csvfh)
            for row in reader:
                rowId = row["#"]
                self.rows[rowId] = row

    def byId(self, rowId, default=None):
        return self.rows.get(rowId, default)

    def findBy(self, field_name, value, default=None):
        for row in self.rows.values():
            if row[field_name] == value:
                return row


class LanguageSheet:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.rows = {}
        self.buildIndex()

    def buildIndex(self):
        self.rows = {}
        with open(self.csv_path, 'r') as csvfh:
            for i in range(0,3): 
                csvfh.readline()  # skip first 3 lines
            reader = csv.reader(csvfh)
            for row in reader:
                stringId = row[1]
                stringValue = row[2]
                self.rows[stringId] = stringValue

    def byId(self, stringId, default=None):
        return self.rows.get(stringId, default)



def extract_array2d(row, field_name):
    output = {} 
    prefix = "{}[".format(field_name)
    for key in row.keys():
        if not key.startswith(prefix):
            continue
        idx = int(key[len(prefix):-1])
        output[idx] = row[key]
    highest = max(output.keys())

    f = [None] * (highest+1)
    for i in output.keys():
        f[i] = output[i]
    return f