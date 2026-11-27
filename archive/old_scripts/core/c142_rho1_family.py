r"""
c142_rho1_family.py -- $\rho=1$ 层：构造 $\beta_0\propto\alpha_0$ 的实例，检验 $q=2$ 是否可 liftable

动机（proof/J）：$\mathcal A=\langle\alpha_0,\beta_0,S\rangle_{A'}$ 这一支只能给 $q=\mathrm{obs}+1$。
  真正能压低 $q$ 的是 $\rho<\mathrm{obs}$。最小的一层是 $\rho=1$：
  $$\rho=1\iff \mathcal A=\mathrm{span}\{\alpha_0\}\iff \beta_0\propto\alpha_0 .$$

构造（关键观察）：
  $$\ell\,(AN-cN)=0\ \text{恒有非零解}\quad(\text{因为 } AN-cN \text{ 是 } n\times d,\ d<n)$$
  取这样的 $\ell$ 作 $L_0=\ell$，则
  $$\alpha_0=L_0N,\qquad \beta_0=L_0AN=c\,\alpha_0\ \Longrightarrow\ \beta_0\propto\alpha_0\ ✓$$

于是 $\rho=1$、$q=2$（$|R|=1$）是**允许的最小配置**（P4b: $\rho\le q-1$）。
本脚本对每个构造的实例，用"线性约束 + 取样 + 原始判据复核"判定 $q=2$ 是否 liftable。

跑法：python scripts/core/c142_rho1_family.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul, tr, rank = AI.mul, AI.tr, AI.rank
cond_5a_orig, cond_5b_orig = AI.cond_5a_orig, AI.cond_5b_orig


def make_instance(rng, n=5, c=None):
    """构造满足 $\beta_0=c\alpha_0$ 的实例（$L_0=\ell$ 取 $\ell(AN-cN)=0$ 的非零解）"""
    while True:
        A_ = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        CA = mul(C, A_)
        try:
            Nc = AI.nullspace(AI.vstack([C, CA]))
        except AssertionError:
            continue
        d = len(Nc)
        if d == 0: continue
        N = [[Nc[j][i] for j in range(d)] for i in range(n)]
        AN = mul(A_, N)
        cc = Fr(c) if c is not None else Fr(rng.randint(-2, 2))
        # ℓ(AN - cN) = 0
        M = [[AN[j][k] - cc * N[j][k] for k in range(d)] for j in range(n)]   # n x d
        sols = AI.nullspace(tr(M))          # 作用在 ℓ 上：M^T ℓ^T = 0
        if not sols: continue
        ell = [s[0] if False else s[i] for i in range(n)] if False else list(sols[0])
        L0 = [ell]
        D = AI.build_data(A_, C, L0)
        if D["d"] == 0 or all(x == 0 for x in D["alpha0"]): continue
        # 校验 β0 = c·α0
        be = mul(L0, mul(A_, N))[0]
        al = D["alpha0"]
        if not AI.in_span(be, [al]): continue
        return A_, C, L0, D, cc


def main():
    print("=" * 82)
    print("ρ=1 层：β0 ∝ α0 的构造实例，检验 q=2（|R|=1）是否 liftable")
    print("=" * 82)
    print(f"{'seed':>4} {'d':>2} {'obs':>3} {'c':>3} {'inV':>5} {'q=2 lift':>8} {'q=3 lift':>8}")
    stats = dict(inst=0, q2=0, q3=0, inV=0)
    for seed in range(24):
        rng = random.Random(seed)
        try:
            A_, C, L0, D, c = make_instance(rng, n=5)
        except AssertionError:
            continue
        al = D["alpha0"]
        Arows = [al]                       # ρ = 1
        wit2, _ = F.try_A(Arows, A_, C, L0, D, 2, random.Random(seed + 7), n_trials=12)
        wit3, _ = F.try_A(Arows, A_, C, L0, D, 3, random.Random(seed + 7), n_trials=12)
        stats["inst"] += 1; stats["q2"] += wit2 is not None; stats["q3"] += wit3 is not None
        stats["inV"] += bool(D["inV"])
        print(f"{seed:>4} {D['d']:>2} {D['obs']:>3} {str(c):>3} {str(D['inV']):>5} "
              f"{str(wit2 is not None):>8} {str(wit3 is not None):>8}")
    print("-" * 82)
    print(f"实例 {stats['inst']}；α0∈V 的 {stats['inV']}；q=2 liftable {stats['q2']}；q=3 liftable {stats['q3']}")
    print("读法：若 q=2 能成功且 obs≥2，则 q=2 < obs+1 ⟹ 击穿 P1 的构造上界。")


if __name__ == "__main__":
    main()
