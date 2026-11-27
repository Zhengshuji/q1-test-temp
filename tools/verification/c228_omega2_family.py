"""Exact counterexample to the claimed omega=2, q=3 impossibility (attempt 217).

The construction is the expert's 10-dimensional family (68/69 answer, Section 1.4):
fixed A, C, L0; L(t) has a variable 2-plane kernel, fixed image, uniform spectral
admissibility, and satisfies P_ind for every t.

Run: python tools/verification/c228_omega2_family.py
"""
import sys
from fractions import Fraction as F

sys.path.insert(0, '.')
sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')

import linalg_q as LQ
from tools.verification.consistency_checks import check_candidate


def data():
    n = 10
    A = [[F(0)] * n for _ in range(n)]
    for i, j in [(0, 7), (1, 8), (2, 9), (7, 4), (8, 5), (9, 6)]:
        A[j][i] = F(1)
    C = [
        [F(0), F(0), F(0), F(0), F(1), F(0), F(0), F(0), F(0), F(0)],
        [F(0), F(0), F(0), F(0), F(0), F(1), F(0), F(0), F(0), F(0)],
        [F(0), F(0), F(0), F(0), F(0), F(0), F(1), F(0), F(0), F(0)],
    ]
    L0 = [[F(1), F(0), F(0), F(0), F(0), F(0), F(0), F(0), F(0), F(0)]]
    return n, A, C, L0


def L_of_t(n, t):
    l2 = [F(0), F(1), t, F(0), F(0), F(0), F(0), F(1), F(0), F(0)]
    l3 = [F(1), F(1), t, F(0), F(0), F(0), F(0), F(1), F(1), t]
    return [[F(1)] + [F(0)] * (n - 1), l2, l3]


def main():
    n, A, C, L0 = data()
    for t in (F(0), F(1), F(2), F(-1), F(3)):
        L = L_of_t(n, t)
        res = check_candidate(A, C, L0, L, tag='c228 t=%s' % t, verbose=True)
        assert res['cond'] and res['five_b'], 't=%s failed' % t
    print('PASS: the 10-dimensional family is feasible for all tested t')
    print('It refutes the claimed omega=2, q=3 impossibility (attempt 217).')


if __name__ == '__main__':
    main()
