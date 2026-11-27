r"""$r=1$ 层的精确参数化（sympy）：找出 $(A)$ 在该层上的条件。

chart：$Z$ 的列 = $e_4+a e_7+d e_8$、$e_5+b e_7+e e_8$、$e_6+c e_7+f e_8$。
$CA=[e_7;e_8]$ ⟹ $CAZ$ 的两行是 $(a,b,c)$、$(d,e,f)$；$r=1$ ⟺ 两行成比例，记为 $(d,e,f)=\lambda(a,b,c)$。

在 $r=1$ 上计算 $(A)$：$A(\operatorname{im}Z\cap\ker CA)\subseteq\operatorname{im}Z$，把条件化为 $(a,b,c,\lambda)$ 的多项式并分解。

用法：python proof/layer_program/c250_r1_stratum.py
"""
import sympy as sp


def main():
    a, b, c, lam = sp.symbols('a b c lam')
    # 8 维坐标 e1..e8
    e = [sp.Matrix([1 if k == i else 0 for k in range(8)]) for i in range(8)]
    # Z 的三列（r=1：第二行 = lam * 第一行）
    z1 = e[3] + a * e[6] + lam * a * e[7]
    z2 = e[4] + b * e[6] + lam * b * e[7]
    z3 = e[5] + c * e[6] + lam * c * e[7]
    Z = sp.Matrix.hstack(z1, z2, z3)
    # ker(CAZ) = {(x1,x2,x3): a x1 + b x2 + c x3 = 0}
    # K' = Z · ker(CAZ)
    # 取核的两个基向量（符号化）
    x1, x2, x3 = sp.symbols('x1 x2 x3')
    eq = a * x1 + b * x2 + c * x3
    # 解出 x3 = -(a x1 + b x2)/c（假设 c≠0；一般情形由对称性覆盖）
    k1 = sp.Matrix([1, 0, -a / c])
    k2 = sp.Matrix([0, 1, -b / c])
    Kp = sp.Matrix.hstack(Z * k1, Z * k2)
    # A：e4->e8, e5->e5, e6->e6, e1->e3, e2->e4, e3->e7, e7->e1, e8->e2
    A = sp.zeros(8, 8)
    A[7, 3] = 1   # e4 -> e8
    A[4, 4] = 1   # e5 -> e5
    A[5, 5] = 1   # e6 -> e6
    A[2, 0] = 1   # e1 -> e3
    A[3, 1] = 1   # e2 -> e4
    A[6, 2] = 1   # e3 -> e7
    A[0, 6] = 1   # e7 -> e1
    A[1, 7] = 1   # e8 -> e2
    AKp = A * Kp
    M = sp.Matrix.hstack(Z, AKp)
    print('M 的尺寸：', M.shape)
    # (A) ⟺ rank M = 3 ⟺ 所有 4x4 子式 = 0
    minors = []
    rows = list(range(8))
    import itertools
    for rsel in itertools.combinations(range(8), 4):
        for csel in itertools.combinations(range(5), 4):
            sub = M[list(rsel), list(csel)]
            d = sp.simplify(sub.det())
            if d != 0:
                minors.append(sp.factor(d))
    print(f'非零的 4x4 子式个数：{len(minors)}')
    uniq = list({m for m in minors})
    print('互不相同的非零子式：')
    for m in uniq[:8]:
        print('  ', m)


if __name__ == '__main__':
    main()
