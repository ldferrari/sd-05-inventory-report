import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        try:
            assert filepath.endswith(".xml")
        except AssertionError:
            raise ValueError("Arquivo inválido")
        else:
            tree = ET.parse(filepath)
            root = tree.getroot()
            data = []
            for record in root:
                product = {}
                for tag in record:
                    product[tag.tag] = tag.text
                data.append(product)
            return data
