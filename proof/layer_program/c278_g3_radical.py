r"""B3：G3（退化线性截面）的精确判定——$(r,m)=(2,4)$。

**检验的命题**：$X=\operatorname{Gr}(2,4)\cap L$ 的张成是否等于 $L$。
$\operatorname{Gr}(2,4)\subset\mathbb P^5$ 的 Plücker 关系只有一个二次型
$$Q=p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}.$$
$X=L\cap Q$。设 $Q|_L$ 的对称矩阵为 $M$（在 $L$ 的一组基下）：

| $\operatorname{rank}M$ | 几何 | $\operatorname{span}(X)$ |
|---|---|---|
| 0 | $Q|_L\equiv0$，$X=L$ | $=L$ ✓ |
| 1 | $Q|_L=\ell^2$，$X=\{\ell=0\}$ | $=\ell^\perp\subsetneq L$ ⟹ **G3 退化** |
| $\ge2$ | 真二次超曲面 | $=L$ ✓ |

于是判定归结为**一个对称矩阵的秩**——精确、无需 Gröbner。

用法：python proof/layer_program/c278_g3_radical.py
"""
import itertools
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI

# Plücker 坐标顺序：(12),(13),(14),(23),(24),(34)
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def plucker_quadric(u):
    p12, p13, p14, p23, p24, p34 = u
    return p12 * p34 - p13 * p24 + p14 * p23


def basis_of_L(conds, dim=6):
    """L = {c·p = 0}，返回 L 的一组基（向量列表）。"""
    M = [list(c) for c in conds]
    if not M:
        return [[Fr(1) if i == j else Fr(0) for j in range(dim)] for i in range(dim)]
    ns = AI.nullspace(M)
    return ns


def restrict_quadric(basis, dim=6):
    """把 Q 限制到 L：返回对称矩阵 M_ij = Q(b_i + b_j) - Q(b_i) - Q(b_j)（极化），即 2*双线性型。"""
    d = len(basis)
    val = [plucker_quadric(b) for b in basis]

    def polar(i, j):
        s = [basis[i][k] + basis[j][k] for k in range(dim)]
        return plucker_quadric(s) - val[i] - val[j]

    M = [[Fr(0)] * d for _ in range(d)]
    for i in range(d):
        M[i][i] = 2 * val[i]
        for j in range(i + 1, d):
            M[i][j] = M[j][i] = polar(i, j)
    return M


def main():
    random.seed(20261031)
    print("B3：Gr(2,4) 线性截面的张成（rank(M) 判定）")
    print("rank=0 ⟹ X=L；rank=1 ⟹ 退化（span⊊L）；rank>=2 ⟹ span=L\n")
    rows = []
    for E in range(1, 6):
        deg = 0
        tot = 0
        for trial in range(40):
            conds = [[Fr(random.randint(-2, 2)) for _ in range(6)] for _ in range(E)]
            if any(all(x == 0 for x in c) for c in conds):
                continue
            if AI.rank(conds) < E:
                continue
            basis = basis_of_L(conds)
            if not basis:
                continue
            M = restrict_quadric(basis)
            rk = AI.rank(M)
            tot += 1
            if rk == 1:
                deg += 1
                if deg == 1:
                    rows.append((E, len(basis) - 1, rk, "退化示例", conds))
        rows.append((E, None, None, f"{tot} 例中 rank=1 的 {deg} 个", None))

    print(f"{'E':<3}{'dim L':<8}{'rank M':<8}结论")
    for E, dimL, rk, note, _ in rows:
        print(f"{E:<3}{str(dimL):<8}{str(rk):<8}{note}")

    print("\n说明：随机线性条件下 rank(M)=1 的频率给出 G3 的'厚度'经验值；")
    print("精确结论是：**退化 ⟺ Q|_L 是线性形式的平方 ⟺ rank(M)=1**，可精确判定。")


if __name__ == '__main__':
    main()
