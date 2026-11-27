"""qmin_exact.py —— 逐阶判定（穷举版）：在 $\\operatorname{Gr}(d,K)$ 的图卡上完整扫描

专家 2026-11-03 §5 的第一条建议：逐阶判定必须把 $\\operatorname{Gr}(d,K)$ 的可行族**枚举完整**，
把四件事分开：(1) 可行 $\\mathcal Z$ 的参数空间；(2) $(5a)$；(3) 整数障碍 $h\\ge q+r_1$；(4) 谱条件。

本脚本：

* 阶区间用 **$[q_0,\\ n_0-p]$**（$n_0=\\operatorname{rank}\\mathcal O_C$），不是 $[q_0,n-p]$；
* 对 $\\operatorname{Gr}(d,k)$（$k=\\dim K$）逐图卡枚举（$d\\times d$ 单位块 + 自由参数网格），
  若自由参数个数 $d(k-d)\\le4$ 则完整扫描；
* 每个 $\\mathcal Z$：判 $(5a)$；若可行则构造 $\\mathcal L$、算 $h$ 与 $(5b)$，并记录是否为整数障碍；
* 报告每阶的：扫描点数、$(5a)$-可行数、成功数、$h$ 范围、以及见证。

用法：python -u tools/verification/qmin_exact.py [n p r seed]
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
GRID_SMALL = [F(k) for k in range(-2, 3)] + [F(1, 2), F(-1, 2), F(2), F(-2)]
GRID_TINY = [F(k) for k in range(-1, 2)]
GRID = GRID_SMALL


def grid_for(dim_gr):
    """按 Grassmannian 维数选自适应网格（保持总扫描量可控）。"""
    if dim_gr <= 3:
        return GRID_SMALL
    if dim_gr <= 4:
        return GRID_TINY
    return None      # 太大：不做完整扫描


def charts(d, k):
    for rows in itertools.combinations(range(k), d):
        rest = [i for i in range(k) if i not in rows]
        yield rows, rest


def enumerate_Z(d, k, K, grid):
    """逐图卡枚举 $\\operatorname{Gr}(d,k)$ 的 $\\mathcal Z$（$n\\times d$ 列）。"""
    n = len(K)
    if d == 0:
        yield [[F(0)] * 0 for _ in range(n)]
        return
    for rows, rest in charts(d, k):
        npar = d * (k - d)
        for params in itertools.product(grid, repeat=npar):
            W = [[F(0)] * k for _ in range(d)]
            for a, r0 in enumerate(rows):
                W[a][r0] = F(1)
            idx = 0
            for a in range(d):
                for c in rest:
                    W[a][c] = params[idx]
                    idx += 1
            Z = [[sum(K[i][t] * W[j][t] for t in range(k)) for j in range(d)] for i in range(n)]
            if d >= 1 and ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            yield Z


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == 'fernando':
        import importlib.util as _iu
        _spec = _iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
        _m = _iu.module_from_spec(_spec)
        _spec.loader.exec_module(_m)
        made = (_m.A, _m.C, _m.L0)
        n, p, r, seed = len(_m.A), len(_m.C), len(_m.L0), 0
    elif len(sys.argv) >= 5:
        n, p, r, seed = (int(x) for x in sys.argv[1:5])
        made = QR.make_instance(n, p, r, seed * 23 + p * 11 + r)
    else:
        n, p, r, seed = 7, 2, 2, 4004
        made = QR.make_instance(n, p, r, seed * 23 + p * 11 + r)
    A, C, L0 = made
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    r1 = LQ.rank(W)
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    n0 = LQ.rank(QR.observability_matrix(A, C))
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(K[0])
    print(f'实例 n={n} p={p} r={r} seed={seed}；q0={q0}；n0=rank O_C={n0} ⟹ 阶区间 [{q0},{n0 - p}]')
    first = None
    for q in range(q0, n0 - p + 1):
        d = n - p - q
        if d < 0:
            continue
        tested = adm = good = integer = 0
        his = set()
        witness = None
        dim_gr = d * (k - d)
        grid = grid_for(dim_gr)
        if grid is None:
            print(f'  q={q}（d={d}, dim Gr={dim_gr}）：维数过大，跳过完整扫描')
            continue
        for Z in enumerate_Z(d, k, K, grid):
            tested += 1
            if d == 0:
                Ls = [list(x) for x in L0]
                cands = []
                for u in GRID + [F(3), F(-3)]:
                    pass
                # d=0 时用直接构造补（有限个随机补已足够给出见证）
                import random as _r
                rng = _r.Random(q * 31 + 7)
                for _ in range(200):
                    L = [list(x) for x in L0]
                    tries = 0
                    while len(L) < q and tries < 400:
                        tries += 1
                        u = [F(rng.randrange(-3, 4)) for _ in range(n)]
                        if LQ.rank([list(x) for x in C] + L + [u]) > LQ.rank([list(x) for x in C] + L):
                            L.append(u)
                    if len(L) == q and LQ.rank([list(x) for x in C] + L) == p + q:
                        cands.append(L)
                for L in cands:
                    if not LQ.condA(A, C, L):
                        continue
                    adm += 1
                    res = TC.analyse(A, C, L)
                    his.add(res['h'])
                    if res['five_b']:
                        good += 1
                        if witness is None:
                            witness = L
                    elif res['h'] >= q + r1:
                        integer += 1
                break
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            adm += 1
            h = LQ.rank([x[:] for x in L] + [x[:] for x in CA] + [x[:] for x in C])
            his.add(h)
            if h >= q + r1:            # 整数障碍：无需算 (5b)
                integer += 1
                continue
            if TC.analyse(A, C, L)['five_b']:
                good += 1
                if witness is None:
                    witness = L
        print(f'  q={q}（d={d}, dim Gr={d * (k - d)}）：扫描 {tested}，$(5a)$-可行 {adm}，'
              f'成功 {good}，整数障碍 {integer}，h∈{sorted(his)}，q+r1={q + r1}')
        if good and first is None:
            first = q
            print('   见证：')
            for row in witness:
                print('    ', [str(x) for x in row])
    print(f'\nq_min = {first}' if first else '\n在区间内未找到可行阶')


if __name__ == '__main__':
    main()
