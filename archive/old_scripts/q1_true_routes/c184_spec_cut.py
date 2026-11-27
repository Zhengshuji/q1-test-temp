"""c184_spec_cut.py — 检验：spec_cut > 0 是否只在 E∩K 可行时发生

A,C,L0 取 F_3 上的小整数矩阵；枚举 F_3^4 的全部子空间（作为有理子空间）；
- d_alg = max dim Z, Z ⊆ E, A(Z∩K) ⊆ Z
- d_true = max dim Z 再加 (8c)
记录 (E∩K 可行, d_alg, d_true)。

用法：python q1_true/scripts/c184_spec_cut.py
"""
import sys
import os
import itertools
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts", "core"))
sys.path.insert(0, HERE)

from fractions import Fraction as Fr
import audit_independent as AI
import c183_minAB as C183

mul, rank = AI.mul, AI.rank


def rref_list(rows):
    return AI.rref(rows)[0]


def in_span(rows, v):
    return rank([list(x) for x in rows] + [list(v)]) == len(rref_list(rows))


def inter(P, Q):
    if not P or not Q:
        return []
    Pp = AI.nullspace(P)
    Qp = AI.nullspace(Q)
    Mx = Pp + Qp
    return AI.nullspace(Mx) if Mx else []


def poly_gcd_deg(rows_poly, h, ncols):
    mins = []
    for rr in itertools.combinations(range(len(rows_poly)), h):
        for cc in itertools.combinations(range(ncols), h):
            v = AI._det_poly([[rows_poly[r][c] for c in cc] for r in rr])
            if any(x != 0 for x in v):
                mins.append(v)
    if not mins:
        return None
    g = mins[0]
    for v in mins[1:]:
        g = AI.pgcd(g, v)
        if len(g) <= 1:
            break
    return len(g) - 1


def cond_8c(Zrows, A, Kbasis):
    n = len(A)
    d = len(Kbasis)
    V = [[Kbasis[j][i] for j in range(d)] for i in range(n)]
    AV = mul(A, V)
    dZ = len(Zrows)
    Z = [[Zrows[j][i] for j in range(dZ)] for i in range(n)]
    rows = []
    for i in range(n):
        row = []
        for j in range(d):
            row.append([-AV[i][j], V[i][j]])
        for j in range(dZ):
            row.append([Z[i][j], Fr(0)])
        rows.append(row)
    h = rank([[V[i][j] for j in range(d)] + [Z[i][j] for j in range(dZ)] for i in range(n)])
    g = poly_gcd_deg(rows, h, d + dZ)
    return g == 0


def main():
    p, n = 3, 4
    subs = [C183.rref([list(v) for v in S], p, n) for S in C183.all_subspaces(p, n)]
    print("子空间数", len(subs))
    rng = random.Random(7)
    stats = {}
    for t in range(12):
        A = [[Fr(rng.randrange(p)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randrange(p)) for _ in range(n)] for _ in range(2)]
        L0 = [[Fr(rng.randrange(p)) for _ in range(n)]]
        CA = mul(C, A)
        K = AI.nullspace(AI.vstack([C, CA]))
        E = AI.nullspace(AI.vstack([C, L0]))
        if not K or not E:
            continue
        EK = inter(E, K)
        feasible = True
        for v in EK:
            Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
            if not in_span(E, Av):
                feasible = False
                break
            if not in_span(EK, Av):
                feasible = False
                break
        d_alg = 0
        d_true = 0
        for Z in subs:
            if rank([list(x) for x in Z] + [list(x) for x in E]) != len(rref_list(E)):
                continue
            ZK = inter(Z, K)
            ok = True
            for v in ZK:
                Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
                if not in_span(Z, Av):
                    ok = False
                    break
            if not ok:
                continue
            d_alg = max(d_alg, len(Z))
            if cond_8c(Z, A, K):
                d_true = max(d_true, len(Z))
        key = (feasible, d_alg, d_true)
        stats[key] = stats.get(key, 0) + 1
    print("(E∩K 可行, d_alg, d_true) -> 计数")
    for k in sorted(stats):
        print("  ", k, stats[k])


if __name__ == "__main__":
    main()
