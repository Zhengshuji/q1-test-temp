"""fast_feasible.py —— 快速**充分**判据：Bézout 矩阵满行秩 ⟹ 该阶可行

原理（专家 $(*)$ 的直接推论）：$M(\theta)$ 有 $2D$ 行。若在某 $\\theta$ 上
$$\\operatorname{rank}M(\\theta)=2D\\quad(\\text{满行秩}),$$
则 $e_0$（也在 $\\mathbb C^{2D}$ 里）必然落在 $\\operatorname{col}M(\\theta)$ ⟹ $(5b)$ 在该 $\\theta$ 成立；
再加 $(5a)$（`condA`）与七条一致性检查，就得到**该阶可行**的证书。

这给出一个**多项式时间可判的充分条件**：只需在若干有理 $\\theta$ 上做**数值秩**（有理算术），
不需要符号消元。若所有图卡、所有采样 $\\theta$ 都不满行秩，则该方法**无输出**（交由跌落轨迹分析）。

用法：python -u tools/verification/fast_feasible.py [--max N]
"""

import os
import sys
import itertools
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import consistency_checks as CC           # noqa: E402
import bezout_rank_test as BR             # noqa: E402
import chart_gcd_analysis as CGA          # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction


def full_row_rank_witness(A, C, L0, q, rows, n_tries=24):
    """在有理 θ 上找使 rank M(θ) = 2D 的点；成功则返回见证 L 与 θ。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    # 适用条件：rank[V|Z] 在该图卡上恒定（否则极大子式尺寸错误，本方法无效）
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    if not BR.rank_is_constant(A, C, L0, q, rows, len(V[0]) + d):
        return None, None
    mins, D, tam, lam = BR.build_minors(A, C, L0, q, rows)
    if not mins or D == 0 or not tam:
        return None, None
    if len(mins) * D > 400:
        return None, None
    M, e0 = BR.coefficient_matrix(mins, D, tam, lam)
    rows_needed = 2 * D
    cands = [F(0), F(1), F(-1), F(2), F(-2), F(3), F(1, 2), F(-1, 2), F(3, 2), F(5, 2)]
    for th in cands[:n_tries]:
        sub = dict(zip(tam, [sp.Rational(th.numerator, th.denominator)] * len(tam)))
        rk = M.subs(sub).rank()
        if rk != rows_needed:
            continue
        Z = DS.Z_from_theta(A, C, L0, q, rows, [th] * (d * (k - d)))
        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            continue
        L = ZG.L_from_Z(A, C, L0, Z, q)
        if L is None or not LQ.condA(A, C, L):
            continue
        if TC.analyse(A, C, L)['five_b']:
            CC.check_candidate(A, C, L0, L, tag=f'q={q} theta={th}', verbose=False)
            return L, th
    return None, None


def decide(A, C, L0, q):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d < 0 or d > k:
        return 'UNKNOWN', 'd 越界', None
    tried = 0
    for rows in itertools.combinations(range(k), d):
        L, th = full_row_rank_witness(A, C, L0, q, rows)
        tried += 1
        if L is not None:
            return 'FEASIBLE', f'图卡 {rows}：rank M(θ) = 2D 满行秩，θ={th}', L
    return 'UNKNOWN', f'{tried} 个图卡上均未出现满行秩（或超预算）', None


def main():
    maxn = 40
    args = sys.argv[1:]
    if '--max' in args:
        maxn = int(args[args.index('--max') + 1])
    from collections import Counter
    stats = Counter()
    done = 0
    for n in (5, 6, 7):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3010):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    k = len(Kc[0])
                    d = n - p - q0
                    if d <= 0 or d >= k:
                        continue
                    v, why, w = decide(A, C, L0, q0)
                    stats[v] += 1
                    print(f'n={n} p={p} r={r} seed={seed} q0={q0} d={d} k={k}: {v}'
                          + (f'（θ={why.split("θ=")[-1]}）' if v == 'FEASIBLE' else ''))
                    done += 1
                    if done >= maxn:
                        print('\n统计：', dict(stats))
                        return
    print('\n统计：', dict(stats))


if __name__ == '__main__':
    main()
