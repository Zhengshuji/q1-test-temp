r"""在 $r=1$ 的边界 chart 上（$(A)\iff b=0$，参数 $(a,\mu)$）计算 $(S)$：
商铅笔 $T_\lambda$（$3\times2$）的极大子式 gcd，作为 $(a,\mu)$ 的函数。

$Z=[e_4+a e_7+\mu a e_8,\ e_5,\ e_6]$；$\mathcal V=\operatorname{span}(e_3,e_4,e_5,e_6)$；
$S=\mathcal V\cap Z=\operatorname{span}(e_5,e_6)$（$a\ne0$）；$\mathcal V/S=\operatorname{span}(e_3,e_4)$；
$\ker C/Z$ 用 $e_3,e_4,e_7$ 的类作基（$\dim q=3$）。

用法：python proof/layer_program/c252_r1_S.py
"""
import sympy as sp


def main():
    a, mu, lam = sp.symbols('a mu lam')
    e = [sp.Matrix([1 if k == i else 0 for k in range(8)]) for i in range(8)]
    z1 = e[3] + a * e[6] + mu * a * e[7]
    z2 = e[4]
    z3 = e[5]
    Z = sp.Matrix.hstack(z1, z2, z3)
    A = sp.zeros(8, 8)
    A[7, 3] = 1; A[4, 4] = 1; A[5, 5] = 1
    A[2, 0] = 1; A[3, 1] = 1; A[6, 2] = 1
    A[0, 6] = 1; A[1, 7] = 1
    # V 的基
    V = sp.Matrix.hstack(e[2], e[3], e[4], e[5])
    # S 的基：e5, e6 在 V 坐标下是 e3,e4（第 4,5 列）；V/S 用 e3, e4
    # 商铅笔：T_λ 的列 = (λ u − A u) mod Z，u = e3, e4
    # 用 Z 的列 + e3, e4 的“修正”作基不严格；直接构造 3x2 的 T：
    # 对 u in {e3, e4}: (λ u − A u) 在 V+Z 中，模 Z 后落在 span(e3, e4, e7)/(Z)
    # 这里用最直接的做法：T 的元素取 (λ u − Au) 在基 [z1,z2,z3,e3,e4,e7] 下的坐标
    B = sp.Matrix.hstack(z1, z2, z3, e[2], e[3], e[6])   # 8x6 的生成集
    # 用最小范数解坐标（这里直接解线性系统）
    cols = []
    for u in (e[2], e[3]):
        x = sp.simplify(lam * u - A * u)
        # 解 B c = x 的最小二乘符号解（B 非方阵）；用 B.T B 不可行，改为：
        # 因为 x 在 B 的列空间里，解 c 用 B.B^T? 简化：用 sp.linsolve
        c = sp.linsolve((B, x), sp.symbols('c1:7'))
        cols.append(c)
    print('T 的列（解集）：')
    for c in cols:
        print('  ', c)


if __name__ == '__main__':
    main()
