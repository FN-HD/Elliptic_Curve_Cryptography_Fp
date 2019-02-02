from unittest import TestCase
from Mods.Math.PolynomialFp import Polynomial


class TestPolynomial(TestCase):
    def test_init(self):
        poly1 = Polynomial({'x^3': 2, 'x^1': 2, 'x': 8, 'x^0': 22})
        poly2 = Polynomial({'x^3': 5, 'y^2': 4, 'x': 1, '1': 4})
        poly3 = Polynomial({'x': 7})
        poly4 = Polynomial({'x^2*y^3': 2, 'x^3*z^2': 2})

        self.assertEqual(poly1, Polynomial({'x^3': 2, 'x^1': 10, '1': 22}))
        self.assertEqual(poly1.get_differential_f('x'), Polynomial({'x^2': 6, '1': 10}))

        self.assertEqual(poly1 + poly2, Polynomial({'x^3': 7, 'x^1': 11, 'y^2': 4, '1': 26}))
        self.assertEqual(poly1 * 3, Polynomial({'x^3': 6, 'x^1': 30, '1': 66}))
        self.assertEqual(poly3 * poly4, Polynomial({'x^3*y^3': 14, 'x^4*z^2': 14}))
