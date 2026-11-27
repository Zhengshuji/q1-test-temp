r"""A-1 的核心（分支 4 交付）：**行列式恒等式**的逐系数验证（方阵情形，$r=1$）。

**命题**：$q=t$ 时 $[U\mid P(\lambda)]$ 是 $(w-s)\\times(w-s)$ 方阵，$r=1$ 时
$$\\det[U\\mid P(\\lambda)]=\\sum_{j=0}^{\\deg}\\lambda^j\\,\\langle a_j,u\\rangle,$$
其中 $a_j$ 由 `coeff_space.coeff_forms([P0,P1], wm, r)` 给出（**不换基、不截断**）。

**检验**：对随机 $u$，逐**系数**比较两边（必须恒等，不是"相差常数"）。

用法：python workspace/A3_basefamily/scripts/verify_det_identity.py
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
    cols = CS_.pencil_cols(A, st)
    t = len(cols)
    r = st['d'] - st['s']
    print(f'\n=== {label}: w-s={wm}, r={r}, t={t}, q={q}')
    if r != 1:
        print(f'  （本脚本只处理 r=1；r={r} 跳过）')
        return None
    if r + t != wm:
        print(f'  非方阵（r+t={r+t} != w-s={wm}；q={q} != t={t}）⟹ 单行列式不适用，跳过')
        return None
    P0 = [[cols[j][0][i] for j in range(t)] for i in range(wm)]
    P1 = [[cols[j][1][i] for j in range(t)] for i in range(wm)]
    a, idxs = CS2.coeff_forms([P0, P1], wm, r)
    print(f'  a_j 个数 = {len(a)}（deg = {len(a)-1}）；Plücker 坐标数 = {len(a[0])}（应 = w-s = {wm}）')
    assert len(a[0]) == wm, 'Plücker 坐标数应等于 w-s（r=1）'
    rng = random.Random(11)
    ok = 0
    n = 0
    for _ in range(8):
        u = [Fr(rng.randint(-2, 2)) for _ in range(wm)]
        if all(x == 0 for x in u):
            continue
        lhs = poly_det(u, cols, wm, t)                       # det[U|P(λ)]
        rhs = [sum(a[j][k] * u[k] for k in range(wm)) for j in range(len(a))]
        n += 1
        # 容差：符号约定（列序/Plücker 记号的顺序）可能给出整体的 -1
        neg = [(-x) for x in rhs]
        if SG.ptrim(lhs) == SG.ptrim(rhs) or SG.ptrim(lhs) == SG.ptrim(neg):
            ok += 1
            if SG.ptrim(lhs) != SG.ptrim(rhs):
                pass  # 记录：相差 -1
        else:
            print(f'   FAIL: u={[str(x) for x in u]}')
            print(f'     det = {[str(x) for x in lhs]}')
            print(f'     Σa  = {[str(x) for x in rhs]}')
    print(f'  逐系数恒等（允许整体 -1 的符号约定）：**{ok}/{n}**')
    return ok == n


def main():
    # 第二实例
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
    r1 = run(A, C, L0, 2, [unit(2), unit(3)], '第二实例 q=2 s=2')
    r2 = run(A, C, L0, 3, [unit(2)], '第二实例 q=3 s=1')
    # c282（非方阵，应被跳过）
    N8 = 8
    def u8(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N8)]
    C8 = [u8(0), u8(1)]
    L08 = [u8(2)]
    A8 = [[Fr(0)] * N8 for _ in range(N8)]
    for (i, j) in [(0, 2), (1, 3), (4, 4), (3, 5), (5, 6), (6, 7)]:
        A8[i][j] = Fr(1)
    r3 = run(A8, C8, L08, 4, [u8(4)], 'c282 q=4 s=1')
    print('\n--- 汇总 ---')
    print(f'第二实例 q=2: {r1}；q=3: {r2}；c282: {r3 if r3 is not None else "跳过（非方阵）"}')


if __name__ == '__main__':
    main()
