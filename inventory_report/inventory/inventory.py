from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, filepath, type):
        product_list = []
        if filepath.endswith(".csv"):
            product_list = CsvImporter.import_data(filepath)
        elif filepath.endswith(".json"):
            product_list = JsonImporter.import_data(filepath)
        elif filepath.endswith(".xml"):
            product_list = XmlImporter.import_data(filepath)

        if type == "simples":
            return SimpleReport.generate(product_list)
        else:
            return CompleteReport.generate(product_list)
