from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ElementTree


class Inventory():
    @classmethod
    def is_csv(cls, list):
        result = []
        with open(list, "r") as data:
            reader_csv = csv.DictReader(data, delimiter=",")
            for company in reader_csv:
                result.append(company)
            return result

    @classmethod
    def is_json(cls, list):
        result = []
        with open(list, "r") as data:
            reader_json = json.load(data)
            for company in reader_json:
                result.append(company)
            return result

    @classmethod
    def is_xml(cls, list):
        result = []
        with open(list, "r") as data:
            reader_xml = ElementTree.parse(data).getroot()
            for company in reader_xml:
                objecto = {}
                for company_data in company:
                    objecto[company_data.tag] = company_data.text
                result.append(objecto)
            return result

    @classmethod
    def report_size(cls, report, data):
        if report == "simples":
            return SimpleReport.generate(data)
        if report == "completo":
            return CompleteReport.generate(data)

    @classmethod
    def import_data(cls, list, report):
        if list.endswith(".csv"):
            data = cls.is_csv(list)
        if list.endswith(".json"):
            data = cls.is_json(list)
        if list.endswith(".xml"):
            data = cls.is_xml(list)
        final_result = cls.report_size(report, data)
        return final_result
