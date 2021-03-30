from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, filepath, type):
        try:
            if filepath.endswith('.csv'):
                with open(filepath) as file:
                    arquivo = csv.DictReader(file, delimiter=',')
                    # print(arquivo)
                    # print("oi eu aqui")
                    product_list = [item for item in arquivo]
                    # print(product_list)
            elif filepath.endswith('.json'):
                with open(filepath) as file:
                    #reader = file.read()
                    product_list = json.load(file)
                    # print(arquivo)
                    # print("oi eu aqui")
                    # print(product_list)
            elif filepath.endswith('.xml'):
                with open(filepath) as file:
                    reader = file.read()
                    arquivo = xmltodict.parse(reader)
                    # print(arquivo['dataset']['record'])
                    arquivo_ordenado = arquivo['dataset']['record']
                    product_list = [item for item in arquivo_ordenado]
                    # print(product_list)
        except FileNotFoundError:
            raise ValueError(f'Arquivo {filepath} não encontrado')
        else:
            if type == "simples":
                return SimpleReport.generate(product_list)
            else:
                return CompleteReport.generate(product_list)

#  https://github.com/martinblech/xmltodict indicação de Kyle!