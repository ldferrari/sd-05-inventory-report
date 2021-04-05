import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def __init__(self):
        Importer.__init__(self)

    def import_data(path):
        try:
            assert path.endswith(".csv")
            with open(path) as file:
                filepath_reader = csv.reader(file, delimiter=",")
                header, *data = filepath_reader
        except AssertionError:
            raise ValueError("Arquivo inválido")
        else:
            newArr = []
            for item in data:
                newArr.append(dict(zip(header, item)))
            return newArr
