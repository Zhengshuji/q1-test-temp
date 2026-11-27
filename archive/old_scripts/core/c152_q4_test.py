r"""
c152_q4_test.py -- $q_{\min}$ 停在哪：在 $q=2,3$ 都失败的实例上测 $q=4$（$\rho=3$）

背景：
  * P7 解决 $q=2$（$\rho=1$）；
  * [N](../proof/N_从P7到rho2_2026-10-20.md) §7：$q=3$（$\rho=2$）只救回约 5%；
  * 项目早先 `c89`/`c90` 曾主张 $q_{\min}=\mathrm{obs}+1$（后被 $n{=}7$ 反例否掉）。

本脚本：对 $n{=}5,p{=}1$（$d=3$，故 $\mathrm{obs}+1\le4$）的实例，
  1. 判 P7；2. 对 P7 假者测 $q=3$（$\mathcal A=\mathrm{span}\{\alpha_0,\beta_0\}$）；
  3. 对 $q=3$ 失败者测 $q=4$（$\rho=3$，即 $\mathcal A=\mathbb{R}^3$ —— **无约束**，
     只需 $M$ 的前四行秩 $=3$ 且 (a)(b) 成立）。

$q=4$ 的做法：直接采样 $\ell_2,\ell_3,\ell_4\in\mathbb{R}^n$（$M$ 的行 $=\ell_iN$，
$F$ 的行 $=\ell_iAN$；首行固定），检查
  $$\operatorname{rank}M=3,\qquad \operatorname{row}(F)\subseteq\operatorname{row}(M),\qquad (5b)$$
（(a) 用秩判据：$\operatorname{rank}[M;F]=\operatorname{rank}M$。）

跑法：python scripts/core/c152_q4_test.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F
import c151_rho2_rescue as R2

mul = AI.mul


def try_q4(A_, C, L0, D, rng, n_trials=12):
    """q=4、rho=3：采样 3 个自由行，检查 rank M=3、row(F)⊆row(M)、(5b)"""
    N, AN = D["N"], mul(A_, D["N"])
    n = AI.cols(A_)
    for _ in range(n_trials):
        L = [list(L0[0])] + [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(3)]
        M = mul(L, N); Fm = mul(L, AN)
        if AI.rank(M) != 3: continue
        if AI.rank(M + Fm) != AI.rank(M): continue          # row(F) ⊆ row(M)
        if AI.cond_5a_orig(A_, C, L) and AI.cond_5b_orig(A_, C, L):
            return L
    return None


def main():
    print("=" * 84)
    print("q_min 停在哪：P7 假 → 试 q=3 → 再试 q=4（n=5,p=1，obs+1≤4）")
    print("=" * 84)
    print(f"{'seed':>5} {'obs':>3} {'P7':>5} {'q3':>5} {'q4':>5} {'5a':>4} {'5b':>4}")
    st = dict(inst=0, p7t=0, p7f=0, q3ok=0, q4ok=0, both_fail=0)
    shown = 0
    for seed in range(400):
        rng = random.Random(seed)
        A_, C, L0, D = AI.rand_instance(rng, 5)
        if D["d"] != 3: continue
        al = D["alpha0"]; be = mul(L0, mul(A_, D["N"]))[0]
        st["inst"] += 1
        if R2.p7(A_, C, L0, D):
            st["p7t"] += 1; continue
        st["p7f"] += 1
        if not D["inV"]:      # P1：不可行
            continue
        q3 = None
        if not AI.in_span(be, [al]):
            q3, _ = F.try_A([al, be], A_, C, L0, D, 3, random.Random(seed), n_trials=12)
        if q3 is not None:
            st["q3ok"] += 1; continue
        q4 = try_q4(A_, C, L0, D, random.Random(seed + 3))
        st["q4ok"] += q4 is not None
        st["both_fail"] += q4 is None
        if shown < 14:
            print(f"{seed:>5} {D['obs']:>3} {'False':>5} {str(q3 is not None):>5} "
                  f"{str(q4 is not None):>5} "
                  f"{str(AI.cond_5a_orig(A_,C,q4)) if q4 else '-':>4} "
                  f"{str(AI.cond_5b_orig(A_,C,q4)) if q4 else '-':>4}")
            shown += 1
    print("-" * 84)
    print(f"实例 {st['inst']}：P7 真 {st['p7t']}，P7 假 {st['p7f']}")
    print(f"  q=3 成功 {st['q3ok']}；q=3 失败后 q=4 成功 {st['q4ok']}；q=4 也失败 {st['both_fail']}")


if __name__ == "__main__":
    main()
