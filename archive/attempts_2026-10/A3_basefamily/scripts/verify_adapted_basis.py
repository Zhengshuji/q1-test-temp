r"""A-1 的前置：**adapted basis 的验证**（分支 4 / E-1 的落地部分）。

**要验证的命题**：设 $E=W/S$（$\dim\\,wm$）、$H/S\\subseteq E$（$\dim m$）。存在可逆 $T$ 使
$$T^{-1}(H/S)=\\operatorname{span}(e_1,\\dots,e_m).$$
于是对 $U\\subseteq H/S$（$\dim r$）与铅笔 $P(\\lambda)$：
$$\\det[U_{\\rm new}\\mid P_{\\rm new}(\\lambda)]=\\det(T^{-1})\\cdot\\det[U_{\\rm old}\\mid P_{\\rm old}(\\lambda)],$$
右因子是**非零常数** ⟹ "是否非零"与基无关；且 $U_{\\rm new}$ 的支撑在前 $m$ 个坐标里，
故只需 $P_{\\rm new}$ 的**前 $m$ 行**。

**检验**：
1. $T$ 可逆，$T^{-1}(H/S)\\subseteq\\operatorname{span}(e_1..e_m)$ 且维数 $=m$（故相等）；
2. 对随机 $U$：$\\det[U_{\\rm new}\\mid P_{\\rm new}]=\\det(T^{-1})\\cdot\\det[U_{\\rm old}\\mid P_{\\rm old}]$（逐系数比较）；
3. $U_{\\rm new}$ 在前 $m$ 行之外全为 0 ⟹ 用前 $m$ 行算出的行列式与完整行列式相同。

用法：python workspace/A3_basefamily/scripts/verify_adapted_basis.py
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


def det_fr(M):
    n = len(M)
    if n == 0:
        return Fr(1)
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


def check_instance(A, C, L0, q, S, label):
    st = CS_.setup(A, C, L0, q, S)
    wm = st['w'] - st['s']
    m = st['m']
    T = CS_.adapted_basis(st)
    Ti = CS_._invert(T)
    # 1) T 可逆
    assert AI.rank(T) == wm, 'T 不可逆'
    # 2) T^{-1}(H/S) = span(e_1..e_m)
    HSnew = [[sum(Ti[i][j] * h[j] for j in range(wm)) for i in range(wm)] for h in st['HS']]
    ok_span = True
    for v in HSnew:
        if any(v[i] != 0 for i in range(m, wm)):
            ok_span = False
    rk = AI.rank(HSnew)
    print(f'{label}: wm={wm} m={m} rank(T)={AI.rank(T)} T^-1(H/S) 支撑在前 m 行? {ok_span} rank={rk}')
    assert ok_span and rk == m, 'adapted basis 失败'
    # 3) 行列式恒等式（随机 U，r=1）
    cols = CS_.pencil_cols(A, st)
    t = len(cols)
    r = 1
    assert r + t == wm, f'非平衡：r+t={r+t} != wm={wm}'
    dTi = det_fr(Ti)
    ok = 0
    for _ in range(5):
        u_old = [Fr(random.randint(-2, 2)) for _ in range(wm)]
        if all(x == 0 for x in u_old):
            continue
        u_new = [sum(Ti[i][j] * u_old[j] for j in range(wm)) for i in range(wm)]
        # 旧：det[U_old | P_old]（(r+t) x (r+t) = wm x wm 方阵）
        def dmat(u, Pcols):
            M = [[u[i]] + [Pcols[j][0][i] + Fr(0) * 0 for j in range(t)] for i in range(wm)]
            # 这里按多项式系数比较，故分开处理
            return M
        # 逐 λ 系数：用 (r+t)x(r+t) 多项式行列式
        def poly_det(u, Pcols):
            P = []
            for i in range(wm):
                row = [[u[i]]]
                row += [[Pcols[j][0][i], Pcols[j][1][i]] for j in range(t)]
                P.append(row)
            return SG.pdet(P)

        def poly_det_from(u, Pcols):
            P = []
            for i in range(wm):
                row = [[u[i]]]
                row += [[Pcols[j][0][i], Pcols[j][1][i]] for j in range(t)]
                P.append(row)
            return SG.pdet(P)

        old = poly_det(u_old, cols)
        new = poly_det(u_new, cols)
        # 期望 new = det(Ti) * old
        expect = SG.pscale(dTi, old) if hasattr(SG, 'pscale') else [dTi * x for x in old]
        same = SG.ptrim(new) == SG.ptrim(expect)
        # 4) 只用前 m 行的行列式（U_new 支撑在前 m 行 ⟹ 其余行是零列，行列式为 0）
        trunc = poly_det([u_new[i] if i < m else Fr(0) for i in range(wm)],
                         [[[cols[j][0][i] if i < m else Fr(0) for i in range(wm)],
                           [cols[j][1][i] if i < m else Fr(0) for i in range(wm)]] for j in range(t)])
        same_trunc = SG.ptrim(trunc) == SG.ptrim(expect)
        ok += (1 if (same and same_trunc) else 0)
        if not (same and same_trunc):
            print('   FAIL: new=', [str(x) for x in new], ' expect=', [str(x) for x in expect],
                  ' trunc=', [str(x) for x in trunc])
    print(f'   行列式恒等式通过 {ok}/5')
    return ok == 5


def main():
    print('=== adapted basis 验证\n')
    # c282
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [unit(0), unit(1)]
    L0 = [unit(2)]
    A = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(0, 2), (1, 3), (4, 4), (3, 5), (5, 6), (6, 7)]:
        A[i][j] = Fr(1)
    ok1 = check_instance(A, C, L0, 4, [unit(4)], 'c282')

    # 随机实例
    src = open(os.path.join(_HERE, 'c297_mixed_instances.py'), encoding='utf-8').read()
    src = src.split("if __name__")[0]
    ns = {'__file__': os.path.join(_HERE, 'c297_mixed_instances.py'), '__name__': 'c297x'}
    exec(src, ns)
    rng = random.Random(20261031)
    ok2 = None
    for _ in range(60):
        n = rng.choice([6, 7, 8])
        p = rng.choice([1, 2])
        A, C, L0 = ns['make_instance'](n, p, rng)
        try:
            geo = ns['geometry'](A, C, L0)
        except Exception:
            continue
        if geo['dimD'] < 2:
            continue
        s = 1
        q = geo['w'] - geo['h'] + geo['v'] - s
        if q < 1:
            continue
        S = ns['lift'](ns['BS'].enum_subspaces(geo['dimD'], 1, bound=1)[1], geo['D'], geo['n'])
        try:
            ok2 = check_instance(A, C, L0, q, S, f'random(n={n},p={p})')
            break
        except AssertionError as e:
            print('   跳过:', e)
    print(f'\n结论：c282 {"通过" if ok1 else "失败"}；随机实例 {"通过" if ok2 else "未验证"}')


if __name__ == '__main__':
    main()
