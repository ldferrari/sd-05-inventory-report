from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iteravel):
        self.iteravel = iteravel
        self.posicao = 0

    def __next__(self):
        try:
            valor_atual = self.iteravel[self.posicao]
        except IndexError:
            raise StopIteration()
        else:
            self.posicao += 1
            return valor_atual

#   https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration
#   https://docs.python.org/3/library/collections.abc.html
