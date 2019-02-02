from Mods.Math.Rational_Number import RationalNumber


class Matrix:
    def __init__(self, args):
        if not isinstance(args, (list, tuple)):
            raise TypeError('args is not list')

        self.args = []

        for i, row in enumerate(args):
            if not isinstance(row, (list, tuple)):
                raise TypeError('Row' + str(i) + 'is not list.')

            if len(row) != len(args[0]):
                raise TypeError('Row' + str(i) + 'is failed.')

            s_row = []

            for comp in row:
                if isinstance(comp, type(args[0][0])):
                    s_row.append(comp)
                elif isinstance(comp, (int, RationalNumber, float)):
                    s_row.append(RationalNumber(comp))
                else:
                    raise TypeError('component in row '+str(i)+'is failed.')

            self.args.append(tuple(s_row))

        self.args = tuple(self.args)

    def __add__(self, other):
        if isinstance(other, Matrix):
            if other.size != self.size:
                raise TypeError('both size are not same.')
            return Matrix([
                [comp + other[i][j] for j, comp in enumerate(row)]for i, row in enumerate(self)
            ])
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.args == other.args
        else:
            raise TypeError('you input no matrix.')

    def __iter__(self):
        return MatrixIter(self)

    def __getattr__(self, item):
        if item == 'row_size':
            return len(self.args)
        elif item == 'clm_size':
            return len(self.args[0])
        elif item == 'size':
            return [self.row_size, self.clm_size]
        else:
            raise AttributeError(item)

    def __getitem__(self, item):
        if isinstance(item, list):
            return (self.args[item[0]])[item[1]]
        elif isinstance(item, int):
            return self.args[item]
        else:
            raise AttributeError(item)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.clm_size != other.row_size:
                raise TypeError('we can not do multication')
            args = []
            for i in range(self.row_size):
                args.append([])
                for j in range(other.clm_size):
                    args[i].append(0)
                    for k in range(self.clm_size):
                        args[i][j] += (self[i][k])*(other[k][j])

            return Matrix(args)
        elif isinstance(other, type(self.args[0][0])):
            return Matrix([[comp * other for comp in row] for row in self])
        elif isinstance(other, (int, RationalNumber, float)):
            return Matrix([
                [comp * RationalNumber(other) for comp in row] for row in self
            ])
        else:
            return NotImplemented

    def __str__(self):
        matrix_str = ''

        for row in self:
            matrix_str += '('+','.join(
                [' '*(8-len(str(comp)))+str(comp) for comp in row]
            ) + ') \n'

        return matrix_str


class MatrixIter:
    def __init__(self, matrix):
        self.index = 0
        self.terms = matrix.args

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.terms):
            raise StopIteration
        v = list(self.terms[self.index])
        self.index += 1
        return v
