class Memento:
    def __init__(self, cof):
        if isinstance(cof, list):
            self.a = cof[2]
            self.b = cof[1]
            self.c = cof[0]

    def __add__(self, other):
        if isinstance(other, Memento):
            return Memento([
                (self[0] + other[0]) / 2,
                (self[1] + other[1]) / 2,
                (self[2] + other[2]) / 2
            ])

    def __getattr__(self, item):
        if item == 'a':
            return self.a
        elif item == 'b':
            return self.b
        elif item == 'c':
            return self.c
        else:
            raise AttributeError(item)
