from Mods.Math.Fp import Fp


class FpElement:
    def __init__(self, a=0):
        if Fp.has_instance():
            if isinstance(a, FpElement):
                self.n = a.n
            else:
                self.n = a % Fp.get_instance().p
        else:
            raise TypeError('Fp is undefined')

    def __add__(self, other):
        if isinstance(other, FpElement):
            return FpElement(self.n + other.n)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, FpElement):
            return self.n == other.n

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return FpElement(-self.n)

    def __mul__(self, other):
        if isinstance(other, FpElement):
            return FpElement(self.n * other.n)
        elif isinstance(other, int):
            return FpElement(self.n * other)
        else:
            return NotImplemented

    def __pow__(self, other):
        if not isinstance(other, int):
            print("div")
            return NotImplemented

        ans = FpElement(1)
        if other == 0:
            return ans
        elif other % 2 == 1:
            ans = self

        return ans*((self*self)**(other//2))

    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        if isinstance(other, FpElement):
            if other.n == 0:
                raise TypeError('we cannot divide by 0')
            elif self.n == 0:
                return self
            else:
                return self*(other**(Fp.get_instance().p -2))

    def __str__(self):
        return str(self.n)