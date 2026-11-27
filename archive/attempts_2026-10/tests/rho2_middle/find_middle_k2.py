"""find_middle_k2.py — 定向搜索"中间层 k=2"实例（Q1-FALSE）

目标：找 (A,C,L0) 使
    dim V = 3,  q(2) = 3（即 q=3 有 rho=2 的解），且 q=2 无解（rho*=2，不是 0/1）。
则 rho* = 2 < dim V = 3，是真正的中间层，且 q_min = rho*+1 = 3 < dim V+1 = 4。

做法：n=7, p=2（使 d=n-rank[C;CA] 可能到 3），随机实例；
      先按 dimV==3 过滤，再查 q=2 是否无解，最后搜 q=3, rho=2。

用法：
    python q1_false/tests/find_middle_k2.py --number 60 --trials 2000 --seed 101
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--number", type=int, default=60)
    ap.add_argument("--trials", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=101)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    found = []
    for t in range(args.number):
        if t % 5 == 0:
            print(f"  ... 已扫 {t}/{args.number}（命中 {len(found)}）", flush=True)
        n = 7
        p = 2
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        if rank(L0) != 1:
            continue
        CA = mul(C, A)
        Nv = AI.nullspace(AI.vstack([C, CA]))
        d = len(Nv)
        if d != 3:
            continue
        Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
        try:
            D = M.reduced_data(A, C, L0)
        except Exception:
            continue
        if len(D["V"]) != 3 or not D["inV"]:
            continue
        # q=2 是否有解（任何 rho）
        L2, _ = LA.find_solution(A, C, L0, 2, random.Random(t), 400, Nmat=Nmat)
        if L2 is not None:
            continue
        # q=3, rho=2
        L3, rho3 = LA.find_solution(A, C, L0, 3, random.Random(t + 7), args.trials,
                                    rho_target=2, Nmat=Nmat)
        if L3 is None:
            continue
        print(f"[hit] t={t} dimV=3 rho={rho3} q=3  (q=2 无解)")
        found.append(dict(t=t, A=[[str(x) for x in r] for r in A],
                          C=[[str(x) for x in r] for r in C],
                          L0=[[str(x) for x in r] for r in L0],
                          L=[[str(x) for x in r] for r in L3]))
        # 复核
        ok, det = LA.is_solution(L3, A, C, L0)
        print(f"   复核: {ok} {det}")
        break

    if found:
        out = os.path.join(ROOT, "q1_false", "tests", "results")
        os.makedirs(out, exist_ok=True)
        path = os.path.join(out, f"middle_k2_seed{args.seed}.json")
        json.dump(found[0], open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"已保存 {path}")
    else:
        print("本轮没找到（可增大 --number / --trials）")


if __name__ == "__main__":
    main()
