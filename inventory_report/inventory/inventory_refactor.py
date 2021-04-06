from collections.abc import Iterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.inventory_iterator import InventoryInterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryInterator(self.data)

    def import_data(self, path, report_type):
        self.data.extend(self.importer.import_data(path))

        if report_type == 'completo':
            return CompleteReport.generate(self.data)
        return SimpleReport.generate(self.data)
