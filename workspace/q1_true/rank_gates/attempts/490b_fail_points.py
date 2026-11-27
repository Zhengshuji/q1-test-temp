"""490b: 在同族里找 (5a) 成立但 (5b) 失败的点，看失败是否有参数规律。"""
import random
from fractions import Fraction
from itertools import combinations
import sympy as sp

lam = sp.symbols('lam')
M = sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
random.seed(5)
fails = []
oks = 0
for trial in range(200):
    a = Fraction(random.randint(1, 5))
    b = Fraction(random.randint(-4, 4))
    c = Fraction(random.randint(-4, 4))
    d = b * c / a
    s1 = Fraction(random.randint(-3, 3))
    s2 = Fraction(random.randint(-3, 3))
    r1 = [Fraction(random.randint(-3, 3)), a * s1, b * s1, Fraction(random.randint(-3, 3))]
    r2 = [Fraction(random.randint(-3, 3)), a * s2, b * s2, d]

    def rat(x):
        return sp.Rational(x.numerator, x.denominator)

    H = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [rat(x) for x in r1], [rat(x) for x in r2]])
    if H.rank() != 3:
        continue
    HA = sp.Matrix([[0, 0, 0, 0], [1, 0, 0, 0],
                    (sp.Matrix([[rat(x) for x in r1]]) * M).tolist()[0],
                    (sp.Matrix([[rat(x) for x in r2]]) * M).tolist()[0]])
    v = sp.Matrix([0, 0, rat(b), -rat(a)])
    if any(sp.simplify(x) != 0 for x in HA * v):
        continue
    P = lam * H - HA
    minors = []
    for ri in combinations(range(4), 3):
        for ci in combinations(range(4), 3):
            minors.append(sp.expand(P.extract(ri, ci).det()))
    minors = [m for m in minors if m != 0]
    g = sp.gcd_list(minors) if minors else sp.Integer(0)
    if sp.degree(g, lam) > 0:
        fails.append((a, b, c, s1, s2, r1, r2, sp.factor(g)))
    else:
        oks += 1
print('ok', oks, 'fail', len(fails))
for a, b, c, s1, s2, r1, r2, g in fails[:10]:
    print('a,b,c=', a, b, c, 's1,s2=', s1, s2, 'g=', g)
