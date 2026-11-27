"""descent_algorithm.py — 局部下降算法（Q1-FALSE 候选）

算法：
  1. 取一个初始解 V（用 §21 构造，dim = dimV+1；失败则搜索）
  2. while K0^⊥ ⊄ F(V):
        取 f ∈ K0^⊥ \\ F，令 V := ker f（dim 减 1）
  3. 输出 V

由引理 4.3，每一步都是合法压缩（H 是解）；终止时 V 满足 K0^⊥ ⊆ F。

问题：终止点是否是**全局**最小？（refute 实例的局部解可能 ≥ q_min。）
本脚本在实例库上对比：descent 的结果 vs 搜索得到的 q_min。

用法：
    python q1_false/tests/descent_algorithm.py --certs
    python q1_false/tests/descent_algorithm.py --random 6 --seed 31
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


def restriction(V, y):
    return [dot(row, y) for row in V]


def in_span(vec, basis):
    if not basis:
        return all(x == 0 for x in vec)
    return len(AI.row_basis([list(b) for b in basis] + [list(vec)])) == len(AI.row_basis(basis))


def k0_perp(V, L0):
    import sympy
    q = len(V)
    G = sympy.Matrix([[dot(V[i], V[j]) for j in range(q)] for i in range(q)])
    rows = []
    for k0 in L0:
        b = sympy.Matrix([dot(V[i], k0) for i in range(q)])
        rows.append([Fr(x) for x in G.LUsolve(b)])
    return AI.nullspace(rows)


def check_rows(L, A, C, L0):
    q = len(L)
    if q < len(L0) or rank(L) != q:
        return False
    if rank(L + [r[:] for r in L0]) != q:
        return False
    CA = mul(C, A)
    if rank(AI.vstack([mul(L, A), L, CA, C])) != rank(AI.vstack([L, CA, C])):
        return False
    return M.cond5b(L, A, C) == 0


def _intersect(X, Y):
    """行空间交（(X^⊥+Y^⊥)^⊥）。"""
    Xp = AI.nullspace(X) if X else []
    Yp = AI.nullspace(Y) if Y else []
    both = AI.row_basis(Xp + Yp)
    return AI.nullspace(both) if both else X


def _subset(X, Y):
    if not X:
        return True
    return rank([list(r) for r in X] + [list(r) for r in Y]) == rank(Y)


def descend(V, A, C, L0, Kbasis, AK, quiet=True):
    """返回 (V_final, trace)；trace 记录每步的 (dim, dimF, dimK0p, dimInter)。

    守卫（引理 4.3 的缺口）：若 W = V∩J ⊆ K0，则任何含 K0 的超平面都含 W，
    从而 H+W = H ≠ V，$(5a)$ 不再自动 —— 此时超平面压缩不存在，直接停。
    """
    trace = []
    n = len(A)
    J = AI.row_basis(mul(C, A) + C)
    while True:
        F = AI.row_basis([restriction(V, y) for y in (Kbasis + AK)])
        K0p = k0_perp(V, L0)
        inter = AI.row_basis([x for x in K0p if in_span(x, F)])
        W = _intersect(V, J)
        trace.append((len(V), len(F), len(K0p), len(inter), len(W), _subset(W, L0)))
        if len(inter) == len(K0p):
            return V, trace
        if _subset(W, L0):
            # 可容许超平面为空：超平面压缩不存在（引理 4.3 的缺口）
            trace.append(("NO_ADMISSIBLE", len(V)))
            return V, trace
        f = next(x for x in K0p if not in_span(x, F))
        cs = AI.nullspace([list(f)])
        if not cs or len(cs) != len(V) - 1:
            return V, trace
        V2 = AI.row_basis([[sum(c[i] * V[i][t] for i in range(len(V))) for t in range(n)] for c in cs])
        if len(V2) != len(V) - 1:
            return V, trace
        if not check_rows(V2, A, C, L0):
            trace.append(("FAIL", len(V2)))
            return V, trace
        V = V2


def run_one(name, A, C, L0, trials=400):
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    if not Nv:
        return None
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
    Kbasis = [[Nmat[i][j] for i in range(n)] for j in range(len(Nv))]
    AK = [[sum(A[i][j] * k[j] for j in range(n)) for i in range(n)] for k in Kbasis]

    D = M.reduced_data(A, C, L0)
    if not D["inV"]:
        return None

    # 初始解：先试构造 q=dimV+1，再退回搜索
    V0 = None
    rng = random.Random(11)
    for t in range(trials):
        L = [row[:] for row in L0]
        while len(L) < len(D["V"]) + 1:
            row = [Fr(rng.randint(-2, 2)) for _ in range(n)]
            if any(x != 0 for x in row):
                L.append(row)
        if rank(L) == len(L) and check_rows(L, A, C, L0):
            V0 = L
            break
    if V0 is None:
        for q in range(len(L0), n + 1):
            L, _ = LA.find_solution(A, C, L0, q, rng, trials, Nmat=Nmat)
            if L is not None:
                V0 = L
                break
    if V0 is None:
        return dict(name=name, ok=False)

    Vd, trace = descend(V0, A, C, L0, Kbasis, AK)
    short = []
    for t in trace:
        if isinstance(t[0], str):
            short.append(t)
        else:
            short.append((t[0], t[3], t[2], t[5]))   # (dim, dimInter, dimK0p, W⊆K0?)
    print(f"{name:24s} 初始 q={len(V0)} -> 下降 q={len(Vd)}  迹(dim,∩,K0⊥,W⊆K0)={short}")
    return dict(name=name, start=len(V0), end=len(Vd), trace=trace)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--certs", action="store_true")
    ap.add_argument("--random", type=int, default=0)
    ap.add_argument("--seed", type=int, default=31)
    ap.add_argument("--r", default="1")
    args = ap.parse_args()

    toF = lambda m: [[Fr(x) for x in row] for row in m]
    insts = []
    if args.certs or args.random == 0:
        for fn, key in [("counterexample_refute_dimV1.json", "L"),
                        ("certificate_middle_layer.json", "L_2row"),
                        ("certificate_rhostar_lt_dimV.json", None),
                        ("counterexample_candidate.json", "L"),
                        ("counterexample_d4.json", "L")]:
            d0 = json.load(open(os.path.join(ROOT, "lit", fn), encoding="utf-8"))
            insts.append((fn[:-5], toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])))
    if args.random:
        r = tuple(int(x) for x in args.r.split(","))
        insts += LA.random_instances(args.random, args.seed, r_choices=r)

    for name, A, C, L0 in insts:
        try:
            run_one(name, A, C, L0)
        except Exception as e:
            print(f"{name}: ERR {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
