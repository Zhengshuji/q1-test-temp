r"""复算 [P2]=arXiv:2609.37992 §VII 的 $n=8$ 例子：$(\eta_1,\eta_2)=(2,1)$、$q_0=3$、$n_0-p=6$。

P2 的断言：$q_0=3$、$n_0=\operatorname{rank}\mathcal O_C=8$（完全可观测）、阶范围 $\{3,4,5,6\}$，
且在 $q=3,4$ 上对所有图卡精确求值后**无**谱可行成员，最小可行阶 $\nu_{\min}=5=q_0+2$。

本脚本用项目的工具复算其中**可独立验证**的部分：$\eta_j$（全局秩保留）、$q_0$、$n_0$。
（$\nu_{\min}=5$ 需要复现他们在 $\mathrm{Gr}(3,4)$ 四个图卡上的精确求值，本脚本不做。）

用法：python proof/layer_program/c209_paper2_example.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, _HERE)

import audit_independent as AI
import importlib.util as iu

_spec = iu.spec_from_file_location('C207', os.path.join(_HERE, 'c207_q0_eta.py'))
Q0 = iu.module_from_spec(_spec)
_spec.loader.exec_module(Q0)

A = [[Fr(x) for x in r] for r in
     [[0, 1, 0, 1, 0, 0, 0, 0],
      [0, -1, 1, 0, 0, 0, 0, -1],
      [1, 0, -1, 1, 0, 0, 1, -1],
      [-1, -1, 0, -2, 0, 0, 0, 0],
      [0, 0, 0, 0, -2, 0, 0, 1],
      [0, 0, 0, 0, 0, -2, 1, 0],
      [0, 0, 0, 0, 0, -1, -2, 1],
      [0, 0, 0, 0, 0, 0, 1, -2]]]
C = [[Fr(x) for x in r] for r in [[-2, -2, 2, -2, -1, 0, 1, -3],
                                  [0, 0, 1, 2, 2, 3, -1, -2]]]
L = [[Fr(x) for x in r] for r in [[-2, -1, -2, -3, -1, 3, 2, 0],
                                  [1, -1, -2, 1, 0, 2, 0, 1]]]


def main():
    kept, eta = Q0.rank_retention(A, C + L)
    p = len(C)
    eta_C, eta_L = eta[:p], eta[p:]
    q0 = sum(eta_L)
    print(f'n={len(A)}、p={p}、r={len(L)}')
    print(f'每个 generator 保留的行数：{eta}（C 侧 {eta_C}、L 侧 {eta_L}）')
    print(f'q0 = Σ η_L = {q0}（论文：3）')
    # n0 = rank O_C
    e = [[Fr(1) if t == i else Fr(0) for t in range(len(A))] for i in range(len(A))]
    O = []
    for q in range(len(A)):
        for ei in e:
            v = ei
            for _ in range(q):
                v = AI.mul([v], A)[0]
            O.append(v)
    n0 = AI.rank(O)
    print(f'n0 = rank O_C = {n0}（论文：8）；n0 - p = {n0 - p}（论文：6）')
    assert q0 == 3 and n0 == 8 and n0 - p == 6
    print('\n复算一致 ✓：q0=3、n0=8、阶范围 {3,4,5,6}（论文的 ν_min=5 需要复现其图卡求值，未做）')


if __name__ == '__main__':
    main()
