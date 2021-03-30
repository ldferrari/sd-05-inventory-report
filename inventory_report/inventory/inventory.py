from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    # Always use cls for the first argument to class methods.

    @classmethod
    def import_data_csv(self, filepath):
        result_csv = []
        with open(filepath, "r") as file:
            reader_csv = csv.DictReader(file, delimiter=",")
            for row in reader_csv:
                result_csv.append(row)
        return result_csv

    @classmethod
    def import_data_json(self, filepath):
        result_json = []
        with open(filepath, "r") as file:
            reader_json = json.load(file)
            for row in reader_json:
                result_json.append(row)
        return result_json

    @classmethod
    def import_data_xml(self, filepath):
        with open(filepath, "r") as file:
            tree = ET.parse(file)
            root = tree.getroot()
            dicionario = []

            for child in root:
                objeto = {}
                for grandchild in child:
                    objeto[grandchild.tag] = grandchild.text
                dicionario.append(objeto)

        return dicionario

    @classmethod
    def generate_report(self, report, result_tratado):
        if report == "simples":
            return SimpleReport.generate(result_tratado)
        if report == "completo":
            return CompleteReport.generate(result_tratado)

    @classmethod
    def import_data(self, filepath, report):
        # stringCSV = ', '
        result_tratado = ''
        if filepath.endswith(".csv"):
            result_tratado = self.import_data_csv(filepath)
        if filepath.endswith(".json"):
            result_tratado = self.import_data_json(filepath)
        if filepath.endswith(".xml"):
            result_tratado = self.import_data_xml(filepath)

        return self.generate_report(report, result_tratado)
