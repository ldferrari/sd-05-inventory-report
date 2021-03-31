import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):

    @classmethod
    def import_data(self, path):
        try:
            assert path.split('.')[1] == 'json'
        except AssertionError:
            raise ValueError('Arquivo inválido')
        except FileNotFoundError:
            raise ValueError(f'Arquivo {path} não encontrado')
        else:
            with open(path) as file:
                content = file.read()
                new_list = json.loads(content)
                return new_list
