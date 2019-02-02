from unittest import TestCase
from Mods.Math.Matrix import Matrix
from Mods.Math.Rational_Number import RationalNumber


class TestMatrix(TestCase):
    def test__init__(self):
        m = Matrix([[3, 2], [RationalNumber(1, 2), 3]])

        self.assertEqual(m[[0, 0]], RationalNumber(3))
        self.assertEqual(m[[0, 1]], RationalNumber(2))
        self.assertEqual(m[[1, 0]], RationalNumber(1, 2))
        self.assertEqual(m[[1, 1]], RationalNumber(3))
        self.assertEqual(str(m), '(       3,       2) \n(     1/2,       3) \n')

    def test__operator__(self):
        m1 = Matrix([[3, 2], [RationalNumber(1, 2), 3]])
        m2 = Matrix([[1, 2], [RationalNumber(1, 5), 2]])
        m3 = Matrix([[3, 2], [RationalNumber(1, 2), 3]])

        self.assertEqual(m1+m2, Matrix([[4, 4], [RationalNumber(7, 10), 5]]))
        self.assertEqual(m2*m3, Matrix([
            [4, 8], [RationalNumber(8, 5), RationalNumber(32, 5)]
        ]))
        self.assertEqual(m2*3, Matrix(
            [[3, 6], [RationalNumber(3, 5), 6]]))
