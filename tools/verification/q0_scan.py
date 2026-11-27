"""q0_scan.py —— 在**最小阶** $q_0$ 上判定 $(5b)$（Z-参数化；闭包做不到）

闭包会加多行，因此此前无法在 $q_0$ 上检验"$q_{\\min}=q_0$ 吗"。用 Z-参数化
（[z_generator.py](z_generator.py)）可以在任意阶（含 $q_0$）生成候选：

$$\mathcal Z=KW,\\quad W\\in\\operatorname{Gr}(d,\\,n-p-r),\\quad d=n-p-q_0 .$$

对每个功能可观测实例：在 $\\operatorname{Gr}(d,\\,n-p-r)$ 中抽 $\\mathcal Z$，反构 $\\mathcal L$，
先筛 $(5a)$，再判 $(5b)$。

* 若在 $q_0$ 找到 $(5b)$ 见证 ⟹ **$q_{\\min}=q_0$（精确）**；
* 找不到 ⟹ $q_{\\min}>q_0$（只知道下界；不是"$q_{\\min}>q_0$ 的证明"，因为抽样可能漏）。

用法：python -u tools/verification/q0_scan.py
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import z_generator as ZG                  # noqa: E402


def main():
    stats = dict(inst=0, eq_q0=0, gt_q0=0, noalg=0)
    rows = []
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
                    stats['inst'] += 1
                    cands = ZG.sample_L_at_order(A, C, L0, q0, 60, seed * 91 + q0)
                    if not cands:
                        stats['noalg'] += 1
                        rows.append((n, p, r, seed, q0, 0, 0))
                        print(f'  n={n} p={p} r={r} seed={seed} q0={q0}: 未找到代数可行样本（薄集）')
                        continue
                    feas = sum(1 for L in cands if TC.analyse(A, C, L)['five_b'])
                    rows.append((n, p, r, seed, q0, len(cands), feas))
                    if feas:
                        stats['eq_q0'] += 1
                    else:
                        stats['gt_q0'] += 1
                    print(f'  n={n} p={p} r={r} seed={seed} q0={q0}: 代数可行 {len(cands)}，(5b) {feas}'
                          + ('  ⟹ q_min=q0' if feas else '  ⟹ q_min>q0'))
    print(f'\n合计：可观测实例 {stats["inst"]}；q_min=q0（精确）{stats["eq_q0"]}；'
          f'q_min>q0（仅下界）{stats["gt_q0"]}；代数可行样本为空 {stats["noalg"]}')


if __name__ == '__main__':
    main()
