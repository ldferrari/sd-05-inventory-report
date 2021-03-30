from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        try:
            assert filepath.endswith('.csv')
            with open(filepath) as file:
                arquivo = csv.DictReader(file, delimiter=',')
                # print(arquivo)
                # print("oi eu aqui")
                product_list = [item for item in arquivo]
        except AssertionError:
            raise ValueError("Arquivo inválido")
        except FileNotFoundError:
            raise ValueError(f'Arquivo {filepath} não encontrado')
        except OSError:
            raise ValueError("Formato invalido")
        else:
            return product_list
