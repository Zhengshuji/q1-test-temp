#!/usr/bin/env python3
"""c354 — 数域上的多变量算术 + 结式判据：把"纤维是否生成好"变成精确判定。

思路：纤维的铅笔 P(λ) = λH − H_A 的 ω×ω 极大子式 f_i(λ; x) 的系数是 x=(x1,x2,x3) 的多项式、
系数在数域 K = Q[mu]/(f) 里。则
    纤维生成好  <=  ∃ 一对 (i,j): Res_λ(f_i, f_j) ≢ 0 （作为 x 的多项式）。
（gcd(f_i,f_j)=1 ⟹ 所有 f 的 gcd = 1。）这是**充分**条件，正好用于 YES 侧。

实现：K 上用 dict{(e1,e2,e3): K-元素} 表示 x-多项式；Sylvester 行列式用展开计算。
"""

from __future__ import annotations

import itertools
import os
import sys
from fractions import Fraction as F

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402
import c352_number_field_decider as d  # noqa: E402
from nf import NF, mat_nullspace  # noqa: E402

NV = 3   # x 的变量个数


# ---------- K 上的多变量多项式（dict 表示） ----------
def p_zero():
    return {}


def p_const(Fq, c):
    if Fq.is_zero(c):
        return {}
    return {(0,) * NV: c}


def p_add(Fq, a, b):
    out = dict(a)
    for k, v in b.items():
        if k in out:
            s = Fq.add(out[k], v)
            if Fq.is_zero(s):
                del out[k]
            else:
                out[k] = s
        else:
            out[k] = v
    return out


def p_neg(Fq, a):
    return {k: Fq.neg(v) for k, v in a.items()}


def p_sub(Fq, a, b):
    return p_add(Fq, a, p_neg(Fq, b))


