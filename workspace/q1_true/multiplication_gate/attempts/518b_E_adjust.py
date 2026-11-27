"""518b：E = α h1 + β h2（α,β 常数），搜索使门上三子式 gcd 为常数的 (α,β)。"""
import sympy as sp

x, y, lam = sp.symbols('x y lam')
Q = lam**2 - lam * y + y  # 参考
for al in range(-3, 4):
    for be in range(-3, 4):
        p1 = sp.Matrix([[ (lam - al) * x * y - x - be, (lam - al) * x, -(x + be) ]])
        p2 = sp.Matrix([[ lam + 1, 1, lam - y + 1 ]])
        minors = []
        for j in range(3):
            for k in range(j + 1, 3):
                minors.append(sp.expand(p1[0, j] * p2[0, k] - p1[0, k] * p2[0, j]))
        minors = [m for m in minors if sp.expand(m) != 0]
        if not minors:
            continue
        g = sp.gcd_list(minors)
        if sp.degree(sp.expand(g), lam) == 0:
            print('FOUND', al, be, 'gcd=', g)
