"""490 的探针：q=4 显式族里，det H=0 是否迫使 (5b) 失败？

族：n=6、C=e6^T、A=移位、K0=span(e1..e4)、N=I_4、L0=[e1;e2]，
H=[e1;e2;r1;r2]，H_A=[0;e1;r1 M;r2 M]（M 是 A|K0 的坐标矩阵）。
门候选：det H = a d - b c = 0（2x2 子式）。
在 (5a) 子簇（r_i[1] b - r_i[2] a = 0）上取有理点，计算 3x3 子式的 gcd。
注意：这是探索，不是证明；只用于否定“det H=0 本身就是门”。
"""
import random
from fractions import Fraction
from itertools import combinations
import sympy as sp

lam = sp.symbols('lam')
M = sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
random.seed(3)
stats = {'rank3': 0, 'five_a': 0, 'gcd1': 0, 'gcd_pos': 0}
examples = []
for trial in range(100):
    a = Fraction(random.randint(1, 4))
    b = Fraction(random.randint(-3, 3))
    c = Fraction(random.randint(-3, 3))
    d = b * c / a
    r1 = [Fraction(random.randint(-3, 3)), a, b, Fraction(random.randint(-3, 3))]
    r2 = [Fraction(random.randint(-3, 3)), a, b, d]

    def rat(x):
        return sp.Rational(x.numerator, x.denominator)

    H = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [rat(x) for x in r1], [rat(x) for x in r2]])
    if H.rank() != 3:
        continue
    stats['rank3'] += 1
    HA = sp.Matrix([[0, 0, 0, 0], [1, 0, 0, 0],
                    (sp.Matrix([[rat(x) for x in r1]]) * M).tolist()[0],
                    (sp.Matrix([[rat(x) for x in r2]]) * M).tolist()[0]])
    v = sp.Matrix([0, 0, rat(b), -rat(a)])
    if any(sp.simplify(x) != 0 for x in HA * v):
        continue
    stats['five_a'] += 1
    P = lam * H - HA
    minors = []
    for ri in combinations(range(4), 3):
        for ci in combinations(range(4), 3):
            minors.append(sp.expand(P.extract(ri, ci).det()))
    minors = [m for m in minors if m != 0]
    g = sp.gcd_list(minors) if minors else sp.Integer(0)
    if sp.degree(g, lam) == 0:
        stats['gcd1'] += 1
        if len(examples) < 3:
            examples.append((r1, r2, g))
    else:
        stats['gcd_pos'] += 1
print(stats)
for r1, r2, g in examples:
    print('feasible point:', r1, r2, 'gcd=', g)
