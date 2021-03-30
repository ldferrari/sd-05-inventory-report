import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        try:
            assert ".csv" in filepath
            # assert filepath.endswith(".csv"), other option
            with open(filepath) as file:
                csv_reader = csv.DictReader(file, delimiter=",")
                print(f"csv_reader: {csv_reader}")
                # returns csv_reader: <csv.DictReader object at 0x7fe35e434f70>
                csv_data = []
                for product in csv_reader:
                    csv_data.append(product)
                return csv_data
        except AssertionError:
            raise ValueError("Formato invalido")
        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")


if __name__ == "__main__":
    print(CsvImporter.import_data('inventory_report/data/inventory.csv'))

# from own former project csv example:
# https://github.com/tryber/sd-05-tech-news/pull/10/files
