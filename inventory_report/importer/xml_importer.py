from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(filepath, "r") as file:
            tree = ET.parse(file)
            root = tree.getroot()
            dicionario = []

            for child in root:
                objeto = {}
                for grandchild in child:
                    objeto[grandchild.tag] = grandchild.text
                dicionario.append(objeto)

        return dicionario

# up
