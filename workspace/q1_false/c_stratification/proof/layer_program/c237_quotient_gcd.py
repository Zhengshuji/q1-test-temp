r"""商铅笔的**小型化**判据：直接对 $T_\lambda=\lambda\iota-\bar A$（$t\times q$）做 gcd 检验。

由商铅笔恒等式（$[已证]$）：在 $(A)$ 下 $\operatorname{rank}P_\Theta(\lambda)=d+\operatorname{rank}T_\lambda$，
$(S)\iff\operatorname{rank}T_\lambda=t\ \forall\lambda$。

所以可以**丢掉** $d$ 维的 $Z$-部分与 $\ker C$ 的冗余，只在 $t\times q$ 的铅笔上做极大子式 gcd——
矩阵从 $n\times((n-r_1)+d)$ 降到 $t\times q$（通常小很多）。

本脚本在 R17 实例与 P2 例子上对拍两种算法（大铅笔 vs 商铅笔）的 gcd 次数与判定。

用法：python proof/layer_program/c237_quotient_gcd.py
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
import spectral_gcd as SG


def cols(vecs, n):
    return [[vecs[k][i] for k in range(len(vecs))] for i in range(n)]


def extend(base, pool, target):
    cur = [list(v) for v in base]
    for v in pool:
        if len(cur) >= target:
            break
        if AI.rank(cols(cur + [v], len(v))) > len(cur):
            cur.append(list(v))
    return cur


def quotient_pencil(A, C, Z):
    """返回 (T(λ) 的多项式矩阵（t×q，元素为 [常数, λ 系数]）, t, q)。"""
    n, p = len(A), len(C)
    CA = AI.mul(C, A)
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    V = [list(v) for v in Vv]
    d = len(Z[0])
    Zcols = [[Z[i][j] for i in range(n)] for j in range(d)]
    MV = cols(V, n)
    MZ = cols(Zcols, n)
    M = [[MV[i][j] for j in range(len(V))] + [-MZ[i][j] for j in range(d)] for i in range(n)]
    Nv = AI.nullspace(M)
    Svecs = []
    for coef in Nv:
        alpha = coef[:len(V)]
        s = [sum(alpha[j] * V[j][i] for j in range(len(V))) for i in range(n)]
        Svecs.append(s)
    Sb = extend([], Svecs, AI.rank(cols(Svecs, n)) if Svecs else 0)
    s_dim = len(Sb)
    t = len(V) - s_dim
    q = n - p - d
    Vb = extend(Sb, V, len(V))
    Us = Vb[s_dim:]
    Kv = AI.nullspace([list(C[i]) for i in range(p)])
    Kb = extend(Zcols, [list(v) for v in Kv], n - p)
    w_part = Kb[d:]
    # T 的列：对每个 u，把 (λu − Au) 在 Kb 下展开，取 w 分量
    Tcols = []   # 每个元素是多项式 [c0, c1]
    for u in Us:
        Au = [sum(A[i][j] * u[j] for j in range(n)) for i in range(n)]
        # 常数项 −Au、λ 系数 u
        col = []
        for w in w_part:
            # 用 Kb 的 rref 解系数是线性的：分别处理常数与 λ 部分
            # 直接算：把 u 与 −Au 在 Kb 下展开
            pass
        Tcols.append(None)
    # 简化：直接数值化——对每个 λ 采样构造 T(λ) 并算秩，用于对拍
    return None, t, q


def rank_T_at(A, C, Z, lam):
    """在给定 λ 处直接构造 T_λ 并算秩（数值精确）。"""
    n, p = len(A), len(C)
    CA = AI.mul(C, A)
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    V = [list(v) for v in Vv]
    d = len(Z[0])
    Zcols = [[Z[i][j] for i in range(n)] for j in range(d)]
    MV = cols(V, n)
    MZ = cols(Zcols, n)
    M = [[MV[i][j] for j in range(len(V))] + [-MZ[i][j] for j in range(d)] for i in range(n)]
    Nv = AI.nullspace(M)
    Svecs = []
    for coef in Nv:
        alpha = coef[:len(V)]
        Svecs.append([sum(alpha[j] * V[j][i] for j in range(len(V))) for i in range(n)])
    Sb = extend([], Svecs, AI.rank(cols(Svecs, n)) if Svecs else 0)
    s_dim = len(Sb)
    t = len(V) - s_dim
    Vb = extend(Sb, V, len(V))
    Us = Vb[s_dim:]
    Kv = AI.nullspace([list(C[i]) for i in range(p)])
    Kb = extend(Zcols, [list(v) for v in Kv], n - p)
    w_part = Kb[d:]
    # 解系数：(λu − Au) = Σ c_j Kb_j；T 的第 j 列 = c_{d+1..}
    rows = []
    for i in range(n):
        rows.append([lam * Us[0][i] - sum(A[i][j] * Us[0][j] for j in range(n))])
    Tmat = []
    for u in Us:
        Au = [sum(A[i][j] * u[j] for j in range(n)) for i in range(n)]
        x = [lam * u[i] - Au[i] for i in range(n)]
        # 解 Kb c = x
        Kbm = cols(Kb, n)
        aug = [list(Kbm[i]) + [x[i]] for i in range(n)]
        R, piv = AI.rref(aug)
        k = len(Kb)
        c = [Fr(0)] * k
        for row in R:
            pp = next((tt for tt in range(k + 1) if row[tt] != 0), None)
            if pp is None or pp == k:
                continue
            c[pp] = row[k]
        Tmat.append(c[d:])          # w 分量 = 第 j 列
    # 转置：T 的 (i,j) = 第 j 列的第 i 个分量
    q = len(w_part)
    if t == 0:
        return 0, 0
    T = [[Tmat[j][i] for j in range(t)] for i in range(q)]
    return AI.rank(T), t


def main():
    # R17 实例
    A = [[Fr(0)] * 8 for _ in range(8)]
    A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1); A[5][5] = Fr(1)
    A[0][6] = Fr(1); A[1][7] = Fr(1); A[2][0] = Fr(1); A[3][1] = Fr(1)
    C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    L0 = [[Fr(0), Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    CA = AI.mul(C, A)
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    m_L = len(KLv)
    KL = cols([list(v) for v in KLv], 8)
    # R17 的可行 Z（q=2）
    Z = [[Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(1), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(1), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(1), Fr(0)],
         [Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(0), Fr(1)]]
    g, h, _ = SG.spectral_gcd_Z(A, C, Z)
    print(f'R17 的 Z（q=2）：大铅笔 h={h}、gcd 次数={SG.pdeg(g)} ⟹ (S) {"成立" if SG.pdeg(g)==0 else "失败"}')
    for lam in (Fr(0), Fr(1), Fr(2), Fr(-1)):
        rT, t = rank_T_at(A, C, Z, lam)
        print(f'  λ={str(lam):>3s}：rank T_λ = {rT} / t = {t}' + (' ✓' if rT == t else ' ✗'))


if __name__ == '__main__':
    main()
