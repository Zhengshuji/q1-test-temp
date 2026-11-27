"""gadget_degree.py —— 构件 2：让 $V,K$ 对变量有**仿射**依赖，测不可行条件的次数

**背景**：B.13f 的"二次方程"其实可写成更简单的**线性**形式：设 $\\dim V=\\dim K=1$、$v\\not\\parallel k$，则
$$\\exists\\lambda:(\\lambda I-A)v\\parallel k\\iff\\det[\\,Av,\\ v,\\ k\\,]=0$$
（三重积 $=(Av)\\cdot(v\\times k)$）。若 $v,k$ **固定**（与变量无关），这是变量（$A$ 的条目）的**一次**条件；
只有当 $v,k$ 本身依赖变量时才会升次。

**本轮实验**：把变量放进 $C$（而不是 $A$），即 $C(x)=(1,x,0,0)$，其余固定，于是 $V,K$ 依赖 $x$。
测条件 $\\det[Av,v,k]=0$ 关于 $x$ 的**次数**：若为 2，则"一个二次约束"确实可被表达（gadget 构件 2 成立）。

用法：python -u tools/verification/gadget_degree.py
"""

import os
import sys
import random
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402
import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import toeplitz_criterion as TC           # noqa: E402

F = Fraction
x = sp.symbols('x')


def col(M, j):
    return [M[i][j] for i in range(len(M))]


def triple(u, v, w):
    c = [v[1] * w[2] - v[2] * w[1], v[2] * w[0] - v[0] * w[2], v[0] * w[1] - v[1] * w[0]]
    return sum(u[i] * c[i] for i in range(3)) if len(u) == 3 else None


def main():
    rng = random.Random(20261104)
    n, p, r = 3, 1, 1
    hits = 0
    for trial in range(1500):
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        Cp = [[F(1), F(0), F(0)]]          # 变量 x 放在 C 的第 2 个位置
        L0 = [[F(0), F(0), F(1)]]          # 固定：ker L0 = span{e1,e2}
        if LQ.rank(L0) != r or LQ.rank(Cp + L0) != p + r:
            continue
        Cs = sp.Matrix([[sp.Rational(t.numerator, t.denominator) for t in row] for row in Cp])
        Cs[0, 1] = x
        As = sp.Matrix([[sp.Rational(t.numerator, t.denominator) for t in row] for row in A])
        Ls = sp.Matrix([[sp.Rational(t.numerator, t.denominator) for t in row] for row in L0])
        # 需要 rank[C;CA] = 2（使 dim V = 1）
        M1 = Cs.col_join(Cs * As)
        if sp.Matrix(M1).rank() != 2:
            continue
        ns = sp.Matrix(M1).nullspace()
        if len(ns) != 1:
            continue
        v = ns[0]
        M2 = Cs.col_join(Ls)
        nk = sp.Matrix(M2).nullspace()
        if len(nk) != 1:
            continue
        k = nk[0]
        Av = As * v
        M3 = sp.Matrix.hstack(Av, v, k)          # 3×3
        det = sp.simplify(sp.expand(M3.det()))
        if sp.simplify(det) == 0:
            continue
        num = sp.simplify(sp.numer(sp.cancel(det)))
        poly = sp.Poly(sp.expand(num), x)
        deg = poly.degree()
        hits += 1
        if hits <= 8:
            print(f'  实例 {trial}：条件次数 = {deg}；根 = {sp.roots(poly, x)}')
    print(f'\n共 {hits} 个可用实例（n=3, p=r=1, dim V = dim K = 1，变量在 C 里）')


if __name__ == '__main__':
    main()
