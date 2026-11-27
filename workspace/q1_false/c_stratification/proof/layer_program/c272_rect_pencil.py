r"""矩形铅笔实例（全超平面区）——证明判据必须加 $B_S$ 约束。

实例：$n=6$、$p=2$、$r=1$、$C=[e_1;e_2]$、$L_0=e_3$、$A$ 使 $CA=[e_3;e_4]$ 且 $Ae_5=e_5,\ Ae_6=e_4$。

关系：$\mathcal V=\operatorname{span}(e_5,e_6)$、$H=\operatorname{span}(e_4,e_5,e_6)$、$S=\operatorname{span}(e_5)$、
$K=H/S=\operatorname{span}(e_4,e_6)$、$I_\lambda=\operatorname{span}(e_4-\lambda e_6)$（$\dim\equiv1=m-1$）。

判据（不带 $B_S$）：$f_\lambda=(\lambda,1)$，$u=e_6$ 给出 $f_\lambda(u)=1\ne0$ ⟹ 预测**可行**。
实际：$e_6\in B_S=G/S=\mathcal V/S$，被 $U\cap B_S=0$ 排除 ⟹ **不可行**（42 个 (A)-可行 $U$ 全失败）。

用法：python proof/layer_program/c272_rect_pencil.py
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

N = 6
C = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
A = [[0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0]]
L0 = [[0, 0, 1, 0, 0, 0]]


def F(M):
    return [[Fr(x) for x in r] for r in M]


def main():
    Ai, Ci, L0i = F(A), F(C), F(L0)
    CA = AI.mul(Ci, Ai)
    V = AI.nullspace([r[:] for r in (Ci + CA)])
    H = AI.nullspace([r[:] for r in (Ci + L0i)])
    W = AI.nullspace([r[:] for r in Ci])
    print(f'v={len(V)}, h={len(H)}, w={len(W)}')
    print('V =', [[str(x) for x in v] for v in V])
    print('H =', [[str(x) for x in v] for v in H])
    S = [[Fr(1) if k == 4 else Fr(0) for k in range(N)]]           # span(e5)
    HS = [[Fr(1) if k == 3 else Fr(0) for k in range(N)],          # e4
          [Fr(1) if k == 5 else Fr(0) for k in range(N)]]          # e6
    print(f'\nS = span(e5)，K = H/S = span(e4,e6)，I_lam = span(e4 - lam e6)（dim = 1 = m-1）')
    print('B_S = G/S = V/S = span(e6) ⟹ 纤维要求 u 不与 e6 共线')
    print('判据（无 B_S）：f_lam = (lam,1)，u = e6 ⟹ f_lam(u) = 1 ≠ 0 ⟹ 预测可行')
    ok = bad = 0
    for a in range(-3, 4):
        for b in range(-3, 4):
            if (a, b) == (0, 0):
                continue
            u = [Fr(a) * HS[0][i] + Fr(b) * HS[1][i] for i in range(N)]
            if AI.rank([S[0], u]) < 2:      # U ∩ B_S = 0（B_S = span(e6)）
                continue
            Z = [[S[0][k], u[k]] for k in range(N)]
            if AI.rank(Z) < 2:
                continue
            CAZ = AI.mul(CA, Z)
            Rv = AI.nullspace(CAZ)
            Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(2)]
            AZ = SG.apply_col(Ai, Z)
            AZR = AI.mul(AZ, Rm)
            M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
            if AI.rank(M1) != 2:
                continue
            g, _, _ = SG.spectral_gcd_Z(Ai, Ci, Z)
            if SG.pdeg(g) == 0:
                ok += 1
            else:
                bad += 1
    print(f'\n(A)-可行 U：{ok + bad} 个，其中 (S) 成立 {ok}、失败 {bad}')
    print('⟹ 实际不可行；判据（不带 B_S）错误')


if __name__ == '__main__':
    main()
