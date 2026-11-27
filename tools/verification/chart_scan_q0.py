"""chart_scan_q0.py —— 在 $q_0$ 阶上按 Grassmann 图卡扫描（公开例子）

$q=q_0$ 时 $d=n-p-q_0$，候选 $\\mathcal Z=KW$，$W\\in\\operatorname{Gr}(d,\\,n-p-r)$。
每个图卡 $\\mathcal I$ 用 $W_{\\mathcal I}(\\Theta)=[I_d\\ \\Theta]\\Pi_{\\mathcal I}^{\\mathsf T}$ 参数化，
未知量个数 $d\\cdot(n-p-r-d)$。本脚本对 $\\Theta$ 做**密集有理扫描**，找出满足 $(5a)$ 的点，
再判 $(5b)$——用于定位"论文所说的 $(A)$ 族"（与抽样不同：这里在一个低维图卡内有系统地扫）。

用法：python tools/verification/chart_scan_q0.py
"""

import itertools
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import z_generator as ZG                  # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import importlib.util as iu               # noqa: E402

F = Fraction


def chart_W(m, d, J, theta):
    """$W_{\\mathcal I}(\\Theta)=[I_d\\ \\Theta]\\Pi^{\\mathsf T}$：$m\\times d$。"""
    W = [[F(0)] * d for _ in range(m)]
    rest = [j for j in range(m) if j not in J]
    for i, j in enumerate(J):
        W[j][i] = F(1)
    for t, j in enumerate(rest):
        for i in range(d):
            W[j][i] = theta[i * len(rest) + t]
    return W


def all_thetas(k, values):
    if k == 0:
        return [[]]
    out = [[]]
    for _ in range(k):
        out = [t + [v] for t in out for v in values]
    return out


def scan(A, C, L0, q, values):
    n, p, r = len(A), len(C), len(L0)
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    m = len(K[0])
    d = n - p - q
    hits = []
    k = d * (m - d)
    thetas = all_thetas(k, values)
    for J in itertools.combinations(range(m), d):
        for th in thetas:
            W = chart_W(m, d, J, th)
            # Z = K W
            Zc = [[sum(K[i][t] * W[t][j] for t in range(m)) for j in range(d)] for i in range(n)]
            if ZG.bool_rank(ZG.cols_to_rows(Zc)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Zc, q)
            if L is None:
                continue
            if LQ.rank([list(x) for x in L] + [list(x) for x in L0]) != LQ.rank(L):
                continue
            if not LQ.condA(A, C, L):
                continue
            res = TC.analyse(A, C, L)
            hits.append((J, th, res['five_b'], res['eps_smith']))
    return hits


def main():
    spec = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m = iu.module_from_spec(spec)
    spec.loader.exec_module(m)
    A, C, L0 = m.A, m.C, m.L0
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    print(f'公开例子：n={len(A)} p={len(C)} r={len(L0)} q0={q0}')
    values = [F(k) for k in (-2, -1, 0, 1, 2)]
    for q in (q0,):
        hits = scan(A, C, L0, q, values)
        feas = [h for h in hits if h[2]]
        print(f'\nq={q}（d={len(A)-len(C)-q}）：扫到 $(A)$ 成立的点 {len(hits)} 个，其中 (5b) 成立 {len(feas)}')
        for J, th, fb, eps in hits[:8]:
            print(f'   图卡 J={J} Θ={[str(x) for x in th]}  (5b)={fb} eps={eps}')


if __name__ == '__main__':
    main()
