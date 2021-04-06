import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if (len(sys.argv) < 3):
        return sys.stderr.write("Verifique os argumentos\n")

    filepath = sys.argv[1]
    tipo = sys.argv[2]

    if (filepath.endswith(".json")):
        instance = InventoryRefactor(JsonImporter)
    elif (filepath.endswith(".csv")):
        instance = InventoryRefactor(CsvImporter)
    elif (filepath.endswith(".xml")):
        instance = InventoryRefactor(XmlImporter)
    else:
        raise ValueError("Arquivo inválido")

    sys.stdout.write(instance.import_data(filepath, tipo))
    # stdout elimina o \n adicionado ao final

#   http://devfuria.com.br/python/sys-argv/
#   https://stackoverflow.com/questions/493386/how-to-print-without-newline-or-space
