"""c176_verify_fernando_8c.py — 独立验证 (5b) <=> (8c)

(5b): rank[lam L - LA; CA; C] == rank[L; CA; C]  for all lam
(8c): rank[(lam I - A)V  Z] == rank[V  Z]        for all lam
      其中 Z = ker[C;L], V 是 K = ker[C;CA] 的基。

随机生成 (A,C,L)，用精确子式 gcd 判两个条件，比较布尔值。

用法：python q1_true/scripts/c176_verify_fernando_8c.py
"""
import sys
import os
import itertools
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts", "core"))

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M

mul, rank = AI.mul, AI.rank


def gcd_degree_of_pencil(rows_poly, h, ncols):
    """rows_poly: list of rows, each row = list of [const, coeff] over ncols columns.
       返回 gcd 的次数（0 表示条件成立）。"""
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


def cond_5b(L, A, C):
    n = len(A)
    CA = mul(C, A)
    LA = mul(L, A)
    rows = [[[-LA[i][j], L[i][j]] for j in range(n)] for i in range(len(L))]
    for r in CA:
        rows.append([[r[j], Fr(0)] for j in range(n)])
    for r in C:
        rows.append([[r[j], Fr(0)] for j in range(n)])
    h = rank(AI.vstack([L, CA, C]))
    return gcd_degree_of_pencil(rows, h, n) == 0


def cond_8c(L, A, C):
    n = len(A)
    CA = mul(C, A)
    K = AI.nullspace(AI.vstack([C, CA]))
    if not K:
        return None
    V = [[K[j][i] for j in range(len(K))] for i in range(n)]     # n x (n-r1)
    Zv = AI.nullspace(AI.vstack([C, L]))
    Z = [[Zv[j][i] for j in range(len(Zv))] for i in range(n)]   # n x d
    AV = mul(A, V)
    nv, nz = len(K), len(Zv)
    # 行：n 个；列：nv + nz
    rows = []
    for i in range(n):
        row = []
        for j in range(nv):
            row.append([-AV[i][j], V[i][j]])      # (lam I - A)V
        for j in range(nz):
            row.append([Z[i][j], Fr(0)])          # Z
        rows.append(row)
    h = rank([[V[i][j] for j in range(nv)] + [Z[i][j] for j in range(nz)] for i in range(n)])
    return gcd_degree_of_pencil(rows, h, nv + nz) == 0


def main():
    rng = random.Random(5)
    n = 5
    agree = 0
    total = 0
    for trial in range(60):
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        p = 2
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        q = rng.choice([2, 3])
        L = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(q)]
        if rank(L) != q:
            continue
        b5 = cond_5b(L, A, C)
        b8 = cond_8c(L, A, C)
        if b8 is None:
            continue
        total += 1
        if b5 == b8:
            agree += 1
        else:
            print("不一致 trial", trial, "5b=", b5, "8c=", b8)
    print("比较", total, "个随机 (A,C,L)；5b 与 8c 一致:", agree)


if __name__ == "__main__":
    main()
