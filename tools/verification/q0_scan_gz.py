"""q0_scan_gz.py —— 用 $G_{\\mathcal Z}$ 判据重扫 $q_0$ 阶（提高命中率）

上一轮的 $q_0$ 阶抽样命中率极低（多数实例只拿到 1 个样本），原因已定位：
$\\dim G_{\\mathcal Z}<q_0$ 的 $\\mathcal Z$ 连必要条件都不过（282/300）。
本脚本改为：

1. 抽 $\\mathcal Z$，先算 $G_{\\mathcal Z}=\\{\\ell\\in\\mathcal Z^{\\perp}:\\ell A\\in\\mathcal Z^{\\perp}+W\\}$；
2. 只有 $\\dim G_{\\mathcal Z}\\ge q_0$ 才继续；
3. 在 $G_{\\mathcal Z}$ **内部**构造 $\\mathcal L$（行从 $G_{\\mathcal Z}$ 的基里取，保证含 $L_0$、$[C;L]$ 满秩）；
4. 判 $(5b)$（Toeplitz 零度），统计"$q_0$ 阶是否可行"。

与 [q0_scan.py](q0_scan.py)（旧法）比较命中率。

用法：python -u tools/verification/q0_scan_gz.py
"""

import os
import sys
from collections import Counter
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import type3_structured as T3             # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import g_z_criterion as GZc               # noqa: E402

F = Fraction


def build_inside(A, C, L0, G, q):
    L = [list(x) for x in L0]
    for g in G:
        if len(L) == q:
            break
        if LQ.rank([list(x) for x in C] + L + [g]) > LQ.rank([list(x) for x in C] + L):
            L.append(g)
    return L if len(L) == q else None


def main():
    import random
    stats = Counter()
    rows = []
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
                    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    mm = len(K[0])
                    d = n - p - q0
                    if d < 0:
                        continue
                    rng = random.Random(seed * 7 + q0)
                    gz_ok = built = feasible = 0
                    for _ in range(80):
                        if d == 0:
                            Z = []
                            G, B, rS = GZc.G_of(A, C, [[] for _ in range(n)]) if False else (None, None, None)
                            stats['d0'] += 1
                            break
                        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
                        Z = [[sum(K[i][t] * Wm[t][j] for t in range(mm)) for j in range(d)]
                             for i in range(n)]
                        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                            continue
                        G, B, rS = GZc.G_of(A, C, Z)
                        if LQ.rank(G) < q0:
                            continue
                        gz_ok += 1
                        L = build_inside(A, C, L0, G, q0)
                        if L is None:
                            continue
                        built += 1
                        if not LQ.condA(A, C, L):
                            stats['condA_fail'] += 1
                            continue
                        h, s, m, d_fin = T3.fast_dfin(A, C, L)
                        if d_fin == 0:
                            feasible += 1
                    stats['inst'] += 1
                    if feasible:
                        stats['qmin_eq_q0'] += 1
                    elif built:
                        stats['qmin_gt_q0'] += 1
                    else:
                        stats['no_candidate'] += 1
                    rows.append((n, p, r, seed, q0, gz_ok, built, feasible))
                    print(f'n={n} p={p} r={r} seed={seed} q0={q0}: dimG≥q0 的 Z {gz_ok}，'
                          f'构造出 L {built}，(5b) 成立 {feasible}'
                          + ('  ⟹ q_min=q0' if feasible else ''))
    print(f"\n合计：实例 {stats['inst']}；q_min=q0（精确）{stats['qmin_eq_q0']}；"
          f"q_min>q0（仅下界）{stats['qmin_gt_q0']}；无候选 {stats['no_candidate']}")


if __name__ == '__main__':
    main()
