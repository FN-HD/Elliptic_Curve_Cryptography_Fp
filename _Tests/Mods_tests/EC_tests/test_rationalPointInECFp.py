from unittest import TestCase
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve
from Mods.EC.Rational_Point_In_ECFp import RationalPointInEC
from Mods.Math.Fp import Fp


class TestRationalPointInEC(TestCase):
    def test(self):
        Fp.get_instance(5)
        EllipticCurve.get_instance(0, 1, 1)

        o = RationalPointInEC()
        p1 = RationalPointInEC(0, 1)
        p2 = RationalPointInEC(0, 4)
        p3 = RationalPointInEC(2, 1)
        p4 = RationalPointInEC(2, 4)
        p5 = RationalPointInEC(3, 1)
        p6 = RationalPointInEC(3, 4)

        self.assertEqual(p1, RationalPointInEC(0, 1))
        self.assertEqual(p3+p3, p4)
        self.assertEqual(p1+p3, p6)
        self.assertEqual(2*p3, p4)
        self.assertEqual(3*p3, o)