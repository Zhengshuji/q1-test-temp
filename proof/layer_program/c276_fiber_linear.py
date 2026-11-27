r"""G4 正向实例搜索（修正版）：$(A)\iff T_S\subseteq U$ 是**线性条件**，不应采样。

对随机实例：
1. 算 $\mathcal V,H,G,b$，取 $S\subseteq G$（$\dim s$）；
2. 算 $T_S=(A(S)+S)/S$（$\dim k$）与 $B_S=G/S$（$\dim b-s$）；
3. 纤维非空的**代数条件**：$T_S\cap B_S=0$ 且 $r-k\le (m-k)-\dim(B_S/T_S)$；
4. 取满足该条件的 $U\supseteq T_S$（构造），检验 $(S)$ 与"$\dim I_\lambda\equiv m-1$"。

用法：python proof/layer_program/c276_fiber_linear.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG


def F(M):
    return [[Fr(x) for x in r] for r in M]


def inter_basis(c1, c2, N):
    allc = c1 + c2
    n1 = len(c1)
    M = [[allc[j][i] for j in range(n1)] + [-allc[n1 + k][i] for k in range(len(c2))]
         for i in range(N)]
    out = []
    for v in AI.nullspace(M):
        w = [sum(v[j] * c1[j][i] for j in range(n1)) for i in range(N)]
        if any(x != 0 for x in w):
            if AI.rank(out + [w]) > len(out):
                out.append(w)
    return out


def main():
    rng = random.Random(41)
    hits = 0
    for trial in range(800):
        N = rng.choice([7, 8])
        p = rng.choice([2, 3])
        A = F([[rng.randint(-2, 2) for _ in range(N)] for _ in range(N)])
        C = F([[rng.randint(-2, 2) for _ in range(N)] for _ in range(p)])
        L0 = F([[rng.randint(-2, 2) for _ in range(N)]])
        if AI.rank(C + L0) < p + 1:
            continue
        CA = AI.mul(C, A)
        V = AI.nullspace([r[:] for r in (C + CA)])
        H = AI.nullspace([r[:] for r in (C + L0)])
        if len(V) < 3 or len(H) < 3:
            continue
        G = inter_basis(V, H, N)
        b = len(G)
        if b < 2:
            continue
        s = b - 1
        m = len(H) - s
        t = len(V) - s
        if m < 2 or t < m - 1 or s > b:
            continue
        S = G[:s]
        # T_S = (A(S)+S)/S 的基（在 H/S 中的像）：对每个 x∈S 算 Ax mod (S + H?) — 取 Ax 模 S
        AS = []
        for x in S:
            Ax = [sum(A[i][k] * x[k] for k in range(N)) for i in range(N)]
            AS.append(Ax)
        # T_S 在 H/S 中的基：Ax 与 S 张成的维数减去 s
        TS = []
        for Ax in AS:
            if AI.rank([list(x) for x in S] + TS + [Ax]) > len(S) + len(TS):
                TS.append(Ax)
        k = len(TS)
        # B_S = G/S
        BS = []
        for gv in G:
            if AI.rank([list(x) for x in S] + BS + [gv]) > len(S) + len(BS):
                BS.append(gv)
        bb = len(BS)
        # 纤维非空的代数条件：T_S ∩ B_S = 0（模 S）且 r-k <= (m-k)-(bb)
        r = 1
        cond = (r - k <= (m - k) - bb) and (AI.rank([list(x) for x in S] + TS + BS) == len(S) + k + bb)
        if not cond:
            continue
        # 全超平面？
        def imP(lam):
            cols = []
            for x in V:
                Av = [sum(A[i][k2] * x[k2] for k2 in range(N)) for i in range(N)]
                cols.append([Av[i] - lam * x[i] for i in range(N)])
            return cols
        def dim_I(lam):
            inter = inter_basis(imP(lam) + S, H, N)
            return AI.rank([list(x) for x in S] + inter) - len(S)
        dims = [dim_I(lam) for lam in [Fr(0), Fr(1), Fr(2)]]
        if len(set(dims)) != 1 or dims[0] != m - 1:
            continue
        hits += 1
        # k=r=1 时 U = T_S 唯一，直接在该 Z 上检验 (S)
        U = TS[0]
        Z = [[S[t2][k2] for t2 in range(s)] + [U[k2]] for k2 in range(N)]
        assert AI.rank(Z) == s + 1, 'Z 维数不对'
        CAZ = AI.mul(CA, Z)
        Rv = AI.nullspace(CAZ)
        Rm = [[Rv[j][i] for j in range(len(Rv))] for i in range(s + 1)]
        AZ = SG.apply_col(A, Z)
        AZR = AI.mul(AZ, Rm)
        M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
        okA = AI.rank(M1) == s + 1
        g, _, _ = SG.spectral_gcd_Z(A, C, Z)
        okS = SG.pdeg(g) == 0
        print(f'trial {trial}: N={N} p={p} b={b} s={s} m={m} t={t} k={k} dimI={dims[0]}'
              f' ⟹ (A)={okA}, (S)={okS}（U=T_S 唯一）')
        if hits >= 3:
            break
    print('命中:', hits)


if __name__ == '__main__':
    main()
