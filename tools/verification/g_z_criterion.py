"""g_z_criterion.py —— $(5a)$ 的 $\\mathcal Z$-层判据：$\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$

对固定 $\\mathcal Z$（$\\operatorname{row}[C;\\mathcal L]=\\mathcal Z^{\\perp}$）定义
$$G_{\\mathcal Z}:=\\bigl\\{\\ell\\in\\mathcal Z^{\\perp}:\\ \\ell A\\in\\mathcal Z^{\\perp}+W\\bigr\\},\\qquad W=\\operatorname{row}[C;CA].$$
则（按定义）
$$(5a)\\iff \\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}.$$
于是：

* **$\\mathcal Z$-层的必要条件**：$\\dim G_{\\mathcal Z}\\ge q$（否则没有 $q$ 维补能落在 $G$ 里）；
* **补是有关的**：固定 $\\mathcal Z$ 后，只有落在 $G_{\\mathcal Z}$ 里的补满足 $(5a)$——
  所以 $(5a)$ **不是** $\\mathcal Z$ 的函数（此前"只依赖 $\\mathcal Z$"的说法是错的）。

本脚本核验：$(5a)\\iff\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$（逐点），
以及 $\\dim G_{\\mathcal Z}\\ge q$ 的必要性（用 admissible 样本检验）。

用法：python -u tools/verification/g_z_criterion.py
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

F = Fraction


def G_of(A, C, Z):
    n = len(A)
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    ZT = [[Z[i][j] for i in range(n)] for j in range(len(Z[0]))]
    B = [list(x) for x in LQ.nullspace(ZT)]          # Z⊥
    S = [x[:] for x in B] + [x[:] for x in W]
    rS = LQ.rank(S)
    G = []
    for b in B:
        bA = LQ.mul([b], A)[0]
        if LQ.rank(S + [bA]) == rS:
            G.append(b)
    return G, B, rS


def in_span(rows, v):
    return LQ.rank([r[:] for r in rows] + [v]) == LQ.rank([r[:] for r in rows])


def main():
    name = 'diag-distinct-n7'
    A = T3.diag_family(7, [0, 1, 2, 3])
    n, p, r = 7, 2, 1
    import random
    rngC = random.Random(sum(ord(ch) for ch in name) * 13 + p * 17)
    C = None
    for _ in range(60):
        cand = [[F(rngC.randrange(2)) for _ in range(n)] for _ in range(p)]
        if LQ.rank(cand) == p and LQ.rank(T3.obs_matrix(A, cand)) == n:
            C = cand
            break
    L0 = T3.pick_L0(A, C, r, seed=sum(ord(ch) for ch in name) * 7 + p * 31 + r)
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    mm = len(K[0])
    d = n - p - q0
    print(f'{name}: n={n} p={p} q0={q0} d={d} dimK={mm}')
    rng = random.Random(17)
    ok_iff = 0
    bad_iff = 0
    need = Counter()
    for _ in range(300):
        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
        Z = [[sum(K[i][t] * Wm[t][j] for t in range(mm)) for j in range(d)] for i in range(n)]
        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            continue
        G, B, rS = G_of(A, C, Z)
        dimG = LQ.rank(G)
        L = ZG.L_from_Z(A, C, L0, Z, q0)
        if L is None:
            continue
        cond = LQ.condA(A, C, L)
        inG = all(in_span(G, list(row)) for row in L)
        if cond == inG:
            ok_iff += 1
        else:
            bad_iff += 1
        need[(dimG >= q0, cond)] += 1
    print(f'(5a) ⟺ row L ⊆ G_Z：一致 {ok_iff}，不一致 {bad_iff}')
    print(f'(dim G_Z ≥ q0, (5a)) 的联合计数：{dict(need)}')
    assert bad_iff == 0


if __name__ == '__main__':
    main()
