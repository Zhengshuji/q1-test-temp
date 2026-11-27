r"""A-1 的**判据**验证（方阵、$r=1$）：$a_j$ 判据 ⟺ 直接判据（含可容许性）。

**背景**：
- $r=1$ 时每个非零向量都可分解 ⟹ **没有 G3 障碍** ⟹ 线性判据应当是**充要**的（QA25 §1.2）；
- 但可容许性（$T_S\\subseteq U$、$U\\cap G=S$）必须一起查（§37 的教训）。

**检验**（两个方阵 $r=1$ 实例 + c282 作对照）：
对 $H/S$ 的格点 $u$：
| 直接侧 | 判据侧 |
|---|---|
| $q_u(\\lambda)=\\det[u\\mid P(\\lambda)]$ 是非零常数 | $\\langle a_j,u\\rangle=0\\ (j\\ge1)$ 且 $\\langle a_0,u\\rangle\\ne0$ |
| 且可容许：$T_S\\subseteq\\operatorname{span}(u)$、$u\\notin G/S$ | 同样要检查可容许 |

不一致数必须为 **0**。

用法：python workspace/A3_basefamily/scripts/verify_criterion_square_r1.py
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
import spectral_gcd as SG
import coeff_of_S as CS_
import coeff_space as CS2


def q_poly(u, cols, wm, t):
    P = []
    for i in range(wm):
        row = [[u[i]]]
        row += [[cols[j][0][i], cols[j][1][i]] for j in range(t)]
        P.append(row)
    return SG.pdet(P)


def check(A, C, L0, q, S, label):
    st = CS_.setup(A, C, L0, q, S)
    wm = st['w'] - st['s']
    m = st['m']
    cols = CS_.pencil_cols(A, st)
    t = len(cols)
    r = st['d'] - st['s']
    if r != 1 or r + t != wm:
        print(f'{label}: r={r}、r+t={r+t}、w-s={wm} ⟹ 跳过（只做方阵 r=1）')
        return None
    P0 = [[cols[j][0][i] for j in range(t)] for i in range(wm)]
    P1 = [[cols[j][1][i] for j in range(t)] for i in range(wm)]
    a, idxs = CS2.coeff_forms([P0, P1], wm, r)
    # 可容许性数据（都在 H/S 的 row 坐标里）
    # G/S 的坐标（G = V ∩ H，用**零化子**构造）
    wb = st['WB']
    Vp = AI.nullspace([list(x) for x in st['V']])
    Hp = AI.nullspace([list(x) for x in st['H']])
    Ggeo = AI.nullspace(Vp + Hp)
    Gc = []
    for g in Ggeo:
        full = CS_._solve_in_basis(wb, g)[st['s']:]
        Gc.append(full)
    rkG = AI.rank(Gc) if Gc else 0
    # T_S 的坐标
    TS = []
    for sv in S:
        av = [sum(A[i][k] * sv[k] for k in range(len(sv))) for i in range(len(sv))]
        TS.append(CS_._solve_in_basis(wb, av)[st['s']:])
    rkT = AI.rank(TS) if TS else 0
    print(f'\n=== {label}: w-s={wm}, m={m}, r=1, t={t}, q={q}；dim(G/S)={rkG}，k=dim T_S={rkT}')
    mism = 0
    n_direct = 0
    n_crit = 0
    tested = 0
    for coefs in itertools.product((-2, -1, 0, 1, 2), repeat=wm):
        if all(c == 0 for c in coefs):
            continue
        u = [Fr(c) for c in coefs]
        # 可容许性
        adm = True
        if rkG and AI.rank(Gc + [u]) == rkG:
            adm = False                       # u ∈ G/S
        if rkT == 1:
            gen = next(x for x in TS if any(x))
            if AI.rank([list(gen), list(u)]) == 1 and any(gen):
                pass
            else:
                adm = False                   # U 必须恰为 T_S（r=1、k=1）
        elif rkT > 1:
            adm = False
        if not adm:
            continue
        tested += 1
        # 直接侧
        qq = q_poly(u, cols, wm, t)
        direct = all(x == 0 for x in qq[1:]) and qq[0] != 0
        # 判据侧
        crit = (all(sum(a[j][k] * u[k] for k in range(wm)) == 0 for j in range(1, len(a)))
                and sum(a[0][k] * u[k] for k in range(wm)) != 0)
        n_direct += (1 if direct else 0)
        n_crit += (1 if crit else 0)
        if direct != crit:
            mism += 1
    print(f'  可容许的 u：{tested} 个；直接可行 {n_direct}；判据可行 {n_crit}；**不一致 {mism}**')
    if n_direct == 0:
        print('  ⚠ 没有 True 点 ⟹ 该检验是**空的**（CLAUDE §10.2 地基检查）')
    return (mism == 0, n_direct)


def main():
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
    r1 = check(A, C, L0, 2, [unit(2), unit(3)], '第二实例 q=2 s=2')
    r2 = check(A, C, L0, 3, [unit(2)], '第二实例 q=3 s=1')
    print(f'\n汇总：q=2 -> {r1}；q=3 -> {r2}')
    # 随机搜索一个**有 True 点**的方阵 r=1 实例
    import random
    src = open(os.path.join(_HERE, 'c297_mixed_instances.py'), encoding='utf-8').read()
    ns = {'__file__': os.path.join(_HERE, 'c297_mixed_instances.py'), '__name__': 'c297x'}
    exec(src.split("if __name__")[0], ns)
    import base_sweep as BS
    rng = random.Random(20261101)
    print('\n=== 搜索含 True 点的方阵 r=1 实例')
    for trial in range(80):
        n = rng.choice([6, 7, 8])
        pp = rng.choice([1, 2])
        A2, C2, L02 = ns['make_instance'](n, pp, rng)
        try:
            geo = ns['geometry'](A2, C2, L02)
        except Exception:
            continue
        if geo['dimD'] < 2:
            continue
        for s in (1, 2):
            if s > geo['dimD']:
                continue
            qq = geo['v'] - s
            if qq < 1:
                continue
            coords = BS.enum_subspaces(geo['dimD'], s, bound=1)
            if not coords:
                continue
            S = ns['lift'](coords[0], geo['D'], n)
            if len(S) < s:
                continue
            try:
                res = check(A2, C2, L02, qq, S, f'trial{trial}(n={n},p={pp},s={s})')
            except Exception:
                continue
            if res and res[1] > 0:
                print(f'  ✓ 找到：不一致 {0 if res[0] else "?"}，直接可行 {res[1]}')
                return
    print('  未找到含 True 点的方阵 r=1 实例（80 次）')


if __name__ == '__main__':
    main()
