r"""实现"部分相交"的两种观察者实例（失败 / 成立）。

实例族：$n=6$、$p=1$、$C=e_1$；$A e_6=e_1$（故 $CA=e_6$、$\mathcal V=\ker[e_1;e_6]=\operatorname{span}(e_2,e_3,e_4,e_5)$）；
$A e_4=e_4$、$A e_5=e_5$；$Z=\operatorname{span}(e_4,e_5)\subseteq\mathcal V$（$s=2$、$t=2$）；$q=3$（$d=2$）。
$\mathcal V/S=\operatorname{span}(e_2,e_3)$、$\ker C/Z=\operatorname{span}(e_2,e_3,e_6)$、$\iota(x_1,x_2)=(x_1,x_2,0)$。

- **失败例**：$A e_2=e_2$、$A e_3=e_3+e_6$ ⟹ $\bar A(x)=(x_1,\,x_2,\,x_2)$ ⟹ $\lambda=1$、$x=(1,0)$ 处奇异；
- **成立例**：$A e_2=2e_3$、$A e_3=e_2+e_6$ ⟹ $\bar A(x)=(x_2,\,2x_1,\,x_2)$ ⟹ 无成比例方向。

两者都满足 $(A)$（$Z\subseteq\mathcal V$ 且 $A$-不变）与"部分相交"（$\operatorname{im}\bar A\cap\operatorname{im}\iota=\operatorname{span}(e_2)$）。

用法：python proof/layer_program/c242_partial_intersection.py
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
import importlib.util as iu

_spec = iu.spec_from_file_location('C238', os.path.join(_HERE, 'c238_quotient_gcd_symbolic.py'))
Q = iu.module_from_spec(_spec)
_spec.loader.exec_module(Q)

N, P = 6, 1
C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
Z = [[Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)]]


def run(tag, ae2, ae3):
    A = [[Fr(0)] * N for _ in range(N)]
    for i in range(N):
        A[i][1] = ae2[i]     # A e2
        A[i][2] = ae3[i]     # A e3
    A[3][3] = Fr(1)          # A e4 = e4
    A[4][4] = Fr(1)          # A e5 = e5
    A[0][5] = Fr(1)          # A e6 = e1
    CA = AI.mul(C, A)
    r1 = AI.rank(AI.vstack([C, CA]))
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    d = 2
    q = N - P - d
    CAZ = AI.mul(CA, Z)
    Rv = AI.nullspace(CAZ)
    Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZ = SG.apply_col(A, Z)
    AZR = AI.mul(AZ, Rm)
    M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
    okA = AI.rank(M1) == d
    g, t, qq = Q.quotient_gcd(A, C, Z)
    okS = SG.pdeg(g) == 0
    # 交：im ι 与 im Ā（在 ker C/Z 的 w-基下）
    I, Am, tt, qqq = Q.classes(A, C, Z) if hasattr(Q, 'classes') else (None, None, t, q)
    if I is None:
        # 用 c240 的函数
        spec = iu.spec_from_file_location('C240', os.path.join(_HERE, 'c240_theorem_E_check.py'))
        M240 = iu.module_from_spec(spec)
        spec.loader.exec_module(M240)
        I, Am, tt, qqq = M240.classes(A, C, Z)
    both = [list(I[i]) + list(Am[i]) for i in range(len(I))]
    rI, rA = AI.rank(I), AI.rank(Am)
    inter_dim = rI + rA - AI.rank(both)
    subset = AI.rank(both) == rI
    print(f'{tag}：r1={r1}、dim V={len(Vv)}、q={q}、t={tt}、dim(imι)={rI}、dim(imĀ)={rA}、'
          f'交维数={inter_dim}、Ā⊆ι={subset}')
    print(f'   (A)={okA}、(S)={okS}（商铅笔 gcd 次数={SG.pdeg(g)}）')


def main():
    # 失败例：A e2 = e2，A e3 = e3 + e6
    run('失败例', [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)],
        [Fr(0), Fr(0), Fr(1), Fr(0), Fr(0), Fr(1)])
    # 成立例：A e2 = 2 e3，A e3 = e2 + e6
    run('成立例', [Fr(0), Fr(0), Fr(2), Fr(0), Fr(0), Fr(0)],
        [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(1)])


if __name__ == '__main__':
    main()
