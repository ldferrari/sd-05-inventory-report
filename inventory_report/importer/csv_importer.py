from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, list):
        if not list.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        result_csv = []
        with open(list, "r") as date:
            reader_csv = csv.DictReader(date, delimiter=",")
            for company in reader_csv:
                result_csv.append(company)
            return result_csv
