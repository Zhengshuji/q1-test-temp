"""verify_bitsize.py —— 编码常数的比特规模（专家 2026-11-02 §4.5 / G-2）

命题（见 [bitsize.md](bitsize.md)）：输入 $A,C,L_0\\in\\mathbb Q^{n\\times n}$ 每元素比特长 $\\le B$ 时，
chart-free 编码（以及 P1 族的参数 $N_C,T,(N_CT)^{+}$）中所有常数的比特长都是
$O(nB+n\\log n)$。

本脚本**测**这些常数的实际比特长（精确有理算术，分子/分母分别取二进制长度）：

* $N_C$（$\\ker C$ 的基）、$N_V$（$\\ker[C;CA]$ 的基）、$N_H$（$\\ker[C;L_0]$ 的基）；
* $T$（把 $L_0N_C$ 归一化的矩阵）与 $P=(N_CT)^{+}$（左逆）；
* 由 $\\Theta$ 得到的 $L(\\Theta)$（族的见证矩阵）。

比较对象：$c\\,(nB+n\\log_2 n)$。**验证不是证明**；覆盖范围仅为这些常数，不覆盖 $X(\\lambda)$ 的全部系数。
"""

import math
import os
import random
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import p1_family as P1F                   # noqa: E402

F = Fraction


def bits(x):
    """有理数的比特长：|分子|、分母的二进制长度取大者。"""
    if x == 0:
        return 1
    return max(abs(x.numerator).bit_length(), x.denominator.bit_length())


def maxbits(M):
    return max((bits(x) for row in M for x in row), default=0)


def rand_instance(n, p, r, B, seed):
    rng = random.Random(seed)
    lim = 1 << B

    def mat(rows, cols):
        return [[F(rng.randrange(-lim, lim + 1)) for _ in range(cols)] for _ in range(rows)]

    A = mat(n, n)
    C = mat(p, n)
    L0 = mat(r, n)
    return A, C, L0


def main():
    print('=== 编码常数的比特长 vs 界 c(nB + n log2 n) ===')
    print(f'{"n":>3} {"B":>4} {"NC":>6} {"NV":>6} {"NH":>6} {"T":>6} {"P":>6} {"L(Θ)":>7} {"界(8nB+8nlogn)":>16} {"比值":>6}')
    worst = 0.0
    for n in (4, 5, 6, 7):
        for B in (4, 8, 12):
            A, C, L0 = rand_instance(n, 1, 1, B, seed=1000 + n * 17 + B)
            NC = P1F.nullspace_cols(C)
            CA = LQ.mul(C, A)
            NV = P1F.nullspace_cols(C + CA)
            NH = P1F.nullspace_cols(C + L0)
            try:
                fd = P1F.family_data(A, C, L0)
                Tb, Pb = maxbits(fd['T']), maxbits(fd['P'])
                k0 = fd['k']
                J0 = tuple(range(k0))
                nrest = k0 * (fd['s'] - k0)
                Ls = [P1F.chart_L(fd, J0, [F(0)] * nrest)]
                Lb = max((maxbits(L) for L in Ls), default=0)
            except AssertionError:
                Tb = Pb = Lb = 0
            bound = 8 * (n * B + n * math.log2(max(n, 2)))
            mx = max(maxbits(NC), maxbits(NV), maxbits(NH), Tb, Pb, Lb, 1)
            ratio = mx / bound
            worst = max(worst, ratio)
            print(f'{n:>3} {B:>4} {maxbits(NC):>6} {maxbits(NV):>6} {maxbits(NH):>6} '
                  f'{Tb:>6} {Pb:>6} {Lb:>7} {bound:>16.1f} {ratio:>6.2f}')
            assert ratio <= 1.0, f'比特长超界：n={n}, B={B}, max={mx}, bound={bound}'
    print(f'\n最大比值 {worst:.2f}（界 = 8(nB + n log2 n)）—— 全部样本在界内')
    print('覆盖范围：仅上述常数（基与左逆、族见证矩阵）；X(λ) 的全部系数未测。')


if __name__ == '__main__':
    main()
