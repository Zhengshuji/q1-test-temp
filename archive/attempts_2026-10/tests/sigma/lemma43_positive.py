"""lemma43_positive.py — 给引理 4.3 找数值正例（Q1-FALSE）

目标
----
引理 4.3（THE_LEMMA §4.3）：若 K0^⊥ ⊄ F，则存在超平面 H ⊇ K0，H 是解。

要验证它，需要**非极小**的解 V（极小解往往满足 K0^⊥ ⊆ F）。
构造方式：取极小解 V0，加一行 w ∈ J，使 V' = V0 + span{w} 仍是解：

  (a) w ∈ J                    （保证 rank 不变：wN = 0）
  (b) Aw ∈ V0 + J              （保证 (5a)）
  (c) w ⊥ A(Z),  Z = K ∩ V0^⊥  （保证 (5b) 的核不变）

全部是 w 的线性条件，可直接解空间。

用法：
    python q1_false/tests/lemma43_positive.py --inst counterexample_refute_dimV1.json
"""
import sys
import os
import json
import random
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA

mul, tr, rank = AI.mul, AI.tr, AI.rank


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def at(M_, v):
    """v^T M_"""
    return [sum(v[i] * M_[i][j] for i in range(len(M_))) for j in range(len(M_[0]))]


def check_rows(L, A, C, L0):
    q = len(L)
    if q < len(L0):
        return False, None, "short"
    if rank(L) != q:
        return False, None, "dep"
    if rank(L + [r[:] for r in L0]) != q:
        return False, None, "no_K0"
    CA = mul(C, A)
    if rank(AI.vstack([mul(L, A), L, CA, C])) != rank(AI.vstack([L, CA, C])):
        return False, None, "5a"
    g = M.cond5b(L, A, C)
    if g != 0:
        return False, None, f"5b({g})"
    Nv = AI.nullspace(AI.vstack([C, CA]))
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(len(A))] if Nv else None
    return True, (rank(mul(L, Nmat)) if Nmat else 0), "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inst", default="counterexample_refute_dimV1.json")
    args = ap.parse_args()

    path = args.inst if os.path.isabs(args.inst) else os.path.join(ROOT, "lit", args.inst)
    d0 = json.load(open(path, encoding="utf-8"))
    toF = lambda m: [[Fr(x) for x in row] for row in m]
    A, C, L0 = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])
    n = len(A)

    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    if not Nv:
        print("d=0，跳过")
        return
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
    d = len(Nv)
    Kbasis = [[Nmat[i][j] for i in range(n)] for j in range(d)]   # K 的基（行）

    # 1) 找极小解 V0
    V0 = None
    for q in range(len(L0), n + 1):
        L, rho = LA.find_solution(A, C, L0, q, random.Random(3), 4000, Nmat=Nmat)
        if L is not None:
            V0 = L
            break
    if V0 is None:
        print("没找到极小的解")
        return
    ok, rho0, why = check_rows(V0, A, C, L0)
    print(f"极小解: q={len(V0)} rho={rho0} ok={ok} ({why})")

    # 1b) 推论检验：极小解必须满足 K0^⊥ ⊆ F（否则引理给出更小的解，矛盾）
    AK0 = [[sum(A[i][j] * k[j] for j in range(n)) for i in range(n)] for k in Kbasis]
    F0 = AI.row_basis([restriction(V0, y) for y in (Kbasis + AK0)])
    K0p0 = K0_perp(V0, L0)
    inter0 = AI.row_basis([x for x in K0p0 if in_span(x, F0)])
    print(f"推论检验: dim K0^⊥(V0)={len(K0p0)} dim F(V0)={len(F0)} "
          f"交={len(inter0)}  => 必要条件成立? {len(inter0) == len(K0p0)}")

    # 2) Z = K ∩ V0^⊥（在 K 的坐标下）
    VN = mul(V0, Nmat)                      # q×d
    Zc = AI.nullspace(VN)                   # 坐标
    Z = [[sum(z[j] * Nmat[i][j] for j in range(d)) for i in range(n)] for z in Zc]
    AZ = [[sum(A[i][j] * z[j] for j in range(n)) for i in range(n)] for z in Z]
    AK = [[sum(A[i][j] * k[j] for j in range(n)) for i in range(n)] for k in Kbasis]
    print(f"dim Z = {len(Z)}")

    # 3) U = (V0 + J)^⊥ 的基（约束 Aw ∈ V0+J）
    J = AI.row_basis(mul(C, A) + C)
    V0J = AI.row_basis(V0 + J)
    U = AI.nullspace(V0J)                   # (V0+J)^⊥ 的基
    AZt = [at(A, u) for u in U]             # A^T u

    # 4) 约束：w·k = 0 (k∈K)，w·(Az) = 0，w·(A^T u) = 0
    cons = [list(k) for k in Kbasis] + [list(z) for z in AZ] + [list(x) for x in AZt]
    Wsol = AI.nullspace(cons) if cons else []
    print(f"J 的维数={len(J)}  dim(V0+J)={len(V0J)}  候选 w 空间 dim={len(Wsol)}")

    # 5) 逐个候选 w 试
    for idx, w in enumerate(Wsol):
        if rank(V0 + [w]) == len(V0):
            continue                       # w 已在 V0 里
        V1 = AI.row_basis(V0 + [w])
        ok1, rho1, why1 = check_rows(V1, A, C, L0)
        print(f"  w#{idx}: dim V'={len(V1)} 解? {ok1} rho={rho1} ({why1})")
        if not ok1:
            continue
        # 6) 判据
        F = AI.row_basis([restriction(V1, y) for y in (Kbasis + AK)])
        K0perp = K0_perp(V1, L0)
        inter = AI.row_basis([x for x in K0perp if in_span(x, F)])
        print(f"    dim F={len(F)} dim K0^⊥={len(K0perp)} 交={len(inter)}  条件={len(inter) < len(K0perp)}")
        if len(inter) < len(K0perp):
            f = next(x for x in K0perp if not in_span(x, F))
            cs = AI.nullspace([list(f)])
            H = AI.row_basis([[sum(c[i] * V1[i][t] for i in range(len(V1))) for t in range(n)] for c in cs])
            okH, rhoH, whyH = check_rows(H, A, C, L0)
            print(f"    H: dim={len(H)} 解? {okH} rho={rhoH} ({whyH})")
        break


def restriction(V, y):
    return [dot(row, y) for row in V]


def in_span(vec, basis):
    if not basis:
        return all(x == 0 for x in vec)
    return len(AI.row_basis([list(b) for b in basis] + [list(vec)])) == len(AI.row_basis(basis))


def K0_perp(V, L0):
    """K0^⊥ 在 V 的取值向量表示：解 c·(V k0^T)=0 等价于 f(k0)=0。
    用坐标：c(k0) 满足 V^T ... 这里复用 cp_check 的思路：解 Gram 方程。"""
    import sympy
    q = len(V)
    G = sympy.Matrix([[dot(V[i], V[j]) for j in range(q)] for i in range(q)])
    rows = []
    for k0 in L0:
        b = sympy.Matrix([dot(V[i], k0) for i in range(q)])
        rows.append([Fr(x) for x in G.LUsolve(b)])
    return AI.nullspace(rows)


if __name__ == "__main__":
    main()
