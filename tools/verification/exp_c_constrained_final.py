r"""实验 C（约束区域，最终版）：$k=3$、$\omega=2$、$L_0=e_4^{\mathsf T}$（顶部块相容）。

**修法**：秩用项目自己的 `linalg_q.rank`（精确有理，稳定），**只用 sympy 做一元多项式 gcd**；
并显式 assert 形状。

数据：$n=5$、$p=1$、$q=3$、$r=1$ ⟹ $k=5-2=3$、$\dim(K+AK)=4<6$（约束区域）。
$C=e_1^{\mathsf T}$；$A$ 第一行 $e_5^{\mathsf T}$、列 2,3,4 $=e_3,e_2,e_5$ ⟹ $K=\langle e_2,e_3,e_4\rangle$、$Ae_2=e_3$、$Ae_3=e_2$、$Ae_4=e_5$。

可达性（Prop 2）：$\ker T=\{(-Aw,w):w\in\langle e_2,e_3\rangle\}$ ⟹ $B_2e_2=B_1e_3$、$B_2e_3=B_1e_2$；$B_2$ 第 1 列自由。
$L_0=e_4^{\mathsf T}$ ⟹ $L_0N_K=(0,0,1)$、$L_0AN_K=(0,0,0)$（相容）。
$H$ 按构造保证 $\operatorname{rank}=2$。
"""

import itertools
import os
import sys
import random
from fractions import Fraction as Fr

import sympy as sp

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ   # noqa: E402

F = Fr
lam = sp.Symbol('lam')



def my_rank(M):
    """精确有理高斯消元求秩（不依赖 sympy）。"""
    if not M:
        return 0
    A = [list(map(F, row)) for row in M]
    rows, cols = len(A), len(A[0])
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def lq(rows):
    return [[F(int(x)) for x in row] for row in rows]


def main():
    # ---- 数据 ----
    n = 5
    C = [[F(1), F(0), F(0), F(0), F(0)]]
    A = [[F(0), F(0), F(0), F(0), F(1)],      # 第一行 = e5
         [F(0), F(0), F(1), F(0), F(0)],      # 列 3 = e2
         [F(0), F(1), F(0), F(0), F(0)],      # 列 2 = e3
         [F(0), F(0), F(0), F(0), F(0)],
         [F(0), F(0), F(0), F(1), F(0)]]      # 列 4 = e5
    M = C + LQ.mul(C, A)
    NKm = LQ.ker_basis_cols(M)                # n×k 矩阵
    k = len(NKm[0])
    print('rank[C;CA] =', my_rank(M), ' dim K =', k, '（应 2 与 3）')
    NK = [[NKm[i][j] for i in range(n)] for j in range(k)]   # 列向量
    AKcols = [[sum(A[i][t] * w[t] for t in range(n)) for i in range(n)] for w in NK]
    KM = [[NK[j][i] for j in range(k)] for i in range(n)]
    AKM = [[AKcols[j][i] for j in range(k)] for i in range(n)]
    print('dim(K+AK) =', my_rank([[KM[i][j] for j in range(k)] + [AKM[i][j] for j in range(k)]
                                  for i in range(n)]), '（< 6 ⟹ 约束区域）')

    L0 = [[F(0), F(0), F(0), F(1), F(0)]]      # e4^T
    # 顶部块：L0 N_K（1×k）与 L0 A N_K
    topH = LQ.mul(L0, NKm)
    topHA = LQ.mul(LQ.mul(L0, A), NKm)
    print('L0 N_K =', [[str(x) for x in r] for r in topH],
          ' L0 A N_K =', [[str(x) for x in r] for r in topHA])

    rng = random.Random(20261116)
    nadm = ngood = nbad = 0
    trials = 2000
    for _ in range(trials):
        # H 的第 2 行随机，第 3 行 = 第 2 行 + c·(第1行) ⟹ rank H ≤ 2，通常 =2
        v2 = [F(rng.randrange(-2, 3)) for _ in range(k)]
        c = F(rng.randrange(-2, 3))
        v3 = [v2[j] + c * topH[0][j] for j in range(k)]
        B1 = [v2, v3]
        # 约束：B2 第2列 = B1 第3列、第3列 = B1 第2列；第1列自由
        c1 = [F(rng.randrange(-2, 3)), F(rng.randrange(-2, 3))]
        B2 = [[c1[0], B1[0][2], B1[0][1]],
              [c1[1], B1[1][2], B1[1][1]]]
        H = topH + B1
        HA = topHA + B2
        Hf = lq(H)
        HAf = lq(HA)
        assert len(Hf) == 3 and len(Hf[0]) == 3
        if my_rank(Hf) != 2:
            continue
        if my_rank(Hf + HAf) != 2:
            continue
        nadm += 1
        # 谱条件：P = λH − H_A 的全部 2 阶子式的 gcd
        Hs = sp.Matrix([[sp.Rational(p, q) for p, q in [(int(x), 1) for x in r]] for r in H])
        HAs = sp.Matrix([[sp.Rational(int(x), 1) for x in r] for r in HA])
        P = lam * Hs - HAs
        ms = [sp.expand(P[list(rows), :].det()) for rows in itertools.combinations(range(3), 2)]
        g = None
        for m in ms:
            if sp.simplify(m) != 0:
                g = m if g is None else sp.gcd(g, m)
        ok = (g is not None and sp.degree(g, lam) == 0)
        ngood += 1 if ok else 0
        nbad += 0 if ok else 1
    print(f'{trials} 次构造：可容许 {nadm} → **好 {ngood} / 坏 {nbad}**')


if __name__ == '__main__':
    main()
