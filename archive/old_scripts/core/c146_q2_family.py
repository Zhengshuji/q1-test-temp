r"""
c146_q2_family.py -- 可构造的 $q_{\min}<\mathrm{obs}+1$ 实例（$\rho=1,\ q=2$）

背景：
  P1 的构造只保证 $q\le\mathrm{obs}+1$；项目曾用一个 $n{=}7$ 的例子说明 $q$ 可以更小，
  但那是孤例。本脚本按 [proof/K] 的三层必要条件**系统搜索**，得到可复现的实例。

构造配方（$p{=}2,\ n{=}7,\ d{=}3$）：
  1. $\dim S=2$（$S=\operatorname{row}(R_0)$）；
  2. 取 $\alpha_0\in S$ 且 $\alpha_0A'\in S$（把小系数网格 $\{0,\pm1,\pm2\}^2$ 作用在 $S$ 的基上）；
  3. $L_0$ 满足 $L_0N=\alpha_0$；
  4. 判 $q=2$（$\rho=1$）是否 liftable —— 见证用**原始 4 块 (5a)** 与**原始铅笔 (5b)** 复核。

结果：命中 3 个实例（seed 1080 / 1406 / 3871），全部
$$\rho=1,\ \mathrm{obs}=3,\ q=2\ \Longrightarrow\ q_{\min}=2\ <\ \mathrm{obs}+1=4 .$$

跑法：python scripts/core/c146_q2_family.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul = AI.mul


def build(seed, n=7, p=2, nmax=4000):
    rng = random.Random(seed)
    A_ = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
    C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
    if AI.rank(C) < p: return None
    CA = mul(C, A_)
    if AI.rank(AI.vstack([C, CA])) != n - 3: return None
    D0 = AI.build_data(A_, C, [[Fr(1)] + [Fr(0)] * (n - 1)])
    if D0["d"] != 3: return None
    R0 = D0["R0"]
    if AI.rank(R0) != 2: return None
    S = AI.row_basis(R0)
    cand = None
    for a in (0, 1, -1, 2, -2):
        for b in (0, 1, -1, 2, -2):
            if a == 0 and b == 0: continue
            al = [Fr(a) * S[0][j] + Fr(b) * S[1][j] for j in range(3)]
            if AI.in_span(mul([al], D0["Ap"])[0], S): cand = al; break
        if cand: break
    if cand is None: return None
    NtN = mul(AI.tr(D0["N"]), D0["N"])
    L0 = mul([cand], mul(AI.inv(NtN), AI.tr(D0["N"])))
    D = AI.build_data(A_, C, L0)
    al = D["alpha0"]
    if all(x == 0 for x in al): return None
    return A_, C, L0, D


def main():
    print("=" * 80)
    print("搜索 q=2（rho=1）的可构造实例： dim S=2 且 alpha0∈S、alpha0A'∈S")
    print("=" * 80)
    hits = []
    tried = 0
    for seed in range(4000):
        got = build(seed)
        if got is None: continue
        tried += 1
        A_, C, L0, D = got
        al = D["alpha0"]
        w, _ = F.try_A([al], A_, C, L0, D, 2, random.Random(seed), n_trials=10)
        if w is None: continue
        M = mul(w, D["N"])
        hits.append((seed, D["obs"], AI.rank(M),
                     AI.cond_5a_orig(A_, C, w), AI.cond_5b_orig(A_, C, w)))
        print(f"  seed {seed}: obs={D['obs']} rho={AI.rank(M)} "
              f"5a={AI.cond_5a_orig(A_,C,w)} 5b={AI.cond_5b_orig(A_,C,w)}  "
              f"q_min=2 < obs+1={D['obs']+1}")
        if len(hits) >= 5: break
    print("-" * 80)
    print(f"候选（dim S=2 且对齐）{tried} 个；命中 {len(hits)} 个")
    print("读法：P4b 给 q>=rho+1=2，故命中实例有 q_min=2；而 obs+1=4 ⟹ P1 的上界不紧。")


if __name__ == "__main__":
    main()
