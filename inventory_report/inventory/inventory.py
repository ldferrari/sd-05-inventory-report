import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def read_json(file):
    with open(file, "r") as file:
        return json.load(file)


def read_csv(file):
    with open(file, "r") as file:
        csv_data = csv.DictReader(file)
        return list(csv_data)


class Inventory:
    @classmethod
    def import_data(self, filepath, type):
        if filepath.endswith(".csv"):
            data = read_csv(filepath)
        if filepath.endswith(".json"):
            data = read_json(filepath)
        if type == 'completo':
            report = CompleteReport.generate(data)
        else:
            report = SimpleReport.generate(data)
        return report
