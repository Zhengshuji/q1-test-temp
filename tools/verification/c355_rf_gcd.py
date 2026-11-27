#!/usr/bin/env python3
"""c355 — K(x)[lambda] 上的 gcd（有理函数系数），用来判定纤维是否生成好。

纤维的极大子式 f_i(lambda; x) 的系数是 x 的多项式（系数在数域 K 里）。
把它们看成 K(x)（有理函数域）上的 lambda-多项式，做欧几里得 gcd：
  deg_lambda gcd = 0  ⟹ 纤维**生成好**（generic gcd = 1）；
  deg_lambda gcd > 0  ⟹ 纤维**全坏**（generic gcd 有公根）。
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
import c354_generic_gcd_nf as g  # noqa: E402
from nf import NF, mat_nullspace  # noqa: E402

p_add, p_mul, p_is_zero, p_neg = g.p_add, g.p_mul, g.p_is_zero, g.p_neg
p_sub = g.p_sub


class RF:
    """K 上的有理函数 = num/den（都是 x 的多项式）。"""

    __slots__ = ("num", "den")

    def __init__(self, num, den=None):
        self.num = num
        self.den = den if den is not None else {(0,) * g.NV: Fq_one[0].one()}

    # 下面用全局 Fq（在运行时设置）


Fq_one = None


def rf_mul(A, B):
    Fq = Fq_one[0]
    return RF(p_mul(Fq, A.num, B.num), p_mul(Fq, A.den, B.den))


def rf_add(A, B):
    Fq = Fq_one[0]
    return RF(p_add(Fq, p_mul(Fq, A.num, B.den), p_mul(Fq, B.num, A.den)),
              p_mul(Fq, A.den, B.den))


def rf_sub(A, B):
    Fq = Fq_one[0]
    return RF(p_sub(Fq, p_mul(Fq, A.num, B.den), p_mul(Fq, B.num, A.den)),
              p_mul(Fq, A.den, B.den))


def rf_inv(A):
    return RF(A.den, A.num)


def rf_is_zero(A):
    return p_is_zero(A.num)


def poly_deg_rf(P):
    for i in range(len(P) - 1, -1, -1):
        if not rf_is_zero(P[i]):
            return i
    return -1


def poly_trim_rf(P):
    while P and rf_is_zero(P[-1]):
        P.pop()
    return P


def poly_rem_rf(A, B):
    A = list(A)
    db = poly_deg_rf(B)
    while True:
        da = poly_deg_rf(A)
        if da < db:
            break
        fac = rf_mul(A[da], rf_inv(B[db]))
        shift = da - db
        for i in range(db + 1):
            A[shift + i] = rf_sub(A[shift + i], rf_mul(fac, B[i]))
        poly_trim_rf(A)
    return A


def poly_gcd_rf(A, B):
    A = list(A)
    B = list(B)
    while B and poly_deg_rf(B) >= 0:
        R = poly_rem_rf(A, B)
        A, B = B, R
    return poly_trim_rf(A)


def decide(seed: int, AC=None, verbose=False):
    global Fq_one
    if AC is None:
        A, C = d.build_instance(seed)
    else:
        A, C = AC
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
    out = []
    for f, mult in facs:
        fp = sp.Poly(f, x)
        deg = fp.degree()
        if deg < 1:
            continue
        coeffs = [int(fp.coeff_monomial(x**i)) for i in range(deg)] + [1]
        Fq = NF(coeffs)
        Fq_one = (Fq,)
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
        rows = [[Fq.sub(Mf[i][j], mu) if i == j else Mf[i][j] for j in range(k)] for i in range(k)]
        ns = mat_nullspace(Fq, rows)
        if not ns:
            out.append((sp.sstr(f), "无特征向量", True))
            continue
        # 守卫（专家 101 号 §3.3）：若特征空间维数 > 1，方向集是 P^{d-1}（无穷多），
        # 只取 ns[0] 会漏 ⟹ 结论标"不完备"。
        multi_dir = len(ns) > 1
        c = ns[0]
        v = [Fq.zero() for _ in range(n)]
        for j in range(k):
            if Fq.is_zero(c[j]):
                continue
            for i in range(n):
                if N[i, j] != 0:
                    v[i] = Fq.add(v[i], Fq.mul(Fq.elt(F(int(N[i, j]))), c[j]))
        Av = []
        for i in range(n):
            acc = Fq.zero()
            for j in range(n):
                if A[i, j] != 0:
                    acc = Fq.add(acc, Fq.mul(Fq.elt(F(int(A[i, j]))), v[j]))
            Av.append(acc)
        ks = g.rank_rows(Fq, [v, Av])
        if ks not in (1, 2):
            out.append((sp.sstr(f), "秩异常", True))
            continue
        is_eigen = (ks == 1)      # v 也是 A 的特征向量：此时只算一个"切片"，结论对 NO 不完备
        polys = g.fibre_polys(A, N, v, Fq, None)
        if not polys:
            out.append((sp.sstr(f), "无子式", True))
            continue
        # 转成 RF 系数的 lambda-多项式
        P = [[RF(cc) for cc in Pi] for Pi in polys]
        P = [poly_trim_rf(Q) for Q in P]
        P = [Q for Q in P if poly_deg_rf(Q) >= 0]
        if not P:
            out.append((sp.sstr(f), "无子式", True))
            continue
        gg = P[0]
        for Q in P[1:]:
            gg = poly_gcd_rf(gg, Q)
            if poly_deg_rf(gg) == 0:
                break
        dg = poly_deg_rf(gg)
        if dg == 0:
            out.append((sp.sstr(f), "生成好", False))
        else:
            tag = f"全坏（gcd 次数 {dg}）" if not is_eigen else f"切片全坏（gcd 次数 {dg}）"
            out.append((sp.sstr(f), tag, is_eigen or multi_dir))
    return out


def main() -> None:
    print("=" * 74)
    print("K(x)[lambda] 上的 gcd：纤维 YES/NO（含可靠性标记）")
    print("=" * 74)
    for seed in (4242, 4245, 4246):
        res = decide(seed)
        if res is None:
            print(f"  seed {seed}: 构造失败")
            continue
        print(f"  seed {seed}:")
        any_good = False
        undetermined = False
        for item in res:
            f, r, incomplete = item
            print(f"     因子 {f}: {r}" + ("（不完备：切片）" if incomplete and "生成好" not in r else ""))
            if "生成好" in r:
                any_good = True
            elif incomplete:
                undetermined = True
        if any_good:
            print("     => **可行**")
        elif undetermined:
            print("     => 未判定（有切片/未覆盖的方向）")
        else:
            print("     => **不可行**（所有方向全坏）")


if __name__ == "__main__":
    main()
