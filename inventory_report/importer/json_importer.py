from .importer import Importer
import json


class JsonImporter(Importer):

    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".json"):
            raise ValueError("Arquivo inválido")
        listing = []
        with open(filepath, "r") as file:
            reading = json.load(file)
            for row in reading:
                listing.append(row)
        return listing
