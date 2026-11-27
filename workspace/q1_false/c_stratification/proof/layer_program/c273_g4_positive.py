r"""G4 正向验证：$n=8$、$p=2$、$r=1$、$s=2$、$m=3$、$\dim(H/G)=2$ 的实例。

判据（带 $B_S$ 约束）：可行 $\iff\exists u\in K\setminus B_S$ 使 $f_\lambda(u)\ne0\ \forall\lambda$。
对照：暴力枚举 $U$（$\dim r=1$，$U\cap B_S=0$）并做精确 $(S)$ 检验。

用法：python proof/layer_program/c273_g4_positive.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG

N = 8
A = [[0, -2, -2, 2, 0, 1, 1, 2], [0, -1, -1, 0, 1, -2, -1, 2],
     [1, -2, -2, -2, 1, 1, -2, 2], [1, 0, -2, -1, -2, 2, 0, -1],
     [2, -1, 0, 2, 0, 2, 0, 0], [2, -2, 1, -1, 1, 2, 1, -1],
     [-1, -1, 2, 0, 2, -1, 2, -2], [-2, -2, 1, -2, 2, 0, 2, 0]]
C = [[2, 0, -2, 0, 0, 2, 0, 1], [2, -1, 0, -1, -2, 2, -2, 1]]
L0 = [[-1, 0, 2, -1, 2, -2, 1, -1]]


def F(M):
    return [[Fr(x) for x in r] for r in M]


def intersect_basis(cols1, cols2):
    allc = cols1 + cols2
    n1 = len(cols1)
    M = []
    for i in range(N):
        row = [allc[j][i] for j in range(n1)]
        row += [-allc[n1 + k][i] for k in range(len(cols2))]
        M.append(row)
    Mt = [[M[i][j] for i in range(N)] for j in range(len(M[0]))]
    out = []
    for v in AI.nullspace(Mt):
        w = [sum(v[j] * cols1[j][i] for j in range(n1)) for i in range(N)]
        if any(x != 0 for x in w):
            out.append(w)
    return out


def main():
    Ai, Ci, L0i = F(A), F(C), F(L0)
    CA = AI.mul(Ci, Ai)
    V = AI.nullspace([r[:] for r in (Ci + CA)])
    H = AI.nullspace([r[:] for r in (Ci + L0i)])
    W = AI.nullspace([r[:] for r in Ci])
    Vm = [[V[k][i] for k in range(len(V))] for i in range(N)]
    Hm = [[H[k][i] for k in range(len(H))] for i in range(N)]
    b = len(V) + len(H) - AI.rank([list(Vm[i]) + list(Hm[i]) for i in range(N)])
    print(f'v={len(V)}, h={len(H)}, w={len(W)}, b={b}, dim(H/G)={len(H)-b}')
    # G = V ∩ H 的基（用交的算法，不能只试标准基）
    G = intersect_basis(V, H)
    s = 2
    S = G[:s]
    m = len(H) - s
    print(f's={s}, m={m}, t={len(V)-s}')

    def imP(lam):
        cols = []
        for x in V:
            Av = [sum(Ai[i][k] * x[k] for k in range(N)) for i in range(N)]
            cols.append([Av[i] - lam * x[i] for i in range(N)])
        return cols

    def dim_I(lam):
        inter = intersect_basis(imP(lam) + S, H)
        return AI.rank([list(x) for x in S] + inter) - len(S)

    dims = [dim_I(lam) for lam in [Fr(0), Fr(1), Fr(2), Fr(3), Fr(4)]]
    # 暴力枚举 U（dim r=1 的线 in K，避开 B_S=G/S）
    HS = []
    for hv in H:
        if AI.rank([list(x) for x in S] + HS + [hv]) == len(S) + len(HS) + 1:
            HS.append(hv)
        if len(HS) == m:
            break
    Bb = G[0]
    ok = bad = 0
    for a in range(-2, 3):
        for b2 in range(-2, 3):
            for c2 in range(-2, 3):
                if (a, b2, c2) == (0, 0, 0):
                    continue
                u = [Fr(a) * HS[0][i] + Fr(b2) * HS[1][i] + Fr(c2) * HS[2][i] for i in range(N)]
                if AI.rank([u, Bb]) < 2:
                    continue
                Z = [[S[t][k] for t in range(s)] + [u[k]] for k in range(N)]
                if AI.rank(Z) < s + 1:
                    continue
                CAZ = AI.mul(CA, Z)
                Rv = AI.nullspace(CAZ)
                Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(s + 1)]
                AZ = SG.apply_col(Ai, Z)
                AZR = AI.mul(AZ, Rm)
                M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
                if AI.rank(M1) != s + 1:
                    continue
                g, _, _ = SG.spectral_gcd_Z(Ai, Ci, Z)
                if SG.pdeg(g) == 0:
                    ok += 1
                else:
                    bad += 1
    print(f'(A)-可行 U: {ok + bad}; (S) 成立 {ok}, 失败 {bad}')
    print(f'dim I_lam = {dims}（期望恒 = m-1 = {m-1}）')


if __name__ == '__main__':
    main()
