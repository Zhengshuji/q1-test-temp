"""nf.py —— 极简数域算术（纯 Fraction，不用 sympy 的根式）。

数域 K = Q[mu]/(f)，f 首一、整系数、不可约。
元素 = 长度 d 的有理向量（按 1, mu, ..., mu^{d-1} 展开）。
多项式（在 lambda 上）的元素系数在 K 里；gcd 用 Euclid。
"""

from __future__ import annotations

from fractions import Fraction as F


class NF:
    def __init__(self, f_coeffs):
        # f(x) = x^d + c_{d-1} x^{d-1} + ... + c_0
        self.f = [F(c) for c in f_coeffs]
        self.d = len(self.f) - 1
        assert self.f[-1] == 1

    # --- 域元素 ---
    def zero(self):
        return tuple(F(0) for _ in range(self.d))

    def one(self):
        v = [F(0)] * self.d
        v[0] = F(1)
        return tuple(v)

    def elt(self, *coeffs):
        v = [F(0)] * self.d
        for i, c in enumerate(coeffs[: self.d]):
            v[i] = F(c)
        return tuple(v)

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def mul(self, a, b):
        d = self.d
        assert len(a) == d, (len(a), d, a)
        assert len(b) == d, (len(b), d, b)
        prod = [F(0)] * (2 * d - 1)
        for i, x in enumerate(a):
            if x == 0:
                continue
            for j, y in enumerate(b):
                if y != 0:
                    prod[i + j] += x * y
        # 约化：x^d = -(c_0 + c_1 x + ... + c_{d-1} x^{d-1})
        for k in range(len(prod) - 1, d - 1, -1):
            c = prod[k]
            if c == 0:
                continue
            for i in range(d):
                prod[k - d + i] -= c * self.f[i]
            prod[k] = F(0)
        return tuple(prod[:d])

    def is_zero(self, a):
        return all(x == 0 for x in a)

    # 多项式（在 x 上）的扩展 Euclid，用于求逆
    def _poly_divmod(self, a, b):
        a = [F(x) for x in a]
        b = [F(x) for x in b]
        while len(a) > 0 and a[-1] == 0:
            a.pop()
        while len(b) > 0 and b[-1] == 0:
            b.pop()
        q = [F(0)] * max(0, len(a) - len(b) + 1)
        while len(a) >= len(b) and a:
            coef = a[-1] / b[-1]
            shift = len(a) - len(b)
            q[shift] = coef
            for i in range(len(b)):
                a[shift + i] -= coef * b[i]
            while len(a) > 0 and a[-1] == 0:
                a.pop()
        return q, a

    def inv(self, a):
        assert not self.is_zero(a)
        # 扩展 Euclid：r_i = s_i * a + t_i * f，初始 r0 = f (s0 = 0), r1 = a (s1 = 1)
        r0, r1 = list(self.f), list(a)
        s0, s1 = [F(0)], [F(1)]
        while r1 and any(x != 0 for x in r1):
            q, r = self._poly_divmod(r0, r1)
            r0, r1 = r1, r
            qs = [F(0)] * (max(len(q) + len(s1) - 1, 0)) if (q and s1) else []
            for i, x in enumerate(q):
                for j, y in enumerate(s1):
                    qs[i + j] += x * y
            news = [F(0)] * max(len(s0), len(qs))
            for i, x in enumerate(s0):
                news[i] += x
            for i, x in enumerate(qs):
                news[i] -= x
            s0, s1 = s1, news
        c = r0[0]
        u = [x / c for x in s0]
        vec = [F(0)] * self.d
        for i, x in enumerate(u[: self.d]):
            vec[i] = x
        return tuple(vec)

    def div(self, a, b):
        return self.mul(a, self.inv(b))


# --- 域上的多项式（lambda 为变量）---
def poly_trim(p):
    p = list(p)
    while p and p[-1] == 0 and False:
        p.pop()
    return p


def poly_is_zero(Fq, p):
    return all(Fq.is_zero(c) for c in p)


def poly_deg(Fq, p):
    for i in range(len(p) - 1, -1, -1):
        if not Fq.is_zero(p[i]):
            return i
    return -1


def poly_divmod(Fq, a, b):
    a = list(a)
    b = list(b)
    db = poly_deg(Fq, b)
    q = [Fq.zero() for _ in range(max(0, poly_deg(Fq, a) - db + 1))]
    while True:
        da = poly_deg(Fq, a)
        if da < db:
            break
        coef = Fq.div(a[da], b[db])
        shift = da - db
        q[shift] = coef
        for i in range(db + 1):
            a[shift + i] = Fq.sub(a[shift + i], Fq.mul(coef, b[i]))
        a[da] = Fq.zero()
    return q, a


def poly_gcd(Fq, a, b):
    a = list(a)
    b = list(b)
    while not poly_is_zero(Fq, b):
        _, r = poly_divmod(Fq, a, b)
        a, b = b, r
    if poly_is_zero(Fq, a):
        return a
    d = poly_deg(Fq, a)
    inv = Fq.inv(a[d])
    return [Fq.mul(c, inv) for c in a]


def mat_nullspace(Fq, rows):
    """行列表（每行是域元素列表）的零空间，返回基（域元素向量的列表）。"""
    m = len(rows)
    n = len(rows[0]) if m else 0
    A = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(n):
        pivrow = None
        for i in range(r, m):
            if not Fq.is_zero(A[i][c]):
                pivrow = i
                break
        if pivrow is None:
            continue
        A[r], A[pivrow] = A[pivrow], A[r]
        inv = Fq.inv(A[r][c])
        A[r] = [Fq.mul(x, inv) for x in A[r]]
        for i in range(m):
            if i != r and not Fq.is_zero(A[i][c]):
                fac = A[i][c]
                A[i] = [Fq.sub(A[i][j], Fq.mul(fac, A[r][j])) for j in range(n)]
        piv.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        vec = [Fq.zero() for _ in range(n)]
        vec[fc] = Fq.one()
        for i, pc in enumerate(piv):
            vec[pc] = Fq.neg(A[i][fc])
        basis.append(vec)
    return basis
