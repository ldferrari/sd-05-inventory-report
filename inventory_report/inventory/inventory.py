import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data_csv(cls, filepath, type):
        listing = []
        with open(filepath, "r") as file:
            reading = csv.DictReader(file, delimiter=",")
            for row in reading:
                listing.append(row)
        return listing

    @classmethod
    def import_data_json(cls, filepath, type):
        listing = []
        with open(filepath, "r") as file:
            reading = json.load(file)
            for row in reading:
                listing.append(row)
        return listing

    @classmethod
    def generate(self, type, listing):
        if type == "simples":
            return SimpleReport.generate(listing)
        else:
            return CompleteReport.generate(listing)

    @classmethod
    def import_data(self, filepath, type):
        import_data = ""
        if filepath.endswith(".csv"):
            import_data = self.import_data_csv(filepath, type)
        if filepath.endswith(".json"):
            import_data = self.import_data_json(filepath, type)
        return self.generate(type, import_data)

