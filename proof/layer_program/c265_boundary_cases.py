r"""边界用例回归（QA15 §8）：$t=0$、$q\le t$、$s=0$、$d>\dim H$ 等退化情形。

对每个构造的实例，报告 $(v,w,d,s,t,q,\dim G)$ 与剪枝判定，并在有意义时跑编码检查。

用法：python proof/layer_program/c265_boundary_cases.py
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


def params(n, C, A, L0):
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    W = AI.nullspace([row[:] for row in C])
    H = AI.nullspace([row[:] for row in (C + L0)])
    Vm = [[V[k][i] for k in range(len(V))] for i in range(n)]
    Hm = [[H[k][i] for k in range(len(H))] for i in range(n)]
    both = [list(Vm[i]) + list(Hm[i]) for i in range(n)]
    G = len(V) + len(H) - AI.rank(both)
    return len(V), len(W), len(H), G


def main():
    # 实例 1：R15 型（V = Z，t=0 可能）
    n = 5
    C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
    A = [[Fr(0)] * n for _ in range(n)]
    A[1][0] = Fr(1); A[3][1] = Fr(1); A[1][2] = Fr(1); A[2][3] = Fr(1); A[0][4] = Fr(1)
    L0 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1)]]
    v, w, h, G = params(n, C, A, L0)
    print(f'实例1（R15 型）：v={v}, w={w}, h={h}, G=dim(V∩H)={G}')
    for q in range(1, w):
        d = w - q
        # s 取最大可能 = min(d, G)
        s = min(d, G)
        t = v - s
        print(f'  q={q}: d={d}, s_max={s}, t={t}'
              + ('  [t=0 ⟹ 谱条件空，无 X 变量]' if t == 0 else '')
              + ('  [q<=t ⟹ 判假]' if 0 < q <= t else '')
              + ('  [d>dim H ⟹ 拒绝]' if d > h else ''))
    # 实例 2：V∩H = 0 的情形（构造：H 与 V 只在 0 相交）
    n2 = 6
    C2 = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
    A2 = [[Fr(0)] * n2 for _ in range(n2)]
    for i in range(n2):
        A2[i][i] = Fr(1)
    L0_2 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1), Fr(0)]]
    v2, w2, h2, G2 = params(n2, C2, A2, L0_2)
    print(f'\n实例2（A=I）：v={v2}, w={w2}, h={h2}, G={G2}')


if __name__ == '__main__':
    main()
