from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, list):
        if not list.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        result = []
        with open(list, "r") as data:
            reader_xml = ET.parse(data).getroot()
            for company in reader_xml:
                objecto = {}
                for company_data in company:
                    objecto[company_data.tag] = company_data.text
                result.append(objecto)
            return result