def p_mul(Fq, a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(ka[i] + kb[i] for i in range(NV))
            prod = Fq.mul(va, vb)
            if Fq.is_zero(prod):
                continue
            if k in out:
                s = Fq.add(out[k], prod)
                if Fq.is_zero(s):
                    del out[k]
                else:
                    out[k] = s
            else:
                out[k] = prod
    return out


def p_is_zero(a):
    return len(a) == 0


def p_scalar_mul(Fq, a, c):
    if Fq.is_zero(c):
        return {}
    return {k: Fq.mul(v, c) for k, v in a.items()}


# ---------- 多变量多项式环上的小型行列式 ----------
def det_poly(Fq, M):
    n = len(M)
    if n == 0:
        return p_const(Fq, Fq.one())
    if n == 1:
        return M[0][0]
    total = {}
    for j in range(n):
        minor = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = p_mul(Fq, M[0][j], det_poly(Fq, minor))
        if j % 2 == 1:
            term = p_neg(Fq, term)
        total = p_add(Fq, total, term)
    return total


def resultant(Fq, f, g):
    """f, g: λ-多项式，系数是 x-多项式（list，低次在前）。返回 Res_λ(f,g)。"""
    def deg(p):
        k = -1
        for i, c in enumerate(p):
            if not p_is_zero(c):
                k = i
        return k
    df, dg = deg(f), deg(g)
    if df < 0 or dg < 0:
        return {}
    if df == 0 and dg == 0:
        return {}
    n = df + dg
    S = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(dg):
        for k in range(df + 1):
            S[i][i + k] = f[df - k]
    for i in range(df):
        for k in range(dg + 1):
            S[dg + i][i + k] = g[dg - k]
    return det_poly(Fq, S)


# ---------- 判定 ----------
def fibre_polys(A, N, v, Fq, x_coeffs):
    """构造该 v 与 x-符号（系数 x_coeffs）下的铅笔子式（λ-多项式，系数是 x-多项式）。

    纤维参数个数 r = dim(U^⊥) - ω，其中 dim U = rank{v, Av}：
    非特征（dim U = 2）时 r = ρ-1；特征（dim U = 1）时 r = ρ。二者都只依赖 p。
    """
    global NV
    n = A.rows
    k = N.cols
    om = k - 1
    # K0 ∩ v^perp 的基
    fv = []
    for j in range(k):
        s = Fq.zero()
        for i in range(n):
            if N[i, j] != 0:
                s = Fq.add(s, Fq.mul(v[i], Fq.elt(F(int(N[i, j])))))
        fv.append(s)
    K0v = mat_nullspace(Fq, [fv])
    if len(K0v) != om:
        return None
    W0 = []
    for b in K0v:
        w = [Fq.zero() for _ in range(n)]
        for j in range(k):
            if not Fq.is_zero(b[j]):
                for i in range(n):
                    if N[i, j] != 0:
                        w[i] = Fq.add(w[i], Fq.mul(Fq.elt(F(int(N[i, j]))), b[j]))
        W0.append(w)
    # U^perp
    Av = []
    for i in range(n):
        acc = Fq.zero()
        for j in range(n):
            if A[i, j] != 0:
                acc = Fq.add(acc, Fq.mul(Fq.elt(F(int(A[i, j]))), v[j]))
        Av.append(acc)
    Qm = mat_nullspace(Fq, [v, Av])
    # 纤维参数个数：dim(U^⊥) - ω = (n - dim U) - ω
    dimU = rank_rows(Fq, [v, Av])
    NV = (n - dimU) - om
    if NV < 0:
        return None
    sel = []
    cur = list(W0)
    for Qrow in Qm:
        if rank_rows(Fq, cur + [Qrow]) > len(cur):
            cur = cur + [Qrow]
            sel.append(Qrow)
        if len(sel) == NV:
            break
    if len(sel) < NV:
        return None
    # x = sum x_j * sel[j]（符号）
    xvec = []
    for i in range(n):
        poly = {}
        for j in range(NV):
            e = (0,) * NV
            e = e[:j] + (1,) + e[j + 1:]
            poly[e] = sel[j][i]
        xvec.append(poly)
    # L 的行：W0 的 om 行（常数多项式）+ xvec
    Lrows = []
    for w in W0:
        Lrows.append([p_const(Fq, w[i]) for i in range(n)])
    Lrows.append(xvec)
    # H = L N, HA = L A N（多项式）
    def mulL(Lrows_, Mat):
        out = []
        for r in Lrows_:
            row = []
            for j in range(Mat.cols):
                acc = {}
                for i in range(Mat.rows):
                    if Mat[i, j] != 0:
                        acc = p_add(Fq, acc, p_scalar_mul(Fq, r[i], Fq.elt(F(int(Mat[i, j])))))
                row.append(acc)
            out.append(row)
        return out
    H = mulL(Lrows, N)
    HA = mulL(mulL(Lrows, sp.Matrix(A)), N)
    # 铅笔：P = λH - HA，元素是 λ 的线性多项式（系数是 x-多项式）
    P = [[[p_neg(Fq, HA[i][j]), H[i][j]] for j in range(k)] for i in range(len(Lrows))]
    # 3x3 子式
    polys = []
    for rs in itertools.combinations(range(len(Lrows)), om):
        for cs in itertools.combinations(range(k), om):
            # 展开（Leibniz），每个条目是 λ-线性
            total = []
            for perm in itertools.permutations(range(om)):
                sign = 1
                pl = list(perm)
                for a in range(om):
                    for b in range(a + 1, om):
                        if pl[a] > pl[b]:
                            sign = -sign
                prod = [p_const(Fq, Fq.one())]
                for t in range(om):
                    entry = P[rs[t]][cs[perm[t]]]
                    new = [{} for _ in range(len(prod) + 1)]
                    for a, ca in enumerate(prod):
                        for b, cb in enumerate(entry):
                            new[a + b] = p_add(Fq, new[a + b], p_mul(Fq, ca, cb))
                    prod = new
                if sign < 0:
                    prod = [p_neg(Fq, z) for z in prod]
                if not total:
                    total = prod
                else:
                    if len(total) < len(prod):
                        total = total + [{} for _ in range(len(prod) - len(total))]
                    for a, c in enumerate(prod):
                        total[a] = p_add(Fq, total[a], c)
            if total and any(not p_is_zero(c) for c in total):
                polys.append(total)
    return polys


def rank_rows(Fq, rows):
    A = [list(r) for r in rows]
    mrows = len(A)
    ncols = len(A[0]) if mrows else 0
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, mrows):
            if not Fq.is_zero(A[i][c]):
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = Fq.inv(A[r][c])
        A[r] = [Fq.mul(x, inv) for x in A[r]]
        for i in range(mrows):
            if i != r and not Fq.is_zero(A[i][c]):
                fac = A[i][c]
                A[i] = [Fq.sub(A[i][j], Fq.mul(fac, A[r][j])) for j in range(ncols)]
        r += 1
        if r == mrows:
            break
    return r


