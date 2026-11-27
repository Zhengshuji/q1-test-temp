r"""c302：$r=2$、$m=5$ 的真实实例上跑双向量判定（A2 的实例层）。

**目标**：在 $\mathrm{DEC}(q)$ 的真实 $K$ 上问：$K$ 里有没有**可分解**的 $p_U$（即有没有 $U$）。
与 $r=1$ 的系数判据不同，这里"可分解"不是自动的（$m=5$ 时 $\Lambda^2\mathbb C^5$ 里一般元不可分解）。

**要造的实例**：$m=h-s=5$、$r=d-s=2$、$q=t$（方阵域）。由恒等式
$$r+t=w-q+v-2s,\quad t=v-s,\quad m=h-s$$
取 $n=9,p=2$（$w=7$）、$v=n-2p-2=5$、$h=n-p-1=6$，则 $s=h-m=1$、$q=v-s=4$、$r=w-q-s=2$、$t=4=q$ ✓。

**做法**：
1. 随机搜索一个满足 $v=5,h=6,\dim(V\cap D\cap H)\ge1$ 的 $A$（不满足就换）；
2. 对每个 $S\in\operatorname{Gr}(1,V\cap D\cap H)$：用 `coeff_forms_full` 算 $a_j$，限制到 $E=H/S$；
3. $K=\bigcap_{j\ge1}\ker a_j^E$；把**线性**可容许条件 $T_S\subseteq U_p$ 收缩成 $K'\subseteq K$；
4. `bivector.has_decomposable(K', 5)` —— 判定"存在可分解元"；
5. 对照：枚举可容许 $U\in\operatorname{Gr}(2,5)$，直接算 $\det[U\mid P]$ 是否非零常数。

**等级**：精确验证。若第 4 步给出 `None`（未决），如实打印，不强行下结论。

用法：python workspace/A3_basefamily/scripts/c302_bivector_m5.py
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
import base_sweep as BS
import bivector as BV
import coeff_of_S as CS
import poly_smith as PS


def try_instance(rng, n=9, p=2, tries=4000):
    """找一个满足 v=5, h=6, dim(V∩D∩H)≥1 的实例。"""
    for _ in range(tries):
        C = [[Fr(1) if k == i else Fr(0) for k in range(n)] for i in range(p)]
        L0 = [[Fr(1) if k == p else Fr(0) for k in range(n)]]
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        try:
            geo = BS.geometry(A, C, L0)
        except AssertionError:
            continue
        if geo['v'] != 5 or geo['h'] != 6:
            continue
        VD = AI.nullspace(AI.nullspace([list(x) for x in geo['V']])
                          + [[sum(A[i][k] * y[i] for i in range(n)) for k in range(n)]
                             for y in AI.nullspace([list(x) for x in geo['H']])])
        VDH = AI.nullspace(AI.nullspace([list(x) for x in VD])
                           + AI.nullspace([list(x) for x in geo['H']]))
        if len(VDH) < 1:
            continue
        return A, C, L0, geo, VDH
    return None


def restrict_lines(K, t, m):
    r"""$K'=\{p\in K:\ \iota_t p=0\}$，其中 $(\iota_t p)_i=\sum_j p_{ij}t_j$（即 $t\subseteq U_p$）。"""
    idx = BV.index_map(m)
    rows = []
    for i in range(m):
        row = [Fr(0)] * len(BV.pairs(m))
        for j in range(m):
            if i == j:
                continue
            ij = (i, j) if i < j else (j, i)
            sgn = Fr(1) if i < j else Fr(-1)
            row[idx[ij]] += sgn * t[j]
        if any(x != 0 for x in row):
            rows.append(row)
    # 把约束作用在 K 上：p = sum c_k K_k，要求 rows · p = 0
    M = [[sum(rows[a][i] * K[k][i] for i in range(len(K[0]))) for k in range(len(K))]
         for a in range(len(rows))]
    null = AI.nullspace(M) if M else [[Fr(1) if i == k else Fr(0) for i in range(len(K))]
                                      for k in range(len(K))]
    return [[sum(null[s][k] * K[k][i] for k in range(len(K))) for i in range(len(K[0]))]
            for s in range(len(null))]


