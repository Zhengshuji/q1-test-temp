#!/usr/bin/env python3
"""c353 — 用自建数域算术做判定（不依赖 sympy 的根式表达）。

流程：K0 = ker[C;CA]（sympy，有理）→ 压缩 M（有理）→ 特征多项式分解（sympy，有理系数）
     → 对每个不可约因子建数域 K = Q[mu]/(f) → (M - mu I) 的零空间 → v = N c
     → 纤维（K0 cap v^perp、U^perp、x 有理样本）→ 铅笔子式在 K[lambda] 上的 gcd
     → gcd 为 1 ⟹ 该纤维生成好 ⟹ 可行（YES 侧）。
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
from nf import NF, mat_nullspace, poly_gcd, poly_deg, poly_is_zero  # noqa: E402


def rank_over(Fq, rows):
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


def to_field(Fq, mat):
    """sympy 有理矩阵 -> 域元素矩阵（行列表）。注意：有理数 p/q 对应**常数**域元素 p/q。"""
    out = []
    for i in range(mat.rows):
        row = []
        for j in range(mat.cols):
            r = sp.Rational(mat[i, j])
            row.append(Fq.elt(F(r.p, r.q)))
        out.append(row)
    return out


def decide(seed: int, verbose=False):
    A, C = d.build_instance(seed)
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    if W.rank() != 4:
        return None
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
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
        # (M - mu I) 的零空间，K 上
        Mf = to_field(Fq, sp.Matrix(M))
        mu = Fq.elt(*([0] + [1] + [0] * (deg - 2))) if deg >= 2 else Fq.elt(F(int(fp.coeff_monomial(1))))
        if deg == 1:
            mu = Fq.elt(F(-int(fp.coeff_monomial(1))), )
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
        # v = N c（N 是整数矩阵）
        v = [Fq.zero() for _ in range(n)]
        for j in range(k):
            if Fq.is_zero(c[j]):
                continue
            for i in range(n):
                if N[i, j] != 0:
                    v[i] = Fq.add(v[i], Fq.mul(Fq.elt(F(int(N[i, j]))), c[j]))
        # U = span(v, A v)
        Av = []
        for i in range(n):
            acc = Fq.zero()
            for j in range(n):
                aij = A[i, j]
                if aij != 0:
                    acc = Fq.add(acc, Fq.mul(Fq.elt(F(int(aij))), v[j]))
            Av.append(acc)
        U = [v, Av]
        if rank_over(Fq, U) != 2:
            continue        # 特征方向
        # K0 ∩ v^perp：v·(N a) = 0
        fv = []
        for j in range(k):
            s = Fq.zero()
            for i in range(n):
                if N[i, j] != 0:
                    s = Fq.add(s, Fq.mul(v[i], Fq.elt(F(int(N[i, j])))))
            fv.append(s)
        K0v = mat_nullspace(Fq, [fv])
        if len(K0v) != om:
            continue
        W0 = []
        for b in K0v:
            w = [Fq.zero() for _ in range(n)]
            for j in range(k):
                if not Fq.is_zero(b[j]):
                    for i in range(n):
                        if N[i, j] != 0:
                            w[i] = Fq.add(w[i], Fq.mul(Fq.elt(F(int(N[i, j]))), b[j]))
            W0.append(w)
        # U^perp 的基（K 上）
        Qm = mat_nullspace(Fq, [[U[i][j] for j in range(n)] for i in range(2)])
        sel = []
        cur = [[W0[i][j] for j in range(n)] for i in range(len(W0))]
        for Qrow in Qm:
            cand = cur + [Qrow]
            if rank_over(Fq, cand) > len(cur):
                cur = cand
                sel.append(Qrow)
            if len(sel) == 3:
                break
        if len(sel) < 1:
            continue
        for cc in ([1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1], [2, -1, 0], [-1, 2, 1],
                   [3, 1, -2], [1, -3, 2], [2, 2, -1], [-2, -1, 3], [5, 1, 1], [1, 5, -3]):
            if len(sel) < 3:
                cc = cc[: len(sel)]
            xv = [Fq.zero() for _ in range(n)]
            for t in range(len(sel)):
                if cc[t] == 0:
                    continue
                for j in range(n):
                    xv[j] = Fq.add(xv[j], Fq.mul(Fq.elt(F(cc[t])), sel[t][j]))
            L = W0 + [xv]
            # H = L N, HA = L A N
            def mulL(Lrows, Mat):
                out = []
                for r in Lrows:
                    row = []
                    for j in range(Mat.cols):
                        s = Fq.zero()
                        for i in range(Mat.rows):
                            if Mat[i, j] != 0:
                                s = Fq.add(s, Fq.mul(r[i], Fq.elt(F(int(Mat[i, j])))))
                        row.append(s)
                    out.append(row)
                return out
            H = mulL(L, N)
            HA = mulL(mulL(L, sp.Matrix(A)), N)
            if rank_over(Fq, H) != om:
                continue
            KH = mat_nullspace(Fq, H)
            ok = True
            for hrow in HA:
                for kv in KH:
                    s = Fq.zero()
                    for j in range(k):
                        s = Fq.add(s, Fq.mul(hrow[j], kv[j]))
                    if not Fq.is_zero(s):
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            # 铅笔 P = lam H - HA：元素是 (H[i][j], HA[i][j]) 的多项式
            def minor_poly(rs, cs):
                # 用行列式展开（4x4 子式 3x3，直接按 Leibniz）
                sz = len(rs)
                poly = None
                for perm in itertools.permutations(range(sz)):
                    sign = 1
                    pl = list(perm)
                    for i in range(sz):
                        for j in range(i + 1, sz):
                            if pl[i] > pl[j]:
                                sign = -sign
                    # 乘积：prod (lam*H - HA)
                    prod = [Fq.one()]
                    for t in range(sz):
                        i = rs[t]
                        j = cs[perm[t]]
                        # 多项式：[-HA[i][j], H[i][j]]
                        fac = [Fq.neg(HA[i][j]), H[i][j]]
                        new = [Fq.zero()] * (len(prod) + len(fac) - 1)
                        for a in range(len(prod)):
                            for b in range(len(fac)):
                                new[a + b] = Fq.add(new[a + b], Fq.mul(prod[a], fac[b]))
                        prod = new
                    if sign < 0:
                        prod = [Fq.neg(z) for z in prod]
                    if poly is None:
                        poly = prod
                    else:
                        if len(poly) < len(prod):
                            poly = poly + [Fq.zero()] * (len(prod) - len(poly))
                        for a in range(len(prod)):
                            poly[a] = Fq.add(poly[a], prod[a])
                return poly
            polys = []
            for rs in itertools.combinations(range(len(L)), om):
                for cs in itertools.combinations(range(k), om):
                    p = minor_poly(list(rs), list(cs))
                    if not poly_is_zero(Fq, p):
                        polys.append(p)
            if not polys:
                continue
            g = polys[0]
            for q in polys[1:]:
                g = poly_gcd(Fq, g, q)
            if poly_deg(Fq, g) == 0 and not poly_is_zero(Fq, g):
                return dict(seed=seed, factor=sp.sstr(f), deg=deg, cc=cc, feasible=True)
    return dict(seed=seed, feasible=False)


def main() -> None:
    print("=" * 74)
    print("自建数域算术的判定器（YES 侧）")
    print("=" * 74)
    for seed in (4245, 4242, 4246):
        r = decide(seed)
        if r is None:
            print(f"  seed {seed}: 构造失败")
        elif r.get("feasible"):
            print(f"  seed {seed}: **可行**（因子 {r['factor']}，x 系数 {r['cc']}）")
        else:
            print(f"  seed {seed}: 未找到好点（不构成不可行结论）")


if __name__ == "__main__":
    main()
