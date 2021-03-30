from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        root = ET.parse(filepath).getroot()
        tree = []

        for branch in root:
            element = {}
            for twig in branch:
                element[twig.tag] = twig.text
            tree.append(element)

        return tree

        # comment out to reduce complexity
        # except FileNotFoundError:
        #     raise ValueError("Arquivo não encontrado")
