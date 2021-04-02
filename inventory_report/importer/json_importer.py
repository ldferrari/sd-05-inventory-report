from .importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, list):
        if not list.endswith(".json"):
            raise ValueError("Arquivo inválido")
        result_json = []
        with open(list, "r") as date:
            reader_json = json.load(date)
            for company in reader_json:
                result_json.append(company)
            return result_json
