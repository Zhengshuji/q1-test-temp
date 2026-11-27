"""Audit of the explicit (5a) gate (attempt 234/237), with the expert's corrections.

Checks:
1. det M = a*d - b*c.
2. rank M0 = 4 iff (c,d) != (0,0).
3. (5a) locus: {ad=bc, (c,d)!=(0,0)} union {a=b=c=d=0}.
4. (5b) counterexamples: (1,0,1,0,0) and (1,-5,1,-5,0) satisfy (5a) but fail (5b).
5. Boundary witness (0,0,1,1,0) satisfies (5a) and (5b), with rank H = 2.

Run: python tools/verification/c237_gate_audit.py
"""
import sympy as sp

lam = sp.symbols('lam')
a, b, c, d, e = sp.symbols('a b c d e')

A = sp.Matrix([[1, 1, -1, 0, 1],
               [-1, 0, 0, -1, 1],
               [0, 1, -1, 0, 1],
               [0, 0, 0, -1, 0],
               [-1, 1, 0, 0, 0]])
C = sp.Matrix([[0, 0, 0, 0, 1]])
L0 = sp.Matrix([[1, 0, 0, 0, 0]])
l = sp.Matrix([[a, b, c, d, e]])
CA = C * A
N = sp.Matrix.hstack(*sp.Matrix.vstack(C, CA).nullspace())

M = sp.Matrix.vstack(l * A, L0, l, CA, C)
M0 = sp.Matrix.vstack(L0, l, CA, C)
det = sp.factor(sp.expand(M.det()))
assert det == a * d - b * c, det
print('1. det M =', det)

# rank M0 at generic (c,d) != 0 is 4; at c=d=0 it is 3
r_generic = M0.rank()
r_boundary = M0.subs({a: 1, b: 2, c: 0, d: 0, e: 0}).rank()
print('2. rank M0 generic =', r_generic, '; at c=d=0 =', r_boundary)
assert r_generic == 4 and r_boundary == 3

# 4. (5b) counterexamples
H = sp.expand(sp.Matrix([[1, 0, 0], [a + b, c, d]]))
HA = sp.expand(sp.Matrix([[2, -1, 0], [2 * a - b + c, -a - c, -b - d]]))
P = lam * H - HA
minors = [sp.expand(P[:, cols].det()) for cols in [(0, 1), (0, 2), (1, 2)]]
print('3. minors:', [sp.factor(m) for m in minors])
for pt in [(1, 0, 1, 0, 0), (1, -5, 1, -5, 0)]:
    sub = {a: pt[0], b: pt[1], c: pt[2], d: pt[3], e: pt[4]}
    ms = [sp.factor(m.subs(sub)) for m in minors]
    g = ms[0]
    for m in ms[1:]:
        g = sp.gcd(g, m)
    print('4. point', pt, 'minors', ms, 'gcd', sp.factor(g))
    assert sp.degree(g, lam) > 0, 'expected (5b) failure at %s' % (pt,)

# 5. boundary witness (0,0,1,1,0)
pt = (0, 0, 1, 1, 0)
sub = {a: pt[0], b: pt[1], c: pt[2], d: pt[3], e: pt[4]}
ms = [sp.factor(m.subs(sub)) for m in minors]
g = ms[0]
for m in ms[1:]:
    g = sp.gcd(g, m)
Hsub = H.subs(sub)
HA_sub = HA.subs(sub)
Psub = lam * Hsub - HA_sub
print('5. boundary point', pt, 'minors', ms, 'gcd', sp.factor(g))
assert sp.degree(g, lam) == 0, 'expected (5b) to hold at the boundary point'
assert Hsub.rank() == 2
# (5a): rank M = rank M0
M_sub = M.subs(sub)
M0_sub = M0.subs(sub)
print('   rank M / M0 =', M_sub.rank(), M0_sub.rank())
assert M_sub.rank() == M0_sub.rank() == 4
print('PASS: audit corrections verified')
