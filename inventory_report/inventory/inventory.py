import csv
import json
import xml.etree.ElementTree as xml
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data_csv(cls, filepath):
        listing = []
        with open(filepath, "r") as file:
            reading = csv.DictReader(file, delimiter=",")
            for row in reading:
                listing.append(row)
        return listing

    @classmethod
    def import_data_json(cls, filepath):
        listing = []
        with open(filepath, "r") as file:
            reading = json.load(file)
            for row in reading:
                listing.append(row)
        return listing

    @classmethod
    def generate(self, type, listing):
        if type == "simples":
            return SimpleReport.generate(listing)
        else:
            return CompleteReport.generate(listing)

    @classmethod
    def import_data_xml(self, filepath):
        listing = []
        with open(filepath, "r") as file:
            tree = xml.parse(file)
            root = tree.getroot()
            for child in root:
                knot = {}
                for grandchild in child:
                    knot[grandchild.tag] = grandchild.text
                listing.append(knot)
        return listing

    @classmethod
    def import_data(self, filepath, type):
        import_data = ""
        if filepath.endswith(".csv"):
            import_data = self.import_data_csv(filepath)
        if filepath.endswith(".json"):
            import_data = self.import_data_json(filepath)
        if filepath.endswith(".xml"):
            import_data = self.import_data_xml(filepath)
        return self.generate(type, import_data)
