"""gap_criterion_check.py —— 复核专家 §10.1 指出的问题：Type I 的充分条件写反了？

专家指出：由 row L0 ⊆ row L，若 row L0 ∩ W 里有非 row C 的向量，则它同时属于 row L ∩ W，
因而 δ ≥ 1、**不是** Type I。所以"dim(row L0 ∩ W) ≤ p ⟹ Type I"方向可疑。

本脚本：对 qmin_upper.tsv 的 89 个实例，算
  d1 = dim(row L0 ∩ W)
  d2 = dim(row L0 ∩ row C)
  d3 = dim((row L0 + row C) ∩ W)      （Type I 要求 d3 = p）
  s0, r1, p
并对以下三个候选判据与"实测有阶差"做列联表：
  A（旧）  d1 ≤ p
  B（专家）row L0 ∩ W = 0   （即 d1 = 0）
  C（推导）d3 = p           （即 (row L0+row C)∩W = row C）

用法：python -u tools/verification/gap_criterion_check.py
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
import qmin_scan_pr as QR                 # noqa: E402

DATA = os.path.join(_ROOT, 'workspace', 'augmentation_family', 'data', 'qmin_upper.tsv')


def inter_dim(A_rows, B_rows):
    ra = LQ.rank([list(x) for x in A_rows])
    rb = LQ.rank([list(x) for x in B_rows])
    rab = LQ.rank([list(x) for x in A_rows] + [list(x) for x in B_rows])
    return ra + rb - rab


def main():
    lines = [l.rstrip('\n').split('\t') for l in io.open(DATA, encoding='utf-8') if l.strip()][1:]
    tab = {k: Counter() for k in ('A', 'B', 'C')}
    rows = []
    for rec in lines:
        n, p, rr, seed, q0, n0, up = (int(rec[0]), int(rec[1]), int(rec[2]), int(rec[3]),
                                      int(rec[4]), int(rec[5]), rec[6])
        made = QR.make_instance(n, p, rr, seed * 17 + p * 7 + rr)
        if made is None:
            continue
        A, C, L0 = made
        O = QR.observability_matrix(A, C)
        if LQ.rank(O + [list(x) for x in L0]) != LQ.rank(O):
            continue
        CA = LQ.mul(C, A)
        W = [list(x) for x in C] + [list(x) for x in CA]
        r1 = LQ.rank(W)
        S = [list(x) for x in C] + [list(x) for x in L0] + [list(x) for x in CA]
        s0 = LQ.rank(S)
        d1 = inter_dim([list(x) for x in L0], W)
        d2 = inter_dim([list(x) for x in L0], [list(x) for x in C])
        d3 = inter_dim([list(x) for x in L0] + [list(x) for x in C], W)
        obs_gap = None if up == 'None' else (int(up) - q0 > 0)
        rows.append((n, p, rr, seed, q0, s0, r1, d1, d2, d3, obs_gap))
        if obs_gap is None:
            continue
        for name, pred in (('A', d1 <= p), ('B', d1 == 0), ('C', d3 == p)):
            tab[name][(pred, obs_gap)] += 1

    print('实例数', len(rows), '；有见证（可判阶差）的', sum(1 for r in rows if r[-1] is not None))
    print('\n列联表：(预测有阶差?, 实测有阶差?) -> 计数')
    for name, label in (('A', 'A: dim(row L0∩W) ≤ p'), ('B', 'B: row L0∩W = 0'),
                        ('C', 'C: (row L0+row C)∩W = row C（即 Type I 的必要条件）')):
        t = tab[name]
        tp, fp = t[(True, True)], t[(True, False)]
        fn, tn = t[(False, True)], t[(False, False)]
        print(f'  {label}: 命中 {tp}, 假阳性 {fp}, 漏 {fn}, 真阴性 {tn}')
    print('\n逐例（d1=dim(L0∩W), d2=dim(L0∩C), d3=dim((L0+C)∩W), p, s0, r1, 实测阶差）：')
    for (n, p, rr, seed, q0, s0, r1, d1, d2, d3, g) in rows[:20]:
        print(f'  n={n} p={p} r={rr} seed={seed}: d1={d1} d2={d2} d3={d3} p={p} '
              f's0={s0} r1={r1} 阶差={g}')


if __name__ == '__main__':
    main()
