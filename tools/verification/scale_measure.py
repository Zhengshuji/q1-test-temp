"""scale_measure.py —— B：**判定代价的结构量随 $n$ 的增长**（专家 §5.2 的"编码规模"问题）

专家指出：$\\exists\\mathbb R$ 成员性取决于**编码规模**，而 Bézout/子式表示的规模由
$$N=\\#\\{\\text{极大子式}\\},\\qquad D=\\max\\deg_\\lambda m_i,\\qquad \\#\\text{图卡}=C(k,d),\\qquad \\#\\text{层}$$
决定，其中 $N=\\binom{n}{s}\\binom{s+d}{s}$（$s=\\dim V+d$）可能**组合爆炸**。

本脚本只**数结构 + 测耗时**（不需要符号消元），目标：
1. 给出 $N,D,\\#\\text{图卡},\\#\\text{层}$ 随 $n$ 的实测增长；
2. 判断"子式表示是否为多项式规模"；
3. 顺带测 $(5b)$ 的三条判据（Toeplitz / gcd / 零空间）在小 $n$ 上的耗时基线。

用法：python -u tools/verification/scale_measure.py
"""

import os
import sys
import time
import itertools
from math import comb
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402


def structure_sizes(A, C, L0, q):
    """数结构量：s、D 上界、图卡数、层数、N。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(K[0])
    CA = LQ.mul(C, A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
    dimV = len(V[0])
    ncols = dimV + d                   # P_Z 的列数
    s = min(n, ncols)                  # 极大子式的尺寸（= 法秩的典型值）
    N = comb(n, s) * comb(ncols, s)    # 极大子式个数
    D = dimV                           # deg_λ 上界
    ncharts = comb(k, d) if 0 <= d <= k else 0
    nlayers = s                        # ρ 的取值个数（1..s）
    return dict(n=n, p=p, r=r, q=q, d=d, k=k, dimV=dimV, ncols=ncols, s=s, N=N, D=D,
                charts=ncharts, layers=nlayers, cols=ncols)


def bench_pencil(A, C, L, reps=1):
    """测三条 $(5b)$ 判据的耗时（取一个候选）。"""
    import toeplitz_criterion as TC
    import spectral_gcd as SG
    t0 = time.time()
    for _ in range(reps):
        TC.analyse(A, C, L)
    t_toe = (time.time() - t0) / reps
    t0 = time.time()
    for _ in range(reps):
        SG.spectral_gcd(A, C, L)
    t_gcd = (time.time() - t0) / reps
    return t_toe, t_gcd


def main():
    print('=== 结构量随 $n$ 的增长（$p=r=1$, $q=q_0$）===')
    hdr = f'{"n":>3} {"p":>2} {"d":>2} {"k":>2} {"s":>3} {"D":>3} {"#图表":>6} {"#层":>4} {"N(子式数)":>14} {"耗时(s)":>8}'
    print(hdr)
    print('-' * len(hdr))
    rows = []
    for n in (5, 6, 7, 8, 9, 10, 12, 14, 16, 20):
        p = 1
        r = 1
        made = QR.make_instance(n, p, r, 4000 + n)
        if made is None:
            # 生成失败时用"典型"参数直接构造：A 随机、C=e_1^T、L0=e_2^T
            continue
        A, C, L0 = made
        O = QR.observability_matrix(A, C)
        if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
            continue
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        for q in sorted({q0, max(q0, n // 2)}):
            try:
                st = structure_sizes(A, C, L0, q)
            except Exception as e:                        # noqa: BLE001
                print(f'{n:>3} q={q} 计算失败：{e}')
                continue
            st['q0'] = q0
            rows.append(st)
            print(f'{st["n"]:>3} {st["p"]:>2} {st["q"]:>3} {st["d"]:>3} {st["k"]:>3} {st["dimV"]:>4} '
                  f'{st["s"]:>4} {st["D"]:>3} {st["charts"]:>6} {st["layers"]:>4} {st["N"]:>16}')

    # 增长律
    print('\n=== 增长率（相邻行之比）===')
    for a, b in zip(rows, rows[1:]):
        if a['N'] > 0:
            print(f'n={a["n"]}→{b["n"]}: N 之比 = {b["N"] / a["N"]:.2f}'
                  f'（{(b["N"] / a["N"]) ** (1 / max(1, b["n"] - a["n"])):.2f} 每步）')


if __name__ == '__main__':
    main()
