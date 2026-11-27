"""narrow_intermediate.py —— 最窄中间层 $r_1=p+2$（$\\rho=2$，$\\delta=1$）的统计

按专家 2026-11-05 §"principal recommendation"：$r_1=p+2$ 时中间层只含 $\\delta=1$ 一个值，几何歧义最小，
"剩下的问题纯粹是谱的"。

本脚本收集：$q_{\\min}-q_0$、$q_0$ 阶是否有可行候选、以及 $\\delta=1$ 层上可行/失败的比例。

用法：python -u tools/verification/narrow_intermediate.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import decide_symbolic as DS              # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction


def terminal_L(A, C, L0, n, p, r, rng):
    q = n - p
    need = q - r
    for _ in range(200):
        extra = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(need)]
        L = [list(x) for x in L0] + extra
        if LQ.rank(L) != q:
            continue
        if LQ.rank([list(x) for x in C] + L) != n:
            continue
        return L
    return None


def main():
    rng = random.Random(20261128)
    st = Counter()
    for trial in range(1500):
        n = rng.choice([6, 7])
        p = rng.choice([2, 3])
        r = rng.choice([1, 2])
        if p + r >= n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank([list(x) for x in C] + L0) != p + r:
            continue
        O = QR.observability_matrix(A, C)
        n0 = LQ.rank(O)
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        r1 = LQ.rank([list(x) for x in CA] + [list(x) for x in C])
        if r1 != p + 2:
            continue
        st['r1=p+2 实例'] += 1
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        qmin = None
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d < 0 or d > k:
                continue
            if d == 0:
                L = terminal_L(A, C, L0, n, p, r, rng)
                cands = [L] if L is not None else []
            else:
                cands = []
                for rows in itertools.combinations(range(k), d):
                    Z = DS.Z_from_theta(A, C, L0, q, rows, [F(0)] * (d * (k - d)))
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                        continue
                    try:
                        L = ZG.L_from_Z(A, C, L0, Z, q)
                    except AssertionError:
                        continue
                    cands.append(L)
            for L in cands:
                if L is None or not LQ.condA(A, C, L):
                    continue
                h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                Vd = LQ.rank([list(x) for x in L] + [list(x) for x in C])
                delta = h - Vd
                V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
                ok = True if not (V and V[0]) else bool(OT.observability_ok(A, C, L)[0])
                st[f'层 δ={delta}'] += 1
                if ok:
                    st[f'层 δ={delta} 可行'] += 1
                if ok and qmin is None:
                    qmin = q
                break
        if qmin is not None:
            st[f'qmin-q0 = {qmin - q0}'] += 1
            st['qmin<n-p' if qmin < n - p else 'qmin=n-p'] += 1
    print('统计（仅 r1=p+2 的实例）：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
