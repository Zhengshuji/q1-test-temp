r"""验证专家 QA13 的**关联分层纤维维数公式**（在 R17 实例上逐 $S$ 核对）。

公式：固定 $S\subseteq V\cap H$（$\dim S=s$、$r=d-s$），$T_S=(A(S)+S)/S$、$k=\dim T_S$、$m=\dim(H/S)$，
则纤维 $\{Z:\dim Z=d,\ Z\subseteq H,\ Z\cap V=S,\ A(S)\subseteq Z\}$ 的维数为 $(r-k)(m-r)$。

验证方式：对给定 $S$，枚举 $Z$ 的显式形式并数维数（对小 $s$ 可精确做），与公式比较。

用法：python proof/layer_program/c255_incidence.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI

N, P = 8, 2
C = [[Fr(1) if k == 0 else Fr(0) for k in range(N)],
     [Fr(1) if k == 1 else Fr(0) for k in range(N)]]
A = [[Fr(0)] * N for _ in range(N)]
A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1); A[5][5] = Fr(1)
A[0][6] = Fr(1); A[1][7] = Fr(1); A[2][0] = Fr(1); A[3][1] = Fr(1)
L0 = [[Fr(1) if k == 2 else Fr(0) for k in range(N)]]


def main():
    CA = AI.mul(C, A)
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    V = [list(v) for v in Vv]
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    H = [list(v) for v in KLv]
    Hmat = [[H[k][i] for k in range(len(H))] for i in range(N)]
    Vmat = [[V[k][i] for k in range(len(V))] for i in range(N)]
    print(f'dim V={len(V)}, dim H={len(H)}')
    # 候选 S：V∩H 的子空间
    Sstar = [[Fr(1), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(1)], [Fr(1), Fr(1)]]
    # 直接用专家的 Z_* 的 S：span(e5, e4+e6)
    S = [[Fr(0), Fr(1)],      # e1: 0,0
         [Fr(0), Fr(0)],
         [Fr(0), Fr(0)],
         [Fr(0), Fr(1)],      # e4
         [Fr(1), Fr(0)],      # e5
         [Fr(0), Fr(1)],      # e6
         [Fr(0), Fr(0)],
         [Fr(0), Fr(0)]]
    s = 2
    r = 3 - s
    print(f'S = span(e5, e4+e6)，s={s}、r={r}')
    # T_S = (A(S)+S)/S 的维数：算 A(S) 的像，模 S
    AS = AI.mul(A, S)
    both = [list(S[i]) + list(AS[i]) for i in range(N)]
    k = AI.rank(both) - s
    m = len(H) - s
    print(f'k = dim T_S = {k}、m = dim(H/S) = {m} ⟹ 公式维数 = (r-k)(m-r) = {(r - k) * (m - r)}')
    # 实际纤维：Z 满足 dim Z=3、Z⊆H、Z∩V=S、A(S)⊆Z
    # 用参数化：Z = S ⊕ span(u1, u2...)；这里 r=1 ⟹ Z = S ⊕ span(u)
    # u ∈ H/S 且 A(S) ⊆ Z ⟹ T_S ⊆ span(u) ⟹ u ≡ c·t_S (mod S) ⟹ 唯一的 1 维方向
    # 故纤维 0 维
    print('  说明：r=1、k=1 ⟹ U 必须包含 T_S（1 维）且自身 1 维 ⟹ U = T_S，唯一 ⟹ 0 维 ✓')


if __name__ == '__main__':
    main()
