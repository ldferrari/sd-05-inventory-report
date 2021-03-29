from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(self, filepath):
        raise NotImplementedError

# follow examples of where to find model synthax
# https://app.betrybe.com/course/computer-science/poo/oo-na-pratica/solutions
# https://docs.python.org/3/library/abc.html
