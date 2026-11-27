"""497b：结构化构造 q=5（A 完整移位, E=e4*）的 rank-3 实例。
取 v=(0,a,b,c)，u=Pv、w=Qv；让 S 的行落在 span(u,w)^⊥，则 H v=H_A v=0。
再检查 rank H=3 与 (5b)。"""
import random
from itertools import combinations
import sympy as sp

lam = sp.symbols('lam')
n = 6
A = sp.zeros(n, n)
for i in range(n - 1):
    A[i + 1, i] = 1
C = sp.Matrix([[0, 0, 0, 0, 0, 1]])
N = sp.zeros(n, 4)
for i in range(4):
    N[i, i] = 1
P = sp.zeros(n, 4)
for i in range(4):
    P[i, i] = 1
Q = sp.zeros(n, 4)
for i in range(4):
    Q[i + 1, i] = 1

random.seed(71)
cnt = {'total': 0, 'rank3': 0, 'gcd1': 0, 'gcd_pos': 0}
ex = []
for trial in range(200):
    a, b, c = (random.randint(-3, 3) for _ in range(3))
    if (a, b, c) == (0, 0, 0):
        continue
    v = sp.Matrix([0, a, b, c])
    u = P * v
    w = Q * v
    # basis of span(u,w)^perp
    M = sp.Matrix.hstack(u, w).T          # 2x6
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
    cnt['total'] += 1
    if sp.Matrix.vstack(H, HA).rank() != 3:
        continue
    cnt['rank3'] += 1
    Pm = lam * H - HA
    minors = []
    for ri in combinations(range(Pm.rows), 3):
        for ci in combinations(range(Pm.cols), 3):
            minors.append(sp.expand(Pm.extract(ri, ci).det()))
    minors = [m for m in minors if m != 0]
    g = sp.gcd_list(minors) if minors else sp.Integer(0)
    if sp.degree(g, lam) == 0:
        cnt['gcd1'] += 1
        if len(ex) < 2:
            ex.append((a, b, c, g))
    else:
        cnt['gcd_pos'] += 1
print(cnt)
for e in ex:
    print('feasible params:', e)
