r"""核实专家的商铅笔恒等式与 Theorem D（维数障碍）——**显式构造** $T_\lambda$。

恒等式（专家 §3.1，在 $(A)$ 下）：
$$\operatorname{rank}P_\Theta(\lambda)=d+\operatorname{rank}T_\lambda,\qquad
T_\lambda=\lambda\iota-\bar A:\ \mathcal V/S\to\ker C/Z,\quad S=\mathcal V\cap Z .$$
Theorem D：$t=\dim(\mathcal V/S)>0$ 且 $(S)$ 成立 ⟹ $q>t$；等价地 $q\le t$ ⟹ $(S)$ 失败。

构造方式：取 $\mathcal V$ 的基 $\{s_i\}\cup\{u_j\}$（$s_i$ 张成 $S$）、$\ker C$ 的基 $\{z_k\}\cup\{w_l\}$（$z_k$ 张成 $Z$，$w_l$ 是 $\ker C/Z$ 的基）。
对每个 $u_j$ 与每个 $\lambda$，把 $\lambda u_j-Au_j$ 在 $\ker C$ 的基下展开，取 $w$-分量即为 $T_\lambda$ 的第 $j$ 列。

用法：python proof/layer_program/c229_quotient_pencil.py
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


def cols_to_mat(vecs, n):
    return [[vecs[k][i] for k in range(len(vecs))] for i in range(n)]


def extend_basis(base, pool, target):
    """把 base（列向量列表）用 pool 里的向量扩充到秩 target；返回新的列向量列表。"""
    cur = [list(v) for v in base]
    for v in pool:
        if len(cur) >= target:
            break
        if AI.rank(cols_to_mat(cur + [v], len(v))) > len(cur):
            cur.append(list(v))
    return cur


def solve_coeffs(basis_vecs, x):
    """把 x 在 basis_vecs（线性无关）下展开，返回系数；basis 需张成 x 所在空间。"""
    n = len(x)
    B = cols_to_mat(basis_vecs, n)
    # 解 B c = x：用增广矩阵的 rref
    aug = [list(B[i]) + [x[i]] for i in range(n)]
    R, piv = AI.rref(aug)
    k = len(basis_vecs)
    c = [Fr(0)] * k
    for row in R:
        p = next((t for t in range(k + 1) if row[t] != 0), None)
        if p is None or p == k:
            continue
        c[p] = row[k]
    return c


def analyze(A, C, Z, lam):
    """返回 (d, t, q, rankP(λ), rankT(λ))。"""
    n, p = len(A), len(C)
    CA = AI.mul(C, A)
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    V = [list(v) for v in Vv]
    d = len(Z[0])
    # S = V ∩ Z
    Zv = [list(Z[i]) for i in range(n)]          # 行
    Zcols = [[Z[i][j] for i in range(n)] for j in range(d)]
    # 交集：nullspace of [V | -Z]（列拼接）
    MV = cols_to_mat(V, n)
    MZ = cols_to_mat(Zcols, n)
    M = [[MV[i][j] for j in range(len(V))] + [-MZ[i][j] for j in range(d)] for i in range(n)]
    Nv = AI.nullspace(M)                         # (h+d) 维向量 (α, β)：Vα = Zβ
    Svecs = []
    for coef in Nv:
        alpha = coef[:len(V)]
        s = [sum(alpha[j] * V[j][i] for j in range(len(V))) for i in range(n)]
        if AI.rank([s]) == 1:
            Svecs.append(s)
    Svecs = [v for v in Svecs if AI.rank([v]) == 1]
    # 去重为基
    Sb = extend_basis([], Svecs, AI.rank(cols_to_mat(Svecs, n)) if Svecs else 0)
    s_dim = len(Sb)
    t = len(V) - s_dim
    q = n - p - d
    # 补全 V 的基：S 的基 + t 个向量
    Vb = extend_basis(Sb, V, len(V))
    Us = Vb[s_dim:]
    # ker C 的基
    Kv = AI.nullspace([list(C[i]) for i in range(p)])
    Kb = extend_basis(Zcols, [list(v) for v in Kv], n - p)
    z_part = Kb[:d]
    w_part = Kb[d:]
    # P(λ) 的秩
    Vmat = cols_to_mat(V, n)
    AV = AI.mul(A, Vmat)
    rows = [[lam * Vmat[i][k] - AV[i][k] for k in range(len(V))] + list(Z[i]) for i in range(n)]
    rankP = AI.rank(rows)
    # T_λ 的列
    Tcols = []
    for u in Us:
        Au = [sum(A[i][j] * u[j] for j in range(n)) for i in range(n)]
        x = [lam * u[i] - Au[i] for i in range(n)]
        c = solve_coeffs(Kb, x)
        Tcols.append(c[d:])
    rankT = AI.rank(cols_to_mat(Tcols, len(Tcols[0]))) if Tcols and Tcols[0] else 0
    return d, t, q, rankP, rankT


def main():
    A = [[Fr(x) for x in r] for r in
         [[0, 1, 0, 1, 0, 0, 0, 0], [0, -1, 1, 0, 0, 0, 0, -1], [1, 0, -1, 1, 0, 0, 1, -1],
          [-1, -1, 0, -2, 0, 0, 0, 0], [0, 0, 0, 0, -2, 0, 0, 1], [0, 0, 0, 0, 0, -2, 1, 0],
          [0, 0, 0, 0, 0, -1, -2, 1], [0, 0, 0, 0, 0, 0, 1, -2]]]
    C = [[Fr(x) for x in r] for r in [[-2, -2, 2, -2, -1, 0, 1, -3], [0, 0, 1, 2, 2, 3, -1, -2]]]
    L0 = [[Fr(x) for x in r] for r in [[-2, -1, -2, -3, -1, 3, 2, 0], [1, -1, -2, 1, 0, 2, 0, 1]]]
    n, p = len(A), len(C)
    CA = AI.mul(C, A)
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    m_L = len(KLv)
    KL = cols_to_mat([list(v) for v in KLv], n)
    rng = random.Random(2)
    print(f'{"q":>3s} {"d":>3s} {"t":>3s} {"q>t":>5s} {"rankP=d+rankT ?":>18s} {"(A)":>5s} {"(S)":>5s}')
    for q in (3, 4, 5):
        d = n - p - q
        if d < 0 or d > m_L:
            continue
        for _ in range(200):
            I = tuple(sorted(rng.sample(range(m_L), d))) if d else ()
            th = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(m_L - d)] if d else []
            W = [[Fr(0)] * d for _ in range(m_L)]
            Iset = set(I)
            for a, ri in enumerate(I):
                W[ri][a] = Fr(1)
            free = [x for x in range(m_L) if x not in Iset]
            for a, ri in enumerate(free):
                for b in range(d):
                    W[ri][b] = th[a][b]
            Z = AI.mul(KL, W) if d else [[Fr(0)] for _ in range(n)]
            if d and AI.rank(Z) < d:
                continue
            CAZ = AI.mul(CA, Z) if d else [[Fr(0)]]
            Rv = AI.nullspace(CAZ) if d else []
            R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
            AZ = SG.apply_col(A, Z) if d else [[Fr(0)] for _ in range(n)]
            AZR = AI.mul(AZ, R) if d else [[] for _ in range(n)]
            M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
            okA = (AI.rank(M1) == d) if d else True
            if not okA:
                continue
            g, h, _c = SG.spectral_gcd_Z(A, C, Z)
            okS = SG.pdeg(g) == 0
            okid = True
            for lam in (Fr(0), Fr(1), Fr(2), Fr(-3), Fr(5)):
                dd, t, qq, rP, rT = analyze(A, C, Z, lam)
                if rP != dd + rT:
                    okid = False
                t_last, q_last = t, qq
            print(f'{q:3d} {d:3d} {t_last:3d} {str(q_last > t_last):>5s} {str(okid):>18s} '
                  f'{str(okA):>5s} {str(okS):>5s}')
            break


if __name__ == '__main__':
    main()
