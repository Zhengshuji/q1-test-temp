"""527c：搜索使 Res_lam(d12,d23) 为非零常数的常系数（d12, d23 见 527b）。"""
import itertools
import sympy as sp

x, lam = sp.symbols('x lam')
hits = []
for al1, be1, al2, be2, al3, be3 in itertools.product([-2, -1, 0, 1, 2], repeat=6):
    r1 = (lam * x - al1, -be1)
    r2 = (lam - al2, -be2)
    r3 = (-al3, lam - be3)
    d12 = sp.expand(r1[0] * r2[1] - r1[1] * r2[0])
    d23 = sp.expand(r2[0] * r3[1] - r2[1] * r3[0])
    if sp.expand(d12) == 0 or sp.expand(d23) == 0:
        continue
    res = sp.factor(sp.resultant(d12, d23, lam))
    if res != 0 and sp.degree(sp.expand(res), x) == 0:
        hits.append(((al1, be1, al2, be2, al3, be3), res))
        if len(hits) >= 8:
            break
print('hits:', len(hits))
for h in hits:
    print(h)
