import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        try:
            assert ".csv" in filepath
            # assert filepath.endswith(".csv"), other option
            with open(filepath) as file:
                csv_reader = csv.DictReader(file, delimiter=",")
                csv_data = []
                for product in csv_reader:
                    csv_data.append(product)
                return csv_data
        except AssertionError:
            raise ValueError("Formato invalido")
        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")

# from own former project csv example:
# https://github.com/tryber/sd-05-tech-news/pull/10/files
