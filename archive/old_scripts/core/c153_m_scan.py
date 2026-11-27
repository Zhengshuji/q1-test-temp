r"""
c153_m_scan.py -- $\rho=2$ 的自由度只存在于 $\beta_0\parallel\alpha_0$ 的薄集：扫 $m$，看能否救回 P7 假者

逻辑：
  * $\beta_0\not\parallel\alpha_0$ ⟹ 任何含 $\alpha_0,\beta_0$ 的平面只能是 $\mathrm{span}\{\alpha_0,\beta_0\}$
    ⟹ $\rho\le2$ 的判定是**一次检查**（多项式）；
  * $\beta_0\parallel\alpha_0$ ⟹ 平面 $=\mathrm{span}\{\alpha_0,m\}$，$m$ 在 $\mathbb{P}^{d-1}$ 上自由
    ⟹ 只有这一段有真正的搜索。

本脚本：用 `c142` 的构造造出 $\beta_0\parallel\alpha_0$ 的实例，**筛掉 P7 为真的**，
再对剩下的实例扫 $m$，测 $q=3$ 能否成功。

跑法：python scripts/core/c153_m_scan.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from itertools import product

import audit_independent as AI
import c141_invariant_family as F
import c151_rho2_rescue as R2
import c142_rho1_family as R1

mul = AI.mul


def scan_m(A_, C, L0, D, rng, grid=(-1, 0, 1, 2)):
    al = D["alpha0"]
    ok = []
    for coef in product(grid, repeat=3):
        m = [Fr(x) for x in coef]
        if all(x == 0 for x in m): continue
        if AI.rank([al, m]) != 2: continue          # 必须与 alpha0 独立
        w, _ = F.try_A([al, m], A_, C, L0, D, 3, random.Random(0), n_trials=8)
        if w is not None and AI.cond_5a_orig(A_, C, w) and AI.cond_5b_orig(A_, C, w):
            ok.append(coef)
    return ok


def main():
    print("=" * 80)
    print("薄集（β0∥α0）且 P7 假：扫 m ∈ P^{d-1}，q=3 能否救回？")
    print("=" * 80)
    print(f"{'seed':>5} {'d':>2} {'obs':>3} {'P7':>5} {'#m扫':>4} {'#可lift':>7}")
    st = dict(inst=0, p7f=0, rescued=0, none=0)
    shown = 0
    for seed in range(120):
        rng = random.Random(seed)
        try:
            A_, C, L0, D, c = R1.make_instance(rng, n=5)
        except AssertionError:
            continue
        if D["d"] != 3: continue
        st["inst"] += 1
        if R2.p7(A_, C, L0, D):
            continue
        st["p7f"] += 1
        ok = scan_m(A_, C, L0, D, rng)
        st["rescued"] += bool(ok)
        st["none"] += (not ok)
        if shown < 16:
            print(f"{seed:>5} {D['d']:>2} {D['obs']:>3} {'False':>5} {81:>4} {len(ok):>7}")
            shown += 1
    print("-" * 80)
    print(f"实例 {st['inst']}；其中 P7 假 {st['p7f']}；"
          f"扫到可 lift 的 m 的 {st['rescued']}；一个都没有 {st['none']}")


if __name__ == "__main__":
    main()
