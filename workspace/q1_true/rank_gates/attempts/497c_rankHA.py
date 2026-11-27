"""497c：在 497b 的构造点上看 rank H_A 的分布（是否总是 ≤2 ⇒ λ=0 掉秩）。"""
import random
from itertools import combinations
from collections import Counter
import sympy as sp

lam = sp.symbols('lam')
n = 6
P = sp.zeros(n, 4)
for i in range(4):
    P[i, i] = 1
Q = sp.zeros(n, 4)
for i in range(4):
    Q[i + 1, i] = 1
random.seed(71)
ranks = Counter()
gdeg = Counter()
for trial in range(200):
    a, b, c = (random.randint(-3, 3) for _ in range(3))
    if (a, b, c) == (0, 0, 0):
        continue
    v = sp.Matrix([0, a, b, c])
    M = sp.Matrix.hstack(P * v, Q * v).T
    ns = M.nullspace()
    if len(ns) < 4:
        continue
    rows = []
    for _ in range(3):
        coeff = [random.randint(-3, 3) for _ in range(len(ns))]
        row = sum((coeff[i] * ns[i] for i in range(len(ns))), sp.zeros(n, 1))
        rows.append(row.T)
    S = sp.Matrix.vstack(sp.Matrix([[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]]), *rows)
    H = S * P
    HA = S * Q
    if H.rank() != 3:
        continue
    ranks[HA.rank()] += 1
    Pm = lam * H - HA
    minors = [sp.expand(Pm.extract(ri, ci).det()) for ri in combinations(range(5), 3) for ci in combinations(range(4), 3)]
    minors = [m for m in minors if m != 0]
    g = sp.gcd_list(minors) if minors else sp.Integer(0)
    gdeg[sp.degree(g, lam)] += 1
print('rank HA histogram:', dict(ranks))
print('gcd degree histogram:', dict(gdeg))
