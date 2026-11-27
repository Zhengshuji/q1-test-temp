"""layer_min_affine.py —— 比较实验：线性条件 vs 线性+行列式条件（精确有理算术）

问题（Workstream A，attempts/10 §6.5）：
  在一个图卡内，把 U 参数化为 G(Θ) = [I_ρ ; Θ]（行按图卡 I 重排）。
  - A_lin : 只要求 U_0 ⊆ im G(Θ)（**线性**方程）
  - A_full: 再要求 T U ⊆ U + B（等价于 rank[T G, G, B] = rank[G, B]，**行列式**条件）
  问：A_lin = A_full 吗？若否，给出**精确反例点**（一个 Θ + 某个非零子式）。

谨慎约定：
  * 全部有理数精确运算；
  * 采样只能"反驳"（找到反例），永远不算"确认"；
  * 每个结论都打印被检验的量；不打印"已验证等价"这种话。

用法：python tools/verification/layer_min_affine.py
"""

import itertools
import os
import sys
from fractions import Fraction

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
from min_layer_closure import (  # noqa: E402
    rref, rank, span_basis, matvec, mul, quotient_data, closure, unit,
)


# ---------------------------------------------------------------- 图卡与 G(Θ)


def chart_G(d, rho, chart, theta):
    """按图卡 chart（长度 rho、升序）构造 d×rho 的 G(Θ)；theta 是 (d,rho) 的字典 (i,j)->值。"""
    G = [[Fraction(0)] * rho for _ in range(d)]
    for j, i in enumerate(chart):
        G[i][j] = Fraction(1)
    for i in range(d):
        if i in chart:
            continue
        for j in range(rho):
            G[i][j] = theta.get((i, j), Fraction(0))
    return G


def linear_conditions(d, rho, chart, U0):
    """U_0 ⊆ im G(Θ) 的线性方程：对每个 u0，sum_j theta[i,j]*u0[chart[j]] = u0[i]（i 不在图卡）。

    返回 (rows, rhs, vars)：每行是 vars 上的系数。不相容由调用方（rref）处理。
    """
    vars_ = [(i, j) for i in range(d) if i not in chart for j in range(rho)]
    vidx = {v: k for k, v in enumerate(vars_)}
    rows, rhs = [], []
    for u0 in U0:
        for i in range(d):
            if i in chart:
                continue
            row = [Fraction(0)] * len(vars_)
            for j in range(rho):
                c = u0[chart[j]]
                if c != 0:
                    row[vidx[(i, j)]] += c
            rows.append(row)
            rhs.append(u0[i])
    return rows, rhs, vars_


def solve_affine(rows, rhs, vars_):
    """解线性方程组；返回 (particular, nullspace 基) 或 None（不相容）。"""
    m, k = len(rows), len(vars_)
    if m == 0:
        return {v: Fraction(0) for v in vars_}, []
    aug = [rows[i] + [rhs[i]] for i in range(m)]
    R, piv = rref(aug)
    for row in R:
        if all(row[c] == 0 for c in range(k)) and row[k] != 0:
            return None
    piv_cols = [p for p in piv if p < k]
    free = [c for c in range(k) if c not in piv_cols]
    part = {vars_[c]: Fraction(0) for c in range(k)}
    for r_i, p in enumerate(piv_cols):
        part[vars_[p]] = R[r_i][k]
    null = []
    for f in free:
        v = {name: Fraction(0) for name in vars_}
        v[vars_[f]] = Fraction(1)
        for r_i, p in enumerate(piv_cols):
            v[vars_[p]] = -R[r_i][f]
        null.append(v)
    return part, null


