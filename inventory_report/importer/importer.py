import abc


class Importer(abc.ABC):
    @abc.abstractmethod
    def import_data(self):
        raise NotImplementedError
