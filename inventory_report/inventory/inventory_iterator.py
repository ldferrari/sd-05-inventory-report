from collections.abc import Iterator


class InventoryInterator(Iterator):
    elements = []
    current_index = 0

    def __init__(self, el):
        self.elements = el

    def __next__(self):
        try:
            element = self.elements[self.current_index]
        except IndexError:
            raise StopIteration
        else:
            self.current_index += 1
            return element
