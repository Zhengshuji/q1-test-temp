"""680：638 数据上带自由行的随机可行性搜索（验证 678 的判据）。"""
import itertools
import random
import sympy as sp

lam = sp.symbols('lam')
Z = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 0, 0]])  # 638 的 Z'
S = sp.Matrix([[0, 1, 0]])  # S = span{e2}


def build(H, G, d):
    HA = H * Z + G
    P = lam * H - HA
    q, k = H.shape
    minors = []
    for rows in itertools.combinations(range(q), d):
        for cols in itertools.combinations(range(k), d):
            f = sp.expand(P.extract(rows, cols).det())
            if f != 0:
                minors.append(f)
    m = len(minors)
    M = sp.zeros(2 * d, m * d)
    b = sp.zeros(2 * d, 1)
    b[0] = 1
    for i, f in enumerate(minors):
        cs = sp.Poly(sp.expand(f), lam).all_coeffs()[::-1]
        for s, c in enumerate(cs):
            for t in range(d):
                if s + t < 2 * d:
                    M[s + t, i * d + t] += c
    return M, b


def rand_G():
    return sp.Matrix([[0, random.randint(-2, 2), 0] for _ in range(3)])


H0 = sp.Matrix([[1, 0, 0]])
found = []
random.seed(0)
for _ in range(2000):
    # 秩 2：自由行取 (a,b,0)，(c,d,0)
    a, b = random.randint(-2, 2), random.randint(-2, 2)
    c, d = random.randint(-2, 2), random.randint(-2, 2)
    H = sp.Matrix.vstack(H0, sp.Matrix([[a, b, 0]]), sp.Matrix([[c, d, 0]]))
    if H.rank() != 2:
        continue
    G = rand_G()
    M, b = build(H, G, 2)
    if M.rank() == 4:
        found.append((H.tolist(), G.tolist()))
        break

print('found feasible point:', bool(found))
if found:
    print('H =', found[0][0])
    print('G =', found[0][1])
    M, b = build(sp.Matrix(found[0][0]), sp.Matrix(found[0][1]), 2)
    print('rank M =', M.rank(), 'rank aug =', M.row_join(b).rank())

# 638 的已知可行点
H = sp.diag(1, 1, 0)
G = sp.Matrix([[0, 0, 0], [0, 0, 0], [0, 1, 0]])
M, b = build(H, G, 2)
print('638 known: rank M =', M.rank(), 'rank aug =', M.row_join(b).rank())
