r"""A-2：$(A)$ 条件作为**独立约束**——它是 $U$ 的什么类型的条件？

对固定 $S$、$Z=S\oplus U$（$\dim Z=d$），$(A)$ 是
$$\operatorname{rank}[\,Z \mid A Z R\,]=d,\qquad R\ \text{的列张成}\ \ker(CAZ),$$
即 $A$ 把 $ZR$ 送进 $Z$。

**问题**：作为 $U\in\operatorname{Gr}(r,H/S)$ 的函数，$(A)$ 是
- 线性条件？
- 二次条件？
- 还是一片"薄集"？

**做法**（c282，$r=1$）：在 $H/S$ 的整数格点上枚举 $u$，算 $(A)$ 与 $(S)$，看
1. $(A)$-集是否是一个线性子空间（检查它对加法/数乘封闭）；
2. $(A)$ 与 $(S)$ 的联合可行集有多大。

用法：python workspace/A3_basefamily/scripts/a2_condition_A.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import coeff_of_S as CS_
import spectral_gcd as SG


def c282():
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [unit(0), unit(1)]
    L0 = [unit(2)]
    A = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(0, 2), (1, 3), (4, 4), (3, 5), (5, 6), (6, 7)]:
        A[i][j] = Fr(1)
    return A, C, L0, [unit(4)]


def cond_A(A, C, Z):
    n = len(A)
    d = len(Z[0])
    CA = AI.mul(C, A)
    CAZ = AI.mul(CA, Z)
    Rv = AI.nullspace(CAZ)
    R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZ = SG.apply_col(A, Z)
    if not R or not R[0]:
        AZR = [[Fr(0)] * d for _ in range(n)]
    else:
        AZR = AI.mul(AZ, R)
    M = [list(Z[i]) + list(AZR[i]) for i in range(n)]
    return AI.rank(M) == d


def main():
    A, C, L0, S = c282()
    st = CS_.setup(A, C, L0, 4, S)
    m, r = st['m'], st['d'] - st['s']
    wm = st['w'] - st['s']
    print(f"c282: m={m}, r={r}, s={st['s']}, d={st['d']}")
    print(f"{'u (H/S 坐标)':<20}{'(A)':<8}{'(S)':<8}联合")
    # HS[j] 是 W/S 坐标，先还原成 n 维向量
    hvecs = [[sum(st['HS'][j][k] * st['WB'][st['s'] + k][i] for k in range(wm))
              for i in range(st['n'])] for j in range(m)]

    def lift(u):
        return [sum(u[j] * hvecs[j][i] for j in range(m)) for i in range(st['n'])]

    okA_list = []
    okAS = 0
    tot = 0
    for coefs in itertools.product((-1, 0, 1), repeat=m):
        if all(c == 0 for c in coefs):
            continue
        u = [Fr(c) for c in coefs]
        # 还原到 n 维（H/S 的坐标 -> 经 rows？这里 u 直接是 H/S 的坐标，用 HS 基）
        Uvec = lift(u)
        Z = list(S) + [Uvec]
        Zmat = [[Z[j][i] for j in range(len(Z))] for i in range(st['n'])]
        a = cond_A(A, C, Zmat)
        g, h, _c = SG.spectral_gcd_Z(A, C, Zmat)
        s_ok = (SG.pdeg(g) == 0)
        tot += 1
        if a:
            okA_list.append(u)
        if a and s_ok:
            okAS += 1
            print(f"{str(coefs):<20}{str(a):<8}{str(s_ok):<8}✓")
    print(f"\n共 {tot} 个 u：$(A)$ 成立 {len(okA_list)} 个；$(A)\\wedge(S)$ 成立 {okAS} 个")
    # 线性性检验：(A)-集对加法/数乘封闭？
    if len(okA_list) >= 2:
        u1, u2 = okA_list[0], okA_list[1]
        s = [u1[i] + u2[i] for i in range(m)]
        # 再算一次
        Uvec = lift(s)
        Z = list(S) + [Uvec]
        Zmat = [[Z[j][i] for j in range(len(Z))] for i in range(st['n'])]
        print(f"线性性检验：u1+u2 满足 (A)? {cond_A(A, C, Zmat)}")
        u2s = [2 * x for x in u1]
        Uvec = lift(u2s)
        Z = list(S) + [Uvec]
        Zmat = [[Z[j][i] for j in range(len(Z))] for i in range(st['n'])]
        print(f"线性性检验：2·u1 满足 (A)? {cond_A(A, C, Zmat)}")


if __name__ == '__main__':
    main()
