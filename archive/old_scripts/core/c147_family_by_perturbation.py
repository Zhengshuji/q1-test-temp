r"""
c147_family_by_perturbation.py -- 命中实例的邻域：$q=2$ 是孤立点还是开集现象？

做法：取 `c146` 的命中实例（seed 1080），对 $(A,C)$ 做单元素 $\pm1$ 扰动，
重新走一遍"找 $\alpha_0\in S$ 且 $\alpha_0A'\in S$ → 取 $L_0$ → 判 $q=2$"的流程。

  * 若大量扰动仍成功 ⟹ 该性质在**开集**上成立 ⟹ "$q_{\min}<\mathrm{obs}+1$"不是孤立现象；
  * 若几乎全部失败 ⟹ 命中的是**薄集**，需要精确构造（闭式族）。

跑法：python scripts/core/c147_family_by_perturbation.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F
import c146_q2_family as Q

mul = AI.mul


def build_from(A_, C, grid=(0, 1, -1, 2, -2)):
    """给定 (A,C)：找 alpha0 ∈ S 且 alpha0A' ∈ S，取 L0N = alpha0。返回 (L0, D) 或 None"""
    n = AI.cols(A_)
    D0 = AI.build_data(A_, C, [[Fr(1)] + [Fr(0)] * (n - 1)])
    if D0["d"] != 3: return None
    R0 = D0["R0"]
    if AI.rank(R0) != 2: return None
    S = AI.row_basis(R0)
    cand = None
    for a in grid:
        for b in grid:
            if a == 0 and b == 0: continue
            al = [Fr(a) * S[0][j] + Fr(b) * S[1][j] for j in range(3)]
            if AI.in_span(mul([al], D0["Ap"])[0], S): cand = al; break
        if cand: break
    if cand is None: return None
    NtN = mul(AI.tr(D0["N"]), D0["N"])
    L0 = mul([cand], mul(AI.inv(NtN), AI.tr(D0["N"])))
    D = AI.build_data(A_, C, L0)
    if all(x == 0 for x in D["alpha0"]): return None
    return L0, D


def test(A_, C, rng_seed=0):
    got = build_from(A_, C)
    if got is None: return None
    L0, D = got
    w, _ = F.try_A([D["alpha0"]], A_, C, L0, D, 2, random.Random(rng_seed), n_trials=10)
    return dict(obs=D["obs"], ok=w is not None,
                a5=AI.cond_5a_orig(A_, C, w) if w else None,
                b5=AI.cond_5b_orig(A_, C, w) if w else None)


def main():
    A0, C0, L00, D0 = Q.build(1080)
    print("=" * 80)
    print("基准实例（seed 1080）与其单元素 ±1 扰动：q=2 是否保持？")
    print("=" * 80)
    base = test(A0, C0)
    print(f"基准: {base}")
    rng = random.Random(0)
    ok = bad = none = 0
    results = []
    for k in range(24):
        A_ = [row[:] for row in A0]
        i, j = rng.randrange(7), rng.randrange(7)
        delta = rng.choice([-1, 1])
        A_[i][j] = A_[i][j] + delta
        r = test(A_, C0, rng_seed=k)
        results.append((i, j, delta, r))
        if r is None: none += 1
        elif r["ok"] and r["a5"] and r["b5"]: ok += 1
        else: bad += 1
    for i, j, d, r in results:
        tag = "—" if r is None else ("OK" if r["ok"] and r["a5"] and r["b5"] else "fail")
        print(f"  A[{i}][{j}] {d:+d}: {tag}" + (f"  (obs={r['obs']})" if r else ""))
    print("-" * 80)
    print(f"扰动 24 个：成功 {ok}，失败 {bad}，无候选 {none}")


if __name__ == "__main__":
    main()
