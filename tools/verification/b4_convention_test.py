"""判定 B.4 的正确形式：在 $\\mathcal V=\\mathbb C^n$（即 $\\operatorname{row}[\\mathcal L;C]=\\mathbb C^n$）时，
铅笔在 $\\lambda$ 处降秩，究竟等价于

(P) 存在 $0\\ne x$（**列**向量）使 $Cx=CAx=0$ 且 $(\\lambda I-A)x=0$（右特征向量），
(D) 存在 $0\\ne\\psi$（**行**向量）使 $\\psi C=\\psi CA=0$ 且 $\\psi(\\lambda I-A)=0$（$A^{\\mathsf T}$ 的左特征向量/对偶形式）。

脚本随机取实例，逐条核验，输出 (P)/(D) 与"降秩"的吻合统计。
"""
import os
import sys
import random
from fractions import Fraction
from collections import Counter

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ   # noqa: E402

F = Fraction


def kernel(M):
    """返回 M 的核的基（列向量列表）。"""
    n = len(M[0]) if M else 0
    m = len(M)
    # 用 linalg_q 的 ker_cols（输入是行堆叠）
    import z_generator as ZG
    K = ZG.ker_cols(M, )
    if not K or not K[0]:
        return []
    return [[K[i][j] for i in range(len(K))] for j in range(len(K[0]))]


def main():
    import z_generator as ZG
    rng = random.Random(20261107)
    st = Counter()
    for _ in range(4000):
        n = 3
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        CA = LQ.mul(C, A)
        # L 取 n-1 行，使 row[L;C]=C^n
        for _try in range(20):
            L = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n - 1)]
            if LQ.rank([list(x) for x in L] + C) == n:
                break
        else:
            continue
        lam = F(rng.randrange(-2, 3))
        # 铅笔 (n-1+2) x n
        rows = []
        for r in L:
            rl = [lam * r[j] for j in range(n)]
            la = [sum(r[k] * A[k][j] for k in range(n)) for j in range(n)]
            rows.append([rl[j] - la[j] for j in range(n)])
        rows += CA + C
        drop = LQ.rank(rows) < n
        M = [[lam * (1 if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)]
        # (P): x != 0, Cx=CAx=0, Mx=0  ⟺  ker[C;CA;M] 的维数 > 0 ... 但要 x 非零且同时在两核里
        K1 = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])   # V
        K2 = ZG.ker_cols(M)                                            # ker M
        # 交的维数：dims
        d1 = len(K1[0]) if (K1 and K1[0]) else 0
        d2 = len(K2[0]) if (K2 and K2[0]) else 0
        # 用 [C;CA;M] 的零空间直接算交
        KM = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA] + M)
        dP = len(KM[0]) if (KM and KM[0]) else 0
        P = dP > 0
        # (D): psi != 0 行向量, psi M = 0 且 psi C^T = 0  ⟺  M^T psi^T = 0 与 C psi^T=0
        Mt = [[M[j][i] for j in range(n)] for i in range(n)]
        KD = ZG.ker_cols(Mt + [list(x) for x in C])
        dD = len(KD[0]) if (KD and KD[0]) else 0
        D = dD > 0
        st['样本'] += 1
        st['降秩'] += 1 if drop else 0
        st['P 与降秩一致'] += 1 if (P == drop) else 0
        st['D 与降秩一致'] += 1 if (D == drop) else 0
        if P != drop:
            st['P 反例'] += 1
        if D != drop:
            st['D 反例'] += 1
    print('统计：')
    for k in sorted(st):
        print(f'  {k}: {st[k]}')


if __name__ == '__main__':
    main()
