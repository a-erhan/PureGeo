from core.geometry import Triangle

def test_SSS():
    T = Triangle.define(AB=5, BC=7, AC=8).solve()
    assert round(T.A + T.B + T.C, 2) == 180.00
def test_SAS():
    T = Triangle.define(AB=5, AC=6, A=60).solve()
    assert round(T.B + T.C + T.A, 2) == 180.00
def test_ASA():
    T = Triangle.define(AB=10, A=50, B=60).solve()
    assert round(T.A + T.B + T.C, 2) == 180.00     
def test_area_heron():
    T = Triangle.define(AB=3, BC=4, AC=5).solve()
    assert T.area() == 6

def test_explain_contains_keywords():
    T = Triangle.define(AB=5, BC=7, AC=8).solve()
    exp = T.explain()
    assert "Kosinüs" in exp or "Sinüs" in exp

