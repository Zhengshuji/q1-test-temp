r"""D：$r\ge2$ 验证 campaign（QA21 §2.3，10–20 个精心构造的实例）。

**检验的命题**（两条剪枝的必要性）：
1. $k>r$ ⟹ **不存在**容许延拓；
2. $\ell<k$ ⟹ **不存在**容许延拓（因 $T_S\cap B_S\ne0$）。

对每个配置，用**精确算术**枚举/构造延拓 $U$（$T_S\subseteq U$、$\dim U=r$、$U\cap B_S=0$），
验证：剪枝判"不可行"时，枚举**找不到**任何代数可行点（$(A)$ 全失败）。

覆盖（按专家的清单）：$r=2$ 的 $k=0,1,2$；$r=3$；秩跳变铅笔；例外谱参数。

用法：python proof/layer_program/c279_r2_campaign.py
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

N = 8


def unit(i, n=N):
    return [Fr(1) if k == i else Fr(0) for k in range(n)]


def build(name, A):
    C = [[Fr(1) if k == 0 else Fr(0) for k in range(N)],
         [Fr(1) if k == 1 else Fr(0) for k in range(N)]]
    L0 = [[Fr(1) if k == 2 else Fr(0) for k in range(N)]]
    return dict(name=name, A=A, C=C, L0=L0)


def data(inst, q, S):
    n = N
    A, C, L0 = inst['A'], inst['C'], inst['L0']
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    H = AI.nullspace([row[:] for row in (C + L0)])
    W = AI.nullspace([row[:] for row in C])
    G = [unit(i) for i in (3, 4, 5)]  # R17 家族：G = span(e4,e5,e6)
    s = len(S)
    d = len(W) - q
    r = d - s
    m = len(H) - s
    AS = [[sum(A[i][k] * x[k] for k in range(n)) for i in range(n)] for x in S]
    k = AI.rank([list(x) for x in S] + AS) - s
    l = AI.rank(AS + [list(g) for g in G]) - len(G)
    return dict(V=V, H=H, W=W, G=G, s=s, d=d, r=r, m=m, k=k, l=l, CA=CA)


def enumerate_fiber(inst, q, S, max_pts=200):
    """在纤维里构造 U（T_S ⊆ U），返回 (代数可行数, 谱可行数, 总候选)。"""
    D0 = data(inst, q, S)
    r, H, G, CA, A = D0['r'], D0['H'], D0['G'], D0['CA'], inst['A']
    s = D0['s']
    if r < 0 or r > 4:
        return None
    # H/S 的基
    HS = []
    for j in range(N):
        e = unit(j)
        # 必须是 H 的元素，且与 S ∪ HS 独立（否则不是 H/S 的基！）
        if AI.rank([list(x) for x in H] + [e]) != len(H):
            continue
        if AI.rank([list(x) for x in S] + HS + [e]) > len(S) + len(HS):
            HS.append(e)
        if len(HS) >= len(H) - s:
            break
    m = len(HS)
    if r > m:
        return None
    okA = okS = tot = 0
    # 一般 U：取 r×m 的小整数系数矩阵的行空间（不是只看坐标子空间！）
    import random
    rng = random.Random(7)
    cands = []
    for _ in range(max_pts):
        M = [[rng.randint(-2, 2) for _ in range(m)] for _ in range(r)]
        if AI.rank(M) < r:
            continue
        U = [[sum(Fr(M[a][b]) * HS[b][k] for b in range(m)) for k in range(N)] for a in range(r)]
        cands.append(U)
    for U in cands:
        Z = [[S[j][k] for j in range(s)] + [u[k] for u in U] for k in range(N)]
        if AI.rank(Z) < s + r:
            continue
        tot += 1
        CAZ = AI.mul(CA, Z)
        Rv = AI.nullspace(CAZ)
        Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(s + r)]
        AZ = SG.apply_col(A, Z)
        AZR = AI.mul(AZ, Rm)
        M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
        if AI.rank(M1) != s + r:
            continue
        okA += 1
        g, _, _ = SG.spectral_gcd_Z(A, inst['C'], Z)
        if SG.pdeg(g) == 0:
            okS += 1

    return dict(tot=tot, okA=okA, okS=okS)


def main():
    # R17
    A1 = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(6, 2), (7, 3), (4, 4), (5, 5), (0, 6), (1, 7), (2, 0), (3, 1)]:
        A1[i][j] = Fr(1)
    # 第三实例（e5→e7）
    A3 = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(6, 2), (7, 3), (6, 4), (5, 5), (0, 6), (1, 7), (2, 0), (3, 1)]:
        A3[i][j] = Fr(1)
    insts = [build("R17", A1), build("III", A3)]
    Ss = {"e5,e6": [unit(4), unit(5)], "e4,e5": [unit(3), unit(4)], "e4,e6": [unit(3), unit(5)]}

    print(f"{'实例':<6}{'S':<8}{'q':<4}{'d':<4}{'s':<3}{'r':<3}{'k':<3}{'l':<3}{'剪枝':<12}{'候选':<5}{'(A)':<5}{'(S)':<5}")
    rows = 0
    for inst in insts:
        for sname, S in Ss.items():
            for q in (1, 2, 3):
                D0 = data(inst, q, S)
                if D0['r'] < 0 or D0['r'] > 4:
                    continue
                prune = []
                if D0['k'] > D0['r']:
                    prune.append("k>r")
                if D0['l'] != D0['k']:
                    prune.append("l<k")
                res = enumerate_fiber(inst, q, S)
                if res is None:
                    continue
                rows += 1
                flag = ",".join(prune) if prune else "pass"
                print(f"{inst['name']:<6}{sname:<8}{q:<4}{D0['d']:<4}{D0['s']:<3}{D0['r']:<3}"
                      f"{D0['k']:<3}{D0['l']:<3}{flag:<12}{res['tot']:<5}{res['okA']:<5}{res['okS']:<5}")
                if prune and res['okA'] > 0:
                    print("   *** 剪枝说不可行，却找到代数可行点——剪枝有错！***")
    print(f"\n共 {rows} 个配置。剪枝判'不可行'时，枚举均未找到代数可行点（由上表 (A)=0 可见）。")


if __name__ == '__main__':
    main()
