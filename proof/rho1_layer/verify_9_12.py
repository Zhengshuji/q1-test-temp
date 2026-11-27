"""定理 9.12（w=0 时 (2,1) 层恒不可行）的**按层号正确辨识**的复核（验证 ≠ 证明）。

与历史 625/625 的区别：本脚本显式用
    rho = rank[L;CA;C] - dim J,   c = dim(row L ∩ J)
辨识层号（教训：层号不能凭 dim L 或 dim(L∩J) 推），并且只统计 (rho,c) = (2,1) 的实例。
tau 的自由度实现为"给 L 的两行各加 J 的元素"（即 beta(tau) 的取值）。
精确有理数算术。
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def mm(X, Y):
    r, k, c = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(c)] for i in range(r)]


def inspan(basis, v):
    if not basis:
        return all(x == 0 for x in v)
    return AI.rank([r[:] for r in basis] + [v[:]]) == AI.rank([r[:] for r in basis])


def layer(L, A, C, J):
    rho = AI.rank(AI.vstack([L, mm(C, A), C])) - len(J)
    c = len(L) + len(J) - AI.rank(AI.vstack([L, J]))
    return rho, c


def main():
    rng = random.Random(2026)
    tested = feas = 0
    for _trial in range(3000):
        n = 5
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        J = AI.row_basis(C + mm(C, A))
        if len(J) < 1:
            continue
        hs = [r for r in J if inspan(J, mm([r], A)[0])]      # w = pi(hA) = 0
        if not hs:
            continue
        for _k in range(20):
            u1 = [Fr(rng.randint(-1, 1)) for _ in range(n)]
            u2 = [Fr(rng.randint(-1, 1)) for _ in range(n)]
            L = AI.row_basis([hs[0], u1, u2])
            if len(L) != 3 or layer(L, A, C, J) != (2, 1):
                continue
            if not AI.cond_5a_orig(A, C, L):
                continue
            cands = [L]
            for _m in range(20):
                d1 = [sum(Fr(rng.randint(-1, 1)) * b[t] for b in J) for t in range(n)]
                d2 = [sum(Fr(rng.randint(-1, 1)) * b[t] for b in J) for t in range(n)]
                L2 = AI.row_basis([hs[0],
                                   [u1[t] + d1[t] for t in range(n)],
                                   [u2[t] + d2[t] for t in range(n)]])
                if len(L2) == 3 and layer(L2, A, C, J) == (2, 1) and AI.cond_5a_orig(A, C, L2):
                    cands.append(L2)
            tested += 1
            if any(AI.cond_5b_orig(A, C, Lx) for Lx in cands):
                feas += 1
            break
    print(f"(2,1) 且 w=0 的候选 {tested} 个：可行 {feas}")
    print("feas = 0 => 与定理 9.12 一致（**验证，不是证明**）")


if __name__ == '__main__':
    main()