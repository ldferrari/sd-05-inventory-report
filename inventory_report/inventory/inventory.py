import os
import csv
import json
import xml.etree.ElementTree as ET
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        file_path, file_extension = os.path.splitext(path)

        with open(path) as file:
            data = cls.load_file(cls, file_extension, file)

            if report_type == "simples":
                return SimpleReport.generate(data)

            if report_type == "completo":
                return CompleteReport.generate(data)

    @staticmethod
    def load_file(cls, file_extension, file):
        if file_extension == ".csv":
            file_data = csv.DictReader(file)
            data = list(file_data)
        elif file_extension == ".json":
            data = json.load(file)
        elif file_extension == ".xml":
            data = cls.converter_xml(file)
        else:
            data = []
        return data

    @classmethod
    def converter_xml(cls, file):
        tree = ET.parse(file)
        root = tree.getroot().findall("record")

        data = []

        for elem in root:
            dicionario = {}

            for item in elem:
                dicionario[item.tag] = item.text

            data.append(dicionario)

        return data
