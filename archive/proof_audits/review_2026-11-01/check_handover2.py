r"""HANDOVER2 的独立核对脚本（2026-11-01 接手者）。

只做三件事（全部精确有理算术）：
1. 核对 A2 §40.1 / 支4 §3 的两个维数等式：
   - `r+t = w-q`（**应为假**；反例 c282）
   - `r+t = w-s  <=>  q = t`（**应为真**）
   并核对 支4 §3(4) 的 `r = w-v`（**应为假**）。
2. 复刻 c300_g3_check 的随机过滤，统计"能进入系数判据"的实例里 q 与 t 的关系：
   - 若 q != t 恒成立，则支5 的 58 例都**不在** §40 的方阵适用域里。
3. 对一个方阵实例，比较两个 `a_j`：
   - `coeff_of_S.coeff_forms_of_S`（用 m 行、q=m-r 列）
   - `verify_det_identity` 用的全行版（wm 行、t 列）
   若两者给出的多项式不同，则 `coeff_forms_of_S` **不是** §41 已验证的那个对象。

用法：python workspace/review_2026-11-01/check_handover2.py
"""
import itertools
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))
sys.path.insert(0, os.path.join(_ROOT, 'workspace', 'A3_basefamily', 'scripts'))

import audit_independent as AI
import coeff_of_S as CS_
import coeff_space as CS2
import spectral_gcd as SG
import base_sweep as BS


def unit(n, i):
    return [Fr(1) if k == i else Fr(0) for k in range(n)]


# ---------------- 实例 ----------------
def c282():
    n = 8
    C = [unit(n, 0), unit(n, 1)]
    L0 = [unit(n, 2)]
    A = [[Fr(0)] * n for _ in range(n)]
    for (i, j) in [(0, 2), (1, 3), (4, 4), (3, 5), (5, 6), (6, 7)]:
        A[i][j] = Fr(1)
    return A, C, L0


def second():
    n = 6
    C = [unit(n, 0)]
    A = [[Fr(0)] * n for _ in range(n)]
    for (i, j) in [(0, 5), (2, 2), (3, 3), (1, 1), (4, 4)]:
        A[i][j] = Fr(1)
    L0 = [unit(n, 1)]
    return A, C, L0


def dims(A, C, L0, q, S):
    st = CS_.setup(A, C, L0, q, S)
    v = len(st['V'])
    wm = st['w'] - st['s']
    t = v - st['s']
    r = st['d'] - st['s']
    return st, dict(w=st['w'], s=st['s'], d=st['d'], m=st['m'], wm=wm,
                    r=r, t=t, q=q, v=v)


def part1():
    print('=' * 78)
    print('PART 1：维数等式')
    A, C, L0 = c282()
    for q, S, label in [(4, [unit(8, 4)], 'c282 q=4 s=1')]:
        _st, D = dims(A, C, L0, q, S)
        print(f'{label}: w={D["w"]} s={D["s"]} v={D["v"]} d={D["d"]} '
              f'r={D["r"]} t={D["t"]} wm={D["wm"]} m={D["m"]}')
        print(f'  r+t = {D["r"] + D["t"]}；w-q = {D["w"] - q}；w-s = {D["wm"]}')
        print(f'  [断言] r+t = w-q ？ {D["r"] + D["t"] == D["w"] - q}'
              f'   ← A2 §40.1/支4 §3(1) 声称恒等')
        print(f'  [断言] (r+t=w-s) <=> (q=t) ？ '
              f'{(D["r"] + D["t"] == D["wm"]) == (q == D["t"])}')
        print(f'  [断言] r = w-v ？ {D["r"] == D["w"] - D["v"]}'
              f'   ← 支4 §3(4)/A2 §41.8 的写法')
        print(f'  （r={D["r"]}，w-v={D["w"] - D["v"]}）')

    A, C, L0 = second()
    for q, S, label in [(2, [unit(6, 2), unit(6, 3)], '第二实例 q=2 s=2'),
                        (3, [unit(6, 2)], '第二实例 q=3 s=1')]:
        _st, D = dims(A, C, L0, q, S)
        print(f'{label}: r={D["r"]} t={D["t"]} wm={D["wm"]} q={q}')
        print(f'  [断言] (r+t=w-s) <=> (q=t) ？ '
              f'{(D["r"] + D["t"] == D["wm"]) == (q == D["t"])}')


