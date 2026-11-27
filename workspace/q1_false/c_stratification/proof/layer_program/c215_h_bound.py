r"""验证必要条件：$\operatorname{rank}[V\mid Z]=n-p$ 时 $(S)$ 必失败（定理见 [../h_bound/README.md]）。

对 P1/P2 的例子、随机 $\Theta$：检查
- 若 $h=n-p$ 且 $\dim V\ge1$ ⟹ 精确 $(S)$（gcd 次数 $>0$）必失败；
- 若某点 $(S)$ 成立 ⟹ 该点 $h<n-p$。

用法：python proof/layer_program/c215_h_bound.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))
sys.path.insert(0, _HERE)

import audit_independent as AI
import spectral_gcd as SG
import importlib.util as iu

_spec = iu.spec_from_file_location('C211', os.path.join(_HERE, 'c211_allbad_scan.py'))
M211 = iu.module_from_spec(_spec)
_spec.loader.exec_module(M211)

P1 = dict(A=[[Fr(x) for x in r] for r in
            [[-14, 3, -4, 5, -1, -1, 1, 0],
             [-3, 5, 3, -2, -6, 0, 8, 0],
             [22, -17, 1, -9, 8, 3, -11, 0],
             [9, -11, -2, -6, 7, 1, -5, 0],
             [21, -2, 12, -14, -6, 3, 2, 0],
             [0, 1, -1, 0, 0, -5, 3, 0],
             [10, -9, 1, -3, 5, 1, -10, 0],
             [0, 0, 0, 0, 0, 0, 0, -1]]],
          C=[[Fr(x) for x in r] for r in [[2, -3, 0, 0, 2, 0, -4, 0],
                                          [-1, -10, -3, 2, 5, 0, -10, 0]]],
          L=[[Fr(x) for x in r] for r in [[-2, 3, 1, 0, -2, 0, 1, 0],
                                          [-7, 8, 3, 0, -6, 0, 2, 0]]])


def check(A, C, L, q, rng, samples=12):
    n, p = len(A), len(C)
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L)])
    m_L = len(KLv)
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + AI.mul(C, A))])
    dimV = len(Vv)
    d = n - p - q
    bad_h = bad_s = 0
    total = 0
    for _ in range(samples):
        I = tuple(sorted(rng.sample(range(m_L), d)))
        theta = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(m_L - d)]
        Z = AI.mul(KL, M211.chart_matrix(d, I, theta))
        if AI.rank(Z) < d:
            continue
        total += 1
        Vrows = [[Vv[k][i] for k in range(dimV)] for i in range(n)]
        h = AI.rank([Vrows[i] + list(Z[i]) for i in range(n)])
        g, h2, _ = SG.spectral_gcd_Z(A, C, Z)
        s_ok = SG.pdeg(g) == 0
        if h == n - p and dimV >= 1:
            bad_h += 1
            if s_ok:
                print(f'  反例！h=n-p={n-p} 但 (S) 成立（q={q}, I={I}, Θ={theta}）')
        if s_ok:
            bad_s += 1
            if h >= n - p:
                print(f'  反例！(S) 成立但 h={h} >= n-p={n-p}（q={q}, I={I}）')
    print(f'  q={q}：采样 {total}；h=n-p 的点 {bad_h} 个；(S) 成立 {bad_s} 个（应全满足 h<n-p）')
    return bad_h, bad_s


def main():
    rng = random.Random(20261030)
    print('P2 例子（n=8, p=2）：')
    check(M211.A, M211.C, M211.L, 4, rng)
    check(M211.A, M211.C, M211.L, 5, rng)
    print('P1 例子（n=8, p=2）：')
    check(P1['A'], P1['C'], P1['L'], 4, rng)
    print('\n结论：未出现反例 ✓（定理的实例侧验证；定理本身见 ../h_bound/README.md）')


if __name__ == '__main__':
    main()

