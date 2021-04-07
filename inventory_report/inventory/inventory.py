import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():

    @classmethod
    def edit_csv(cls, list):
        result_csv = []
        with open(list, "r") as data:
            reader_csv = csv.DictReader(data, delimiter=",")
            for company in reader_csv:
                result_csv.append(company)
            return result_csv

    @classmethod
    def edit_json(cls, list):
        result_json = []
        with open(list, "r") as data:
            reader_json = json.load(data)
            for company in reader_json:
                result_json.append(company)
            return result_json

    @classmethod
    def edit_xml(cls, list):
        result_xml = []
        with open(list, "r") as data:
            reader_xml = ET.parse(data).getroot()
            for company in reader_xml:
                objecto = {}
                for company_data in company:
                    objecto[company_data.tag] = company_data.text
                result_xml.append(objecto)
            return result_xml

    @classmethod
    def report_size(cls, report, data):
        if report == "simples":
            return SimpleReport.generate(data)
        if report == "completo":
            return CompleteReport.generate(data)

    @classmethod
    def import_data(cls, list, report):
        if list.endswith(".csv"):
            data = cls.edit_csv(list)
        if list.endswith(".json"):
            data = cls.edit_json(list)
        if list.endswith(".xml"):
            data = cls.edit_xml(list)
        final_result = cls.report_size(report, data)
        print(final_result)
        return final_result
