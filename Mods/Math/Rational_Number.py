import math


class RationalNumber:
    def __init__(self, n=0, d=1):
        if isinstance(d, int):
            pass
        elif isinstance(d, RationalNumber):
            n = d.den * n
            d = d.num
        elif isinstance(d, float):
            k = 10 ** 5
            n = n * k
            d = int(d * k)
        else:
            raise TypeError("you input wrong into denominator.")

        if isinstance(n, int):
            pass
        elif isinstance(n, RationalNumber):
            d = n.den * d
            n = n.num
        elif isinstance(n, float):
            n = int(n * 10 ** 5)
            d = d * 10 ** 5
        else:
            raise TypeError("you input wrong integer number")

        if n == 0:
            d = 1

        if d < 0:
            n = -n
            d = -d
        elif d == 0:
            raise TypeError("you input non-zero number into denominator.")

        gcd = math.gcd(abs(n), d)
        self.pair = (n // gcd, d // gcd)

    # if it is in integer,you can get true
    def is_integer(self):
        return self.den == 1

    # The following method is a special method.
    # we can get absolute value.
    def __abs__(self):
        return RationalNumber(abs(self.num), self.den)

    # It is a method for normal addition in Rational Number.
    def __add__(self, other):
        if isinstance(other, RationalNumber):
            return RationalNumber(other.num * self.den + self.num * other.den, other.den * self.den)
        elif isinstance(other, (int, float)):
            return self + RationalNumber(other)
        elif '__radd__' in dir(other):
            return other.__radd__(self)
        return NotImplemented

    # Whether self == other.
    def __eq__(self, other):
        return (self - other).num == 0

    # We can convert self to float.
    def __float__(self):
        return self.num / self.den

    # self >= other
    def __ge__(self, other):
        return self > other or self == other

    # We can get num or den
    def __getattr__(self, attrname):
        if attrname == "numerator" or attrname == "num":
            return self.pair[0]
        elif attrname == 'denominator' or attrname == "den":
            return self.pair[1]
        raise AttributeError(attrname)

    # self > other
    def __gt__(self, other):
        return (self - other).num > 0

    # we can convert self to int.
    def __int__(self):
        return int(float(self))

    # we can get invert self.
    def __invert__(self):
        return RationalNumber(self.den, self.num)

    # self <= other
    def __le__(self, other):
        return not self > other

    # self < other
    def __lt__(self, other):
        return not self >= other

    # It is method for multiplication in rational number.
    def __mul__(self, other):
        if isinstance(other, RationalNumber):
            return RationalNumber(self.num * other.num, self.den * other.den)
        elif isinstance(other, (int, float)):
            return self * RationalNumber(other)
        elif '__rmul__' in dir(other):
            return other.__rmul__(self)
        return NotImplemented

    # -self
    def __ne__(self, other):
        return not self == other

    # self != other
    def __neg__(self):
        return (-1) * self

    # +self
    def __pos__(self):
        return self

    # self ** other
    def __pow__(self, other):
        if isinstance(other, int):
            if other == 1:
                return self
            elif other > 1:
                return (self ** (other - 1)) * self
            elif other == 0:
                return RationalNumber(1, 1)
            else:
                return (1 / self) ** (-other)
        return NotImplemented

    # other + self
    def __radd__(self, other):
        return self + other

    # other == self
    def __req__(self, other):
        return self == other

    # other => self
    def __rge__(self, other):
        return self <= other

    # other > self
    def __rgt__(self, other):
        return self < other

    # other <= self
    def __rle__(self, other):
        return self >= other

    # other < self
    def __rlt__(self, other):
        return self > other

    # other * self
    def __rmul__(self, other):
        return self * other

    # other * self
    def __rsub__(self, other):
        return -(self - other)

    # other / self
    def __rtruediv__(self, other):
        return RationalNumber(other) / self

    # It is a method for string.
    def __str__(self):
        return str(self.num) + (self.den != 1) * ("/" + str(self.den))

    # self - other
    def __sub__(self, other):
        return self + (-other)

    # self/other
    def __truediv__(self, other):
        return self * RationalNumber(1, other)
