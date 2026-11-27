"""qmin_decide.py —— 逐阶判定 $q_{\\min}$ 的统一入口（小 $n$）

对实例按阶 $q=q_0,\\dots,n-p$ 逐阶处理：

1. **单点情形**（$q=r$，此时 $d=\\dim\\ker[C;L_0]$，可行族只有一个点 $\\mathcal L=L_0$）：直接判 $(5a)/(5b)$；
2. **整数障碍**：算 $s_0=\\dim(\\operatorname{row}[C;L_0]+W)$、$t=q-r$、$h_{\\max}=s_0+\\min(t,n-s_0)$；
   若 $h_{\\max}\\ge q+r_1$ 且候选的 $h$ 都达到（$V\\cap S=0$ 时 $h=s_0+t$），报"可能 Type I"；
3. **抽样**：在谱区抽 $Z$、筛 $(5a)$、判 $(5b)$；报告"可行（带见证）"或"无见证"。

输出：$q_{\\min}$ 的见证（若有）、各低阶的失败类型（整数/谱）。

用法：python -u tools/verification/qmin_decide.py [n p r seed]
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import type3_structured as T3             # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

F = Fraction


def rowspace(rows):
    out = []
    for r0 in rows:
        if LQ.rank(out + [r0]) > len(out):
            out.append(list(r0))
    return out


def decide(A, C, L0, samples=60, verbose=True):
    n, p, r = len(A), len(C), len(L0)
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    r1 = LQ.rank(W)
    s0 = len(rowspace([x[:] for x in C] + [x[:] for x in L0] + [x[:] for x in W]))
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    mm = len(K[0])
    out = []
    for q in range(q0, n - p + 1):
        d = n - p - q
        t = q - r
        h_max = s0 + min(t, n - s0) if t >= 0 else None
        if d < 0:
            continue
        # 单点：d = dim K
        if d == mm:
            L = [list(x) for x in L0]
            if len(L) != q:
                continue
            cond = LQ.condA(A, C, L) if q == len(L) else False
            res = TC.analyse(A, C, L) if cond else None
            ok = bool(cond and res['five_b'])
            out.append((q, 'single-point', cond, ok, res))
            if verbose:
                print(f'  q={q}: 单点（d=dim K={mm}）；(5a)={cond}；(5b)={None if res is None else res["five_b"]}'
                      f'{"；h=" + str(res["h"]) if res else ""}')
            continue
        adm = succ = 0
        witness = None
        his = set()
        rng = __import__('random').Random(q * 97 + q0 * 13 + 7)
        for _ in range(samples):
            if d <= 0:
                break
            Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
            Z = [[sum(K[i][tt] * Wm[tt][j] for tt in range(mm)) for j in range(d)]
                 for i in range(n)]
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            adm += 1
            h, s, m, d_fin = T3.fast_dfin(A, C, L)
            his.add(h)
            if d_fin == 0:
                succ += 1
                if witness is None:
                    witness = L
        if adm == 0:
            out.append((q, 'no-candidate', None, None, None))
            if verbose:
                print(f'  q={q}: 无 (5a)-可行候选（采样 {samples}）')
            continue
        ok = succ > 0
        kind = 'feasible' if ok else ('integer' if all(h >= q + r1 for h in his) else 'spectral')
        out.append((q, kind, adm, ok, witness))
        if verbose:
            print(f'  q={q}: 候选 {adm}，成功 {succ}，h∈{sorted(his)}，q+r1={q + r1}'
                  f' ⟹ {"可行" if ok else ("Type I" if kind == "integer" else "Type III")}')
    return out


def main():
    if len(sys.argv) == 5:
        n, p, r, seed = (int(x) for x in sys.argv[1:])
        made = QR.make_instance(n, p, r, seed * 23 + p * 11 + r)
    else:
        n, p, r, seed = 7, 3, 2, 4001
        made = QR.make_instance(n, p, r, seed * 23 + p * 11 + r)
    if made is None:
        print('实例生成失败')
        return
    A, C, L0 = made
    print(f'实例：n={n} p={p} r={r} seed={seed}')
    out = decide(A, C, L0)
    first = next((q for (q, kind, a, ok, w) in out if ok), None)
    print(f'\nq_min = {first}' if first else '\n未找到可行阶（在 q ≤ n−p 内）')


if __name__ == '__main__':
    main()
