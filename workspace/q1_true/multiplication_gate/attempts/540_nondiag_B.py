"""540：ChatGPT 的非对角 B 试验：算 3×3 子式、两两 resultant，检查是否被 u3-u1u2 整除
（target 关于 u3 线性且系数 1，故整除 ⇔ 代入 u3=u1u2 后为零）。"""
import itertools
import sympy as sp

u1, u2, u3, v1, v2, v3, lam = sp.symbols('u1 u2 u3 v1 v2 v3 lam')
u = sp.Matrix([[u1, u2, u3]])
v = sp.Matrix([[v1, v2, v3]])
H = sp.Matrix.vstack(sp.eye(3), u, v)
A0 = sp.diag(0, 1, 0)
B = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
HA = sp.Matrix.vstack(A0, u * B, v * B)
P = lam * H - HA

minors = []
for idx in itertools.combinations(range(5), 3):
    m = sp.expand(sp.Matrix([P[i, :] for i in idx]).det())
    if sp.expand(m) != 0:
        minors.append((idx, m))
print('nonzero minors:', len(minors))

found = 0
for (i1, m1), (i2, m2) in itertools.combinations(minors, 2):
    r = sp.factor(sp.resultant(m1, m2, lam))
    if r == 0:
        continue
    on_gate = sp.simplify(sp.expand(r.subs(u3, u1 * u2)))
    if on_gate == 0:
        print('FOUND', i1, i2)
        found += 1
        break
print('done, found =', found)
