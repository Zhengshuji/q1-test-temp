"""b22_equality_obstruction.py —— 核验专家给出的 B.22（等号障碍）及其定量结论

**B.22（专家 2026-11-05 给出）**：设 $(5a)$ 成立、$\\operatorname{rank}\\mathcal L=q\\ge1$、$h=q+r_1$。取 $B$（$r_1\\times n$，满行秩）
使 $\\operatorname{row}B=\\operatorname{row}[CA;C]$，$H_0=[\\mathcal L;B]$。则 $H_0$ 满行秩 ⟹ 由 $(5a)$ 得 $\\mathcal LA=K H_0$，
$K=[K_1\\ K_2]$，于是
$$\\begin{bmatrix}\\lambda\\mathcal L-\\mathcal LA\\\\ B\\end{bmatrix}
=\\begin{bmatrix}\\lambda I_q-K_1&-K_2\\\\ 0&I_{r_1}\\end{bmatrix}\\begin{bmatrix}\\mathcal L\\\\ B\\end{bmatrix},$$
故 $\\operatorname{rank}Q_{\\mathcal L}(\\lambda)=q+r_1\\iff\\det(\\lambda I_q-K_1)\\ne0$；后者是 $q$ 次首一多项式，
$q\\ge1$ 时必有根 ⟹ $(5b)$ 失败。更强：$Q$ 严格等价于 $\\operatorname{diag}(\\lambda I_q-K_1,I_{r_1})$ ⟹ $d_{\\rm fin}=q$、$d_\\infty=r_1$。

本脚本在随机等号样本上核验：$H_0$ 满行秩、$K$ 的存在与分块、行列式恒等式、以及根处的秩跌。

用法：python -u tools/verification/b22_equality_obstruction.py
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

import sympy as sp                        # noqa: E402
import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction
lam = sp.symbols('lam')


def row_basis(M, n):
    """M 的行空间的基（满行秩矩阵）。"""
    rows = [list(r) for r in M]
    keep = []
    for r in rows:
        cand = keep + [r]
        if LQ.rank(cand) == len(cand):
            keep = cand
    return keep


def solve_K(LA, H0):
    """解 K H0 = LA（H0 满行秩 ⟹ 有解）。返回 K 或 None。"""
    # 逐行解 K的每一行：用 H0^T 的最小二乘/精确解：H0^T k^T = LA^T
    n = len(H0[0])
    m = len(H0)
    H0T = [[H0[i][j] for i in range(m)] for j in range(n)]   # n × m
    K = []
    for r in LA:
        # 解 H0^T k = r（k ∈ Q^m）
        Aq = [row[:] + [r[i]] for i, row in enumerate(H0T)]
        # 高斯消元
        rows_, cols_ = len(Aq), m
        piv = []
        rr = 0
        for c in range(cols_):
            p = next((i for i in range(rr, rows_) if Aq[i][c] != 0), None)
            if p is None:
                continue
            Aq[rr], Aq[p] = Aq[p], Aq[rr]
            inv = Aq[rr][c]
            Aq[rr] = [v / inv for v in Aq[rr]]
            for i in range(rows_):
                if i != rr and Aq[i][c] != 0:
                    f = Aq[i][c]
                    Aq[i] = [v - f * w for v, w in zip(Aq[i], Aq[rr])]
            piv.append(c)
            rr += 1
            if rr == rows_:
                break
        for i in range(rr, rows_):
            if all(v == 0 for v in Aq[i][:cols_]) and Aq[i][cols_] != 0:
                return None
        k = [F(0)] * cols_
        for i, c in enumerate(piv):
            k[c] = Aq[i][cols_]
        K.append(k)
    return K


def main():
    rng = random.Random(20261111)
    st = Counter()
    for trial in range(3000):
        n = rng.choice([5, 6])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r >= n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank([list(x) for x in C] + L0) != p + r:
            continue
        O = QR.observability_matrix(A, C)
        n0 = LQ.rank(O)
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        r1 = LQ.rank([list(x) for x in CA] + [list(x) for x in C])
        K_ = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K_ and K_[0]):
            continue
        k = len(K_[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d <= 0 or d > k:
                continue
            for rows_ in itertools.combinations(range(k), d):
                Z = DS.Z_from_theta(A, C, L0, q, rows_, [F(0)] * (d * (k - d)))
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                try:
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                except AssertionError:
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                if h != q + r1:
                    continue
                st['等号样本'] += 1
                # 专家构造
                B = row_basis([list(x) for x in CA] + [list(x) for x in C], n)
                st['B 的行数 = r1'] += 1 if len(B) == r1 else 0
                H0 = [list(x) for x in L] + B
                st['H0 满行秩'] += 1 if LQ.rank(H0) == q + r1 else 0
                LA = LQ.mul(L, A)
                Kmat = solve_K(LA, H0)
                st['K 存在'] += 1 if Kmat is not None else 0
                if Kmat is None:
                    continue
                st['K 尺寸正确'] += 1 if (len(Kmat) == q and len(Kmat[0]) == q + r1) else 0
                K1 = [row[:q] for row in Kmat]
                K2 = [row[q:] for row in Kmat]
                # 行列式恒等式：det[[λI−K1, −K2],[0, I]] = det(λI−K1)，两者都是 q 次首一
                K1s = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in K1])
                p1 = sp.expand((lam * sp.eye(q) - K1s).det())
                st['det(λI−K1) 次数 = q'] += 1 if sp.degree(p1, lam) == q else 0
                # 根处秩跌
                roots = sp.roots(p1, lam)
                ok_drop = True
                for rt in list(roots)[:3]:
                    # 在 λ=rt 处算 rank Q
                    As = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A])
                    Ls = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in L])
                    CAs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in CA])
                    Cs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in C])
                    Q = sp.zeros(q + 2 * p, n)
                    for i in range(q):
                        for j in range(n):
                            Q[i, j] = sp.expand((lam * Ls - Ls * As)[i, j])
                    for i in range(p):
                        for j in range(n):
                            Q[q + i, j] = CAs[i, j]
                            Q[q + p + i, j] = Cs[i, j]
                    rk = Q.subs(lam, rt).rank()
                    if rk >= h:
                        ok_drop = False
                st['根处秩跌 < h'] += 1 if ok_drop else 0
                break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
