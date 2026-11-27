"""c167_probe_tightness.py — 对一个小实例做穷举/半穷举的紧性判定

背景：c166 在 counterexample_refute_dimV1 (n=5) 上发现
    ρ=1 的最小 q 只搜到 3，而层下界 max(r,ρ+1)=2。
n=5、q=2 时 R 只有 5 个坐标，可以在小整数格点上做**穷举**，
以区分"搜索深度不足"与"真缺口"。

用法：
    python c167_probe_tightness.py --inst refute --box 2
"""
import sys
import os
import json
import argparse
import itertools

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "exact_linalg"))
from fractions import Fraction as Fr

import audit_independent as AI
import c162_dimV_formula as M

mul, rank = AI.mul, AI.rank
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load(fn, key="L"):
    d = json.load(open(os.path.join(ROOT, "proof", "refuted", "certificates", fn), encoding="utf-8"))
    toF = lambda m: [[Fr(x) for x in r] for r in m]
    return toF(d["A"]), toF(d["C"]), toF(d["L0"]), toF(d[key]) if key in d else None


def check(L, A, C, L0, quick_only=False):
    n = len(A)
    if L[:len(L0)] != L0:
        return None
    q = len(L)
    if rank(L) != q:
        return None
    CA = mul(C, A)
    LA = mul(L, A)
    if rank(AI.vstack([LA, L, CA, C])) != rank(AI.vstack([L, CA, C])):
        return None
    h = rank(AI.vstack([L, CA, C]))
    for lam in (2, -3, 5, -7, 11, 13, 17, -19):
        rows = [[Fr(lam) * L[i][j] - LA[i][j] for j in range(n)] for i in range(q)] + CA + C
        if rank(rows) != h:
            return None
    if quick_only:
        return True
    g = M.cond5b(L, A, C)
    return True if g == 0 else None


def rho_of(L, A, C):
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    if not Nv:
        return 0
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
    return rank(mul(L, Nmat))


def box_search(A, C, L0, q, box):
    n = len(A)
    hits = []
    total = 0
    rng = range(-box, box + 1)
    for tail in itertools.product(rng, repeat=(q - len(L0)) * n):
        L = [row[:] for row in L0]
        for i in range(q - len(L0)):
            L.append([Fr(tail[i * n + j]) for j in range(n)])
        total += 1
        ok = check(L, A, C, L0)
        if ok:
            hits.append((rho_of(L, A, C), L))
    return hits, total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inst", default="refute")
    ap.add_argument("--box", type=int, default=2)
    ap.add_argument("--qs", default="2")
    args = ap.parse_args()

    if args.inst == "refute":
        A, C, L0, Lc = load("counterexample_refute_dimV1.json", "L")
    elif args.inst == "middle":
        A, C, L0, Lc = load("certificate_middle_layer.json", "L_2row")
    else:
        raise SystemExit("unknown instance")

    n = len(A)
    print(f"instance={args.inst} n={n} p={len(C)} r={len(L0)} box={args.box}")
    D = M.reduced_data(A, C, L0)
    print(f"d={D['d']} dimV={len(D['V'])} rho0={rho_of(L0, A, C)}")
    for q in [int(x) for x in args.qs.split(",")]:
        hits, total = box_search(A, C, L0, q, args.box)
        rhos = sorted(set(h[0] for h in hits))
        print(f"q={q}: 枚举 {total} 个整数矩阵 -> 解 {len(hits)} 个, ρ 取值 {rhos}")
        for rho, L in hits[:3]:
            print("   rho=", rho, "L=", [[str(x) for x in row] for row in L])


if __name__ == "__main__":
    main()
