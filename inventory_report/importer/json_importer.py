from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import read_json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if file_path.split('.')[1] != 'json':
            raise ValueError("Arquivo inválido")

        return read_json(file_path)
