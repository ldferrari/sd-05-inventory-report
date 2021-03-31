from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import read_csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if file_path.split('.')[1] != 'csv':
            raise ValueError("Arquivo inválido")

        return read_csv(file_path)
