import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        try:
            assert filepath.endswith(".csv")
        except AssertionError:
            raise ValueError("Arquivo inválido")
        else:
            with open(filepath, "r") as file:
                data = list(csv.DictReader(file))
                return list(data)
