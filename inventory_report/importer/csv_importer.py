from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, list):
        if not list.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        result = []
        with open(list, "r") as data:
            reader_csv = csv.DictReader(data, delimiter=",")
            for company in reader_csv:
                result.append(company)
            return result
