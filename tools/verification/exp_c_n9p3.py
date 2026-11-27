r"""实验 C（结构化版，修正维数后）：$n=9,\ p=3,\ q=3,\ r=1$ ⟹ $k=3$、$\omega=2$、$k>\omega$，**自由区域**。

数据：$C=[I_3\ 0]$（$3\times9$）；$A$ 的列 4,5,6 $=e_1,e_2,e_3$、列 7,8,9 $=e_4,e_5,e_6$、列 1,2,3 $=0$。
则 $CA$ 的行为 $e_4^{\mathsf T},e_5^{\mathsf T},e_6^{\mathsf T}$，$[C;CA]$ 的 6 行为 $e_1..e_6$ ⟹ $\operatorname{rank}=6$、$k=3$、
$K=\langle e_7,e_8,e_9\rangle$、$AK=\langle e_4,e_5,e_6\rangle$ ⟹ $K\cap AK=0$（**自由区域**）。

构造：$L_0=e_7^{\mathsf T}$；$H=UV$、$H_A=GV$（$3\times3$、秩 2），顶部行 ${=}L_0N_K=(1,0,0)$、$L_0AN_K=(0,0,0)$；
随机 $U,G$ 的第 2、3 行；解 $R$（$2\times9$）由 $RN_K=H_{2:3,:}$、$RAN_K=(H_A)_{2:3,:}$；
谱条件：$3\times2$ 铅笔 $\lambda U-G$ 的三个 2 阶子式的 gcd 是否为非零常数。
"""

import itertools
import random
import sympy as sp

F = sp.Rational
lam = sp.Symbol('lam')


def build():
    n = 9
    C = sp.zeros(3, n)
    for i in range(3):
        C[i, i] = 1
    A = sp.zeros(n, n)
    for k in range(3):
        A[k, 3 + k] = 1       # 列 4,5,6 = e1,e2,e3
        A[3 + k, 6 + k] = 1   # 列 7,8,9 = e4,e5,e6
    return A, C


def main():
    A, C = build()
    n = 9
    M = C.col_join(C * A)
    NKm = M.nullspace()
    NK = sp.Matrix.hstack(*NKm)
    print('rank[C;CA] =', M.rank(), ' dim K =', NK.cols, '（应 6 与 3）')
    Kcols = [NK[:, j] for j in range(NK.cols)]
    AK = [A * Kcols[j] for j in range(len(Kcols))]
    print('dim(K + AK) =', sp.Matrix.hstack(*Kcols, *AK).rank(), '（= 6 ⟹ K ∩ AK = 0 ✓）')
    L0 = sp.zeros(1, n)
    L0[0, 6] = 1
    print('L0 N_K =', (L0 * NK).tolist(), '  L0 A N_K =', (L0 * A * NK).tolist())

    rng = random.Random(20261114)
    U0 = sp.Matrix([[1, 0]])
    G0 = sp.Matrix([[0, 0]])
    V = sp.Matrix([[1, 0, 0], [0, 1, 0]])
    ngood = nbad = nsolve = 0
    trials = 200
    for _ in range(trials):
        U = U0.col_join(sp.Matrix([[F(rng.randrange(-2, 3)), F(rng.randrange(-2, 3))] for _ in range(2)]))
        G = G0.col_join(sp.Matrix([[F(rng.randrange(-2, 3)), F(rng.randrange(-2, 3))] for _ in range(2)]))
        H, HA = U * V, G * V
        rows, rhs = [], []
        for j in range(NK.cols):
            for i in range(2):
                row = [F(0)] * (2 * n)
                for t in range(n):
                    row[i * n + t] = NK[t, j]
                rows.append(row)
                rhs.append(H[i + 1, j])
        ANK = A * NK
        for j in range(NK.cols):
            for i in range(2):
                row = [F(0)] * (2 * n)
                for t in range(n):
                    row[i * n + t] = ANK[t, j]
                rows.append(row)
                rhs.append(HA[i + 1, j])
        Meq, b = sp.Matrix(rows), sp.Matrix(rhs)
        if Meq.rank() != Meq.row_join(b).rank():
            nsolve += 1
            continue
        P = lam * U - G
        ms = [sp.expand(P[list(r), :].det()) for r in itertools.combinations(range(3), 2)]
        g = None
        for m in ms:
            if sp.simplify(m) != 0:
                g = m if g is None else sp.gcd(g, m)
        ok = (g is not None and sp.degree(g, lam) == 0)
        ngood += 1 if ok else 0
        nbad += 0 if ok else 1
    print(f'{trials} 次构造：线性系统不可解 {nsolve}；**好 {ngood}**；坏 {nbad}')
    print('⟹ 好 > 0 ⟹ 该层存在可行点（自由区域）；好 = 0 ⟹ 全坏（坏分量）')


if __name__ == '__main__':
    main()
