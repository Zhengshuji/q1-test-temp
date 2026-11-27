"""552：n=5,k=3,m=1 的枚举：L0=[e1;e2;e3]，A 的 K0 列取小向量，r 符号。
分类 (5b) 的 gcd：常数/非常数、是否依赖 r。"""
import itertools
import sympy as sp

r1, r2, r3, r4, r5, lam = sp.symbols('r1 r2 r3 r4 r5 lam')
r = sp.Matrix([[r1, r2, r3, r4, r5]])

vecs = {
    '0': [0, 0, 0, 0, 0],
    'e1': [1, 0, 0, 0, 0],
    'e2': [0, 1, 0, 0, 0],
    'e3': [0, 0, 1, 0, 0],
}

summary = {}
examples = []
for c1, c2, c3 in itertools.product(vecs.values(), repeat=3):
    AN = sp.Matrix([[c1[i], c2[i], c3[i]] for i in range(5)])  # 5x3
    H = sp.Matrix.vstack(sp.eye(3), r[:, 0:3])
    HA = sp.Matrix.vstack(AN.row(0), AN.row(1), AN.row(2), r * AN)
    P = lam * H - HA
    ms = []
    for idx in itertools.combinations(range(4), 3):
        ms.append(sp.expand(sp.Matrix([P[i, :] for i in idx]).det()))
    ms = [m for m in ms if sp.expand(m) != 0]
    if not ms:
        continue
    g = sp.factor(sp.gcd_list(ms))
    deg = sp.degree(sp.expand(g), lam)
    depends_r = any(sp.diff(g, v) != 0 for v in (r1, r2, r3, r4, r5))
    key = (deg, depends_r)
    summary[key] = summary.get(key, 0) + 1
    if deg == 0 and len(examples) < 3:
        examples.append((c1, c2, c3, g))
print('summary:', summary)
for e in examples:
    print('example:', e)
