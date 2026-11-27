"""Indexing check for the Gram-Bezout certificate (attempt 313).

For the 244 pencil P (3x3, omega=2):
  f_i = 2x2 minors, coefficients c_{i,a};
  B_{(i,j),t} = c_{i,t-j},  0<=j<omega, 0<=t<2omega;
  (B^T B)_{t,t'} = sum_j S_{t-j,t'-j},  S_{a,b}=sum_i c_{i,a}c_{i,b}.

Run: python tools/verification/c313_gram_indexing.py
"""
import itertools

import sympy as sp

lam = sp.symbols('lam')


def coeffs(poly, degree):
    p = sp.Poly(sp.expand(poly), lam)
    return [sp.expand(p.coeff_monomial(lam ** k)) for k in range(degree + 1)]


def main():
    P = sp.Matrix([[0, 0, lam],
                   [lam - 3, 2 * lam - 6, -1],
                   [3 * lam - 3, 6 * lam - 6, lam - 3]])
    omega = 2
    f = []
    for rows in itertools.combinations(range(3), omega):
        for cols in itertools.combinations(range(3), omega):
            f.append(sp.expand(P.extract(rows, cols).det()))
    c = [coeffs(fi, omega) for fi in f]  # c[i][a], a=0..omega

    # S_{a,b} = sum_i c_{i,a} c_{i,b}
    S = {}
    for a in range(omega + 1):
        for b in range(omega + 1):
            S[a, b] = sum(c[i][a] * c[i][b] for i in range(len(f)))

    # B rows (i,j), cols t: c_{i,t-j}
    rows = []
    for i in range(len(f)):
        for j in range(omega):
            rows.append([c[i][t - j] if 0 <= t - j <= omega else 0
                         for t in range(2 * omega)])
    B = sp.Matrix(rows)
    print('B shape =', B.shape)
    M = B.T * B

    for t in range(2 * omega):
        for tp in range(2 * omega):
            val = sum(S.get((t - j, tp - j), 0) for j in range(omega))
            assert sp.expand(M[t, tp] - val) == 0
    print('PASS: (B^T B)_{t,t\'} = sum_j S_{t-j,t\'-j}')

    e0 = sp.Matrix([1, 0, 0, 0])
    assert sp.Matrix.vstack(B, e0.T).rank() == B.rank()
    print('PASS: e0 in row(B) for the 244 pencil')


if __name__ == '__main__':
    main()
