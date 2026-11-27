r"""核验"可实现性"构造：$n=6,p=2,k=2$ 时 $K\cap AK=0$ 可否同时满足 $K=\ker[C;CA]$ 与秩条件。

构造（坐标式）：
  $K=\langle e_1,e_2\rangle$；
  $C$ 的前两列为零、第 3..6 列取单位阵的两行（使 $[C;CA]$ 在 $e_3..e_6$ 上满秩）；
  $A$ 把 $K$ 送到 $\langle e_3,e_4\rangle\subseteq\ker C$，并把 $e_3..e_6$ 送到合适位置使 $[C;CA]$ 秩 $=n-k=4$。

然后对随机的目标对 $(H,H_A)\in(\mathbb Q^{q\times k})^2$，解 $M$ 使
  $M N_K=H$、$M A N_K=H_A$，
并验证解确实存在（线性方程组有解）。
"""

import os
import sys
import random
from fractions import Fraction as Fr

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ   # noqa: E402

F = Fr


def run():
    n, p, k, q = 6, 2, 2, 3
    # C: 前两列 0，第 3..6 列给秩 2
    C = [[F(0), F(0), F(1), F(0), F(0), F(0)],
         [F(0), F(0), F(0), F(1), F(0), F(0)]]
    # A: e1->e3, e2->e4（K 的像落在 ker C 内），其余把 e3..e6 送到独立方向
    # A 按列定义：e1->e5, e2->e6（K 的像落在 ker C = <e1,e2,e5,e6> 内），
    # e5->e3, e6->e4（使 CA 在 e5,e6 上满秩 2），e3,e4->0
    A = [[F(0), F(0), F(0), F(0), F(0), F(0)],   # row1
         [F(0), F(0), F(0), F(0), F(0), F(0)],   # row2
         [F(0), F(0), F(0), F(0), F(1), F(0)],   # row3: e5 -> e3
         [F(0), F(0), F(0), F(0), F(0), F(1)],   # row4: e6 -> e4
         [F(1), F(0), F(0), F(0), F(0), F(0)],   # row5: e1 -> e5
         [F(0), F(1), F(0), F(0), F(0), F(0)]]   # row6: e2 -> e6
    CA = LQ.mul(C, A)
    M = C + CA
    rk = LQ.rank(M)
    NK = LQ.ker_basis_cols(M)
    kmat = NK
    kdim = len(kmat[0]) if kmat else 0
    print(f'rank[C;CA] = {rk}（应 = n-k = {n - k}）；dim K = {kdim}（应 = {k}）')
    # K 与 AK 的交
    Kcols = [[kmat[i][j] for i in range(n)] for j in range(kdim)]
    AKcols = []
    for c in Kcols:
        AKcols.append([sum(A[i][t] * c[t] for t in range(n)) for i in range(n)])
    inter = []
    # 解 alpha: sum a_j K_j = sum b_j AK_j
    m = n
    a, b = len(Kcols), len(AKcols)
    rows = [[Kcols[j][i] for j in range(a)] + [-AKcols[j][i] for j in range(b)] for i in range(m)]
    for z in LQ.ker_basis_cols(rows) if rows else []:
        vec = [sum(z[j] * Kcols[j][i] for j in range(a)) for i in range(m)]
        if any(v != 0 for v in vec):
            inter.append(vec)
    print(f'dim(K ∩ AK) = {LQ.rank([[inter[j][i] for j in range(len(inter))] for i in range(m)]) if inter else 0}（应 = 0）')

    # 可实现性：随机目标对 (H, H_A)，检查 M N_K = H、M A N_K = H_A 是否可解
    rng = random.Random(7)
    ok = 0
    trials = 20
    for _ in range(trials):
        H = [[F(rng.randrange(-2, 3)) for _ in range(kdim)] for _ in range(q)]
        HA = [[F(rng.randrange(-2, 3)) for _ in range(kdim)] for _ in range(q)]
        # 未知：M 的 qn 个条目；方程：q*kd*2 个
        # 写成线性系统：对每个 (row i, col j) 有 sum_t M[i][t] NK[t][j] = H[i][j]
        rows_eq = []
        rhs = []
        for i in range(q):
            for j in range(kdim):
                row = [F(0)] * (q * n)
                for t in range(n):
                    row[i * n + t] = NK[t][j]
                rows_eq.append(row)
                rhs.append(H[i][j])
        # M A N_K = H_A：先算 (A N_K)
        ANK = [[sum(A[i][t] * NK[t][j] for t in range(n)) for j in range(kdim)] for i in range(n)]
        for i in range(q):
            for j in range(kdim):
                row = [F(0)] * (q * n)
                for t in range(n):
                    row[i * n + t] = ANK[t][j]
                rows_eq.append(row)
                rhs.append(HA[i][j])
        # 解（用 least squares 的行化简）：构造增广矩阵并求相容性
        aug = [rows_eq[i] + [rhs[i]] for i in range(len(rows_eq))]
        r1 = LQ.rank([[row[:-1][j] for j in range(q * n)] for row in aug])
        r2 = LQ.rank([[row[j] for j in range(q * n + 1)] for row in aug])
        if r1 == r2:
            ok += 1
    print(f'随机目标对可解：{ok}/{trials}（应 = {trials}）')


if __name__ == '__main__':
    run()
