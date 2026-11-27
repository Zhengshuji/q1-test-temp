"""scalar_gadget.py —— 把 B.13e 的条件写成**一个二次方程**（标量情形 $\dim V=\dim K=1$）

**目标**（专家 §D1 的 gadget 第一步）：证明"某阶不可行"在标量情形下等价于**一个二次方程**，
即不可行性可以写成多项式的零点条件——这是把二次方程组编码进来的必要构件。

**推导**：设 $\dim V=\dim K=1$，$V=\langle v\rangle$、$K=\langle k\rangle$（$v,k\in\mathbb C^n$）。
单-$\\lambda$ 证书（B.13e）要求 $\\exists\\lambda_0$ 使 $(\\lambda_0I-A)v\\parallel k$。
把 $\\lambda$ 当未知，这等价于
$$(\\lambda v-Av)\\times k=0\\ \\text{对某个}\\ \\lambda
\\iff (Av)\\times k\\ \\text{与}\\ v\\times k\\ \\text{共线}
\\iff \\bigl((Av)\\times k\\bigr)\\times(v\\times k)=0 .$$
（前者关于 $\\lambda$ 线性，消去 $\\lambda$ 后剩下的就是最后一个**二次**条件。）

**核验**：在 $n=3$、$p=r=1$、$\\dim V=\\dim K=1$、$q=1$（此时 $d=1=\\dim K$，$\\mathcal Z=K$ 被强制）
的实例上比较：
* (i) 上述二次条件是否成立；
* (ii) 唯一候选 $\\mathcal Z=K$ 是否真的失败（Toeplitz 精确判据）。
二者应当一致（若一致，则"该阶不可行" $\\iff$ 一个二次方程，标量情形下**已证**）。

用法：python -u tools/verification/scalar_gadget.py
"""

import os
import sys
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import toeplitz_criterion as TC           # noqa: E402

F = Fraction


def cross(u, v):
    return [u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0]]


def col(M, j):
    return [M[i][j] for i in range(len(M))]


def main():
    rng = random.Random(20261104)
    st = Counter()
    n, p, r, q = 3, 1, 1, 1
    for trial in range(3000):
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        if LQ.rank(C) != 1 or LQ.rank(L0) != 1:
            continue
        if LQ.rank([list(x) for x in C] + L0) != 2:
            continue
        CA = LQ.mul(C, A)
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        dV = len(V[0]) if (V and V[0]) else 0
        dK = len(K[0]) if (K and K[0]) else 0
        if not (dV == 1 and dK == 1):
            continue
        # q=1：d = n-p-q = 1 = dim K ⟹ Z = K 强制
        kvec = col(K, 0)
        Z = [[kvec[i]] for i in range(n)]      # n×1 矩阵
        L = ZG.L_from_Z(A, C, L0, Z, 1)
        if L is None or not LQ.condA(A, C, L):
            continue
        st['admissible'] += 1
        v = col(V, 0)
        k = kvec
        Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
        vk = cross(v, k)
        nondeg = any(t != 0 for t in vk)                 # V ≠ K（否则证书的例外成立）
        cond = cross(cross(Av, k), vk)                   # 二次条件
        quad_ok = all(t == 0 for t in cond)
        if not nondeg:
            # 退化：v ∥ k ⟹ 叉积恒零，条件无意义；单列统计
            st['degenerate(V=K)'] += 1
        # Toeplitz 精确判据
        try:
            res = TC.analyse(A, C, L)
        except AssertionError:
            st['toeplitz_assert'] += 1
            continue
        fails = (not res['five_b'])
        if not nondeg:
            st['degenerate_feasible' if not fails else 'degenerate_fail'] += 1
            continue
        st['tested'] += 1
        if quad_ok == fails:
            st['agree'] += 1
        else:
            st['disagree'] += 1
            if st['disagree'] <= 5:
                print(f'  不一致：二次条件={quad_ok}，实际失败={fails}（h={res["h"]}）')
    print('统计：', dict(st))
    print('  agree = "二次条件成立" == "该阶不可行"；disagree 应为 0')
    print('  注：q=1 时 d=1=dim K，Z 被强制，故"整族不可行"就是"唯一候选失败"')


if __name__ == '__main__':
    main()
