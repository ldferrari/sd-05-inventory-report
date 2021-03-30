from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if ".csv" not in filepath:
            raise ValueError("Arquivo inválido")
            
        try:
            with open(filepath) as file:
                reader = csv.reader(file, delimiter=",")

                header, *data = reader

                stock_Jsoned = [
                    {header[i]: info[i] for i in range(len(info))}
                    for info in data
                ]

                return stock_Jsoned

        except FileNotFoundError:
            raise ValueError(f"Arquivo {filepath} não encontrado")
