"""507b：固定行 q=2、k=2 的小枚举（快速版）。
找 l1、A 使 det[l1 A; l1] = c*(z - x*y)（c 为非零常数）。
"""
import itertools
import sympy as sp

x, y, z = sp.symbols('x y z')
target = sp.expand(z - x * y)
vals = [sp.Integer(0), sp.Integer(1), sp.Integer(-1), x, y, z]
l1s = [(sp.Integer(1), sp.Integer(0)), (sp.Integer(0), sp.Integer(1)),
       (sp.Integer(1), sp.Integer(1)), (z, sp.Integer(1)), (sp.Integer(1), z)]

hits = []
for l1 in l1s:
    for entries in itertools.product(vals, repeat=4):
        A = sp.Matrix(2, 2, entries)
        e1 = sp.expand((l1[0] * A[0, 0] + l1[1] * A[1, 0]) * l1[1]
                       - (l1[0] * A[0, 1] + l1[1] * A[1, 1]) * l1[0])
        if e1 == 0:
            continue
        c = sp.expand(e1).coeff(z, 1)
        if c == 0:
            continue
        if sp.expand(e1 - c * target) == 0:
            hits.append((l1, A.tolist(), e1, c))
            if len(hits) >= 5:
                break
    if len(hits) >= 5:
        break
print('hits:', len(hits))
for l1, A, e1, c in hits:
    print('l1=', l1, 'A=', A, 'det=', e1, 'c=', c)
