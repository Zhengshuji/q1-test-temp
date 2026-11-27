r"""
c145_construct_with_intersection.py -- 按 $S\cap\mathrm{span}\{\alpha_0\}\ne0$ **正面构造** $\rho=1,q=2$

依据（proof/K §7，已证）：
  $$\rho=1,\ q=2\ \text{可行}\ \Longrightarrow\ S\cap\operatorname{span}\{\alpha_0\}\ne0 .$$
本节反过来按该条件造实例：

  需要 $L_0$ 同时满足
  $$\ell R_0=\sigma\,\ell N\ (\Longrightarrow L_0R_0\in S\cap\mathrm{span}\{\alpha_0\}),\qquad
    \ell NA'=\mu\,\ell N\ (\Longrightarrow \alpha_0A'\parallel\alpha_0)$$
  这两条都是关于 $\ell$ 的**线性**方程（共 $2d$ 条，$n$ 个未知量）。
  对每对 $(\sigma,\mu)$ 解出 $\ell$：若存在非零解且 $\ell N\ne0$，就得到
  $$\alpha_0=\ell N,\quad \beta_0=\ell AN=(\mu+\sigma)\alpha_0\ \ (c=\mu+\sigma),$$
  即 $\rho=1$ 的合格配置。然后测 $q=2$ 是否 liftable。

跑法：python scripts/core/c145_construct_with_intersection.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul, tr, rank = AI.mul, AI.tr, AI.rank


def build_L0(A_, C, D, sigma, mu):
    r"""解 $\ell R_0=\sigma\ell N$、$\ell NA'=\mu\ell N$，返回 $\ell$（或 None）"""
    N, R0, Ap = D["N"], D["R0"], D["Ap"]
    n, d = AI.cols(A_), D["d"]
    pre = mul(N, Ap)                       # n x d = N A'
    rows = []
    for i in range(d):
        rows.append([R0[j][i] - sigma * N[j][i] for j in range(n)])
        rows.append([pre[j][i] - mu * N[j][i] for j in range(n)])
    sols = AI.nullspace(rows)
    for s in sols:
        ell = list(s)
        if all(x == 0 for x in mul([ell], N)[0]): continue
        return ell
    return None


def main():
    print("=" * 88)
    print("正面构造：强制 S∩span{a0}≠0（ℓR0=σℓN）与 α0A'∥α0（ℓNA'=μℓN），再测 q=2")
    print("=" * 88)
    print(f"{'seed':>4} {'d':>2} {'obs':>3} {'(σ,μ)':>9} {'c':>4} {'dimV':>4} {'q=2':>5} {'beat':>5}")
    st = dict(inst=0, built=0, q2=0, beat=0, n_try=0)
    grid = [Fr(a, 2) for a in range(-4, 5)]
    for seed in range(25):
        rng = random.Random(seed)
        # 一般实例（p=2, n=7, d=3）
        while True:
            A_ = [[Fr(rng.randint(-1, 1)) for _ in range(7)] for _ in range(7)]
            C = [[Fr(rng.randint(-1, 1)) for _ in range(7)] for _ in range(2)]
            if rank(C) < 2: continue
            CA = mul(C, A_)
            if rank(AI.vstack([C, CA])) != 4: continue
            break
        # 用任意 L0 先算 (N, A', R0)；它们不依赖 L0
        L0tmp = [[Fr(1)] + [Fr(0)] * 6]
        D = AI.build_data(A_, C, L0tmp)
        if D["d"] != 3: continue
        st["inst"] += 1
        hit = None
        for sigma in grid:
            for mu in grid:
                st["n_try"] += 1
                ell = build_L0(A_, C, D, sigma, mu)
                if ell is None: continue
                L0 = [ell]
                D2 = AI.build_data(A_, C, L0)
                al = D2["alpha0"]
                if all(x == 0 for x in al): continue
                # 验证构造条件
                be = mul(L0, mul(A_, D2["N"]))[0]
                if not AI.in_span(be, [al]): continue
                # S ∩ span{a0}
                S = AI.row_basis(D2["R0"]) if rank(D2["R0"]) > 0 else []
                inter = (len(S) + 1 - AI.rank(AI.vstack([S, [al]]))) if S else 0
                if inter < 1: continue
                w2, _ = F.try_A([al], A_, C, L0, D2, 2, random.Random(seed + 5), n_trials=10)
                q2 = w2 is not None
                beat = q2 and D2["obs"] >= 2
                st["built"] += 1; st["q2"] += q2; st["beat"] += beat
                print(f"{seed:>4} {D2['d']:>2} {D2['obs']:>3} {f'({sigma},{mu})':>9} "
                      f"{str(be[0]/al[0] if al[0]!=0 else '?'):>4} {inter:>4} {str(q2):>5} {str(beat):>5}")
                hit = True
                break
            if hit: break
    print("-" * 88)
    print(f"实例 {st['inst']}；尝试 (σ,μ) 组合 {st['n_try']}；构造成功(含交集) {st['built']}；"
          f"q=2 成功 {st['q2']}；其中 obs≥2（击穿 obs+1）{st['beat']}")


if __name__ == "__main__":
    main()
