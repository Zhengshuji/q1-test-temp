r"""chart-free 编码：补完 $W$ 坐标化与左逆证书（在 R17、$q=3$ 上）。

用法：python proof/layer_program/c259_chartfree_full.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI

N = 8
C = [[Fr(1) if k == 0 else Fr(0) for k in range(N)],
     [Fr(1) if k == 1 else Fr(0) for k in range(N)]]
A = [[Fr(0)] * N for _ in range(N)]
A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1); A[5][5] = Fr(1)
A[0][6] = Fr(1); A[1][7] = Fr(1); A[2][0] = Fr(1); A[3][1] = Fr(1)


def unit(i):
    return [Fr(1) if k == i else Fr(0) for k in range(N)]


def mat(cols_):
    return [[cols_[j][i] for j in range(len(cols_))] for i in range(N)]


def solve(M, B):
    """解 M X = B（M: n×k 列满秩，B: n×m），返回 k×m。"""
    k = len(M[0])
    m = len(B[0])
    aug = [[M[i][j] for j in range(k)] + [B[i][c] for c in range(m)] for i in range(N)]
    R, _ = AI.rref(aug)
    return [[R[i][k + c] for c in range(m)] for i in range(k)]


def main():
    Wv = AI.nullspace([row[:] for row in C])
    Wm = mat(Wv)                     # 8×6
    w = len(Wv)
    S_ = [unit(4), unit(5)]
    Q_ = [unit(2), unit(3)]
    Y_ = [[unit(3)[k] + unit(6)[k] for k in range(N)]]
    Z = mat([S_[0], S_[1], Y_[0]])   # 8×3
    Q = mat(Q_)                      # 8×2
    # W 坐标
    ZW = solve(Wm, Z)                # 6×3
    QW = solve(Wm, Q)                # 6×2
    AQ = AI.mul(A, Q)                # 8×2（AQ ⊆ W）
    AQW = solve(Wm, AQ)              # 6×2
    # R：3×6，核 = im ZW
    ZWt = [[ZW[i][j] for i in range(w)] for j in range(3)]
    lens = AI.nullspace(ZWt)         # (im ZW)^⊥，3 维
    Rm = [[lens[k][i] for k in range(3)] for i in range(w)]   # 6×3
    R = [[Rm[i][j] for i in range(w)] for j in range(3)]      # 3×6
    print('R·ZW = 0 ?', AI.mul(R, ZW) == [[Fr(0)] * 3 for _ in range(3)])
    RQW = AI.mul(R, QW)              # 3×2
    RAQW = AI.mul(R, AQW)            # 3×2
    print('rank(R Q_W) =', AI.rank(RQW), '（应 t = 2）')
    # 左逆：X(λ)=X0+λX1（t=2），X(λ)P(λ)=I_2，P(λ)=λRQW − RAQW
    # 系数：X0(−RAQW)=I；X0 RQW − X1 RAQW = 0；X1 RQW = 0
    # 未知：X0, X1（各 2×3 = 6 个，共 12）
    def vid(k, i, j):
        return k * 6 + i * 3 + j
    rows, rhs = [], []
    # X0·(−RAQW) = I_2
    for i in range(2):
        for c in range(2):
            co = [Fr(0)] * 12
            for r in range(3):
                co[vid(0, i, r)] -= RAQW[r][c]
            rows.append(co)
            rhs.append(Fr(1) if i == c else Fr(0))
    # X0·RQW − X1·RAQW = 0
    for i in range(2):
        for c in range(2):
            co = [Fr(0)] * 12
            for r in range(3):
                co[vid(0, i, r)] += RQW[r][c]
                co[vid(1, i, r)] -= RAQW[r][c]
            rows.append(co)
            rhs.append(Fr(0))
    # X1·RQW = 0
    for i in range(2):
        for c in range(2):
            co = [Fr(0)] * 12
            for r in range(3):
                co[vid(1, i, r)] += RQW[r][c]
            rows.append(co)
            rhs.append(Fr(0))
    aug = [rows[i][:] + [rhs[i]] for i in range(len(rows))]
    Rr, _ = AI.rref(aug)
    sol = [Fr(0)] * 12
    bad = False
    for row in Rr:
        p = next((t for t in range(13) if row[t] != 0), None)
        if p is None:
            continue
        if p == 12:
            bad = True
            break
        sol[p] = row[12]
    print('左逆线性系统可解 ?', not bad)
    if not bad:
        X0 = [[sol[vid(0, i, j)] for j in range(3)] for i in range(2)]
        X1 = [[sol[vid(1, i, j)] for j in range(3)] for i in range(2)]
        ok = True
        for lam in (Fr(0), Fr(1), Fr(2), Fr(-1)):
            P = [[lam * RQW[r][c] - RAQW[r][c] for c in range(2)] for r in range(3)]
            Xl = [[X0[i][r] + lam * X1[i][r] for r in range(3)] for i in range(2)]
            prod = [[sum(Xl[i][r] * P[r][c] for r in range(3)) for c in range(2)] for i in range(2)]
            if prod != [[Fr(1) if i == c else Fr(0) for c in range(2)] for i in range(2)]:
                ok = False
        print('X(λ)P(λ) = I_2 对所有测试 λ ?', ok)


if __name__ == '__main__':
    main()
