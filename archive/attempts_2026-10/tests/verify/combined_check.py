"""combined_check.py — q=2 精确 + q=3,rho=1 精确，交叉判定（Q1-FALSE）

反例条件：
  (a) L0 不是解（=> q>=r+1=2 不够，需 q>=2 且 q=1 不可能）；
  (b) q=2 精确不可行（D47 判定器）；
  (c) q=3,rho=1 精确可达（exact_r1_q3）。
若三者同时成立：q_min=3, rho*=1，修正公式 max(r+delta, rho*+1)=2 被推翻。
"""
import sys
import os
import random
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))
sys.path.insert(0, HERE)

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c164_trusted_baseline as TB
import rho1_solver as RS
import exact_r1_q3 as E3

mul, rank = AI.mul, AI.rank


def main():
    rng = random.Random(20251026)
    n_inst = n_no2 = n_reach = n_hit = 0
    for t in range(200):
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
        if M.cond5a(L0, A, C) and (M.cond5b(L0, A, C) == 0):
            continue
        n_inst += 1
        sol2 = RS.solve_case(A, C, L0)
        no2 = sol2 is None
        if no2:
            n_no2 += 1
        try:
            r3 = E3.check_instance(A, C, L0)
        except Exception:
            r3 = "ERR"
        reach = (r3 == "reachable")
        if reach:
            n_reach += 1
        if no2 and reach:
            n_hit += 1
            print(f"[COUNTEREXAMPLE CANDIDATE] t={t} n={n} p={p}")
            out = os.path.join(ROOT, "q1_false", "tests", "results")
            os.makedirs(out, exist_ok=True)
            json.dump(dict(A=[[str(x) for x in r] for r in A],
                           C=[[str(x) for x in r] for r in C],
                           L0=[[str(x) for x in r] for r in L0]),
                      open(os.path.join(out, "candidate_r1_nontight.json"), "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
            if n_hit >= 2:
                break
    print(f"\n实例 {n_inst}；q=2 不可行 {n_no2}；q=3,rho=1 可达 {n_reach}；两者同时 {n_hit}")


if __name__ == "__main__":
    main()
