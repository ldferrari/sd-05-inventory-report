from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if ".json" not in filepath:
            raise ValueError("Arquivo inválido")

        with open(filepath) as file:
            return json.load(file)
