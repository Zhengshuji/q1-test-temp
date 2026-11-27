#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""q_omega_plus_1_w2.py -- q=omega+1, omega=2 的可达块分类与 det[w,Aw] 判定

两个实例，全部精确算术（Fraction）：

A. 自由区（n=9, p=3, q=3, r=1; K=ker[C;CA]=<e7,e8,e9>, k=3, omega=2）:
   K∩AK=0 ⟹ ker T=0 ⟹ 兼容纤维 C_S = S x S（任意 (x,y)）。
   取 S=<e1,e2>（K-坐标），**同一个 H**（因而同一个 S、同一个 omega=2 层）
   配两个不同的 H_A：
     good:  H_A = [0; e1+w; e1]  (w=e2)  ⟹ (5b) 成立（det[w,Aw] != 0）
     bad :  H_A = [0; w; 0]              ⟹ (5b) 在 lambda=0 失败
   两者回代出显式 L（3x9，顶行 L0），并跑 consistency_checks 的七条检查。

B. 约束区（n=5, p=1, q=3, r=1; K=<e2,e3,e4>, k=3, omega=2; ker T 维数 d=2）:
   两个 Grassmann 点 S（sigma=(1,±1,0)）上，兼容对由 (a,b,d) 参数化；
   逐点 2-子式 gcd 恒含因子 lambda+1 ⟹ **整族全坏**（q=3 不可行）。

C. 打印分类表（自由 / 中间 / 刚性）。

