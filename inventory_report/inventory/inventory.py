from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, filepath, type):
        try:
            assert filepath.endswith('.csv')
            with open(filepath) as file:
                arquivo = csv.DictReader(file, delimiter=',')
                # print(arquivo)
                # print("oi eu aqui")
                product_list = [item for item in arquivo]
                # print(product_list)
        except AssertionError:
            raise ValueError("Formato invalido")
        except FileNotFoundError:
            raise ValueError(f'Arquivo {filepath} não encontrado')
        else:
            if type == "simples":
                return SimpleReport.generate(product_list)
            else:
                return CompleteReport.generate(product_list)
