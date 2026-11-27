"""class_I_scan.py —— Class I（$p=r=1$）的阶谱数据：$q_{\\min}=q_0$ 有多常见？

**背景**（B.18）：$p=r=1$、$(c,A)$ 可观测时 $r_1=2$、$\\dim V=\\dim K=n-2$、$\\dim(V\\cap K)\\ge n-3$、
且 $\\mathcal Z\\subseteq V\\cap K$ 时商铅笔形状为 $(q+1)\\times(q-1)$。
$q=2$ 时"最大交集候选"$\\mathcal Z=V\\cap K$ 不可容许（77/77），故候选必须落在 $s<d$ 的层。

**本轮问题**：对 $p=r=1$，$q=q_0$ 阶到底有没有可行增广？（即 $q_{\\min}=q_0$ 还是更大？）
做法：枚举**全部**标准图卡（$\\binom{k}{d}$ 个）× 若干 $\\theta$，逐候选检查 $(5a)$ 与 $(5b)$（B.12）。

用法：python -u tools/verification/class_I_scan.py
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
import observability_test as OT           # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction


def main():
    rng = random.Random(20261104)
    st = Counter()
    rows = []
    for trial in range(900):
        n = rng.choice([4, 5, 6, 7])
        p = r = 1
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        if LQ.rank(C) != 1 or LQ.rank(L0) != 1:
            continue
        if LQ.rank([list(x) for x in C] + L0) != 2:
            continue
        O = QR.observability_matrix(A, C)
        n0 = LQ.rank(O)
        if n0 != n:
            continue
        if LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        for q in range(q0, n0):          # 测 q0, q0+1, q0+2
            if q > q0 + 2:
                break
            d = n - 1 - q
            if d <= 0 or d > k:
                continue
            tot = feas = adm = 0
            for rows_ in itertools.combinations(range(k), d):
                nv = d * (k - d)
                ths = [[F(b)] * nv for b in range(0, 4)]
                for _ in range(6):
                    ths.append([F(rng.randrange(-3, 4)) for _ in range(nv)])
                for th in ths:
                    Z = DS.Z_from_theta(A, C, L0, q, rows_, th)
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                        continue
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                    if L is None or not LQ.condA(A, C, L):
                        continue
                    tot += 1
                    ok, _ = OT.observability_ok(A, C, L)
                    if ok:
                        feas += 1
            st[f'n={n} q=q0+{q - q0}:样本'] += 1
            if feas:
                st[f'n={n} q=q0+{q - q0}:有可行'] += 1
            else:
                st[f'n={n} q=q0+{q - q0}:无可行'] += 1
            rows.append((n, q0, q, tot, feas))
    print(f'{"n":>2} {"q0":>3} {"q":>3} {"候选":>5} {"可行":>4}')
    for r in rows[:20]:
        print(f'{r[0]:>2} {r[1]:>3} {r[2]:>3} {r[3]:>5} {r[4]:>4}')
    print('\n统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
