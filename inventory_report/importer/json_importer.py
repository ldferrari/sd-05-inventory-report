import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        try:
            assert ".json" in filepath
            # assert filepath.endswith(".json"), other option
            with open(filepath, encoding="utf-8") as file:
                json_data = json.load(file)
            return json_data
        except AssertionError:
            raise ValueError("Arquivo inválido")
        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")


if __name__ == "__main__":
    print(JsonImporter.import_data('inventory_report/data/inventory.json'))
    # path passed as argument depends on where you run python currentfile.py

# Difference between json.load & json.loads:
# https://docs.python.org/3/library/json.html
