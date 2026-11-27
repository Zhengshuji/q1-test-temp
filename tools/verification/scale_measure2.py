"""scale_measure2.py —— B（修正版）：在**受控的阶**上测结构量，判断编码规模是否多项式

上一版的问题：$q_0$ 随实例大幅变化，$d=n-p-q$ 不可比。本版固定 $q=\\lfloor n/2\\rfloor$
（于是 $d\\approx n/2-p$），$p=r=1$（于是 $r_1=2$、$\\dim V=n-2$ 为典型值），只测**结构量**：

* $\\text{ncols}=\\dim V+d$（$P_{\\mathcal Z}$ 的列数）
* $s=\\min(n,\\text{ncols})$（极大子式尺寸）
* $N=\\binom{n}{s}\\binom{\\text{ncols}}{s}$（极大子式个数）
* $D=\\dim V$（$\\deg_\\lambda$ 上界）
* 图卡数 $\\binom{k}{d}$，层数 $s$

并给出 $N$ 的对数与 $n$ 的关系（判断多项式/指数）。

用法：python -u tools/verification/scale_measure2.py
"""

import os
import sys
from math import comb, log2

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402


def sizes(n, p, r, q, r1=2):
    d = n - p - q
    dimV = n - r1
    ncols = dimV + d
    s = max(1, min(n, ncols))
    N = comb(n, s) * comb(ncols, s) if s <= min(n, ncols) else 0
    k = n - p - r
    charts = comb(k, d) if 0 <= d <= k else 0
    return dict(n=n, q=q, d=d, dimV=dimV, ncols=ncols, s=s, N=N, D=dimV,
                charts=charts, layers=s)


def main():
    p = r = 1
    print('=== 受控阶 $q=\\lfloor n/2\\rfloor$（$p=r=1$，典型 $r_1=2$）===')
    hdr = f'{"n":>3} {"q":>3} {"d":>3} {"ncols":>6} {"s":>3} {"D":>4} {"#图表":>8} {"#层":>4} {"N":>18} {"log2 N":>8} {"log2N/n":>9}'
    print(hdr)
    print('-' * len(hdr))
    prev = None
    for n in (6, 8, 10, 12, 14, 16, 18, 20, 24, 28):
        q = n // 2
        st = sizes(n, p, r, q)
        lg = log2(st['N']) if st['N'] > 0 else float('nan')
        print(f'{n:>3} {q:>3} {st["d"]:>3} {st["ncols"]:>6} {st["s"]:>3} {st["D"]:>4} '
              f'{st["charts"]:>8} {st["layers"]:>4} {st["N"]:>18} {lg:>8.1f} {lg / n:>9.2f}')
        prev = st
    print('\n解读：若 $\\log_2 N/n$ 趋于常数 $>0$，则 $N$ 随 $n$ **指数增长**；')
    print('      若趋于 0，则多项式（或亚指数）。')
    # 与专家 §5.2 的对照
    print('\n=== 结论用数据 ===')
    for n in (10, 20, 28):
        st = sizes(n, p, r, n // 2)
        if st['N'] > 0:
            print(f'  n={n}: N = {st["N"]:.3e}，log2 N = {log2(st["N"]):.1f}，'
                  f'log2 N / n = {log2(st["N"]) / n:.2f}')


if __name__ == '__main__':
    main()
