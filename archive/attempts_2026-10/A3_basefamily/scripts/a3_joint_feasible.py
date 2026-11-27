r"""A-2/A-3 过渡：$(A)\wedge(S)$ 的联合可行集 + $(A)\iff A(u)\notin W$ 的**跨实例**检验。

**两个问题**：
1. c282（$q=4$）上，$(A)\wedge(S)$ 在更大格点上是否仍为空？
2. "c282 上 $(A)(u)\iff A(u)\notin W$" 这个实例级刻画，在**第二实例**上是否也成立？

**做法**：精确算术；$(A)$ 用 $\\operatorname{rank}[Z|AZR]=d$，$(S)$ 用 `spectral_gcd_Z`。

用法：python workspace/A3_basefamily/scripts/a3_joint_feasible.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import coeff_of_S as CS_
import spectral_gcd as SG


def c282():
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [unit(0), unit(1)]
    L0 = [unit(2)]
    A = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(0, 2), (1, 3), (4, 4), (3, 5), (5, 6), (6, 7)]:
        A[i][j] = Fr(1)
    return A, C, L0, [unit(4)], 4


def second():
    N = 6
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [[Fr(0)] * N]
    C[0][0] = Fr(1)
    A = [[Fr(0)] * N for _ in range(N)]
    A[0][5] = Fr(1); A[2][2] = Fr(1); A[3][3] = Fr(1)
    A[1][1] = Fr(1); A[4][4] = Fr(1)
    L0 = [[Fr(0)] * N]
    L0[0][1] = Fr(1)
    return A, C, L0, [unit(2), unit(3)], 3


def prep(A, C, L0, S, q):
    st = CS_.setup(A, C, L0, q, S)
    m = st['m']
    wm = st['w'] - st['s']
    hvecs = [[sum(st['HS'][j][k] * st['WB'][st['s'] + k][i] for k in range(wm))
              for i in range(st['n'])] for j in range(m)]
    return st, m, wm, hvecs


def run(label, A, C, L0, S, q, bound=1, s_max=None):
    st, m, wm, hvecs = prep(A, C, L0, S, q)
    n = st['n']
    def lift(u):
        return [sum(u[j] * hvecs[j][i] for j in range(m)) for i in range(n)]
    def inW(x):
        try:
            CS_._solve_in_basis(st['WB'], x)
            return True
        except ValueError:
            return False
    def condA(u):
        Z = list(S) + [lift(u)]
        Zmat = [[Z[j][i] for j in range(len(Z))] for i in range(n)]
        CA = AI.mul(C, A)
        CAZ = AI.mul(CA, Zmat)
        Rv = AI.nullspace(CAZ)
        d = len(Z)
        R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
        AZ = SG.apply_col(A, Zmat)
        AZR = AI.mul(AZ, R) if (R and R[0]) else [[Fr(0)] * d for _ in range(n)]
        M = [list(Zmat[i]) + list(AZR[i]) for i in range(n)]
        return AI.rank(M) == d
    print(f'\n=== {label}（q={q}, m={m}, bound={bound}）')
    tab = {}
    nA = nAS = tot = 0
    s_checked = 0
    for cs in itertools.product(range(-bound, bound + 1), repeat=m):
        if all(c == 0 for c in cs):
            continue
        u = [Fr(c) for c in cs]
        au = lift(u)
        Au = [sum(A[i][k] * au[k] for k in range(n)) for i in range(n)]
        a = condA(u)
        iw = inW(Au)
        tot += 1
        tab[(iw, a)] = tab.get((iw, a), 0) + 1
        if a:
            nA += 1
            if s_checked < 40:          # (S) 较贵，抽样
                Z = list(S) + [au]
                Zmat = [[Z[j][i] for j in range(len(Z))] for i in range(n)]
                g, _h, _c = SG.spectral_gcd_Z(A, C, Zmat)
                s_checked += 1
                if SG.pdeg(g) == 0:
                    nAS += 1
    print(f'  共 {tot} 点；(A) 成立 {nA}')
    print(f'  (A(u)∈W, (A)) 分布: {sorted(tab.items())}')
    print(f'  在 (A) 成立的点里抽检 {s_checked} 个：$(S)$ 也成立 {nAS}')
    return tab, nA, nAS


def main():
    A, C, L0, S, q = c282()
    run('c282', A, C, L0, S, q, bound=1)
    A, C, L0, S, q = second()
    run('第二实例', A, C, L0, S, q, bound=1)


if __name__ == '__main__':
    main()
