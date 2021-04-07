from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, interable):
        self._interable = interable
        self._position = 0

    def __next__(self):
        try:
            value_data = self._interable[self._position]
        except IndexError:
            raise ValueError("Arquivo inválido")
        else:
            self._position += 1
            return value_data
