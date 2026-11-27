r"""用有限域点计数估计 $(A)$-轨迹在 chart 内的维数（R17 实例、$q=3$、$d=3$）。

chart：$Z=K_LW$，$W$ 的前 3 行取单位矩阵、后 2 行是 6 个自由参数 $(a,b,c,d,e,f)$，
即 $Z$ 的列为 $e_4+a e_7+d e_8$、$e_5+b e_7+e e_8$、$e_6+c e_7+f e_8$。
$(A)$：$A(\operatorname{im}Z\cap\ker CA)\subseteq\operatorname{im}Z$。

在 $\mathbb F_p$ 上枚举 $(a,\dots,f)\in\mathbb F_p^6$，统计 $(A)$ 成立的点数；
若点数 $\sim p^1$ 则轨迹是 1 维，$\sim$ 常数则 0 维。

用法：python proof/layer_program/c249_finite_field.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI

N = 8


def rank_mod(M, p):
    """模 p 的秩（用 Fraction 表示整数，最后取模）。"""
    A = [[x % p for x in row] for row in M]
    rows = len(A)
    cols = len(A[0]) if rows else 0
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i][c] % p:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], p - 2, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] % p:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % p for j in range(cols)]
        r += 1
    return r


def main():
    # R17 的 A（整数矩阵）
    Ai = [[0] * N for _ in range(N)]
    Ai[6][2] = 1; Ai[7][3] = 1; Ai[4][4] = 1; Ai[5][5] = 1
    Ai[0][6] = 1; Ai[1][7] = 1; Ai[2][0] = 1; Ai[3][1] = 1
    # K_L = span(e4..e8)
    KLcols = [[0] * N for _ in range(5)]
    for j in range(5):
        KLcols[j][3 + j] = 1
    # CA = [e7; e8] → ker CA = span(e1..e6)
    for p in (3, 5, 7):
        cnt = 0
        tested = 0
        byr = {}
        for a, b, c, d, e, f in itertools.product(range(p), repeat=6):
            # W: 5x3，前 3 行单位，后 2 行自由
            W = [[0, 0, 0] for _ in range(5)]
            for j in range(3):
                W[j][j] = 1
            W[3] = [a, b, c]
            W[4] = [d, e, f]
            Z = [[sum(W[k][j] * KLcols[k][i] for k in range(5)) % p for j in range(3)]
                 for i in range(N)]
            if rank_mod(Z, p) < 3:
                continue
            tested += 1
            # K' = im Z ∩ span(e4,e5,e6)：解 Zα = 组合 of e4,e5,e6
            # 等价于 Zα 的 e7,e8 分量为 0：解 2x3 系统
            rows = [[Z[i][j] for j in range(3)] for i in (6, 7)]
            kv = None
            # 求 {α : rows·α = 0}
            # 手写小核
            sols = []
            for alpha in itertools.product(range(p), repeat=3):
                ok = all(sum(rows[t][j] * alpha[j] for j in range(3)) % p == 0 for t in range(2))
                if ok:
                    sols.append(alpha)
            # K' 的基 = Z·sols
            Kp = [[sum(Z[i][j] * al[j] for j in range(3)) % p for al in sols] for i in range(N)]
            # A K'
            AKp = [[sum(Ai[i][k] * Kp[k][t] for k in range(N)) % p for t in range(len(sols))]
                   for i in range(N)]
            # (A) ⟺ rank[Z | AKp] = 3（AKp 的像 ⊆ im Z）
            M = [[Z[i][j] for j in range(3)] + ([AKp[i][t] for t in range(len(sols))] if sols else [])
                 for i in range(N)]
            r = rank_mod(M, p)
            if r == 3:
                cnt += 1
                rr = rank_mod([[Z[i][j] for j in range(3)] for i in (6, 7)], p)
                byr[rr] = byr.get(rr, 0) + 1
        print(f'p={p}: 总参数点 {p**6}、非退化 {tested}、(A) 成立 {cnt}，按 r=rank(CAZ): {byr}')


if __name__ == '__main__':
    main()
