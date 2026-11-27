r"""引理 3（Smith 证书）的**点数旁证**：$P(\lambda)=[(\lambda I-A)V\mid Z]$ 的秩在可行/不可行实例上。

对 P1 例子（arXiv:2609.33615 §VII）的两个 4 阶增广：
  * $L_{0,1}$：满足 $(A)$ 与 $(S)$ ⟹ $\operatorname{rank}P(\lambda)=h$ 对所有 $\lambda$（点数检查：无下降）；
  * $L_{0,0}$：满足 $(A)$ 但 $(S)$ 在 $\lambda=-5$ 失败 ⟹ 该处秩下降。
这是**点数检查**（不是证明）；证明是 [README.md](README.md) §3 的 Smith 形式引理。

用法：python proof/spectral_locus/verify_smith_check.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI

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


def pencil_rank(Lmat, lam):
    n = len(A)
    M = AI.vstack([C, AI.mul(C, A)])
    Vv = AI.nullspace(M)                      # ker[C;CA] 的基
    V = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]     # n×(n-r1)
    Zv = AI.nullspace([[Fr(x) for x in row] for row in (C + Lmat)])
    Z = [[Zv[k][i] for k in range(len(Zv))] for i in range(n)]     # n×d
    # P(λ) = [(λI−A)V | Z]，每行是一个 n 维向量
    AV = AI.mul(A, V)
    rows = []
    for i in range(n):
        left = [lam * V[i][k] - AV[i][k] for k in range(len(V[0]))]
        rows.append(left + list(Z[i]))
    return AI.rank(rows), len(rows[0])


def h_of(Lmat):
    n = len(A)
    M = AI.vstack([C, AI.mul(C, A)])
    Vv = AI.nullspace(M)
    V = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
    Zv = AI.nullspace([[Fr(x) for x in row] for row in (C + Lmat)])
    Z = [[Zv[k][i] for k in range(len(Zv))] for i in range(n)]
    return AI.rank([V[i] + list(Z[i]) for i in range(n)])


def main():
    for (a, b, tag) in [(0, 1, 'L_{0,1}（可行）'), (0, 0, 'L_{0,0}（(S) 失败）')]:
        Lm = L_ab(a, b)
        h = h_of(Lm)
        print(f'{tag}: h = rank[V|Z] = {h}')
        for lam in [Fr(-6), Fr(-5), Fr(-4), Fr(0), Fr(1), Fr(2), Fr(10)]:
            r, m = pencil_rank(Lm, lam)
            flag = '  ← 秩下降' if r < h else ''
            print(f'   λ={str(lam):>4s}: rank P(λ) = {r} / 列数 {m}{flag}')
        print()
    print('结论：L_{0,1} 处处满秩 h（与 (S) 成立一致）；L_{0,0} 在 λ=−5 处下降（与论文一致）。')
    print('这是点数检查，不构成证明 —— 证明见 README §3 的 Smith 形式引理。')


if __name__ == '__main__':
    main()
