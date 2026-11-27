r"""P2 例子的 **all-bad** 核查（精确 (S)）：q=4 上 $(A)$ 可行但 $(S)$ 全失败；q=5 上 $(S)$ 成立。

用 `tools/verification/spectral_gcd.py` 的**极大子式 gcd**（精确有理多项式）代替"在有限个 $\lambda$ 采样"——
后者会漏掉复根/非整数根，给出假的"(S) 通过"（本脚本的开发过程就踩过，见 CLAUDE §10.1）。

用法：python proof/layer_program/c212_allbad_exact.py [--max 40]
"""
import itertools
import os
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

A, C, L, n, p = M211.A, M211.C, M211.L, M211.n, M211.p


def a_feasible(d, I, theta, KL, m_L):
    W = M211.chart_matrix(d, I, theta)
    Z = AI.mul(KL, W)
    CAZ = AI.mul(AI.mul(C, A), Z)
    Rv = AI.nullspace(CAZ)
    R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZR = AI.mul(AI.mul(A, Z), R)
    M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
    return AI.rank(M1) == d, Z


def main():
    maxpts = 40
    if '--max' in sys.argv:
        maxpts = int(sys.argv[sys.argv.index('--max') + 1])
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L)])
    m_L = len(KLv)
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
    grid = [Fr(-1), Fr(0), Fr(1)]
    for q in (4, 5):
        d = n - p - q
        pts = []
        for I in itertools.combinations(range(m_L), d):
            for t in itertools.product(grid, repeat=(m_L - d) * d):
                theta = [list(t[k * d:(k + 1) * d]) for k in range(m_L - d)]
                ok, Z = a_feasible(d, I, theta, KL, m_L)
                if ok:
                    pts.append((I, t, Z))
        print(f'q={q}: d={d}、(A) 采样点 {len(pts)} 个；用精确 gcd 检查前 {min(maxpts, len(pts))} 个')
        bad = good = 0
        for (I, t, Z) in pts[:maxpts]:
            g, h, cnt = SG.spectral_gcd_Z(A, C, Z)
            if SG.pdeg(g) == 0:
                good += 1
            else:
                bad += 1
        print(f'  精确 (S)：成立 {good} 个、失败 {bad} 个')
        if q == 4:
            assert bad == min(maxpts, len(pts)), 'q=4 上应全部失败（all-bad）'
        else:
            assert good == min(maxpts, len(pts)), 'q=5 上应全部成立'
    print('\n结论（[精确验证]，采样范围内）：P2 的例子在 q=4 上 all-bad、在 q=5 上可行 ✓')


if __name__ == '__main__':
    main()
