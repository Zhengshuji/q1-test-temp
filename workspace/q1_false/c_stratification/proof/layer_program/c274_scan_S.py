r"""G4 可行实例搜索：在 $\\dim(H/G)=2$ 的实例上遍历所有 $S\\subseteq G$（$\\dim s=2$），
找纤维非空者，再检验谱条件。

实例：$n=8$、$p=2$、$v=4$、$h=5$、$b=3$、$\\dim(H/G)=2$。

用法：python proof/layer_program/c274_scan_S.py
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
    out = []
    for v in AI.nullspace(M):
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
    G = intersect_basis(V, H)
    print(f'v={len(V)}, h={len(H)}, w={len(W)}, b={len(G)}')
    s = 2
    m = len(H) - s
    print(f's={s}, m={m}, t={len(V)-s}')

    def imP(lam):
        cols = []
        for x in V:
            Av = [sum(Ai[i][k] * x[k] for k in range(N)) for i in range(N)]
            cols.append([Av[i] - lam * x[i] for i in range(N)])
        return cols

    def dim_I(lam, S):
        inter = intersect_basis(imP(lam) + S, H)
        return AI.rank([list(x) for x in S] + inter) - len(S)

    # 遍历 S ⊆ G（s=2）：S = span(g1 + a g2 + c g3, g2 + b g3)
    results = []
    for a in range(-2, 3):
        for b in range(-2, 3):
            for c in range(-2, 3):
                v1 = [G[0][i] + Fr(a) * G[1][i] + Fr(c) * G[2][i] for i in range(N)]
                v2 = [G[1][i] + Fr(b) * G[2][i] for i in range(N)]
                S = [v1, v2]
                if AI.rank(S) < 2:
                    continue
                dims = [dim_I(lam, S) for lam in [Fr(0), Fr(1), Fr(2), Fr(3)]]
                if len(set(dims)) != 1 or dims[0] != m - 1:
                    continue
                # K = H/S 的基
                HS = []
                for hv in H:
                    if AI.rank([list(x) for x in S] + HS + [hv]) == len(S) + len(HS) + 1:
                        HS.append(hv)
                    if len(HS) == m:
                        break
                # B_S = G/S
                BS = []
                for gv in G:
                    if AI.rank([list(x) for x in S] + BS + [gv]) == len(S) + len(BS) + 1:
                        BS.append(gv)
                ok = bad = afeas = 0
                for c1 in range(-2, 3):
                    for c2 in range(-2, 3):
                        for c3 in range(-2, 3):
                            if (c1, c2, c3) == (0, 0, 0):
                                continue
                            u = [Fr(c1) * HS[0][i] + Fr(c2) * HS[1][i] + Fr(c3) * HS[2][i] for i in range(N)]
                            # U ∩ B_S = 0
                            if BS and AI.rank([u] + BS) < 1 + len(BS):
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
                            afeas += 1
                            g, _, _ = SG.spectral_gcd_Z(Ai, Ci, Z)
                            if SG.pdeg(g) == 0:
                                ok += 1
                            else:
                                bad += 1
                if afeas:
                    results.append(((a, b, c), afeas, ok, bad))
    print(f'全超平面 + 纤维非空的 S 个数: {len(results)}')
    for r in results[:5]:
        print(f'  S 参数 (a,b,c)={r[0]}: (A)-可行 {r[1]}, (S) 成立 {r[2]}, 失败 {r[3]}')


if __name__ == '__main__':
    main()
