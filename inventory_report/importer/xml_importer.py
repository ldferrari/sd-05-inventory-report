# import xml
import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        # no try except structure because of flake complexity error
        if not filepath.endswith(".xml"):
            raise ValueError("Formato invalido")
        tree = ET.parse(filepath)
        root = tree.getroot()
        # print(f"root: {root}")
        # root: <Element 'dataset' at 0x7ff34e4d9d60>
        xml_data = []
        for element in root:
            each_product = {}
            for item in element:
                each_product[item.tag] = item.text
            # print(f"each_product: {each_product}")
            xml_data.append(each_product)
        return xml_data
        # except FileNotFoundError:
        #     raise ValueError("Arquivo não encontrado")


if __name__ == "__main__":
    print(XmlImporter.import_data('inventory_report/data/inventory.xml'))

# https://stackabuse.com/reading-and-writing-xml-files-in-python/
# https://docs.python.org/3/library/xml.etree.elementtree.html
# other possibility: xmltodict https://docs.python-guide.org/scenarios/xml/
