"""base_quadrics.py —— 构件 3：底座（$n=6,p=r=2$, $q=3$）上不可行条件 = 一组**二次方程**

**设定**：$n=6$、$p=r=2$、$r_1=4$ ⟹ $\\dim V=\\dim K=2$、$V\\cap K=0$（$2p+r=6=n$）；
阶 $q=3$ ⟹ $d=1$（$\\mathcal Z$ 是 $K$ 中的直线，两张图卡）。

**条件（B.13e）**：$\\exists\\lambda:(\\lambda I-A)V=K$。令 $K^{\\perp}$ 为 $K$ 的零化子（$4\\times6$），
$$M_1=K^{\\perp}V,\\qquad M_2=K^{\\perp}AV\\qquad(\\text{都是 }4\\times2),$$
则条件 $\\iff\\exists\\lambda:\\lambda M_1=M_2$，后者等价于：对每一列 $k$，$2\\times2$ 子式
$\\lambda (M_1)_{ik}(M_1)_{jl}-\\dots$ 全为零、且两列给出**同一个** $\\lambda$。逐列消去 $\\lambda$ 后即为
$$M_2[:,k]\\wedge M_1[:,k]=0\\ (\\text{6 个二次式})\\ \\wedge\\ \\lambda_0=\\lambda_1\\ (\\text{一个二次式}).$$
即不可行条件是**一组二次方程**（数据里的二次式），故不可行集是**低次代数集**。

本脚本核验：这组二次方程 $\\iff$ 整族在该阶不可行（用 Toeplitz 逐候选判 $(5b)$）。

用法：python -u tools/verification/base_quadrics.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import observability_test as OT           # noqa: E402  # B.12：快（纯线性代数）
import decide_symbolic as DS              # noqa: E402

F = Fraction


def annihilator(K, n):
    """{y : y^T K = 0} 的基，返回 (n−dimK) × n。"""
    dK = len(K[0]) if (K and K[0]) else 0
    Kt = [[K[i][k] for i in range(n)] for k in range(dK)]
    ns = ZG.ker_cols(Kt)
    d = len(ns[0]) if (ns and ns[0]) else 0
    return [[ns[i][j] for i in range(n)] for j in range(d)]


def quadrics_hold(A, C, L0):
    """检验"∃λ: λM1 = M2"（等价于 2×2 子式全零 + 两列 λ 相同）。返回 (成立?, 说明)。"""
    n = len(A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    if not (V and V[0] and K and K[0]):
        return None, 'V 或 K 为零'
    dV, dK = len(V[0]), len(K[0])
    Kp = annihilator(K, n)
    AV = LQ.mul(A, V)
    M1 = [[sum(Kp[i][j] * V[j][k] for j in range(n)) for k in range(dV)] for i in range(len(Kp))]
    M2 = [[sum(Kp[i][j] * AV[j][k] for j in range(n)) for k in range(dV)] for i in range(len(Kp))]
    # 逐列求 λ（若某列全零则跳过），并核验
    lams = []
    for k in range(dV):
        lam = None
        for i in range(len(M1)):
            if M1[i][k] != 0:
                lam = M2[i][k] / M1[i][k]
                break
        if lam is None:
            if any(M2[i][k] != 0 for i in range(len(M2))):
                return False, f'第 {k} 列：M1 全零但 M2 非零'
            continue
        lams.append(lam)
        # 该列的 2×2 子式
        for i in range(len(M1)):
            for j in range(i + 1, len(M1)):
                if M2[i][k] * M1[j][k] - M2[j][k] * M1[i][k] != 0:
                    return False, f'第 {k} 列的 2×2 子式非零'
    if len(set(lams)) > 1:
        return False, f'两列的 λ 不同：{lams}'
    return True, f'λ={lams[0] if lams else "任何"}'


def family_fails(A, C, L0, q, max_theta=4):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    if not K or not K[0]:
        return None, 0, 0
    k = len(K[0])
    if d <= 0 or d > k:
        return None, 0, 0
    tot = feas = 0
    for rows in itertools.combinations(range(k), d):
        for b in range(max_theta + 1):
            Z = DS.Z_from_theta(A, C, L0, q, rows, [F(b)] * (d * (k - d)))
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            tot += 1
            ok, _ = OT.observability_ok(A, C, L)
            if ok:
                feas += 1
    return (tot > 0 and feas == 0), tot, feas


def main():
    rng = random.Random(20261104)
    st = Counter()
    n, p, r, q = 6, 2, 2, 3
    for trial in range(3000):
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank([list(x) for x in C] + L0) != p + r:
            continue
        CA = LQ.mul(C, A)
        if LQ.rank([list(x) for x in C] + [list(x) for x in CA]) != 4:
            continue
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if len(V[0]) != 2 or len(K[0]) != 2:
            continue
        # V ∩ K = 0 ？⟺ rank[C;CA;L0] = 6
        rows = [list(x) for x in C] + [list(x) for x in CA] + [list(x) for x in L0]
        if LQ.rank(rows) != n:
            st['VcapK_ne0'] += 1
            continue
        quad, why = quadrics_hold(A, C, L0)
        fails, tot, feas = family_fails(A, C, L0, q)
        if quad is None or fails is None:
            continue
        st['tested'] += 1
        if bool(quad) == fails:
            st['agree'] += 1
        else:
            st['disagree'] += 1
            if st['disagree'] <= 6:
                print(f'  不一致：二次方程组={quad}（{why}）整族失败={fails}（候选 {tot}，可行 {feas}）')
    print('统计：', dict(st))
    print('  agree = "二次方程组成立" == "整族不可行"；disagree 应为 0')
    print('  注：n=6,p=r=2,q=3、dim V=dim K=2、V∩K=0 —— 唯一的最小非退化底座')


if __name__ == '__main__':
    main()
