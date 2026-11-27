r"""R17 的**独立验证**：把两行 $Z$ 显式写出，逐条核对 $(A)$、$(S)$、功能可观测。

（专家指出报告 §3 第二行写成了 4 个生成元，而 $d=3$；本脚本给出脚本里实际使用的 $Z$ 的列。）

用法：python proof/layer_program/c243_r17_verify.py
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

N, P, R = 8, 2, 1
C = [[Fr(1) if k == 0 else Fr(0) for k in range(N)],
     [Fr(1) if k == 1 else Fr(0) for k in range(N)]]
A = [[Fr(0)] * N for _ in range(N)]
A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1); A[5][5] = Fr(1)
A[0][6] = Fr(1); A[1][7] = Fr(1); A[2][0] = Fr(1); A[3][1] = Fr(1)
L0 = [[Fr(1) if k == 2 else Fr(0) for k in range(N)]]

# 实际使用的 Z（c235 打印出的列）
Z2 = [[Fr(0), Fr(0), Fr(0), Fr(0)],
      [Fr(0), Fr(0), Fr(0), Fr(0)],
      [Fr(0), Fr(0), Fr(0), Fr(0)],
      [Fr(1), Fr(0), Fr(0), Fr(0)],
      [Fr(0), Fr(1), Fr(0), Fr(0)],
      [Fr(0), Fr(0), Fr(1), Fr(0)],
      [Fr(0), Fr(0), Fr(0), Fr(0)],
      [Fr(0), Fr(0), Fr(0), Fr(1)]]
# q=3：列为 e4 - e7 - e8、e5、e6
Z3 = [[Fr(0), Fr(0), Fr(0)],
      [Fr(0), Fr(0), Fr(0)],
      [Fr(0), Fr(0), Fr(0)],
      [Fr(1), Fr(0), Fr(0)],
      [Fr(0), Fr(1), Fr(0)],
      [Fr(0), Fr(0), Fr(1)],
      [Fr(-1), Fr(0), Fr(0)],
      [Fr(-1), Fr(0), Fr(0)]]


def check(tag, q, Z, expected_d):
    CA = AI.mul(C, A)
    d = len(Z[0])
    assert d == expected_d, (tag, d, expected_d)
    assert AI.rank(Z) == d, f'{tag}: rank Z != d'
    CAZ = AI.mul(CA, Z)
    Rv = AI.nullspace(CAZ)
    Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZ = SG.apply_col(A, Z)
    AZR = AI.mul(AZ, Rm)
    M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
    rkM1 = AI.rank(M1)
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    Vc = [[Vv[k][i] for k in range(len(Vv))] for i in range(N)]
    both = [list(Vc[i]) + list(Z[i]) for i in range(N)]
    s = len(Vv) + d - AI.rank(both)
    t = len(Vv) - s
    g, h, hh = SG.spectral_gcd_Z(A, C, Z)
    okA = rkM1 == d
    okS = SG.pdeg(g) == 0
    ZinV = (AI.rank(both) == len(Vv))
    print(f'{tag}：q={q}、d={d}、rank Z={AI.rank(Z)}、dim V={len(Vv)}、s={s}、t={t}')
    print(f'  CAZ 的列 = {[[str(CAZ[i][j]) for j in range(d)] for i in range(P)]}')
    print(f'  ker(CAZ) 维数 = {len(Rv)}、rank[Z,AZR] = {rkM1}（d={d}）⟹ (A)={okA}')
    print(f'  h = {h}、gcd 次数 = {SG.pdeg(g)} ⟹ (S)={okS}')
    print(f'  Z⊆V = {ZinV}')
    return okA and okS and not ZinV


def main():
    ok2 = check('R17 第一行', 2, Z2, 4)
    ok3 = check('R17 第二行', 3, Z3, 3)
    print(f'\n两行都成立：{ok2 and ok3}')


if __name__ == '__main__':
    main()
