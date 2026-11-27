"""673：D_d 与 M 的秩/可解性实验（d=2，H=diag(1,1,0)）。"""
import itertools
import random
import sympy as sp

lam = sp.symbols('lam')


def build_system(H, Z, d):
    q, k = H.shape
    P = lam * H - Z * H
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
        coeffs = sp.Poly(sp.expand(f), lam).all_coeffs()[::-1]
        for s, c in enumerate(coeffs):
            for t in range(d):
                if s + t < 2 * d:
                    M[s + t, i * d + t] += c
    return M, b, m


H = sp.diag(1, 1, 0)
# 638 的 Z
Z638 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
M, b, m = build_system(H, Z638, 2)
print('638: m=', m, 'rank M=', M.rank(), 'rank aug=', M.row_join(b).rank(),
      'solvable=', M.rank() == M.row_join(b).rank())

random.seed(1)
found = 0
for _ in range(300):
    Z = sp.Matrix(3, 3, [random.randint(-2, 2) for _ in range(9)])
    M, b, m = build_system(H, Z, 2)
    if M.rank() < 4 and M.rank() == M.row_join(b).rank():
        print('rank<4 且可解: rank=', M.rank(), 'Z=', Z.tolist())
        found += 1
        if found >= 3:
            break
print('rank<4 且可解的随机样例数:', found)
