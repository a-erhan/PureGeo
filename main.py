from core.geometry import Triangle
from sympy import sqrt,pi
from core.geometry import Triangle



t2 = Triangle.define(AB=6, AC=12, A=60)
t2.solve().summary(symbolic=True, latex_output=False)
