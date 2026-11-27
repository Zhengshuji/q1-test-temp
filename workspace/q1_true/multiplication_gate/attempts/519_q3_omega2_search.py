"""519：q=3、ω=2 的候选门：H0=[[z,x,0],[y,1,0],[0,0,1]]（det=z-xy）；
H_A0 的行取 α h2+β h3（常数），搜索门上 2×2 子式 gcd 为常数的组合。"""
import itertools
import sympy as sp

x, y, lam = sp.symbols('x y lam')
h1 = sp.Matrix([[x * y, x, 0]])
h2 = sp.Matrix([[y, 1, 0]])
h3 = sp.Matrix([[0, 0, 1]])
H0 = sp.Matrix.vstack(h1, h2, h3)

found = []
for coeffs in itertools.product([-2, -1, 0, 1, 2], repeat=6):
    a = [coeffs[0] * h2 + coeffs[1] * h3,
         coeffs[2] * h2 + coeffs[3] * h3,
         coeffs[4] * h2 + coeffs[5] * h3]
    HA = sp.Matrix.vstack(a[0], a[1], a[2])
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
        found.append(coeffs)
        if len(found) >= 5:
            break
print('found:', len(found), found[:5])
