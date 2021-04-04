from inventory_report.importer.importer import Importer
import xmltodict
import json


def read_xml_file(filepath):
    try:
        with open(filepath) as file:
            xml = xmltodict.parse(file.read())
            serializa_obj_to_json = json.dumps(xml)
            json_to_pythonobj = json.loads(serializa_obj_to_json)
            return json_to_pythonobj["dataset"]["record"]
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if (not filepath.endswith("xml")):
            raise ValueError("Arquivo inválido")

        return read_xml_file(filepath)


#   https://github.com/martinblech/xmltodict
#   https://docs.python.org/3/library/json.html
