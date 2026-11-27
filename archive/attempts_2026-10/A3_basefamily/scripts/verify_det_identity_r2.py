r"""A-1（续）：$r\ge2$ 的行列式恒等式（多重线性展开）。

**命题**：$[U\\mid P(\\lambda)]$ 是 $(w-s)\\times(r+t)$ 方阵（$q=t$）。沿 $U$ 的 $r$ 列做 Laplace 展开：
$$\\det[U\\mid P]=\\sum_{|I|=r}\\pm\\,p_U[I]\\cdot\\det\\!\\big(P_{I^{c}}(\\lambda)\\big),$$
其中 $p_U[I]$ 是 $U$ 的 Plücker 坐标、$I^c$ 是补行集。故
$$\\det[U\\mid P(\\lambda)]=\\sum_j\\lambda^j\\Big(\\sum_{|I|=r}c_I\\,a_j[I]\\,p_U[I]\\Big),\\qquad c_I=\\pm1 .$$

**检验**（R17，$q=2$、$s=2$：$r=2$、$t=2$、$w-s=4$ 方阵）：
1. 用坐标子空间 $U=\\operatorname{span}(e_{i_1},e_{i_2})$ 定出每个 $c_I$；
2. 对随机 $U$ 验证恒等式（逐系数）。

用法：python workspace/A3_basefamily/scripts/verify_det_identity_r2.py
"""
import itertools
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


def det_poly(Ucols, cols, wm, t):
    """det[U|P(λ)]：Ucols 是 r 个列（长度 wm），cols 是 t 个 (c0,c1)。"""
    P = []
    for i in range(wm):
        row = [[Ucols[k][i]] for k in range(len(Ucols))]
        row += [[cols[j][0][i], cols[j][1][i]] for j in range(t)]
        P.append(row)
    return SG.pdet(P)


def plucker_of(Ucols):
    """U 的 Plücker 坐标（按 coeff_forms 的 idxs 顺序 = itertools.combinations(range(wm), r)）。"""
    r = len(Ucols)
    wm = len(Ucols[0])
    out = []
    for I in itertools.combinations(range(wm), r):
        M = [[Ucols[k][i] for k in range(r)] for i in I]
        # r×r 行列式
        n = r
        A = [row[:] for row in M]
        d = Fr(1)
        for a in range(n):
            p = next((b for b in range(a, n) if A[b][a] != 0), None)
            if p is None:
                d = Fr(0)
                break
            if p != a:
                A[a], A[p] = A[p], A[a]
                d = -d
            d *= A[a][a]
            inv = Fr(1) / A[a][a]
            for b in range(a + 1, n):
                f = A[b][a] * inv
                for c in range(a, n):
                    A[b][c] -= f * A[a][c]
        out.append(d)
    return out


def main():
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [unit(0), unit(1)]
    L0 = [unit(2)]
    A = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(6, 2), (7, 3), (4, 4), (5, 5), (0, 6), (1, 7)]:
        A[i][j] = Fr(1)
    q, S = 2, [unit(4), unit(5)]
    st = CS_.setup(A, C, L0, q, S)
    wm = st['w'] - st['s']
    cols = CS_.pencil_cols(A, st)
    t = len(cols)
    r = st['d'] - st['s']
    print(f'R17 q={q} s={len(S)}: w-s={wm}, r={r}, t={t}；方阵? {r+t==wm}')
    assert r + t == wm, '非方阵'
    P0 = [[cols[j][0][i] for j in range(t)] for i in range(wm)]
    P1 = [[cols[j][1][i] for j in range(t)] for i in range(wm)]
    a, idxs = CS2.coeff_forms([P0, P1], wm, r)
    print(f'  a_j 个数={len(a)}；Plücker 坐标数={len(a[0])}（应=C({wm},{r})={len(idxs)}）')
    assert len(a[0]) == len(idxs)
    # 1) 定符号
    signs = []
    for idx, I in enumerate(idxs):
        Uc = [[Fr(1) if k == i else Fr(0) for k in range(wm)] for i in I]
        lhs = det_poly(Uc, cols, wm, t)
        # 与 a[·][idx] 比较（取第一个非零系数定符号）
        s = None
        for j in range(max(len(lhs), len(a))):
            l = lhs[j] if j < len(lhs) else Fr(0)
            rr = a[j][idx] if j < len(a) else Fr(0)
            if l != 0 or rr != 0:
                if l == rr:
                    s = Fr(1)
                elif l == -rr:
                    s = Fr(-1)
                else:
                    s = None
                break
        if s is None:
            # 两边恒为零 ⟹ 该坐标的符号无关紧要
            s = Fr(1) if all(x == 0 for x in lhs) else None
        signs.append(s)
    ok_sign = all(s is not None for s in signs)
    print(f'  逐个坐标定符号：{sum(1 for s in signs if s is not None)}/{len(signs)} 成功；符号 = '
          f'{[str(s) for s in signs]}')
    # 2) 随机 U 验证
    rng = random.Random(13)
    ok = 0
    n = 0
    for _ in range(8):
        Uc = [[Fr(rng.randint(-2, 2)) for _ in range(wm)] for _ in range(r)]
        if AI.rank(Uc) < r:
            continue
        lhs = det_poly(Uc, cols, wm, t)
        p = plucker_of(Uc)
        rhs = [sum(signs[idx] * a[j][idx] * p[idx] for idx in range(len(idxs)))
               for j in range(len(a))]
        n += 1
        if SG.ptrim(lhs) == SG.ptrim(rhs):
            ok += 1
        else:
            print(f'   FAIL: lhs={[str(x) for x in lhs]} rhs={[str(x) for x in rhs]}')
    print(f'  随机 U 逐系数恒等：**{ok}/{n}**')


if __name__ == '__main__':
    main()
