"""Exact witness for a dim W_L = 3 instance (attempts/167/168).

n=6, p=1, r=1, k=4, c=2, omega=2, q=3, dim W_L=3 (L0N is an eigenvector, lambda0=1).
The witness L passes all seven checks, so seeds with dim W_L>c are genuinely feasible.

Run:  python tools/verification/c2_dimWL3_witness.py
"""
import sys
sys.path.insert(0, '.')
sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')

from fractions import Fraction as F
import linalg_q as LQ
import z_generator as ZG
from tools.verification.consistency_checks import check_candidate

n = 6
# columns of A: e1->e2, e2->e1, e3->e3+e2, e4->e4, e5->e5, e6->3e6+e2
cols = {
    1: [F(0), F(1), F(0), F(0), F(0), F(0)],
    2: [F(1), F(0), F(0), F(0), F(0), F(0)],
    3: [F(0), F(1), F(1), F(0), F(0), F(0)],
    4: [F(0), F(0), F(0), F(1), F(0), F(0)],
    5: [F(0), F(0), F(0), F(0), F(1), F(0)],
    6: [F(0), F(1), F(0), F(0), F(0), F(3)],
}
A = [[cols[j + 1][i] for j in range(n)] for i in range(n)]
C = [[F(1), F(0), F(0), F(0), F(0), F(0)]]
L0 = [[F(0), F(0), F(1), F(0), F(0), F(0)]]
# witness L (first row L0)
L = [
    [F(0), F(0), F(1), F(0), F(0), F(0)],
    [F(0), F(0), F(1), F(0), F(0), F(1)],
    [F(0), F(1), F(1), F(0), F(0), F(1)],
]


def main():
    N = [r[:] for r in ZG.ker_cols([C[0][:], LQ.mul(C, A)[0]])]
    k = len(N[0]) if N and N[0] else 0
    print('k =', k)
    # W_L = ker[L0 N; L0 A N]
    L0N = LQ.mul(L0, N)[0]
    L0AN = LQ.mul(LQ.mul(L0, A), N)[0]
    WL = ZG.ker_cols([L0N[:], L0AN[:]])
    dWL = len(WL[0]) if WL and WL[0] else 0
    print('dim W_L =', dWL)
    assert dWL == 3
    res = check_candidate(A, C, L0, L, tag='dimWL3', verbose=True)
    assert res['cond'] and res['five_b'], 'checks failed'
    print('PASS: dim W_L=3 instance is feasible (q=3)')


if __name__ == '__main__':
    main()
