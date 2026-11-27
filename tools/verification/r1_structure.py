"""r1_structure.py —— $r=1$ 时固定阶判定集合的**代数结构**（专家 2026-11-03 §3.2 的中间目标）

问题：$r=1$、固定阶 $q=q_0$，可行集（$(5a)$ 与 $(5b)$）在 Grassmann 图卡坐标 $\\Theta$ 下是什么形状？
若是**仿射/线性**的，固定阶判定在 $r=1$ 时就可能是多项式的；若一般非线性，则说明难在哪里。

做法：对每个实例，取 $r=1$、$q=q_0$，$K=\\ker[C;L_0]$（$\\dim k$）、$d=n-p-q$；
在第一个图卡上（$d\\times d$ 单位块 + $d(k-d)$ 个自由参数）做网格扫描，收集
$\\mathcal A=\\{$可行$\\}$ 与 $\\mathcal G=\\{$可行且 $(5b)$ 成立$\\}$，然后检验**中点封闭性**：
若 $\\Theta_1,\\Theta_2\\in\\mathcal A$ 则 $(\\Theta_1+\\Theta_2)/2\\in\\mathcal A$，则集合像仿射集。

用法：python -u tools/verification/r1_structure.py
"""

import os
import sys
import itertools
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

F = Fraction
GRID = [F(v) for v in (-2, -1, 0, 1, 2)] + [F(1, 2), F(-1, 2)]


def Z_of(K, d, k, rows, rest, params):
    n = len(K)
    # W: d×k，单位块在 rows，自由参数填在 rest 列
    W = [[F(0)] * k for _ in range(d)]
    for a, r0 in enumerate(rows):
        W[a][r0] = F(1)
    idx = 0
    for a in range(d):
        for c in rest:
            W[a][c] = params[idx]
            idx += 1
    return [[sum(K[i][t] * W[j][t] for t in range(k)) for j in range(d)] for i in range(n)]


def judge(A, C, L0, Z, q):
    L = ZG.L_from_Z(A, C, L0, Z, q)
    if L is None or not LQ.condA(A, C, L):
        return None
    return TC.analyse(A, C, L)['five_b']


def main():
    triples = []
    for n in (5, 6):
        for p in (1, 2):
            for seed in range(3000, 3060):
                triples.append((n, p, seed))
    done = 0
    for (n, p, seed) in triples:
        made = QR.make_instance(n, p, 1, seed * 17 + p * 7 + 1)
        if made is None:
            continue
        A, C, L0 = made
        O = QR.observability_matrix(A, C)
        if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
            continue
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        k = len(K[0])
        for q in (q0,):
            d = n - p - q
            if d <= 0 or d >= k:
                continue
            npar = d * (k - d)
            if npar > 4:
                continue
            rows = tuple(range(d))
            rest = [i for i in range(k) if i not in rows]
            adm, good = {}, {}
            for params in itertools.product(GRID, repeat=npar):
                Z = Z_of(K, d, k, rows, rest, params)
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                v = judge(A, C, L0, Z, q)
                if v is None:
                    continue
                adm[params] = v
                if v:
                    good[params] = True
            pts = list(adm.keys())
            gpts = list(good.keys())
            if not pts:
                continue

            def mid_test(base, pts, limit=40):
                same = tot = good_hits = 0
                for i in range(len(pts)):
                    for j in range(i + 1, len(pts)):
                        if tot >= limit:
                            break
                        a, b = pts[i], pts[j]
                        m = tuple((a[t] + b[t]) / 2 for t in range(npar))
                        Z = Z_of(K, d, k, rows, rest, m)
                        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                            continue
                        v = judge(A, C, L0, Z, q)
                        tot += 1
                        if v is not None:
                            same += 1
                            if base == 'good' and v:
                                good_hits += 1
                return same, tot, good_hits

            sA, tA, _ = mid_test('adm', pts)
            sG, tG, gG = mid_test('good', gpts) if len(gpts) > 1 else (0, 0, 0)
            print(f'n={n} p={p} r=1 seed={seed} q={q}: d={d} k={k} 参数 {npar}｜'
                  f'可行 {len(pts)}（其中 (5b) 成立 {len(gpts)}）')
            print(f'   中点检验：可行集 {sA}/{tA} 仍可行；好集 {sG}/{tG} 仍可行且其中 {gG} 仍好')
            done += 1
            if done >= 6:
                return


if __name__ == '__main__':
    main()
