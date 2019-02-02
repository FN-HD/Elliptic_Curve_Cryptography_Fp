from unittest import TestCase
from Mods.Math.Fp import Fp
from Mods.Math.Fp_Element import FpElement


class TestFpElement(TestCase):
    def test_init(self):
        Fp.get_instance(5)

        p0 = FpElement(0)
        p1 = FpElement(1)
        p2 = FpElement(2)
        p3 = FpElement(3)
        p4 = FpElement(4)

        self.assertEqual(p1+p0, p1)
        self.assertEqual(p3+p4, p2)

        self.assertEqual(p3-p4, p4)
        self.assertEqual(p4-p2, p2)

        self.assertEqual(p2*p3, p1)
        self.assertEqual(p4*p2, p3)

        self.assertEqual(p3/p2, p4)
        self.assertEqual(p4/p3, p3)