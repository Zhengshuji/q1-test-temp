"""525：n=3,k=2,q=3 族的随机扫描：看是否存在 (5a) 成立且 (5b) 成立的点。"""
import random
from itertools import combinations
import sympy as sp

lam = sp.symbols('lam')
random.seed(7)
cnt = {'total': 0, 'five_a': 0, 'feasible': 0}
for trial in range(500):
    L0 = [[random.randint(-2, 2) for _ in range(3)] for _ in range(2)]
    r = [random.randint(-2, 2) for _ in range(3)]
    L = sp.Matrix([L0[0], L0[1], r])
    H = L[:, 0:2]
    HA = L[:, 1:3]
    om = H.rank()
    if om == 0:
        continue
    cnt['total'] += 1
    if sp.Matrix.vstack(H, HA).rank() != om:
        continue
    cnt['five_a'] += 1
    P = lam * H - HA
    minors = []
    for ri in combinations(range(3), om):
        for ci in combinations(range(2), om):
            minors.append(sp.expand(P.extract(ri, ci).det()))
    minors = [m for m in minors if sp.expand(m) != 0]
    g = sp.gcd_list(minors) if minors else sp.Integer(0)
    if sp.degree(sp.expand(g), lam) == 0:
        cnt['feasible'] += 1
print(cnt)
