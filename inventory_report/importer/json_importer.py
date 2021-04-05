import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def __init__(self):
        Importer.__init__(self)

    def import_data(path):
        try:
            assert path.endswith('.json')
            with open(path) as file:
                json_content = json.load(file)
        except AssertionError:
            raise ValueError('Arquivo inválido')
        else:
            return json_content