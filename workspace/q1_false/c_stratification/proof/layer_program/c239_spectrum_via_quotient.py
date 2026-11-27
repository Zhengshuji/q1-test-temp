r"""用"$q>t$ 剪枝 + 商铅笔 gcd"重跑三个实例的**阶谱**，与已知结果对照。

- P2 例子：$\nu_{\min}=5$（已知）；
- R15 例子：只有 $q=1$ 可行（已知）；
- R17 例子：$q=2,3$ 可行（已知薄层非终端点）。

用法：python proof/layer_program/c239_spectrum_via_quotient.py
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
import spectral_gcd as SG
import importlib.util as iu

_spec = iu.spec_from_file_location('C238', os.path.join(_HERE, 'c238_quotient_gcd_symbolic.py'))
Q = iu.module_from_spec(_spec)
_spec.loader.exec_module(Q)


def spectrum(A, C, L0, orders, verbose=False):
    n, p, r = len(A), len(C), len(L0)
    CA = AI.mul(C, A)
    r1 = AI.rank(AI.vstack([C, CA]))
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    m_L = len(KLv)
    KL = Q.cols([list(v) for v in KLv], n)
    n0rows, cur = [], [list(x) for x in C]
    for _k in range(n):
        n0rows.extend(cur)
        cur = [AI.mul([x], A)[0] for x in cur]
    n0 = AI.rank(n0rows)
    out = {}
    for q in orders:
        d = n - p - q
        if d < 0 or d > m_L:
            out[q] = 'out-of-range'
            continue
        feas = []
        pts = []
        if d * (m_L - d) <= 4:
            for I in itertools.combinations(range(m_L), d):
                for t in itertools.product((-1, 0, 1), repeat=(m_L - d) * d):
                    pts.append((I, [list(t[k * d:(k + 1) * d]) for k in range(m_L - d)]))
        else:
            import random
            rng = random.Random(11)
            for _2 in range(150):
                I = tuple(sorted(rng.sample(range(m_L), d)))
                th = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(m_L - d)]
                pts.append((I, th))
        for I, th in pts:
            W = [[Fr(0)] * d for _ in range(m_L)]
            Iset = set(I)
            for a, ri in enumerate(I):
                W[ri][a] = Fr(1)
            free = [x for x in range(m_L) if x not in Iset]
            for a, ri in enumerate(free):
                for b in range(d):
                    W[ri][b] = th[a][b]
            Z = AI.mul(KL, W)
            if d and AI.rank(Z) < d:
                continue
            CAZ = AI.mul(CA, Z) if d else [[Fr(0)]]
            Rv = AI.nullspace(CAZ) if d else []
            Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
            AZ = SG.apply_col(A, Z) if d else [[Fr(0)] for _ in range(n)]
            AZR = AI.mul(AZ, Rm) if d else [[] for _ in range(n)]
            M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
            if d and AI.rank(M1) != d:
                continue
            g, t, qq = Q.quotient_gcd(A, C, Z)
            if qq <= t:
                continue                    # Theorem D 剪枝：q ≤ t 必失败
            if SG.pdeg(g) == 0:
                feas.append((I, th))
                break
        out[q] = f'可行（找到 {len(feas)} 个见证）' if feas else '未找到可行点'
        if verbose:
            print(f'  q={q}: d={d}, {out[q]}')
    return out, dict(r1=r1, dimV=len(Vv), n0=n0, n0mp=n0 - p, m_L=m_L)


def main():
    # P2 例子
    A2 = [[Fr(x) for x in r] for r in
          [[0, 1, 0, 1, 0, 0, 0, 0], [0, -1, 1, 0, 0, 0, 0, -1], [1, 0, -1, 1, 0, 0, 1, -1],
           [-1, -1, 0, -2, 0, 0, 0, 0], [0, 0, 0, 0, -2, 0, 0, 1], [0, 0, 0, 0, 0, -2, 1, 0],
           [0, 0, 0, 0, 0, -1, -2, 1], [0, 0, 0, 0, 0, 0, 1, -2]]]
    C2 = [[Fr(x) for x in r] for r in [[-2, -2, 2, -2, -1, 0, 1, -3],
                                       [0, 0, 1, 2, 2, 3, -1, -2]]]
    L2 = [[Fr(x) for x in r] for r in [[-2, -1, -2, -3, -1, 3, 2, 0],
                                       [1, -1, -2, 1, 0, 2, 0, 1]]]
    print('P2 例子（预期：5 可行；4 不可行）')
    out, info = spectrum(A2, C2, L2, [3, 4, 5], verbose=True)
    print(f'  参数：{info}')

    # R15 例子
    A3 = [[Fr(0)] * 5 for _ in range(5)]
    A3[1][0] = Fr(1); A3[3][1] = Fr(1); A3[1][2] = Fr(1); A3[2][3] = Fr(1); A3[0][4] = Fr(1)
    C3 = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
    L3 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1)]]
    print('\nR15 例子（预期：只有 1 可行）')
    out, info = spectrum(A3, C3, L3, [1, 2, 3, 4], verbose=True)
    print(f'  参数：{info}')

    # R17 例子
    A4 = [[Fr(0)] * 8 for _ in range(8)]
    A4[6][2] = Fr(1); A4[7][3] = Fr(1); A4[4][4] = Fr(1); A4[5][5] = Fr(1)
    A4[0][6] = Fr(1); A4[1][7] = Fr(1); A4[2][0] = Fr(1); A4[3][1] = Fr(1)
    C4 = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    L4 = [[Fr(0), Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    print('\nR17 例子（预期：2、3 可行）')
    out, info = spectrum(A4, C4, L4, [1, 2, 3, 4], verbose=True)
    print(f'  参数：{info}')


if __name__ == '__main__':
    main()
