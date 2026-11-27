r"""第二个实例的**终端阶**（$q=n_0-p=1$）：$Z=K_L$，检查 $(A)\wedge(S)$ 与编码。

$n=6$、$p=1$、$C=e_1$、$Ae_6=e_1$、$Ae_i=e_i\ (i=2,3,4,5)$；$V=\operatorname{span}(e_2,e_3,e_4,e_5)$、
$K_L=\operatorname{span}(e_3,e_4,e_5,e_6)$、$Z=K_L$（$d=4$）、$S=\operatorname{span}(e_3,e_4,e_5)$（$s=3$）、
$Q=[e_2]$（$t=1$）、$Y=[e_6]$（$r=1$）、$q=1$。

用法：python proof/layer_program/c262_terminal.py
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


def solve(M, B, rows):
    k = len(M[0])
    m = len(B[0])
    aug = [[M[i][j] for j in range(k)] + [B[i][c] for c in range(m)] for i in range(rows)]
    R, _ = AI.rref(aug)
    return [[R[i][k + c] for c in range(m)] for i in range(k)]


def mat(cols_, n):
    return [[cols_[j][i] for j in range(len(cols_))] for i in range(n)]


def main():
    N = 6
    C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    A = [[Fr(0)] * N for _ in range(N)]
    A[0][5] = Fr(1)
    for i in (2, 3, 4):
        A[i][i] = Fr(1)
    A[5][1] = Fr(1)   # A e2 = e6（使命功能可观测）
    L0 = [[Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]

    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]

    S_ = [unit(2), unit(3)]            # e3,e4
    Q_ = [unit(1), unit(4)]            # e2,e5
    Y_ = [unit(5)]                      # e6
    s, r = len(S_), len(Y_)
    S = mat(S_, N); Q = mat(Q_, N); Y = mat(Y_, N)
    Z = [[S[i][j] for j in range(s)] + [Y[i][j] for j in range(r)] for i in range(N)]
    CA = AI.mul(C, A)
    V = [list(v) for v in AI.nullspace([row[:] for row in (C + CA)])]
    W = [list(v) for v in AI.nullspace([row[:] for row in C])]
    v, w = len(V), len(W)
    d, t, q = s + r, v - s, w - (s + r)
    print(f'n={N}, v={v}, w={w}, s={s}, r={r}, d={d}, t={t}, q={q}')
    g, h, _c = SG.spectral_gcd_Z(A, C, Z)
    print(f'(S)：h={h}、gcd={SG.pdeg(g)} ⟹ {SG.pdeg(g) == 0}')
    M = [[S[i][j] for j in range(s)] + [Q[i][j] for j in range(t)] + [Y[i][j] for j in range(r)]
         for i in range(N)]
    print('rank M =', AI.rank(M), '（应', s + t + r, '）')
    K = solve(M, [[Fr(1) if i == j else Fr(0) for j in range(N)] for i in range(N)], N)
    print('K·M = I ?', AI.mul(K, M) == [[Fr(1) if i == j else Fr(0) for j in range(s + t + r)]
                                       for i in range(s + t + r)])
    AS = AI.mul(A, S)
    G = solve(Z, AS, N)
    print('A(S) = Z·G ?', AI.mul(Z, G) == AS)
    Wm = mat(W, N)
    ZW = solve(Wm, Z, N)
    QW = solve(Wm, Q, N)
    AQW = solve(Wm, AI.mul(A, Q), N)
    ZWt = [[ZW[i][j] for i in range(w)] for j in range(d)]
    lens = AI.nullspace(ZWt)
    print('dim (im ZW)^⊥ =', len(lens), '（应 q =', q, '）')
    Rm = [[lens[k][i] for k in range(q)] for i in range(w)]
    R = [[Rm[i][j] for i in range(w)] for j in range(q)]
    print('R·ZW = 0 ?', AI.mul(R, ZW) == [[Fr(0)] * d for _ in range(q)])
    RRt = [[sum(R[i][k] * R[j][k] for k in range(w)) for j in range(q)] for i in range(q)]
    Yj = solve(RRt, [[Fr(1) if i == j else Fr(0) for j in range(q)] for i in range(q)], q)
    Rt = [[R[i][j] for i in range(q)] for j in range(w)]
    J = AI.mul(Rt, Yj)
    print('R·J = I ?', AI.mul(R, J) == [[Fr(1) if i == j else Fr(0) for j in range(q)]
                                       for i in range(q)])
    RQW = AI.mul(R, QW)
    print('rank(R Q_W) =', AI.rank(RQW), '（应 t =', t, '）')


if __name__ == '__main__':
    main()
