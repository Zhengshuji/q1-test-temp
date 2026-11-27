r"""全层不可行搜索：对 $q=2$、$k=2$ 的实例逐层判定 $\omega=0,1,2$ 是否都不可行。

若三层都不可行 ⟹ 该实例在 $q=2$ **不可行** ⟹ $q_{\min}\ge3$（可证的**下界实例**）。

逐层判据：
  $\omega=0$：可容许 ⟺ 存在可达对使 $H=0$ 且 $H_A=0$ ⟺ $E=\operatorname{row}(L_0N_K)=0$ 且 $F_0=\operatorname{row}(L_0AN_K)=0$
            （Grassmann 判据在 $\omega=0$ 时 $S=0$，需 $E+F_0\subseteq0$）；
  $\omega=1$：$q=2>1$。可容许且**好** ⟺ 存在可达对使 $\operatorname{rank}H=1$、$\ker H\subseteq\ker H_A$、
            且 $\operatorname{rank}[H\ H_A]=2$（$\omega=1$ 的专家判据）；
  $\omega=2$：$q=2=\omega$ ⟹ **方阵** ⟹ 必失败（专家定理）。

数据：$n=4$、$p=1$、$C=e_1^{\mathsf T}$；$A$ 第一行 $e_4^{\mathsf T}$（$K=\langle e_2,e_3\rangle$、$k=2$）；
$L_0$ 取与 $K$ 相交非零的行；$R$ 为 $1\times4$（$m=q-r=1$）。

由于 $\omega=2$ 自动不可行，**只需判定 $\omega=1$**：用 $\omega=1$ 的判据做**精确**符号判定
（$H=uv^{\mathsf T}$、$H_A=gv^{\mathsf T}$，好 $\iff\operatorname{rank}[u\ g]=2$）。
这里对 $R\in\{-1,0,1\}^4$ 精确枚举（$4$ 维，可穷尽），逐点分类。
"""

from fractions import Fraction as Fr
import itertools

F = Fr


def rank(M):
    if not M:
        return 0
    A = [list(map(F, row)) for row in M]
    r, rows, cols = 0, len(A), len(A[0])
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c] != 0), None)
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


def mul(X, Y):
    return [[sum(X[i][t] * Y[t][j] for t in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def main():
    n, p, q, r = 4, 1, 2, 1
    C = [[F(1), F(0), F(0), F(0)]]
    A = [[F(0), F(0), F(0), F(1)],
         [F(0), F(0), F(1), F(0)],
         [F(0), F(1), F(0), F(0)],
         [F(0), F(0), F(0), F(0)]]
    M = C + mul(C, A)
    NKm = None
    # K 的基：解 [C;CA] v = 0
    Kb = []
    for v in itertools.product([-1, 0, 1], repeat=n):
        vv = [F(x) for x in v]
        if all(x == 0 for x in vv):
            continue
        if all(sum(M[i][j] * vv[j] for j in range(n)) == 0 for i in range(len(M))):
            Kb.append(vv)
    # 取线性无关的两个
    basis = []
    for v in Kb:
        if rank(basis + [v]) > len(basis):
            basis.append(v)
        if len(basis) == 2:
            break
    NK = [[basis[j][i] for j in range(2)] for i in range(n)]
    print('k =', rank(NKm if NKm else NK), '（应 2）；K 的基 =', [[str(x) for x in b] for b in basis])
    print('rank[C;CA] =', rank(M), '（应 2）')

    L0 = [[F(0), F(0), F(1), F(0)]]      # e3^T（与 K 相交非零）
    E = mul(L0, NK)
    F0 = mul(mul(L0, A), NK)
    print('E =', [[str(x) for x in r] for r in E], ' F0 =', [[str(x) for x in r] for r in F0])
    ok0 = (rank(E) == 0 and rank(F0) == 0)
    print(f'omega=0 可容许? {ok0}（需 E=F0=0）')
    print(f'omega=2 可容许? False（q=2=omega ⟹ 方阵 ⟹ 专家定理：必失败）')

    # omega=1：穷举 R
    ngood = nbad = nadm = 0
    for Rv in itertools.product([-1, 0, 1], repeat=n):
        R = [[F(x) for x in Rv]]
        L = L0 + R
        H = mul(L, NK)
        HA = mul(mul(L, A), NK)
        if rank(H) != 1:
            continue
        if rank(H + HA) != 1:          # row H_A ⊆ row H
            continue
        nadm += 1
        if rank([h + ha for h, ha in zip(H, HA)]) == 2:
            ngood += 1
        else:
            nbad += 1
    print(f'omega=1：可容许 {nadm} 个 ⟹ 好 {ngood} / 坏 {nbad}')
    feasible1 = (ngood > 0)
    print()
    print('=== 该实例逐层 ===')
    print(f'  omega=0: {"可容许" if ok0 else "不可行"}')
    print(f'  omega=1: {"可行" if feasible1 else ("不可行（全坏）" if nadm else "不可行（空）")}')
    print('  omega=2: 不可行（方阵）')
    if (not ok0) and (not feasible1):
        print('⟹ **全层不可行** ⟹ 该实例在 q=2 不可行 ⟹ q_min >= 3')
    else:
        print('⟹ 存在可行层 ⟹ q_min = 2（或其他）')


if __name__ == '__main__':
    main()
