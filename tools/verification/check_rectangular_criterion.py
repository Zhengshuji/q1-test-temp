r"""核对"矩形判据"的正确形式（Stage 1 修正版）在反例实例上的表现。

正确判据：$(5b)\iff\gcd\{\text{全部 }\omega\text{ 阶子式 of }\lambda H-H_A\}\in\mathbb C^\times$
（$\omega=\operatorname{rank}H$、$H=\mathcal L N_K$、$H_A=\mathcal LA N_K$）。

本例 $k=1$、$\omega=1$、$q=2$：铅笔 $\lambda H-H_A$ 是 $2\times1$，
其 $1$ 阶子式就是两个条目——两个线性多项式；条件是它们**无公共复根**。
"""

import os
import sys
from fractions import Fraction as Fr

import sympy as sp

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ   # noqa: E402


def analyse(A, C, L0, R, tag):
    n = len(A)
    M = C + LQ.mul(C, A)
    NK = LQ.ker_basis_cols(M)
    k = len(NK[0]) if NK else 0
    As = sp.Matrix(A)
    Cs = sp.Matrix(C)
    L0s = sp.Matrix(L0)
    Rs = sp.Matrix(R)
    Ls = L0s.col_join(Rs)
    NKs = sp.Matrix(NK)
    H = Ls * NKs
    HA = (Ls * As) * NKs
    om = H.rank()
    lam = sp.Symbol('lam')
    P = lam * H - HA                     # q x k 多项式矩阵（一次）
    print(f'{tag}: k={k}, omega={om}, H={H.tolist()}, H_A={HA.tolist()}')
    if om == 0:
        print('  omega=0 ⟹ 无 0 阶子式，条件空洞（(5b) 自动成立）')
        return
    # omega 阶子式：选 omega 列（这里 k=1，只有一列）与 q 中选 omega 行
    import itertools
    minors = []
    for rows in itertools.combinations(range(P.rows), om):
        sub = P[list(rows), :]
        if sub.cols == om:
            m = sp.expand(sub.det())
            minors.append((rows, sp.Poly(m, lam) if m != 0 else None))
    print('  omega 阶子式:', [(r, sp.factor(m.as_expr()) if m is not None else 0) for r, m in minors])
    # 公共根：两两求 gcd（这里只有 k=1，子式是线性多项式）
    g = None
    for _, m in minors:
        if m is None:
            continue
        g = m if g is None else sp.gcd(g, m)
    print('  子式的 gcd =', sp.factor(g.as_expr()) if g is not None else 'none',
          ' ⟹', '常数（(5b) 成立）' if g is not None and sp.degree(g.as_expr(), lam) == 0 else '非常数（(5b) 失败）')


def main():
    # 反例实例（我错误命题的反例）
    A = [[0, 1, 0], [-1, -1, -1], [-1, -1, -1]]
    C = [[1, 0, 0]]
    L0 = [[0, 0, 1]]
    print('=== 反例实例（应可行：子式 gcd 为常数）===')
    analyse(A, C, L0, [[-1, -1, -1]], 'A1/L0=e3, R=(-1,-1,-1)')

    print('\n=== 同一实例的另一 R（看判据是否随 R 变）===')
    analyse(A, C, L0, [[0, 0, 0]], 'A1/L0=e3, R=(0,0,0)')


if __name__ == '__main__':
    main()
