r"""Certificate: the "second instance" has no observer of any order (q_min = infinity).

Instance (A2 §32 / a3_joint_feasible.second):
    n = 6, p = 1, C = e_0^T, L_0 = e_1^T,
    A e_5 = e_0, A e_i = e_i (i=1,2,3,4), A e_0 = 0.

Claim: for every L = [L_0; R] (any number q >= 1 of rows),
    (5b) fails at lambda = 1:
    rank[L - L A; C A; C] <= 2 < 3 <= rank[L; C A; C].
Reason: e_1,...,e_4 in V = ker[C;CA] are eigenvectors of A for lambda=1, hence are killed by
C, C A and L(I-A); and [L;CA;C] contains the independent rows e_1, e_5, e_0.

Also checks:
  * the full-pencil spectral gcd for Z = 0 is (x-1)^4;
  * the rank barrier: r(1) = dim pi((I-A)C^n) = 0, while pi(L_0) != 0 forces rho >= 1.

Exact rational arithmetic; every number below is asserted.
用法：python workspace/review_2026-11-01/check_qmin5.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG


def unit(n, i):
    return [Fr(1) if k == i else Fr(0) for k in range(n)]


def instance():
    n = 6
    C = [unit(n, 0)]
    L0 = [unit(n, 1)]
    A = [[Fr(0)] * n for _ in range(n)]
    A[0][5] = Fr(1)          # A e5 = e0
    for i in (1, 2, 3, 4):   # A e_i = e_i
        A[i][i] = Fr(1)
    return A, C, L0, n


def rank(rows):
    return AI.rank([list(r) for r in rows])


def main():
    A, C, L0, n = instance()
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    print('v =', len(V), ' V basis =', [[str(x) for x in v] for v in V])
    assert len(V) == 4
    assert all(AI.rank([[v[k] for v in V] for k in range(n)] + [unit(n, i)]) == 4
               for i in (1, 2, 3, 4))

    # The four eigenvectors in V are killed by C, CA and (I-A).
    for i in (1, 2, 3, 4):
        ei = unit(n, i)
        assert AI.mul(C, [[x] for x in ei]) == [[Fr(0)]]
        assert AI.mul(CA, [[x] for x in ei]) == [[Fr(0)]]
        Aei = [sum(A[k][j] * ei[j] for j in range(n)) for k in range(n)]
        assert Aei == ei, f'e{i} is not a 1-eigenvector'

    # An explicit L of q = 5 with [L; C] invertible (from the audit run).
    L = [
        [Fr(-1), Fr(2), Fr(-2), Fr(0), Fr(-2), Fr(1)],
        [Fr(1), Fr(1), Fr(1), Fr(-1), Fr(-2), Fr(1)],
        [Fr(-2), Fr(1), Fr(1), Fr(2), Fr(-2), Fr(1)],
        [Fr(0), Fr(-1), Fr(2), Fr(-2), Fr(0), Fr(-2)],
        [Fr(-2), Fr(-2), Fr(2), Fr(-2), Fr(1), Fr(-1)],
    ]
    LA = AI.mul(L, A)
    r_rhs = rank(L + CA + C)
    M1 = [[L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
    r_lhs = rank(M1 + CA + C)
    print('rank[L;CA;C] =', r_rhs, ' rank[L-LA;CA;C] at lambda=1 =', r_lhs)
    assert r_rhs >= 3 and r_lhs <= 2, 'the lambda=1 rank drop did not occur'

    # Full-pencil spectral gcd for Z = 0 (d = 0).
    Z0 = [[] for _ in range(n)]
    g, h, cnt = SG.spectral_gcd_Z(A, C, Z0, verbose=True)
    print('gcd for Z=0 =', [str(x) for x in g], ' degree =', SG.pdeg(g), ' h =', h, ' minors =', cnt)
    assert SG.pdeg(g) == 4
    assert g == [Fr(1), Fr(-4), Fr(6), Fr(-4), Fr(1)], 'gcd is not (x-1)^4'

    # Rank barrier: r(1) = dim pi((I-A)C^n), J = row[C;CA].
    I = [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    ImA = [[I[i][j] - A[i][j] for j in range(n)] for i in range(n)]
    r1 = rank(C + CA + ImA) - rank(C + CA)
    rho0 = rank(C + CA + L0) - rank(C + CA)
    print('r(1) =', r1, ' dim pi(L0) =', rho0)
    assert r1 == 0 and rho0 == 1, 'rank-barrier values changed'

    print('\nCERTIFICATE OK: (5b) fails at lambda=1 for every L; q_min = infinity.')


if __name__ == '__main__':
    main()
