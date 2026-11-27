"""Exact check of the Gram certificates in attempt 277 (c278).

Part 1: (5b) Gram certificate for the 3x3 pencil P of attempt 244.
  - f_i = all 2x2 minors of P; B = coefficient vectors of f_i and lambda*f_i
    (degrees 0..3).
  - (5b) holds (gcd of f_i is 1) and e0=(1,0,0,0) lies in row(B);
    equivalently B^T B x = e0 is solvable.
  - Cauchy-Binet: sum_i f_i(lam) f_i(mu) = sum_J det(P_J(lam)^T P_J(mu)).

Part 2: (5a) Gram certificate.
  - G_H = H^T H, G_S = H^T H + H_A^T H_A.
  - For the 244 H,HA: e_2(G_H)>0 and e_3(G_S)=0.
  - Perturbing H_A so that rank[H;H_A]=3 gives e_3(G_S)>0.

Run: python tools/verification/c278_gram_certificate.py
"""
import itertools

import sympy as sp

lam, mu = sp.symbols('lam mu')


def coefficients(poly, degree):
    p = sp.Poly(sp.expand(poly), lam)
    return [sp.expand(p.coeff_monomial(lam ** k)) for k in range(degree + 1)]


def main():
    # ---------------- Part 1: (5b) ----------------
    P = sp.Matrix([[0, 0, lam],
                   [lam - 3, 2 * lam - 6, -1],
                   [3 * lam - 3, 6 * lam - 6, lam - 3]])
    omega = 2
    f = []
    for rows in itertools.combinations(range(3), omega):
        for cols in itertools.combinations(range(3), omega):
            f.append(sp.expand(P.extract(rows, cols).det()))
    print('number of 2x2 minors =', len(f))
    g = f[0]
    for h in f[1:]:
        g = sp.gcd(g, h)
    print('gcd of minors =', sp.factor(g))
    assert sp.degree(sp.factor(g), lam) == 0, '(5b) should hold'

    # B: rows = coeff vectors of lambda^t f_i, t=0..omega-1; 2*omega columns
    B = []
    for fi in f:
        for t in range(omega):
            B.append(coefficients(lam ** t * fi, 2 * omega - 1))
    B = sp.Matrix(B)
    print('B shape =', B.shape, 'rank B =', B.rank())
    e0 = sp.Matrix([1, 0, 0, 0])
    # e0 in row(B) iff rank([B; e0]) = rank(B)
    print('rank[B;e0] =', sp.Matrix.vstack(B, e0.T).rank())
    assert sp.Matrix.vstack(B, e0.T).rank() == B.rank()

    # solve B^T B x = e0 exactly
    M = B.T * B
    sol = M.gauss_jordan_solve(e0)
    x = sol[0]
    print('B^T B x =', sp.simplify(M * x))
    assert sp.simplify(M * x - e0) == sp.zeros(4, 1)

    # Cauchy-Binet
    lhs = sp.expand(sum(fi.subs(lam, lam) * fi.subs(lam, mu) for fi in f))
    rhs = 0
    for cols in itertools.combinations(range(3), omega):
        Pj = P[:, list(cols)]
        Pj_mu = Pj.subs(lam, mu)
        rhs += sp.expand((Pj.T * Pj_mu).det())
    print('Cauchy-Binet difference =', sp.factor(sp.expand(lhs - rhs)))
    assert sp.expand(lhs - rhs) == 0

    # B^T B from K: (1+lam*mu) K coefficients
    K = lhs
    weighted = sp.expand((1 + lam * mu) * K)
    for d in range(2 * omega):
        for e in range(2 * omega):
            val = sp.Poly(weighted, lam, mu).coeff_monomial(lam ** d * mu ** e)
            assert sp.expand(val - M[d, e]) == 0
    print('B^T B coefficient formula: OK')

    # ---------------- Part 2: (5a) ----------------
    H = sp.Matrix([[0, 0, 1], [1, 2, 0], [3, 6, 1]])
    HA = sp.Matrix([[0, 0, 0], [3, 6, 1], [3, 6, 3]])
    GH = H.T * H
    GS = H.T * H + HA.T * HA
    print('rank H =', H.rank(), 'rank[H;HA] =', sp.Matrix.vstack(H, HA).rank())
    assert sp.Matrix.vstack(H, HA).rank() == H.rank() == 2
    # elementary symmetric e2, e3 via charpoly coefficients
    def e_sym(G, j):
        x = sp.Symbol('x')
        cp = G.charpoly(x).as_expr()
        # charpoly = x^n - e1 x^{n-1} + e2 x^{n-2} - ...
        return sp.expand((-1) ** j * cp.coeff(x, G.shape[0] - j))

    print('e2(GH) =', e_sym(GH, 2), '; e3(GS) =', e_sym(GS, 3))
    assert e_sym(GH, 2) > 0
    assert sp.simplify(e_sym(GS, 3)) == 0

    HA_bad = sp.Matrix(HA)
    HA_bad[0, 0] = 1
    GS_bad = H.T * H + HA_bad.T * HA_bad
    print('perturbed rank[H;HA] =', sp.Matrix.vstack(H, HA_bad).rank(),
          '; e3(GS_bad) =', e_sym(GS_bad, 3))
    assert sp.Matrix.vstack(H, HA_bad).rank() == 3
    assert sp.simplify(e_sym(GS_bad, 3)) != 0
    print('PASS: Gram certificates for (5a) and (5b) verified on the 244 data')


if __name__ == '__main__':
    main()
