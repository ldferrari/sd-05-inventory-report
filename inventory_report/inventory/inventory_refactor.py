from ..inventory.inventory_iterator import InventoryIterator
from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport
from collections.abc import Iterable

Report = {"simples": SimpleReport, "completo": CompleteReport}


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def import_data(self, report, report_type):
        self.data += self.importer.import_data(report)
        return Report[report_type].generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
