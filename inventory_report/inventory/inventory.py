from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
# Tip: make req 6 and then reqs 3 4 5 together


def data_by_format(path):
    if path.endswith(".json"):
        return JsonImporter.import_data(path)
    elif path.endswith(".csv"):
        return CsvImporter.import_data(path)
    elif path.endswith(".xml"):
        return XmlImporter.import_data(path)


class Inventory:

    @classmethod
    def import_data(cls, filepath, report_type):
        # 1/ first import according to file format
        data = data_by_format(filepath)
        # 2/ then generate report according to report type
        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)


# if __name__ == "__main__":
#     print(Inventory.import_data('./data/inventory.json', 'simple'))
#     print(Inventory.import_data('./data/inventory.json', 'complete'))
#     print(Inventory.import_data('./data/inventory.csv', 'simple'))
#     print(Inventory.import_data('./data/inventory.csv', 'complete'))
#     print(Inventory.import_data('./data/inventory.xml', 'simple'))
#     print(Inventory.import_data('./data/inventory.xml', 'complete'))

# Academic honesty: the following PR made me realize the empty files
# that were made available so we write each format importer in them:
# https://github.com/tryber/sd-04-inventory-report/pull/16/files

# Also checked my understanding that it was better to start with req6
# with https://github.com/tryber/sd-05-inventory-report/pull/5/commits
