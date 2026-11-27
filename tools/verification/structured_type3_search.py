"""structured_type3_search.py —— 按专家 2026-11-04 §Step 2 的结构化搜索：找第二个"整族 Type III"实例

搜索策略（不是随机采样，而是**按结构定向**）：

1. **必要条件筛选**（便宜，全部精确）：
   * $\\varepsilon=0$ —— 由 B.13d 的三情形秩判据直接判（$\\operatorname{rank}U_0=0$；$=1$ 时
     $\\operatorname{im}U_1\\subseteq\\operatorname{im}U_0$；$\\ge2$ 时 $U_1=\\alpha U_0$）；
   * **维数取等** $q_0-r=n-r_1-1$（整族覆盖判据能成立的唯一维数情形）；
   * $(C,A)$ 可观测、$L_0$ 可观测（否则 $q_{\\min}=\\infty$，无意义）。
2. **整族失败检验**：对通过筛选的实例，在 $q_0$ 阶枚举全部图卡、每卡取若干 $\\theta$，用 Toeplitz 判据
   逐候选判 $(5b)$；若**全部失败**则为候选，再由逐图卡符号 gcd 复核（C4 用的就是这条路线）。

**注意**：这里第二步用稠密 $\\theta$ 的枚举，只用于**找候选**；结论必须由符号 gcd 或显式证书确认
（纪律：薄集不许采样）。

用法：python -u tools/verification/structured_type3_search.py
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
import toeplitz_criterion as TC           # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction


def epsilon_zero(A, C, L0):
    """B.13d 的三情形判据：返回 (是否 eps=0, rank U0, 说明)。"""
    n = len(A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    dV = len(V[0]) if (V and V[0]) else 0
    r = len(L0)
    if dV == 0:
        return True, 0, 'dim V = 0'
    M0 = [[sum(L0[i][j] * V[j][k] for j in range(n)) for k in range(dV)] for i in range(r)]
    M1 = [[sum(sum(L0[i][j] * A[j][m] for j in range(n)) * V[m][k] for m in range(n))
           for k in range(dV)] for i in range(r)]
    rk0 = LQ.rank(M0) if M0 else 0
    if rk0 == 0:
        return True, 0, 'rank U0 = 0'
    if rk0 == 1:
        stacked = [M0[i][:] + M1[i][:] for i in range(r)]
        return LQ.rank(stacked) == rk0, 1, 'rank U0 = 1：像包含'
    alpha = None
    for i in range(r):
        for k in range(dV):
            if M0[i][k] != 0:
                alpha = M1[i][k] / M0[i][k]
                break
        if alpha is not None:
            break
    ok = alpha is not None and all(M1[i][k] == alpha * M0[i][k] for i in range(r) for k in range(dV))
    return ok, rk0, f'rank U0 ≥ 2：α={alpha}'


def whole_family_fails(A, C, L0, q, max_theta=3):
    """在 q 阶枚举全部图卡与若干稠密 θ；返回 (全失败?, 总数, 可行数, Type I 数, Type III 数)。"""
    n = len(A)
    p, r = len(C), len(L0)
    r1 = LQ.rank([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    tot = feas = typeI = typeIII = 0
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d <= 0 or d > k:
        return None, 0, 0, 0, 0
    nv = d * (k - d)
    for rows in itertools.combinations(range(k), d):
        vals_list = [tuple(F(b) for b in [v] * nv) for v in range(max_theta)]
        for th in vals_list:
            Z = DS.Z_from_theta(A, C, L0, q, rows, th)
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            tot += 1
            try:
                res = TC.analyse(A, C, L)
            except AssertionError:
                continue
            if res['five_b']:
                feas += 1
            elif res['h'] >= q + r1:
                typeI += 1
            else:
                typeIII += 1
    if tot == 0:
        return None, 0, 0, 0, 0
    return (feas == 0), tot, feas, typeI, typeIII


def main():
    rng = random.Random(20261104)
    stat = Counter()
    cands = []
    for trial in range(1500):
        n = rng.choice([6, 7])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r > n:
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
        if n0 != n:                       # 要求 (C,A) 可观测
            continue
        if LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        stat['observable'] += 1
        eps0, rk0, why = epsilon_zero(A, C, L0)
        if not eps0:
            continue
        stat['eps0'] += 1
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        r1 = LQ.rank([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
        if q0 - r != n - r1 - 1:
            continue
        stat['tight'] += 1
        out = whole_family_fails(A, C, L0, q0)
        if out[0] is None:
            continue
        fails, tot, feas, typeI, typeIII = out
        stat['tested'] += 1
        if fails and typeIII == tot:
            stat['whole_family_typeIII'] += 1
            cands.append((n, p, r, rk0, q0, r1, tot))
            print(f'  ★ 整族 Type III 候选：n={n} p={p} r={r} rankU0={rk0} q0={q0} r1={r1} '
                  f'（{tot} 个候选全为 Type III）')
        elif fails:
            stat['whole_family_typeI'] += 1
    print('\n统计：', dict(stat))
    if cands:
        print(f'\n整族 Type III 候选 {len(cands)} 个（需符号 gcd 复核）：')
        for c in cands[:10]:
            print('   n=%d p=%d r=%d rankU0=%d q0=%d r1=%d 候选数=%d' % c)
    else:
        print('\n未找到新的整族 Type III 实例（在 ε=0 且维数取等的筛选后）。')


if __name__ == '__main__':
    main()
