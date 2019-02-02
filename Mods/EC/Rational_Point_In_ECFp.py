from Mods.Math.Fp_Element import FpElement
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve


class RationalPointInEC:
    def __init__(self, x0=0, x1=None):
        ec = None

        if EllipticCurve.has_instance():
            ec = EllipticCurve.get_instance()
            self.ec = ec
        else:
            raise TypeError('EC does not exist')

        if x0 is None or x1 is None:
            # pair = (0, None) is a point at infinity.
            # because the point at infinity in elliptic curve is x = 0. (x^3=0)
            x0 = FpElement(0)
            x1 = None
        else:
            x0 = FpElement(x0)
            x1 = FpElement(x1)

        if ec.includes(x0, x1) or x1 is None:
            self.pair = (x0, x1)
        else:
            raise TypeError('EC does not have this point')

    # We can get slope of self and other.
    def get_slope(self, other):
        if isinstance(other, RationalPointInEC):
            d = FpElement(0)

            if self == other:
                # if self == other, they are in the same ec
                for a in self.ec.get_differential_f('x'):
                    if a[0] == '1':
                        d += a[1]
                        continue

                    d += a[1] * (self.x ** int(a[0].split('^')[1]))
                d = d / (2 * self.y)
            else:
                d = (self.y - other.y) / (self.x - other.x)

            return d
        else:
            return NotImplemented

    # boolean method
    # Whether self is a point at infinity.
    def is_a_point_at_infinity(self):
        return self.y is None

    def is_in_the_EC(self):
        return self.ec == EllipticCurve.get_instance()

    # Special method.
    # It is a method for addition.
    def __add__(self, other):
        if isinstance(other, RationalPointInEC):
            if self.is_a_point_at_infinity():
                return other
            elif other.is_a_point_at_infinity():
                return self
            return -(self*other)
        else:
            return NotImplemented

    # It is a method for equivalent.
    def __eq__(self, other):
        if isinstance(other, RationalPointInEC):
            if self.is_in_the_EC() and other.is_in_the_EC():
                pass
            else:
                raise TypeError('Now point is not in ec')

            if self.is_a_point_at_infinity():
                return other.is_a_point_at_infinity()
            else:
                return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    # It is a method for item.
    def __getattr__(self, item):
        if item == 'x':
            return self.pair[0]
        elif item == 'y':
            return self.pair[1]
        else:
            raise AttributeError(item)

    # It is a method for inverse of addition.
    def __neg__(self):
        if self.is_a_point_at_infinity():
            return self
        else:
            return RationalPointInEC(self.x, -self.y)

    # It is a method for int mul or to get cross point
    def __mul__(self, other):
        if isinstance(other, RationalPointInEC):
            return self.__mul_with_point(other)
        elif isinstance(other, int):
            return self.__mul_with_int(other)
        else:
            return NotImplemented

    # It is a method for commutative mul.
    def __rmul__(self, other):
        return self*other

    # It is a method for subtraction.
    def __sub__(self, other):
        return self + (other.__neg__())

    # It is a method for string.
    def __str__(self):
        if self.is_a_point_at_infinity():
            return 'O'
        else:
            return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # The following method is a method for special method.
    # It is a method for getting cross point of ec and line, which has self and other.
    def __mul_with_point(self, other):
        if not isinstance(other, RationalPointInEC):
            return NotImplemented

        if self.is_in_the_EC() and other.is_in_the_EC():
            pass
        else:
            raise TypeError('Now point is not in ec')

        if self.is_a_point_at_infinity():
            return other
        elif other.is_a_point_at_infinity():
            return self
        elif self == -other:
            return RationalPointInEC()

        d = self.get_slope(other)
        x = -self.x-other.x-(self.ec[2]-d**2)/self.ec[3]
        y = d*(x-self.x)+self.y

        return RationalPointInEC(x, y)

    # It is a method for mul with integer.
    def __mul_with_int(self, other):
        if not isinstance(other, int):
            return NotImplemented

        ans = RationalPointInEC()
        if other == 0:
            return ans
        elif other == 1:
            return self
        elif other % 2 == 1:
            ans = self

        return ans + (self+self)*(other//2)

#        if other > 1:
#            return self * (other - 1) + self
#        elif other == 1:
#            return self
#        elif other == 0:
#            return self - self
#        else:
#            return -(self * (-other))
