import math
from sympy import sqrt, Rational, simplify, sin, cos, acos, deg, rad, pi

def sqrt_simplify(value):
    """Try to return a simplified square root (symbolic if possible)."""
    return simplify(sqrt(value))

def deg2rad(d):
    return simplify(d * pi / 180)

def rad2deg(r):
    return simplify(r * 180 / pi)

