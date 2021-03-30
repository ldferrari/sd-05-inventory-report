from abc import ABC, abstractmethod
# https://docs.python.org/3/library/abc.html#abc.abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(self, pathname):
        raise NotImplementedError
