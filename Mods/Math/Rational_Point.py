from Mods.Math.Rational_Number import RationalNumber
from Mods.Math.Matrix import Matrix


class RationalPoint(Matrix):
    def __init__(self, comps):
        if isinstance(comps, list):
            super().__init__([[comp] for comp in comps])
        elif isinstance(comps, (int, float, RationalNumber)):
            super().__init__([[comps]])
        else:
            raise TypeError('you input wrong')

    def __getitem__(self, item):
        if isinstance(item, int):
            if 0 <= item < len(self):
                return self[[item, 0]]
            raise TypeError('out of list')
        else:
            return super().__getitem__(item)

    def __iter__(self):
        return RationalPointIter(self)

    def __mul__(self, other):
        if isinstance(other, RationalPoint):
            if len(self) != len(other):
                raise TypeError('you can not do bracket')
            return sum([comp + other[i] for i, comp in enumerate(self)])
        else:
            return super().__mul__(other)

    def __len__(self, other):
        return self.row_size


class RationalPointIter:
    def __init__(self,point):
        self.index = 0
        self.term = point.args

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.term):
            raise StopIteration
        v = self.term[self.index][0]
        self.index += 1
        return v
