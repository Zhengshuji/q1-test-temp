r"""c301：G3 在 **$q=t,\ r=2$** 域的重做（专家 2026-11-01 §9.1 + 任务 3）。

**为什么重做**：支 5 的 58 例全在 $q\ne t$ 域，且用的是 $m$ 行**截断**对象（`coeff_forms_balanced`，
它甚至不是铅笔的某个子式）。专家要求：用**真铅笔**（$w_m$ 行、$r+t=w_m$ 方阵）在 $q=t$ 上重测，
五个量**分列**记录，不许合并成一个布尔。

**实例**：R17，$q=2$（$n=8,p=2$；$d=4$，$s=2$，$r=2$，$t=2$，$m=3$，$w_m=4$，$q=t$ ✓ 方阵）。

**坐标约定**：用**适配基** $T$（`adapted_basis`）把 $H/S$ 变成 $\operatorname{span}(e_1..e_m)$，
于是 $U\subseteq E=H/S$ 的 Plücker 坐标只占 $I\subseteq[m]$ 的位置，$a_j$ 可无歧义地限制到 $\Lambda^r E$。
换基只乘 $\det T^{-1}\ne0$，不影响"是否非零常数"。

**五列**：
1. $\dim K$，$K=\bigcap_{j\ge1}\ker a_j^E\subseteq\Lambda^2E$；
2. $a_0|_K\ne0$（线性松弛 C2，专家 §2.4 的精确形式是 $a_0|_D\ne0$）；
3. $\dim D_{\rm adm}(K)$（可容许 + 可分解 + 落在 $K$ 里的 Plücker 点张成）；
4. $a_0|_{D_{\rm adm}}\ne0$（精确系数判据 C1）；
5. 直接铅笔：$\det[U\mid P(\lambda)]$ 是非零常数（独立路径，不经过 $a_j$）。

**自检**：逐 $U$ 比较"C1（系数路径）"与"直接 det"，必须完全一致；不一致说明实现有问题。

**等级**：精确验证（有理算术、有限格点）。**不是证明**；只回答"在这个域里 G3 是否发生"。

用法：python workspace/A3_basefamily/scripts/c301_g3_square.py
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
import coeff_of_S as CS
import spectral_gcd as SG
import base_sweep as BS
import poly_smith as PS


def unit(n, i):
    return [Fr(1) if k == i else Fr(0) for k in range(n)]


def r17():
    N = 8
    C = [unit(N, 0), unit(N, 1)]
    L0 = [unit(N, 2)]
    A = [[Fr(0)] * N for _ in range(N)]
    A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1)
    A[5][5] = Fr(1); A[0][6] = Fr(1); A[1][7] = Fr(1)
    return A, C, L0


def rank_of(cols):
    if not cols:
        return 0
    n = len(cols[0])
    return AI.rank([[cols[j][i] for j in range(len(cols))] for i in range(n)])


def det(M):
    n = len(M)
    if n == 0:
        return Fr(1)
    A = [list(row) for row in M]
    d = Fr(1)
    for i in range(n):
        p = next((k for k in range(i, n) if A[k][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            A[i], A[p] = A[p], A[i]
            d = -d
        d *= A[i][i]
        inv = Fr(1) / A[i][i]
        for k in range(i + 1, n):
            f = A[k][i] * inv
            for j in range(i, n):
                A[k][j] -= f * A[i][j]
    return d


def matmul(T, M):
    """T: wm×wm，M: wm×c。返回 T·M。"""
    wm, c = len(T), len(M[0]) if M else 0
    return [[sum(T[i][k] * M[k][j] for k in range(wm)) for j in range(c)] for i in range(wm)]


def pdet_is_const(polys):
    """polys[i][j] 是多项式（系数列表）；返回 det 是否非零常数。"""
    d = SG.pdet(polys)
    return SG.pdeg(d) == 0


def kernel_functional(lam, m):
    """ker(lam·x) ⊆ C^m 的基（m=3、2 维）。"""
    piv = next(i for i in range(m) if lam[i] != 0)
    basis = []
    for j in range(m):
        if j == piv:
            continue
        v = [Fr(0)] * m
        v[j] = Fr(1)
        v[piv] = Fr(-lam[j]) / Fr(lam[piv])
        basis.append(v)
    return basis


def plucker(U):
    r = len(U)
    m = len(U[0])
    return [det([[U[b][i] for b in range(r)] for i in I])
            for I in itertools.combinations(range(m), r)]


def main():
    A, C, L0 = r17()
    q, s = 2, 2
    n = len(A)
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    W = AI.nullspace([row[:] for row in C])
    H = AI.nullspace([row[:] for row in (C + L0)])
    Vperp = AI.nullspace([list(x) for x in V])
    Hperp = AI.nullspace([list(x) for x in H])
    G = AI.nullspace(Vperp + Hperp)
    Gperp = AI.nullspace([list(x) for x in G])
    D = AI.nullspace(Gperp + AI.mul(Hperp, A))
    w, v, h, b, dimD = len(W), len(V), len(H), len(G), len(D)
    d = w - q
    r, t, wm, m = d - s, v - s, w - s, h - s
    print(f'R17: n={n} p={len(C)} w={w} v={v} h={h} b={b} dimD={dimD}')
    print(f'     q={q} d={d} s={s} r={r} t={t} m={m} w_m={wm}   方阵(r+t=w_m): {r+t==wm}   q=t: {q==t}')
    assert r + t == wm and q == t, '本脚本只处理 q=t 的方阵域'

    # S 的池：V ∩ D ∩ H
    VD = AI.nullspace(Vperp + [[sum(A[i][k] * y[i] for i in range(n)) for k in range(n)]
                                for y in Hperp])
    VDH = AI.nullspace(AI.nullspace([list(x) for x in VD]) + Hperp)
    print(f'     dim(V∩D∩H) = {len(VDH)}')

    # E 的全部 2 维子空间（E 三维 ⟹ 都是某个线性泛函的核）
    Us = []
    seen = set()
    for lam in itertools.product((-1, 0, 1), repeat=m):
        if all(c == 0 for c in lam):
            continue
        lead = next(c for c in lam if c != 0)
        key = tuple(x / lead for x in lam)
        if key in seen:
            continue
        seen.add(key)
        Us.append(kernel_functional(lam, m))
    print(f'     E 内 2 维子空间（P² 的格点）：{len(Us)}\n')

    S_list = []
    seenS = set()
    for coefs in itertools.product((-1, 0, 1), repeat=len(VDH)):
        S = [[Fr(c) * x for x in VDH[j]] for j, c in enumerate(coefs) if c != 0]
        if len(S) != s or rank_of(S) != s:
            continue
        key = tuple(tuple(x) for x in S)
        if key in seenS:
            continue
        seenS.add(key)
        S_list.append(S)
    print(f'     S 的格点数：{len(S_list)}\n')

    total_adm = total_true = total_fp = 0
    n_cross = [0, 0]
    n_legacy = [0, 0]
    summary = []
    for S in S_list:
        st = CS.setup(A, C, L0, q, S)
        P0, P1 = None, None
        cols = CS.pencil_cols(A, st)
        P0 = [[cols[j][0][i] for j in range(t)] for i in range(wm)]
        P1 = [[cols[j][1][i] for j in range(t)] for i in range(wm)]
        # 适配基：H/S → span(e_1..e_m)
        T = CS.adapted_basis(st)
        Ti = CS._invert(T)
        Pn0 = matmul(Ti, P0)
        Pn1 = matmul(Ti, P1)
        # 断言：适配基下 H/S 确实是前 m 个坐标
        for hv in st['HS']:
            tv = [sum(Ti[i][k] * hv[k] for k in range(wm)) for i in range(wm)]
            assert all(tv[i] == 0 for i in range(m, wm)), '适配基没把 H/S 变成前 m 个坐标'
        a, idxs = CS.CS.coeff_forms([Pn0, Pn1], wm, r)
        aE, idxE = CS.restrict_to_E(a, idxs, m)
        assert len(aE[0]) == 3
        forms = [aE[j] for j in range(1, len(aE)) if any(aE[j])]
        K = AI.nullspace(forms) if forms else [[Fr(1) if k == i else Fr(0) for k in range(3)]
                                               for i in range(3)]
        dimK = len(K)
        C2 = any(sum(aE[0][i] * u[i] for i in range(3)) != 0 for u in K)
        # T_S、G/S 在适配基下
        TS, GS = [], []
        for x in S:
            Ax = [sum(A[i][k] * x[k] for k in range(n)) for i in range(n)]
            c = CS._solve_in_basis(st['WB'], Ax)[s:]
            TS.append([sum(Ti[i][k] * c[k] for k in range(wm)) for i in range(wm)])
        for g in G:
            c = CS._solve_in_basis(st['WB'], g)[s:]
            GS.append([sum(Ti[i][k] * c[k] for k in range(wm)) for i in range(wm)])
        # 只保留 H/S 部分（前 m 个坐标）
        TS = [x[:m] for x in TS]
        GS = [x[:m] for x in GS]
        rkTS, rkG = rank_of(TS), rank_of(GS)

        pts = []
        n_adm_S = n_true_S = 0
        n_xcheck = n_xok = 0
        for U in Us:
            if TS and rank_of(U + TS) != r:
                continue
            if GS and rank_of(GS + U) != rkG + r:
                continue
            n_adm_S += 1
            pU = plucker(U)
            inK = all(sum(forms[j][k] * pU[k] for k in range(3)) == 0 for j in range(len(forms)))
            if inK:
                pts.append(pU)
            # 直接路径：把 U 嵌入 W_m（前 m 个坐标），det[U|P_n(λ)] 是否为非零常数
            Ufull = [[U[j][k] if k < m else Fr(0) for k in range(wm)] for j in range(r)]
            Qpoly = PS.make_pencil(Ufull, Pn0, Pn1)
            direct = PS.full_col_rank_constant(Qpoly)[0]
            # 交叉检查：旧的"枚举子式 + gcd"路径（2026-11-01 起只作核对）
            polys = []
            for i in range(wm):
                row = [[Ufull[j][i]] for j in range(r)]
                row += [[Pn0[i][j], Pn1[i][j]] for j in range(t)]
                polys.append(row)
            direct_legacy = pdet_is_const(polys)
            n_legacy[0] += 1
            if direct != direct_legacy:
                print(f'  !! Smith 与枚举子式不一致：S={S} U={U} {direct} vs {direct_legacy}')
                total_fp += 1
            else:
                n_legacy[1] += 1
            c1 = inK and sum(aE[0][k] * pU[k] for k in range(3)) != 0
            if c1 != direct:
                print(f'  !! C1 与 direct 不一致：S={S} U={U} C1={c1} direct={direct}')
                total_fp += 1
            if direct:
                n_true_S += 1
            # 第三条独立路径：check_Z（(A)+(S)，n 维、不经过系数/适配基）
            if n_xcheck < 2:
                Zcols = [list(sv) for sv in S]
                for j in range(r):
                    u_ws_j = [sum(T[i][k] * (U[j][k] if k < m else Fr(0)) for k in range(wm))
                              for i in range(wm)]
                    Zcols.append([sum(u_ws_j[k] * st['WB'][s + k][i] for k in range(wm))
                                  for i in range(n)])
                Zmat = [[Zcols[j][i] for j in range(len(Zcols))] for i in range(n)]
                okA, okS, _g = BS.check_Z(A, C, Zmat)
                n_xcheck += 1
                n_cross[0] += 1
                if okA and (okS == direct):
                    n_xok += 1
                    n_cross[1] += 1
                else:
                    print(f'  !! check_Z 不符：S={S} okA={okA} okS={okS} direct={direct}')
        dimD_adm = AI.rank(pts) if pts else 0
        C1 = any(sum(aE[0][k] * p[k] for k in range(3)) != 0 for p in pts)
        total_adm += n_adm_S
        total_true += n_true_S
        summary.append((dimK, C2, dimD_adm, C1))
        print(f'  S = {[[str(x) for x in sv] for sv in S]}')
        print(f'    dimK={dimK}  a0|K≠0={C2}  dimD_adm={dimD_adm}  a0|D≠0={C1}'
              f'   可容许U={n_adm_S}  直接det通过={n_true_S}')
        if dimK and dimD_adm < dimK:
            print('    注：D_adm ⊊ K（K 里有不可分解/不可容许的点）')
        if C2 and not C1:
            print('    >>> 假阳性：线性松弛说可行，精确判据说不可行')
    print(f'\n汇总：S {len(S_list)} 个；可容许 U 共 {total_adm} 个；直接 det 通过 {total_true} 个；'
          f'C1/direct 不一致 {total_fp} 个')
    print(f'check_Z 交叉核对：{n_cross[0]} 个 (S,U)，一致 {n_cross[1]} 个')
    print(f'Smith vs 枚举子式：{n_legacy[0]} 个 U，一致 {n_legacy[1]} 个')
    print('(dimK, C2, dimD_adm, C1)：', summary)
    assert total_fp == 0, 'C1 与 direct 不一致——实现有问题'
    print('\n读法：直接 det 通过数 = 0 ⟹ 该域（R17 q=2）无可行 U（null result，'
          '与不可行相容，不能反证）；>0 ⟹ 有 True 点，才谈得上 G3。')


if __name__ == '__main__':
    main()
