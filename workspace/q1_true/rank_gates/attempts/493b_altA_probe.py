"""493b：不同 A（K0 上取 J5 上移位，C=e7, A e7=e6）的 q=4,k=5 族探针。
子族 r2=αr1+βe1+γe2（rank H=3）。检查 (5a) 与 (5b) 是否可能同时成立。"""
import random
from itertools import combinations
import sympy as sp

lam = sp.symbols('lam')
k = 5
# A on K0: e_i -> e_{i+1} (i<5), e5->0;  A e7 = e6
M = sp.zeros(k, k)
for i in range(k - 1):
    M[i + 1, i] = 1

random.seed(21)
cnt = {'total': 0, 'five_a': 0, 'gcd1': 0, 'gcd_pos': 0}
ex = []
for trial in range(300):
    r1 = [random.randint(-3, 3) for _ in range(k)]
    al = random.randint(-2, 2)
    be = random.randint(-2, 2)
    ga = random.randint(-2, 2)
    r2 = [al * r1[i] + (be if i == 0 else 0) + (ga if i == 1 else 0) for i in range(k)]
    # H0=[e1;e2]; H_A0 = [e1 A; e2 A] = [e2; e3]
    H = sp.Matrix([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], r1, r2])
    HA = sp.Matrix([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                    (sp.Matrix([r1]) * M).tolist()[0], (sp.Matrix([r2]) * M).tolist()[0]])
    cnt['total'] += 1
    if H.rank() != 3:
        continue
    # (5a): row HA subset row H  <=> rank[H;HA]=rank H
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
