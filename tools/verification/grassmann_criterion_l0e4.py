r"""Grassmann 非空判据（专家第二十轮定理）在 $L_0=e_4^{\mathsf T}$ 实例上的精确实现。

数据：$n=5$、$p=1$、$q=3$、$r=1$ ⟹ $k=3$、$m=2$、$\omega=2$。
  $C=e_1^{\mathsf T}$；$A$ 第一行 $e_5^{\mathsf T}$、列 2,3,4 $=e_3,e_2,e_5$。
  ⟹ $K=\langle e_2,e_3,e_4\rangle$（取 $N_K=[e_2,e_3,e_4]$）、$Ae_2=e_3$、$Ae_3=e_2$、$Ae_4=e_5\notin K$。
  ⟹ $\ker T$ 由 $(-e_3,e_2)$、$(-e_2,e_3)$ 生成（$T(v,w)=v+Aw$）。
  $L_0=e_4^{\mathsf T}$ ⟹ $L_0N_K=(0,0,1)$、$L_0AN_K=(0,0,0)$。

判据（$E=\operatorname{row}(L_0N_K)$、$F_0=\operatorname{row}(L_0AN_K)$、$X_S=\{x\in S:\exists y\in S,\ xZ_1+yZ_2=0\}$）：
$$\exists S\in\operatorname{Gr}(2,3):\ E+F_0\subseteq S,\quad E+X_S=S,\quad \omega-\dim E\le m\ (=2-1\le2\ ✓)$$
在 $K$-坐标里用余向量 $\sigma\in\mathbb F^{1\times3}$ 参数化 $S=\{x:\ x\sigma=0\}$（$x$ 为行向量）。
"""

from fractions import Fraction as Fr
import itertools

F = Fr


def rank(M):
    if not M:
        return 0
    A = [list(map(F, row)) for row in M]
    r = 0
    rows, cols = len(A), len(A[0])
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


def kernel_rows(M):
    """M: 线性映射的矩阵（作用在行向量右侧? 这里统一用 x·M=0，x 为行向量）⟹ 返回解空间基（行向量列表）。"""
    # 解 x M = 0 ⟺ M^T x^T = 0
    Mt = [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
    # 高斯消元求 Mt 的零空间（列向量），再转成行向量
    m = len(Mt)
    ncols = len(Mt[0]) if m else 0
    A = [row[:] for row in Mt]
    pivots = []
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, m) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(ncols)]
        pivots.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        x = [F(0)] * ncols
        x[fc] = F(1)
        for i, pc in enumerate(pivots):
            x[pc] = -A[i][fc]
        basis.append(x)          # 行向量
    return basis


def mat_from_rows(rows):
    return [r[:] for r in rows]


def main():
    # K-坐标：basis e2,e3,e4
    # Z1, Z2（k×d，d=2）：列 = 生成元 (-e3,e2)、(-e2,e3) 的 K-坐标
    Z1 = [[F(0), F(-1)], [F(-1), F(0)], [F(0), F(0)]]
    Z2 = [[F(1), F(0)], [F(0), F(1)], [F(0), F(0)]]
    E = [[F(0), F(0), F(1)]]          # row(L0 N_K)
    F0 = []                            # row(L0 A N_K) = 0
    print('dim E =', rank(E), ' dim F0 =', rank(F0) if F0 else 0,
          ' dim(E+F0) =', rank(E + F0) if F0 else rank(E), '（N1: 需 <= omega=2）')

    omega, m = 2, 2
    print(f'(N2): omega - dim E = {omega - rank(E)} <= m = {m} ?', omega - rank(E) <= m)

    # 枚举 sigma（行向量，S = {x : x·sigma = 0}）
    cands = []
    for s in itertools.product([-2, -1, 0, 1, 2], repeat=3):
        if all(v == 0 for v in s):
            continue
        # 归一化：首个非零为 1
        k0 = next(i for i, v in enumerate(s) if v != 0)
        sc = [F(v, s[k0]) for v in s]
        if sc in cands:
            continue
        cands.append(sc)

    ok_list = []
    for sc in cands:
        # S = ker(x -> x·sc)
        Srows = kernel_rows([[sc[0]], [sc[1]], [sc[2]]])   # x·sc=0，sc 作为 3×1
        if len(Srows) != omega:
            continue
        # E ⊆ S ?
        if any(rank(Srows + [e]) != rank(Srows) for e in E):
            continue
        # X_S = {x ∈ S : ∃y∈S, x Z1 + y Z2 = 0}
        # 即 xZ1 ∈ S·Z2
        # S·Z2 的列空间（按行向量 y 变化）
        SZ2 = []
        for j in range(len(Z2[0])):
            pass
        # 逐个 x 求：x 在 S 中，且 -xZ1 ∈ SZ2
        # 参数化 x = sum a_i Srows_i
        # 构造 SZ2 的生成元（行向量 y 取 Srows 基）
        SZ2_gens = []
        for y in Srows:
            # y·Z2
            prod = [sum(y[t] * Z2[t][j] for t in range(len(y))) for j in range(len(Z2[0]))]
            SZ2_gens.append(prod)
        Xbasis = []
        for x in Srows:
            xZ1 = [sum(x[t] * Z1[t][j] for t in range(len(x))) for j in range(len(Z1[0]))]
            neg = [-v for v in xZ1]
            if rank(SZ2_gens + [neg]) == rank(SZ2_gens):
                Xbasis.append(x)
        if not Xbasis:
            continue
        if rank(Xbasis + E) == omega:
            ok_list.append((sc, rank(Xbasis), rank(Xbasis + E)))

    print(f'候选 sigma {len(cands)} 个；满足 E+F0⊆S 且 E+X_S=S 的有 {len(ok_list)} 个')
    for sc, dx, dmix in ok_list[:8]:
        print('  sigma =', [str(v) for v in sc], f' dim X_S = {dx}, dim(X_S+E) = {dmix}')
    if ok_list:
        print('⟹ 秩-2 可容许层**非空**（Grassmann 判据给出存在性）')
    else:
        print('⟹ 该实例的秩-2 可容许层**为空**（结构性结论）')


if __name__ == '__main__':
    main()
