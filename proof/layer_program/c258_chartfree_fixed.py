r"""chart-free 编码（修正版）：显式列构造 + 正确的左/右逆。

用法：python proof/layer_program/c258_chartfree_fixed.py
"""
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


def left_inv(M):
    """K: K M = I（M 列满秩）。K = (M^T M)^{-1} M^T。"""
    rows, cols = len(M), len(M[0])
    Mt = [[M[i][j] for i in range(rows)] for j in range(cols)]
    MtM = AI.mul(Mt, M)
    aug = [[MtM[i][j] for j in range(cols)] + [Mt[i][j] for j in range(rows)] for i in range(cols)]
    R, _ = AI.rref(aug)
    K = [[R[i][cols + j] for j in range(rows)] for i in range(cols)]
    return K, AI.mul(K, M)


def right_inv(Rm):
    """J: R J = I（R 行满秩）。J = R^T (R R^T)^{-1}。"""
    q = len(Rm)
    w = len(Rm[0])
    Rt = [[Rm[i][j] for i in range(q)] for j in range(w)]
    RRt = AI.mul(Rm, Rt)
    aug = [[RRt[i][j] for j in range(q)] + [Rt[i][j] for j in range(w)] for i in range(q)]
    R2, _ = AI.rref(aug)
    # 解 RRt X = Rt（X: q×w），则 J = Rt? 注意：J = R^T (RR^T)^{-1} ⟹ J 是 w×q
    X = [[R2[i][q + j] for j in range(w)] for i in range(q)]     # q×w = (RR^T)^{-1} R
    Jt = AI.mul(Rt, [[X[i][j] for i in range(q)] for j in range(w)]) if False else None
    # 直接用定义：J = R^T · (RR^T)^{-1}；Rt 是 w×q，(RR^T)^{-1} 是 q×q
    Xinv = [[R2[i][q + j] for j in range(q)] for i in range(q)]  # 前 q 列是 (RR^T)^{-1} 的右块？需仔细
    # 更稳：解 RRt Y = I_q，得 Y=(RRt)^{-1}；再 J = Rt·Y
    aug2 = [[RRt[i][j] for j in range(q)] + [Fr(1) if i == j else Fr(0) for j in range(q)]
            for i in range(q)]
    R3, _ = AI.rref(aug2)
    Y = [[R3[i][q + j] for j in range(q)] for i in range(q)]
    J = AI.mul(Rt, Y)
    return J, AI.mul(Rm, J)


def main():
    S = [unit(4), unit(5)]
    Q = [unit(2), unit(3)]
    Y = [[unit(3)[k] + unit(6)[k] for k in range(N)]]
    M = mat(S + Q + Y)                       # 8×5
    print('rank M =', AI.rank(M))
    K, KM = left_inv(M)
    print('K·M = I_5 ?', KM == [[Fr(1) if i == j else Fr(0) for j in range(5)] for i in range(5)])
    Z = mat([S[0], S[1], Y[0]])              # 8×3
    print('rank Z =', AI.rank(Z))
    # 商映射 R：核 = im Z_W；先在标准坐标里取 R 使 R Z = 0 且 R 行满秩
    # （W = ker C 的坐标以后再加；这里先在标准坐标验证 R 与 J）
    Zt = [[Z[i][j] for i in range(N)] for j in range(3)]     # 3×8
    lens = AI.nullspace(Zt)                                  # (im Z)^⊥，5 维
    Rmat = [[lens[k][i] for k in range(len(lens))] for i in range(N)]  # 8×5
    Rq = [[Rmat[i][j] for i in range(N)] for j in range(len(lens))]    # 5×8
    print('R·Z = 0 ?', AI.mul(Rq, Z) == [[Fr(0)] * 3 for _ in range(5)])
    # 取 q 行：需要 q = w - d = 6 - 3 = 3 行；在标准坐标里 W=ker C 维 6，先跳过后面的坐标细节
    print('（余下：W 坐标化 + 左逆证书，见下一轮）')


if __name__ == '__main__':
    main()