def det_condition_ok(T, B, G, rho, verbose=False):
    """检查 T U ⊆ U + B：rank[TG, G, B] == rank[G, B]。"""
    TG = [[matvec(T, [G[i][j] for i in range(len(G))])[r] for j in range(rho)]
          for r in range(len(T))]
    # 注意 matvec(T, g_j) 给的是列；用列拼接
    TG = [[sum(T[r][i] * G[i][j] for i in range(len(G))) for j in range(rho)]
          for r in range(len(T))]
    Bcols = [[B[k][r] for k in range(len(B))] for r in range(len(B[0]))] if B else []
    Bl = len(B)
    cols = []
    for j in range(rho):
        cols.append([TG[r][j] for r in range(len(T))])
    for j in range(rho):
        cols.append([G[r][j] for r in range(len(T))])
    for b in B:
        cols.append([b[r] for r in range(len(T))])
    Mat = [[cols[j][r] for j in range(len(cols))] for r in range(len(T))]
    GB = [[G[r][j] for j in range(rho)] + [B[k][r] for k in range(Bl)] for r in range(len(G))]
    r1 = rank(Mat)
    r2 = rank(GB)
    if verbose:
        print(f'      rank[TG,G,B]={r1}, rank[G,B]={r2}')
    return r1 == r2


def analyse(T, B, U0, name, n_random=6, seed=0):
    d = len(T)
    Ustar = closure(T, B, U0, verbose=False)
    rho = len(Ustar)
    print(f'  d={d}, rho=rho_ci={rho}, dim B={len(B)}, dim U0={len(U0)}')
    if rho == 0:
        print('  rho=0：层退化，跳过')
        return
    rng = []
    for chart in itertools.combinations(range(d), rho):
        rows, rhs, vars_ = linear_conditions(d, rho, chart, U0)
        sol = solve_affine(rows, rhs, vars_)
        if sol is None:
            print(f'  图卡 {chart}: 线性条件不相容（U_0 不在该图卡的 U 里）')
            rng.append((chart, 'infeasible', None))
            continue
        part, null = sol
        G = chart_G(d, rho, chart, part)
        ok = det_condition_ok(T, B, G, rho)
        print(f'  图卡 {chart}: 线性解集维数={len(null)}，特解处 det 条件 {"成立" if ok else "不成立"}')
        rng.append((chart, 'feasible', (part, null, ok)))
        if not ok:
            print(f'    >>> 反例证书：Θ={ {k: str(v) for k, v in part.items()} }（该点满足线性条件，违反 T U ⊆ U+B）')
        # 在解集上采样（只能反驳）
        for s in range(n_random):
            th = dict(part)
            for k, v in enumerate(null):
                c = Fraction((s * 7 + k * 13 + 1) % 11 - 5, 3)  # 确定性的"伪随机"有理数
                for name_, val in v.items():
                    th[name_] = th.get(name_, Fraction(0)) + c * val
            Gs = chart_G(d, rho, chart, th)
            if not det_condition_ok(T, B, Gs, rho):
                print(f'    >>> 反例证书（采样点 s={s}）：该点满足线性条件，违反 T U ⊆ U+B')
                break
        else:
            print(f'    解集上 {n_random} 个有理点都满足 det 条件（**不是**确认，只是没找到反例）')
    return rng


def main():
    print('=== 实例 1：R17-like ===')
    A1 = [[Fraction(0)] * 5 for _ in range(5)]
    for i in range(5):
        A1[i][i] = Fraction(i)
    A1[0][1] = Fraction(1)
    analyse(*quotient_data(A1, [unit(5, 0)], [unit(5, 2)])[:3], name='R17-like')

    print('=== 实例 2：second ===')
    A2 = [[Fraction(0)] * 6 for _ in range(6)]
    for i in range(4):
        A2[i][i] = Fraction(1)
    A2[5][5] = Fraction(1)
    A2[0][5] = Fraction(1)
    analyse(*quotient_data(A2, [unit(6, 0)], [unit(6, 1)])[:3], name='second')

    print('=== 合成数据（不是某个 (A,C,L0) 的商数据）：d=4, rho=3, B=0, U0=span{e0} ===')
    print('    目的：让线性解集**正维**，才能检验"线性条件是否蕴含行列式条件"')
    T = [[Fraction(0)] * 4 for _ in range(4)]
    T[1][0] = Fraction(1)   # e0 -> e1
    T[2][1] = Fraction(1)   # e1 -> e2
    analyse(T, [], [[Fraction(1), Fraction(0), Fraction(0), Fraction(0)]], name='synthetic')

    print('=== 实例 3：chain ===')
    A3 = [[Fraction(0)] * 4 for _ in range(4)]
    for i in range(3):
        A3[i][i + 1] = Fraction(1)
    analyse(*quotient_data(A3, [unit(4, 0)], [unit(4, 3)])[:3], name='chain')





