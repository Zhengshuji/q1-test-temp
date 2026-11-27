"""O1 block check for c=1 (attempts/191): for a fixed V=L and a chosen H,
compute Z's blocks A_*, B_* and the gcd of the omega-minors of P(lambda).

If B_* = 0 (H_A in row H), P(lambda)=H(lambda I - S) has a nonconstant determinant
and is bad.  Otherwise the gcd test is the definitive check.

Run: python tools/verification/c1_pencil_block.py
"""
import sys
sys.path.insert(0, '.')
sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')
from fractions import Fraction as F
import linalg_q as LQ
import z_generator as ZG
from tools.verification.stratum_solver import prepare, gcd_minors


def block_check(A, C, L0, q, omega, V, bottom):
    """V: line in K0 coords (k-vector); bottom: list of (h, hA) pairs to add (q-omega rows)."""
    N, k, AN, L0N1, L0AN1, RD, G, n = prepare(A, C, L0)
    r = len(L0)
    L0N = [[sum(F(L0[i][u]) * F(N[u][t]) for u in range(n)) for t in range(k)] for i in range(r)]
    L0AN = [[sum(F(L0[i][u]) * F(AN[u][t]) for u in range(n)) for t in range(k)] for i in range(r)]
    H = [row[:] for row in L0N]
    HA = [row[:] for row in L0AN]
    for h, ha in bottom:
        H.append(h[:]); HA.append(ha[:])
    if LQ.rank(H) != omega:
        return {'rankH': LQ.rank(H), 'ok': False}
    # basis Q of im H (q x omega)
    Q = []
    for col in range(k):
        vec = [H[i][col] for i in range(q)]
        if LQ.rank(Q + [vec]) > len(Q):
            Q.append(vec)
        if len(Q) == omega:
            break
    # X: k x omega with H X = Q
    X = [[None] * omega for _ in range(k)]
    for j in range(omega):
        s = LQ.solve([[H[i][t] for t in range(k)] for i in range(q)], [[Q[j][i]] for i in range(q)])
        if s is None:
            return {'ok': False, 'reason': 'H X = Q unsolvable'}
        for t in range(k):
            X[t][j] = s[0][t]
    # ZQ = HA X  (q x omega)
    ZQ = [[sum(F(HA[i][t]) * F(X[t][j]) for t in range(k)) for j in range(omega)] for i in range(q)]
    # A_* = Q^+ ZQ, B_* = R^+ ZQ
    QtQ = [[sum(Q[a][i] * Q[b][i] for i in range(q)) for b in range(omega)] for a in range(omega)]
    inv = LQ.solve([r[:] for r in QtQ], [[F(1) if i == j else F(0)] for i in range(omega)])
    # inv is (solution, ns); build Q^+
    M = inv[0]
    # M is vector of first column; do per column properly
    Qinv = [[F(0)] * q for _ in range(omega)]
    for j in range(omega):
        col = LQ.solve([r[:] for r in QtQ], [[F(1) if i == j else F(0)] for i in range(omega)])[0]
        for a in range(omega):
            Qinv[a][j] = col[a]
    A_star = [[sum(Qinv[a][i] * ZQ[i][b] for i in range(q)) for b in range(omega)] for a in range(omega)]
    Rc = ZG.ker_cols([Q[a][:] for a in range(omega)])  # q x (q-omega)
    R = [[Rc[i][j] for j in range(len(Rc[0]))] for i in range(q)]
    B_star = [[sum(R[i][a] * ZQ[i][b] for i in range(q)) for b in range(omega)] for a in range(q - omega)]
    P = [[(-HA[i][t], H[i][t]) for t in range(k)] for i in range(q)]
    g = gcd_minors(P, q, k, omega)
    return {'rankH': LQ.rank(H), 'Astar': A_star, 'Bstar': B_star,
            'Bzero': all(x == 0 for row in B_star for x in row),
            'gcd_degree': len(g) - 1, 'gcd': g}


if __name__ == '__main__':
    # synthetic: n=6, C=e1, L0=[e4;e5;e6], A e3=e1, A e4=e4, A e5=e5, A e6=e6
    n = 6
    cols = {1: [F(0), F(1), F(0), F(0), F(0), F(0)],
            2: [F(1), F(0), F(0), F(0), F(0), F(0)],
            3: [F(1), F(0), F(0), F(0), F(0), F(0)],
            4: [F(0), F(0), F(0), F(1), F(0), F(0)],
            5: [F(0), F(0), F(0), F(0), F(1), F(0)],
            6: [F(0), F(0), F(0), F(0), F(0), F(1)]}
    A = [[cols[j + 1][i] for j in range(n)] for i in range(n)]
    C = [[F(1), F(0), F(0), F(0), F(0), F(0)]]
    L0 = [[F(0), F(0), F(0), F(1), F(0), F(0)],
          [F(0), F(0), F(0), F(0), F(1), F(0)],
          [F(0), F(0), F(0), F(0), F(0), F(1)]]
    k, q, omega = 4, 4, 3
    V = [F(0), F(0), F(1), F(0)]  # e3 in K0 coords
    # bottom row: h = e5^*, lift l = e5 (admissible: l1=0)
    h = [F(0), F(0), F(0), F(1)]
    # hA = l A N: A e5 = e5 -> e5^*
    ha = [F(0), F(0), F(0), F(1)]
    print(block_check(A, C, L0, q, omega, V, [(h, ha)]))
