"""observability_test.py —— 核验专家 2026-11-04 §3 的**可观性归约**

**归约（专家给出）**：设 $(5a)$ 成立并取 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$。令
$H=[\mathcal L;CA;C]$、$D(\lambda)=\\begin{pmatrix}\lambda I-\Lambda&-G_1&-G_0\\\\0&I&0\\\\0&0&I\end{pmatrix}$，
则 $Q_{\mathcal L}=DH$，且 $\operatorname{rank}(DH)=\operatorname{rank}H\iff\ker D\cap\operatorname{im}H=0$。
算出 $\ker D(\lambda)=\{(u,0,0):(\lambda I-\Lambda)u=0\}$、$\operatorname{im}H=\{(\mathcal Lx,CAx,Cx)\}$，得

$$(5b)\iff U:=\mathcal L(\ker[C;CA])\ \text{不含}\ \Lambda\ \text{的非零特征向量}.$$

再取 $E$ 使 $\ker E=U$，由 PBH：
$$(5b)\iff(E,\Lambda)\ \text{可观测}\iff\operatorname{rank}[E;E\Lambda;\dots;E\Lambda^{q-1}]=q .$$

本脚本用**精确有理算术**实现该判据，并与既有的三条判据对照（Toeplitz / 极大子式 gcd / 零空间铅笔），
特别覆盖 $V\cap\mathcal Z\ne0$（掉秩）的样本。

用法：python -u tools/verification/observability_test.py
"""

import os
import sys
import itertools
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import toeplitz_criterion as TC           # noqa: E402

F = Fraction


