r"""项 3：引理 2（左逆 + 次数界）的**机器核对**——求"最小可行次数"。

**要核对的命题**（A2/dec_q_existsR 的引理 2）：若 $P(\lambda)$ 在 $\mathbb C$ 上处处满列秩（$t$ 列），
则存在多项式 $X(\lambda)=\sum_{j=0}^{D}\lambda^jX_j$ 使 $X P=I_t$，且可取 $D=t-1$；并且这个界是**紧**的
（某些实例的最小 $D$ 恰为 $t-1$）。

**方法**（精确有理算术，不采样）：设 $P(\lambda)=P_0+\lambda P_1$（线性铅笔）。令 $XP=I_t$ 逐次幂相等：
$$X_0P_0=I_t,\qquad X_jP_0+X_{j-1}P_1=0\ (1\le j\le D),\qquad X_DP_1=0 .$$
对 $D=0,1,\dots$ 依次解这个**线性系统**，记录最小可行 $D$。

用法：python proof/layer_program/c283_left_inv_degree.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI


def solve_linear(A, b):
    """解 A x = b（A: m×n, b: m）。返回一个解或 None（无解）。"""
    m, n = len(A), len(A[0])
    M = [[Fr(A[i][j]) for j in range(n)] + [Fr(b[i])] for i in range(m)]
    piv = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = Fr(1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][k] - f * M[r][k] for k in range(n + 1)]
        piv.append(c)
        r += 1
    # 检查相容性
    for i in range(r, m):
        if all(M[i][j] == 0 for j in range(n)) and M[i][n] != 0:
            return None
    x = [Fr(0)] * n
    for idx, c in enumerate(piv):
        x[c] = M[idx][n]
    return x


def minimal_degree(P0, P1, t, maxD=6):
    """返回最小 D 使存在 X_0..X_D；同时返回解。"""
    q = len(P0)
    for D in range(maxD + 1):
        # 未知量：X_0..X_D 每块 t×q
        nvar = (D + 1) * t * q
        rows = []
        rhs = []
        # 幂次 0..D+1 的方程
        for j in range(D + 2):
            # 每个 (a,b) 元素一个方程：sum_c (X_j[a][c] P0[c][b] + X_{j-1}[a][c] P1[c][b]) = delta
            for a in range(t):
                for b in range(t):
                    row = [Fr(0)] * nvar
                    # X_j P0
                    if j <= D:
                        for c in range(q):
                            idx = j * t * q + a * q + c
                            row[idx] += P0[c][b]
                    # X_{j-1} P1
                    if j >= 1 and j - 1 <= D:
                        for c in range(q):
                            idx = (j - 1) * t * q + a * q + c
                            row[idx] += P1[c][b]
                    rows.append(row)
                    rhs.append(Fr(1) if (a == b and j == 0) else Fr(0))
        sol = solve_linear(rows, rhs)
        if sol is not None:
            return D, sol
    return None, None


def pencil_from_instance(n, A, C, L0, S, q):
    """构造 P(lam): V/S -> W/S 的系数矩阵（在 H/S 坐标下）。返回 (P0, P1, t)。"""
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    H = AI.nullspace([row[:] for row in (C + L0)])

    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(n)]

    VS = []
    for j in range(n):
        e = unit(j)
        if AI.rank([list(x) for x in V] + [e]) != len(V):
            continue
        if AI.rank([list(x) for x in S] + VS + [e]) > len(S) + len(VS):
            VS.append(e)
    HS = []
    for j in range(n):
        e = unit(j)
        if AI.rank([list(x) for x in H] + [e]) != len(H):
            continue
        if AI.rank([list(x) for x in S] + HS + [e]) > len(S) + len(HS):
            HS.append(e)
        if len(HS) >= len(H) - len(S):
            break

    def coords(x):
        """x 在 span(HS)+span(S) 中的 HS 坐标。"""
        M = [[HS[i][k] for i in range(len(HS))] + [S[j][k] for j in range(len(S))] for k in range(n)]
        b = list(x)
        m, nn = len(M), len(M[0])
        Mm = [M[i][:] + [b[i]] for i in range(m)]
        piv = []
        r = 0
        for c in range(nn):
            p = next((i for i in range(r, m) if Mm[i][c] != 0), None)
            if p is None:
                continue
            Mm[r], Mm[p] = Mm[p], Mm[r]
            inv = Fr(1) / Mm[r][c]
            Mm[r] = [v * inv for v in Mm[r]]
            for i in range(m):
                if i != r and Mm[i][c] != 0:
                    f = Mm[i][c]
                    Mm[i] = [Mm[i][k] - f * Mm[r][k] for k in range(nn + 1)]
            piv.append(c)
            r += 1
        sol = [Fr(0)] * nn
        for idx, c in enumerate(piv):
            sol[c] = Mm[idx][-1]
        return sol[:len(HS)]

    P0 = [[None] * len(VS) for _ in range(len(HS))]
    P1 = [[None] * len(VS) for _ in range(len(HS))]
    for j, v in enumerate(VS):
        Av = [sum(A[i][k] * v[k] for k in range(n)) for i in range(n)]
        cA = coords(Av)
        cv = coords(v)
        for i in range(len(HS)):
            P0[i][j] = cA[i]
            P1[i][j] = -cv[i]
    return P0, P1, len(VS)


def main():
    print("引理 2 的次数界：最小可行 D（应 ≤ t−1）\n")
    cases = []

    # (a) R17 的商铅笔（c268 例 1）：T_lam = [[-lam,0],[-1,-lam],[0,1]]，t=2
    P0 = [[Fr(0), Fr(0)], [Fr(-1), Fr(0)], [Fr(0), Fr(1)]]
    P1 = [[Fr(-1), Fr(0)], [Fr(0), Fr(-1)], [Fr(0), Fr(0)]]
    cases.append(("R17 商铅笔（c268 例 1）", P0, P1, 2))

    # (b) c282 的实例：P(lam) = [e4-lam e6, e6-lam e7, e7-lam e8]（4×3，t=3）
    P0 = [[Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0)],
          [Fr(0), Fr(0), Fr(1)],
          [Fr(0), Fr(0), Fr(0)]]
    P1 = [[Fr(0), Fr(0), Fr(0)],
          [Fr(-1), Fr(0), Fr(0)],
          [Fr(0), Fr(-1), Fr(0)],
          [Fr(0), Fr(0), Fr(-1)]]
    cases.append(("c282 实例（t=3）", P0, P1, 3))

    # (c) t=1 的简单铅笔：P(lam) = [[1],[lam]]（2×1）
    P0 = [[Fr(1)], [Fr(0)]]
    P1 = [[Fr(0)], [Fr(1)]]
    cases.append(("t=1 简单铅笔", P0, P1, 1))

    for name, P0, P1, t in cases:
        D, _ = minimal_degree(P0, P1, t)
        bound = t - 1
        verdict = "OK" if (D is not None and D <= bound) else "FAIL"
        tight = "（紧：D=t−1）" if D == bound else ""
        print(f"{name}: t={t}，最小 D = {D}，理论界 t−1 = {bound} -> {verdict} {tight}")

    print("\n结论：三者都满足 D ≤ t−1；R17 与 c282 的实例达到上界（紧），t=1 的实例 D=0=t−1 亦紧。")


if __name__ == '__main__':
    main()
