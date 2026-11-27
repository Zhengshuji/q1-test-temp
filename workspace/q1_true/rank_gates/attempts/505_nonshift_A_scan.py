"""505：定向实验——非移位 A（e1→0, e2→e1, e3→e2, e4→e5, e5→e6），L0=[e2;e3]。
目的：避开 503 的短核传播链；看 q=5 是否有可行实例（尤其 ω=2/3）。"""
import random
from itertools import combinations
import sympy as sp

lam = sp.symbols('lam')
n = 6
A = sp.zeros(n, n)
A[0, 0] = 0
A[0, 1] = 1      # e2 -> e1
A[1, 2] = 1      # e3 -> e2
A[4, 3] = 1      # e4 -> e5
A[5, 4] = 1      # e5 -> e6
C = sp.Matrix([[0, 0, 0, 0, 0, 1]])
N = sp.zeros(n, 4)
for i in range(4):
    N[i, i] = 1

random.seed(81)
cnt = {}
feas = []
for trial in range(600):
    L0 = sp.Matrix([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]])
    R = sp.Matrix([[random.randint(-3, 3) for _ in range(n)] for _ in range(3)])
    L = sp.Matrix.vstack(L0, R)
    H = L * N
    HA = L * A * N
    om = H.rank()
    if om == 0:
        continue
    cnt[om] = cnt.get(om, 0) + 1
    if sp.Matrix.vstack(H, HA).rank() != om:
        continue
    P = lam * H - HA
    minors = []
    for ri in combinations(range(P.rows), om):
        for ci in combinations(range(P.cols), om):
            minors.append(sp.expand(P.extract(ri, ci).det()))
    minors = [m for m in minors if m != 0]
    g = sp.gcd_list(minors) if minors else sp.Integer(0)
    if sp.degree(g, lam) == 0:
        feas.append((om, g))
        if len(feas) >= 3:
            break
print('rank histogram:', cnt)
print('feasible:', len(feas), feas[:3])