def solve_linear(Amat, bvec):
    """解 Amat x = bvec（精确有理）；返回一个解或 None。"""
    Aq = [row[:] + [bvec[i]] for i, row in enumerate(Amat)]
    rows, cols = len(Aq), len(Amat[0]) if Amat else 0
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if Aq[i][c] != 0), None)
        if p is None:
            continue
        Aq[r], Aq[p] = Aq[p], Aq[r]
        inv = Aq[r][c]
        Aq[r] = [v / inv for v in Aq[r]]
        for i in range(rows):
            if i != r and Aq[i][c] != 0:
                f = Aq[i][c]
                Aq[i] = [v - f * w for v, w in zip(Aq[i], Aq[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    for i in range(r, rows):
        if all(v == 0 for v in Aq[i][:cols]) and Aq[i][cols] != 0:
            return None
    x = [F(0)] * cols
    for i, c in enumerate(piv):
        x[c] = Aq[i][cols]
    return x


def factor_Lambda(A, C, L, LA_rows=None):
    """求 $\Lambda,G_0,G_1$ 使 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$（若 $(5a)$ 成立则可解）。"""
    n, p, q = len(A), len(C), len(L)
    CA = LQ.mul(C, A)
    LA = LQ.mul(L, A)
    qq = len(L)
    # 未知数：Λ(q×q) + G0(q×p) + G1(q×p)
    nunk = qq * qq + 2 * qq * p
    Amat, bvec = [], []
    for i in range(qq):
        for j in range(n):
            row = [F(0)] * nunk
            for k in range(qq):
                row[k * qq + i] = F(L[k][j])          # Λ[i][k] * L[k][j]
            for k in range(p):
                row[qq * qq + i * p + k] = F(C[k][j])       # G0[i][k] * C[k][j]
                row[qq * qq + qq * p + i * p + k] = F(CA[k][j])  # G1[i][k] * CA[k][j]
            Amat.append(row)
            bvec.append(F(LA[i][j]))
    x = solve_linear(Amat, bvec)
    if x is None:
        return None
    # 方程里未知数编号是 k*qq+i 对应 Lambda[i][k]，故解包时按此取
    Lam = [[x[k * qq + i] for k in range(qq)] for i in range(qq)]
    return Lam


def annihilator(M, q):
    """返回 E（(q−s)×q）使 ker E = im M，s = rank M。用 M^T 的左零空间基。"""
    # 收集 {y ∈ Q^q : y^T M = 0}
    dV = len(M[0]) if M else 0
    rows = [list(M[i]) for i in range(q)]       # q × dV
    # 求行空间正交补：解 rows · y = 0（dV 个方程，q 个未知数）
    Amat = [[rows[i][j] for i in range(q)] for j in range(dV)]
    # 用齐次解空间基
    basis = nullspace(Amat, q)
    return basis


def nullspace(Amat, ncols):
    """精确求 Amat x = 0 的解空间基（列表的列表）。"""
    Aq = [row[:] for row in Amat]
    rows = len(Aq)
    piv = []
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, rows) if Aq[i][c] != 0), None)
        if p is None:
            continue
        Aq[r], Aq[p] = Aq[p], Aq[r]
        inv = Aq[r][c]
        Aq[r] = [v / inv for v in Aq[r]]
        for i in range(rows):
            if i != r and Aq[i][c] != 0:
                f = Aq[i][c]
                Aq[i] = [v - f * w for v, w in zip(Aq[i], Aq[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -Aq[i][fc]
        basis.append(v)
    return basis


def observability_ok(A, C, L):
    """专家归约的判据：$(5b)\iff(E,\Lambda)$ 可观测。返回 (结论, 说明)。"""
    n, p, q = len(A), len(C), len(L)
    Lam = factor_Lambda(A, C, L)
    if Lam is None:
        return None, '无法取因子化（(5a) 失败？）'
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    dV = len(V[0])
    # M = L·V（q × dV）
    M = [[sum(L[i][j] * V[j][k] for j in range(n)) for k in range(dV)] for i in range(q)]
    E = annihilator(M, q)                       # ker E = im M
    m = len(E)
    if m == 0:
        # E 为空 ⟹ ker E = 全空间 ⊇ U ⟹ 任何特征向量都在 U 里 ⟹ 不可观测（q>0 时）
        return (q == 0), 'E 为空（U=ℂ^q）：不可观测 ⟹ (5b) 失败'
    # 可观性矩阵 [E; EΛ; ...; EΛ^{q-1}]，尺寸 (m·q) × q
    cur = [row[:] for row in E]
    blocks = [cur]
    for _ in range(q - 1):
        cur = [[sum(cur[i][k] * Lam[k][j] for k in range(q)) for j in range(q)] for i in range(len(cur))]
        blocks.append(cur)
    O = [row[:] for b in blocks for row in b]
    rk = LQ.rank(O)
    return rk == q, f'rank O = {rk}（应 = q = {q}），E 的尺寸 {m}×{q}'


def main():
    from collections import Counter
    stat = Counter()
    for n in (5, 6, 7):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3004):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [list(x) for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    for L in ZG.sample_L_at_order(A, C, L0, q0, 10, seed * 5 + q0):
                        if L is None:
                            continue
                        ok_obs, why = observability_ok(A, C, L)
                        if ok_obs is None:
                            stat['skip'] += 1
                            continue
                        # 既有判据：Toeplitz（仅在 (5a) 下有效）
                        if LQ.condA(A, C, L):
                            try:
                                fiveb = TC.analyse(A, C, L)['five_b']
                            except AssertionError:
                                stat['toeplitz_assert'] += 1
                                continue
                            stat['samples'] += 1
                            if ok_obs == fiveb:
                                stat['agree'] += 1
                            else:
                                stat['disagree'] += 1
                                print(f'  不一致 n={n} p={p} r={r} seed={seed}: 可观性={ok_obs} '
                                      f'Toeplitz={fiveb}（{why}）')
                        else:
                            stat['not_admissible'] += 1
    print('\n统计：', dict(stat))
    print('  agree = 可观性归约 == Toeplitz 的 (5b)；disagree 应为 0')


if __name__ == '__main__':
    main()
