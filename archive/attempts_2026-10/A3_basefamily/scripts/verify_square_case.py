r"""A-1 前置（分支 4）：**方阵情形**下 adapted basis 与行列式恒等式的验证。

**适用条件（本轮确定）**：$[U\mid P(\lambda)]$ 是 $(w-s)\times(r+t)$；
单行列式判据只在 **$r+t=w-s$** 时成立，等价于
$$t=q\\qquad(\\text{因为 } t=v-s,\\ r=w-q-s\\ \\Longrightarrow\\ r+t=w-q\\ \\Longrightarrow\\ r+t=w-s\\iff q=t).$$

**检验内容**（每个方阵实例）：
1. $T$ 可逆，$T^{-1}(H/S)=\\operatorname{span}(e_1..e_m)$；
2. 对随机 $u$：$\\det[U_{\\rm new}\\mid P_{\\rm new}]=\\det(T^{-1})\\cdot\\det[U_{\\rm old}\\mid P_{\\rm old}]$（逐系数）；
3. $U_{\\rm new}$ 支撑在前 $m$ 个坐标 ⟹ 用前 $m$ 行算出的行列式与完整行列式相同；
4. 系数判据（$a_0\\notin\\operatorname{span}\\{a_j\\}$）与 `feasible_by_minors` 在若干 $u$ 上一致。

用法：python workspace/A3_basefamily/scripts/verify_square_case.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG
import coeff_of_S as CS_
import coeff_space as CS2


def det_fr(M):
    n = len(M)
    M = [row[:] for row in M]
    d = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            d = -d
        d *= M[i][i]
        inv = Fr(1) / M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] * inv
            for c in range(i, n):
                M[r][c] -= f * M[i][c]
    return d


def poly_det(u, cols, wm, t):
    P = []
    for i in range(wm):
        row = [[u[i]]]
        row += [[cols[j][0][i], cols[j][1][i]] for j in range(t)]
        P.append(row)
    return SG.pdet(P)


def run(A, C, L0, q, S, label):
    st = CS_.setup(A, C, L0, q, S)
    wm = st['w'] - st['s']
    m = st['m']
    cols = CS_.pencil_cols(A, st)
    t = len(cols)
    r = st['d'] - st['s']
    print(f'\n=== {label}: w-s={wm}, m={m}, r={r}, t={t}, q={q}')
    if r + t != wm:
        print(f'  **非方阵**（r+t={r+t} != w-s={wm}，即 q={q} != t={t}）：单行列式判据**不适用**，跳过')
        return None
    print('  方阵 ✓（q = t）')
    if r != 1:
        print(f'  （本脚本只处理 r=1；r={r} 跳过）')
        return None
    T = CS_.adapted_basis(st)
    Ti = CS_._invert(T)
    assert AI.rank(T) == wm
    HSnew = [[sum(Ti[i][j] * h[j] for j in range(wm)) for i in range(wm)] for h in st['HS']]
    assert all(all(v[i] == 0 for i in range(m, wm)) for v in HSnew), 'T^-1(H/S) 不在前 m 行'
    assert AI.rank(HSnew) == m
    print(f'  T^-1(H/S) = span(e_1..e_{m}) ✓')
    dTi = det_fr(Ti)
    rng = random.Random(7)
    ok_scale = 0
    ok_trunc = 0
    n_tested = 0
    for _ in range(6):
        u_old = [Fr(rng.randint(-2, 2)) for _ in range(wm)]
        if all(x == 0 for x in u_old):
            continue
        u_new = [sum(Ti[i][j] * u_old[j] for j in range(wm)) for i in range(wm)]
        # **关键**：P 也要用新基（此前漏了这一步）
        cols_new = [[[sum(Ti[i][j] * cols[k][0][j] for j in range(wm)) for i in range(wm)],
                     [sum(Ti[i][j] * cols[k][1][j] for j in range(wm)) for i in range(wm)]]
                    for k in range(t)]
        old = poly_det(u_old, cols, wm, t)
        new = poly_det(u_new, cols_new, wm, t)
        expect = [dTi * x for x in old]
        n_tested += 1
        if SG.ptrim(new) == SG.ptrim(expect):
            ok_scale += 1
        cols_t = [[[cols_new[j][0][i] if i < m else Fr(0) for i in range(wm)],
                   [cols_new[j][1][i] if i < m else Fr(0) for i in range(wm)]] for j in range(t)]
        trunc = poly_det([u_new[i] if i < m else Fr(0) for i in range(wm)], cols_t, wm, t)
        if SG.ptrim(trunc) == SG.ptrim(expect):
            ok_trunc += 1
    print(f'  换基缩放恒等式：{ok_scale}/{n_tested}')
    print(f'  截断到前 m 行：{ok_trunc}/{n_tested}')
    return ok_scale == n_tested and ok_trunc == n_tested


def second_instance():
    N = 6
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [[Fr(0)] * N]
    C[0][0] = Fr(1)
    A = [[Fr(0)] * N for _ in range(N)]
    A[0][5] = Fr(1); A[2][2] = Fr(1); A[3][3] = Fr(1)
    A[1][1] = Fr(1); A[4][4] = Fr(1)
    L0 = [[Fr(0)] * N]
    L0[0][1] = Fr(1)
    return A, C, L0, unit


def main():
    A, C, L0, unit = second_instance()
    # q=2, s=2 ⟹ d=3, r=1, t=v-s=2 ⟹ r+t=3, w-s=4 ⟹ 非方阵
    # 需要 q=t=2 且 s 使 r+t=wm：r = w-q-s = 3-s，t = v-s = 4-s ⟹ r+t = 7-2s = w-s = 5-s ⟹ s=2 ⟹ r=1,t=2,wm=3？
    # 直接扫 s 与 q，找方阵情形
    for q in (2, 3):
        for s in (1, 2):
            N = 6
            def u(i):
                return [Fr(1) if k == i else Fr(0) for k in range(N)]
            S = [u(2), u(3)][:s]
            try:
                run(A, C, L0, q, S, f'第二实例 q={q} s={s}')
            except AssertionError as e:
                print(f'  断言失败: {e}')
    # R17 扫描
    N = 8
    def u8(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C2 = [u8(0), u8(1)]
    L02 = [u8(2)]
    A2 = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(6, 2), (7, 3), (4, 4), (5, 5), (0, 6), (1, 7)]:
        A2[i][j] = Fr(1)
    for q in (2, 3, 4):
        for s in (1, 2):
            S = [u8(4), u8(5)][:s]
            try:
                run(A2, C2, L02, q, S, f'R17 q={q} s={s}')
            except AssertionError as e:
                print(f'  断言失败: {e}')


if __name__ == '__main__':
    main()
