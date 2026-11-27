r"""$c=0$ 边界 chart（R17 点所在）的符号计算：$r=1$ 层的 $(A)$ 条件。

$Z=[e_4+a e_7+d e_8,\ e_5+b e_7+e e_8,\ e_6]$，$r=1\iff ae=bd$，参数化 $(d,e)=\mu(a,b)$。
$(A)\iff A(Z\cdot\ker(CAZ))\subseteq\operatorname{im}Z$，把 $4\times4$ 子式化简分解。

用法：python proof/layer_program/c251_boundary_chart.py
"""
import itertools
import sympy as sp


def main():
    a, b, mu = sp.symbols('a b mu')
    e = [sp.Matrix([1 if k == i else 0 for k in range(8)]) for i in range(8)]
    z1 = e[3] + a * e[6] + mu * a * e[7]
    z2 = e[4] + b * e[6] + mu * b * e[7]
    z3 = e[5]
    Z = sp.Matrix.hstack(z1, z2, z3)
    # ker(CAZ) = {(x1,x2,x3): a x1 + b x2 = 0}
    # 取基：(b,-a,0)、(0,0,1)
    k1 = sp.Matrix([b, -a, 0])
    k2 = sp.Matrix([0, 0, 1])
    Kp = sp.Matrix.hstack(Z * k1, Z * k2)
    A = sp.zeros(8, 8)
    A[7, 3] = 1; A[4, 4] = 1; A[5, 5] = 1
    A[2, 0] = 1; A[3, 1] = 1; A[6, 2] = 1
    A[0, 6] = 1; A[1, 7] = 1
    AKp = A * Kp
    M = sp.Matrix.hstack(Z, AKp)
    print('M 尺寸：', M.shape)
    uniq = set()
    for rsel in itertools.combinations(range(8), 4):
        for csel in itertools.combinations(range(5), 4):
            d = sp.simplify(M[list(rsel), list(csel)].det())
            if d != 0:
                uniq.add(sp.factor(d))
    print(f'互不相同的非零 4x4 子式（{len(uniq)} 个）：')
    for m in sorted(uniq, key=str)[:10]:
        print('  ', m)


if __name__ == '__main__':
    main()
