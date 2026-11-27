r"""
c149_real_spectrum.py -- 检验猜想：$q=2$（$\rho=1$）$\iff$ 商映射 $\mathbb{R}^d/S$ 有**实**特征值

理由（$\rho=1$ 时 $\mathcal A=\mathrm{span}\{\alpha_0\}$，(a) 要求）
$$\alpha_0A'=\lambda\,\alpha_0+s,\qquad s\in S .$$
取 $\lambda$ 为**实**数时才有**实**向量 $\alpha_0$。而 $\lambda$ 是 $A'$ 在 $S$ 上的"商映射"
$$\bar A':\ \mathbb{R}^d/S\to\mathbb{R}^d/S$$
的特征值。故：
  * $\bar A'$ 有实特征值 ⟹ 存在实的 $\alpha_0$ ⟹ $q=2$ 有可能；
  * $\bar A'$ 的谱为共轭复对 ⟹ 除 $\alpha_0\in S$（即 $\alpha_0A'\in S$）外无解。

$d=3,\ \dim S=1$ 时商空间是 2 维，$\bar A'$ 可以是"旋转"（复谱）——这正是要找的"必须大"的区域。

脚本：对随机实例分类（实谱 / 复谱），分别测 $q=2$。

跑法：python scripts/core/c149_real_spectrum.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul = AI.mul


def quotient_matrix(S, Ap, d):
    r"""$\bar A'$ 的矩阵（$\mathbb{R}^d/S$ 的一组基下）。
    取 $S$ 的基补成 $\mathbb{R}^d$ 的基，再对补基向量作用 $A'$，模 $S$ 取坐标。"""
    r = len(S)
    # 补基：从标准基里挑，使 [S; e_i ...] 满秩
    comp = []
    for i in range(d):
        e = [Fr(1) if j == i else Fr(0) for j in range(d)]
        if AI.rank(S + comp + [e]) > r + len(comp):
            comp.append(e)
        if len(comp) == d - r: break
    B = S + comp                      # d x d，满秩
    Binv = AI.inv(B)
    out = []
    for e in comp:
        v = mul([e], Ap)[0]
        coef = mul([v], Binv)[0]      # v = coef · B
        out.append([coef[r + k] for k in range(d - r)])
    return out


def has_real_eigen(Mat):
    """2x2 或 1x1 实矩阵是否有实特征值（用判别式，精确有理数）"""
    n = len(Mat)
    if n == 1: return True
    if n == 2:
        tr = Mat[0][0] + Mat[1][1]
        det = Mat[0][0] * Mat[1][1] - Mat[0][1] * Mat[1][0]
        return tr * tr - 4 * det >= 0
    raise NotImplementedError


def test(seed, n=7, p=2):
    rng = random.Random(seed)
    A_ = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
    C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
    if AI.rank(C) < p: return None
    CA = mul(C, A_)
    if AI.rank(AI.vstack([C, CA])) != n - 3: return None
    D0 = AI.build_data(A_, C, [[Fr(1)] + [Fr(0)] * (n - 1)])
    if D0["d"] != 3: return None
    R0 = D0["R0"]
    if AI.rank(R0) != 1: return None
    S = AI.row_basis(R0)
    Q = quotient_matrix(S, D0["Ap"], 3)
    real = has_real_eigen(Q)
    # 用 c148 的思路：K0 = {alpha0 ∈ S : alpha0A' ∈ S}
    s = S[0]
    K0 = [s] if AI.in_span(mul([s], D0["Ap"])[0], S) else []
    ok = False
    if K0:
        al = K0[0]
        NtN = mul(AI.tr(D0["N"]), D0["N"])
        L0 = mul([al], mul(AI.inv(NtN), AI.tr(D0["N"])))
        Dd = AI.build_data(A_, C, L0)
        if not all(x == 0 for x in Dd["alpha0"]):
            w, _ = F.try_A([Dd["alpha0"]], A_, C, L0, Dd, 2, random.Random(seed), n_trials=10)
            ok = w is not None
    return dict(seed=seed, obs=D0["obs"], real=real, k0=bool(K0), q2=ok)


def main():
    print("=" * 80)
    print("d=3, dim S=1：商映射谱型 vs q=2（rho=1）")
    print("=" * 80)
    print(f"{'seed':>5} {'obs':>3} {'实谱':>5} {'K0≠0':>6} {'q=2':>5}")
    stat = {True: [0, 0], False: [0, 0]}   # real -> [n, ok]
    shown = 0
    for seed in range(4000):
        r = test(seed)
        if not r: continue
        stat[r["real"]][0] += 1
        if r["q2"]: stat[r["real"]][1] += 1
        if shown < 14:
            print(f"{r['seed']:>5} {r['obs']:>3} {str(r['real']):>5} {str(r['k0']):>6} {str(r['q2']):>5}")
            shown += 1
        if stat[True][0] + stat[False][0] >= 400: break
    print("-" * 80)
    for k in (True, False):
        n_, ok_ = stat[k]
        print(f"实谱={k}: 实例 {n_}，q=2 成功 {ok_}")
    print("预期：实谱 True 时 q=2 可成；复谱 False 时（除 K0≠0）应为 0。")


if __name__ == "__main__":
    main()
