"""q0_variants.py —— 比较三种 $q_0$ 算法，看哪一种等于"最小可容许阶" $q_{\\rm adm}$

* **A（当前 `eta_and_q0`）**：逐行处理，**一行一旦某阶不独立就永久停该行**；
* **B（不早停）**：逐行处理，但扫描该行 $k=0..n-1$ 全部阶，只收集独立向量，不提前停行；
* **C（全局贪心）**：把 $\\{\\ell_iA^k\\}$ 全体按 $(k,i)$ 排序逐个尝试，不因依赖而停止任何行。

对每个实例比较 A/B/C 与 $q_{\\rm adm}$（逐阶扫描可容许性的最小阶）。

用法：python -u tools/verification/q0_variants.py
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

F = Fraction


def variant_A(A, C, L0):
    return Q0.eta_and_q0(A, C, L0)[0]


def variant_B(A, C, L0):
    n, p = len(A), len(C)
    kept = [list(x) for x in C]
    eta = [0] * len(L0)
    for i, g in enumerate(L0):
        v = list(g)
        for k in range(n):
            if LQ.rank(kept + [v]) > len(kept):
                kept.append(v)
                eta[i] += 1
            v = LQ.mul([v], A)[0]
    return sum(eta)


def variant_C(A, C, L0):
    n = len(A)
    kept = [list(x) for x in C]
    eta = [0] * len(L0)
    vecs = []
    for i, g in enumerate(L0):
        v = list(g)
        row = []
        for k in range(n):
            row.append(v)
            v = LQ.mul([v], A)[0]
        vecs.append(row)
    for k in range(n):
        for i in range(len(L0)):
            v = vecs[i][k]
            if LQ.rank(kept + [v]) > len(kept):
                kept.append(v)
                eta[i] += 1
    return sum(eta)


def admissible_exists(A, C, L0, q, rng):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    if d < 0:
        return False
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    if not (K and K[0]):
        return False
    k = len(K[0])
    if d > k:
        return False
    if d == 0:
        need = n - p - r
        for _ in range(100):
            extra = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(need)]
            L = [list(x) for x in L0] + extra
            if LQ.rank([list(x) for x in C] + L) != n:
                continue
            return LQ.condA(A, C, L)
        return False
    ths = [[F(b)] * (d * (k - d)) for b in (0, 1, -1, 2)]
    for _ in range(4):
        ths.append([F(rng.randrange(-3, 4)) for _ in range(d * (k - d))])
    for rows in itertools.combinations(range(k), d):
        for th in ths:
            Z = DS.Z_from_theta(A, C, L0, q, rows, th)
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            try:
                L = ZG.L_from_Z(A, C, L0, Z, q)
            except AssertionError:
                continue
            if L is not None and LQ.condA(A, C, L):
                return True
    return False


def main():
    rng = random.Random(20261203)
    st = Counter()
    for trial in range(400):
        n = rng.choice([5, 6])
        p = rng.choice([1, 2])
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
        if LQ.rank(QR.observability_matrix(A, C)) != n:
            continue
        if LQ.rank(QR.observability_matrix(A, L0)) != n:
            continue
        qA, qB, qC = variant_A(A, C, L0), variant_B(A, C, L0), variant_C(A, C, L0)
        qadm = None
        for q in range(r, n - p + 1):
            if admissible_exists(A, C, L0, q, rng):
                qadm = q
                break
        if qadm is None:
            continue
        st['实例'] += 1
        st[f'A - qadm = {qA - qadm}'] += 1
        st[f'B - qadm = {qB - qadm}'] += 1
        st[f'C - qadm = {qC - qadm}'] += 1
        st['A=B' if qA == qB else 'A≠B'] += 1
        st['B=C' if qB == qC else 'B≠C'] += 1
    print('统计（qadm 为最小可容许阶）：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
