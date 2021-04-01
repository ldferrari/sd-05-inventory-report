from abc import ABC


class Importer(ABC):
    @classmethod
    def importer_data(self, filepath):
        pass
    