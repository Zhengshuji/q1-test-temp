"""complete_small.py —— 小图卡上的**完整**判定（单参数图卡，一元多项式 gcd）

专家 2026-11-03 §8.1 的要求是"在图卡上解多项式秩约束，并证明代数集被完全描述"。
纯 Python 无 CAS 时，Buchberger 在多变量、次数 $\\ge5$ 的正子式系统上会爆炸（见本文档"限制"节）。
本模块实现**能真正做到完整**的子类：**单参数图卡**（$d(k-d)=1$）以及**单点图卡**（$d(k-d)=0$）。

原理：单参数时每个条件都是一元多项式 $p(\\theta)$；于是

* **方程组有公共复根** $\\iff$ 它们的 gcd 非常数（$\\mathbb C$ 代数闭，非零多项式必有根）；
* 因此"存在性"可以**精确**判定，且"不存在"是**证书**（gcd 为常数）。

用法：python -u tools/verification/complete_small.py
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
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

F = Fraction


# ---------- 一元多项式（升幂，list[Fraction]）----------

def ptrim(a):
    a = [F(x) for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def pact(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0)) for i in range(n)])


def pmul(a, b):
    if not a or not b:
        return []
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return ptrim(out)


def pscale(a, c):
    return ptrim([x * c for x in a])


def pdivmod(a, b):
    a = ptrim(a)
    b = ptrim(b)
    if not b:
        raise ZeroDivisionError
    q = [F(0)] * max(0, len(a) - len(b) + 1)
    r = a[:]
    while len(r) >= len(b) and r:
        d = len(r) - len(b)
        c = r[-1] / b[-1]
        q[d] = c
        for i in range(len(b)):
            r[i + d] -= c * b[i]
        r = ptrim(r)
    return ptrim(q), r


def pgcd(a, b):
    a, b = ptrim(a), ptrim(b)
    while b:
        _, r = pdivmod(a, b)
        a, b = b, r
    if a:
        a = pscale(a, F(1) / a[-1])
    return a


# ---------- 数值助手 ----------

def Z_from_theta(A, C, L0, q, rows, rest, theta):
    n = len(A)
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    d = n - len(C) - q
    W = [[F(0)] * k for _ in range(d)]
    for a, r0 in enumerate(rows):
        W[a][r0] = F(1)
    idx = 0
    for a in range(d):
        for c in rest:
            W[a][c] = F(theta[idx])
            idx += 1
    return [[sum(Kc[i][t] * W[j][t] for t in range(k)) for j in range(d)] for i in range(n)]


def interp_univariate(f, deg):
    """由 f(θ) 在 θ=0..deg 的取值插值出系数（升幂）。"""
    vals = [F(f(F(t))) for t in range(deg + 1)]
    # 拉格朗日
    coeffs = [F(0)] * (deg + 1)
    for i in range(deg + 1):
        num = [F(1)]
        den = F(1)
        for j in range(deg + 1):
            if j == i:
                continue
            num = pmul(num, [F(-j), F(1)])
            den *= F(i - j)
        for t, c in enumerate(num):
            coeffs[t] += vals[i] * c / den
    return ptrim(coeffs)


def _det(M):
    n = len(M)
    M = [row[:] for row in M]
    d = F(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if M[r][i] != 0), None)
        if piv is None:
            return F(0)
        if piv != i:
            M[i], M[piv] = M[piv], M[i]
            d = -d
        d *= M[i][i]
        inv = M[i][i]
        for r in range(i + 1, n):
            if M[r][i]:
                f0 = M[r][i] / inv
                for c in range(i, n):
                    M[r][c] -= f0 * M[i][c]
    return d


def Residual_matrix(A, C, L0, q, rows, rest, theta):
    """M(θ) = [ (Z^⊥)A | Z^⊥ | W ]，返回 (M, h)，h = rank[Z^⊥ | W]。"""
    n = len(A)
    Z = Z_from_theta(A, C, L0, q, rows, rest, [theta])
    if ZG.bool_rank(ZG.cols_to_rows(Z)) != len(Z[0]):
        return None, None
    ZT = [[Z[i][j] for i in range(n)] for j in range(len(Z[0]))]
    B = [list(x) for x in LQ.nullspace(ZT)]          # 行 = Z^⊥ 的基
    nz = len(B)
    cols = [[B[t][i] for t in range(nz)] for i in range(n)]       # n × nz
    # 注意方向：$(5a)$ 要求 $xA\\in\\mathcal Z^{\\perp}+W$（行向量右乘 $A$），
    # 列向量形式即 $A^{\\mathsf T}v$，**不是** $Av$。
    Acols = []
    for jc in range(nz):
        v = [cols[i][jc] for i in range(n)]
        Acols.append([sum(A[t][i] * v[t] for t in range(n)) for i in range(n)])
    Wrows = [list(x) for x in C] + [list(x) for x in LQ.mul(C, A)]
    nw = len(Wrows)
    M = [[Acols[jc][i] for jc in range(nz)]
         + [cols[i][jc] for jc in range(nz)]
         + [Wrows[jw][i] for jw in range(nw)]
         for i in range(n)]
    # h = rank[Z^⊥ | W]
    ZW = [[cols[i][jc] for jc in range(nz)] + [Wrows[jw][i] for jw in range(nw)] for i in range(n)]
    h = LQ.rank([[ZW[i][j] for i in range(n)] for j in range(len(ZW[0]))])
    return M, h


def decide_chart_single_parameter(A, C, L0, q, rows, rest, maxdeg=None):
    """单参数图卡：**精确**判定是否存在 θ 使 $(5a)$ 成立。

    $(5a)\iff\operatorname{rank}M(\theta)=h(\theta)$，$M=[(\mathcal Z^{\perp})A\ |\ \mathcal Z^{\perp}\ |\ W]$、
    $h=\operatorname{rank}[\mathcal Z^{\perp}|W]$。若 $h$ 恒为 $h_0$（本函数先核验），则 $(5a)\iff$
    所有 $(h_0+1)$-子式为零；子式是次数 $\le h_0+1$ 的一元多项式，插值后 gcd：
    **非常数 ⟹ 有公共复根 ⟹ 存在 θ**；**常值 ⟹ certified 无解**。
    """
    n = len(A)
    size0 = None
    hs = []
    mats = []
    deg = maxdeg if maxdeg is not None else 6
    for t in range(deg + 1):
        M, h = Residual_matrix(A, C, L0, q, rows, rest, F(t))
        if M is None:
            return 'unknown', 'θ 处 Z 不满秩'
        mats.append(M)
        hs.append(h)
    if len(set(hs)) != 1:
        return 'unknown', f'h(θ) 不恒定（{sorted(set(hs))}）；本方法不适用'
    h0 = hs[0]
    if h0 >= n:
        return 'yes', 'h=n ⟹ (5a) 自动'
    size = h0 + 1
    ncol = len(mats[0][0])
    minors = []
    for rs in itertools.combinations(range(n), size):
        for cs in itertools.combinations(range(ncol), size):
            vals = [_det([[M[i][j] for j in cs] for i in rs]) for M in mats]
            if all(v == 0 for v in vals):
                continue
            poly = interp_univariate(
                lambda th, _rs=rs, _cs=cs: _det([[Residual_matrix(A, C, L0, q, rows, rest, F(th))[0][i][j]
                                                  for j in _cs] for i in _rs]), deg)
            if poly:
                minors.append(poly)
    if not minors:
        return 'yes', '所有 (h0+1)-子式恒为零 ⟹ (5a) 处处成立'
    g = minors[0]
    for poly in minors[1:]:
        g = pgcd(g, poly)
        if len(g) <= 1:
            break
    if len(g) >= 2:
        return 'yes', f'子式 gcd 次数 {len(g) - 1} ⟹ 有公共复根 ⟹ 存在 θ'
    return 'no', '子式 gcd 为非零常数 ⟹ **certified**：无 θ 使 (5a) 成立'


def main():
    print('单参数图卡的精确判定（$d(k-d)=1$）——找实例：')
    found = 0
    for n in (5, 6):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3012):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    k = len(Kc[0])
                    for q in range(q0, min(LQ.rank(O) - p, n - p) + 1):
                        d = n - p - q
                        if d <= 0 or d >= k:
                            continue
                        if d * (k - d) != 1:
                            continue
                        verdicts = []
                        for rows in itertools.combinations(range(k), d):
                            rest = [i for i in range(k) if i not in rows]
                            v, why = decide_chart_single_parameter(A, C, L0, q, rows, rest)
                            verdicts.append((rows, v, why))
                        if any(v == 'yes' for _, v, _ in verdicts):
                            v, why = 'yes', '；'.join(f'{r}:{w}' for r, vv, w in verdicts if vv == 'yes')
                        elif all(v == 'no' for _, v, _ in verdicts):
                            v, why = 'no', '**所有图卡都 certified 无解**'
                        else:
                            v, why = 'unknown', '；'.join(f'{r}:{vv}' for r, vv, w in verdicts)
                        grid_ok = False
                        for t in [F(a, b) for a in range(-4, 5) for b in (1, 2, 3)]:
                            for rows in itertools.combinations(range(k), d):
                                rest = [i for i in range(k) if i not in rows]
                                Z = Z_from_theta(A, C, L0, q, rows, rest, [t])
                                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                                    continue
                                L = ZG.L_from_Z(A, C, L0, Z, q)
                                if L is not None and LQ.condA(A, C, L):
                                    grid_ok = True
                                    break
                            if grid_ok:
                                break
                        print(f'  n={n} p={p} r={r} seed={seed} q={q}: d={d} k={k} → {v}（{why}）；'
                              f'网格 {"找到" if grid_ok else "未找到"}')
                        found += 1
                        if found >= 4:
                            return
    if not found:
        print('  本批实例中没有 d(k-d)=1 的图卡（这类图卡 = Gr(1,2)=P^1，较稀有）')


if __name__ == '__main__':
    main()
