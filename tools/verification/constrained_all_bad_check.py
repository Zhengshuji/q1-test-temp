#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""constrained_all_bad_check.py -- 约束区 n=5 实例 q=3, omega=2 的"整族全坏"证明核验

实例：n=5, p=1, q=3, r=1；C=e1^T；A 行 1 = e5^T，列 2,3,4 = e3,e2,e5；L0=e4^T。
K=<e2,e3,e4>（K-坐标记为 e1,e2,e3），ker T 的基 (-e3,e2),(-e2,e3)；
Z1=[[0,-1,0],[-1,0,0]]、Z2=[[1,0,0],[0,1,0]]；E=L0 N_K=(0,0,1)。

两个 Grassmann 点：
  S1 = {x1+x2=0}: x=(a,-a,b), y=(-a,a,d)
  S2 = {x1-x2=0}: x=(a,a,b),  y=(a,a,d)
（sanity: x Z1 + y Z2 = 0）

证明要点（本脚本核验）：
  S1 上在 lambda=-1 处，lambda H - H_A 的全部行都落在 span{e3} 里 => 秩 <=1 <2；
  S2 上在 lambda=+1 处同理。
故 q=3, omega=2 的整个层全坏（与 200 点采样一致，但这是证明而非采样）。
"""
import os
import sys
import random
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for _p in ('tools/exact_linalg', 'tools/verification'):
    sys.path.insert(0, os.path.join(_ROOT, _p))

import linalg_q as LQ                 # noqa: E402

F = Fraction
# Z1, Z2 是 k x d（3x2）矩阵，列是 ker T 的生成元（K-坐标）
Z1 = [[F(0), F(-1)], [F(-1), F(0)], [F(0), F(0)]]
Z2 = [[F(1), F(0)], [F(0), F(1)], [F(0), F(0)]]
E = [F(0), F(0), F(1)]


def dot(x, Z):
    """x (1 x k) times Z (k x d) -> 1 x d."""
    return [sum(x[t] * Z[t][j] for t in range(len(x))) for j in range(len(Z[0]))]


def vec_add(u, v):
    return [a + b for a, b in zip(u, v)]


def build_point(kind, a, b, d, a2, b2, d2):
    if kind == 'S1':
        x1 = [F(a), F(-a), F(b)]
        y1 = [F(-a), F(a), F(d)]
        x2 = [F(a2), F(-a2), F(b2)]
        y2 = [F(-a2), F(a2), F(d2)]
    else:
        x1 = [F(a), F(a), F(b)]
        y1 = [F(a), F(a), F(d)]
        x2 = [F(a2), F(a2), F(b2)]
        y2 = [F(a2), F(a2), F(d2)]
    # 相容性 x Z1 + y Z2 = 0（1 x d = 1 x 2）
    assert vec_add(dot(x1, Z1), dot(y1, Z2)) == [F(0), F(0)]
    assert vec_add(dot(x2, Z1), dot(y2, Z2)) == [F(0), F(0)]
    H = [E[:], x1, x2]
    HA = [[F(0), F(0), F(0)], y1, y2]
    return H, HA


def check_q2_witness():
    """q=2 的显式增广 L=[e4;e5] 过七条检查；q=1 失败。"""
    import importlib.util as iu
    spec = iu.spec_from_file_location('CC', os.path.join(_HERE, 'consistency_checks.py'))
    CC = iu.module_from_spec(spec)
    spec.loader.exec_module(CC)
    n = 5
    C = [[F(1) if j == 0 else F(0) for j in range(n)]]
    A = [[F(0)] * n for _ in range(n)]
    A[0][4] = F(1)   # 行 1 = e5^T
    A[2][1] = F(1)   # 列 2 = e3
    A[1][2] = F(1)   # 列 3 = e2
    A[4][3] = F(1)   # 列 4 = e5
    L0 = [[F(0), F(0), F(0), F(1), F(0)]]   # e4^T
    L2 = [L0[0][:], [F(0), F(0), F(0), F(0), F(1)]]
    r2 = CC.check_candidate(A, C, L0, L2, tag='q=2 witness', verbose=False)
    assert r2['five_b'] is True, 'q=2 witness should satisfy (5b)'
    r1 = CC.check_candidate(A, C, L0, [L0[0][:]], tag='q=1', verbose=False)
    assert r1['five_b'] is False, 'q=1 should fail (5b)'
    print('  q=2 witness L=[e4;e5] passes the seven checks; q=1 fails => q_min=2')


def main():
    rng = random.Random(20261108)
    print('=== 约束区 n=5, q=3, omega=2：整族全坏 ===')
    for kind, lam0 in [('S1', F(-1)), ('S2', F(1))]:
        tested = 0
        for _ in range(400):
            H, HA = build_point(kind, *(rng.randint(-3, 3) for _ in range(6)))
            if LQ.rank([r[:] for r in H]) != 2:
                continue
            if LQ.rank([r[:] for r in H] + [r[:] for r in HA]) != 2:
                continue
            # P(lam0) = lam0 H - H_A
            P = [[lam0 * H[i][j] - HA[i][j] for j in range(3)] for i in range(3)]
            r = LQ.rank(P)
            assert r <= 1, f'{kind}: rank(P({lam0})) = {r} > 1（预期全落在一维）'
            tested += 1
        print(f'  {kind}: 在 lambda={lam0} 处 rank(lam H - H_A) <= 1  '
              f'（{tested} 个可容许点全部通过）')
    check_q2_witness()
    print('⟹ 两个 S 的整个 q=3, omega=2 层全坏（证明见 attempts/103）')
    print('   但实例的 q_min=2（q=2 的 omega=1 层可行），"q_min=4" 已撤回')


if __name__ == '__main__':
    main()
