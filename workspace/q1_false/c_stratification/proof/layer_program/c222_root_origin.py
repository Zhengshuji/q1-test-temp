r"""谱失败的"公根"来自哪里？—— 分类：$A$ 在 $\mathcal V$ 上的特征值 vs. 其它。

$P(\lambda)=[(\lambda I-A)\mathcal V\mid Z]$，公根 $\lambda_0$ 满足 $\exists x\ne0$：
$$(\lambda_0 I-A)\mathcal V x_{\mathcal V}+Z x_Z=0.$$
- 若 $x_Z=0$：$\lambda_0$ 是 $A|_{\mathcal V}$ 的特征值（**结构型**，与 $Z$ 无关）；
- 若 $x_Z\ne0$：由 $\mathcal V$ 与 $Z$ 的耦合产生（**耦合型**，依赖 $Z$）。

本脚本对若干实例/点算 gcd 的根与 $A$ 的特征值，做数值分类（只作**描述**，不是证明）。

用法：python proof/layer_program/c222_root_origin.py
"""
import os
import sys
from fractions import Fraction as Fr

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG


def roots_of(g):
    if SG.pdeg(g) <= 0:
        return []
    coeffs = [float(x) for x in g][::-1]     # 高次在前
    return list(np.roots(coeffs))


def classify(A, C, Z, tag):
    g, h, _ = SG.spectral_gcd_Z(A, C, Z)
    rs = roots_of(g)
    ev = np.linalg.eigvals(np.array([[float(x) for x in row] for row in A]))
    print(f'{tag}: h={h}；gcd 次数={SG.pdeg(g)}、根 {np.round(np.sort_complex(rs),3) if rs else "—"}')
    print(f'   eig(A) = {np.round(np.sort_complex(ev),3)}')
    if rs:
        for r in rs:
            d = min(abs(r - e) for e in ev)
            print(f'   根 {r:.3f}：到 eig(A) 的最近距离 {d:.3e} ⟹ {"A-特征值" if d < 1e-6 else "耦合型"}')


def main():
    # (1) P2 例子 q=4 的一个 (A)-点
    A2 = [[Fr(x) for x in r] for r in
          [[0, 1, 0, 1, 0, 0, 0, 0],
           [0, -1, 1, 0, 0, 0, 0, -1],
           [1, 0, -1, 1, 0, 0, 1, -1],
           [-1, -1, 0, -2, 0, 0, 0, 0],
           [0, 0, 0, 0, -2, 0, 0, 1],
           [0, 0, 0, 0, 0, -2, 1, 0],
           [0, 0, 0, 0, 0, -1, -2, 1],
           [0, 0, 0, 0, 0, 0, 1, -2]]]
    C2 = [[Fr(x) for x in r] for r in [[-2, -2, 2, -2, -1, 0, 1, -3],
                                       [0, 0, 1, 2, 2, 3, -1, -2]]]
    L2 = [[Fr(x) for x in r] for r in [[-2, -1, -2, -3, -1, 3, 2, 0],
                                       [1, -1, -2, 1, 0, 2, 0, 1]]]
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C2 + L2)])
    m_L = len(KLv)
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(8)]
    W = [[Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(0), Fr(0)]]
    Z = AI.mul(KL, [[Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)], [Fr(0), Fr(0)]])
    classify(A2, C2, Z, 'P2 例子 q=4（一个 (A)-点）')

    # (2) 对角例子：gcd 根应为 A 的特征值 3
    A3 = [[Fr(0), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(2), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(3)]]
    C3 = [[Fr(1), Fr(0), Fr(0), Fr(0)]]
    Z3 = [[Fr(0), Fr(0)], [Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)]]
    classify(A3, C3, Z3, '对角例子（Z=span(e2,e3)）')


if __name__ == '__main__':
    main()
