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