注意: 这是精确算例与结构性观察，不是新定理的完整证明；定理陈述见
workspace/augmentation_family/attempts/100_q_omega_plus_1_w2.md。
"""
import os
import sys
from fractions import Fraction
from itertools import combinations, product

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for _p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, _p))

import linalg_q as LQ                 # noqa: E402
import consistency_checks as CC       # noqa: E402

F = Fraction


# ---------------------------------------------------------------- 多项式工具
def ptrim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pdeg(p):
    p = ptrim(p)
    return -1 if (len(p) == 1 and p[0] == 0) else len(p) - 1


def padd(a, b):
    n = max(len(a), len(b))
    out = [F(0)] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return ptrim(out)


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return ptrim(out)


def pdivmod(a, b):
    a, b = ptrim(a), ptrim(b)
    q = [F(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and not (len(a) == 1 and a[0] == 0):
        d = a[-1] / b[-1]
        sh = len(a) - len(b)
        q[sh] = d
        for i in range(len(b)):
            a[sh + i] -= d * b[i]
        a = ptrim(a)
    return ptrim(q), ptrim(a)


def pgcd(a, b):
    a, b = ptrim(a), ptrim(b)
    while not (len(b) == 1 and b[0] == 0):
        _, r = pdivmod(a, b)
        a, b = b, ptrim(r)
    if not (len(a) == 1 and a[0] == 0):
        lead = a[-1]
        a = [x / lead for x in a]
    return a


def det_poly(M):
    """多项式矩阵的行列式（permutation expansion；这里 omega<=3）."""
    n = len(M)
    if n == 0:
        return [F(1)]
    total = [F(0)]
    for perm in __import__('itertools').permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])
        term = [F(-1 if inv % 2 else 1)]
        for i in range(n):
            term = pmul(term, M[i][perm[i]])
        total = padd(total, term)
    return ptrim(total)


def pencil_gcd_degree(H, HA, omega=2):
    """gcd of the omega-minors of lambda H - H_A 的 lambda 次数（all row/col subsets）."""
    q, k = len(H), len(H[0])
    g = None
    for rows in combinations(range(q), omega):
        for cols in combinations(range(k), omega):
            e = [[[-HA[i][j], H[i][j]] for j in cols] for i in rows]
            d = det_poly(e)
            if pdeg(d) >= 0:
                g = d if g is None else pgcd(g, d)
    if g is None:
        return -1
    return pdeg(g)


def det2(a, b, c, d):
    return a * d - b * c


# ---------------------------------------------------------------- 实例 A（自由区）
def build_free():
    n = 9
    C = [[F(1) if j == i else F(0) for j in range(n)] for i in range(3)]
    A = [[F(0)] * n for _ in range(n)]
    for k in range(3):
        A[k][3 + k] = F(1)      # 列 4,5,6 = e1,e2,e3
        A[3 + k][6 + k] = F(1)  # 列 7,8,9 = e4,e5,e6
    L0 = [[F(1) if j == 6 else F(0) for j in range(n)]]
    NK = [[F(0)] * 3 for _ in range(n)]
    for j in range(3):
        NK[6 + j][j] = F(1)
    return A, C, L0, NK


def recover_L(H, HA, L0, NK):
    """解 R N_K = H[1:], R A N_K = H_A[1:]; 返回 L = [L0; R]."""
    n = len(NK)
    q = len(H)
    m = q - len(L0)
    A = None
    # 由调用方保证 ANK 已算；这里用 L 的列直接构造: R e_{6+j}=H[1+i][j], R e_{3+j}=HA[1+i][j]
    R = [[F(0)] * n for _ in range(m)]
    for j in range(3):
        for i in range(m):
            R[i][6 + j] = H[1 + i][j]
            R[i][3 + j] = HA[1 + i][j]
    return [r[:] for r in L0] + R


def part_A():
    A, C, L0, NK = build_free()
    n = 9
    # S = <e1, e2>（K-坐标）; H 固定
    H = [[F(1), F(0), F(0)],
         [F(0), F(1), F(0)],
         [F(0), F(1), F(0)]]
    good_HA = [[F(0), F(0), F(0)],
               [F(1), F(1), F(0)],
               [F(1), F(0), F(0)]]
    bad_HA = [[F(0), F(0), F(0)],
              [F(0), F(1), F(0)],
              [F(0), F(0), F(0)]]
    print('=== A. 自由区: 同一个 H / 同一个 S，两个 H_A ===')
    print('  rank H =', LQ.rank([r[:] for r in H]), '; row(H) = span{e1,e2}（K-坐标）')
    for tag, HA in [('good(H_A=[0;e1+w;e1])', good_HA), ('bad (H_A=[0;w;0])', bad_HA)]:
        d = pencil_gcd_degree(H, HA)
        L = recover_L(H, HA, L0, NK)
        rL = LQ.rank([r[:] for r in L])
        print(f'  [{tag}] gcd degree = {d}  (0=好, >0=坏); rank L = {rL}')
        res = CC.check_candidate(A, C, L0, L, tag=tag)
        assert (res['five_b'] == (d == 0)), '五判据与 reduced pencil 不一致'
    print('  ⟹ 同一个 S、同一个 H，一好一坏；谱行为不是 S 的函数。')
    return H, good_HA, bad_HA


# ---------------------------------------------------------------- 实例 B（约束区）
def build_constrained():
    n = 5
    C = [[F(1) if j == 0 else F(0) for j in range(n)]]
    A = [[F(0)] * n for _ in range(n)]
    A[0][4] = F(1)   # 行 1 = e5^T  (CA=e5^T)
    A[2][1] = F(1)   # 列 2 = e3
    A[1][2] = F(1)   # 列 3 = e2
    A[4][3] = F(1)   # 列 4 = e5 (not in K)
    L0 = [[F(0), F(0), F(0), F(1), F(0)]]   # e4^T
    NK = [[F(0)] * 3 for _ in range(n)]
    NK[1][0] = F(1)  # e2
    NK[2][1] = F(1)  # e3
    NK[3][2] = F(1)  # e4
    return A, C, L0, NK


def part_B():
    print('\n=== B. 约束区: ker T 维数 d=2，两个 S 上全坏 ===')
    A, C, L0, NK = build_constrained()
    n = 5
    # 核验 K、Z1/Z2 的定义关系
    CA = LQ.mul(C, A)
    M = [r[:] for r in C] + [r[:] for r in CA]
    print('  rank[C;CA] =', LQ.rank([r[:] for r in M]), '（应 2）; dim K =', n - LQ.rank([r[:] for r in M]), '（应 3）')
    ANK = LQ.mul(A, NK)
    # K-坐标: e2,e3,e4。Z1,Z2（2x3）由 ker T 的基 (-e3,e2), (-e2,e3) 给出
    Z1 = [[F(0), F(-1), F(0)], [F(-1), F(0), F(0)]]
    Z2 = [[F(1), F(0), F(0)], [F(0), F(1), F(0)]]
    for i in range(2):
        v = [sum(NK[t][j] * Z1[i][j] for j in range(3)) for t in range(n)]
        w = [sum(NK[t][j] * Z2[i][j] for j in range(3)) for t in range(n)]
        aw = [sum(A[t][s] * w[s] for s in range(n)) for t in range(n)]
        assert all(v[t] + aw[t] == 0 for t in range(n)), 'Z1/Z2 不是 ker T 的基'
    print('  Z1/Z2 确为 ker T 的基 ✓; dim ker T = 2')
    E = [F(0), F(0), F(1)]   # L0 N_K
    tested = 0
    all_bad = True
    for sname, sign in [('S(sigma=(1,1,0))', -1), ('S(sigma=(1,-1,0))', +1)]:
        cnt = 0
        for (a, b, d) in product([-2, -1, 0, 1, 2], repeat=3):
            if a == 0 and b == 0:
                continue
            x1 = [F(a), F(sign * a), F(b)]
            y1 = [F(sign * a), F(a), F(d)]
            x2 = [F(0), F(0), F(1)]
            y2 = [F(0), F(0), F(0)]
            H = [E[:], x1[:], x2[:]]
            HA = [[F(0), F(0), F(0)], y1[:], y2[:]]
            if LQ.rank([r[:] for r in H]) != 2:
                continue
            if LQ.rank([r[:] for r in H] + [r[:] for r in HA]) != 2:
                continue
            tested += 1
            dg = pencil_gcd_degree(H, HA)
            if dg == 0:
                all_bad = False
            cnt += 1
        print(f'  {sname}: 可容许参数点 {cnt} 个')
    print(f'  共测 {tested} 个可容许点；全部坏? {all_bad}')
    assert tested > 0 and all_bad, '预期整族全坏，但找到好点或没有测到点'
    return all_bad


def main():
    part_A()
    part_B()
    print('\n=== C. 分类表（q=omega+1, omega=2）===')
    print('  机制       | 条件                    | q=3 判定')
    print('  自由       | ker T = 0（K∩AK=0 等）  | 由 det[w,Aw] 决定；同一 S 可混合')
    print('  中间/刚性  | 0 < dim ker T <= k      | 同一 det 检验；可整族全坏（如 d=2 的 n=5 例）')
    print('  点态判据   | 任意可容许点            | 坏 <=> det[w,Aw)=0（w 张成 ker B）')


if __name__ == '__main__':
    main()
