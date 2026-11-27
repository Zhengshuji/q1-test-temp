"""520b：n=5 落地的显式核验（参数 β,γ,γ',α,δ,u1,u2,u3 = -2,0,2,2,-2,-1,2,2）。"""
import sympy as sp

x, y, lam = sp.symbols('x y lam')
be, ga, ga2, al, de, u1, u2, u3 = -2, 0, 2, 2, -2, -1, 2, 2

H0 = sp.Matrix([[x * y, x, 0], [y, 1, 0], [0, 0, 1]])
A00 = sp.Matrix([[be, 0, 0], [0, be, ga], [0, 0, ga2]])
a = sp.Matrix([[al * y, al, de]])
u = sp.Matrix([[u1], [u2], [u3]])
HA = sp.expand(H0 * A00 + u * a)
print('HA =', HA)
print('rank H0 at gate (generic x) =', H0.rank())
print('rank HA =', HA.rank())

P = lam * H0 - HA
minors = []
for i in range(3):
    for j in range(3):
        for k in range(j + 1, 3):
            for l in range(i + 1, 3):
                minors.append(sp.expand(P[i, j] * P[l, k] - P[i, k] * P[l, j]))
minors = [m for m in minors if sp.expand(m) != 0]
g = sp.factor(sp.gcd_list(minors))
print('gcd =', g, ' degree in lam =', sp.degree(sp.expand(g), lam))
