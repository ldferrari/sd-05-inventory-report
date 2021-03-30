from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        try:
            assert filepath.endswith('.json')
            with open(filepath) as file:
                product_list = json.load(file)
        except AssertionError:
            raise ValueError("Arquivo inválido")
        except FileNotFoundError:
            raise ValueError(f'Arquivo {filepath} não encontrado')
        except OSError:
            raise ValueError("Formato invalido")
        else:
            return product_list
