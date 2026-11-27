r"""验证专家 QA13 的**结构化左逆次数界**：

设 $P(\lambda)=\lambda E-F\in\mathbb C[\lambda]^{m\times t}$、$\operatorname{rank}E=t$、且 $P(\lambda)$ 对所有 $\lambda$ 满列秩。
则存在多项式矩阵 $X(\lambda)$ 使 $X(\lambda)P(\lambda)=I_t$ 且 $\deg X\le t-1$。

做法：设 $X(\lambda)=\sum_{k=0}^{t-1}\lambda^kX_k$，比较 $\lambda$-系数得到线性方程组，精确求解并验证。

用法：python proof/layer_program/c254_left_inverse.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG


def solve_linear(Amat, b):
    """解 Amat·x = b（精确）；返回一个解或 None。Amat 是列表的列表（行）。"""
    n = len(Amat)
    m = len(Amat[0]) if n else 0
    aug = [list(Amat[i]) + [b[i]] for i in range(n)]
    R, piv = AI.rref(aug)
    x = [Fr(0)] * m
    for row in R:
        p = next((t for t in range(m + 1) if row[t] != 0), None)
        if p is None:
            continue
        if p == m:
            return None
        x[p] = row[m]
    return x


def main():
    rng = random.Random(2026)
    okc = 0
    trials = 4
    for _ in range(trials):
        t = 3
        m = t + 2
        # E：m×t，rank t（前 t 行单位 + 随机）
        E = [[Fr(rng.randint(-2, 2)) for _ in range(t)] for _ in range(m)]
        for i in range(t):
            E[i][i] = Fr(1)
        if AI.rank(E) < t:
            continue
        # F：随机；检查 pencil 满列秩（用 gcd 判据：t×t 子式 gcd = 常数）
        F = [[Fr(rng.randint(-2, 2)) for _ in range(t)] for _ in range(m)]
        # 子式：P(λ) = λE − F 的 t×t 子式
        import itertools
        minors = []
        for rows in itertools.combinations(range(m), t):
            # 每个子式的多项式：det(λ E_r − F_r)
            # 用插值：在 λ=0..t 处求值再插值
            vals = []
            for lam in range(t + 1):
                M = [[lam * E[r][c] - F[r][c] for c in range(t)] for r in rows]
                vals.append(SG.pdet([[ [M[i][j]] for j in range(t)] for i in range(t)]))
            # vals[i] 是常数多项式
            vals = [v[0] for v in vals]
            poly = [Fr(0)] * (t + 1)
            # 拉格朗日插值（点 0..t）
            for i in range(t + 1):
                # 基多项式
                num = [Fr(1)]
                den = Fr(1)
                for j in range(t + 1):
                    if i == j:
                        continue
                    num = SG.pmul(num, [-Fr(j), Fr(1)])
                    den *= Fr(i - j)
                for k in range(len(num)):
                    poly[k] += vals[i] * num[k] / den
            minors.append(poly)
        minors = [x for x in minors if x != [Fr(0)] * (t + 1)]
        if not minors:
            continue
        g = minors[0]
        for mm in minors[1:]:
            g = SG.pgcd(g, mm)
            if SG.pdeg(g) == 0:
                break
        if SG.pdeg(g) != 0:
            continue
        # 满列秩确认；解 X_k
        # 未知量：X_k (t×m)，k=0..t-1 ⟹ 变量数 t*t*m
        nv = t * t * m
        def vid(k, i, j):
            return k * t * m + i * m + j
        rows_eq = []
        rhs = []
        # 系数：λ^j 的 (i,l) 元素 = Σ_k [X_{j-1}E − X_j F]  （X_{-1}=X_t=0）
        for j in range(t + 1):
            for i in range(t):
                for l in range(t):
                    coeffs = [Fr(0)] * nv
                    if j - 1 >= 0:
                        for r in range(m):
                            coeffs[vid(j - 1, i, r)] += E[r][l]
                    if j < t:
                        for r in range(m):
                            coeffs[vid(j, i, r)] -= F[r][l]
                    rows_eq.append(coeffs)
                    rhs.append(Fr(1) if (j == 0 and i == l) else Fr(0))
        sol = solve_linear(rows_eq, rhs)
        if sol is None:
            print(f't={t}, m={m}: 线性系统无解（样本）')
            continue
        # 验证 X(λ)(λE−F) = I：在 λ=0,1,2 处数值检查
        Xk = [[[sol[vid(k, i, j)] for j in range(m)] for i in range(t)] for k in range(t)]
        good = True
        for lam in (0, 1, 2, -1):
            # X(lam) = Σ lam^k Xk
            Xl = [[sum((Fr(lam) ** k) * Xk[k][i][j] for k in range(t)) for j in range(m)]
                  for i in range(t)]
            P = [[Fr(lam) * E[r][c] - F[r][c] for c in range(t)] for r in range(m)]
            prod = [[sum(Xl[i][r] * P[r][c] for r in range(m)) for c in range(t)] for i in range(t)]
            if prod != [[Fr(1) if i == c else Fr(0) for c in range(t)] for i in range(t)]:
                good = False
        print(f't={t}, m={m}: 解出 deg≤{t-1} 的左逆，验证 X(λ)P(λ)=I ⟹ {good}')
        if good:
            okc += 1
    print(f'\n{okc}/{trials} 个实例验证成功')


if __name__ == '__main__':
    main()
