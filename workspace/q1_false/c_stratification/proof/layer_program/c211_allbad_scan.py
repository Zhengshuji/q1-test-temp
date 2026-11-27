r"""all-bad 的实例核查：P2（arXiv:2609.37992）§VII 的例子在 q=3,4 上"$(A)$ 可行但全部 $(S)$ 失败"。

做法（精确有理算术）：固定阶 $q$、$d=n-p-q$、$m_L=n-\operatorname{rank}[C;L_0]$。
对每个图卡 $I$（$d$ 行的子集）与参数 $\Theta\in\mathbb R^{(m_L-d)\times d}$：
$$Z=K_LW_I(\Theta),\quad W_I(\Theta)=P_I^{\mathsf T}\binom{I_d}{\Theta},$$
逐点检查
- $(A)$：$\operatorname{rank}[Z,\ AZR_Z]=d$，$\operatorname{im}R_Z=\ker(CAZ)$；
- $(S)$：$h=\operatorname{rank}[V\mid Z]$，$\operatorname{rank}[(\lambda I-A)V\mid Z]=h$ 对一批 $\lambda$ 成立。

注意：$\lambda$ 只取有限点 ⟹ $(S)$ 的"通过"是**必要不充分**；因此本脚本对"(S) 失败"是**充分**的（找到失败点即真失败），
对"(S) 通过"只作参考。这是**点数检查**，不是证明。

��**已被 c212_allbad_exact.py 取代**（本脚本的 $(S)$ 测试是点数式的，会漏复根/非整数根，见 CLAUDE §10.1）。保留作对照。\n\n用法：python proof/layer_program/c211_allbad_scan.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI

# P2 §VII 的例子
A = [[Fr(x) for x in r] for r in
     [[0, 1, 0, 1, 0, 0, 0, 0],
      [0, -1, 1, 0, 0, 0, 0, -1],
      [1, 0, -1, 1, 0, 0, 1, -1],
      [-1, -1, 0, -2, 0, 0, 0, 0],
      [0, 0, 0, 0, -2, 0, 0, 1],
      [0, 0, 0, 0, 0, -2, 1, 0],
      [0, 0, 0, 0, 0, -1, -2, 1],
      [0, 0, 0, 0, 0, 0, 1, -2]]]
C = [[Fr(x) for x in r] for r in [[-2, -2, 2, -2, -1, 0, 1, -3],
                                  [0, 0, 1, 2, 2, 3, -1, -2]]]
L = [[Fr(x) for x in r] for r in [[-2, -1, -2, -3, -1, 3, 2, 0],
                                  [1, -1, -2, 1, 0, 2, 0, 1]]]
n = len(A)
p = len(C)


def chart_matrix(d, I, theta):
    """W_I(Θ) = P_I^T [I_d; Θ]：行 I 放 I_d，其余行按序放 Θ。返回 m_L×d。"""
    m = n - AI.rank([[Fr(x) for x in row] for row in (C + L)])
    W = [[Fr(0)] * d for _ in range(m)]
    Iset = set(I)
    for a, row_idx in enumerate(I):
        W[row_idx][a] = Fr(1)
    free = [r for r in range(m) if r not in Iset]
    for a, row_idx in enumerate(free):
        for b in range(d):
            W[row_idx][b] = theta[a][b]
    return W


def check_point(d, I, theta):
    m = n - AI.rank([[Fr(x) for x in row] for row in (C + L)])
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L)])   # 基（列）
    KL = [[KLv[k][i] for k in range(len(KLv))] for i in range(n)]    # n×m
    W = chart_matrix(d, I, theta)
    Z = AI.mul(KL, W)                                                # n×d
    # (A): rank[Z, AZR] = d, im R = ker(CAZ)
    CA = AI.mul(C, A)
    CAZ = AI.mul(CA, Z)                                              # p×d
    Rv = AI.nullspace(CAZ)                                           # 基
    R = [[Rv[k][i] for k in range(len(Rv))] for i in range(n if False else len(Rv))]
    # 构造 d×(d-rank) 的 R：Rv 是 d 维向量
    R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZ = AI.mul(A, Z)
    AZR = AI.mul(AZ, R)
    M1 = [[Z[i][j] for j in range(d)] + [AZR[i][j] for j in range(len(Rv))] for i in range(n)]
    okA = AI.rank(M1) == d
    # (S): h = rank[V|Z]，P(λ)=[(λI−A)V | Z]
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    V = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
    h = AI.rank([V[i] + list(Z[i]) for i in range(n)])
    AV = AI.mul(A, V)
    okS = True
    for lam in [Fr(x) for x in range(-8, 9)]:
        rows = [[lam * V[i][k] - AV[i][k] for k in range(len(Vv))] + list(Z[i]) for i in range(n)]
        if AI.rank(rows) != h:
            okS = False
            break
    return okA, okS, h


def main():
    grid = [Fr(x) for x in (-1, 0, 1)]
    print(f'n={n}, p={p}, r={len(L)}')
    for q in (3, 4, 5):
        d = n - p - q
        m = n - AI.rank([[Fr(x) for x in row] for row in (C + L)])
        print(f'\nq={q}: d={d}, m_L={m}；图卡数 = C({m},{d}) = {len(list(itertools.combinations(range(m), d)))}')
        totA = totS = 0
        examples = []
        for I in itertools.combinations(range(m), d):
            for t in itertools.product(grid, repeat=(m - d) * d):
                theta = [list(t[k * d:(k + 1) * d]) for k in range(m - d)]
                okA, okS, h = check_point(d, I, theta)
                if okA:
                    totA += 1
                    if okS:
                        totS += 1
                    else:
                        examples.append((I, t, h))
        print(f'  (A) 成立的采样点：{totA}；其中 (S) 通过：{totS}'
              + (f'；首个 (S) 失败例：图卡 {examples[0][0]}, Θ={examples[0][1]}, h={examples[0][2]}' if examples else ''))


if __name__ == '__main__':
    main()


