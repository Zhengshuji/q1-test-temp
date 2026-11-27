"""683：通用可行性采样器（随机 V,U,G，验证 678/681/682 的判据）。"""
import itertools
import random
import sympy as sp

lam = sp.symbols('lam')


def build_V(H0, d, k, rng):
    rows = []
    if H0 is not None:
        rows.extend([H0.row(i) for i in range(H0.rows)])
    while len(rows) < d:
        rows.append(sp.Matrix(1, k, [rng.randint(-2, 2) for _ in range(k)]))
    V = sp.Matrix.vstack(*rows)
    return V if V.rank() == d else None


def build_U(r0, q, d, rng):
    top = sp.zeros(r0, d)
    for i in range(r0):
        top[i, i] = 1
    free = sp.Matrix(q - r0, d, [rng.randint(-2, 2) for _ in range((q - r0) * d)])
    return sp.Matrix.vstack(top, free)


def random_G(S, q, rng):
    B = S.rowspace()
    if not B:
        return sp.zeros(q, S.cols)
    rows = []
    for _ in range(q):
        row = sum((rng.randint(-2, 2) * b for b in B), sp.zeros(1, S.cols))
        rows.append(row)
    return sp.Matrix.vstack(*rows)


def rank_M(H, G, Zp, d):
    P = lam * H - (H * Zp + G)
    q, k = H.shape
    minors = []
    for rows in itertools.combinations(range(q), d):
        for cols in itertools.combinations(range(k), d):
            f = sp.expand(P.extract(rows, cols).det())
            if f != 0:
                minors.append(f)
    if not minors:
        return 0
    m = len(minors)
    M = sp.zeros(2 * d, m * d)
    for i, f in enumerate(minors):
        cs = sp.Poly(sp.expand(f), lam).all_coeffs()[::-1]
        for s, c in enumerate(cs):
            for t in range(d):
                if s + t < 2 * d:
                    M[s + t, i * d + t] += c
    return M.rank()


def test(name, Zp, S, H0, q, d, trials=300, seed=0):
    rng = random.Random(seed)
    k = Zp.cols
    r0 = H0.rows if H0 is not None else 0
    hits = 0
    for _ in range(trials):
        V = build_V(H0, d, k, rng)
        if V is None:
            continue
        U = build_U(r0, q, d, rng)
        H = U * V
        if H.rank() != d:
            continue
        G = random_G(S, q, rng)
        if rank_M(H, G, Zp, d) == 2 * d:
            hits += 1
            break
    print(f'{name}: d={d}, q={q}, r0={r0} -> certificate found: {bool(hits)}')


if __name__ == '__main__':
    test('638', sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 0, 0]]), sp.Matrix([[0, 1, 0]]), None, 3, 2, seed=1)
    test('657', sp.Matrix([[0, 0], [1, 0]]), sp.Matrix([[1, 0]]), sp.Matrix([[1, 0]]), 3, 1, seed=2)
    test('661', sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[1, 0]]), sp.Matrix([[0, 1]]), 2, 2, seed=3)
