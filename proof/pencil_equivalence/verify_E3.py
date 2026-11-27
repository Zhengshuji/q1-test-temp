"""E3 的精确复核：(5b) ⟺ dim(V ∩ F_λ) = dim(V ∩ J) 对每个 λ。

E3（docs/00 §0.3）的原文：
    F_λ = { v : v(λI − A) ∈ J },   (5b) ⟺ dim(V ∩ F_λ) = dim(V ∩ J) ∀λ .
纸面证明在 archive/expert_correspondence/Q1_FOR_EXPERT_7.md 定理 1（**本项目从未复核** ✗）。
本脚本只做一件事：在有限实例上**逐 λ** 比较两边，找反例。
（验证 ≠ 证明；见 CLAUDE §4。）

用法：python proof/pencil_equivalence/verify_E3.py [--trials 200]
"""
import random
import sys
from fractions import Fraction as F

N_DEFAULT = 200
LAMS = [F(0), F(1), F(-1), F(2), F(1, 2), None]   # None = 每例再随机取一个有理数


def mm(X, Y):
    assert len(X[0]) == len(Y), 'dim mismatch'
    return [[sum(F(X[i][k]) * F(Y[k][j]) for k in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def rank(M):
    if not M:
        return 0
    M = [[F(x) for x in r] for r in M]
    rows, cols, r = len(M), len(M[0]), 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


def nullspace_cols(M):
    """解 Mx = 0，返回列向量基。"""
    if not M or not M[0]:
        return []
    A = [[F(x) for x in r] for r in M]
    rows, cols, piv, r = len(A), len(A[0]), [], 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append((r, c))
        r += 1
        if r == rows:
            break
    pc = [p[1] for p in piv]
    basis = []
    for fc in range(cols):
        if fc in pc:
            continue
        v = [F(0)] * cols
        v[fc] = F(1)
        for pr, pcc in piv:
            v[pcc] = -A[pr][fc]
        basis.append(v)
    return basis


def left_null(N):
    """返回 v 的基，使 vN = 0。"""
    if not N:
        return []
    NT = [[N[i][j] for i in range(len(N))] for j in range(len(N[0]))]
    return nullspace_cols(NT)


def one_case(rng, n):
    A = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    C = [[rng.randint(-2, 2) for _ in range(n)]]
    L0 = [[rng.randint(-2, 2) for _ in range(n)]]
    CA = mm(C, A)
    Jrows = C + CA
    j = rank(Jrows)
    if j >= n:
        return []
    Jb = []
    for r in Jrows:
        if rank(Jb + [r]) > len(Jb):
            Jb.append(r)
    U = nullspace_cols([[F(x) for x in r] for r in Jb])      # ker(Jb)，n−j 维
    Um = [[U[k][t] for k in range(len(U))] for t in range(n)]  # n × (n−j)
    q = j + rng.randint(1, min(2, n - j))
    L = [L0[0][:]] + [[rng.randint(-2, 2) for _ in range(n)] for _ in range(q - 1)]
    if rank(L) < q:
        return []
    r0 = rank(L + Jrows)
    dimVJ = rank(L) + j - r0
    out = []
    for lam in LAMS:
        if lam is None:
            lam = F(rng.randint(-3, 3), rng.randint(1, 3))
        M = [[(lam if a == b else 0) - A[a][b] for b in range(n)] for a in range(n)]
        N = mm(M, Um)
        Fl = left_null(N)
        dimVF = rank(L) + len(Fl) - rank(L + Fl) if Fl else 0
        LA = mm(L, A)
        rk = rank([[lam * L[i][k] - LA[i][k] for k in range(n)] for i in range(len(L))]
                  + CA + C)
        out.append((rk == r0, dimVF == dimVJ, lam, rk, r0, dimVF, dimVJ))
    return out


def main():
    trials = N_DEFAULT
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    rng = random.Random(20261030)
    ok = bad = 0
    for _ in range(trials):
        for (eq_rank, eq_int, lam, rk, r0, dvf, dvj) in one_case(rng, 4):
            if eq_rank == eq_int:
                ok += 1
            else:
                bad += 1
                if bad <= 5:
                    print(f'  mismatch: lam={lam} rank {rk}/{r0}, dimVF={dvf}, dimVJ={dvj}')
    print(f'E3 逐 λ 比较：{ok}/{ok + bad} 一致' + ('' if bad else ' ✓'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
