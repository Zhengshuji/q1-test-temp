"""delta_fixed.py —— 修正 $\\delta$ 的算法并重扫

**错误**：先前脚本用 `delta = dim(V) + rank(CA) − rank([V;CA])`，得到的其实是**交维数** $\\dim(D\\cap\\mathcal V)$，
不是 $\\delta$。正确公式（都是维数恒等式）：
$$\\delta=h-\\dim\\mathcal V=h-(q+p),\\qquad \\dim(D\\cap\\mathcal V)=\\dim D-\\delta .$$

本脚本用正确公式重扫：按 $\\delta$ 分层统计 $(5b)$ 可行性；并核验 B.32（$\\rho=r_1-p\\le1$ ⟹ $q_{\\min}=n-p$）。
终阶（$d=0$）的 $\\mathcal L$ 直接构造（$[C;\\mathcal L]$ 为基）。

用法：python -u tools/verification/delta_fixed.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter, defaultdict

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
    """构终阶的 ℒ（$q=n-p$）：[C;L] 为 $\\mathbb C^n$ 的基。"""
    rows = [list(x) for x in C] + [list(x) for x in L0]
    if LQ.rank(rows) != p + r:
        return None
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


def feasible(A, C, L):
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    if not (V and V[0]):
        return True
    ok, _w = OT.observability_ok(A, C, L)
    return bool(ok)


def main():
    rng = random.Random(20261127)
    per = defaultdict(lambda: [0, 0])
    st = Counter()
    for trial in range(1200):
        n = rng.choice([6, 7])
        p = rng.choice([1, 2, 3])
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
        rho = r1 - p
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
                delta = h - Vd                     # 正确公式
                ok = feasible(A, C, L)
                tag = ('δ=ρ' if delta == rho else ('中间层' if 1 <= delta < rho else ('δ=0' if delta == 0 else f'δ={delta}?')))
                per[(p, r, r1, tag)][0] += 1
                if ok:
                    per[(p, r, r1, tag)][1] += 1
                if ok and qmin is None:
                    qmin = q
                break
        if rho <= 1:
            st['ρ≤1 实例'] += 1
            if qmin == n - p:
                st['ρ≤1：qmin=n-p ✓（B.32）'] += 1
            elif qmin is None:
                st['ρ≤1：未找到可行（异常）'] += 1
            else:
                st[f'ρ≤1：qmin={qmin}≠n-p（反例？）'] += 1
        else:
            st['ρ≥2 实例'] += 1
            if qmin is not None and qmin < n - p:
                st['ρ≥2：qmin<n-p（次终端可行）'] += 1
    print('按 (p,r,r1,层) 分层：')
    for key in sorted(per):
        p_, r_, r1_, tag = key
        s_, f_ = per[key]
        print(f'  p={p_} r={r_} r1={r1_} {tag:>8}: {s_:>5} 样本, {f_:>5} 可行')
    print()
    print('B.32 核验：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
