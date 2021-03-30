from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        try:
            assert filepath.endswith(".xml")
            with open(filepath) as file:
                reader = file.read()
                arquivo = xmltodict.parse(reader)
                # print(arquivo['dataset']['record'])
                arquivo_ordenado = arquivo["dataset"]["record"]
                product_list = [item for item in arquivo_ordenado]
                # print(product_list)
        except AssertionError:
            raise ValueError("Arquivo inválido")
        except FileNotFoundError:
            raise ValueError(f"Arquivo {filepath} não encontrado")
        except OSError:
            raise ValueError("Formato invalido")
        else:
            return product_list


#  https://github.com/martinblech/xmltodict indicação de Kyle!
