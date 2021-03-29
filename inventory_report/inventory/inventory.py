from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


def get_csv_stock(path):
    try:
        with open(path) as file:
            reader = csv.reader(file, delimiter=",")

            header, *data = reader

            stock_Jsoned = [
                {header[i]: info[i] for i in range(len(info))} for info in data
            ]

            return stock_Jsoned

    except FileNotFoundError:
        raise ValueError(f"Arquivo {path} não encontrado")


def get_json_stock(path):
    with open(path) as file:
        return json.load(file)


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):

        if ".csv" in path:
            stock = get_csv_stock(path)
        if ".json" in path:
            stock = get_json_stock(path)

        if report_type == "simples":
            report = SimpleReport.generate(stock)
        else:
            report = CompleteReport.generate(stock)

        return report
