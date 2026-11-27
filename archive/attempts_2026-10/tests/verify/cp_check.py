"""cp_check.py — 压缩引理的判定与验证（Q1-FALSE）

理论（推导见 q1_false/THE_LEMMA.md §4.3）：

  设 V 是解（dim q），K = ker[C;CA]，K0 = row(L0)，J = K^⊥，W = V∩J。
  令 F = { <·, y>|_V : y ∈ K + AK } ⊆ V^*。
  若 K0^⊥ ⊄ F，则 V 有 dim q-1 的解子空间 H = ker f（f ∈ K0^⊥ \\ F）。

  理由：(5a) 自动（H+W=V ⟹ π(H)=π(V) 不变）；
        (5b) 的坏超平面恰是 ker Φ_λ(ξ)，它们都在 F 里，故 f 选在 F 外即可。

用法：
    python q1_false/tests/cp_check.py --inst counterexample_refute_dimV1.json --q 3 --rho 1
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

mul, rank = AI.mul, AI.rank


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def restriction_coords(V, y):
    """f(v)=<v,y> 在基 V 下的坐标向量。"""
    return [dot(row, y) for row in V]


def in_span(vec, basis):
    if not basis:
        return all(x == 0 for x in vec)
    return len(AI.row_basis([list(b) for b in basis] + [list(vec)])) == len(AI.row_basis(basis))


def check_solution_rows(L, A, C, L0):
    """只按行空间判定（不要求字面前缀）：返回 (ok, rho, 明细)。"""
    q = len(L)
    if q < len(L0):
        return False, None, {"why": "too_short"}
    if rank(L) != q:
        return False, None, {"why": "dependent"}
    if rank(L + [r[:] for r in L0]) != q:   # K0 ⊆ V
        return False, None, {"why": "no_K0"}
    CA = mul(C, A)
    LA_ = mul(L, A)
    if rank(AI.vstack([LA_, L, CA, C])) != rank(AI.vstack([L, CA, C])):
        return False, None, {"why": "5a"}
    g = M.cond5b(L, A, C)
    if g != 0:
        return False, None, {"why": f"5b(g={g})"}
    Nv = AI.nullspace(AI.vstack([C, CA]))
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(len(A))]
    rho = rank(mul(L, Nmat)) if Nv else 0
    return True, rho, {"why": "ok"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inst", default="counterexample_refute_dimV1.json")
    ap.add_argument("--q", type=int, default=3)
    ap.add_argument("--rho", type=int, default=1)
    ap.add_argument("--trials", type=int, default=20000)
    args = ap.parse_args()

    path = args.inst if os.path.isabs(args.inst) else os.path.join(ROOT, "lit", args.inst)
    d0 = json.load(open(path, encoding="utf-8"))
    toF = lambda m: [[Fr(x) for x in row] for row in m]
    A, C, L0 = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])
    n = len(A)

    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
    Kbasis = [[Nmat[i][j] for i in range(n)] for j in range(len(Nv))]
    AKbasis = [[sum(A[i][j] * k[j] for j in range(n)) for i in range(n)] for k in Kbasis]

    L, rho = LA.find_solution(A, C, L0, args.q, random.Random(7), args.trials,
                              rho_target=args.rho, Nmat=Nmat)
    if L is None:
        print(f"没找到 q={args.q}, rho={args.rho} 的解")
        return
    V = L
    ok0, rho0_, d0_ = check_solution_rows(V, A, C, L0)
    print(f"解: q={len(V)} rho={rho}  复核={ok0} {d0_}")

    # F（用"在基 V 上的取值"表示）：span{ (<V_i,y>)_i : y ∈ K+AK }
    F = AI.row_basis([restriction_coords(V, y) for y in (Kbasis + AKbasis)])
    # K0 在基 V 下的坐标 c(k0)：解 G c = b，b_i=<V_i,k0>
    import sympy
    G = sympy.Matrix([[dot(V[i], V[j]) for j in range(len(V))] for i in range(len(V))])
    M0 = []
    for k0 in L0:
        b = sympy.Matrix([dot(V[i], k0) for i in range(len(V))])
        c = [Fr(x) for x in G.LUsolve(b)]
        M0.append(c)          # 1×q
    K0perp = AI.nullspace(M0)
    inter = AI.row_basis([x for x in K0perp if in_span(x, F)])
    print(f"dim F={len(F)}  dim K0^⊥={len(K0perp)}  dim(F∩K0^⊥)={len(inter)}")
    cond = len(inter) < len(K0perp)
    print(f"条件 K0^⊥ ⊄ F ： {cond}")

    if not cond:
        print("该构造给不出压缩（不代表一定不可压缩）。")
        return

    f = next(x for x in K0perp if not in_span(x, F))   # f 是"取值向量"
    # H = {v ∈ V : f(v)=0}：系数 c 满足 f·c = 0
    cs = AI.nullspace([list(f)])
    H = AI.row_basis([[sum(c[i] * V[i][t] for i in range(len(V))) for t in range(n)] for c in cs])
    print(f"\n构造 H: dim={len(H)}（期望 {len(V)-1}）")
    ok, rhoH, det = check_solution_rows(H, A, C, L0)
    print(f"  H 是解? {ok}  rho(H)={rhoH}  明细={det}")


if __name__ == "__main__":
    main()
