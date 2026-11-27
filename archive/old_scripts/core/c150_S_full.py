r"""
c150_S_full.py -- $S=\mathbb{R}^d$（$R_0$ 满秩）区：$q=2$ 是否同样普遍？

此时 $S=\mathbb{R}^d$，故
  * $K_0=\{\alpha_0:\alpha_0A'\in S\}=\mathbb{R}^d$ —— **任何** $\alpha_0$ 都合格；
  * 但 $\beta_0=\alpha_0A'+L_0R_0$ 仍须 $\parallel\alpha_0$，用 $k\in\ker N$ 解：
    $$(L_0+k)R_0=c\,\alpha_0-\alpha_0A',\qquad N^{\mathsf T}k=0 .$$

若这一区也 $q=2$ 普遍成立，则"$q_{\min}=2$ 普遍"被钉死，唯一悬念就是 $\dim S$ 小的对抗性区域。

跑法：python scripts/core/c150_S_full.py            # 默认 d=3 (n=7,p=2)
      python scripts/core/c150_S_full.py 4          # d=4 (n=8,p=2)
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul = AI.mul


def build_L0(N, al):
    NtN = mul(AI.tr(N), N)
    return mul([al], mul(AI.inv(NtN), AI.tr(N)))


def solve_k(A_, C, D, al, L0, n):
    """$(L_0+k)R_0=c\\alpha_0-\\alpha_0A'$，$N^{\\mathsf T}k=0$"""
    R0, N, Ap = D["R0"], D["N"], D["Ap"]
    d = D["d"]
    base = mul([al], Ap)[0]
    lr0 = mul(L0, R0)[0]
    rows, rhs = [], []
    for i in range(d):
        rows.append([R0[j][i] for j in range(n)] + [-al[i]])
        rhs.append(-(base[i] + lr0[i]))
    for i in range(d):
        rows.append([N[j][i] for j in range(n)] + [Fr(0)])
        rhs.append(Fr(0))
    return F.solve_affine(rows, rhs, n + 1)


def run(seed, n, p, d_target):
    rng = random.Random(seed)
    A_ = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
    C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
    if AI.rank(C) < p: return None
    if AI.rank(AI.vstack([C, mul(C, A_)])) != n - d_target: return None
    D0 = AI.build_data(A_, C, [[Fr(1)] + [Fr(0)] * (n - 1)])
    if D0["d"] != d_target: return None
    if AI.rank(D0["R0"]) != d_target: return None        # S = R^d
    al = [Fr(1)] + [Fr(0)] * (d_target - 1)
    L0 = build_L0(D0["N"], al)
    sol = solve_k(A_, C, D0, al, L0, n)
    if sol is None: return dict(seed=seed, ok=None, obs=D0["obs"], reason="k-系统不相容")
    x0, kers = sol
    k = x0[:n]
    L0 = [[L0[0][j] + k[j] for j in range(n)]]
    D = AI.build_data(A_, C, L0)
    if all(x == 0 for x in D["alpha0"]): return None
    w, _ = F.try_A([D["alpha0"]], A_, C, L0, D, 2, random.Random(seed), n_trials=12)
    return dict(seed=seed, ok=w is not None, obs=D0["obs"],
                a5=AI.cond_5a_orig(A_, C, w) if w else None,
                b5=AI.cond_5b_orig(A_, C, w) if w else None)


def main():
    d_target = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    n = d_target + 4
    p = 2
    print("=" * 78)
    print(f"S = R^d 区：d={d_target}, n={n}, p={p} —— q=2 (rho=1) 是否普遍？")
    print("=" * 78)
    print(f"{'seed':>5} {'obs':>3} {'q=2':>5} {'5a':>4} {'5b':>4} {'备注'}")
    stat = dict(n=0, ok=0, fail=0, no=0)
    shown = 0
    for seed in range(3000):
        r = run(seed, n, p, d_target)
        if r is None: continue
        stat["n"] += 1
        if r["ok"] is None: stat["no"] += 1
        elif r["ok"]: stat["ok"] += 1
        else: stat["fail"] += 1
        if shown < 12:
            print(f"{r['seed']:>5} {r['obs']:>3} {str(r.get('ok')):>5} "
                  f"{str(r.get('a5')):>4} {str(r.get('b5')):>4} {r.get('reason','')}")
            shown += 1
        if stat["n"] >= 120: break
    print("-" * 78)
    print(f"实例 {stat['n']}：q=2 成功 {stat['ok']}，失败 {stat['fail']}，k-系统不相容 {stat['no']}")


if __name__ == "__main__":
    main()
