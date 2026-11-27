"""witness_scan.py —— **见证优先**的快速逐阶扫描：给 $q_{\\min}$ 的**上界**（每个带七条检查）

与 [fast_rank.py](fast_rank.py)、[joint_theta.py](joint_theta.py) 的分工：

* 本模块只做**可行方向**：在有理解参数 $\\theta$ 上直接构造 $\\mathcal L$，核 $(5a)$、$(5b)$、七条检查；
  找到即给 `FEASIBLE`（**上界** $q_{\\min}\\le q$），找不到就报 `NO_WITNESS`（**不是**不可行证明）。
* 不可行方向（下界）仍需 `joint_theta` 的 Gröbner（贵），只在需要时单独跑。

候选 $\\theta$ 取小分母有理数（秩跌落点常是有理/简单点，见 attempts/43）。

用法：python -u tools/verification/witness_scan.py [--budget 600] [--nmax 7] [--out PATH]
"""

import os
import sys
import time
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
import consistency_checks as CC           # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction
CANDS = [F(0), F(1), F(-1), F(2), F(-2), F(3), F(-3), F(1, 2), F(-1, 2), F(3, 2), F(-3, 2),
         F(5, 2), F(1, 3), F(-1, 3), F(2, 3), F(4, 3), F(1, 4), F(3, 4), F(5, 3), F(7, 2)]


def try_orders(A, C, L0, q, charts, cands):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    for rows in charts:
        nv = d * (len(ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])[0]) - d)
        for th in cands:
            ths = [th] * nv
            Z = DS.Z_from_theta(A, C, L0, q, rows, ths)
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            if TC.analyse(A, C, L)['five_b']:
                CC.check_candidate(A, C, L0, L, tag=f'q={q} theta={ths}', verbose=False)
                return L, ths, rows
    return None, None, None


def decide(A, C, L0, q, cands=None):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d < 0 or d > k:
        return 'BAD_ORDER', None, None
    charts = list(itertools.combinations(range(k), d))
    L, th, rows = try_orders(A, C, L0, q, charts, cands or CANDS)
    if L is not None:
        return 'FEASIBLE', L, (rows, th)
    return 'NO_WITNESS', None, None


def main():
    budget = 600.0
    nmax = 7
    out = os.path.join(_ROOT, 'workspace', 'augmentation_family', 'data', 'qmin_upper.tsv')
    args = sys.argv[1:]
    if '--budget' in args:
        budget = float(args[args.index('--budget') + 1])
    if '--nmax' in args:
        nmax = int(args[args.index('--nmax') + 1])
    if '--out' in args:
        out = args[args.index('--out') + 1]
    os.makedirs(os.path.dirname(out), exist_ok=True)
    new = not os.path.exists(out)
    fh = open(out, 'a', encoding='utf-8', newline='\n')
    if new:
        fh.write('n\tp\tr\tseed\tq0\tn0\tq_upper\torders\ttime\n')
    t0 = time.time()
    done = 0
    from collections import Counter
    stat = Counter()
    for n in range(5, nmax + 1):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3010):
                    if time.time() - t0 > budget:
                        print(f'[budget] {time.time() - t0:.0f}s，停止')
                        fh.close()
                        print('统计：', dict(stat))
                        return
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    n0 = LQ.rank(O)
                    hi = n0 - p
                    ts = time.time()
                    orders, vers = [], []
                    up = None
                    for q in range(q0, hi + 1):
                        v, L, info = decide(A, C, L0, q)
                        orders.append(q)
                        vers.append(v)
                        if v == 'FEASIBLE':
                            up = q
                            break
                        if v == 'BAD_ORDER':
                            break
                    el = round(time.time() - ts, 2)
                    fh.write(f'{n}\t{p}\t{r}\t{seed}\t{q0}\t{n0}\t{up}\t{orders}\t{vers}\t{el}\n')
                    fh.flush()
                    done += 1
                    stat['found' if up is not None else 'none'] += 1
                    print(f'n={n} p={p} r={r} seed={seed}: q0={q0} n0={n0} ⟹ q_min ≤ {up}'
                          f'（{el}s；{" → ".join(vers)}）', flush=True)
    fh.close()
    print(f'完成 {done}；统计 {dict(stat)}；总耗时 {time.time() - t0:.0f}s')


if __name__ == '__main__':
    main()
