r"""
c151_rho2_rescue.py -- 在 P7 判据为假（$q=2$ 不可能）的实例上测 $q=3$（$\rho=2$）

问题：$q_{\min}$ 的判定是逐层的。第一层（$\rho\le1$）已由 **P7** 解决。
    那么**第二层**（$\rho\le2$，即 $q\le3$）值不值得攻？
    只有当"P7 为假但 $q=3$ 可行"的实例**大量存在**时才值得。

做法：
  1. 随机 $(A,C)$（$p=1$），筛 $d=3$；
  2. 用 P7 的原判据判 $\rho\le1$ 是否可达；
  3. 对 **P7 为假**的实例：取 $\mathcal A=\mathrm{span}\{\alpha_0,\beta_0\}$（2 维，若 $\beta_0\not\parallel\alpha_0$），
     用线性约束 + 取样判 $q=3$ 是否 liftable；见证用**原始** (5a)/(5b) 复核。

跑法：python scripts/core/c151_rho2_rescue.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul = AI.mul


def p7(A_, C, L0, D):
    r"""P7：$\rho\le1$ 可达 $\iff L_0\in\mathcal S$ 且 $(\ell\mapsto(u,w))$ 像维数 $=2$"""
    N, al, n = D["N"], D["alpha0"], AI.cols(A_)
    AN = mul(A_, N); d = D["d"]
    M = []
    for i in range(d):
        M.append([N[j][i] for j in range(n)] + [-al[i], Fr(0)])
    for i in range(d):
        M.append([AN[j][i] for j in range(n)] + [Fr(0), -al[i]])
    sols = AI.nullspace(M)
    if not sols: return False
    Sb = AI.row_basis([s[:n] for s in sols])
    uw = [s[n:] for s in sols]
    return AI.in_span(list(L0[0]), Sb) and AI.rank(uw) == 2


def run(seed, n=5, p=1):
    rng = random.Random(seed)
    A_, C, L0, D = AI.rand_instance(rng, n)
    if D["d"] != 3: return None
    al = D["alpha0"]
    be = mul(L0, mul(A_, D["N"]))[0]
    crit = p7(A_, C, L0, D)
    out = dict(seed=seed, obs=D["obs"], inV=D["inV"], p7=crit)
    if crit:
        w, _ = F.try_A([al], A_, C, L0, D, 2, random.Random(seed), n_trials=12)
        out["q2"] = w is not None
        return out
    # P7 假：试 rho=2, q=3
    out["q2"] = False
    if AI.in_span(be, [al]):
        out["note"] = "β0∥α0（ρ=1 形状）却 P7 假"
        return out
    Arows = [al, be]
    w, _ = F.try_A(Arows, A_, C, L0, D, 3, random.Random(seed), n_trials=14)
    out["q3"] = w is not None
    if w is not None:
        out["a5"] = AI.cond_5a_orig(A_, C, w)
        out["b5"] = AI.cond_5b_orig(A_, C, w)
    return out


def main():
    print("=" * 84)
    print("P7 为假（q=2 不可能）的实例：q=3（rho=2）能否救回？")
    print("=" * 84)
    print(f"{'seed':>5} {'obs':>3} {'inV':>5} {'P7':>5} {'q3':>5} {'5a':>4} {'5b':>4}")
    stat = dict(p7t=0, p7f=0, q2ok=0, q3ok=0, q3fail=0, feas=0, feas_ok=0)
    shown = 0
    for seed in range(600):
        r = run(seed)
        if r is None: continue
        if r["p7"]:
            stat["p7t"] += 1; stat["q2ok"] += r["q2"]
        else:
            stat["p7f"] += 1
            if r["inV"]:
                stat["feas"] += 1
                stat["feas_ok"] += r.get("q3", False)
            stat["q3ok"] += r.get("q3", False)
            stat["q3fail"] += (not r.get("q3", False))
            if shown < 16:
                print(f"{r['seed']:>5} {r['obs']:>3} {str(r['inV']):>5} {str(r['p7']):>5} "
                      f"{str(r.get('q3')):>5} {str(r.get('a5')):>4} {str(r.get('b5')):>4}")
                shown += 1
    print("-" * 84)
    print(f"P7 真：{stat['p7t']}（其中 q=2 成功 {stat['q2ok']}）")
    print(f"P7 假：{stat['p7f']}（其中 q=3 成功 {stat['q3ok']}，失败 {stat['q3fail']}）")
    print(f"  ├ 其中可行（α0∈V）{stat['feas']} 个，q=3 成功 {stat['feas_ok']}")
    print(f"  └ 不可行（α0∉V）{stat['p7f']-stat['feas']} 个（P1 说必败）")
    print("读法：若 P7 假的实例里 q=3 大量成功 ⟹ rho<=2 这一层值得攻；否则不值得。")


if __name__ == "__main__":
    main()
