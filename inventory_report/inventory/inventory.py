from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, filepath, type):
        try:
            if filepath.endswith(".csv"):
                with open(filepath) as file:
                    arquivo = csv.DictReader(file, delimiter=",")
                    product_list = [item for item in arquivo]
                    print(arquivo)
            elif filepath.endswith(".json"):
                with open(filepath) as file:
                    # reader = file.read()
                    product_list = json.load(file)
            elif filepath.endswith(".xml"):
                with open(filepath) as file:
                    arquivo = xmltodict.parse(file.read())
                    arquivo_ordenado = arquivo["dataset"]["record"]
                    product_list = [item for item in arquivo_ordenado]
        except AssertionError:
            raise ValueError("Formato invalido")
        except FileNotFoundError:
            raise ValueError(f"Arquivo {filepath} não encontrado")
        else:
            if type == "simples":
                return SimpleReport.generate(product_list)
            else:
                return CompleteReport.generate(product_list)
