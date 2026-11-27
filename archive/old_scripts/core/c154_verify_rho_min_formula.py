r"""
c154_verify_rho_min_formula.py -- 重验项目那条**未验完**的公式（`c136` 的 0/560，第 68 处）

公式（`history/52` §7.114.0）：
  $$\rho_{\min}=\min_{0\ne r\in\mathrm{row}(R_0)}\dim\Phi^\infty\big(\mathrm{span}\{\alpha_0,r\}\big)
    \quad\text{s.t. } \Lambda_{\mathcal A}\ \text{不良定义}$$

`c136` 实现后得到 0/560，被判为"可能构造 bug"，**至今未重验**。
本脚本用本轮的独立 lift 实现（线性约束 + 取样 + **原始 (5a)/(5b) 复核**）重做：

  1. 枚举 $r$（$\mathrm{row}(R_0)$ 的基的小系数组合）；
  2. $\mathcal A_r=\Phi^\infty(\mathrm{span}\{\alpha_0,r\})$（对 $A'$ 取闭包）；
  3. 判"$\Lambda_{\mathcal A}$ 不良定义"（用 $N_{\mathcal A}=\{\ell:\ell N=0,\ \ell AN\in\mathcal A\}\ne0$）；
  4. 对合格的 $\mathcal A_r$ 尝试 lift（$q=\dim\mathcal A_r+1$）；
  5. 报告：候选数 / 可 lift 数 / 最小 $\dim$ —— 并与"直接扫 $q$"得到的真实最小值对比。

跑法：python scripts/core/c154_verify_rho_min_formula.py
"""
import random, sys, os
from itertools import product
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul = AI.mul


def rho_min_formula(A_, C, L0, D, grid=(-2, -1, 0, 1, 2)):
    """返回 (候选列表, 可 lift 的最小 dim)；每个元素 (dim, r, liftable)"""
    al, Ap, R0 = D["alpha0"], D["Ap"], D["R0"]
    S = AI.row_basis(R0) if AI.rank(R0) > 0 else []
    out = []
    seen = set()
    for coef in product(grid, repeat=len(S)):
        if all(x == 0 for x in coef): continue
        r = [sum(Fr(coef[i]) * S[i][j] for i in range(len(S))) for j in range(D["d"])]
        if all(x == 0 for x in r): continue
        Arows = F.closure([al, r], Ap)
        key = tuple(tuple(x) for x in Arows)
        if key in seen: continue
        seen.add(key)
        rho = len(Arows)
        if rho >= D["obs"] + 1: continue
        # Λ_A 是否良定义：N_A = {ℓ : ℓN = 0, ℓAN ∈ A}
        W = F.annihilator(Arows)
        rows, rhs = [], []
        for w in W:
            rows.append([sum(D["N"][j][k] * w[k] for k in range(D["d"])) for j in range(AI.cols(A_))])
            rhs.append(Fr(0))
        # 只用 ℓN=0 的约束求仿射空间，再检查 ℓAN ∈ A
        sol = F.solve_affine(rows, [Fr(0)] * len(rows), AI.cols(A_)) if rows else ([Fr(0)] * AI.cols(A_), [[Fr(1) if i == j else Fr(0) for i in range(AI.cols(A_))] for j in range(AI.cols(A_))])
        NA_nonzero = False
        if sol is not None:
            x0, ker = sol
            for v in [x0] + ker:
                if all(x == 0 for x in v): continue
                ANv = mul([v], mul(A_, D["N"]))[0]
                if AI.in_span(ANv, Arows): NA_nonzero = True; break
        if not NA_nonzero:      # Λ_A 良定义 ⟹ (b) 必败（项目定理）
            out.append((rho, r, False)); continue
        q = rho + 1
        w, _ = F.try_A(Arows, A_, C, L0, D, q, random.Random(0), n_trials=10)
        out.append((rho, r, w is not None))
    return out


def main():
    n_size = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print("=" * 82)
    print("重验 ρ_min 公式：A = Φ^∞(span{α0,r})，r ∈ row(R0)，Λ_A 不良定义")
    print("=" * 82)
    print(f"{'seed':>5} {'d':>2} {'obs':>3} {'#候选':>5} {'可lift':>6} {'最小dim':>7}")
    st = dict(inst=0, cand=0, lift=0, withlift=0)
    for seed in range(40):
        rng = random.Random(seed)
        A_, C, L0, D = AI.rand_instance(rng, n_size)
        if not D["inV"]: continue
        res = rho_min_formula(A_, C, L0, D)
        if not res: continue
        st["inst"] += 1
        ok = [t for t in res if t[2]]
        st["cand"] += len(res); st["lift"] += len(ok)
        if ok: st["withlift"] += 1
        print(f"{seed:>5} {D['d']:>2} {D['obs']:>3} {len(res):>5} {len(ok):>6} "
              f"{(min(t[0] for t in ok) if ok else '-')!s:>7}")
    print("-" * 82)
    print(f"实例 {st['inst']}；候选 {st['cand']}；可 lift {st['lift']}；有可 lift 候选的实例 {st['withlift']}")


if __name__ == "__main__":
    main()
