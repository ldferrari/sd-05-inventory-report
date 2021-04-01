import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():

    @classmethod
    def edit_csv(cls, list):
        result_csv = []
        with open(list, "r") as date:
            reader_csv = csv.DictReader(date, delimiter=",")
            for company in reader_csv:
                result_csv.append(company)
            return result_csv

    @classmethod
    def import_data(cls, list, report):
        date = cls.edit_csv(list)
        if report == "simples":
            return SimpleReport.generate(date)
        if report == "completo":
            return CompleteReport.generate(date)
