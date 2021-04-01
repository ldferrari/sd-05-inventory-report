import abc


class Importer(abc.ABC):
    def __init__(self):
        @abc.abstractclassmethod
        def import_data(path):
            pass
