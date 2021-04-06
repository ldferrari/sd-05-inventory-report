from .importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, list):
        if not list.endswith(".json"):
            raise ValueError("Arquivo inválido")
        result = []
        with open(list, "r") as data:
            reader_json = json.load(data)
            for company in reader_json:
                result.append(company)
            return result
