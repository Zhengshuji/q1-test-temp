"""k=5 族探针：n=7, C=e7, A 移位, K0=span(e1..e5), N=I5, L0=[e1;e2], m=2。
H=[e1;e2;r1;r2] (4x5), H_A=[0;e1;r1 M;r2 M]。
统计随机点中 rank H=3 的比例，以及这些点上 (5a)/(5b)。"""
import random
from itertools import combinations
import sympy as sp
from fractions import Fraction

lam = sp.symbols('lam')
k = 5
M = sp.zeros(k, k)
for i in range(1, k):
    M[i, i - 1] = 1

random.seed(13)
cnt = {'total': 0, 'rank3': 0, 'five_a': 0, 'gcd1': 0, 'gcd_pos': 0}
ex = []
for trial in range(400):
    r1 = [random.randint(-3, 3) for _ in range(k)]
    r2 = [random.randint(-3, 3) for _ in range(k)]
    H = sp.Matrix([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], r1, r2])
    HA = sp.Matrix([[0, 0, 0, 0, 0], [1, 0, 0, 0, 0],
                    (sp.Matrix([r1]) * M).tolist()[0], (sp.Matrix([r2]) * M).tolist()[0]])
    cnt['total'] += 1
    if H.rank() != 3:
        continue
    cnt['rank3'] += 1
    ns = H.nullspace()
    if any(any(sp.simplify(x) != 0 for x in HA * v) for v in ns):
        continue
    cnt['five_a'] += 1
    P = lam * H - HA
    minors = []
    for ri in combinations(range(4), 3):
        for ci in combinations(range(k), 3):
            minors.append(sp.expand(P.extract(ri, ci).det()))
    minors = [m for m in minors if m != 0]
    g = sp.gcd_list(minors) if minors else sp.Integer(0)
    if sp.degree(g, lam) == 0:
        cnt['gcd1'] += 1
        if len(ex) < 2:
            ex.append((r1, r2, g))
    else:
        cnt['gcd_pos'] += 1
print(cnt)
for e in ex:
    print('feasible:', e)
