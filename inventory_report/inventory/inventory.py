import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def read_csv(file_path):
    try:
        with open(file_path, 'r') as products:
            ler = csv.reader(products, delimiter=',')
            header, *data = ler
    except FileNotFoundError:
        raise ValueError("File not found")
    else:
        output = []
        lista = {}
        for line in data:
            for index, value in enumerate(header):
                lista[value] = line[index]
            output.append(lista)
            lista = {}
        return output


def read_json(file_path):
    try:
        with open(file_path) as file:
            return json.load(file)
    except FileNotFoundError:
        raise ValueError("File not found")


def read_xml(file_path):
    try:
        with open(file_path) as file:
            ler = xmltodict.parse(file.read())
            print(type(json.dumps(ler)))
            data = json.loads(json.dumps(ler))['dataset']['record']
            return data
    except FileNotFoundError:
        raise ValueError("File not found")


def create_report(file_path):
    if file_path.split('.')[1] == 'csv':
        report = read_csv(file_path)
        return report
    if file_path.split('.')[1] == 'json':
        report = read_json(file_path)
        return report
    if file_path.split('.')[1] == 'xml':
        report = read_xml(file_path)
        return report

class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        report = create_data(file_path)

        if (report_type == "simples"):
            return SimpleReport.generate(report)

        if (report_type == "completo"):
            return CompleteReport.generate(report)
