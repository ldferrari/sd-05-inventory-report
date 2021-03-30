import csv
import json
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

    @classmethod
    def import_data(self, filepath, report_type):
        if filepath.endswith(".csv"):
            data = self.read_csv(filepath)
        else:
            data = self.read_json(filepath)
        if report_type == "simples":
            report = SimpleReport.generate(data)
        else:
            report = CompleteReport.generate(data)
        return report
