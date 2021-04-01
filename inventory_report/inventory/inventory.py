import csv
import json
import xml.etree.ElementTree as ET
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
    def edit_json(cls, list):
        result_json = []
        with open(list, "r") as date:
            reader_json = json.load(date)
            for company in reader_json:
                result_json.append(company)
            return result_json

    @classmethod
    def import_data(cls, list, report):
        if list.endswith(".csv"):
            date = cls.edit_csv(list)
        if list.endswith(".json"):
            date = cls.edit_json(list)
        if report == "simples":
            return SimpleReport.generate(date)
        if report == "completo":
            return CompleteReport.generate(date)
