import math


class SymmetricGRP:
    def __init__(self, n):
        if isinstance(n, int):
            self.deg = n
            self.index = 0
        else:
            raise TypeError()

    def __len__(self):
        return math.fractorial(self.deg)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self):
            self.index = 0
            raise StopIteration
        l = []
        for i in range(self.deg):
            l.append(i)

