r"""精确 (S) 判据：铅笔 $P(\lambda)=[(\lambda I-A)V\mid Z]$ 的**极大子式 gcd**（有理系数多项式）。

$(S)$ 成立 $\iff$ gcd 是非零常数（对 pole assignability，$\lambda\in\mathbb C$）。
这是本项目 B.1 的判据，用在 P1/P2 的阶判据上（$Z$ 张成 $\ker[C;L]$，$V$ 张成 $\ker[C;CA]$）。

本模块提供：
- `spectral_gcd(A, C, Lmat)`：返回 (gcd 多项式, h, 子式个数)；
- 多项式用 list[Fraction] 表示（低次在前）。

用法（自检）：python tools/verification/spectral_gcd.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI


# ---------- 多项式（list[Fraction]，低次在前） ----------
def ptrim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else Fr(0)) + (b[i] if i < len(b) else Fr(0)) for i in range(n)])


def psub(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else Fr(0)) - (b[i] if i < len(b) else Fr(0)) for i in range(n)])


def pmul(a, b):
    if a == [Fr(0)] or b == [Fr(0)]:
        return [Fr(0)]
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            out[i + j] += x * y
    return ptrim(out)


def pscale(a, s):
    return ptrim([x * s for x in a])


def pdeg(a):
    a = ptrim(a)
    if a == [Fr(0)]:
        return -1
    return len(a) - 1


def pdivmod(a, b):
    a, b = ptrim(a), ptrim(b)
    if b == [Fr(0)]:
        raise ZeroDivisionError
    q = [Fr(0)] * max(1, len(a) - len(b) + 1)
    r = list(a)
    db = pdeg(b)
    lb = b[-1]
    while pdeg(r) >= db and r != [Fr(0)]:
        d = pdeg(r) - db
        c = r[-1] / lb
        q[d] = c
        shift = [Fr(0)] * d + [c * x for x in b]
        r = psub(r, shift)
    return ptrim(q), ptrim(r)


def pgcd(a, b):
    a, b = ptrim(a), ptrim(b)
    while b != [Fr(0)]:
        _, r = pdivmod(a, b)
        a, b = b, r
    # 首一化
    if a == [Fr(0)] or a[-1] == 0:
        return [Fr(0)]
    return pscale(a, Fr(1) / a[-1])


def pdet(M):
    """M: 矩阵，元素是多项式。递归展开。"""
    k = len(M)
    if k == 0:
        return [Fr(1)]
    if k == 1:
        return ptrim(M[0][0])
    acc = [Fr(0)]
    for j in range(k):
        if pdeg(M[0][j]) < 0:
            continue
        minor = [[M[i][c] for c in range(k) if c != j] for i in range(1, k)]
        term = pmul(M[0][j], pdet(minor))
        if j % 2 == 1:
            term = pscale(term, Fr(-1))
        acc = padd(acc, term)
    return ptrim(acc)


# ---------- 铅笔与 gcd ----------
def build_pencil(A, C, Lmat):
    """返回 (P, h)：P 的元素为多项式（λ 的一次式），h = rank[V|Z]。"""
    n = len(A)
    M = AI.vstack([C, AI.mul(C, A)])
    Vv = AI.nullspace(M)
    V = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]        # n×(n-r1)
    Zv = AI.nullspace([[Fr(x) for x in row] for row in (C + list(Lmat))])
    Z = [[Zv[k][i] for k in range(len(Zv))] for i in range(n)]        # n×d
    AV = AI.mul(A, V)
    P = []
    for i in range(n):
        row = []
        for k in range(len(Vv)):
            row.append([-AV[i][k], V[i][k]])                          # −(AV) + λ V
        for j in range(len(Zv)):
            row.append([Z[i][j]])
        P.append(row)
    h = AI.rank([V[i] + list(Z[i]) for i in range(n)])
    return P, h


def spectral_gcd(A, C, Lmat, verbose=False):
    P, h = build_pencil(A, C, Lmat)
    n = len(P)
    m = len(P[0])
    if h <= 0:
        return [Fr(0)], h, 0
    minors = []
    for rows in itertools.combinations(range(n), h):
        for cols in itertools.combinations(range(m), h):
            M = [[P[r][c] for c in cols] for r in rows]
            d = pdet(M)
            if d != [Fr(0)]:
                minors.append(d)
    if not minors:
        return [Fr(0)], h, 0
    g = minors[0]
    for f in minors[1:]:
        g = pgcd(g, f)
        if pdeg(g) == 0:
            break
    if verbose:
        print(f'  h={h}、子式数={len(minors)}、gcd 次数={pdeg(g)}')
    return g, h, len(minors)


def apply_col(A, Z, name='Z'):
    """$A\\cdot Z$（**列作用**），带方向断言：$Z$ 必须是 $n\\times d$（每列一个基向量）。

    2026-10-30 教训（R16 撤回）：$(A)$、$A$-不变性等检查必须用列作用；
    把 $v^{\\mathsf T}A$（行作用）误当 $Av$ 会得出假反例。
    """
    assert len(Z) == len(A), f'{name} 的行数应 = n = {len(A)}（列基是 n×d）'
    return AI.mul(A, Z)


def spectral_gcd_Z(A, C, Z, verbose=False):
    """直接给 Z（n×d，列满秩）的版本：P(λ)=[(λI−A)V | Z]，V 张成 ker[C;CA]。"""
    n = len(A)
    M = AI.vstack([C, AI.mul(C, A)])
    Vv = AI.nullspace(M)
    V = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
    AV = AI.mul(A, V)
    Z = [[Fr(x) for x in row] for row in Z]
    assert len(Z) == n, 'Z 的行数应 = n（列基；方向断言）'
    assert AI.mul(C, Z) == [[Fr(0)] * len(Z[0]) for _ in range(len(C))], 'Z 的列应被 C 消灭（CZ=0；方向断言）'
    P = []
    for i in range(n):
        row = [[-AV[i][k], V[i][k]] for k in range(len(Vv))]
        row += [[Z[i][j]] for j in range(len(Z[0]))]
        P.append(row)
    h = AI.rank([V[i] + list(Z[i]) for i in range(n)])
    if h <= 0:
        return [Fr(0)], h, 0
    minors = []
    for rows in itertools.combinations(range(n), h):
        for cols in itertools.combinations(range(len(P[0])), h):
            d = pdet([[P[r][c] for c in cols] for r in rows])
            if d != [Fr(0)]:
                minors.append(d)
    if not minors:
        return [Fr(0)], h, 0
    g = minors[0]
    for f in minors[1:]:
        g = pgcd(g, f)
        if pdeg(g) == 0:
            break
    if verbose:
        print(f'  h={h}、子式数={len(minors)}、gcd 次数={pdeg(g)}')
    return g, h, len(minors)


def main():
    # 自检：P1 的两个 4 阶增广 —— L_{0,1} 的 gcd 应为常数，L_{0,0} 应为 λ+5
    A = [[Fr(x) for x in r] for r in
         [[-14, 3, -4, 5, -1, -1, 1, 0],
          [-3, 5, 3, -2, -6, 0, 8, 0],
          [22, -17, 1, -9, 8, 3, -11, 0],
          [9, -11, -2, -6, 7, 1, -5, 0],
          [21, -2, 12, -14, -6, 3, 2, 0],
          [0, 1, -1, 0, 0, -5, 3, 0],
          [10, -9, 1, -3, 5, 1, -10, 0],
          [0, 0, 0, 0, 0, 0, 0, -1]]]
    C = [[Fr(x) for x in r] for r in [[2, -3, 0, 0, 2, 0, -4, 0],
                                      [-1, -10, -3, 2, 5, 0, -10, 0]]]
    L = [[Fr(x) for x in r] for r in [[-2, 3, 1, 0, -2, 0, 1, 0],
                                      [-7, 8, 3, 0, -6, 0, 2, 0]]]

    def L_ab(a, b):
        a, b = Fr(a), Fr(b)
        return L + [
            [-4 * a - 1, 6 * a + 2, 2 * a, 0, -4 * a - 1, -a, 2 * a + 2, 0],
            [2 - 4 * b, 6 * b + 1, 0, 2 * b - 1, -4 * b, -b, 2 * b + 3, 0],
        ]

    for (a, b, tag) in [(0, 1, 'L_{0,1}（(S) 应成立）'), (0, 0, 'L_{0,0}（(S) 应在 λ=−5 失败）')]:
        g, h, cnt = spectral_gcd(A, C, L_ab(a, b), verbose=True)
        print(f'{tag}: gcd = {g}（次数 {pdeg(g)}）')


if __name__ == '__main__':
    main()
