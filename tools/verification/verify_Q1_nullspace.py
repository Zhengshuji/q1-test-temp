"""verify_Q1_nullspace.py —— 核验专家 2026-11-03 §1 的零空间铅笔判据，以及 C4 的比例性

**(1) 零空间铅笔判据**（专家 Q1.1，同时适用于 $h<n$ 与 $r\\ge2$）：
$$(5b)\\ \\Longleftrightarrow\\ \\operatorname{rank}\\bigl[(\\lambda I-A)V\\ \\ Z\\bigr]
=\\operatorname{rank}\\bigl[V\\ \\ Z\\bigr]\\quad\\forall\\lambda\\in\\mathbb C,$$
其中 $V$ 是 $\\ker[C;CA]$ 的满列秩基、$Z$ 是 $\\mathcal Z=\\ker[C;\\mathcal L]$ 的满列秩基。

**(2) C4 实例的比例性**（专家 §8.5）：对 $r=2$ 的 $L_0$，需要
$$\\det\\begin{pmatrix}L_{0,1}Ax & L_{0,1}x\\\\ L_{0,2}Ax & L_{0,2}x\\end{pmatrix}=0\\quad\\forall x\\in V,$$
即两个向量 $L_0Ax$ 与 $L_0x$ 成比例。这是 $x$ 的二次型，只需在基上验证（极化恒等式）。

用法：python tools/verification/verify_Q1_nullspace.py
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
import toeplitz_criterion as TC           # noqa: E402
import spectral_gcd as SG                 # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import importlib.util as iu               # noqa: E402

F = Fraction


def apply_col(A, Z):
    """$A Z$（列），断言 $Z$ 是 $n\\times d$。"""
    n = len(A)
    if not Z:
        return [[] for _ in range(n)]
    d = len(Z[0])
    assert len(Z) == n, 'Z 应为 n 行'
    out = [[F(0)] * d for _ in range(n)]
    for i in range(n):
        for j in range(d):
            s = F(0)
            for t in range(n):
                s += A[i][t] * Z[t][j]
            out[i][j] = s
    return out


def augment(*mats):
    """按列拼接（行数相同）。"""
    n = len(mats[0])
    out = []
    for i in range(n):
        row = []
        for M in mats:
            row += [M[i][j] for j in range(len(M[0]))]
        out.append(row)
    return out


def nullspace_basis(M):
    """$\\{x : Mx=0\\}$ 作为列基（n×d）。"""
    rows = [list(x) for x in LQ.nullspace(M)]
    if not rows:
        return [[] for _ in range(len(M[0]))]
    d = len(rows)
    n = len(rows[0])
    return [[rows[i][j] for i in range(d)] for j in range(n)]


def rank_of_cols(M):
    n = len(M)
    d = len(M[0]) if M else 0
    if d == 0:
        return 0
    rows = [[M[i][j] for i in range(n)] for j in range(d)]
    return LQ.rank(rows)


def nullspace_test(A, C, L, lams):
    """专家 Q1.1：$\\operatorname{rank}[(\\lambda I-A)V\\ Z]=\\operatorname{rank}[V\\ Z]$ 对所有 $\\lambda$。"""
    n = len(A)
    V = nullspace_basis([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    Z = nullspace_basis([list(x) for x in C] + [list(x) for x in L])
    ref = rank_of_cols(augment(V, Z))
    for lam in lams:
        Mmat = [[lam * (1 if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)]
        lhs = rank_of_cols(augment(apply_col(Mmat, V), Z))
        if lhs != ref:
            return False, lam
    return True, None




def nullspace_gcd(A, C, L):
    """专家 Q1.1 的**精确**版本：$P_Z(\lambda)=[(\lambda I-A)V\ \ Z]$ 的**极大子式 gcd**。

    常数（非零）$\iff$ 对所有 $\lambda$ 秩不变 $\iff$ $(5b)$。用多项式行列式精确计算，
    不抽样 $\lambda$（抽样会漏掉复根/非有理根）。
    """
    import itertools
    import spectral_gcd as SG
    n = len(A)
    V = nullspace_basis([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    Z = nullspace_basis([list(x) for x in C] + [list(x) for x in L])
    dv = len(V[0]) if V else 0
    d = len(Z[0]) if Z else 0
    # 列数
    ncol = dv + d
    # 行：P0 = [ -A V | Z ]，P1 = [ V | 0 ]
    AV = apply_col(A, V) if dv else [[] for _ in range(n)]
    P0 = []
    P1 = []
    for i in range(n):
        row0 = ([ -AV[i][j] for j in range(dv)] if dv else []) + ([Z[i][j] for j in range(d)] if d else [])
        row1 = ([V[i][j] for j in range(dv)] if dv else []) + ([F(0)] * d)
        P0.append(row0)
        P1.append(row1)
    # 参考秩 = rank[V | Z]
    ref = rank_of_cols(augment(V, Z)) if (dv or d) else 0
    if ref == 0 or ncol == 0:
        return [F(1)]
    g = None
    for rows in itertools.combinations(range(n), ref):
        for cols in itertools.combinations(range(ncol), ref):
            M = [[[P0[i][j], P1[i][j]] for j in cols] for i in rows]
            detpoly = SG.pdet(M)
            if SG.pdeg(detpoly) < 0:
                continue                      # 零多项式
            g = detpoly if g is None else SG.pgcd(g, detpoly)
            if g is not None and SG.pdeg(g) == 0:
                return SG.pscale(g, F(1) / g[0])
    return g if g is not None else [F(0)]

def main():
    print('=== (1) 零空间判据与 Toeplitz / gcd 的一致性 ===')
    lams = [F(k) for k in range(-3, 4)] + [F(a, b) for a in range(-3, 4) for b in (2, 3)]
    cases = []
    # C4 实例
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, cands4 = V4.build()
    for L in cands4[:2]:
        cases.append(('C4', A4, C4m, L))
    # 异常实例的 L_*（专家给的）
    A7, C7, L07 = QR.make_instance(7, 2, 2, 4004 * 23 + 2 * 11 + 2)
    Lstar = [[F(-1), F(0), F(0), F(0), F(-1), F(0), F(0)],
             [F(1), F(0), F(0), F(0), F(0), F(0), F(1)],
             [F(1), F(0), F(0), F(-1), F(0), F(-1), F(1)]]
    cases.append(('Lstar', A7, C7, Lstar))
    # 若干随机实例（含 r=1、r=2）
    import random
    for (n, p, r, seed) in [(6, 1, 1, 3004), (6, 2, 1, 3002), (7, 2, 2, 3003), (5, 2, 1, 3000)]:
        made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
        if made is None:
            continue
        A, C, L0 = made
        if LQ.rank(QR.observability_matrix(A, C) + [x[:] for x in L0]) != \
           LQ.rank(QR.observability_matrix(A, C)):
            continue
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        d = n - p - q0
        if d <= 0:
            continue
        rng = random.Random(seed)
        Kc = K
        mm = len(Kc[0])
        n_ = len(Kc)
        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
        Zc = [[sum(Kc[i][t] * Wm[t][j] for t in range(mm)) for j in range(d)] for i in range(n_)]
        if ZG.bool_rank(ZG.cols_to_rows(Zc)) != d:
            continue
        L = ZG.L_from_Z(A, C, L0, Zc, q0)
        if L is None:
            continue
        cases.append((f'rand{n}/{p}/{r}', A, C, L))

    agree = 0
    total = 0
    for tag, A, C, L in cases:
        if not LQ.condA(A, C, L):
            continue
        total += 1
        toe = TC.analyse(A, C, L)['five_b']
        gcd = SG.spectral_gcd(A, C, L)[0]
        nsp_sampled, bad_lam = nullspace_test(A, C, L, lams)
        ng = nullspace_gcd(A, C, L)
        nsp = (len(ng) == 1 and ng[0] != 0)
        gcd_ok = (gcd == [F(1)])
        ok = (toe == nsp == gcd_ok)
        print(f'  {tag}: Toeplitz={toe} 零空间gcd判据={nsp}（抽样版={nsp_sampled}）gcd为常数={gcd_ok} → {"一致" if ok else "不一致！"}'
              + ('' if bad_lam is None else f'（掉秩 λ={bad_lam}）'))
        agree += 1 if ok else 0
    print(f'  一致 {agree}/{total}')

    print('\n=== (2) C4 的比例性（$2\\times2$ 行列式在 V 上恒零）===')
    V = nullspace_basis([list(x) for x in C4m] + [list(x) for x in LQ.mul(C4m, A4)])
    dV = len(V[0])
    nb = len(A4)

    def det2(x):
        Ax = [sum(A4[i][j] * x[j] for j in range(nb)) for i in range(nb)]
        a1 = sum(L04[0][i] * Ax[i] for i in range(nb))
        b1 = sum(L04[0][i] * x[i] for i in range(nb))
        a2 = sum(L04[1][i] * Ax[i] for i in range(nb))
        b2 = sum(L04[1][i] * x[i] for i in range(nb))
        return a1 * b2 - a2 * b1

    vecs = [[V[i][j] for i in range(nb)] for j in range(dV)]
    vals = []
    for j in range(dV):
        vals.append(det2(vecs[j]))
    cross = []
    for j in range(dV):
        for k2 in range(j + 1, dV):
            x = [vecs[j][i] + vecs[k2][i] for i in range(nb)]
            cross.append(det2(x))
    print(f'  dim V = {dV}；基上 det = {[str(v) for v in vals]}；基和上 det = {[str(v) for v in cross]}')
    assert all(v == 0 for v in vals) and all(v == 0 for v in cross), '比例性不成立'
    print('  ✓ 二次型在 V 的基与基和上均为零 ⟹ 由极化恒等式在所有 x∈V 上恒零（比例性成立）')


if __name__ == '__main__':
    main()
