from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath):

        if (not filepath.endswith("json")):
            raise ValueError("Arquivo inválido")

        try:
            with open(filepath) as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError(f"Arquivo {filepath} não encontrado")
