from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import read_xml


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if file_path.split('.')[1] != 'xml':
            raise ValueError("Arquivo inválido")

        return read_xml(file_path)
