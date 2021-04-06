import csv
import json
import xml.etree.ElementTree as XML
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data_csv(cls, filepath, type):
        list = []
        with open(filepath, "r") as file:
            read = csv.DictReader(file, delimiter=",")
            for row in read:
                list.append(row)
        return list

    @classmethod
    def import_data_json(cls, filepath, type):
        list = []
        with open(filepath, "r") as file:
            read = json.load(file)
            for row in read:
                list.append(row)
        return list

    @classmethod
    def import_data_xml(cls, filepath, type):
        with open(filepath, "r") as file:
            list = []
            tree = XML.parse(file)
            root = tree.getroot()
            # https://stackabuse.com/reading-and-writing-xml-files-in-python/
            for elem in root:
                node = {}
                for sub_elem in elem:
                    node[sub_elem.tag] = sub_elem.text
                list.append(node)
        return list

    @classmethod
    def generate(self, type, list):
        if type == "simples":
            return SimpleReport.generate(list)
        else:
            return CompleteReport.generate(list)

    @classmethod
    def import_data(self, filepath, type):
        dado_importado = ""

        if filepath.endswith(".csv"):
            dado_importado = (self.import_data_csv(filepath, type))
        if filepath.endswith(".json"):
            dado_importado = (self.import_data_json(filepath, type))
        if filepath.endswith(".xml"):
            dado_importado = (self.import_data_xml(filepath, type))
        return self.generate(type, dado_importado)
