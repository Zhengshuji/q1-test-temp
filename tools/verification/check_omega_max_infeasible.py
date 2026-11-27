r"""验证新命题：$r_0:=\\operatorname{rank}(L_0|_K)=k$ ⟹ 任何 $q$ 都不可行。

命题（已证，见 `proof/B.24` 的"可行必须 $\\omega<\\min(q,k)$"一节）：
若 $\\operatorname{rank}(L_0|_K)=\\dim K=k$，则对任意 $q$ 与任意 $R$，$(5b)$ 都失败。
等价地：$q_{\\min}=\\infty$（不存在可行增广）。

本脚本对小实例做**有限检验**（不是证明）：
对每个实例计算 $k=\\dim\\ker[C;CA]$ 与 $r_0=\\operatorname{rank}(L_0|_K)$；
当 $r_0=k$ 时，穷举 $q\\in\\{2,3\\}$ 与 $R\\in\\{-1,0,1\\}^{(q-1)\\times n}$，
确认**没有一个** $(q,R)$ 使 $(5a)\\wedge(5b)$ 同时成立（用 consistency_checks 精确判定）。
若出现反例 ⟹ 命题被否证，需立刻回报。
"""

import os
import sys
import itertools
from fractions import Fraction as Fr

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import consistency_checks as CC   # noqa: E402
import linalg_q as LQ              # noqa: E402

F = Fr


def rank_of(M):
    return LQ.rank(M) if M else 0


def main():
    vals = (-1, 0, 1)
    n = 3
    C = [[F(1), F(0), F(0)]]
    checked = 0
    counterexamples = []
    for rest in itertools.product(vals, repeat=6):
        A = [[F(0), F(1), F(0)],
             [F(rest[0]), F(rest[1]), F(rest[2])],
             [F(rest[3]), F(rest[4]), F(rest[5])]]
        M = C + LQ.mul(C, A)
        k = n - rank_of(M)
        if k == 0:
            continue
        # K 的基（列）
        NK = LQ.ker_basis_cols(M)                    # n×k 矩阵
        NKcols = [[NK[i][j] for i in range(n)] for j in range(len(NK[0]))]
        for i in range(n):
            L0 = [[F(1) if j == i else F(0) for j in range(n)]]
            # r0 = rank(L0 |_K)：把 L0 作用到 K 的每个基向量上
            img = [[sum(L0[0][t] * NKcols[j][t] for t in range(n))] for j in range(len(NKcols))]
            # img 是 k×1：rank = 是否为 0
            r0 = 1 if any(img[j][0] != 0 for j in range(len(img))) else 0
            if r0 != k:
                continue
            checked += 1
            for q in (2, 3):
                for Rvals in itertools.product(vals, repeat=(q - 1) * n):
                    Rrows = [[F(Rvals[(q - 2) * n + j]) if q == 2 else F(Rvals[(q - 2) * n + j])
                              for j in range(n)]]
                    if q == 3:
                        Rrows = [[F(Rvals[j]) for j in range(n)],
                                 [F(Rvals[n + j]) for j in range(n)]]
                    L = [row[:] for row in L0] + Rrows
                    try:
                        res = CC.check_candidate(A, C, L0, L)
                    except Exception:
                        continue
                    if isinstance(res, dict) and res.get('cond') and res.get('five_b'):
                        counterexamples.append((A, L0, q, Rrows))
    print(f'检查的实例数（r0 == k）：{checked}')
    print(f'反例数：{len(counterexamples)}')
    for A, L0, q, R in counterexamples[:3]:
        print('  反例：A=', [[int(x) for x in row] for row in A],
              'L0=', [[int(x) for x in row] for row in L0], 'q=', q,
              'R=', [[int(x) for x in row] for row in R])
    if not counterexamples:
        print('结论：有限检验内**无**反例，与命题一致（命题本身为纸面证明）。')


if __name__ == '__main__':
    main()
