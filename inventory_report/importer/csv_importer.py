from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        try:
            if not filepath.endswith(".csv"):
                raise ValueError("Arquivo inválido")
            with open(filepath) as file:
                csv_reader = csv.DictReader(file, delimiter=",")
                items = [item for item in csv_reader]

            return items

        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")
