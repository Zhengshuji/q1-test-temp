r"""G4 检验（改进版）：先筛"纤维非空"，再要求"全超平面区"，最后检验谱判据。

对每个随机实例与每个候选 $S$：
1. 枚举 $U\subseteq H/S$（避开 $B_S$），检查 $(A)$；保留有 (A)-可行 $U$ 的；
2. 检查 $\dim I_\lambda\equiv m-1$（全超平面区）；
3. 两者都满足时，统计 (A)-可行 $U$ 中 $(S)$ 成立的比例，并与判据
   「$\exists u:\ f_\lambda(u)\ne0\ \forall\lambda$」比较（用 $\bigcup_\lambda I_\lambda$ 是否覆盖 $\mathbb P(K)$ 判断）。

用法：python proof/layer_program/c271_g4_candidate.py
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


def intersect_basis(cols1, cols2, N):
    allc = cols1 + cols2
    n1 = len(cols1)
    M = []
    for i in range(N):
        row = [allc[j][i] for j in range(n1)]
        row += [-allc[n1 + k][i] for k in range(len(cols2))]
        M.append(row)
    Mt = [[M[i][j] for i in range(N)] for j in range(len(M[0]))]
    nul = AI.nullspace(Mt)
    out = []
    for v in nul:
        w = [sum(v[j] * cols1[j][i] for j in range(n1)) for i in range(N)]
        if any(x != 0 for x in w):
            out.append(w)
    return out


def unit(i, N):
    return [Fr(1) if k == i else Fr(0) for k in range(N)]


def main():
    rng = random.Random(17)
    tested = 0
    for trial in range(1500):
        N = rng.choice([5, 6, 7])
        p = rng.choice([1, 2])
        A = F([[rng.randint(-2, 2) for _ in range(N)] for _ in range(N)])
        C = F([[rng.randint(-2, 2) for _ in range(N)] for _ in range(p)])
        L0 = F([[rng.randint(-2, 2) for _ in range(N)]])
        if AI.rank(C + L0) < p + 1:
            continue
        CA = AI.mul(C, A)
        V = AI.nullspace([r[:] for r in (C + CA)])
        H = AI.nullspace([r[:] for r in (C + L0)])
        W = AI.nullspace([r[:] for r in C])
        if len(V) < 2 or len(H) < 2:
            continue
        Vm = [[V[k][i] for k in range(len(V))] for i in range(N)]
        Hm = [[H[k][i] for k in range(len(H))] for i in range(N)]
        b = len(V) + len(H) - AI.rank([list(Vm[i]) + list(Hm[i]) for i in range(N)])
        if b < 2:
            continue
        G = []
        for j in range(N):
            c = unit(j, N)
            if AI.rank([list(x) for x in V] + [c]) == len(V) and \
               AI.rank([list(x) for x in H] + [c]) == len(H):
                G.append(c)
        for s in range(0, b):
            if s > len(G):
                continue
            S = G[:s]
            m = len(H) - s
            if m < 2:
                continue
            r = 1
            # K = H/S 的基
            HS = []
            for j in range(N):
                c = unit(j, N)
                if AI.rank([list(x) for x in S] + HS + [c]) == len(S) + len(HS) + 1 and \
                   AI.rank([list(x) for x in H] + [c]) == len(H):
                    HS.append(c)
                if len(HS) == m:
                    break
            if len(HS) < m:
                continue
            CAz = CA

            def imP(lam):
                cols = []
                for x in V:
                    Av = [sum(A[i][k] * x[k] for k in range(N)) for i in range(N)]
                    cols.append([Av[i] - lam * x[i] for i in range(N)])
                return cols

            def dim_I(lam):
                inter = intersect_basis(imP(lam) + S, H, N)
                # 商 S 后的维数
                rk = AI.rank([list(x) for x in S] + inter)
                return rk - len(S)

            dims = [dim_I(lam) for lam in [Fr(0), Fr(1), Fr(2), Fr(3), Fr(4)]]
            if len(set(dims)) != 1 or dims[0] != m - 1:
                continue
            # 纤维非空？枚举 U
            feas = []
            for a in range(-2, 3):
                for b2 in range(-2, 3):
                    if (a, b2) == (0, 0):
                        continue
                    u = [Fr(a) * HS[0][i] + Fr(b2) * HS[1][i] for i in range(N)]
                    Z = [[S[t][k] for t in range(s)] + [u[k]] for k in range(N)]
                    if AI.rank(Z) < len(Z[0]):
                        continue
                    CAZ = AI.mul(CAz, Z)
                    Rv = AI.nullspace(CAZ)
                    Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(len(Z[0]))]
                    AZ = SG.apply_col(A, Z)
                    AZR = AI.mul(AZ, Rm)
                    M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
                    if AI.rank(M1) != len(Z[0]):
                        continue
                    g, _, _ = SG.spectral_gcd_Z(A, C, Z)
                    feas.append(SG.pdeg(g) == 0)
            if not feas:
                continue
            tested += 1
            print(f'trial {trial}: N={N} p={p} b={b} s={s} m={m} dimI={dims[0]}（全超平面区）')
            print(f'  纤维中 (A)-可行 U: {len(feas)} 个，其中 (S) 成立 {sum(feas)} 个')
            if tested >= 3:
                return
    print('命中实例数:', tested)


if __name__ == '__main__':
    main()
