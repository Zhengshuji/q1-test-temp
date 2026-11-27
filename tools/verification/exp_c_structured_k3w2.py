r"""实验 C（结构化版，修法 ①/②）：$k=3$、$\omega=2$、$k>\omega$，**构造**层上的点而非采样。

数据：$n=6$、$p=2$、$q=3$、$r=1$ ⟹ $k=6-\operatorname{rank}[C;CA]=6-3=3$。
  $C=\begin{pmatrix}e_1^{\mathsf T}\\ e_2^{\mathsf T}\end{pmatrix}$；$A$：第 1 行 $=e_3^{\mathsf T}$、第 2 行 $=0$，
  列 4,5,6 $=e_1,e_2,e_3$（故 $Ae_4=e_1,\ Ae_5=e_2,\ Ae_6=e_3$）。
  ⟹ $CA=\begin{pmatrix}e_3^{\mathsf T}\\0\end{pmatrix}$、$\operatorname{rank}[C;CA]=3$、$K=\langle e_4,e_5,e_6\rangle$（$k=3$）；
  $K\cap AK=0$（$AK=\langle e_1,e_2,e_3\rangle$）且 $A|_K$ 单射 ⟹ **自由区域**（可实现性引理适用）。

构造：$L_0=e_4^{\mathsf T}$ ⟹ $L_0N_K=(1,0,0)$、$L_0AN_K=(0,0,0)$。
取 $V=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix}$，$U$ 的第 1 行 $=(1,0)$、$G$ 的第 1 行 $=(0,0)$；其余行随机。
令 $H=UV$、$H_A=GV$（$3\times3$、秩 2），解线性系统 $RN_K=H_{2:3,:}$、$RAN_K=(H_A)_{2:3,:}$ 得 $R$，
再在 $3\times2$ 铅笔 $\lambda U-G$ 上算三个 2 阶子式的 gcd ⟹ 好/坏。
"""

import itertools
import random
import sympy as sp

F = sp.Rational
lam = sp.Symbol('lam')


def build():
    n = 6
    C = sp.zeros(2, n)
    C[0, 0] = 1
    C[1, 1] = 1
    A = sp.zeros(n, n)
    A[0, 2] = 1                      # 第 1 行 = e3^T
    A[0, 3], A[1, 4], A[2, 5] = 1, 1, 1   # 列4,5,6 = e1,e2,e3
    return A, C


def main():
    A, C = build()
    n, Ccols = 6, None
    # 检查 K 与秩
    M = C.col_join(C * A)
    NK = M.nullspace()
    NKmat = sp.Matrix.hstack(*NK)
    print('rank[C;CA] =', M.rank(), ' dim K =', NKmat.cols, '（应 3 与 3）')
    Kcols = [NKmat[:, j] for j in range(NKmat.cols)]
    AK = [(A * Kcols[j]) for j in range(len(Kcols))]
    # K ∩ AK
    X = sp.Matrix.hstack(*Kcols, *AK)
    print('dim(K+AK) =', X.rank(), '（= 6 ⟹ K ∩ AK = 0 ✓）')

    L0 = sp.zeros(1, n)
    L0[0, 3] = 1
    print('L0 N_K =', (L0 * NKmat).tolist(), ' L0 A N_K =', (L0 * A * NKmat).tolist())

    rng = random.Random(20261113)
    U0 = sp.Matrix([[1, 0]])
    G0 = sp.Matrix([[0, 0]])
    V = sp.Matrix([[1, 0, 0], [0, 1, 0]])
    ngood = nbad = nsolve_fail = 0
    trials = 300
    for _ in range(trials):
        U = U0.col_join(sp.Matrix([[F(rng.randrange(-2, 3)), F(rng.randrange(-2, 3))] for _ in range(2)]))
        G = G0.col_join(sp.Matrix([[F(rng.randrange(-2, 3)), F(rng.randrange(-2, 3))] for _ in range(2)]))
        H = U * V
        HA = G * V
        # 解 R (2x6)：R N_K = H[1:,:] 且 R A N_K = HA[1:,:]
        rows_eq, rhs = [], []
        for j in range(NKmat.cols):
            for i in range(2):
                row = [F(0)] * 12
                for t in range(n):
                    row[i * n + t] = NKmat[t, j]
                rows_eq.append(row)
                rhs.append(H[i + 1, j])
        ANK = A * NKmat
        for j in range(NKmat.cols):
            for i in range(2):
                row = [F(0)] * 12
                for t in range(n):
                    row[i * n + t] = ANK[t, j]
                rows_eq.append(row)
                rhs.append(HA[i + 1, j])
        Meq = sp.Matrix(rows_eq)
        b = sp.Matrix(rhs)
        aug = Meq.row_join(b)
        if Meq.rank() != aug.rank():
            nsolve_fail += 1
            continue
        # 谱条件：3x2 铅笔 λU-G 的三个 2 阶子式
        P = lam * U - G
        ms = [sp.expand(P[list(rows), :].det()) for rows in itertools.combinations(range(3), 2)]
        g = None
        for m in ms:
            if sp.simplify(m) != 0:
                g = m if g is None else sp.gcd(g, m)
        ok = (g is not None and sp.degree(g, lam) == 0)
        if ok:
            ngood += 1
        else:
            nbad += 1
    print(f'{trials} 次构造：线性系统不可解 {nsolve_fail}；好 {ngood}；坏 {nbad}')
    print('⟹ 若 好 > 0：该层上存在可行点；若 好 = 0：**全坏**（坏分量）')


if __name__ == '__main__':
    main()
