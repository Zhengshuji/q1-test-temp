"""488 的反例核验：q1 可行实例可以有 rank L > 3。

构造：n=5、p=1、C=e5^T、A 为移位（e_i A = e_{i-1}，e_1 A=0）、L=I_5、L0=e1^T。
精确有理算术；只核 (5a) 与可观测性（(5b) 由 PBH 对 ∀λ 成立）。
"""
from fractions import Fraction


def rank(rows):
    m = [list(map(Fraction, r)) for r in rows]
    if not m:
        return 0
    nrows, ncols = len(m), len(m[0])
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(nrows):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        r += 1
        if r == nrows:
            break
    return r


n = 5
A = [[0] * n for _ in range(n)]
for i in range(1, n):
    A[i][i - 1] = 1          # e_i A = e_{i-1}
C = [[0, 0, 0, 0, 1]]        # C = e5^T
L = [[1 if i == j else 0 for j in range(n)] for i in range(n)]   # L = I_5
L0 = [[1, 0, 0, 0, 0]]


def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]


LA = matmul(L, A)
CA = matmul(C, A)

r_lca = rank(L + CA + C)
r_full = rank(LA + L + CA + C)
assert r_lca == n, r_lca
assert r_full == n, r_full          # (5a)

# observability
obs = C[:]
cur = C
for _ in range(n - 1):
    cur = matmul(cur, A)
    obs += cur
assert rank(obs) == n, 'not observable'

# (5b) 抽查若干 λ；∀λ 由 PBH（可观测）给出
for lam in [0, 1, 2, 3, 5]:
    M = [[lam * L[i][j] - LA[i][j] for j in range(n)] for i in range(n)]
    assert rank(M + CA + C) == n, lam

rL = rank(L)
rX = rank(L + L0)
print('rank[L;CA;C] =', r_lca)
print('rank[LA;L;CA;C] =', r_full)
print('observability rank =', rank(obs))
print('rank L =', rL, ' rank[L;L0] =', rX)
assert rL == n and rX == n
assert rL > 3
print('OK: q1-feasible instance with rank L = 5 > 3')
