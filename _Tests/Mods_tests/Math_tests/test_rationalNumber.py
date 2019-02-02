from unittest import TestCase
from Mods.Math.Rational_Number import RationalNumber


class TestRationalNumber(TestCase):
    def test_init(self):
        values = (
            (1, 2, 1, 2),
            (1, 1, 1, 1),
            (1, -3, -1, 3),
            (RationalNumber(3, 1), RationalNumber(2, 9), 27, 2),
            (0.005, 5, 1, 1000),
            (0.00000005, 1, 0, 1)
        )
        for v in values:
            r = RationalNumber(v[0], v[1])
            self.assertEqual(r.num, v[2])
            self.assertEqual(r.den, v[3])

    def test_init_error(self):
        with self.assertRaises(TypeError):
            RationalNumber(1, 0.000005)
        with self.assertRaises(TypeError):
            RationalNumber(1, 0)

    def test_abs(self):
        r0 = RationalNumber(-1, 2)
        r1 = RationalNumber(3, 6)
        r2 = RationalNumber(1, 2)

        self.assertEqual(abs(r0), r1)
        self.assertEqual(abs(r2), r1)

    def test_add(self):
        values = (
            (RationalNumber(1, 2), RationalNumber(1, 3), RationalNumber(5, 6)),
            (RationalNumber(1, 2), 1, RationalNumber(3, 2)),
            (1, RationalNumber(1, 3), RationalNumber(4, 3)),
            (RationalNumber(1, 2), 0.5, 1),
            (1.5, RationalNumber(1, 3), RationalNumber(11, 6)),
            (RationalNumber(1, 6), RationalNumber(5, 6), 1),
            (RationalNumber(1, 6), RationalNumber(-1, 6), 0)
        )

        for v in values:
            r = v[0] + v[1]
            self.assertEqual(r, v[2])

    def test_convertion(self):
        r0 = RationalNumber(3, 1)
        r1 = RationalNumber(1, 2)

        self.assertEqual(int(r0), 3)
        self.assertEqual(float(r1), 0.5)

    def test_div(self):
        values = (
            (RationalNumber(1, 2), RationalNumber(1, 3), RationalNumber(3, 2)),
            (RationalNumber(1, 2), 2, RationalNumber(1, 4)),
            (6, RationalNumber(1, 3), 18),
            (RationalNumber(1, 2), 2.5, RationalNumber(1, 5)),
            (0.4, RationalNumber(1, 3), RationalNumber(12, 10)),
            (RationalNumber(1, 6), RationalNumber(-1, 3), RationalNumber(-1, 2)),
            (RationalNumber(0, 6), RationalNumber(1, 1), 0)
        )

        for v in values:
            r = v[0] / v[1]
            self.assertEqual(r, v[2])

    def test_is_integer(self):
        r0 = RationalNumber(1, 2)
        r1 = RationalNumber(3, 3)

        self.assertFalse(r0.is_integer())
        self.assertTrue(r1.is_integer())

    def test_neg(self):
        values = (
            (RationalNumber(1, 2), RationalNumber(-1, 2)),
            (RationalNumber(0, 1), 0),
            (RationalNumber(-4, 8), RationalNumber(1, 2))
        )

        for v in values:
            r = -v[0]
            self.assertEqual(r, v[1])

    def test_mul(self):
        values = (
            (RationalNumber(1, 2), RationalNumber(1, 3), RationalNumber(1, 6)),
            (RationalNumber(1, 2), 2, 1),
            (-6, RationalNumber(1, 3), -2),
            (RationalNumber(1, 2), 0.5, RationalNumber(1, 4)),
            (-0.3, RationalNumber(1, 3), RationalNumber(1, -10)),
            (RationalNumber(1, 6), RationalNumber(-6, 1), -1),
            (RationalNumber(1, 6), RationalNumber(0, 1), 0)
        )

        for v in values:
            r = v[0] * v[1]
            self.assertEqual(r, v[2])

    def test_order(self):
        r0 = RationalNumber(1, 2)
        r1 = RationalNumber(3, 6)
        r2 = RationalNumber(3, 1)
        r3 = RationalNumber(-12, -4)

        self.assertEqual(r0, r1)
        self.assertEqual(r2, r3)
        self.assertEqual(r2, 3)

        self.assertTrue(r0.__ge__(r1))
        self.assertTrue(r1.__gt__(0))
        self.assertTrue(r3.__gt__(-0.1))

        self.assertFalse(r1 < r0)
        self.assertFalse(r1.__rgt__(0))
        self.assertFalse(r3.__rgt__(-0.1))

    def test_pow(self):
        r0 = RationalNumber(1, 2)
        r1 = RationalNumber(0, 1)

        self.assertEqual(r0**3, RationalNumber(1, 8))
        self.assertEqual(r1**4, 0)
        self.assertEqual(r0**0, 1)
        self.assertEqual(r0**(-2), 4)

    def test_str_(self):
        self.assertEqual(str(RationalNumber(-2, 3)), '-2/3')

