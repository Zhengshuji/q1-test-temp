"""gap_arithmetic.py —— 检验"阶差"能否由**纯算术量**预测

已知（[docs/02](../../docs/02_theorems_proven.md) B.9 + 整族一致）：

* $(5b)\\Rightarrow h<q+r_1$；故 $h\\ge q+r_1$（Type I）的阶**不可行**；
* 在 $V'\\cap S=0$ 时 $h=s_0+q-r$，于是 Type I $\\iff s_0\\ge r_1+r$（**与 $Z$ 无关**）。

而 $s_0=\\dim(\\operatorname{row}[C;L_0]+W)$，且
$$s_0-(r_1+r)=p-\\dim(\\operatorname{row}L_0\\cap W).$$

**预测**：在 $q_0$ 阶出现阶差（$q_{\\min}>q_0$）$\\iff$ $\\dim(\\operatorname{row}L_0\\cap W)\\le p$
（即 $q_0$ 阶的所有可容许 $Z$ 都是 Type I，因而都被 $(5b)$ 排除）。

本脚本对每个实例算出这些量，与 [witness_scan](witness_scan.py) 的实测阶差对照，统计命中率。

用法：python -u tools/verification/gap_arithmetic.py
"""

import os
import sys
import io
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

DATA = os.path.join(_ROOT, 'workspace', 'augmentation_family', 'data', 'qmin_upper.tsv')


def row_rank(M):
    return LQ.rank([list(x) for x in M])


def inter_dim(rowsA, rowsB):
    """$\\dim(\\operatorname{row}A\\cap\\operatorname{row}B)$（行空间交）。"""
    # dim(A∩B) = rank(A)+rank(B)-rank([A;B])
    ra = row_rank(rowsA)
    rb = row_rank(rowsB)
    rab = row_rank([list(x) for x in rowsA] + [list(x) for x in rowsB])
    return ra + rb - rab


def main():
    if not os.path.exists(DATA):
        print('缺少数据表；先跑 witness_scan.py')
        return
    lines = [l.rstrip('\n').split('\t') for l in io.open(DATA, encoding='utf-8') if l.strip()][1:]
    stat = Counter()
    detail = []
    for r in lines:
        n, p, rr, seed, q0, n0, up, orders, vers, t = r
        n, p, rr, seed, q0 = int(n), int(p), int(rr), int(seed), int(q0)
        made = QR.make_instance(n, p, rr, seed * 17 + p * 7 + rr)
        if made is None:
            continue
        A, C, L0 = made
        CA = LQ.mul(C, A)
        W = [list(x) for x in C] + [list(x) for x in CA]
        r1 = row_rank(W)
        S = [list(x) for x in C] + [list(x) for x in L0] + [list(x) for x in CA]
        s0 = row_rank(S)
        dint = inter_dim([list(x) for x in L0], W)
        # 预测：q0 阶不可行 ⟺ s0 >= r1 + rr ⟺ dint <= p
        pred_gap = (s0 >= r1 + rr)
        obs_gap = None if up == 'None' else (int(up) - q0 > 0)
        if obs_gap is None:
            stat['no_witness'] += 1
            continue
        if pred_gap == obs_gap:
            stat['agree'] += 1
        else:
            stat['disagree'] += 1
            detail.append((n, p, rr, seed, q0, s0, r1, dint, pred_gap, obs_gap))
        if pred_gap:
            stat['pred_gap'] += 1
        if obs_gap:
            stat['obs_gap'] += 1
    print('统计：', dict(stat))
    if detail:
        print('\n不一致的实例：')
        for x in detail:
            print(f'  n={x[0]} p={x[1]} r={x[2]} seed={x[3]} q0={x[4]}：'
                  f's0={x[5]} r1={x[6]} dim(L0∩W)={x[7]} 预测有阶差={x[8]} 实测={x[9]}')
    # 精确混淆矩阵
    print('\n（预测"有阶差"的实例数 / 实测"有阶差"的实例数见上）')


if __name__ == '__main__':
    main()
