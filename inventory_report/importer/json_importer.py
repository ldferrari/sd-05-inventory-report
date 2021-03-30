from .importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".json"):
            raise ValueError("Arquivo inválido")
        result_json = []
        with open(filepath, "r") as file:
            reader_json = json.load(file)
            for row in reader_json:
                result_json.append(row)
        return result_json
