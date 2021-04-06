import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, filepath, type):
        listing = []
        with open(filepath, "r") as file:
            reading = csv.DictReader(file, delimiter=",")
            for row in reading:
                listing.append(row)

        if type == "simples":
            return SimpleReport.generate(listing)
        else:
            return CompleteReport.generate(listing)
