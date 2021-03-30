from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        try:
            if not filepath.endswith(".json"):
                raise ValueError("Arquivo inválido")
            with open(filepath) as file:
                reader = file.read()
                json_file = json.loads(reader)

                return json_file

        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")
