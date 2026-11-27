"""Exact witness for seed 10, q=3 (c=2, q=omega+1).

The witness was found by the c=2 algorithm (attempts/156): V=W_L, H rows
  h0=L0N, h1=-h0-u1, h2=-h0+u1,
with the row corrections from row[C;CA]; the 3xk pencil has constant gcd 2,
and L=[L0; R] below passes all seven checks of consistency_checks.

Run:  python tools/verification/c2_seed10_witness.py
"""
import sys
sys.path.insert(0, '.')
sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')

from fractions import Fraction as F
import linalg_q as LQ
from tools.verification.p2_stratification_check import data
from tools.verification.consistency_checks import check_candidate

# witness L (3 x 7), first row is L0
L = [
    [F(0), F(0), F(-1), F(1), F(0), F(0), F(-3)],
    [F(0), F(-1), F(0), F(0), F(-1), F(0), F(0)],
    [F(2), F(-1), F(2), F(0), F(-1), F(0), F(0)],
]


def main():
    A, C, L0, k, d, NK, U0, V0, Z1, Z2 = data(10)
    assert L[0] == L0[0], 'first row must be L0'
    res = check_candidate(A, C, L0, L, tag='seed10-witness', verbose=True)
    assert res['cond'], '(5a) failed'
    assert res['five_b'], '(5b) failed'
    print('PASS: seed10 q=3 witness satisfies (5a), (5b) and all seven checks')


if __name__ == '__main__':
    main()
