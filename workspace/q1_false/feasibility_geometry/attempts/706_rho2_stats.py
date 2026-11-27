import itertools
import random
import sympy as sp

lam = sp.symbols('lam')
Zp = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
T = sp.Matrix([[1, 0, 0]])
random.seed(31)
stats = {}
for _ in range(400):
    H = sp.Matrix(3, 3, [random.randint(-2, 2) for _ in range(9)])
    if H.rank() != 2:
        continue
    U = H.rowspace()
    UT = sp.Matrix.vstack(*([r for r in U] + [T.row(0)]))
    rUT = UT.rank()
    if any(sp.Matrix.vstack(UT, H.row(i) * Zp).rank() > rUT for i in range(3)):
        continue
    rows = []
    ok = True
    for i in range(3):
        v = H.row(i) * Zp
        z = sp.symbols(f'z{i}_0:3')
        g = sp.symbols(f'g{i}')
        eqs = [sp.Eq(sum(z[j] * H[j, col] for j in range(3)) - g * T[0, col], v[0, col])
               for col in range(3)]
        sol = sp.solve(eqs, list(z) + [g], dict=True)
        if not sol:
            ok = False
            break
        s0 = sol[0]
        free = [s for s in list(z) + [g] if s not in s0]
        vals = {s: random.randint(-2, 2) for s in free}
        rows.append([sp.simplify((s0.get(zz, zz)).subs(vals)) for zz in z])
    if not ok:
        continue
    Zm = sp.Matrix(rows)
    P = lam * H - Zm * H
    ms = []
    for r in itertools.combinations(range(3), 2):
        for c in itertools.combinations(range(3), 2):
            f = sp.expand(P.extract(r, c).det())
            if f != 0:
                ms.append(f)
    coeffs = []
    for f in ms:
        cs = sp.Poly(f, lam).all_coeffs()[::-1]
        coeffs.append([cs[k] if k < len(cs) else 0 for k in range(3)])
    rho = sp.Matrix(coeffs).rank() if coeffs else 0
    cls = 'e1inU' if sp.Matrix.vstack(*U, T.row(0)).rank() == len(U) else 'notin'
    stats.setdefault(cls, {}).setdefault(rho, 0)
    stats[cls][rho] += 1
print(stats)
