import csv

class CsvSheet:
    def __init__(self, csv_path, lazy=True):
        self.csv_path = csv_path
        self.rows = {}
        self.indexed = False
        if not lazy:
            self.buildIndex()

    def buildIndex(self):
        self.headers = []
        self.types = {}
        self.rows = {}
        with open(self.csv_path, 'r') as csvfh:
            reader = csv.reader(csvfh)
            next(reader)  # skip first line

            # parse header names and types
            columns = next(reader)
            types = next(reader)
            for i in range(0,len(columns)):
                col_name = columns[i] if columns[i] else "col{}".format(i-1)
                self.headers.append((col_name, types[i]))
                self.types[col_name] = types[i]

            # hydrate each row as a dict
            for row in reader:
                rowId = row[0]
                obj = {}
                for i in range(0, len(row)):
                    col_name = self.headers[i][0]
                    obj[col_name] = row[i]
                self.rows[rowId] = obj
        self.indexed = True

    def byId(self, rowId, default=None):
        if not self.indexed:
            self.buildIndex()
        return self.rows.get(rowId, default)

    def findBy(self, field_name, value):
        if not self.indexed:
            self.buildIndex()
        for row in self.rows.values():
            if row[field_name] == value:
                return row

    def findAll(self, field_name, value):
        if not self.indexed:
            self.buildIndex()
        for row in self.rows.values():
            if row[field_name] == value:
                yield row

    def findMatches(self, callback):
        if not self.indexed:
            self.buildIndex()
        for row in self.rows.values():
            if callback(row):
                yield row



    def find(self, cb, default=None):
        if not self.indexed:
            self.buildIndex()
        for row in self.rows.values():
            if cb(row):
                return row

    def all(self):
        if not self.indexed:
            self.buildIndex()
        return self.rows.values()



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


def extract_script(quest):
    total = 50
    output = {}
    for i in range(0, 50):
        inst_key = "Script{{Instruction}}[{}]".format(i)
        arg_key = "Script{{Arg}}[{}]".format(i)
        inst = quest[inst_key]
        arg = quest[arg_key]
        if inst:
            output[inst] = arg
    return output
