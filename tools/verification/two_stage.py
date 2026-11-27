"""two_stage.py —— 落实专家 §5.3/§5.4 的**两阶段**流程：先几何筛选、再谱检验

**第一阶段（几何，便宜）**：对每个候选算 $h$ 与 $\\dim\\mathcal V$，得 $\\delta=h-\\dim\\mathcal V$；
由 B.31，只有 $1\\le\\delta<\\rho$ 的候选**可能**可行（$q+p<n$ 时），其余可直接丢弃。

**第二阶段（谱，昂贵）**：只对留下的候选跑 $(5b)$ 检验。

本脚本对比：不带筛选 vs 带筛选的**谱检验次数**与最终结果是否一致。

用法：python -u tools/verification/two_stage.py
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
        if LQ.rank(L) != q and q > 0:
            continue
        if LQ.rank([list(x) for x in C] + L) != n:
            continue
        return L
    return None


def main():
    rng = random.Random(20261129)
    st = Counter()
    for trial in range(600):
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
        spec_calls_all = 0
        spec_calls_filtered = 0
        feas_all = 0
        feas_filtered = 0
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
                # 第一阶段：几何筛选（只花两次秩）
                h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                Vd = LQ.rank([list(x) for x in L] + [list(x) for x in C])
                delta = h - Vd
                keep = (q + p >= n) or (1 <= delta < rho)
                # 第二阶段：谱检验（昂贵）
                V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
                spec_calls_all += 1
                ok = True if not (V and V[0]) else bool(OT.observability_ok(A, C, L)[0])
                if ok:
                    feas_all += 1
                if keep:
                    spec_calls_filtered += 1
                    if ok:
                        feas_filtered += 1
                elif ok:
                    st['★ 被筛掉但实际可行（B.31 反例？）'] += 1
        st['实例'] += 1
        st['谱检验次数（不筛）'] += spec_calls_all
        st['谱检验次数（筛选后）'] += spec_calls_filtered
        st['可行（不筛）'] += feas_all
        st['可行（筛选后）'] += feas_filtered
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')
    if st['谱检验次数（不筛）']:
        r = st['谱检验次数（筛选后）'] / st['谱检验次数（不筛）']
        print(f'\n筛选后谱检验量 = 原来的 {r:.1%}')


if __name__ == '__main__':
    main()
