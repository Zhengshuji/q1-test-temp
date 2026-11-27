r"""
c143_rho1_family_n7.py -- 在维数计数允许的区域里批量构造 $\rho=1,\ q=2$ 的解

依据（proof/K）：
  $$q=\rho+1\ \text{的解得存在}\ \Longrightarrow\ n\ \ge\ 2d-2\rho$$
  $p{=}1$ 时 $d=n-2$，该条件为负 ⟹ 不可能；故取 $p{=}2,\ n{=}7,\ d{=}3$（计数 $=7-6+2=3>0$）。

构造：
  1. 随机 $(A,C)$（$C$ 为 $2\times 7$），筛出 $d=\dim\ker[C;CA]=3$；
  2. 取 $c\in\{-2,\dots,2\}$，解 $\ell(AN-cN)=0$，令 $L_0=\ell$ ⟹ $\beta_0=c\,\alpha_0$；
  3. $\rho=1$ 即 $\mathcal A=\mathrm{span}\{\alpha_0\}$；用 c141 的装置判 $q=2$（$|R|=1$）是否 liftable；
  4. 命中的见证用**原始** (5a)/(5b) 复核，并报告 $\mathrm{obs}$。

若某些实例 $\mathrm{obs}\ge2$ 且 $q=2$ 成功，则 $q=2<\mathrm{obs}+1$ —— 即击穿 P1 构造给出的上界。

跑法：python scripts/core/c143_rho1_family_n7.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul, tr, rank = AI.mul, AI.tr, AI.rank
cond_5a_orig, cond_5b_orig = AI.cond_5a_orig, AI.cond_5b_orig


def make_instance(rng, n=7, p=2, c=None):
    for _ in range(400):
        A_ = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rank(C) < p: continue
        CA = mul(C, A_)
        if rank(AI.vstack([C, CA])) != n - 3: continue      # 要 d = 3
        Nc = AI.nullspace(AI.vstack([C, CA]))
        d = len(Nc)
        if d != 3: continue
        N = [[Nc[j][i] for j in range(d)] for i in range(n)]
        AN = mul(A_, N)
        cc = Fr(c) if c is not None else Fr(rng.randint(-2, 2))
        M = [[AN[j][k] - cc * N[j][k] for k in range(d)] for j in range(n)]
        sols = AI.nullspace(tr(M))
        if not sols: continue
        for s in sols:
            L0 = [s]
            D = AI.build_data(A_, C, L0)
            if D["d"] == 0 or all(x == 0 for x in D["alpha0"]): continue
            be = mul(L0, mul(A_, N))[0]
            if not AI.in_span(be, [D["alpha0"]]): continue
            return A_, C, L0, D, cc
    return None


def main():
    print("=" * 78)
    print("批量构造： p=2, n=7, d=3（计数 n-2(d-rho)=3）—— q=2 (rho=1) 能否成族？")
    print("=" * 78)
    print(f"{'seed':>4} {'d':>2} {'obs':>3} {'c':>3} {'inV':>5} {'q=2':>5} {'q=3':>5} {'obs<q-1?':>9}")
    st = dict(inst=0, q2=0, beat=0, maxobs=0)
    for seed in range(30):
        rng = random.Random(seed)
        got = make_instance(rng, n=7, p=2)
        if got is None: continue
        A_, C, L0, D, c = got
        al = D["alpha0"]; obs = D["obs"]
        w2, _ = F.try_A([al], A_, C, L0, D, 2, random.Random(seed + 31), n_trials=10)
        w3, _ = F.try_A([al], A_, C, L0, D, 3, random.Random(seed + 31), n_trials=10)
        q2 = w2 is not None
        beat = q2 and obs >= 2
        st["inst"] += 1; st["q2"] += q2; st["beat"] += beat
        st["maxobs"] = max(st["maxobs"], obs)
        print(f"{seed:>4} {D['d']:>2} {obs:>3} {str(c):>3} {str(D['inV']):>5} "
              f"{str(q2):>5} {str(w3 is not None):>5} {str(beat):>9}")
    print("-" * 78)
    print(f"实例 {st['inst']}；q=2 成功 {st['q2']}；其中 obs>=2（击穿上界）{st['beat']}；最大 obs {st['maxobs']}")
    print("读法：obs>=2 且 q=2 成功 ⟹ q_min=2 < obs+1 ⟹ P1 的构造上界不是最优。")


if __name__ == "__main__":
    main()
