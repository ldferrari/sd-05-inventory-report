from collections.abc import Iterator
# https://www.geeksforgeeks.org/iterators-in-python/


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        try:
            info = self.data[self.index]
        except IndexError:
            raise StopIteration()
        else:
            self.index += 1
            return info
