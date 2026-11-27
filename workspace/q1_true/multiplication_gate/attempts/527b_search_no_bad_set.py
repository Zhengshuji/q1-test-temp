"""527b：搜索常系数 a_i=α_i h2+β_i h3，使门上三个 2×2 子式的 gcd 在 Q(x)[lam] 中为 1（无坏集）。"""
import itertools
import sympy as sp

x, lam = sp.symbols('x lam')
hits = []
for al1, be1, al2, be2, al3, be3 in itertools.product([-2, -1, 0, 1, 2], repeat=6):
    r1 = (lam * x - al1, -be1)
    r2 = (lam - al2, -be2)
    r3 = (-al3, lam - be3)
    d12 = sp.expand(r1[0] * r2[1] - r1[1] * r2[0])
    d13 = sp.expand(r1[0] * r3[1] - r1[1] * r3[0])
    d23 = sp.expand(r2[0] * r3[1] - r2[1] * r3[0])
    polys = [p for p in [d12, d13, d23] if sp.expand(p) != 0]
    if len(polys) < 2:
        continue
    g = sp.gcd_list(polys)
    if sp.degree(sp.expand(g), lam) == 0:
        hits.append(((al1, be1, al2, be2, al3, be3), [sp.factor(p) for p in polys]))
        if len(hits) >= 5:
            break
print('hits:', len(hits))
for h in hits:
    print(h)
