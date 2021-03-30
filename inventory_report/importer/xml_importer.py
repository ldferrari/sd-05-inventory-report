from inventory_report.importer.importer import Importer
import xmltodict
import json


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if ".xml" not in filepath:
            raise ValueError("Arquivo inválido")
        with open(filepath) as file:
            doc = xmltodict.parse(file.read())
            stock_jsoned = json.loads(json.dumps(doc))["dataset"]["record"]
            return stock_jsoned
