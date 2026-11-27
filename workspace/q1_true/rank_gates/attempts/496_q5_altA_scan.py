"""496：q=5、n=6、C=e6、A00=e1→e2, e2→0, e3→e3, e4→0（E=e4*）、Ae5=e6。
L0=[e1;e1]，自由 3 行。扫描随机 L，看 (5a) 与 (5b) 是否能同时成立。"""
import random
from itertools import combinations
import sympy as sp

lam = sp.symbols('lam')
n = 6
A = sp.zeros(n, n)
A[1, 0] = 1      # e1 -> e2
A[2, 2] = 1      # e3 -> e3
A[4, 3] = 1      # e4 -> e5
A[5, 4] = 1      # e5 -> e6
C = sp.Matrix([[0, 0, 0, 0, 0, 1]])
N = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])

random.seed(51)
cnt = {'total': 0, 'five_a': 0, 'gcd1': 0, 'gcd_pos': 0}
for trial in range(400):
    L0 = sp.Matrix([[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]])
    R = sp.Matrix([[random.randint(-3, 3) for _ in range(n)] for _ in range(3)])
    L = sp.Matrix.vstack(L0, R)
    H = L * N
    HA = L * A * N
    if H.rank() == 0:
        continue
    cnt['total'] += 1
    if sp.Matrix.vstack(H, HA).rank() != H.rank():
        continue
    cnt['five_a'] += 1
    P = lam * H - HA
    om = H.rank()
    minors = []
    for ri in combinations(range(P.rows), om):
        for ci in combinations(range(P.cols), om):
            minors.append(sp.expand(P.extract(ri, ci).det()))
    minors = [m for m in minors if m != 0]
    g = sp.gcd_list(minors) if minors else sp.Integer(0)
    if sp.degree(g, lam) == 0:
        cnt['gcd1'] += 1
    else:
        cnt['gcd_pos'] += 1
print(cnt)
