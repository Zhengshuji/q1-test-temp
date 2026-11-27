"""514：l1=(z,x,1) 的小搜索。
固定 r1=(1,0,0)、r2=(1-y,0,1)；l2=(a,b,c) 常数；r3=(p,q,r) 常数。
要求：D1(gate)=0 恒等、D2=c0(z-xy)、门上三子式 gcd=1。
"""
import itertools
import sympy as sp

x, y, z, lam = sp.symbols('x y z lam')
r1 = sp.Matrix([[1, 0, 0]])
r2 = sp.Matrix([[1 - y, 0, 1]])

hits = []
for a, b, c in itertools.product([-1, 0, 1], repeat=3):
    if (a, b, c) == (0, 0, 0):
        continue
    l2 = sp.Matrix([[a, b, c]])
    for p, q, r in itertools.product([-1, 0, 1], repeat=3):
        r3 = sp.Matrix([[p, q, r]])
        A = sp.Matrix.vstack(r1, r2, r3)
        l1 = sp.Matrix([[z, x, 1]])
        H0 = sp.Matrix.vstack(l1, l2)
        HA0 = sp.Matrix.vstack(l1 * A, l2 * A)
        D1 = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(0)).det())
        D2 = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(1)).det())
        if sp.expand(D1.subs(z, x * y)) != 0:
            continue
        # D2 = c0*(z-xy)?
        c0 = sp.expand(D2).coeff(z, 1)
        if c0 == 0:
            continue
        if sp.expand(D2 - c0 * (z - x * y)) != 0:
            continue
        hits.append((a, b, c, p, q, r, D1, D2))
print('hits:', len(hits))
for h in hits[:8]:
    print(h[:6], 'D1=', sp.factor(h[6]), 'D2=', sp.factor(h[7]))
