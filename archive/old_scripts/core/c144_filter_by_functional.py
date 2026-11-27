r"""
c144_filter_by_functional.py -- 按"功能泛函不恒零"筛实例，再测 $q=2$

依据（proof/K §6）：
  $\rho=1$、$q=2$ 时两行必须对一切 $\lambda$ 成比例；写成 $\ell N=t\alpha_0,\ \ell AN=\mu\alpha_0$，
  $\beta_0=c\alpha_0$，则
  $$\text{row}_1=(\lambda-c)\alpha_0,\qquad \text{row}_2=(\lambda t-\mu)\alpha_0$$
  $$\Longrightarrow\ \textbf{需要}\ \exists\,\ell\in V_{\mathcal A}:\ \ell AN-c\,\ell N\ne0\quad(\text{即 }\mu\ne ct)$$
  否则铅笔在 $\lambda=c$ 处整行为 $0$，(b) 必败。

本脚本：
  1. 随机 $(A,C)$（$p=2,n=7$，筛 $d=3$）；
  2. 对每个 $c$，取 $L_0\in\ker(AN-cN)$（⟹ $\beta_0=c\alpha_0$）；
  3. **先判**：功能泛函 $\ell\mapsto\ell(AN-cN)$ 在 $V_{\mathcal A}$ 上是否恒零；
  4. 只用"不恒零"的实例去试 $q=2$；报告命中率与 $\mathrm{obs}$。

跑法：python scripts/core/c144_filter_by_functional.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F
import c143_rho1_family_n7 as R

mul, tr, rank = AI.mul, AI.tr, AI.rank


def V_A_basis(Arows, A_, D):
    """$V_{\mathcal A}=\{\ell:\ell N\in\mathcal A,\ \ell AN\in\mathcal A\}$ 的基"""
    N, AN = D["N"], mul(A_, D["N"])
    d = D["d"]; n = AI.cols(A_)
    W = F.annihilator(Arows)
    rows = []
    for w in W:
        rows.append([sum(N[j][k] * w[k] for k in range(d)) for j in range(n)])
        rows.append([sum(AN[j][k] * w[k] for k in range(d)) for j in range(n)])
    if not rows:  # A = R^d
        return [[Fr(1) if i == j else Fr(0) for i in range(n)] for j in range(n)]
    sol = F.solve_affine(rows, [Fr(0)] * len(rows), n)
    if sol is None: return []
    x0, ker = sol
    return ker


def main():
    print("=" * 86)
    print("按功能泛函筛实例： ∃ℓ∈V_A 使 ℓAN - cℓN ≠ 0 ?  —— 再测 q=2")
    print("=" * 86)
    print(f"{'seed':>4} {'d':>2} {'obs':>3} {'c':>3} {'dimVA':>5} {'泛函非零':>7} {'q=2':>5} {'beat':>5}")
    st = dict(inst=0, pass_f=0, q2=0, beat=0, fail_f=0, q2_when_fail=0)
    for seed in range(40):
        rng = random.Random(seed)
        got = R.make_instance(rng, n=7, p=2)
        if got is None: continue
        A_, C, L0, D, c = got
        al = D["alpha0"]
        Vb = V_A_basis([al], A_, D)
        AN = mul(A_, D["N"]); N = D["N"]
        # 功能泛函在 V 上是否恒零
        nonzero = any(any(x != 0 for x in mul([v], [[AN[j][k] - c * N[j][k] for k in range(D["d"])] for j in range(7)])[0])
                      for v in Vb)
        w2, _ = F.try_A([al], A_, C, L0, D, 2, random.Random(seed + 77), n_trials=10)
        q2 = w2 is not None
        beat = q2 and D["obs"] >= 2
        st["inst"] += 1
        if nonzero: st["pass_f"] += 1; st["q2"] += q2; st["beat"] += beat
        else: st["fail_f"] += 1; st["q2_when_fail"] += q2
        print(f"{seed:>4} {D['d']:>2} {D['obs']:>3} {str(c):>3} {len(Vb):>5} {str(nonzero):>7} "
              f"{str(q2):>5} {str(beat):>5}")
    print("-" * 86)
    print(f"实例 {st['inst']}；泛函非零 {st['pass_f']}（其中 q=2 成功 {st['q2']}，击穿 obs+1 的 {st['beat']}）")
    print(f"        泛函恒零 {st['fail_f']}（其中 q=2 成功 {st['q2_when_fail']}）")


if __name__ == "__main__":
    main()
