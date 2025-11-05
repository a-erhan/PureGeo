from sympy import symbols, cos, sin, acos, pi , simplify, N, sqrtdenest
from sympy import nsimplify
from .utils import rad2deg, deg2rad

def format_angle(angle_expr):
    """Angle expr symbolic veya numeric olabilir; güzel insan-dostu string döndürür."""
    # π’nin katı mı kontrol et
    simp = simplify(angle_expr / pi)
    if simp.is_Rational:
        deg = 180 * simp
        return f"{deg}°"
    # saf float ise yuvarla
    try:
        val = float(N(angle_expr))
        return f"{val:.2f}°"
    except Exception:
        return str(simplify(angle_expr))

def format_side(side_expr):
    #Kenarları kökleriyle sade göster."""
    try:
        return str(simplify(sqrtdenest(side_expr)))
    except Exception:
        return str(simplify(side_expr))



from sympy import symbols, cos, sin, acos, simplify, pi, sqrt, N, latex
from sympy.simplify.sqrtdenest import sqrtdenest

def deg2rad(angle):
    return angle * pi / 180

def rad2deg(angle):
    return angle * 180 / pi

class Triangle:
    def __init__(self, AB=None, BC=None, AC=None, A=None, B=None, C=None):
        self.AB = AB
        self.BC = BC
        self.AC = AC
        self.A = A
        self.B = B
        self.C = C

    @classmethod
    def define(cls, **kwargs):
        return cls(**kwargs)

    def known_count(self):
        sides = sum(v is not None for v in [self.AB, self.BC, self.AC])
        angles = sum(v is not None for v in [self.A, self.B, self.C])
        return sides, angles

    def solve(self):
        sides, angles = self.known_count()

        # ---- Case 1: SSS ----
        if sides == 3:
            self.A = rad2deg(acos((self.BC**2 + self.AC**2 - self.AB**2) / (2*self.BC*self.AC)))
            self.B = rad2deg(acos((self.AC**2 + self.AB**2 - self.BC**2) / (2*self.AC*self.AB)))
            self.C = simplify(180 - self.A - self.B)

        # ---- Case 2: SAS ----
        elif sides == 2 and angles == 1:
            if self.AB and self.AC and self.A:
                a = self.AB
                b = self.AC
                A = deg2rad(self.A)  # 🔹 DÜZELTME: dereceyi radyana çevir
                self.BC = simplify(sqrt(a**2 + b**2 - 2*a*b*cos(A)))  # 🔹 burada cos(A) doğru çalışacak
                self.B = rad2deg(acos((b**2 + self.BC**2 - a**2) / (2*b*self.BC)))
                self.C = simplify(180 - self.A - self.B)

        # ---- Case 3: ASA ----
        elif sides == 1 and angles == 2:
            if self.AB and self.A and self.B:
                self.C = simplify(180 - self.A - self.B)
                self.AC = simplify(self.AB * sin(deg2rad(self.B)) / sin(deg2rad(self.C)))
                self.BC = simplify(self.AB * sin(deg2rad(self.A)) / sin(deg2rad(self.C)))

        else:
            raise ValueError("Şu an sadece SSS, SAS, ASA destekleniyor.")

        return self

    def summary(self, symbolic=True, latex_output=False):
        print("─── Triangle Summary ───")

        def fmt(v):
            if v is None:
                return "-"
            v = simplify(v)
            if symbolic:
                return str(v)
            else:
                return f"{N(v, 6)}"

        if not latex_output:
            print("Sides:")
            for name, val in [("AB", self.AB), ("BC", self.BC), ("AC", self.AC)]:
                print(f"  {name} = {fmt(val)}")
            print("Angles (°):")
            for name, val in [("A", self.A), ("B", self.B), ("C", self.C)]:
                print(f"  {name} = {fmt(val)}°")
            print("────────────────────────")
        else:
            exprs = {
                "AB": self.AB, "BC": self.BC, "AC": self.AC,
                "A": self.A, "B": self.B, "C": self.C
            }
            print("LaTeX Output:")
            print(latex({k: simplify(v) for k, v in exprs.items() if v is not None}))

        return self


