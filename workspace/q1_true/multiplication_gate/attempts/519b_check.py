"""519b：显式检查 q=3、omega=2 的候选门（组合 (-2,-2,-2,-2,-2,-1)）。"""
import sympy as sp

x, y, lam = sp.symbols('x y lam')
h1 = sp.Matrix([[x * y, x, 0]])
h2 = sp.Matrix([[y, 1, 0]])
h3 = sp.Matrix([[0, 0, 1]])
H0 = sp.Matrix.vstack(h1, h2, h3)
c = (-2, -2, -2, -2, -2, -1)
a1 = c[0] * h2 + c[1] * h3
a2 = c[2] * h2 + c[3] * h3
a3 = c[4] * h2 + c[5] * h3
HA = sp.Matrix.vstack(a1, a2, a3)
print('rank HA =', HA.rank())
P = lam * H0 - HA
minors = []
for i in range(3):
    for j in range(3):
        for k in range(j + 1, 3):
            for l in range(i + 1, 3):
                minors.append(sp.expand(P[i, j] * P[l, k] - P[i, k] * P[l, j]))
minors = [m for m in minors if sp.expand(m) != 0]
g = sp.gcd_list(minors)
print('gcd =', sp.factor(g), ' degree =', sp.degree(sp.expand(g), lam))
