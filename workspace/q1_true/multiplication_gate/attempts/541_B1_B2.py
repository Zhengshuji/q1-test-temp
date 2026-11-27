"""541：B1≠B2 的最后实验：H=[I3;u;v]，HA=[A0;uB1;vB2]；检查子式 resultant 是否被 u3-u1u2 整除。"""
import itertools
import sympy as sp

u1, u2, u3, v1, v2, v3, lam = sp.symbols('u1 u2 u3 v1 v2 v3 lam')
u = sp.Matrix([[u1, u2, u3]])
v = sp.Matrix([[v1, v2, v3]])
H = sp.Matrix.vstack(sp.eye(3), u, v)
A0 = sp.diag(1, 0, 0)

Bcands = {
    'shift': sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]]),
    'cycle': sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
    'transp': sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),
    'e12_e23': sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]]),
}

found = 0
for (n1, B1), (n2, B2) in itertools.permutations(Bcands.items(), 2):
    HA = sp.Matrix.vstack(A0, u * B1, v * B2)
    P = lam * H - HA
    minors = []
    for idx in itertools.combinations(range(5), 3):
        m = sp.expand(sp.Matrix([P[i, :] for i in idx]).det())
        if sp.expand(m) != 0:
            minors.append((idx, m))
    hit = False
    for (i1, m1), (i2, m2) in itertools.combinations(minors, 2):
        r = sp.factor(sp.resultant(m1, m2, lam))
        if r == 0:
            continue
        if sp.expand(r.subs(u3, u1 * u2)) == 0:
            print('FOUND', n1, n2, i1, i2)
            hit = True
            break
    if hit:
        found += 1
        break
print('done, found =', found)
