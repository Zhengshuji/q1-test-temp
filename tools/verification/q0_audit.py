"""q0_audit.py —— 审计 `eta_and_q0`：它算的是不是"代数最小阶"？

专家 2026-11-05 §1.2 指出三件事需要区分：
* $q_0^{\\rm greedy}$：`eta_and_q0` 逐行贪心给的值；
* $q_0^{\\rm canonical}$：不变量（函数可观测指标）；
* $q_0^{\\rm lit}$：文献的 $q_0$。

本脚本测三件事：
1. **不变性**：把 $L_0$ 换成 $M L_0$（$M$ 可逆）、或置换其行，$q_0^{\\rm greedy}$ 是否不变？
2. **早停是否会漏方向**：是否存在"$\\ell_iA^k$ 依赖但当 $k+1$ 时独立"的情形（贪心会漏掉）？
3. **与"最小可容许阶"比较**：逐阶扫描，找最小的 $q$ 使存在可容许 $\\mathcal L$（$q_{\\rm adm}$），
   与 $q_0^{\\rm greedy}$ 比较。

用法：python -u tools/verification/q0_audit.py
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


def greedy_trace(A, C, L0):
    """复刻 eta_and_q0 的贪心，返回 (q0, 逐步记录)。"""
    n = len(A)
    gens = [list(r) for r in C] + [list(r) for r in L0]
    kept, alive = [], [True] * len(gens)
    eta = [0] * len(gens)
    trace = []
    for q in range(n):
        for i, g in enumerate(gens):
            if not alive[i]:
                continue
            v = g
            for _ in range(q):
                v = LQ.mul([v], A)[0]
            ok = LQ.rank(kept + [v]) > len(kept)
            trace.append((q, i, ok))
            if ok:
                kept.append(v)
                eta[i] += 1
            else:
                alive[i] = False
    p = len(C)
    return sum(eta[p:]), eta[:p], eta[p:], trace


def early_stop_miss(A, C, L0):
    """检测"早停会漏方向"：某行在 q 处依赖（被停），但其 q+1 处向量再往后能独立吗？

    严格做法：对每个被停的 (i, q)，检查 ℓ_iA^{q+1} 是否相对 kept（在该时刻）独立。"""
    n = len(A)
    gens = [list(r) for r in C] + [list(r) for r in L0]
    kept, alive = [], [True] * len(gens)
    misses = 0
    for q in range(n):
        for i, g in enumerate(gens):
            if not alive[i]:
                continue
            v = g
            for _ in range(q):
                v = LQ.mul([v], A)[0]
            if LQ.rank(kept + [v]) > len(kept):
                kept.append(v)
            else:
                alive[i] = False
                # 检查下一阶
                if q + 1 < n:
                    w = LQ.mul([v], A)[0]
                    if LQ.rank(kept + [w]) > len(kept):
                        misses += 1
    return misses


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
    rng = random.Random(20261202)
    st = Counter()
    for trial in range(500):
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
        st['实例'] += 1
        q0, _, _, _ = greedy_trace(A, C, L0)
        # 1) 不变性：M L0（可逆）与行置换
        for _ in range(3):
            M = [[F(rng.randrange(-2, 3)) for _ in range(r)] for _ in range(r)]
            if LQ.rank(M) != r:
                continue
            L0b = LQ.mul(M, L0)
            if LQ.rank([list(x) for x in C] + L0b) != p + r:
                continue
            q0b, _, _, _ = greedy_trace(A, C, L0b)
            st['M 变换后相同' if q0b == q0 else 'M 变换后不同'] += 1
        if r >= 2:
            L0p = [L0[1], L0[0]]
            q0p, _, _, _ = greedy_trace(A, C, L0p)
            st['置换后相同' if q0p == q0 else '置换后不同'] += 1
        # 2) 早停漏方向
        m = early_stop_miss(A, C, L0)
        st['早停有漏方向' if m > 0 else '早停无漏'] += 1
        # 3) 最小可容许阶
        qadm = None
        for q in range(r, n - p + 1):
            if admissible_exists(A, C, L0, q, rng):
                qadm = q
                break
        if qadm is not None:
            st[f'qadm - q0 = {qadm - q0}'] += 1
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
