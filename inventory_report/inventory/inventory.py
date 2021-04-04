from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, filepath, tipo):
        if (filepath.endswith("csv")):
            lista = CsvImporter.import_data(filepath)
        if (filepath.endswith("json")):
            lista = JsonImporter.import_data(filepath)
        if (filepath.endswith("xml")):
            lista = XmlImporter.import_data(filepath)

        if (tipo == "simples"):
            return SimpleReport.generate(lista)

        return CompleteReport.generate(lista)
