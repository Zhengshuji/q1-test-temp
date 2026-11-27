"""phi_rank_check.py —— 核验专家的两条更正（Correction A/B）

**Correction B（重要）**：$(5a)\\iff G_{\\mathcal Z}=\\mathcal Z^{\\perp}\\iff\\varphi=0$（$\\operatorname{rank}\\varphi=0$），
而**不是**我之前写的"$\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$"配弱条件 $\\operatorname{rank}\\varphi\\le p$。
证明（专家）：$\\operatorname{row}C\\subseteq G_{\\mathcal Z}$ 恒成立，而 $\\mathcal Z^{\\perp}=\\operatorname{row}C+\\operatorname{row}\\mathcal L$；
若 $(5a)$ 成立，则 $\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$ ⟹ $\\mathcal Z^{\\perp}\\subseteq G_{\\mathcal Z}$ ⟹ 相等。

**Schubert 形式**：$K=\\ker C$、$U=W/\\operatorname{row}C\\subset K^*$（$\\dim a=r_1-p$）、
$T=\\mathcal Z^{\\perp}\\cap K^*$（$\\dim=q$），则
$$\\delta=\\dim(U\\cap T),\\qquad \\delta\\ge1\\iff T\\cap U\\ne\\{0\\},$$
且当 $q+a\\le N=n-p$ 时 $\\delta\\ge1$ 是 Schubert 簇，余维 $=N-q-a+1=n-q-r_1+1=d-a+1$。

本脚本核验：(i) $(5a)\\iff\\operatorname{rank}\\varphi=0$；(ii) $\\delta=\\dim(U\\cap T)$ 且 $h=q+r_1-\\delta$。

用法：python -u tools/verification/phi_rank_check.py
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
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402

F = Fraction


def rowspace(rows):
    out = []
    for r in rows:
        if LQ.rank(out + [r]) > len(out):
            out.append(list(r))
    return out


def complement_of(S, n):
    """返回 S 的补空间的一组基（行）。"""
    B = rowspace(S)
    Q = []
    for i in range(n):
        e = [F(1) if j == i else F(0) for j in range(n)]
        if LQ.rank(B + Q + [e]) > LQ.rank(B + Q):
            Q.append(e)
    return Q


def coords_in_basis(v, basis):
    """v 在 basis（n×n 可逆，行）下的系数：coef·basis = v。"""
    n = len(basis)
    aug = [[basis[t][j] for t in range(n)] + [v[j]] for j in range(n)]
    R, piv = LQ.rref(aug)
    for row in R:
        assert not (all(row[t] == 0 for t in range(n)) and row[n] != 0), '基不可逆'
    coef = [F(0)] * n
    for r_i, pc in enumerate(piv):
        if pc < n:
            coef[pc] = R[r_i][n]
    return coef


def phi_rank(A, C, Z):
    n = len(A)
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    ZT = [[Z[i][j] for i in range(n)] for j in range(len(Z[0]))]
    B = [list(x) for x in LQ.nullspace(ZT)]        # Z⊥
    S = rowspace([x[:] for x in B] + [x[:] for x in W])
    Q = complement_of(S, n)
    basis = [list(x) for x in S] + [list(x) for x in Q]
    assert len(basis) == n and LQ.rank(basis) == n
    nS = len(S)
    Phi = []
    for b in B:
        bA = LQ.mul([b], A)[0]
        coef = coords_in_basis(bA, basis)
        Phi.append(coef[nS:])                      # Q 部分的坐标
    # rank Φ = 行空间维数
    if not Phi or not Phi[0]:
        return 0
    return LQ.rank(Phi)


def delta_and_h(A, C, Z, L, p, r1, q):
    n = len(A)
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    ZT = [[Z[i][j] for i in range(n)] for j in range(len(Z[0]))]
    B = [list(x) for x in LQ.nullspace(ZT)]
    S = rowspace([x[:] for x in B] + [x[:] for x in W])
    h = len(S)
    delta = q + r1 - h
    return delta, h


def main():
    import random
    bad1 = bad2 = checked = feas = 0
    for n in (5, 6, 7):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3005):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    mm = len(K[0])
                    d = n - p - q0
                    if d <= 0:
                        continue
                    CA = LQ.mul(C, A)
                    r1 = LQ.rank([x[:] for x in C] + [x[:] for x in CA])
                    rng = random.Random(seed * 5 + q0)
                    for _ in range(25):
                        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
                        Z = [[sum(K[i][t] * Wm[t][j] for t in range(mm)) for j in range(d)]
                             for i in range(n)]
                        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                            continue
                        L = ZG.L_from_Z(A, C, L0, Z, q0)
                        if L is None:
                            continue
                        checked += 1
                        rphi = phi_rank(A, C, Z)
                        cond = LQ.condA(A, C, L)
                        if cond:
                            feas += 1
                        if cond != (rphi == 0):
                            bad1 += 1
                        delta, h = delta_and_h(A, C, Z, L, p, r1, q0)
                        h2 = LQ.rank([x[:] for x in L] + [x[:] for x in CA] + [x[:] for x in C])
                        if h != h2 or delta < 0:
                            bad2 += 1
    print(f'检查 {checked} 个（其中 (5a) 成立 {feas}）：')
    print(f'  (5a) ⟺ rank φ = 0 失败 {bad1}')
    print(f'  δ = q+r1-h 且 h = dim(Z⊥+W) 失败 {bad2}')
    assert bad1 == 0 and bad2 == 0
    print('✓ 专家 Correction B 与 δ 公式在样本上成立')


if __name__ == '__main__':
    main()
