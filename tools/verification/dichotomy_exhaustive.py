"""dichotomy_exhaustive.py —— $d=2$ 上**穷举整个 $\\mathcal L$ 族**检验二分假设

对 $p=r=1$、$n=5$（$d=2$ 时 $q=2$）：固定 $\\mathcal Z$，$\\mathcal L$ 的行是
$$\\operatorname{row}\\mathcal L=\\langle\\ell,\\ r\\rangle,\\qquad r\\in\\mathcal Z^\\perp,\\ r\\notin\\langle c,\\ell\\rangle ,$$
即一族一维补（$\\operatorname{Gr}(1,\\mathcal Z^\\perp/\\langle c,\\ell\\rangle)$）。

本脚本：对每个 $\\mathcal Z$（图卡 × θ）、对 $r$ 取 $\theta\\in\\{-3,\\dots,3\\}$ 加 6 个随机值，
逐 $\\mathcal L$ 查 $(5a)$ 与 $(5b)$，统计"可容许且谱可行"的样本数。

若恒为 0 ⟹ 二分假设在小 $n$ 上**穷举成立**（在该参数网格上）。

用法：python -u tools/verification/dichotomy_exhaustive.py
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
    rng = random.Random(20261118)
    st = Counter()
    for trial in range(1200):
        n = 5
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
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        q = 2
        if q < q0:
            continue
        d = n - 1 - q                     # = 2
        if d != 2 or d > k:
            continue
        for rows in itertools.combinations(range(k), d):
            Z = DS.Z_from_theta(A, C, L0, q, rows, [F(0)] * (d * (k - d)))
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            st['Z 样本'] += 1
            # 𝒵^⊥ 的基
            Zt = [[Z[i][j] for i in range(n)] for j in range(d)]
            ns = ZG.ker_cols(Zt)
            dZ = len(ns[0]) if (ns and ns[0]) else 0
            if dZ < q:
                continue
            # 族：row L = ⟨ℓ, r⟩，r ∈ span(ns)，且 {ℓ, r, c} 线性无关
            ths = [[F(a)] for a in range(-3, 4)] + [[F(rng.randrange(-4, 5))] for _ in range(6)]
            adm = feas = 0
            for th in ths:
                r = [sum(ns[i][0] * th[0] for i in range(n))]  # 占位
                r = [ns[i][0] * th[0] for i in range(n)]
                # 要求 r 与 ℓ、c 线性无关（否则 rank[C;L] ≠ p+q）
                L = [list(x) for x in L0] + [r]
                if LQ.rank(L) != q:
                    continue
                if LQ.rank([list(x) for x in C] + L) != p + q:
                    continue
                if not LQ.condA(A, C, L):
                    continue
                adm += 1
                ok, _w = OT.observability_ok(A, C, L)
                if ok:
                    feas += 1
            st['族内可容许'] += adm
            st['族内谱可行'] += feas
            if adm > 0 and feas > 0:
                st['★ 二分假设反例'] += 1
            break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
