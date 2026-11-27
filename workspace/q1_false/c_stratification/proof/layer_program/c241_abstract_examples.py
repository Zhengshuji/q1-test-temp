r"""两个抽象"部分相交"例子的精确核对（$t=2$、$q=3$、$\iota(x_1,x_2)=(x_1,x_2,0)$）。

$T_\lambda=\lambda\iota-\bar A$ 是 $3\times2$ 的铅笔；极大子式是 $2\times2$ 的三个行列式，取 gcd。
$(S)\iff$ gcd 次数 $=0$。

用法：python proof/layer_program/c241_abstract_examples.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import spectral_gcd as SG


def gcd_of_pencil(Tcols, q):
    """Tcols[j] = 第 j 列（长度 q 的向量，每个元素是多项式 [c0, c1]）；返回极大子式的 gcd。"""
    t = len(Tcols)
    T = [[Tcols[j][i] for j in range(t)] for i in range(q)]     # q×t
    minors = []
    for rows in itertools.combinations(range(q), t):
        M = [[T[r][c] for c in range(t)] for r in rows]
        minors.append(SG.pdet(M))
    minors = [m for m in minors if m != [Fr(0)]]
    g = minors[0]
    for m in minors[1:]:
        g = SG.pgcd(g, m)
        if SG.pdeg(g) == 0:
            break
    return g


def build(Abars):
    """Abars: 列表，每个是 2 元组的多项式（对 x1,x2 的分量），返回 T 的列（3×2）。"""
    # ι(x) = (x1, x2, 0)；列 j 对应 x = e_j
    Tcols = []
    for j in range(2):
        col = []
        for i in range(3):
            # λι(e_j)_i = λ（若 i==j）否则 0；减去 Ā(e_j)_i
            lam_coef = Fr(1) if i == j else Fr(0)
            abar = Abars[j][i]           # Fr
            col.append([-abar, lam_coef])
        Tcols.append(col)
    return Tcols


def main():
    # 例 A：Ā(x1,x2) = (x1, 0, x2)
    Acols = build([(Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(0), Fr(1))])
    # Ā(e1) = (1,0,0)、Ā(e2) = (0,0,1)
    gA = gcd_of_pencil(Acols, 3)
    print(f'例 A：Ā(x)=(x_1,0,x_2)，gcd 次数={SG.pdeg(gA)} ⟹ (S) {"成立" if SG.pdeg(gA)==0 else "失败"}')
    # 例 B：Ā(x1,x2) = (x2, 2x1, x2)
    AcolsB = build([(Fr(0), Fr(2), Fr(0)), (Fr(1), Fr(0), Fr(1))])
    gB = gcd_of_pencil(AcolsB, 3)
    print(f'例 B：Ā(x)=(x_2,2x_1,x_2)，gcd 次数={SG.pdeg(gB)} ⟹ (S) {"成立" if SG.pdeg(gB)==0 else "失败"}')


if __name__ == '__main__':
    main()
