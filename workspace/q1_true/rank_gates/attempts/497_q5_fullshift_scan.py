"""497：q=5、n=6、C=e6、A 为完整移位（e1→e2→…→e6→0），E=e4*。
L0=[e1;e1]，自由 3 行。扫描 (5a)/(5b)。"""
import random
from itertools import combinations
import sympy as sp

lam = sp.symbols('lam')
n = 6
A = sp.zeros(n, n)
for i in range(n - 1):
    A[i + 1, i] = 1     # e_i -> e_{i+1}
C = sp.Matrix([[0, 0, 0, 0, 0, 1]])
N = sp.zeros(n, 4)
for i in range(4):
    N[i, i] = 1

random.seed(61)
cnt = {'total': 0, 'rank3': 0, 'rank4': 0, 'five_a': 0, 'gcd1': 0, 'gcd_pos': 0}
for trial in range(400):
    L0 = sp.Matrix([[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]])
    R = sp.Matrix([[random.randint(-3, 3) for _ in range(n)] for _ in range(3)])
    L = sp.Matrix.vstack(L0, R)
    H = L * N
    HA = L * A * N
    if H.rank() == 0:
        continue
    cnt['total'] += 1
    om = H.rank()
    cnt['rank3' if om == 3 else ('rank4' if om == 4 else 'other')] = cnt.get('rank3' if om == 3 else ('rank4' if om == 4 else 'other'), 0) + 1
    if sp.Matrix.vstack(H, HA).rank() != om:
        continue
    cnt['five_a'] += 1
    P = lam * H - HA
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
