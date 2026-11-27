"""type3_search.py —— 定向搜索 Type III（猜想 T 的反例）

猜想 T：在 $q=q_0$ 处 $(5b)\\iff h<q_0+r_1$（即最小阶上的失败总是 B.9）。
反例形态：$h<q_0+r_1$ 但 $d_{\\rm fin}>0$（Type III）。

本脚本在 $q_0$ 阶大量生成 Z-参数化候选，**只统计 $h<q_0+r_1$ 的样本**，看其中是否有 $d_{\\rm fin}>0$。

$d_{\\rm fin}$ 用 Toeplitz 零度**快速算**（不算 Smith）：
$$\\nu_s=(s+1)m-\\sum\\varepsilon\\ \\Longrightarrow\\ d_{\\rm fin}=s-(s+1)m+\\nu_s,$$
并在若干样本上与 `toeplitz_criterion.analyse`（含 Smith 交叉核对）比对。

用法：python -u tools/verification/type3_search.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import descriptor_pencil as DP            # noqa: E402
import observer_pencils as OP             # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import z_generator as ZG                  # noqa: E402

F = Fraction


def fast_invariants(A, C, L):
    """返回 (h, s, m, d_fin)；d_fin 由 Toeplitz 零度给出（不算 Smith）。"""
    P0, P1, h = OP.pencil_from_L(A, C, L)
    q, p = len(L), len(C)
    s = LQ.rank(L)
    m = q + 2 * p - h
    Q0m, Q1m, _ = DP.descriptor_pencil(A, C, L)
    E, Fm, B = TC.split_R(Q0m, Q1m, q)
    nus = TC.toeplitz_nullities(E, Fm, B, s)
    sum_eps = (s + 1) * m - nus[s]
    d_fin = s - sum_eps
    assert d_fin >= 0, f'd_fin={d_fin} < 0（Toeplitz 与理论不符）'
    return h, s, m, d_fin


def main():
    checked = 0
    cross = 0
    total_sub = 0          # h < q0+r1 的样本数
    total_iii = 0          # 其中 d_fin > 0 的（Type III）
    per_inst = []
    for n in (5, 6):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3010):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    CA = LQ.mul(C, A)
                    r1 = LQ.rank([x[:] for x in C] + [x[:] for x in CA])
                    sub = iii = 0
                    cands = ZG.sample_L_at_order(A, C, L0, q0, 160, seed * 37 + q0)
                    for L in cands:
                        checked += 1
                        h, s, m, d_fin = fast_invariants(A, C, L)
                        if cross < 8:
                            ref = TC.analyse(A, C, L)
                            assert ref['d_fin'] == d_fin, 'fast d_fin 与 Smith 路径不一致'
                            cross += 1
                        if h < q0 + r1:
                            sub += 1
                            if d_fin > 0:
                                iii += 1
                    total_sub += sub
                    total_iii += iii
                    if sub:
                        per_inst.append(((n, p, r, seed), q0, len(cands), sub, iii))
    print(f'检查铅笔 {checked} 个（其中 {cross} 个与 Smith 路径交叉核对一致）')
    print(f'h < q0+r1 的样本：{total_sub}；其中 d_fin>0（Type III）：{total_iii}')
    if total_iii:
        print('** 找到 Type III ⟹ 猜想 T 被推翻 **')
    else:
        print('样本内没有 Type III ⟹ 与猜想 T 一致（不是证明）')
    print('\n有 h<q0+r1 样本的实例（实例, q0, 样本数, h<.. 数, TypeIII 数）：')
    for row in per_inst[:20]:
        print('  ', row)


if __name__ == '__main__':
    main()
