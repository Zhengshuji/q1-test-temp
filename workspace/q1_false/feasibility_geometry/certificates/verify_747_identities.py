"""verify_747_identities.py

对 733 族（H=[[2,2],[-1,-1],[2,1]]、g=(-3,-3,-3)）符号验证 747 的两条恒等式：
  f01 = 9*(B + d - lambda)
  f02|_{lambda=B+d} = B*(2*(a-B+c-d) - 3)
从而 B != 0 时 gcd(f01,f02)=1。

纯符号计算（sympy），不含数值。
"""

import sympy as sp

lam, a, B, c, d = sp.symbols('lam a B c d')
H = sp.Matrix([[2, 2], [-1, -1], [2, 1]])
Zp = sp.Matrix([[a, B], [c, d]])
T = sp.Matrix([[1, 0]])
g = [-3, -3, -3]

Z = sp.zeros(3, 3)
for i in range(3):
    z = sp.symbols(f'z{i}_0:3')
    row = H.row(i) * Zp
    eqs = [sp.Eq(sum(z[j] * H[j, k] for j in range(3)) - g[i] * T[0, k], row[0, k])
           for k in range(2)]
    sol = sp.solve(eqs, list(z), dict=True)[0]
    for j in range(3):
        Z[i, j] = sol.get(z[j], z[j])

P = sp.expand(lam * H - Z * H)
f01 = sp.factor(sp.expand(P.extract([0, 1], [0, 1]).det()))
f02 = sp.factor(sp.expand(P.extract([0, 2], [0, 1]).det()))
f12 = sp.factor(sp.expand(P.extract([1, 2], [0, 1]).det()))

print("f01 =", f01)
print("f02 =", f02)
print("f12 =", f12)

id1 = sp.simplify(f01 - 9 * (B + d - lam))
print("identity 1 (f01 - 9(B+d-lam)) =", id1)

val = sp.factor(sp.expand(f02.subs(lam, B + d)))
rhs = B * (2 * (a - B + c - d) - 3)
print("f02|_{lam=B+d} =", val)
print("identity 2 residual =", sp.simplify(val - rhs))

print("gcd(f01,f02) with B=1:", sp.factor(sp.gcd(f01.subs(B, 1), f02.subs(B, 1))))
