r"""对任意可行 $Z$ 自动分解出 $(S,Q,Y)$ 并跑 chart-free 编码的 7 项检查。

用法：python proof/layer_program/c264_general_check.py
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
    k = len(M[0]); m = len(B[0])
    aug = [[M[i][j] for j in range(k)] + [B[i][c] for c in range(m)] for i in range(rows)]
    R, _ = AI.rref(aug)
    return [[R[i][k + c] for c in range(m)] for i in range(k)]


def mat(cs, n):
    return [[cs[j][i] for j in range(len(cs))] for i in range(n)]


def basis_of(vecs, n, target=None):
    out = []
    for v in vecs:
        if target is not None and len(out) >= target:
            break
        if out and AI.rank([list(x) for x in out] + [list(v)]) == len(out):
            continue
        if not out:
            out.append(list(v))
        elif AI.rank([list(x) for x in out] + [list(v)]) > len(out):
            out.append(list(v))
    return out


def run(tag, N, C, A, L0, Z, verbose=True):
    CA = AI.mul(C, A)
    V = [list(v) for v in AI.nullspace([row[:] for row in (C + CA)])]
    W = [list(v) for v in AI.nullspace([row[:] for row in C])]
    v, w = len(V), len(W)
    d = len(Z[0])
    # S = V ∩ Z：解 [V | -Z] 的零空间
    Vm = mat(V, N)
    both = [[Vm[i][j] for j in range(v)] + [-Z[i][j] for j in range(d)] for i in range(N)]
    Nv = AI.nullspace(both)
    Scols = []
    for coef in Nv:
        al = coef[:v]
        x = [sum(al[j] * V[j][i] for j in range(v)) for i in range(N)]
        Scols.append(x)
    S_ = basis_of(Scols, N)
    s = len(S_)
    r = d - s
    t = v - s
    q = w - d
    S = mat(S_, N) if s else [[Fr(0)] for _ in range(N)]
    Q_ = basis_of([x for x in V if x not in S_], N, t)
    Y_ = []
    for j in range(d):
        col = [Z[i][j] for i in range(N)]
        if AI.rank([list(x) for x in S_] + Y_ + [col]) > s + len(Y_):
            Y_.append(col)
    Y = mat(Y_, N)
    Q = mat(Q_, N)
    if verbose:
        print(f'{tag}: v={v}, w={w}, d={d}, s={s}, r={r}, t={t}, q={q}')
    g, h, _c = SG.spectral_gcd_Z(A, C, Z)
    ok = {'(S)': SG.pdeg(g) == 0}
    M = [[S[i][j] for j in range(s)] + [Q[i][j] for j in range(t)] + [Y[i][j] for j in range(r)]
         for i in range(N)]
    ok['rank M'] = AI.rank(M) == s + t + r
    K = solve(M, [[Fr(1) if i == j else Fr(0) for j in range(N)] for i in range(N)], N)
    ok['K·M=I'] = AI.mul(K, M) == [[Fr(1) if i == j else Fr(0) for j in range(s + t + r)]
                                  for i in range(s + t + r)]
    AS = AI.mul(A, S)
    G = solve(Z, AS, N)
    ok['A(S)=ZG'] = AI.mul(Z, G) == AS
    Wm = mat(W, N)
    ZW = solve(Wm, Z, N)
    QW = solve(Wm, Q, N)
    AQW = solve(Wm, AI.mul(A, Q), N)
    ZWt = [[ZW[i][j] for i in range(w)] for j in range(d)]
    lens = AI.nullspace(ZWt)
    ok['dim ker=q'] = len(lens) == q
    Rm = [[lens[k][i] for k in range(q)] for i in range(w)]
    R = [[Rm[i][j] for i in range(w)] for j in range(q)]
    ok['R·ZW=0'] = AI.mul(R, ZW) == [[Fr(0)] * d for _ in range(q)]
    RRt = [[sum(R[i][k] * R[j][k] for k in range(w)) for j in range(q)] for i in range(q)]
    Yj = solve(RRt, [[Fr(1) if i == j else Fr(0) for j in range(q)] for i in range(q)], q)
    Rt = [[R[i][j] for i in range(q)] for j in range(w)]
    J = AI.mul(Rt, Yj)
    ok['R·J=I'] = AI.mul(R, J) == [[Fr(1) if i == j else Fr(0) for j in range(q)] for i in range(q)]
    RQW = AI.mul(R, QW)
    ok['rank(RQ_W)=t'] = AI.rank(RQW) == t
    # 左逆证书：X(λ)=Σ_{k<t} λ^k X_k，X(λ)P(λ)=I_t，P(λ)=λRQW − RAQW
    RAQW = AI.mul(R, AQW)
    nv = t * t * q
    def vid(k, i, j):
        return k * t * q + i * q + j
    rows_eq, rhs = [], []
    for j in range(t + 1):
        for i in range(t):
            for c in range(t):
                co = [Fr(0)] * nv
                if j - 1 >= 0:
                    for rr in range(q):
                        co[vid(j - 1, i, rr)] += RQW[rr][c]
                if j < t:
                    for rr in range(q):
                        co[vid(j, i, rr)] -= RAQW[rr][c]
                rows_eq.append(co)
                rhs.append(Fr(1) if (j == 0 and i == c) else Fr(0))
    aug = [rows_eq[i][:] + [rhs[i]] for i in range(len(rows_eq))]
    Rr, _ = AI.rref(aug)
    sol = [Fr(0)] * nv
    bad = False
    for row in Rr:
        p2 = next((tt for tt in range(nv + 1) if row[tt] != 0), None)
        if p2 is None:
            continue
        if p2 == nv:
            bad = True
            break
        sol[p2] = row[nv]
    ok['左逆系统可解'] = not bad
    if not bad:
        good = True
        for lam in (Fr(0), Fr(1), Fr(2), Fr(-1)):
            P = [[lam * RQW[r][c] - RAQW[r][c] for c in range(t)] for r in range(q)]
            Xl = [[sum((lam ** k) * sol[vid(k, i, rr)] for k in range(t)) for rr in range(q)]
                  for i in range(t)]
            prod = [[sum(Xl[i][rr] * P[rr][c] for rr in range(q)) for c in range(t)]
                    for i in range(t)]
            if prod != [[Fr(1) if i == c else Fr(0) for c in range(t)] for i in range(t)]:
                good = False
        ok['X(λ)P(λ)=I'] = good
    if verbose:
        for k2, vv in ok.items():
            print(f'   {k2}: {"✓" if vv else "✗"}')
    return ok


def main():
    N = 6
    C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    A = [[Fr(0)] * N for _ in range(N)]
    A[0][5] = Fr(1); A[5][1] = Fr(1)
    for i in (2, 3, 4):
        A[i][i] = Fr(1)
    L0 = [[Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
    CA = AI.mul(C, A)
    KLv = AI.nullspace([row[:] for row in (C + L0)])
    KL = mat([list(x) for x in KLv], N)
    m = len(KLv)
    d = 3
    # 命中点：drop=0，自由行 1,2,3 的系数
    th = [[Fr(-2), Fr(-2), Fr(-2)], [Fr(-2), Fr(-2), Fr(-1)], [Fr(0), Fr(0), Fr(0)]]
    W = [[Fr(0)] * d for _ in range(m)]
    for j in range(d):
        W[j][j] = Fr(1)
    for a, i in enumerate([1, 2, 3]):
        for b in range(d):
            W[i][b] = th[a][b]
    Z = AI.mul(KL, W)
    print('rank Z =', AI.rank(Z), '（应', d, '）')
    ok = run('第二实例·终端阶·搜索到的点', N, C, A, L0, Z)


if __name__ == '__main__':
    main()
