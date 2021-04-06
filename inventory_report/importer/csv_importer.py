from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        list = []
        with open(filepath, "r") as file:
            read = csv.DictReader(file, delimiter=",")
            for row in read:
                list.append(row)
        return list
