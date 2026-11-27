"""middle_strata.py —— 中间层（0 < s < dim V）的实验刻画

**问题**：B.16 给出了三层判据，但中间层的失败"有多常见"未定。本轮按构造采样各层：
* 取 $W=V\\cap K$（$\dim w$）；
* 对每个 $s\\le\\min(d,w)$，随机取 $s$ 维 $S\\subseteq W$，再随机扩成 $\\mathcal Z$（$\\dim d$，$S\\subseteq\\mathcal Z\\subseteq K$）；
* 统计每个 $s$ 层上的**可容许率**与**失败率**（失败用 B.12 可观性判据）。

**假设（待检验）**：$s$ 越大越"可行"（因为 $J_{\\mathcal Z}$ 的秩越小，$J_{\\mathcal Z}x\\ne0$ 越难满足），
极端 $s=\\dim V$ 时完全可行（B.16(a)）。

用法：python -u tools/verification/middle_strata.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter, defaultdict

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction


def rand_combination(pool, k, rng):
    """从 pool（n×m 基）里随机取 k 个线性组合，返回 n×k 矩阵（可能退秩，调用方检查）。"""
    n = len(pool)
    m = len(pool[0]) if (pool and pool[0]) else 0
    if m == 0 or k == 0:
        return [[] for _ in range(n)] if k == 0 else None
    out = [[F(0)] * k for _ in range(n)]
    for j in range(k):
        coef = [F(rng.randrange(-2, 3)) for _ in range(m)]
        for i in range(n):
            out[i][j] = sum(pool[i][t] * coef[t] for t in range(m))
    return out


def build_Z(K, W, d, s, rng, tries=40):
    """构造 dim d 的 Z ⊆ K，含一个 s 维 S ⊆ W（即 dim(V∩Z) ≥ s）。返回 (Z, s_actual) 或 None。"""
    n = len(K)
    dK = len(K[0]) if (K and K[0]) else 0
    if s == 0:
        for _ in range(tries):
            Z = rand_combination(K, d, rng)
            if Z is None or ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            return Z, 0
        return None
    w = len(W[0]) if (W and W[0]) else 0
    if s > w or s > d:
        return None
    for _ in range(tries):
        S = rand_combination(W, s, rng)
        if S is None or ZG.bool_rank(ZG.cols_to_rows(S)) != s:
            continue
        R = rand_combination(K, d - s, rng) if d > s else [[] for _ in range(n)]
        if R is None or (d > s and ZG.bool_rank(ZG.cols_to_rows(R)) != d - s):
            continue
        Z = [[S[i][j] for j in range(s)] + [R[i][j] for j in range(d - s)] for i in range(n)]
        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            continue
        return Z, s
    return None


def main():
    rng = random.Random(20261104)
    st = Counter()
    per_s = defaultdict(lambda: [0, 0, 0])     # s -> [samples, admissible, failing]
    for trial in range(600):
        n = rng.choice([6, 7, 8])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r >= n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank(QR.observability_matrix(A, C)) != n:
            continue
        if LQ.rank(QR.observability_matrix(A, L0)) != n:
            continue
        CA = LQ.mul(C, A)
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (V and V[0] and K and K[0]):
            continue
        dV = len(V[0]); dK = len(K[0])
        # W = V ∩ K
        VK = [[V[i][j] for j in range(dV)] + [K[i][j] for j in range(dK)] for i in range(n)]
        w = dV + dK - LQ.rank([[VK[i][j] for i in range(n)] for j in range(dV + dK)])
        if w == 0:
            st['VcapK=0（只有 s=0 层）'] += 1
            continue
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        n0 = LQ.rank(QR.observability_matrix(A, C))
        Wb = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA] + [list(x) for x in L0])  # = V∩K 的基
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d <= 0 or d > dK:
                continue
            for s in range(0, min(d, w) + 1):
                for _ in range(6):
                    built = build_Z(K, Wb, d, s, rng)
                    if built is None:
                        continue
                    Z, s_act = built
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                    if L is None:
                        continue
                    st['samples'] += 1
                    per_s[s][0] += 1
                    if not LQ.condA(A, C, L):
                        continue
                    per_s[s][1] += 1
                    ok, _ = OT.observability_ok(A, C, L)
                    if not ok:
                        per_s[s][2] += 1
    print('总体：', dict(st))
    print(f'\n{"s":>2} {"样本":>6} {"可容许":>6} {"失败":>6} {"失败/可容许":>12}')
    for s in sorted(per_s):
        n_, adm, fail = per_s[s]
        rate = f'{fail}/{adm}' if adm else '—'
        print(f'{s:>2} {n_:>6} {adm:>6} {fail:>6} {rate:>12}')


if __name__ == '__main__':
    main()
