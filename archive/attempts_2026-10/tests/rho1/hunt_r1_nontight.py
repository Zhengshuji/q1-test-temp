"""hunt_r1_nontight.py — 搜 r=1 的非紧最小层（Q1-FALSE）

目标实例：r=1、L0 不是解、q=2 精确不可行（D47 判定器）、但存在 q=3,rho=1 的解。
若存在：q_min=3, rho*=1（rho*=0 不可能，因 L0 不是解），修正公式 max(r+delta,rho*+1)=2 被推翻。

判定器 solve_case 是精确的（q=2, rho=1）；q=3, rho=1 用搜索 + c164 复核。
"""
import sys
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))
sys.path.insert(0, HERE)

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA
import c164_trusted_baseline as TB
import rho1_solver as RS

mul, rank = AI.mul, AI.rank


def main():
    rng = random.Random(20251026)
    tried = no2 = found3 = 0
    hits = []
    for t in range(400):
        n = rng.choice([5, 6])
        p = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        if rank(L0) != 1:
            continue
        D = M.reduced_data(A, C, L0)
        if not D["inV"]:
            continue
        l0sol = M.cond5a(L0, A, C) and (M.cond5b(L0, A, C) == 0)
        if l0sol:
            continue                      # 我们要 L0 不是解
        tried += 1
        # 精确判定 q=2, rho=1
        res = RS.solve_case(A, C, L0)
        if res is not None:
            continue                      # q=2 可行 -> 公式没问题
        no2 += 1
        Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
        if not Nv:
            continue
        Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
        L3, rho3 = LA.find_solution(A, C, L0, 3, random.Random(t), 5000, rho_target=1, Nmat=Nmat)
        if L3 is None:
            continue
        ok, det = TB.check_solution(L3, A, C, L0)
        if not ok:
            continue
        found3 += 1
        print(f"[HIT] t={t} n={n} p={p} d={len(Nv)} dimV={len(D['V'])} rho0={rank(mul(L0,Nmat))} 解 rho={rho3}")
        hits.append((t, n, p, A, C, L0, L3))
        if len(hits) >= 3:
            break
    print(f"\n检验 {tried} 个（L0 不是解），其中 q=2 精确不可行 {no2} 个，找到 q=3,rho=1 的 {found3} 个")
    if hits:
        import json
        out = os.path.join(ROOT, "q1_false", "tests", "results")
        os.makedirs(out, exist_ok=True)
        t, n, p, A, C, L0, L3 = hits[0]
        json.dump(dict(A=[[str(x) for x in r] for r in A],
                       C=[[str(x) for x in r] for r in C],
                       L0=[[str(x) for x in r] for r in L0],
                       L=[[str(x) for x in r] for r in L3]),
                  open(os.path.join(out, "r1_nontight_candidate.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("已保存候选 q1_false/tests/results/r1_nontight_candidate.json")


if __name__ == "__main__":
    main()
