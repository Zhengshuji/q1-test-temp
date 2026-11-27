"""493c：A=J5 上移位、C=e7、k=5，换 L0=[e1;e3]（H_A0=[e2;e4]）。
子族 r2=αr1+βe1+γe3。检查 (5a)/(5b)。"""
import random
from itertools import combinations
import sympy as sp

lam = sp.symbols('lam')
k = 5
M = sp.zeros(k, k)
for i in range(k - 1):
    M[i + 1, i] = 1

random.seed(31)
cnt = {'total': 0, 'five_a': 0, 'gcd1': 0, 'gcd_pos': 0}
ex = []
for trial in range(300):
    r1 = [random.randint(-3, 3) for _ in range(k)]
    al, be, ga = (random.randint(-2, 2) for _ in range(3))
    r2 = [al * r1[i] + (be if i == 0 else 0) + (ga if i == 2 else 0) for i in range(k)]
    H = sp.Matrix([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], r1, r2])
    HA = sp.Matrix([[0, 1, 0, 0, 0], [0, 0, 0, 1, 0],
                    (sp.Matrix([r1]) * M).tolist()[0], (sp.Matrix([r2]) * M).tolist()[0]])
    cnt['total'] += 1
    if H.rank() != 3:
        continue
    if sp.Matrix.vstack(H, HA).rank() != 3:
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
            ex.append((r1, al, be, ga, g))
    else:
        cnt['gcd_pos'] += 1
print(cnt)
for e in ex:
    print('feasible:', e)
