"""type_criterion.py —— 失败类型由整数决定：Type I ⟺ dim(row[C;L_0]+W) ≥ r_1+r

**推导**：$\\mathcal Z\\subseteq K=\\ker[C;L_0]$（$\\dim d$）⟹ $\\mathcal Z^{\\perp}=K^{\\perp}+V$，其中
$V=\\operatorname{span}(v_1,\\dots,v_t)$、$t=q-r$、$V\\cap K^{\\perp}=0$。令
$$S=K^{\\perp}+W=\\operatorname{row}[C;L_0]+\\operatorname{row}[C;CA],\\qquad s_0:=\\dim S .$$
由 B.11，$h=\\dim(\\mathcal Z^{\\perp}+W)=\\dim(S+V)=\\dim S+\\dim\\pi(V)$，其中 $\\pi:\\mathbb C^n\\to\\mathbb C^n/S$。
若 $V\\cap S=0$，则 $\\dim\\pi(V)=t$，于是
$$\\boxed{h=s_0+t=s_0+q-r},$$
**与 $V$ 的选取无关**。因此
$$\\text{Type I}\\iff h\\ge q+r_1\\iff s_0\\ge r_1+r .$$
即失败类型只由 $(s_0,r_1,r,q)$ 这些**整数**决定，与具体增广无关。

本脚本在实例上核验：对每个 $q$，若 $V\\cap S=0$，则所有 $(5a)$-可行样本的 $h$ 都等于 $s_0+q-r$。

用法：python -u tools/verification/type_criterion.py
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
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

F = Fraction


def rowspace(rows):
    out = []
    for r in rows:
        if LQ.rank(out + [r]) > len(out):
            out.append(list(r))
    return out


def main():
    checked = bad = 0
    typeI = typeIII = 0
    for n in (5, 6, 7):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3006):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    CA = LQ.mul(C, A)
                    W = [x[:] for x in C] + [x[:] for x in CA]
                    r1 = LQ.rank(W)
                    S = rowspace([x[:] for x in C] + [x[:] for x in L0] + [x[:] for x in W])
                    s0 = len(S)
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    mm = len(K[0])
                    for q in (q0,):
                        d = n - p - q
                        if d <= 0:
                            continue
                        t = q - r
                        if t < 0:
                            continue
                        rng = __import__('random').Random(seed * 3 + q)
                        for _ in range(20):
                            Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
                            Z = [[sum(K[i][tt] * Wm[tt][j] for tt in range(mm)) for j in range(d)]
                                 for i in range(n)]
                            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                                continue
                            L = ZG.L_from_Z(A, C, L0, Z, q)
                            if L is None or not LQ.condA(A, C, L):
                                continue
                            h = LQ.rank([x[:] for x in L] + [x[:] for x in CA] + [x[:] for x in C])
                            checked += 1
                            if h != s0 + t:
                                bad += 1
                            if h >= q + r1:
                                typeI += 1
                            else:
                                typeIII += 1
                        pred = 'Type I' if s0 >= r1 + r else 'Type III 可能'
                        print(f'n={n} p={p} r={r} seed={seed} q={q}: '
                              f's0={s0} r1={r1} t={t} ⟹ h 应为 {s0 + t}；'
                              f'q+r1={q + r1}；预测 {pred}')
    print(f'\n检查 {checked} 个 (5a)-可行样本：h ≠ s0+t 的 {bad} 个；'
          f'Type I {typeI}、非 Type I {typeIII}')
    assert bad == 0


if __name__ == '__main__':
    main()
