# import xml
import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        tree = ET.parse(filepath)
        root = tree.getroot()
        print(f"root: {root}")
        xml_data = []
        # some iteration
        return xml_data
        # except FileNotFoundError:
        #     raise ValueError("Arquivo não encontrado")


if __name__ == "__main__":
    print(XmlImporter.import_data('inventory_report/data/inventory.csv'))

# https://stackabuse.com/reading-and-writing-xml-files-in-python/
# https://docs.python.org/3/library/xml.etree.elementtree.html
