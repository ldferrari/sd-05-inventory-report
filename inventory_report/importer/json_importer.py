import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        try:
            assert filepath.endswith(".json")
        except AssertionError:
            raise ValueError("Arquivo inválido")
        else:
            with open(filepath, "r") as file:
                return json.load(file)
