"""c179_verify_idea5.py — 验证 IDEA5 的核心化归

断言：M = LN = U V^T（rank k），W = A'^T V，LR0 = -U W^T + Y V^T（Y 唯一），
      且 (5b) <=> rank(lam U - Y) = k for all lam。

在 middle_layer 证书上精确验证。
"""
import sys
import os
import itertools
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts", "core"))

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M

mul, tr, rank = AI.mul, AI.tr, AI.rank
inv = AI.inv if hasattr(AI, "inv") else None


def solve_right(B, Vt):
    """解 Y V^T = B，返回 Y（若行空间条件满足），否则 None"""
    # Y = B V (V^T V)^{-1}
    V = tr(Vt)                     # d x k
    VtV = mul(Vt, V)               # k x k
    try:
        VtVinv = AI.inv(VtV)
    except Exception:
        return None
    Y = mul(mul(B, V), VtVinv)
    # 验证
    if mul(Y, Vt) == B:
        return Y
    return None


def gcd_deg(rows_poly, h, ncols):
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


def main():
    d0 = json.load(open(os.path.join(ROOT, "lit", "certificate_middle_layer.json"), encoding="utf-8"))
    toF = lambda m: [[Fr(x) for x in r] for r in m]
    A, C, L0, L = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"]), toF(d0["L_2row"])
    D = M.reduced_data(A, C, L0)
    d, Ap, R0 = D["d"], D["Ap"], D["R0"]
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    N = [[Nv[j][i] for j in range(d)] for i in range(n)]
    Mn = mul(L, N)                 # q x d
    k = rank(Mn)
    print("q =", len(L), " d =", d, " k=rank(M) =", k)
    Vb = AI.row_basis(Mn)          # k rows of length d  (V^T)
    Vt = Vb                        # k x d
    V = tr(Vt)                     # d x k
    # U = M V (V^T V)^{-1}
    VtV = mul(Vt, V)
    U = mul(mul(Mn, V), AI.inv(VtV))
    print("M = U V^T ?", mul(U, Vt) == Mn)
    W = mul(tr(Ap), V)             # d x k,  W = A'^T V
    Np = mul(L, R0)                # q x d
    B = [[Np[i][j] + mul(U, tr(W))[i][j] for j in range(d)] for i in range(len(L))]
    Y = solve_right(B, Vt)
    print("Y 存在（N' = Y V^T - U W^T）?", Y is not None)
    if Y is None:
        return
    # (5b) 与 rank(lam U - Y) = k 比较
    CA = mul(C, A)
    LA = mul(L, A)
    # (5b) gcd
    rows = [[[-LA[i][j], L[i][j]] for j in range(n)] for i in range(len(L))]
    for r in CA:
        rows.append([[r[j], Fr(0)] for j in range(n)])
    for r in C:
        rows.append([[r[j], Fr(0)] for j in range(n)])
    h = rank(AI.vstack([L, CA, C]))
    g5b = gcd_deg(rows, h, n)
    # rank(lam U - Y) 的 gcd：q x k 矩阵，entry = [ -Y , U ]
    rows2 = [[[-Y[i][j], U[i][j]] for j in range(k)] for i in range(len(L))]
    gP = gcd_deg(rows2, k, k)
    print("(5b) gcd 次数 =", g5b, "   铅笔 gcd 次数 =", gP)


if __name__ == "__main__":
    main()
