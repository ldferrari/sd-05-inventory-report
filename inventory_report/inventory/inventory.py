from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

class Inventory:

    # Criar uma function que recebe o tipo e formato do relatorio
    # A função vai escolher qual método vai usar para "puxar" a lista
    # A função vai "tratar" a lista usando o SimpleReport ou o CompleteReport

    @classmethod
    def import_data(self, path, report_type):
        if path.split('.')[1] == 'csv':
            new_list = CsvImporter.import_data(path)
        elif path.split('.')[1] == 'xml':
            new_list = XmlImporter.import_data(path)
        elif path.split('.')[1] == 'json':
            new_list = JsonImporter.import_data(path)

        if report_type == 'completo':
            return CompleteReport.generate(new_list)
        return SimpleReport.generate(new_list)
