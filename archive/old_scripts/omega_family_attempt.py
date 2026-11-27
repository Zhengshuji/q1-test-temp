"""omega_family.py —— 只在 $(5a)$-**可行集** $\\Omega^\\star_{A,J}$ 内抽样，再判 $(5b)$

背景：P1 §V 的参数化描述的是**所有最小维候选**；$(5a)$ 是之后附加的条件，其约化形式是
（P1 Lemma 2 + 式 (20)）
$$\\operatorname{rank}\\begin{pmatrix}W_J(\\Theta)\\\\ B_{A,T}\\\\ W_J(\\Theta)\\bar A_T\\end{pmatrix}
=\\operatorname{rank}\\begin{pmatrix}W_J(\\Theta)\\\\ B_{A,T}\\end{pmatrix},\\qquad
\\bar A_T=T^{-1}\\bar A T,\\ \\bar A=M_CAN_C,\\ B_A=CAN_C .$$
等价地存在 $\\Gamma$ 使 $W_J(\\Theta)\\bar A_T=\\Gamma\\,[W_J(\\Theta);\\,B_{A,T}]$。

**固定 $\\Gamma$ 后这是 $\\Theta$ 的线性方程组**，所以可以"抽样 $\\Gamma$ → 解 $\\Theta$"直接得到
$(5a)$-可行的候选（不必在 $\\Theta$ 空间里盲抽）。本脚本用这个办法生成**全部 $(5a)$ 可行**的样本，
再测 $(5b)$。

用法：python tools/verification/omega_family.py
"""

import itertools
import os
import random
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import p1_family as P1F                   # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def reduced_data(fd, A, C):
    """$\\bar A=M_CAN_C$、$B_A=CAN_C$、$\\bar A_T=T^{-1}\\bar A T$、$B_{A,T}=B_AT$。"""
    n = len(A)
    Nc = fd['Nc']
    dC = fd['dC']
    Mc = P1F.left_inverse(Nc, 'Nc')            # dC × n
    MC = LQ.mul(Mc, A)                          # dC × n
    MANC = LQ.mul(MC, Nc)                       # dC × dC
    CANC = LQ.mul(LQ.mul(C, A), Nc)             # p × dC
    T = fd['T']
    Tinv = P1F.left_inverse(T, 'T')             # dC × dC
    AT = LQ.mul(LQ.mul(Tinv, MANC), T)
    BAT = LQ.mul(CANC, T)
    return AT, BAT


def W_of(fd, J, theta, k=None):
    """$W_J(\\Theta)$（$q_0\\times d_C$，变换坐标下）。"""
    k = fd['k'] if k is None else k
    s, r, dC = fd['s'], fd['r'], fd['dC']
    q = r + k
    Y = [[F(0)] * s for _ in range(k)]
    rest = [j for j in range(s) if j not in J]
    for i, j in enumerate(J):
        Y[i][j] = F(1)
    for i in range(k):
        for t, j in enumerate(rest):
            Y[i][j] = theta[i * len(rest) + t]
    W = [[F(0)] * dC for _ in range(q)]
    for i in range(r):
        W[i][i] = F(1)
    for i in range(k):
        for j in range(s):
            W[r + i][r + j] = Y[i][j]
    return W


def solve_theta(fd, AT, BAT, J, Gamma, k=None):
    """固定 $\\Gamma$，解 $W(\\Theta)\\bar A_T=\\Gamma[W(\\Theta);B_{A,T}]$ 得 $\\Theta$（无解返回 None）。"""
    k = fd['k'] if k is None else k
    s, dC, r = fd['s'], fd['dC'], fd['r']
    q = r + k
    m = k * (s - k)
    nrows_B = len(BAT)
    # 未知量：theta[0..m-1]；方程：W AT - Gamma [W; BAT] = 0
    eqs = []
    for i in range(q):
        for j in range(dC):
            row = [F(0)] * (m + 1)
            # W(Θ)AT 的第 (i,j) 项：对每个 theta_t 求偏导
            for t in range(m):
                # theta_t 对应 (i0, j0)：Y[i0][j0] 的元素
                i0, j0 = divmod(t, s - k)
                jcol = [c for c in range(s) if c not in J][j0]
                coef = AT[r + i0][j] if i == r + i0 else F(0)
                # -Gamma[i, r+i0] * W[r+i0][jcol] 的偏导 = -Gamma[i, r+i0]
                coef -= Gamma[i][r + i0] if i == r + i0 else F(0)
                row[t] = coef
            # 常数项
            W0 = W_of(fd, J, [F(0)] * m, k=k)
            const = sum(W0[i][t2] * AT[t2][j] for t2 in range(dC))
            const -= sum(Gamma[i][t2] * W0[t2][j] for t2 in range(q))
            const -= sum(Gamma[i][q + t2] * BAT[t2][j] for t2 in range(nrows_B))
            row[m] = -const
            eqs.append(row)
    R, piv = LQ.rref(eqs)
    for row in R:
        if all(row[t] == 0 for t in range(m)) and row[m] != 0:
            return None
    theta = [F(0)] * m
    for r_i, p in enumerate(piv):
        if p < m:
            theta[p] = R[r_i][m]
    return theta


def main():
    rng = random.Random(20261102)
    print('=== 只在 (5a)-可行集 Ω 内抽样，然后判 (5b) ===')
    tot = dict(inst=0, charts=0, omega=0, five_b=0)
    for n in (5, 6, 7):
        for seed in (1000, 1001, 1002):
            A, C, L0 = make_instance(n, seed)
            try:
                fd = P1F.family_data(A, C, L0)
            except AssertionError as e:
                print(f'  n={n} seed={seed}: 跳过（{e}）')
                continue
            tot['inst'] += 1
            AT, BAT = reduced_data(fd, A, C)
            q0, r, s = fd['q0'], fd['r'], fd['s']
            for q in (q0, q0 + 1, q0 + 2):
                k = q - r
                if k < 0 or k > s:
                    continue
                charts = list(itertools.combinations(range(s), k))
                tot['charts'] += len(charts)
                ok, fb = 0, 0
                for J in charts:
                    for _ in range(6):
                        Gamma = [[F(rng.randrange(-2, 3)) for _ in range(q + len(BAT))] for _ in range(q)]
                        th = solve_theta(fd, AT, BAT, J, Gamma, k=k)
                        if th is None:
                            continue
                        L = P1F.chart_L(fd, J, th, k=k)
                        assert LQ.rank(L) == len(L)
                        assert LQ.rank([row[:] for row in L] + [row[:] for row in L0]) == len(L)
                        assert LQ.condA(A, C, L), '(5a) 应成立（Ω 内点）'
                        ok += 1
                        res = TC.analyse(A, C, L)
                        if res['five_b']:
                            fb += 1
                tot['omega'] += ok
                tot['five_b'] += fb
                print(f'  n={n} seed={seed} q={q} (q0={q0}): Ω 内样本 {ok}，其中 (5b) 成立 {fb}')
    print(f'\n合计：实例 {tot["inst"]}，图卡 {tot["charts"]}，Ω 内样本 {tot["omega"]}，'
          f'其中 (5b) 成立 {tot["five_b"]}')
    print('注：Γ 抽样只覆盖 Ω 的一部分；"没找到 (5b)" 不等于 "不存在"。')


if __name__ == '__main__':
    main()
