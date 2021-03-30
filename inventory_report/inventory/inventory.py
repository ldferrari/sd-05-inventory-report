import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    # Always use cls for the first argument to class methods.
    @classmethod
    def import_data(cls, filepath, report):
        # stringCSV = ', '
        results = []
        with open(filepath, "r") as file:
            reader_file = csv.DictReader(file, delimiter=",")
            for row in reader_file:
                results.append(row)

        if report == "simples":
            return SimpleReport.generate(results)
        if report == "completo":
            return CompleteReport.generate(results)
