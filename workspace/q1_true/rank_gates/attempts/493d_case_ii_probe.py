"""493d：L0=[e1;e3]、A=J5 的 case (ii)：r1∈span(e1,e3)，r2 独立（rank H=3）。
看 (5a)/(5b) 是否可同时成立（结构化取样，不是盲目随机）。"""
import random
from itertools import combinations
import sympy as sp

lam = sp.symbols('lam')
k = 5
M = sp.zeros(k, k)
for i in range(k - 1):
    M[i + 1, i] = 1

random.seed(41)
cnt = {'rank3': 0, 'five_a': 0, 'gcd1': 0, 'gcd_pos': 0}
ex = []
for trial in range(200):
    be, ga = random.randint(-3, 3), random.randint(-3, 3)
    r1 = [be, 0, ga, 0, 0]
    r2 = [random.randint(-3, 3) for _ in range(k)]
    H = sp.Matrix([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], r1, r2])
    HA = sp.Matrix([[0, 1, 0, 0, 0], [0, 0, 0, 1, 0],
                    (sp.Matrix([r1]) * M).tolist()[0], (sp.Matrix([r2]) * M).tolist()[0]])
    if H.rank() != 3:
        continue
    cnt['rank3'] += 1
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
            ex.append((r1, r2, g))
    else:
        cnt['gcd_pos'] += 1
print(cnt)
for e in ex:
    print('feasible:', e)
