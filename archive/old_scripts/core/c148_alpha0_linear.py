r"""
c148_alpha0_linear.py -- 把 $\alpha_0$ 的网格搜索换成**解方程**，并统计维数

对 $\mathcal A=\operatorname{span}\{\alpha_0\}$、$\dim S=2$、$d=3$：
$$\alpha_0\in S\ \text{且}\ \alpha_0A'\in S
\iff (a,b)\ \text{满足}\ a\,c_1+b\,c_2=0,$$
其中 $S=\operatorname{span}\{s_1,s_2\}$，$c_i=\det[s_iA';\,s_1;\,s_2]$。

$$\dim\{\alpha_0\}=2\iff c_1=c_2=0\iff S A'\subseteq S\quad(\text{此时整条 }S\text{ 都可用})$$
$$\text{否则}\ \dim=1\quad(\text{只有一个方向})$$

脚本：对每个实例算 $\dim K_0$，取 $\alpha_0\in K_0$，构造 $L_0$ 并判 $q=2$。

跑法：python scripts/core/c148_alpha0_linear.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul = AI.mul


def det3(rows):
    (a, b, c) = rows
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def K0_basis(S, Ap):
    """{alpha0 ∈ span(S) : alpha0 A' ∈ span(S)} 的基（坐标 (a,b) 形式）"""
    s1, s2 = S[0], S[1]
    t1 = mul([s1], Ap)[0]; t2 = mul([s2], Ap)[0]
    c1 = det3([t1, s1, s2]); c2 = det3([t2, s1, s2])
    if c1 == 0 and c2 == 0:
        return [(Fr(1), Fr(0)), (Fr(0), Fr(1))]      # 2 维
    if c1 != 0:
        return [(c2, -c1)]                            # a c1 + b c2 = 0
    return [(Fr(1), Fr(0))]


def build_L0(N, al):
    NtN = mul(AI.tr(N), N)
    return mul([al], mul(AI.inv(NtN), AI.tr(N)))


def test_instance(seed, n=7, p=2):
    rng = random.Random(seed)
    A_ = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
    C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
    if AI.rank(C) < p: return None
    CA = mul(C, A_)
    if AI.rank(AI.vstack([C, CA])) != n - 3: return None
    D0 = AI.build_data(A_, C, [[Fr(1)] + [Fr(0)] * (n - 1)])
    if D0["d"] != 3: return None
    R0 = D0["R0"]
    if AI.rank(R0) != 2: return None
    S = AI.row_basis(R0)
    K0 = K0_basis(S, D0["Ap"])
    results = []
    for (a, b) in K0[:1]:                       # 每个实例取一个方向即可
        al = [a * S[0][j] + b * S[1][j] for j in range(3)]
        if all(x == 0 for x in al): continue
        L0 = build_L0(D0["N"], al)
        # 用 $k\in\ker N$ 的自由度**解出** $\beta_0\parallel\alpha_0$：
        #   (L0+k)R0 = c·alpha0 - alpha0 A'  ,  N^T k = 0
        pre = mul(D0["N"], D0["Ap"])
        base = mul([al], D0["Ap"])[0]
        lr0 = mul(L0, R0)[0]
        rows, rhs = [], []
        for i in range(3):
            rows.append([R0[j][i] for j in range(n)] + [-al[i]])
            rhs.append(-(base[i] + lr0[i]))
        for i in range(3):
            rows.append([D0["N"][j][i] for j in range(n)] + [Fr(0)])
            rhs.append(Fr(0))
        sol = F.solve_affine(rows, rhs, n + 1)
        if sol is not None:
            x0, kerb = sol
            k = x0[:n]
            L0 = [[L0[0][j] + k[j] for j in range(n)]]
        D = AI.build_data(A_, C, L0)
        if all(x == 0 for x in D["alpha0"]): continue
        w, _ = F.try_A([D["alpha0"]], A_, C, L0, D, 2, random.Random(seed), n_trials=10)
        results.append((len(K0), D["obs"], w is not None,
                        AI.cond_5a_orig(A_, C, w) if w else None,
                        AI.cond_5b_orig(A_, C, w) if w else None))
    return results


def main():
    print("=" * 82)
    print("用线性条件定 alpha0：统计 dim K0 与 q=2 的成功率")
    print("=" * 82)
    print(f"{'seed':>5} {'dimK0':>5} {'obs':>3} {'q=2':>5} {'5a':>4} {'5b':>4}")
    stat = {1: [0, 0], 2: [0, 0]}       # dim -> [实例数, 成功数]
    found = 0
    for seed in range(2000):
        r = test_instance(seed)
        if not r: continue
        for (dk, obs, ok, a5, b5) in r:
            stat[dk][0] += 1
            if ok: stat[dk][1] += 1
            if len(stat[1]) and (stat[1][0] + stat[2][0]) <= 12:
                print(f"{seed:>5} {dk:>5} {obs:>3} {str(ok):>5} {str(a5):>4} {str(b5):>4}")
            if ok and obs + 1 > 2: found += 1
        if stat[1][0] + stat[2][0] >= 400: break
    print("-" * 82)
    for dk in (1, 2):
        n_, k_ = stat[dk]
        rate = f"{k_}/{n_}" if n_ else "—"
        print(f"dim K0 = {dk}: 实例 {n_}，q=2 成功 {rate}")
    print(f"其中 q=2 且 obs+1>2（即 q_min<obs+1）的实例累计 {found}")


if __name__ == "__main__":
    main()
