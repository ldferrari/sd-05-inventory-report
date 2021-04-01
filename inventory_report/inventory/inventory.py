import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def parse_csv(path):
    with open(path) as file:
        filepath_reader = csv.reader(file, delimiter=",")
        header, *data = filepath_reader
    newArr = []
    for item in data:
        produto = {}
        for inf in item:
            produto.update({header[item.index(inf)]: inf})
        newArr.append(produto)
    return newArr


class Inventory(CompleteReport):
    def __init__(self):
        CompleteReport.__init__(self)

    def import_data(path, tipo):
        products = parse_csv(path)
        if tipo == "simples":
            return SimpleReport.generate(products)
        if tipo == "completo":
            return CompleteReport.generate(products)
