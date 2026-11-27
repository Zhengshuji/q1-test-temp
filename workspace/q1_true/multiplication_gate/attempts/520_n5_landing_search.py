"""520：n=5 落地搜索。门上 z=xy：
H0=[[xy,x,0],[y,1,0],[0,0,1]]，H_A0=H0*A00+u a，
A00=[[β,0,0],[0,β,γ],[0,0,γ']]，a=(αy,α,δ)，u=(u1,u2,u3)。
随机小整数参数，找门上三子式 gcd 为常数的组合。"""
import random
from itertools import combinations
import sympy as sp

x, y, lam = sp.symbols('x y lam')
random.seed(2026)
hits = []
for trial in range(2000):
    be, ga, ga2, al, de, u1, u2, u3 = [random.randint(-2, 2) for _ in range(8)]
    H0 = sp.Matrix([[x * y, x, 0], [y, 1, 0], [0, 0, 1]])
    A00 = sp.Matrix([[be, 0, 0], [0, be, ga], [0, 0, ga2]])
    a = sp.Matrix([[al * y, al, de]])
    u = sp.Matrix([[u1], [u2], [u3]])
    HA = H0 * A00 + u * a
    if HA.rank() < 2:
        continue
    P = lam * H0 - HA
    minors = []
    for i in range(3):
        for j in range(3):
            for k in range(j + 1, 3):
                for l in range(i + 1, 3):
                    minors.append(sp.expand(P[i, j] * P[l, k] - P[i, k] * P[l, j]))
    minors = [m for m in minors if sp.expand(m) != 0]
    if not minors:
        continue
    g = sp.gcd_list(minors)
    if sp.degree(sp.expand(g), lam) == 0:
        hits.append((be, ga, ga2, al, de, u1, u2, u3))
        if len(hits) >= 3:
            break
print('hits:', len(hits))
for h in hits:
    print(h)
