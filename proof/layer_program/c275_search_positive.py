r"""G4 正向实例的随机搜索：全超平面区 + 纤维非空。

对每个随机实例：
1. 算 $\mathcal V,H,G,b$；
2. 取 $s$ 使 $m=h-s\ge2$、$t=v-s\ge m-1$；
3. $S=G[:s]$，检查 $\dim I_\lambda\equiv m-1$（$\lambda=0,1,2$）；
4. 若满足，暴力枚举若干 $U$ 检查 $(A)$，并统计 $(S)$。

用法：python proof/layer_program/c275_search_positive.py
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
    out = []
    seen = []
    for v in AI.nullspace(M):
        w = [sum(v[j] * cols1[j][i] for j in range(n1)) for i in range(N)]
        if any(x != 0 for x in w):
            cand = seen + [w]
            if AI.rank(cand) > len(seen):
                seen.append(w)
    assert AI.rank(seen) == len(seen)
    return seen


def main():
    rng = random.Random(31)
    stats = {'hyper': 0, 'fiber': 0, 'both': 0, 'tested': 0}
    for trial in range(2000):
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
        W = AI.nullspace([r[:] for r in C])
        if len(V) < 3 or len(H) < 3:
            continue
        G = intersect_basis(V, H, N)
        b = len(G)
        if b < 2:
            continue
        for s in range(max(0, b - 2), b):
            m = len(H) - s
            t = len(V) - s
            if m < 2 or t < m - 1 or s > len(G):
                continue
            S = G[:s]
            def imP(lam):
                cols = []
                for x in V:
                    Av = [sum(A[i][k] * x[k] for k in range(N)) for i in range(N)]
                    cols.append([Av[i] - lam * x[i] for i in range(N)])
                return cols
            def dim_I(lam):
                inter = intersect_basis(imP(lam) + S, H, N)
                return AI.rank([list(x) for x in S] + inter) - len(S)
            dims = [dim_I(lam) for lam in [Fr(0), Fr(1), Fr(2)]]
            if len(set(dims)) != 1 or dims[0] != m - 1:
                continue
            stats['hyper'] += 1
            # K 的基
            HS = []
            for hv in H:
                if AI.rank([list(x) for x in S] + HS + [hv]) == len(S) + len(HS) + 1:
                    HS.append(hv)
                if len(HS) == m:
                    break
            if len(HS) < m:
                continue
            # 暴力若干 U（r=1）
            afeas = 0
            oks = 0
            for _ in range(40):
                co = [Fr(rng.randint(-2, 2)) for _ in range(m)]
                if all(c == 0 for c in co):
                    continue
                u = [sum(co[i] * HS[i][k] for i in range(m)) for k in range(N)]
                Z = [[S[t2][k] for t2 in range(s)] + [u[k]] for k in range(N)]
                if AI.rank(Z) < s + 1:
                    continue
                CAZ = AI.mul(CA, Z)
                Rv = AI.nullspace(CAZ)
                Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(s + 1)]
                AZ = SG.apply_col(A, Z)
                AZR = AI.mul(AZ, Rm)
                M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
                if AI.rank(M1) != s + 1:
                    continue
                afeas += 1
                g, _, _ = SG.spectral_gcd_Z(A, C, Z)
                if SG.pdeg(g) == 0:
                    oks += 1
            if afeas:
                stats['fiber'] += 1
                stats['both'] += 1
                print(f'trial {trial}: N={N} p={p} b={b} s={s} m={m} t={t} dimI={dims[0]}'
                      f' ⟹ (A)-可行 {afeas}, (S) 成立 {oks}')
                if stats['both'] >= 3:
                    print(stats)
                    return
    print(stats)


if __name__ == '__main__':
    main()
