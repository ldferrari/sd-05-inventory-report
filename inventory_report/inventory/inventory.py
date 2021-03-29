import os
import csv
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        with open(path) as file:
            data = cls.load_file(file)

            if report_type == "simples":
                return SimpleReport.generate(data)

            if report_type == "completo":
                return CompleteReport.generate(data)

    @staticmethod
    def load_file(file):
        data = csv.DictReader(file)
        data_list = list(data)

        return data_list
