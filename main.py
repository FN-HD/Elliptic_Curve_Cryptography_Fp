from Mods.Math.Fp import Fp
from Mods.Math.Fp_Element import FpElement
from Mods.EC.Elliptic_Curve_Fp import EllipticCurve
from Mods.EC.Rational_Point_In_ECFp import RationalPointInEC

print(Fp.get_instance(5))
print(EllipticCurve.get_instance(0, 1, 1))

o = RationalPointInEC()
p1 = RationalPointInEC(0, 1)
p2 = RationalPointInEC(0, 4)
p3 = RationalPointInEC(2, 1)
p4 = RationalPointInEC(2, 4)
p5 = RationalPointInEC(3, 1)
p6 = RationalPointInEC(3, 4)

print(o)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)

print(2*p3)
print(o+p1)