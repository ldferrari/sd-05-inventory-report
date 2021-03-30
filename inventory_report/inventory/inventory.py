from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, pathname, report_type):
        report = []

        if pathname.endswith(".csv"):
            report = CsvImporter.import_data(pathname)
        elif pathname.endswith(".json"):
            report = JsonImporter.import_data(pathname)
        elif pathname.endswith(".xml"):
            report = XmlImporter.import_data(pathname)

        if report_type == "simples":
            return SimpleReport.generate(report)
        else:
            return CompleteReport.generate(report)
