from inventory_report.importer.importer import Importer
import csv


def read_csv_file(filepath):
    saida = []
    try:
        with open(filepath) as file:
            inventario = csv.DictReader(file, delimiter=",")
            for linha in inventario:
                result = {}
                for key in linha:
                    result[key] = linha[key]
                saida.append(result)
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    return saida


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if (not filepath.endswith("csv")):
            raise ValueError("Arquivo inválido")

        return read_csv_file(filepath)

#   https://stackoverflow.com/questions/14091387/creating-a-dictionary-from-a-csv-file
