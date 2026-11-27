"""intersection_law.py —— $h=q+r_1-\\delta$ 的 $\delta$ 与"$W\\cap Z^{\\perp}$ 的维数"的关系

猜测的关系：设 $W=\\operatorname{row}[C;CA]$（$\\dim=r_1$）、$\\operatorname{row}C$（$\\dim=p$）、
$\\mathcal Z=\\ker[C;\\mathcal L]$（$\\dim d=n-p-q$）。则 $\\operatorname{row}\\mathcal L$ 是 $\\operatorname{row}C$ 在
$\\mathcal Z^{\\perp}$ 里的补，且
$$h=q+r_1-\\delta,\\qquad \\delta=\\dim(\\operatorname{row}\\mathcal L\\cap W),$$
$$\\delta\\le \\dim(W\\cap\\mathcal Z^{\\perp})-p=:\\delta_{\\rm cap}.$$
本脚本在公开例子与结构化实例上逐点计算 $\\dim(W\\cap\\mathcal Z^{\\perp})$、$\\delta$、$h$，检验：

* 是否总有 $\\delta=\\delta_{\\rm cap}$（即"补"总是把 $W$ 的额外部分吃进来）；
* 是否 $\\delta_{\\rm cap}=0\\iff h=q+r_1\\iff$ B.9 触发。

用法：python -u tools/verification/intersection_law.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import type3_structured as T3             # noqa: E402
import importlib.util as iu               # noqa: E402

F = Fraction


def annih(Z):
    n = len(Z)
    d = len(Z[0])
    ZT = [[Z[i][j] for i in range(n)] for j in range(d)]
    return [list(x) for x in LQ.nullspace(ZT)]


def dim_intersection(rows1, rows2):
    return len(rows1) + len(rows2) - LQ.rank([r[:] for r in rows1] + [r[:] for r in rows2])


def report(tag, A, C, L, Z):
    n, p = len(A), len(C)
    q = len(L)
    CA = LQ.mul(C, A)
    W = [r[:] for r in C] + [r[:] for r in CA]
    r1 = LQ.rank(W)
    Zp = annih(Z)
    dWZ = dim_intersection(W, Zp)
    h, s, m, d_fin = T3.fast_dfin(A, C, L)
    # δ = dim(row L ∩ W)
    delta = dim_intersection([r[:] for r in L], W)
    print(f'  {tag}: n={n} p={p} q={q} r1={r1} | dim(W∩Z⊥)={dWZ} (p={p}) '
          f'⟹ δ_cap={dWZ - p}；实际 δ={delta}；h={h}；q+r1={q + r1}；'
          f'B.9={"是" if h >= q + r1 else "否"}')


def main():
    spec = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m = iu.module_from_spec(spec)
    spec.loader.exec_module(m)
    A, C, L0 = m.A, m.C, m.L0
    n, p, r = len(A), len(C), len(L0)
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    mm = len(K[0])
    import random
    print('=== 公开例子 ===')
    for q in (3, 4, 5):
        d = n - p - q
        rng = random.Random(100 + q)
        shown = 0
        for _ in range(40):
            Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
            Z = [[sum(K[i][t] * Wm[t][j] for t in range(mm)) for j in range(d)] for i in range(n)]
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            report(f'q={q}', A, C, L, Z)
            shown += 1
            if shown >= 2:
                break
    print('\n=== 结构化实例（q0 阶） ===')
    name = 'jordan-n6'
    A2 = T3.jordan_family(6, [1, 2])
    rngC = random.Random(sum(ord(ch) for ch in name) * 13 + 2 * 17)
    C2 = None
    for _try in range(60):
        cand = [[F(rngC.randrange(2)) for _ in range(6)] for _ in range(2)]
        if LQ.rank(cand) != 2:
            continue
        if LQ.rank(T3.obs_matrix(A2, cand)) != 6:
            continue
        C2 = cand
        break
    L02 = T3.pick_L0(A2, C2, 1, seed=sum(ord(ch) for ch in name) * 7 + 2 * 31 + 1)
    print(f'  实例：{name} p=2 r=1；L0 存在={L02 is not None}')
    if L02 is not None:
        from c208_q0_lower_bound import eta_and_q0
        q0 = eta_and_q0(A2, C2, L02)[0]
        K2 = ZG.ker_cols([list(x) for x in C2] + [list(x) for x in L02])
        mm2 = len(K2[0])
        d2 = 6 - 2 - q0
        rng2 = random.Random(999)
        shown = 0
        for _ in range(40):
            Wm = [[F(rng2.randrange(-3, 4)) for _ in range(d2)] for _ in range(mm2)]
            Z = [[sum(K2[i][t] * Wm[t][j] for t in range(mm2)) for j in range(d2)] for i in range(6)]
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d2:
                continue
            L = ZG.L_from_Z(A2, C2, L02, Z, q0)
            if L is None or not LQ.condA(A2, C2, L):
                continue
            report(f'q0={q0}', A2, C2, L, Z)
            shown += 1
            if shown >= 2:
                break


if __name__ == '__main__':
    main()
