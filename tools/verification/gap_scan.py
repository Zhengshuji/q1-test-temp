"""gap_scan.py —— 正阶差实例的**阶差分布**：从 $q_0$ 往上扫，找第一个可行的阶

对结构化实例族里 $q_0$ 阶不可行的实例，在 $q=q_0,q_0+1,q_0+2$ 上各抽 $Z$-参数化候选：
先筛 $(5a)$，再见 $(5b)$。找到的第一个可行阶给出 $q_{\\min}$ 的上界；
由 $q_0$ 阶不可行（唯一性或全失败），可判定 $q_{\\min}$ 的精确值或给出下界。

用法：python -u tools/verification/gap_scan.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import z_generator as ZG                  # noqa: E402
import type3_structured as T3             # noqa: E402
import toeplitz_criterion as TC           # noqa: E402

F = Fraction


def build_instance(name, A, p, r):
    n = len(A)
    import random
    rngC = random.Random(sum(ord(ch) for ch in name) * 13 + p * 17)
    C = None
    for _try in range(60):
        cand = [[F(rngC.randrange(2)) for _ in range(n)] for _ in range(p)]
        if LQ.rank(cand) != p:
            continue
        if LQ.rank(T3.obs_matrix(A, cand)) != n:
            continue
        C = cand
        break
    if C is None:
        return None
    L0 = T3.pick_L0(A, C, r, seed=sum(ord(ch) for ch in name) * 7 + p * 31 + r)
    if L0 is None:
        return None
    O = T3.obs_matrix(A, C)
    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
        return None
    return A, C, L0


def scan_orders(A, C, L0, q0, orders, n_samples=60):
    out = []
    for q in orders:
        if q < len(L0) or q > len(A) - len(C):
            continue
        seed = sum(ord(ch) for ch in 'x') * 0 + q * 101 + q0 * 37
        cands = ZG.sample_L_at_order(A, C, L0, q, n_samples, seed=seed)
        feas = 0
        for L in cands:
            h, s, m, d_fin = T3.fast_dfin(A, C, L)
            if d_fin == 0:
                feas += 1
        out.append((q, len(cands), feas))
    return out


def main():
    families = []
    for n in (5, 6, 7):
        families.append((f'diag-distinct-n{n}', T3.diag_family(n, [0, 1, 2, 3])))
        families.append((f'jordan-n{n}', T3.jordan_family(n, [1, 2])))
    rows = []
    for name, A in families:
        n = len(A)
        for p in (2, 3):
            if p >= n:
                continue
            for r in (1, 2):
                if p + r > n:
                    continue
                made = build_instance(name, A, p, r)
                if made is None:
                    continue
                A1, C, L0 = made
                q0 = Q0.eta_and_q0(A1, C, L0)[0]
                orders = [q for q in (q0, q0 + 1, q0 + 2) if len(L0) <= q <= n - p]
                res = scan_orders(A1, C, L0, q0, orders)
                first = next((q for q, adm, feas in res if feas > 0), None)
                gap = None if first is None else first - q0
                rows.append((name, n, p, r, q0, res, gap))
                print(f'{name:18s} n={n} p={p} r={r} q0={q0}: ' +
                      ' '.join(f'q={q}:{feas}/{adm}' for q, adm, feas in res) +
                      (f'  ⟹ q_min={first}（gap={gap}）' if first else '  ⟹ ≤q0+2 内未找到'))
    gaps = [row[6] for row in rows if row[6] is not None]
    print(f'\n找到可行阶的实例 {len(gaps)}/{len(rows)}；gap 分布 {sorted(gaps)}')


if __name__ == '__main__':
    main()
