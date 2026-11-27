"""dimY_vs_qr.py —— 在 $r=1$ 的实例上检验遮蔽判据 $\\dim Y\\ge q-r$

专家 2026-11-03 §4.2/§5.3 要求：分类 $\\dim Y$ 并与 $q-r$ 比较。
坏点映射在 $r=1$ 时普遍有定义（$z(x)\\in K$ 自动成立），所以本脚本只取 $r=1$ 的实例：

对每个实例、$q=q_0$：

1. 算 $h$（对该阶的可行候选是否恒为 $n$）；
2. 算 $\\dim Y$（Jacobian 秩减一，精确有理插值）；
3. 抽样判 $(5b)$ 得到实际可行性；
4. 检验：$h=n$ 且 $\\dim Y\\ge q-r$ ⟹ 预测"该阶无解"。

用法：python -u tools/verification/dimY_vs_qr.py
"""

import os
import sys
from collections import Counter
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import type3_structured as T3             # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import dim_Y as DY                        # noqa: E402

F = Fraction


def main():
    import random
    stats = Counter()
    rows = []
    for n in (5, 6, 7):
        for p in (1, 2):
            for r in (1,):
                if p + r > n:
                    continue
                for seed in range(3000, 3008):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    CA = LQ.mul(C, A)
                    W = [x[:] for x in C] + [x[:] for x in CA]
                    r1 = LQ.rank(W)
                    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    mm = len(K[0])
                    d = n - p - q0
                    if d <= 0:
                        continue
                    # 抽样判可行性 + 收集 h
                    rng = random.Random(seed * 7 + q0)
                    adm = succ = 0
                    hs = set()
                    for _ in range(30):
                        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
                        Z = [[sum(K[i][tt] * Wm[tt][j] for tt in range(mm)) for j in range(d)]
                             for i in range(n)]
                        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                            continue
                        L = ZG.L_from_Z(A, C, L0, Z, q0)
                        if L is None or not LQ.condA(A, C, L):
                            continue
                        adm += 1
                        h = LQ.rank([x[:] for x in L] + [x[:] for x in CA] + [x[:] for x in C])
                        hs.add(h)
                        if T3.fast_dfin(A, C, L)[3] == 0:
                            succ += 1
                    if adm == 0:
                        continue
                    my, note = DY.dim_Y(A, C, L0)
                    qr = q0 - 1
                    h_eq_n = (hs == {n})
                    pred = None
                    if h_eq_n and my is not None:
                        pred = (my >= qr)
                    actual_infeasible = (succ == 0)
                    stats['inst'] += 1
                    if pred is None:
                        stats['n/a'] += 1
                    elif pred == actual_infeasible:
                        stats['consistent'] += 1
                    else:
                        stats['inconsistent'] += 1
                    rows.append((n, p, q0, seed, r1, my, qr, sorted(hs), pred, actual_infeasible))
                    print(f'n={n} p={p} q0={q0} seed={seed}: r1={r1} h={sorted(hs)} '
                          f'dimY={my} q-r={qr} ⟹ 预测{"无解" if pred else ("有解" if pred is False else "不可用")}；'
                          f'实际{"无解" if actual_infeasible else "有解"}'
                          + ('  ✗不一致' if (pred is not None and pred != actual_infeasible) else ''))
    print('\n统计：', dict(stats))


if __name__ == '__main__':
    main()