# ---------------- PART 2：c300 的适用域 ----------------
def c300_geometry(A, C, L0):
    n = len(A)
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    W = AI.nullspace([row[:] for row in C])
    H = AI.nullspace([row[:] for row in (C + L0)])
    Vt = [list(x) for x in V]
    Ht = [list(x) for x in H]
    Vperp = AI.nullspace(Vt)
    Hperp = AI.nullspace(Ht)
    G = AI.nullspace(Vperp + Hperp)
    Gperp = AI.nullspace([list(x) for x in G])
    D = AI.nullspace(Gperp + AI.mul(Hperp, A))
    return dict(n=n, w=len(W), h=len(H), v=len(V), b=len(G), dimD=len(D),
                V=V, H=H, G=G, D=D)


def liftS(coords, D, n):
    S = []
    for row in coords:
        v = [Fr(0)] * n
        for j, c in enumerate(row):
            for i in range(n):
                v[i] += Fr(c) * D[j][i]
        S.append(v)
    return S


def part2():
    print()
    print('=' * 78)
    print('PART 2：c300 的随机过滤（只有 m=r+t 的实例能真正跑通 coeff_forms_of_S）')
    rng = random.Random(20261101)
    seen = []
    dropped = 0
    n_total = 0
    n_bal = 0
    n_bal_qt = 0
    n_bal_hw = 0
    n_gt = 0
    for trial in range(1200):
        n = rng.choice([7, 8, 9])
        p = rng.choice([2, 3])
        C = [unit(n, i) for i in range(p)]
        L0 = [unit(n, p)]
        A = [[Fr(0)] * n for _ in range(n)]
        for _ in range(n):
            i = rng.randrange(n)
            j = rng.randrange(n)
            A[i][j] = Fr(rng.choice([-1, 1, 2]))
        try:
            geo = c300_geometry(A, C, L0)
        except Exception:
            continue
        if geo['h'] - geo['v'] < 2:
            continue
        s, r = 1, 2
        d = s + r
        q = geo['w'] - d
        if q < 1 or geo['dimD'] < s:
            continue
        coords = BS.enum_subspaces(geo['dimD'], s, bound=1)[:3]
        if not coords:
            continue
        for cf in coords:
            S = liftS(cf, geo['D'], n)
            try:
                a, P, info = CS_.coeff_forms_of_S(A, C, L0, q, S)
            except Exception:
                dropped += 1
                continue
            m, t = info['m'], info['t']
            n_total += 1
            if m < r + t:
                continue
            if m > r + t:
                n_gt += 1
                continue
            n_bal += 1
            if q == t:
                n_bal_qt += 1
            if geo['h'] == geo['w']:
                n_bal_hw += 1
            if len(seen) < 3:
                seen.append(dict(n=n, p=p, w=geo['w'], h=geo['h'], v=geo['v'],
                                 m=m, t=t, r=r, q=q, wm=geo['w'] - s,
                                 S=S, A=A, C=C, L0=L0, geo=geo, info=info))
    print(f'  统计（全部 1200 次 trial，每实例最多 3 个 S）：')
    print(f'    调用 coeff_forms_of_S 的 (实例,S)：{n_total}；异常/丢弃 {dropped}')
    print(f'    其中 m=r+t（§33 对象可用）：{n_bal}；m>r+t（会 IndexError）：{n_gt}')
    print(f'    在 m=r+t 里，q=t（§40 方阵域）的：{n_bal_qt}')
    print(f'    在 m=r+t 里，h=w（⟺ §33 对象 = §40 对象）的：{n_bal_hw}')
    for i, e in enumerate(seen):
        print(f'  例{i + 1}: n={e["n"]} p={e["p"]} w={e["w"]} h={e["h"]} v={e["v"]} '
              f'm={e["m"]} r={e["r"]} t={e["t"]} q={e["q"]} '
              f'| q==t ? {e["q"] == e["t"]}')
    if seen:
        audit_admissible(seen[0])
    return seen


