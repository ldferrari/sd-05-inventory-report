from .importer import Importer
import xml.etree.ElementTree as XML


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(filepath, "r") as file:
            list = []
            tree = XML.parse(file)
            root = tree.getroot()
            for elem in root:
                node = {}
                for sub_elem in elem:
                    node[sub_elem.tag] = sub_elem.text
                list.append(node)
        return list
