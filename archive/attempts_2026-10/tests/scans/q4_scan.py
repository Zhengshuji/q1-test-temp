"""q4_scan.py — Q4 的实例级检验（Q1-FALSE）

取实例 A 的一个 q=3, rho=1 的解 V（它是 W⊆K0 的情形）。
V 内部所有含 K0=row(L0) 的 2 维子空间形如 V' = span{K0, w}，w ∈ V/K0，
即 P^1 上的点 (a:b)。对每个点精确判定 (5a)∧(5b)。

输出：是否存在 V' 是解。用于检验"压缩引理失效时，V 内部是否仍有更小解"。
"""
import sys
import os
import json
import random
import itertools

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA

mul, rank = AI.mul, AI.rank


def main():
    d0 = json.load(open(os.path.join(ROOT, "lit", "counterexample_refute_dimV1.json"), encoding="utf-8"))
    F = lambda m: [[Fr(x) for x in r] for r in m]
    A, C, L0 = F(d0["A"]), F(d0["C"]), F(d0["L0"])
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]

    # 找一个 q=3, rho=1 的解
    V = None
    for seed in range(5):
        L, rho = LA.find_solution(A, C, L0, 3, random.Random(seed), 20000, rho_target=1, Nmat=Nmat)
        if L is not None:
            V = AI.row_basis(L)
            print(f"找到 q=3, rho={rho} 的解（seed {seed}）")
            break
    if V is None:
        print("没找到 q=3, rho=1 的解")
        return
    # V 的基：第一个是 L0（因 L=[L0;*]）
    K0 = L0[0][:]
    others = [row for row in V if rank([row] + [K0]) == 2]
    if len(others) < 2:
        print("V/K0 维数 < 2，无法参数化")
        return
    w1, w2 = others[0], others[1]
    print(f"V dim={len(V)}；参数化 V'=span{{L0, a*w1+b*w2}}，(a:b) ∈ P^1")

    # W ⊆ K0 检查
    J = AI.row_basis(mul(C, A) + C)
    Xp = AI.nullspace(V)
    Yp = AI.nullspace(J)
    W = AI.nullspace(AI.row_basis(Xp + Yp)) if (Xp or Yp) else V
    Wsub = rank([list(r) for r in W] + [K0]) == 1 if W else True
    print(f"dim W={len(W) if W else 0}  W⊆K0? {Wsub}")

    good = []
    tested = 0
    for a, b in itertools.product(range(-6, 7), repeat=2):
        if a == 0 and b == 0:
            continue
        w = [a * w1[t] + b * w2[t] for t in range(n)]
        V2 = AI.row_basis([K0[:], w])
        if len(V2) != 2:
            continue
        tested += 1
        ok, _, det = LA.is_solution([L0[0][:], w], A, C, L0)
        if ok:
            good.append((a, b))
    print(f"扫描 (a:b) 共 {tested} 个，其中是解的: {len(good)} 个 {good[:5]}")


if __name__ == "__main__":
    main()
