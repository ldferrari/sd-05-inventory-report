import os
import csv
import json
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):

        file_path, file_extension = os.path.splitext(path)
        print('\nFILE PATH', file_path)
        print('FILE_EXTENSION', file_extension)
        with open(path) as file:
            data = cls.load_file(cls, file_extension, file)

            if report_type == "simples":
                return SimpleReport.generate(data)

            if report_type == "completo":
                return CompleteReport.generate(data)

    @staticmethod
    def load_file(cls, file_extension, file):
        data = []
        if file_extension == ".csv":
            file_data = csv.DictReader(file)
            data = list(file_data)
        if file_extension == ".json":
            data = json.load(file)
        return data
