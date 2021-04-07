from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, filepath, tipo):
        self.data.extend(self.importer.import_data(filepath))

        if (tipo == "simples"):
            return SimpleReport.generate(self.data)

        return CompleteReport.generate(self.data)

#   https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration
#   https://docs.python.org/3/library/collections.abc.html
#   https://medium.com/design-patterns-in-python/iterator-design-pattern-54655e97552c
