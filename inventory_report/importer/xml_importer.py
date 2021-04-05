import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def __init__(self):
        Importer.__init__(self)

    def import_data(path):
        try:
            assert path.endswith('.xml')
            with open(path) as file:
                xml_cont = xmltodict.parse(file.read())
        except AssertionError:
            raise ValueError('Arquivo inválido')
        else:
            new_list = [dict(item) for item in xml_cont['dataset']['record']]
            return new_list
