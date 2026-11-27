"""b27_check.py —— 核验 B.27 的关键断言：

**B.27（Class I 的 $q_{\\min}=n-1$）**：$p=r=1$、$(c,A)$ 与 $(\\ell,A)$ 可观测、$q\\le n-2$、$\\mathcal L$ 可容许 ⟹ $(5b)$ 失败。
证明骨架：$\\mathcal V=\\mathcal Z^\\perp$（$\\dim=q+1$），$h=\\dim(\\mathcal V+\\langle cA\\rangle)\\in\\{q+1,q+2\\}$；
* 若 $cA\\notin\\mathcal V$：$h=q+2$ ⟹ B.22 ⟹ 失败；
* 若 $cA\\in\\mathcal V$：$(5a)$ ⟹ $\\mathcal VA\\subseteq\\mathcal V$ ⟹ $cA^k\\in\\mathcal V$ 对一切 $k$ ⟹
  $\\mathbb C^n=\\operatorname{span}\\{cA^k\\}\\subseteq\\mathcal V$ ⟹ $n\\le q+1$ ⟹ 与 $q\\le n-2$ 矛盾。

本脚本检查：
1. 在 $q\\le n-2$ 的可容许样本里，**是否存在** Case B（$cA\\in\\mathcal V$）？（应无）
2. 所有此类样本是否都 $(5b)$ 失败？（应全失败）
3. Case B 的样本（若存在）是否都落在 $q\\ge n-1$？

用法：python -u tools/verification/b27_check.py
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
import decide_symbolic as DS              # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction


def main():
    rng = random.Random(20261120)
    st = Counter()
    for trial in range(2500):
        n = rng.choice([4, 5, 6])
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
        for q in range(q0, n0):
            d = n - 1 - q
            if d <= 0 or d > k:
                continue
            for rows in itertools.combinations(range(k), d):
                Z = DS.Z_from_theta(A, C, L0, q, rows, [F(0)] * (d * (k - d)))
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                try:
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                except AssertionError:
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                st['可容许样本'] += 1
                # 𝒱 = 𝒵^⊥
                Zt = [[Z[i][j] for i in range(n)] for j in range(d)]
                ns = ZG.ker_cols(Zt)
                dZ = len(ns[0]) if (ns and ns[0]) else 0
                Vrows = [[ns[i][t] for i in range(n)] for t in range(dZ)]
                cA_in_V = LQ.rank(Vrows + [list(x) for x in CA]) == dZ
                tag = 'CaseB' if cA_in_V else 'CaseA'
                st[f'{tag} 样本'] += 1
                ok, _w = OT.observability_ok(A, C, L)
                st[f'{tag} 且 (5b) 失败' if not ok else f'{tag} 且 (5b) 成立'] += 1
                if cA_in_V:
                    st[f'CaseB 的 q 与 n-1 关系: q={q} n-1={n-1}'] += 1
                break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
