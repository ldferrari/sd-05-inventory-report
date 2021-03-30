from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        result_csv = []
        with open(filepath, "r") as file:
            reader_csv = csv.DictReader(file, delimiter=",")
            for row in reader_csv:
                result_csv.append(row)
        return result_csv