# ---------------------------------------------------------------- 秩分层（专家 2026-11-02 §1.2）


def rank_GB(G, B, d, rho):
    """k(Θ) = rank[G, B]。"""
    Bl = len(B)
    cols = [[G[r][j] for r in range(d)] for j in range(rho)]
    for b in B:
        cols.append([b[r] for r in range(d)])
    Mat = [[cols[j][r] for j in range(len(cols))] for r in range(d)]
    # 去掉全零列后取秩
    nz = [c for c in cols if any(x != 0 for x in c)]
    if not nz:
        return 0
    M2 = [[nz[j][r] for j in range(len(nz))] for r in range(d)]
    return rank(M2)


def expert_counterexample():
    """专家 §1.2 的反例：d=2, B=span{e1}, T e1 = e2, U_t = span{e1 + t e2}。

    预期：t != 0 时 U_t + B = R^2 ⟹ T U_t ⊆ U_t + B 自动成立；
          t = 0 时 U_0 = B，T B = span{e2} 不在 B 里 ⟹ 失败。
    于是可行集 = {t != 0} —— **开集**，不是闭的。
    """
    print('=== 专家反例（§1.2）：可行集是开的 ===')
    d, rho = 2, 1
    # 列约定：T·e1 = e2 写作 T = [[0,0],[1,0]]
    T = [[Fraction(0), Fraction(0)], [Fraction(1), Fraction(0)]]
    B = [[Fraction(1), Fraction(0)]]                             # B = span{e1}
    chart = (0,)
    got = []
    for t in [Fraction(0), Fraction(1), Fraction(-2), Fraction(3, 2)]:
        th = {(1, 0): t}
        G = chart_G(d, rho, chart, th)
        ok = det_condition_ok(T, B, G, rho)
        k = rank_GB(G, B, d, rho)
        got.append((t, k, ok))
        print(f'  t={t}: rank[G,B]={k}, T U ⊆ U+B: {ok}')
    # 由数据断言预期模式（t=0 失败、t!=0 成功），而不是硬编码结论
    d0 = [g for g in got if g[0] == 0][0]
    dn = [g for g in got if g[0] != 0]
    assert d0[2] is False, 't=0 应当失败（TB 不在 B 里）'
    assert all(g[2] for g in dn), 't!=0 应当成功（U+B = 全空间）'
    print('  数据断言成立：t=0 失败、t≠0 成功 ⟹ 可行集 = {t≠0} 在仿射直线里是**开集**（补一个点）。')
    print('  ⟹ A_min 是**可构造集**（constructible），不是单个闭簇；必须按 rank[G,B] 分层描述。')


def stratify(T, B, U0, chart, samples=(-1, 0, 1, Fraction(1, 2))):
    """在给定图卡内按 k=rank[G,B] 分层，统计每层的可行/不可行。"""
    d = len(T)
    rho = len(chart)
    rows, rhs, vars_ = linear_conditions(d, rho, chart, U0)
    sol = solve_affine(rows, rhs, vars_)
    if sol is None:
        print(f'  图卡 {chart}: 线性条件不相容')
        return
    import itertools
    part, null = sol
    by_k = {}
    for cs in itertools.product(samples, repeat=len(null)):
        th = dict(part)
        for c, vec in zip(cs, null):
            for k_, v_ in vec.items():
                th[k_] = th.get(k_, Fraction(0)) + c * v_
        G = chart_G(d, rho, chart, th)
        k = rank_GB(G, B, d, rho)
        ok = det_condition_ok(T, B, G, rho)
        by_k.setdefault(k, [0, 0])
        by_k[k][0] += 1
        if ok:
            by_k[k][1] += 1
    print(f'  图卡 {chart}: 按 k=rank[G,B] 分层（每层：样本数 / 满足 det 的数）')
    for k in sorted(by_k):
        n, okn = by_k[k]
        print(f'    k={k}: {n} / {okn}')


if __name__ == '__main__':
    main()
    expert_counterexample()
