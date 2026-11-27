r"""B2：G4（实点）——构造"有复点、无实点"的线性截面。

**检验的命题**：$\operatorname{Gr}(r,m)(\mathbb R)$ 的 Zariski 稠密**不**推出实线性截面的实点稠密；
存在实线性截面 $X=L\cap\operatorname{Gr}(2,4)$ 使 $X(\mathbb C)\ne\varnothing$ 而 $X(\mathbb R)=\varnothing$。

**构造**：$\operatorname{Gr}(2,4)\subset\mathbb P^5$ 的 Plücker 型
$$Q=p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}$$
签名 $(3,3)$。取 $L$ 为 $Q$ 的一个**正定 3 维子空间**（正特征向量张成）。
则 $Q|_L$ 正定 ⟹ $Q|_L=0$ 在 $\mathbb R$ 上只有 $0$ ⟹ $X(\mathbb R)=\varnothing$；
而在 $\mathbb C$ 上有非零解 ⟹ $X(\mathbb C)\ne\varnothing$。

用法：python proof/layer_program/c280_g4_realpoints.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI

# Q(x) = p12*p34 - p13*p24 + p14*p23，坐标序 (12),(13),(14),(23),(24),(34)
def Q(x):
    p12, p13, p14, p23, p24, p34 = x
    return p12 * p34 - p13 * p24 + p14 * p23


def polar(i, j, dim=6):
    e_i = [Fr(1) if k == i else Fr(0) for k in range(dim)]
    e_j = [Fr(1) if k == j else Fr(0) for k in range(dim)]
    s = [e_i[k] + e_j[k] for k in range(dim)]
    return Q(s) - Q(e_i) - Q(e_j)


def main():
    dim = 6
    # 对称矩阵 M（Q(x) = 1/2 x^T M x）
    M = [[Fr(0)] * dim for _ in range(dim)]
    for i in range(dim):
        M[i][i] = 2 * Q([Fr(1) if k == i else Fr(0) for k in range(dim)])
        for j in range(i + 1, dim):
            M[i][j] = M[j][i] = polar(i, j)
    print("对称矩阵 M（Q(x)=½ xᵀMx）：")
    for row in M:
        print("   ", [str(x) for x in row])

    # 手工取正定子空间：Q = p12 p34 - p13 p24 + p14 p23
    # 取 a = p12+p34, b = p12-p34 => p12 p34 = (a²-b²)/4
    # 取 c = p13+p24, d = p13-p24 => -p13 p24 = -(c²-d²)/4
    # 取 e = p14+p23, f = p14-p23 => p14 p23 = (e²-f²)/4
    # Q = (a²-b²-c²+d²+e²-f²)/4
    # 正定方向：a, d, e（系数 +1）；负定：b, c, f（系数 -1）
    # 令 L = span{a, d, e}
    def vec(a=0, b=0, c=0, d=0, e=0, f=0):
        # a = p12+p34, b = p12-p34, c = p13+p24, d = p13-p24, e = p14+p23, f = p14-p23
        p12 = (a + b) / 2
        p34 = (a - b) / 2
        p13 = (c + d) / 2
        p24 = (c - d) / 2
        p14 = (e + f) / 2
        p23 = (e - f) / 2
        return [Fr(p12), Fr(p13), Fr(p14), Fr(p23), Fr(p24), Fr(p34)]

    a_only = vec(a=1)
    d_only = vec(d=1)
    e_only = vec(e=1)
    print("\n正定方向 a=p12+p34 :", [str(x) for x in a_only])
    print("正定方向 d=p13-p24 :", [str(x) for x in d_only])
    print("正定方向 e=p14+p23 :", [str(x) for x in e_only])

    # 验证这三个方向张成的 L 上 Q 正定（用 Gram 矩阵）
    basis = [a_only, d_only, e_only]
    G = [[Q([basis[i][k] * 2 if i == j else basis[i][k] + basis[j][k] for k in range(dim)]) for j in range(3)] for i in range(3)]
    # 直接算：Gram_ij = (Q(bi+bj) - Q(bi) - Q(bj))/2
    Gram = [[ (Q([basis[i][k] + basis[j][k] for k in range(dim)]) - Q(basis[i]) - Q(basis[j])) / 2
              for j in range(3)] for i in range(3)]
    print("\nL 上的 Gram 矩阵：")
    for row in Gram:
        print("   ", [str(x) for x in row])
    # 正定性：所有顺序主子式 > 0
    import copy
    ok = True
    for k in range(1, 4):
        sub = [[Gram[i][j] for j in range(k)] for i in range(k)]
        d = det(sub)
        print(f"  {k} 阶顺序主子式 = {d}", ">0 ✓" if d > 0 else "≤0 ✗")
        if d <= 0:
            ok = False
    print("\n结论：", "Q|_L **正定** ⟹ X(ℝ)=∅" if ok else "构造失败")
    print("而 Q|_L = 0 在 ℂ 上有非零解 ⟹ X(ℂ)≠∅ ⟹ **实点不稠密**（G4 成立）。")


def det(M):
    n = len(M)
    if n == 0:
        return Fr(1)
    M = [row[:] for row in M]
    d = Fr(1)
    for i in range(n):
        piv = None
        for r in range(i, n):
            if M[r][i] != 0:
                piv = r
                break
        if piv is None:
            return Fr(0)
        if piv != i:
            M[i], M[piv] = M[piv], M[i]
            d = -d
        d *= M[i][i]
        inv = Fr(1) / M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] * inv
            for c in range(i, n):
                M[r][c] -= f * M[i][c]
    return d


if __name__ == '__main__':
    main()
