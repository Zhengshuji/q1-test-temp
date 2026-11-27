r"""项 1：命题 3（全超平面判据）的**实例验证**。

**要检验的命题**（A2 §5）：设 $k=0$、$r=1$，且**每个** $\lambda$ 的
$I_\lambda=\operatorname{im}P(\lambda)\cap(H/S)$ 都是 $H/S$ 的**超平面**，$I_\lambda=\ker f_\lambda$，
$f_\lambda=\sum_j\lambda^j f_j$，$L=\bigcap_{j\ge1}\ker f_j$。则
$$\text{可行}\iff f_0|_L\ne0 .$$

**构造的实例**（$n=8,\ p=2,\ q=4$）：
$C=[e_1;e_2]$、$L_0=e_3$；$A$：$e_1\mapsto e_3,\ e_2\mapsto e_4,\ e_3\mapsto e_3,\ e_4\mapsto e_4,\
e_5\mapsto e_5,\ e_6\mapsto e_4,\ e_7\mapsto e_6,\ e_8\mapsto e_7$。
于是 $\mathcal V=\operatorname{span}(e_5,e_6,e_7,e_8)$（$v=4$）、$H=\operatorname{span}(e_4,\dots,e_8)$（$h=5$）、
$s=1$（$S=\operatorname{span}(e_5)$）、$r=1$、$m=4$、$t=3=m-1$。

**两条独立计算**：
(A) 判据侧：算 $f_\lambda$（$3\times3$ 子式）、$L$、$f_0|_L$；
(B) 直接侧：对每条直线 $u$，算 $q_u(\lambda)=\det[u\mid B(\lambda)]$（$B$ = $I_\lambda$ 的基），
    可行 $\iff q_u$ 是非零常数（无根）。

用法：python proof/layer_program/c282_prop3_instance.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI

N = 8


def unit(i):
    return [Fr(1) if k == i else Fr(0) for k in range(N)]


# ---- 实例 ----------------------------------------------------------------
C = [unit(0), unit(1)]                 # [e1; e2]
L0 = [unit(2)]                         # e3
A = [[Fr(0)] * N for _ in range(N)]
for (i, j) in [(0, 2), (1, 3), (4, 4), (3, 5), (5, 6), (6, 7)]:
    A[i][j] = Fr(1)   # A[i][k] = (A e_k)_i

Q = 4          # q
S = [unit(4)]  # S = span(e5)


def poly_of_matrix(entries):
    """entries: list of lists of Fractions -> 返回多项式系数列表（低次在前）。"""
    deg = max(len(e) for row in entries for e in row) - 1
    out = []
    for j in range(deg + 1):
        out.append([[e[j] if j < len(e) else Fr(0) for e in row] for row in entries])
    return out


def det(M):
    n = len(M)
    if n == 0:
        return Fr(1)
    M = [row[:] for row in M]
    d = Fr(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if M[r][i] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != i:
            M[i], M[piv] = M[piv], M[i]
            d = -d
        d *= M[i][i]
        inv = Fr(1) / M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] * inv
            for c in range(i, n):
                M[r][c] -= f * M[i][c]
    return d


def main():
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    H = AI.nullspace([row[:] for row in (C + L0)])
    W = AI.nullspace([row[:] for row in C])
    print(f"v={len(V)} h={len(H)} w={len(W)}")
    d = len(W) - Q
    s = len(S)
    r = d - s
    m = len(H) - s
    t = len(V) - s
    print(f"d={d} s={s} r={r} m={m} t={t}（命题 3 需要 r=1、m−1=t）")

    # H/S 的基（必须是 H 的元素）
    HS = []
    for j in range(N):
        e = unit(j)
        if AI.rank([list(x) for x in H] + [e]) != len(H):
            continue
        if AI.rank([list(x) for x in S] + HS + [e]) > s + len(HS):
            HS.append(e)
        if len(HS) >= m:
            break
    print("H/S 的基:", [[str(x) for x in v] for v in HS])

    # V/S 的基
    VS = []
    for j in range(N):
        e = unit(j)
        if AI.rank([list(x) for x in V] + [e]) != len(V):
            continue
        if AI.rank([list(x) for x in S] + VS + [e]) > s + len(VS):
            VS.append(e)
        if len(VS) >= t:
            break
    print("V/S 的基:", [[str(x) for x in v] for v in VS])

    # P(lam) = A - lam*I 在 V/S 上，取值在 W/S
    # W/S 的基
    WS = []
    for j in range(N):
        e = unit(j)
        if AI.rank([list(x) for x in W] + [e]) != len(W):
            continue
        if AI.rank([list(x) for x in S] + WS + [e]) > s + len(WS):
            WS.append(e)
    print("W/S 的基:", [[str(x) for x in v] for v in WS])

    # P(lam) 的列（在 W/S 坐标下），每列是 (a0 + a1 lam) 的系数对
    Pcols = []  # list of column: list over W/S coords of (c0, c1)
    for v in VS:
        Av = [sum(A[i][k] * v[k] for k in range(N)) for i in range(N)]
        col = []
        for i, e in enumerate(WS):
            # 解 Av 与 e 在 W/S 坐标：用最小二乘？这里 WS 是 W/S 的基，直接线性表出
            col.append(None)
        Pcols.append((Av, v))
    # 线性表出：Av = sum c_i e_i + (S 的部分)
    def coords_in_quotient(x, basis, sub):
        """x 在 span(basis) + span(sub) 中的坐标（对 basis）。返回系数列表。"""
        M = [[basis[i][k] for i in range(len(basis))] + [sub[j][k] for j in range(len(sub))] + [x[k]]
             for k in range(N)]
        # 解 M c = x 的最小二乘不适用；直接取 x 在 quotient 的坐标：
        # 用 Gram-Schmidt 在商空间里做
        return None

    # 简化：直接用多项式矩阵的 3x3 子式算 f（在 W/S 整体坐标里，I_lam 的基向量是 P(lam)VS）
    # f_lam 是 W/S 上的线性形式，满足 f(P(lam)v)=0 对所有 v。
    # 在 W/S 的坐标（用 WS 基）下，P(lam) 的列坐标 = 解 [WS | S] c = Av。
    def solve_coords(Av):
        """解 Av ∈ span(WS)+span(S)，返回 WS 坐标。"""
        M = [[HS[i][k] for i in range(len(HS))] + [S[j][k] for j in range(len(S))] for k in range(N)]
        rhs = list(Av)
        # 高斯消元求一个解（最小范数不需要，只要一组解）
        Mm = [row[:] + [rhs[i]] for i, row in enumerate(M)]
        rows, cols = len(Mm), len(M[0])
        piv_cols = []
        r0 = 0
        for c in range(cols):
            p = next((r for r in range(r0, rows) if Mm[r][c] != 0), None)
            if p is None:
                continue
            Mm[r0], Mm[p] = Mm[p], Mm[r0]
            inv = Fr(1) / Mm[r0][c]
            Mm[r0] = [x * inv for x in Mm[r0]]
            for r in range(rows):
                if r != r0 and Mm[r][c] != 0:
                    f = Mm[r][c]
                    Mm[r] = [Mm[r][k] - f * Mm[r0][k] for k in range(cols + 1)]
            piv_cols.append(c)
            r0 += 1
        sol = [Fr(0)] * cols
        for idx, c in enumerate(piv_cols):
            sol[c] = Mm[idx][-1]
        return sol[:len(HS)]

    # P(lam) 的第 j 列在 W/S 坐标下：坐标 = coords(Av) + lam * (-coords(v))
    cols = []
    for (Av, v) in [(None, None)] if False else []:
        pass
    for idx in range(t):
        v = VS[idx]
        Av = [sum(A[i][k] * v[k] for k in range(N)) for i in range(N)]
        cA = solve_coords(Av)
        cv = solve_coords(v)
        col = [(cA[i], -cv[i]) for i in range(m)]   # (常数项, lam 的系数)
        cols.append(col)

    # 3x3 子式 -> f 的系数（用伴随/叉积：3 列在 4 维里，f 是它们的零化形式）
    # f 的 4 个分量 = 3x3 子式（带符号）
    def minors_of(cols, lam):
        Mat = [[cols[j][i][0] + lam * cols[j][i][1] for j in range(t)] for i in range(m)]
        out = []
        for skip in range(m):
            rows = [i for i in range(m) if i != skip]
            sub = [[Mat[i][j] for j in range(t)] for i in rows]
            out.append(((-1) ** skip) * det(sub))
        return out

    # 多项式 f_lam：在 lam = 0..t 处插值（t 次以下）
    vals = [minors_of(cols, Fr(k)) for k in range(t + 1)]
    # 插值每个分量的系数
    from fractions import Fraction as F
    def interp(ys):
        # 拉格朗日插值，节点 0..t
        coeffs = [F(0)] * (t + 1)
        for i, yi in enumerate(ys):
            # 基多项式 prod_{j!=i}(x-j)/(i-j)
            num = [F(1)]
            den = F(1)
            for j in range(t + 1):
                if j == i:
                    continue
                # num *= (x - j)
                new = [F(0)] * (len(num) + 1)
                for d, c in enumerate(num):
                    new[d + 1] += c
                    new[d] -= c * j
                num = new
                den *= (F(i) - F(j))
            for d, c in enumerate(num):
                coeffs[d] += yi * c / den
        return coeffs

    fcoef = [interp([vals[k][i] for k in range(t + 1)]) for i in range(m)]
    print("\nf_lam 的分量（lam^0..lam^t 的系数）：")
    for i in range(m):
        print(f"  f_{i}:", [str(c) for c in fcoef[i]])

    # L = ∩_{j>=1} ker f_j  （f_j = fcoef[:][j]）
    forms = [[fcoef[i][j] for i in range(m)] for j in range(1, t + 1)]
    L = AI.nullspace(forms) if forms else [[Fr(1) if i == k else Fr(0) for i in range(m)] for k in range(m)]
    print("\nL = ∩_{j>=1} ker f_j 的基（H/S 坐标）:", [[str(x) for x in v] for v in L])
    f0 = [fcoef[i][0] for i in range(m)]
    val = [sum(f0[i] * u[i] for i in range(m)) for u in L]
    print("f_0|_L 的取值:", [str(x) for x in val])
    nonzero = any(x != 0 for x in val)
    print("判据（A）：f_0|_L ≠ 0 ?", nonzero)

    # (B) 直接侧：对 H/S 的直线 u（网格），算 q_u(lam)=det[u|B(lam)]
    def det_poly(u):
        """返回 q_u 的系数列表（lam^0..t）。"""
        ys = []
        for lam in range(t + 1):
            Mat = [[u[i]] + [cols[j][i][0] + lam * cols[j][i][1] for j in range(t)] for i in range(m)]
            ys.append(det(Mat))
        return interp(ys)

    feas = []
    infeas = []
    for coefs in itertools.product((-2, -1, 0, 1, 2), repeat=m):
        if all(c == 0 for c in coefs):
            continue
        u = [Fr(c) for c in coefs]
        q = det_poly(u)
        # 可行 <=> q 非零常数
        is_const = all(c == 0 for c in q[1:])
        ok = is_const and q[0] != 0
        (feas if ok else infeas).append((coefs, q))
    print(f"\n直接侧（B）：{len(feas)+len(infeas)} 条直线，可行 {len(feas)}、不可行 {len(infeas)}")
    print("可行直线的样本:", [c for c, _ in feas[:3]])
    # 与判据对照：可行 <=> u ∈ L 且 f_0(u) != 0
    def pred(coefs):
        u = [Fr(c) for c in coefs]
        return (all(sum(forms[j][i] * u[i] for i in range(m)) == 0 for j in range(len(forms)))
                and sum(f0[i] * u[i] for i in range(m)) != 0)
    mism = [c for c, _ in feas if not pred(c)] + [c for c, _ in infeas if pred(c)]
    print(f"与判据 (A) 不一致的直线数：**{len(mism)}**", "(应为 0)" if not mism else "*** 判据有误 ***")


if __name__ == '__main__':
    main()
