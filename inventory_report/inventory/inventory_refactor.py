from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, aggregate):
        self.estoque = []
        self.aggregate = aggregate

    def __iter__(self):
        return InventoryIterator(self.estoque)

    def import_data(self, filepath, tipo):
        self.estoque += self.aggregate.import_data(filepath)

        if (tipo == "simples"):
            return SimpleReport.generate(self.estoque)

        return CompleteReport.generate(self.estoque)

#   https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration
#   https://docs.python.org/3/library/collections.abc.html
#   https://medium.com/design-patterns-in-python/iterator-design-pattern-54655e97552c
