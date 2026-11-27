r"""实验 C（最后一块）：**约束区域** $k=3$、$\omega=2$、$n-p<2k$。

$n=5$、$p=1$、$q=3$、$r=1$ ⟹ $k=5-2=3$、$n-p=4<6=2k$（**约束区域**）。
数据：$C=e_1^{\mathsf T}$；$A$ 第一行 $e_5^{\mathsf T}$（$CA=e_5^{\mathsf T}$）、列 2,3,4 $=e_3,e_2,e_5$。
⟹ $K=\langle e_2,e_3,e_4\rangle$；$AK=\langle e_3,e_2,e_5\rangle$；$K\cap AK=\langle e_2,e_3\rangle\ne0$ ✓ 约束。

**按 Prop 2 参数化**（不采样 $R$）：
$T(v,w)=v+Aw$，$\ker T=\{(-Aw,w):w\in\langle e_2,e_3\rangle\}$ ⟹ 可达 $(B_1,B_2)$ 满足
$$B_2e_2=B_1e_3,\qquad B_2e_3=B_1e_2$$
（因 $Ae_2=e_3$、$Ae_3=e_2$），$B_1$ 与 $B_2$ 的第 1 列自由。

$H=\begin{bmatrix}L_0N_K\\B_1\end{bmatrix}$、$H_A=\begin{bmatrix}L_0AN_K\\B_2\end{bmatrix}$（$3\times3$）；
取 $L_0=e_2^{\mathsf T}$ ⟹ $L_0N_K=(1,0,0)$、$L_0AN_K=(0,1,0)$。
判据：$\operatorname{rank}H=2$、$\ker H\subseteq\ker H_A$，以及 $2\times2$ 子式（$P=\lambda H-H_A$）的 gcd 是否为常数。
"""

import itertools
import random
import sympy as sp

F = sp.Rational
lam = sp.Symbol('lam')


def data():
    n = 5
    C = sp.zeros(1, n)
    C[0, 0] = 1
    A = sp.zeros(n, n)
    A[0, 4] = 1        # 第一行 = e5^T  ⟹ CA = e5^T
    A[2, 1] = 1        # 列 2 = e3
    A[1, 2] = 1        # 列 3 = e2
    A[4, 3] = 1        # 列 4 = e5
    return A, C


def main():
    A, C = data()
    M = C.col_join(C * A)
    NK = sp.Matrix.hstack(*M.nullspace())
    print('rank[C;CA] =', M.rank(), ' dim K =', NK.cols, '（应 2 与 3）')
    Kc = [NK[:, j] for j in range(NK.cols)]
    AK = [A * Kc[j] for j in range(len(Kc))]
    print('dim(K + AK) =', sp.Matrix.hstack(*Kc, *AK).rank(), '（< 6 ⟹ 约束区域）')
    L0 = sp.zeros(1, 5)
    L0[0, 3] = 1   # L0 = e4^T（顶部块相容）
    top_H = (L0 * NK)
    top_HA = (L0 * A * NK)
    print('L0 N_K =', top_H.tolist(), ' L0 A N_K =', top_HA.tolist())

    rng = random.Random(20261115)
    ngood = nbad = nadm = 0
    trials = 3000
    for _ in range(trials):
        # 让 rank H = 2 **按构造**：H 的第 3 行 = α*第1行 + β*第2行
        v2 = sp.Matrix([F(rng.randrange(-2, 3)) for _ in range(3)])
        al, be = F(rng.randrange(-2, 3)), F(rng.randrange(-2, 3))
        v3 = al * top_H + be * v2.T
        B1 = sp.Matrix.vstack(v2.T, v3)
        c1 = sp.Matrix([F(rng.randrange(-2, 3)), F(rng.randrange(-2, 3))])
        B2 = sp.zeros(2, 3)
        B2[:, 0] = c1
        B2[:, 1] = B1[:, 2]
        B2[:, 2] = B1[:, 1]
        H = top_H.col_join(B1)
        HA = top_HA.col_join(B2)
        if H.rank() != 2:
            continue
        if sp.Matrix.vstack(H, HA).rank() != 2:   # ker H ⊆ ker H_A
            continue
        nadm += 1
        P = lam * H - HA
        ms = [sp.expand(P[list(r), :].det()) for r in itertools.combinations(range(3), 2)]
        g = None
        for m in ms:
            if sp.simplify(m) != 0:
                g = m if g is None else sp.gcd(g, m)
        ok = (g is not None and sp.degree(g, lam) == 0)
        ngood += 1 if ok else 0
        nbad += 0 if ok else 1
    print(f'{trials} 次采样：可容许(rank H=2 且 ker 含) {nadm} → **好 {ngood} / 坏 {nbad}**')
    print('⟹ 好 > 0 ⟹ 约束区域存在可行点；好 = 0 ⟹ 约束区域全坏（硬度的靶子）')


if __name__ == '__main__':
    main()
