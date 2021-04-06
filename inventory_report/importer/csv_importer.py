from .importer import Importer
import csv


class CsvImporter(Importer):

    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        listing = []
        with open(filepath, "r") as file:
            reading = csv.DictReader(file, delimiter=",")
            for row in reading:
                listing.append(row)
        return listing