def audit_admissible(e):
    """c300 的内层：D_adm=0 到底是"K 里没有可分解点"还是"没有可容许 U"？"""
    A, C, L0, S, geo, info = e['A'], e['C'], e['L0'], e['S'], e['geo'], e['info']
    n, m, r = e['n'], e['m'], e['r']
    st = CS_.setup(A, C, L0, e['q'], S)
    rows = info['rows']
    # K_S（§33 对象）
    a, _P, _i = CS_.coeff_forms_of_S(A, C, L0, e['q'], S)
    forms = [a[j] for j in range(1, len(a)) if any(x != 0 for x in a[j])]
    dimK = len(a[0]) - (AI.rank(forms) if forms else 0)
    # T_S、G/S 的坐标（与 c300 相同：投到 rows 上）
    TSc = []
    for sv in S:
        av = [sum(A[i2][k] * sv[k] for k in range(n)) for i2 in range(n)]
        full = CS_._solve_in_basis(st['WB'], av)[st['s']:]
        TSc.append([full[i2] for i2 in rows])
    rkT = AI.rank(TSc) if TSc else 0
    Gc = []
    for g in geo['G']:
        full = CS_._solve_in_basis(st['WB'], g)[st['s']:]
        Gc.append([full[i2] for i2 in rows])
    rkG = AI.rank(Gc) if Gc else 0
    # 枚举并计数
    n_adm = n_inK = 0
    pts = []
    for basis in BS.enum_subspaces(m, r, bound=1):
        U = [[Fr(c) for c in row] for row in basis]
        if AI.rank(U) != r:
            continue
        if rkT and AI.rank(U + TSc) > r:
            continue
        if rkG and AI.rank(Gc + U) != rkG + r:
            continue
        n_adm += 1
        # 用 c300 的 Plücker 约定
        import c300_g3_check as C3
        pU = C3.plucker_coords(U, m)
        if forms and any(sum(forms[t][k] * pU[k] for k in range(len(pU))) != 0
                         for t in range(len(forms))):
            continue
        n_inK += 1
        pts.append(pU)
    dimD = AI.rank(pts) if pts else 0
    print()
    print(f'  [例1 内层] dim K_S={dimK}；可容许 U 总数={n_adm}；'
          f'其中 p_U∈K_S 的={n_inK}；dim D_adm={dimD}')
    print('   → 若"可容许 U 总数"=0，则 D_adm=0 不能解释成"K 里全是不可分解点"。')


def _plucker_idx(m, r):
    return list(itertools.combinations(range(m), r))


# ---------------- PART 3：m 行 a_j vs 全行 a_j ----------------
def poly_det_full(u, cols, wm, t):
    P = []
    for i in range(wm):
        row = [[u[i]]]
        row += [[cols[j][0][i], cols[j][1][i]] for j in range(t)]
        P.append(row)
    return SG.pdet(P)


def part3():
    print()
    print('=' * 78)
    print('PART 3：coeff_forms_of_S（m 行） vs 全行恒等式（wm 行）')
    A, C, L0 = second()
    q, S = 2, [unit(6, 2), unit(6, 3)]
    st, D = dims(A, C, L0, q, S)
    cols = CS_.pencil_cols(A, st)
    wm, m, r, t = D['wm'], D['m'], D['r'], D['t']
    print(f'  第二实例 q=2 s=2: wm={wm}, m={m}, r={r}, t={t}')
    a_old, _P, info = CS_.coeff_forms_of_S(A, C, L0, q, S)
    print(f'  coeff_forms_of_S: 返回 {len(a_old)} 个 a_j，每个长度 {len(a_old[0])}'
          f'（i.e. 用 {info["m"]} 行、q=m-r={info["m"] - info["r"]} 列）')
    P0 = [[cols[j][0][i] for j in range(t)] for i in range(wm)]
    P1 = [[cols[j][1][i] for j in range(t)] for i in range(wm)]
    a_full, idxs = CS2.coeff_forms([P0, P1], wm, r)
    print(f'  全行版: {len(a_full)} 个 a_j，每个长度 {len(a_full[0])}（=C({wm},{r})）')
    rng = random.Random(7)
    diff = 0
    for trial in range(5):
        u_m = [Fr(rng.randint(-2, 2)) for _ in range(m)]
        u_wm = [Fr(rng.randint(-2, 2)) for _ in range(wm)]
        # 旧的 q_U(λ)（m 行）
        q_old = [sum(a_old[j][k] * u_m[k] for k in range(m))
                 for j in range(len(a_old))]
        # 全行 det（wm 行）
        q_true = poly_det_full(u_wm, cols, wm, t)
        print(f'    u_m={[str(x) for x in u_m]}  u_wm={[str(x) for x in u_wm]}')
        print(f'      q_old (deg {len(q_old) - 1}) = {[str(x) for x in q_old]}')
        print(f'      q_true(deg {SG.pdeg(q_true)}) = {[str(x) for x in q_true]}')
        if len(q_old) != len(q_true) or any(
                q_old[j] != q_true[j] for j in range(min(len(q_old), len(q_true)))):
            diff += 1
    print(f'  5 组随机 u 中，两个多项式**逐系数不同**的有 {diff} 组')
    print('  注：q_old 只依赖前 m 个 Plücker 坐标、且只用了 q=m-r 列；'
          'q_true 依赖全部 wm 个坐标。两者不是同一个对象。')


def main():
    part1()
    part2()
    part3()
    print()
    print('=' * 78)
    print('结论见 HANDOVER2.md §3；本脚本只打印事实，不做推断。')


if __name__ == '__main__':
    main()
