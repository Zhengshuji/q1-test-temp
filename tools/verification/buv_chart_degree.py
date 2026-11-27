"""Symbolic check of the B_{u,v} chart formula and its degree (attempts/171, expert 60).

F_A(X) = [[A21 + A22 X - X A11 - X A12 X], [A31 + A32 X]]
Each entry must be a polynomial in the entries of X of total degree at most two.

Run: python tools/verification/buv_chart_degree.py
"""
import sympy as sp


def check(m, u, seed=0):
    # X is m x u (m = k-u)
    Xs = sp.symbols('x0:%d' % (m * u))
    X = sp.Matrix(m, u, list(Xs))
    rng = sp.randmatrix if False else None
    import random
    rng = random.Random(seed)
    A11 = sp.Matrix(u, u, lambda i, j: rng.randint(-3, 3))
    A12 = sp.Matrix(u, m, lambda i, j: rng.randint(-3, 3))
    A21 = sp.Matrix(m, u, lambda i, j: rng.randint(-3, 3))
    A22 = sp.Matrix(m, m, lambda i, j: rng.randint(-3, 3))
    A31 = sp.Matrix(1, u, lambda i, j: rng.randint(-3, 3))
    A32 = sp.Matrix(1, m, lambda i, j: rng.randint(-3, 3))
    top = A21 + A22 * X - X * A11 - X * A12 * X
    bot = A31 + A32 * X
    F = sp.Matrix(sp.Matrix(top).col_join(bot))
    for i in range(F.rows):
        for j in range(F.cols):
            expr = sp.expand(F[i, j])
            p = sp.Poly(expr, *Xs)
            assert p.total_degree() <= 2, (i, j, p.total_degree(), expr)
    return F.rows, F.cols, len(Xs)


if __name__ == '__main__':
    total = 0
    for m, u in [(2, 2), (1, 2), (2, 3), (3, 3), (3, 4)]:
        for seed in range(5):
            r, c, nv = check(m, u, seed)
            total += 1
    print(f'PASS: chart entries are polynomials of total degree <= 2 on {total} symbolic instances')
