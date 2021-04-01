import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def parse_csv(path):
    with open(path) as file:
        filepath_reader = csv.reader(file, delimiter=",")
        header, *data = filepath_reader
    newArr = []
    for item in data:
        newArr.append(dict(zip(header, item)))
    return newArr


# forma antiga:
# produto = {}
# for inf in item:
# produto.update({header[item.index(inf)]: inf})


def parse_json(path):
    with open(path) as file:
        json_content = json.load(file)
    return json_content


def parse_xml(path):
    with open(path) as file:
        xml_content = xmltodict.parse(file.read())
    new_list = [dict(item) for item in xml_content['dataset']['record']]
    return new_list


def detectar_arquivo(path):
    if path.endswith('.csv'):
        products = parse_csv(path)
    if path.endswith('.json'):
        products = parse_json(path)
    if path.endswith('.xml'):
        products = parse_xml(path)
    return products


class Inventory(CompleteReport):
    def __init__(self):
        CompleteReport.__init__(self)

    def import_data(path, tipo):
        products = detectar_arquivo(path)
        if tipo == "simples":
            return SimpleReport.generate(products)
        if tipo == "completo":
            return CompleteReport.generate(products)

