import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        try:
            assert path.split('.')[1] == 'xml'
        except AssertionError:
            raise ValueError('Arquivo inválido')
        except FileNotFoundError:
            raise ValueError(f'Arquivo {path} não encontrado')
        else:
            tree = ET.parse(path)
            root = tree.getroot()
            new_list = []
            for record in root.findall("record"):
                assembly = {
                    "id": record.find("id").text,
                    "nome_do_produto": record.find("nome_do_produto").text,
                    "nome_da_empresa": record.find("nome_da_empresa").text,
                    "data_de_fabricacao": record.find("data_de_fabricacao").text,
                    "data_de_validade": record.find("data_de_validade").text,
                    "numero_de_serie": record.find("numero_de_serie").text,
                    "instrucoes_de_armazenamento": record.find(
                      "instrucoes_de_armazenamento"
                    ).text
                }
                new_list.append(assembly)
        return new_list
