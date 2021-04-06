from .importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".json"):
            raise ValueError("Arquivo inválido")
        list = []
        with open(filepath, "r") as file:
            read = json.load(file)
            for row in read:
                list.append(row)
        return list
