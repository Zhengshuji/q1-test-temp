"""Machine check of the B_{u,v} quadratic chart identity (attempts/171, expert 60).

For K = span(e_1..e_k) in C^n, chart E = first u coords, F = next k-u, K' = rest:
  U = graph(X) with basis B = [I; X; 0]  (n x u),
  F_A(X) = [[A21 + A22 X - X A11 - X A12 X], [A31 + A32 X]]  ((n-u) x u),
and the identity is  rank F_A(X) = u - dim(U cap A^{-1}U).

Run: python tools/verification/buv_chart_check.py
"""
import sys, random
sys.path.insert(0, '.')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')
from fractions import Fraction as F
import linalg_q as LQ


def block(M, rows, cols):
    return [[M[i][j] for j in cols] for i in rows]


def matmul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def rank(M):
    return LQ.rank([r[:] for r in M])


def check(n, k, u, A, X):
    assert len(A) == n and len(A[0]) == n
    assert len(X) == k - u and len(X[0]) == u
    # blocks: E = 0..u-1, F = u..k-1, K' = k..n-1
    E = list(range(u)); Fb = list(range(u, k)); Kp = list(range(k, n))
    A11 = block(A, E, E); A12 = block(A, E, Fb)
    A21 = block(A, Fb, E); A22 = block(A, Fb, Fb)
    A31 = block(A, Kp, E); A32 = block(A, Kp, Fb)
    XA11 = matmul(X, A11); XA12 = matmul(X, A12)
    XA12X = matmul(XA12, X)
    top = sub(add(A21, matmul(A22, X)), add(XA11, XA12X))
    bot = add(A31, matmul(A32, X))
    FA = top + bot
    # U = graph(X), basis B = [I; X; 0]
    B = [[F(0)] * u for _ in range(n)]
    for i in range(u):
        B[i][i] = F(1)
    for i in range(k - u):
        for j in range(u):
            B[u + i][j] = X[i][j]
    # P_U = B (B^T B)^{-1} B^T ; (I-P_U) A B
    BtB = matmul([[B[i][j] for i in range(n)] for j in range(u)], B)  # u x u
    # invert BtB via LQ.solve with identity columns
    Binv = [[None] * u for _ in range(u)]
    for j in range(u):
        col = LQ.solve([r[:] for r in BtB], [[F(1) if i == j else F(0)] for i in range(u)])[0]
        for i in range(u):
            Binv[i][j] = col[i]
    AB = matmul(A, B)  # n x u
    # (I-P_U) AB = AB - B (B^T B)^{-1} B^T AB
    BtAB = matmul([[B[i][j] for i in range(n)] for j in range(u)], AB)  # u x u
    proj = matmul(B, matmul(Binv, BtAB))  # n x u
    perp = sub(AB, proj)
    dim_int = u - rank(perp)
    return rank(FA), u - dim_int


def main():
    rng = random.Random(2026)
    total = 0
    for n, k, u in [(5, 4, 2), (6, 4, 2), (6, 5, 3), (7, 5, 3), (8, 6, 3)]:
        for trial in range(20):
            A = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(n)]
            X = [[F(rng.randint(-2, 2)) for _ in range(u)] for _ in range(k - u)]
            r, d = check(n, k, u, A, X)
            assert r == d, (n, k, u, trial, r, d, A, X)
            total += 1
    print(f'PASS: rank F_A(X) = u - dim(U cap A^-1 U) on {total} random exact charts')


if __name__ == '__main__':
    main()
