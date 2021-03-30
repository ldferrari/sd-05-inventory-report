import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor

# https://docs.python.org/3/library/sys.html#sys.argv
# https://pythonguides.com/python-stderr-stdin-and-stdout/


def main():
    if len(sys.argv) != 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    main, pathname, report_type = sys.argv

    if pathname.endswith(".csv"):
        importer = CsvImporter
    elif pathname.endswith(".json"):
        importer = JsonImporter
    else:
        importer = XmlImporter

    instance = InventoryRefactor(importer)
    requested_report = instance.import_data(pathname, report_type)

    print(requested_report, end="")