def decide(seed: int):
    A, C = d.build_instance(seed)
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    if W.rank() != 4:
        return None
    N = m.ker_basis(W)
    k = N.cols
    G = N.T * N
    M = G.inv() * (N.T * A * N)
    x = sp.symbols("x")
    cp = sp.Poly(M.charpoly(x).as_expr(), x)
    _, facs = sp.factor_list(cp.as_expr())
    for f, mult in facs:
        fp = sp.Poly(f, x)
        deg = fp.degree()
        if deg < 1:
            continue
        coeffs = [int(fp.coeff_monomial(x**i)) for i in range(deg)] + [1]
        Fq = NF(coeffs)
        Mf = []
        for i in range(k):
            row = []
            for j in range(k):
                r = sp.Rational(M[i, j])
                row.append(Fq.elt(F(r.p, r.q)))
            Mf.append(row)
        if deg == 1:
            mu = Fq.elt(F(-int(fp.coeff_monomial(1))))
        else:
            mu = Fq.elt(*([0] + [1] + [0] * (deg - 2)))
        rows = []
        for i in range(k):
            row = []
            for j in range(k):
                e = Mf[i][j]
                row.append(Fq.sub(e, mu) if i == j else e)
            rows.append(row)
        ns = mat_nullspace(Fq, rows)
        if not ns:
            continue
        c = ns[0]
        v = [Fq.zero() for _ in range(n)]
        for j in range(k):
            if Fq.is_zero(c[j]):
                continue
            for i in range(n):
                if N[i, j] != 0:
                    v[i] = Fq.add(v[i], Fq.mul(Fq.elt(F(int(N[i, j]))), c[j]))
        # 非特征？
        Av = [Fq.add(Fq.zero(), v[i]) for i in range(n)]
        tmp = []
        for i in range(n):
            acc = Fq.zero()
            for j in range(n):
                if A[i, j] != 0:
                    acc = Fq.add(acc, Fq.mul(Fq.elt(F(int(A[i, j]))), v[j]))
            tmp.append(acc)
        if rank_rows(Fq, [v, tmp]) != 2:
            continue
        polys = fibre_polys(A, N, v, Fq, None)
        if not polys:
            continue
        # 两两结式
        for a in range(len(polys)):
            for b in range(a + 1, len(polys)):
                R = resultant(Fq, polys[a], polys[b])
                if not p_is_zero(R):
                    return dict(seed=seed, factor=sp.sstr(f), feasible=True)
    return dict(seed=seed, feasible=False)


def main() -> None:
    print("=" * 74)
    print("数域 + 多变量结式：纤维是否生成好（充分判据）")
    print("=" * 74)
    for seed in (4246, 4242, 4245):
        r = decide(seed)
        if r is None:
            print(f"  seed {seed}: 构造失败")
        elif r.get("feasible"):
            print(f"  seed {seed}: **可行**（因子 {r['factor']}，结式非零）")
        else:
            print(f"  seed {seed}: 所有结式为零（未判定）")


if __name__ == "__main__":
    main()
