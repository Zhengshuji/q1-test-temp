"""668：验证 667 的 Bézout 秩判据 rank[M|e0]=rank M。"""
import itertools
import sympy as sp

lam = sp.symbols('lam')


def bezout_rank(P, d, name):
    q, k = P.shape
    minors = []
    for rows in itertools.combinations(range(q), d):
        for cols in itertools.combinations(range(k), d):
            minors.append(sp.expand(P.extract(rows, cols).det()))
    minors = [m for m in minors if sp.expand(m) != 0]
    m = len(minors)
    # coefficient matrix: unknown g[i,k], i< m, k<d
    A = sp.zeros(2 * d, m * d)
    b = sp.zeros(2 * d, 1)
    b[0] = 1
    for i, f in enumerate(minors):
        poly = sp.Poly(sp.expand(f), lam)
        for kk in range(d):
            for t, c in enumerate(poly.all_coeffs()):
                # term c * lam^t, t counted from highest; convert to power
                pass
        coeffs = sp.Poly(sp.expand(f), lam).all_coeffs()[::-1]  # coeffs[s] = coeff of lam^s
        for s, c in enumerate(coeffs):
            for kk in range(d):
                if s + kk < 2 * d:
                    A[s + kk, i * d + kk] += c
    r = A.rank()
    ra = A.row_join(b).rank()
    print(f'{name}: minors={m}, rank M={r}, rank[M|b]={ra}, solvable={r == ra}')


if __name__ == '__main__':
    # 638: feasible
    H = sp.diag(1, 1, 0)
    Z = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    P = lam * H - Z * H
    bezout_rank(P, 2, '638 (feasible, d=2)')

    # 641B: infeasible
    H2 = sp.Matrix([[-1, -1, 0], [-1, -1, -1], [-1, -1, -1]])
    Z2 = sp.Matrix([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
    P2 = lam * H2 - Z2 * H2
    bezout_rank(P2, 2, '641B (infeasible, d=2)')
