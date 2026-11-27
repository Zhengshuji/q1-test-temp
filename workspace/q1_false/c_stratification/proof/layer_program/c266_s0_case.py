r"""边界用例：$V\cap H=0$、$s=0$、$Z=H$（$n=5$、$p=2$）。

构造：$C=[e_1;e_2]$、$A$ 的前两行为 $e_3,e_4$（故 $CA=[e_3;e_4]$、$r_1=4$、$\mathcal V=\operatorname{span}(e_5)$）、
$L_0=e_5$（故 $H=\ker[e_1;e_2;e_5]=\operatorname{span}(e_3,e_4)$）。
于是 $\mathcal V\cap H=0$ ⟹ $s=0$；$q=1$ 时 $d=2=\dim H$ ⟹ $Z=H$。

用法：python proof/layer_program/c266_s0_case.py
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


def main():
    n = 5
    C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0)]]
    A = [[Fr(0)] * n for _ in range(n)]
    A[0][2] = Fr(1)   # 行 0 = e3
    A[1][3] = Fr(1)   # 行 1 = e4
    A[2][4] = Fr(1)   # 其余任意（保持 A 可逆性无关）
    A[3][4] = Fr(1)
    A[4][0] = Fr(1)
    L0 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1)]]
    CA = AI.mul(C, A)
    print('CA =', [[str(x) for x in row] for row in CA])
    V = AI.nullspace([row[:] for row in (C + CA)])
    H = AI.nullspace([row[:] for row in (C + L0)])
    W = AI.nullspace([row[:] for row in C])
    print(f'v={len(V)}, h={len(H)}, w={len(W)}')
    Vm = [[V[k][i] for k in range(len(V))] for i in range(n)]
    Hm = [[H[k][i] for k in range(len(H))] for i in range(n)]
    both = [list(Vm[i]) + list(Hm[i]) for i in range(n)]
    G = len(V) + len(H) - AI.rank(both)
    print(f'dim(V∩H) = {G}  ⟹ s ≤ {min(2, G)}')
    # q=1 ⟹ d=2=dim H ⟹ Z=H
    q = 1
    d = len(W) - q
    print(f'q={q}: d = w - q = {d}（= dim H ⟹ Z=H）')
    Z = Hm
    g, h, _c = SG.spectral_gcd_Z(A, C, Z)
    print(f'Z=H：h={h}、gcd 次数={SG.pdeg(g)} ⟹ (S) {SG.pdeg(g) == 0}')
    CAZ = AI.mul(CA, Z)
    Rv = AI.nullspace(CAZ)
    Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZ = SG.apply_col(A, Z)
    AZR = AI.mul(AZ, Rm)
    M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
    print(f'(A)：rank[Z,AZR]={AI.rank(M1)}（d={d}）⟹ {AI.rank(M1) == d}')
    print(f'rank(CAZ) = {AI.rank(CAZ)}、dim S = dim(V∩Z) = {len(V) + d - AI.rank([list(Vm[i]) + list(Z[i]) for i in range(n)])}')


if __name__ == '__main__':
    main()