def main():
    rng = random.Random(20261101)
    got = try_instance(rng)
    if got is None:
        print('没找到满足条件的实例——**这不是"不存在"**，只是搜索预算用完了；需要换构造方式')
        return
    A, C, L0, geo, VDH = got
    n, p = geo['n'], geo['p']
    w, v, h = geo['w'], geo['v'], geo['h']
    print(f'实例：n={n} p={p} w={w} v={v} h={h} dim(V∩D∩H)={len(VDH)}')
    s_m = 5
    s = h - s_m
    q = v - s
    d = w - q
    r = d - s
    t = v - s
    wm = w - s
    print(f'     s={s} q={q} d={d} r={r} t={t} m={s_m} w_m={wm}  方阵: {r + t == wm}  q=t: {q == t}')
    assert r == 2 and s_m == 5 and q == t and r + t == wm

    # S 的候选（Gr(1, V∩D∩H)）
    S_list = []
    for coef in range(len(VDH)):
        for c in (1, -1, 2):
            S_list.append([[c * x for x in VDH[coef]]])
    print(f'    S 的候选：{len(S_list)} 个')

    n_true = 0
    n_adm_tot = 0
    n_wit_true = 0
    for S in S_list:
        st = CS.setup(A, C, L0, q, S)
        # 适配基：H/S → span(e_1..e_m)
        cols = CS.pencil_cols(A, st)
        P0 = [[cols[j][0][i] for j in range(t)] for i in range(wm)]
        P1 = [[cols[j][1][i] for j in range(t)] for i in range(wm)]
        T = CS.adapted_basis(st)
        Ti = CS._invert(T)
        a, (Pn0, Pn1), info = CS.coeff_forms_full(A, C, L0, q, S)
        aE, idxE = CS.restrict_to_E(a, info['idxs'], s_m)
        forms = [aE[j] for j in range(1, len(aE)) if any(aE[j])]
        K = AI.nullspace(forms) if forms else [[Fr(1) if i == k else Fr(0)
                                                for k in range(len(idxE))] for i in range(len(idxE))]
        if not K:
            print(f'  S={S[0][:2]}...: K=0 ⟹ 不可行')
            continue
        # T_S（在 E 坐标里）：A(S)/S
        TS = []
        for x in S:
            Ax = [sum(A[i][k] * x[k] for k in range(n)) for i in range(n)]
            c = CS._solve_in_basis(st['WB'], Ax)[st['s']:]
            tv = [sum(Ti[i][k] * c[k] for k in range(wm)) for i in range(wm)]
            if any(tv[:s_m]):
                TS.append(tv[:s_m])
        Kp = restrict_lines(K, TS[0], s_m) if TS else K
        verdict, wit, binfo = BV.has_decomposable(Kp, s_m)
        # G/S（在适配基的 E 坐标里）
        GS = []
        for g in geo['G']:
            c = CS._solve_in_basis(st['WB'], g)[st['s']:]
            gv = [sum(Ti[i][k] * c[k] for k in range(wm)) for i in range(wm)]
            if any(gv[:s_m]):
                GS.append(gv[:s_m])
        rkG = AI.rank(GS) if GS else 0
        # 对照：只枚举**包含 T_S** 的 U（否则 RREF 枚举几乎撞不到给定直线）
        comp = []
        for i in range(s_m):
            e = [Fr(1) if k == i else Fr(0) for k in range(s_m)]
            if not TS or AI.rank([TS[0]] + comp + [e]) > 1 + len(comp):
                comp.append(e)
        n_adm = n_true_S = 0
        for coefs in itertools.product((-1, 0, 1), repeat=len(comp)):
            if all(c == 0 for c in coefs):
                continue
            w = [sum(Fr(coefs[j]) * comp[j][k] for j in range(len(comp))) for k in range(s_m)]
            U = ([TS[0]] if TS else []) + [w]
            if len(U) != r or AI.rank(U) != r:
                continue
            if rkG and AI.rank(GS + U) != rkG + r:
                continue
            n_adm += 1
            Ucols = [[U[i][k] if k < s_m else Fr(0) for k in range(wm)] for i in range(r)]
            Q = PS.make_pencil(Ucols, Pn0, Pn1)
            if PS.full_col_rank_constant(Q)[0]:
                n_true_S += 1
        n_adm_tot += n_adm
        n_true += n_true_S
        # 若 bivector 给了有理见证：直接还原 U 并检验（闭环）
        wcheck = '无见证'
        if wit is not None:
            Uw = BV.subspace_from_plucker(wit, s_m)
            if len(Uw) != r:
                wcheck = f'见证的 U 维数 {len(Uw)} != r（不该发生）'
            else:
                okG = (not rkG) or (AI.rank(GS + Uw) == rkG + r)
                Ucols = [[Uw[i][k] if k < s_m else Fr(0) for k in range(wm)] for i in range(r)]
                Qw = PS.make_pencil(Ucols, Pn0, Pn1)
                okdet = PS.full_col_rank_constant(Qw)[0]
                wcheck = f'见证: U∩G/S=0?{okG} det常数?{okdet}'
                if okdet and okG:
                    n_wit_true += 1
        elif binfo.get('gcd_deg'):
            wcheck = f'gcd 次数={binfo["gcd_deg"]}（无有理根 ⟹ 见证在代数扩张里，闭环未做）'
        print(f'  S[0]={[str(x) for x in S[0][:2]]}...  dimK={len(K)} dimK\'={len(Kp)} '
              f'判定={verdict} ({binfo.get("reason")}); 可容许U={n_adm} 直接det通过={n_true_S}; {wcheck}')
        if verdict is False and n_true_S > 0:
            print('    !! 判定 False 但直接 det 有通过——矛盾')
    print(f'\n汇总：S {len(S_list)} 个；可容许 U 共 {n_adm_tot}；直接 det 通过 {n_true}；'
          f'有理见证闭环通过 {n_wit_true}')
    print('说明：直接 det 通过 = 该 U 的 (S) 成立；有理见证闭环 = 由见证还原出的 U 直接验过 det 常数。')


if __name__ == '__main__':
    main()
