r"""Stage 2 探针：最小**约束区域**实例（$n=4,p=1,q=2,r=1,k=2$，$n-p=3<2k=4$）。

构造：$C=e_1^{\mathsf T}$；$A$ 的第一行为 $e_4^{\mathsf T}$（使 $CA=e_4^{\mathsf T}$，$K=\langle e_2,e_3\rangle$），
$A$ 在 $K$ 上是**交换** $e_2\leftrightarrow e_3$（故 $AK=K$、$K\cap AK=K\ne0$ ⟹ 约束区域），其余列为 0。

预期（手算，需机器核对）：
  * $\dim K=2$、$\ker T$ 维数 2（$T(v,w)=v+Aw$）；
  * $H_A=H\,P$（$P$ 为交换矩阵）⟹ 兼容约束是 **$B_2=B_1P$**（线性同构！）；
  * $\lambda H-H_A=H(\lambda I-P)$ ⟹ 秩降只可能发生在 $\lambda=\pm1$；
  * 于是可行 ⟺ 能选 $(r_2,r_3)$ 避开两个条件。
"""

import os
import sys
import itertools
from fractions import Fraction as Fr

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ        # noqa: E402
import consistency_checks as CC  # noqa: E402

F = Fr


def main():
    n = 4
    # A 的行：row1 = e4（使 CA=e4）；row2 = e3 位置使 A e3 = e2；row3 = e2 位置使 A e2 = e3；row4 = 0
    A = [[F(0), F(0), F(0), F(1)],
         [F(0), F(0), F(1), F(0)],
         [F(0), F(1), F(0), F(0)],
         [F(0), F(0), F(0), F(0)]]
    # 检查：CA 应为 e4^T
    C = [[F(1), F(0), F(0), F(0)]]
    CA = LQ.mul(C, A)
    print('CA =', [[str(x) for x in row] for row in CA], '（应为 e4^T）')
    M = C + CA
    NKmat = LQ.ker_basis_cols(M)
    k = len(NKmat[0]) if NKmat else 0
    print('dim K =', k, '（应为 2）')
    NK = [[NKmat[i][j] for i in range(n)] for j in range(k)]   # 列向量列表

    # ker T：T(v,w)=v+Aw，v,w in K
    # 解：v = -Aw, 要求 Aw in K
    AKcols = []
    for w in NK:
        Ak = [sum(A[i][t] * w[t] for t in range(n)) for i in range(n)]
        AKcols.append(Ak)
    print('A e2 =', [[str(x)] for x in AKcols[0]], ' A e3 =', [[str(x)] for x in AKcols[1]])

    # 对若干 R 检查 (a) H_A=H P (b) 可行性
    L0 = [[F(0), F(0), F(1), F(0)]]   # L0 = e3^T
    for R in ([[F(1), F(0), F(0), F(0)]], [[F(0), F(1), F(0), F(0)]],
              [[F(0), F(0), F(1), F(1)]], [[F(0), F(0), F(1), F(0)]]):
        L = [row[:] for row in L0] + [row[:] for row in R]
        H = LQ.mul(L, NKmat)
        H_A = LQ.mul(LQ.mul(L, A), NKmat)
        # 手算预言：H_A = H * P （列交换）
        HP = [[H[i][1], H[i][0]] for i in range(len(H))]
        same = (H_A == HP)
        try:
            res = CC.check_candidate(A, C, L0, L)
            verdict = f"(5a)={res.get('five_a')}, (5b)={res.get('five_b')}"
        except Exception as e:
            verdict = f'约定排除（{type(e).__name__}）'
        r = [str(x) for x in R[0]]
        print(f'R=({",".join(r)})  H_A==H·P? {same}   {verdict}')


if __name__ == '__main__':
    main()
