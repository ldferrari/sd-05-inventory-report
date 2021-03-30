# Referência
# https://docs.python.org/3/library/xml.etree.elementtree.html

import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def read_csv(filepath):
        with open(filepath, "r") as file:
            data = csv.DictReader(file)
            return list(data)

    def read_json(filepath):
        with open(filepath, "r") as file:
            data = json.load(file)
            return data

    def read_xml(filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()
        data = []
        for record in root:
            product = {}
            for tag in record:
                product[tag.tag] = tag.text
            data.append(product)
        return data

    @classmethod
    def import_data(self, filepath, report_type):
        if filepath.endswith(".csv"):
            data = self.read_csv(filepath)
        elif filepath.endswith(".xml"):
            data = self.read_xml(filepath)
        else:
            data = self.read_json(filepath)
        if report_type == "simples":
            report = SimpleReport.generate(data)
        else:
            report = CompleteReport.generate(data)
        return report
