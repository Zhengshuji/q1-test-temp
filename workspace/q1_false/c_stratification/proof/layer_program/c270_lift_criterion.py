r"""G4 检验：全超平面实例上，比较
(a) 判据「存在 $u$ 使 $f_\lambda(u)\ne0\ \forall\lambda$」（即 $u\notin\bigcup_\lambda I_\lambda$），与
(b) 暴力枚举 $U$ 并做精确 $(S)$ 检验。

实例（$N=5,p=1,v=3,h=3,b=2,s=1,m=2,r=1$，全超平面区）。

$I_\lambda=((\operatorname{im}P(\lambda)+S)\cap H)/S$（模律，$S\subseteq H$）。

用法：python proof/layer_program/c270_lift_criterion.py
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

N = 5
A = [[1, -1, -1, -2, -1], [-2, 0, -1, 1, -1], [2, -2, 1, 1, 0],
     [1, 2, -2, 2, -1], [-1, 0, -2, 0, 1]]
C = [[0, 1, -2, 2, 0]]
L0 = [[-2, 2, 2, 0, -2]]


def F(M):
    return [[Fr(x) for x in r] for r in M]


def intersect_basis(cols1, cols2):
    """span(cols1) ∩ span(cols2) 的基。"""
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


def main():
    Ai, Ci, L0i = F(A), F(C), F(L0)
    CA = AI.mul(Ci, Ai)
    V = AI.nullspace([r[:] for r in (Ci + CA)])
    H = AI.nullspace([r[:] for r in (Ci + L0i)])
    Vm = [[V[k][i] for k in range(len(V))] for i in range(N)]
    Hm = [[H[k][i] for k in range(len(H))] for i in range(N)]
    b = len(V) + len(H) - AI.rank([list(Vm[i]) + list(Hm[i]) for i in range(N)])
    G = []
    for j in range(N):
        c = [Fr(1) if k == j else Fr(0) for k in range(N)]
        if AI.rank([list(x) for x in Vm] + [c]) == len(V) and \
           AI.rank([list(x) for x in Hm] + [c]) == len(H):
            G.append(c)
    s = b - 1
    S = G[:s]
    m = len(H) - s
    print(f'v={len(V)}, h={len(H)}, b={b}, s={s}, m={m}; S 的基 = {[[str(x) for x in v] for v in S]}')

    def imP(lam):
        cols = []
        for x in V:
            Av = [sum(Ai[i][k] * x[k] for k in range(N)) for i in range(N)]
            cols.append([Av[i] - lam * x[i] for i in range(N)])
        return cols

    def I_in_HS(lam):
        inter = intersect_basis(imP(lam) + S, H)
        basis = []
        for w in inter:
            cand = basis + [w]
            if AI.rank([list(x) for x in S] + cand) > len(S) + len(basis):
                basis.append(w)
        return basis

    print('\n各 lam 下 I_lam 的维数（应恒 = m-1 = %d）:' % (m - 1))
    for lam in [Fr(0), Fr(1), Fr(2), Fr(3)]:
        bI = I_in_HS(lam)
        print(f'  lam={lam}: dim = {len(bI)}')

    print('\n暴力枚举 U 并检验 (S)：')
    HS = []
    for j in range(N):
        c = [Fr(1) if k == j else Fr(0) for k in range(N)]
        if AI.rank([list(x) for x in S] + HS + [c]) == len(S) + len(HS) + 1 and \
           AI.rank([list(x) for x in Hm] + [c]) == len(H):
            HS.append(c)
        if len(HS) == m:
            break
    ok = 0
    bad = 0
    for a in range(-3, 4):
        for b2 in range(-3, 4):
            if (a, b2) == (0, 0):
                continue
            u = [Fr(a) * HS[0][i] + Fr(b2) * HS[1][i] for i in range(N)]
            Z = [[S[t][k] for t in range(s)] + [u[k]] for k in range(N)]
            if AI.rank(Z) < len(Z[0]):
                continue
            CAZ = AI.mul(CA, Z)
            Rv = AI.nullspace(CAZ)
            Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(len(Z[0]))]
            AZ = SG.apply_col(Ai, Z)
            AZR = AI.mul(AZ, Rm)
            M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
            if AI.rank(M1) != len(Z[0]):
                continue
            g, _, _ = SG.spectral_gcd_Z(Ai, Ci, Z)
            if SG.pdeg(g) == 0:
                ok += 1
            else:
                bad += 1
    print(f'  (A)-可行且 (S) 成立: {ok};  (A)-可行但 (S) 失败: {bad}')


if __name__ == '__main__':
    main()
