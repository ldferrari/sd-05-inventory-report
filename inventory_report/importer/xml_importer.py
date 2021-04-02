from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, list):
        if not list.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        result_xml = []
        with open(list, "r") as date:
            reader_xml = ET.parse(date).getroot()
            for company in reader_xml:
                objecto = {}
                for company_date in company:
                    objecto[company_date.tag] = company_date.text
                result_xml.append(objecto)
            return result_xml
