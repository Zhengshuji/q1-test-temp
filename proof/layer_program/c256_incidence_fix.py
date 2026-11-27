r"""验证专家 QA14 的关联分层更正：把 $V/S$ 换成 $B_S=(V\cap H)/S$。

在 R17 实例上：
- 检查 $V\not\subseteq H$（故 $V/S$ 不是 $H/S$ 的子空间）；
- 对两个分支的 $S$，算 $b=\dim B_S$、$k=\dim T_S$、$m=\dim(H/S)$，验证纤维维数 $(r-k)(m-r)$ 与可非空条件 $r\le m-b$。

用法：python proof/layer_program/c256_incidence_fix.py
"""
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
    V = [list(v) for v in AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])]
    H = [list(v) for v in AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])]
    Vm = [[V[k][i] for k in range(len(V))] for i in range(N)]
    Hm = [[H[k][i] for k in range(len(H))] for i in range(N)]
    both = [list(Vm[i]) + list(Hm[i]) for i in range(N)]
    inH = AI.rank(both) == len(H)
    G = AI.rank(both)          # dim(V+H) — 若 V⊆H 则等于 dim H
    print(f'dim V={len(V)}、dim H={len(H)}、dim(V+H)={G} ⟹ V⊆H ? {G == len(H)}')
    # V∩H 的维数
    inter = len(V) + len(H) - G
    print(f'dim(V∩H) = {inter}')
    def info(tag, S, s, d):
        Sm = S
        both2 = [list(Sm[i]) + list(Hm[i]) for i in range(N)]
        S_in_H = AI.rank(both2) == len(H)
        # B_S = (V∩H)/S 的维数 = dim(V∩H) - s（因为 S ⊆ V∩H）
        b = inter - s
        r = d - s
        m = len(H) - s
        AS = AI.mul(A, Sm)
        both3 = [list(Sm[i]) + list(AS[i]) for i in range(N)]
        k = AI.rank(both3) - s
        print(f'{tag}：S⊆H={S_in_H}、s={s}、r={r}、b={b}、k={k}、m={m}、'
              f'纤维维数=(r-k)(m-r)={(r - k) * (m - r)}、可非空 r≤m-b ? {r <= m - b}')
    S1 = [[Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(0)],
          [Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)], [Fr(0), Fr(0)]]
    info('S=span(e5,e6)', S1, 2, 3)
    S2 = [[Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(1)],
          [Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)], [Fr(0), Fr(0)]]
    info('S=span(e5,e4+e6)', S2, 2, 3)


if __name__ == '__main__':
    main()
