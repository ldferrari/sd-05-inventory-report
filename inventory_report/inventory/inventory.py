import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET


def read_json(file):
    with open(file, "r") as file:
        return json.load(file)


def read_csv(file):
    with open(file, "r") as file:
        csv_data = csv.DictReader(file)
        return list(csv_data)

# https://docs.python.org/3/library/xml.etree.elementtree.html


def read_xml(file):
    root = ET.parse(file).getroot()
    tree = []
    for record in root:
        dict_format = {}
        for tag in record:
            dict_format[tag.tag] = tag.text
        tree.append(dict_format)
    print(tree)
    return tree


class Inventory:
    @classmethod
    def import_data(self, filepath, type):
        if filepath.endswith(".csv"):
            data = read_csv(filepath)
        elif filepath.endswith(".json"):
            data = read_json(filepath)
        elif filepath.endswith(".xml"):
            data = read_xml(filepath)
        else:
            raise ValueError("Arquivo inválido")
        if type == 'completo':
            report = CompleteReport.generate(data)
        else:
            report = SimpleReport.generate(data)
        return report
