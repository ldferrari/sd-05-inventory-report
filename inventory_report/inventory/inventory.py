import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def read_data_csv(filepath):
    with open(filepath) as file:
        csv_data = csv.DictReader(file)
        return list(csv_data)


def read_data_json(filepath):
    with open(filepath) as file:
        return json.load(file)


class Inventory:
    @classmethod
    def import_data(self, test, type):
        if test.endswith(".csv"):
            data = read_data_csv(test)
        if test.endswith(".json"):
            data = read_data_json(test)
        if type == 'completo':
            report = CompleteReport.generate(data)
        else:
            report = SimpleReport.generate(data)
        return report
