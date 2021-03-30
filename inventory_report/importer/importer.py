from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(self, filepath):
        raise NotImplementedError

# https://docs.python.org/3/library/abc.html#abc.abstractmethod +gabarito de
# POO da trybe, mas ainda não entendendo essa história direito
