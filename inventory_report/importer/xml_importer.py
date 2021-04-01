from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        root = ET.parse(filepath).getroot()
        tree = []
        for record in root:
            dict_format = {}
            for tag in record:
                dict_format[tag.tag] = tag.text
            tree.append(dict_format)
        print(tree)
        return tree
