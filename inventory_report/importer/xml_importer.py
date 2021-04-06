from .importer import Importer
import xml.etree.ElementTree as xml


class XmlImporter(Importer):

    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        listing = []
        with open(filepath, "r") as file:
            tree = xml.parse(file)
            root = tree.getroot()
            for child in root:
                knot = {}
                for grandchild in child:
                    knot[grandchild.tag] = grandchild.text
                listing.append(knot)
        return listing
