r"""**反例**（R14）：宽矩阵情形下 $(S)$ 也能失败 —— "唯一障碍 = 互补"（猜想）是**错的**。

构造：$n=5$、$p=1$、$C=e_1$、$L_0=e_5$，$A$ 让 $W=\operatorname{span}(e_2,e_3,e_4)$ **不变**（循环置换）。
取 $Z=\ker[C;L_0]=W$（$d=3$）。
- $(A)$：$CAZ=0$（$A W\subseteq W\subseteq\ker C$），$AZR=AZ\subseteq W=\operatorname{im}Z$ ⟹ $\operatorname{rank}[Z,AZR]=3=d$ ✓；
- $h=\operatorname{rank}[V\mid Z]=\dim V=4=n-p$，但铅笔列数 $N_c=(n-r_1)+d=4+3=7>h$（**宽矩阵**，非互补）；
- 精确 gcd 次数 **1** ⟹ $(S)$ **失败** ✗。

用两个 $A$（循环置换 / 对角特征值）都复现，说明这是结构性的（与 $A|_W$ 的具体形状无关）。

用法：python proof/layer_program/c219_wide_failure.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG


def check(Amat, tag):
    n, p, r = 5, 1, 1
    A = [[Fr(x) for x in row] for row in Amat]
    C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
    L0 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1)]]
    CA = AI.mul(C, A)
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    d = n - p - r
    assert len(KLv) == d, (len(KLv), d)
    Z = [[KLv[k][i] for k in range(len(KLv))] for i in range(n)]
    CAZ = AI.mul(CA, Z)
    r_ = AI.rank(CAZ)
    Rv = AI.nullspace(CAZ)
    R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZR = AI.mul(AI.mul(A, Z), R)
    M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
    okA = AI.rank(M1) == d
    g, h, _ = SG.spectral_gcd_Z(A, C, Z)
    Nc = len(Vv) + d
    print(f'{tag}: r={r_}、rank[Z,AZR]={AI.rank(M1)}（d={d}）⟹ (A) {okA}；'
          f'h={h}、n-p={n-p}、N_c={Nc}（宽？{Nc > h}）；gcd 次数={SG.pdeg(g)} ⟹ (S) '
          f'{"成立" if SG.pdeg(g) == 0 else "失败"}')
    return okA, h, Nc, SG.pdeg(g)


def main():
    # 实例 1：A|W 循环置换
    A1 = [[0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0]]
    # 实例 2：A|W 对角
    A2 = [[0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 2, 0, 0],
          [0, 0, 0, 3, 0],
          [0, 0, 0, 0, 0]]
    for Amat, tag in [(A1, '实例 1（循环）'), (A2, '实例 2（对角）')]:
        okA, h, Nc, deg = check(Amat, tag)
        assert okA and deg > 0 and Nc > h, '反例条件不满足'
    print('\n⟹ R14：宽矩阵（N_c>h）且非互补的情形下 $(S)$ 也可以失败；'
          '"唯一障碍 = 互补"的猜想被推翻 ✗')


if __name__ == '__main__':
    main()
