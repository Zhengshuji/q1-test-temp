"""554：k=2,m=2（q=4）枚举：L0=[e1;e2]，u,v 符号，A 的 K0 列取小向量；计算 (5b) 的 gcd。"""
import itertools
import sympy as sp

u1, u2, u3, u4, v1, v2, v3, v4, lam = sp.symbols('u1 u2 u3 u4 v1 v2 v3 v4 lam')
u = sp.Matrix([[u1, u2, u3, u4]])
v = sp.Matrix([[v1, v2, v3, v4]])

vecs = {'0': [0, 0, 0, 0], 'e1': [1, 0, 0, 0], 'e2': [0, 1, 0, 0],
        'e3': [0, 0, 1, 0], 'e4': [0, 0, 0, 1]}

summary = {}
examples = []
for (n1, c1), (n2, c2) in itertools.product(vecs.items(), repeat=2):
    AN = sp.Matrix([[c1[i], c2[i]] for i in range(4)])  # 4x2
    H = sp.Matrix.vstack(sp.eye(2), u[:, 0:2], v[:, 0:2])
    HA = sp.Matrix.vstack((sp.Matrix([[1, 0, 0, 0]]) * AN), (sp.Matrix([[0, 1, 0, 0]]) * AN),
                          u * AN, v * AN)
    P = lam * H - HA
    ms = []
    for i in range(4):
        for j in range(i + 1, 4):
            ms.append(sp.expand(P[i, 0] * P[j, 1] - P[i, 1] * P[j, 0]))
    ms = [m for m in ms if sp.expand(m) != 0]
    if not ms:
        continue
    g = sp.factor(sp.gcd_list(ms))
    deg = sp.degree(sp.expand(g), lam)
    depends = any(sp.diff(g, w) != 0 for w in (u1, u2, u3, u4, v1, v2, v3, v4))
    summary[(n1, n2, deg, depends)] = summary.get((n1, n2, deg, depends), 0) + 1
    if deg == 0:
        examples.append((n1, n2, g))
print('constant-gcd cases:', len(examples))
for e in examples[:5]:
    print(e)
print('total combos with nonempty minors:', sum(summary.values()))
