"""failure_types.py —— 把 $q_0$ 阶的失败按专家 §Q1 的三类分类（含对 Type II 的更正）

专家把失败分成三类：
* **Type I**：$h\\ge q+r_1$（B.9）——没有非零左指标，必失败；
* **Type II**：计数不足——由"$\\sum\\varepsilon\\ge$ 非零左指标个数"得必要条件是 $s\\ge k:=q+r_1-h$；
  所以**正确**的判据是 $k>s$ ⟹ 失败（专家原文写"$0<k<s$ ⟹ 失败"，那一步不成立：
  论文的 $\\mathcal L_5$ 有 $k=1<s=5$ 却满足 $(5b)$）；
* **Type III**：$k\\le s$ 且 $h<q+r_1$，但仍然 $d_{\\rm fin}>0$——纯几何障碍，B.9/计数都排除不了。

本脚本对 56 个功能可观测实例在 $q_0$ 阶的样本做分类，报告每类的实例数。

用法：python -u tools/verification/failure_types.py
"""

import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC            # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import z_generator as ZG                  # noqa: E402


def classify(A, C, L):
    res = TC.analyse(A, C, L)
    q, p = len(L), len(C)
    r1 = LQ.rank([r[:] for r in C] + [r[:] for r in LQ.mul(C, A)])
    h, s, d_fin = res['h'], res['s'], res['d_fin']
    k = q + r1 - h
    if res['five_b']:
        return 'ok', dict(q=q, h=h, s=s, r1=r1, k=k, d_fin=d_fin)
    if h >= q + r1:
        return 'I', dict(q=q, h=h, s=s, r1=r1, k=k, d_fin=d_fin)
    if k > s:
        return 'II', dict(q=q, h=h, s=s, r1=r1, k=k, d_fin=d_fin)
    return 'III', dict(q=q, h=h, s=s, r1=r1, k=k, d_fin=d_fin)


def main():
    tally = Counter()
    type_of_instance = {}
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
                    cands = ZG.sample_L_at_order(A, C, L0, q0, 40, seed * 91 + q0)
                    types = Counter()
                    for L in cands:
                        t, info = classify(A, C, L)
                        types[t] += 1
                        tally[t] += 1
                    if cands:
                        type_of_instance[(n, p, r, seed)] = types
    print('样本级分类计数：', dict(tally))
    print('\n按实例（只看有样本的实例）：')
    for key, types in sorted(type_of_instance.items()):
        print(f'  {key}: {dict(types)}')
    nIII = sum(1 for t in type_of_instance.values() if t.get('III', 0) > 0)
    print(f'\n含 Type III 样本的实例数：{nIII}')
    print('注：Type I/II 由整数不变量排除；只有 Type III 需要几何/谱分析。')


if __name__ == '__main__':
    main()
