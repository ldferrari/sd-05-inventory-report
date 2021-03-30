from abc import ABC, abstractmethod


# Pode ser herdada, mas nao instanciada
class Importer(ABC):
    @abstractmethod
    def import_data(self, filepath):
        raise NotImplementedError
        # Levanta um erro se tentar instanciar a classe
