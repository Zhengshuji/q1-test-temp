"""type3_bad_lambda.py —— Type III 反例的"坏 λ"定位（不经 Λ 的特征多项式）

对 C4 的反例（$q_0$ 阶、$h<q_0+r_1$、$d_{\\rm fin}>0$），在**有理**候选 $\\lambda$ 上比较
$\\operatorname{rank}Q_{\\mathcal L}(\\lambda)$ 与 $h$，报告秩降的 $\\lambda$。
秩降点即有限初等因子的根，也就是谱障碍发生的位置。

用法：python -u tools/verification/type3_bad_lambda.py
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import type3_structured as T3             # noqa: E402
import importlib.util as iu               # noqa: E402

F = T3.F


def candidates():
    vals = [F(k) for k in range(-6, 7)]
    vals += [F(a, b) for a in range(-9, 10) for b in (2, 3, 4, 5)]
    vals += [F(3, 10), F(3, 5), F(3, 4), F(10, 3), F(5, 3), F(4, 3)]
    return sorted(set(vals))


def main():
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A, C, L0, q0, cands = V4.build()
    CA = LQ.mul(C, A)
    r1 = LQ.rank([x[:] for x in C] + [x[:] for x in CA])
    lam_list = candidates()
    shown = 0
    for L in cands:
        h, s, m, d_fast = T3.fast_dfin(A, C, L)
        if not (h < q0 + r1 and d_fast > 0):
            continue
        LA = LQ.mul(L, A)
        drops = []
        for lam in lam_list:
            Qm = [[lam * L[i][j] - LA[i][j] for j in range(len(A))] for i in range(len(L))]
            Qm = Qm + [list(r) for r in CA] + [list(r) for r in C]
            if LQ.rank(Qm) < h:
                drops.append(lam)
        print(f'=== 反例候选：h={h} s={s} d_fin={d_fast}；秩降的有理 λ = '
              f'{[str(x) for x in drops] if drops else "（无有理 λ）"} ===')
        shown += 1
        if shown >= 3:
            break


if __name__ == '__main__':
    main()
