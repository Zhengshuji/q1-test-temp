"""joint_theta.py —— 只在 $\\theta$ 上做消元：把 $(5a)$ 与 $(5b)$ 都化成 $\\theta$ 的**行列式条件**

**问题**：`joint_system.py` 把辅助矩阵 $T$ 与 Bézout 系数 $u$ 都当变量，$(5a)+(5b)$ 的 Gröbner 在 50+ 变量上不可行。

**关键**：$T$ 与 $u$ 都是**线性**出现的，所以可以在**有理函数域 $\\mathbb Q(\\theta)$** 上做线性消元，
只留下 $\\theta$ 的行列式条件：

* $(5a)$：$A^{\\mathsf T}X_c=B_aT$ 可解 $\\iff \\operatorname{rank}B_a=\\operatorname{rank}[B_a\\mid A^{\\mathsf T}X_c]$
  $\\iff$ 所有 $(r_a+1)$-子式为零（$r_a=\\operatorname{rank}B_a$ 的典型值）；
* $(5b)$：$e_0\\in\\operatorname{col}M_\\rho$ $\\iff \\operatorname{rank}M_\\rho=\\operatorname{rank}[M_\\rho\\mid e_0]$
  $\\iff$ 所有 $(r_M+1)$-子式为零（$r_M=\\operatorname{rank}M_\\rho$ 的典型值）；
* 另有层条件：所有 $(\\rho+1)$-子式 of $[V|Z]$ 为零。

于是**全部是 $\\theta$ 的多项式**，Gröbner 只在 $1$–$3$ 个变量上做 ⟹ 便宜。
代价（诚实标注）：这只覆盖**典型层**（各秩取典型值）；秩跌落点需另做（见 attempts/48）。

用法：python -u tools/verification/joint_theta.py
"""

import os
import sys
import itertools
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import consistency_checks as CC           # noqa: E402
import chart_gcd_analysis as CGA          # noqa: E402
import decide_symbolic as DS              # noqa: E402
import rank_stratified as RS              # noqa: E402
import joint_system as JS                 # noqa: E402

F = Fraction
CAP = 40


def gen_rank(M, tam, samples=(-2, -1, 0, 1, 2)):
    best = 0
    for t in samples:
        sub = dict(zip(tam, [sp.Integer(t)] * len(tam)))
        try:
            best = max(best, M.subs(sub).rank())
        except Exception:                        # noqa: BLE001
            pass
    return best


def minors_of(M, size, cap=CAP):
    out = []
    if size <= 0 or size > min(M.rows, M.cols):
        return out
    for rs in itertools.combinations(range(M.rows), size):
        for cs in itertools.combinations(range(M.cols), size):
            d0 = sp.expand(M[list(rs), list(cs)].det())
            if d0 != 0:
                out.append(d0)
                if len(out) >= cap:
                    return out
    return out


def analyse_chart(A, C, L0, q, rows):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    tam = CGA.chart_symbols(d, k)
    if not tam:
        # 常数图卡：没有图表参数 ⟹ Z 唯一（d=0 时为空，d=k 时 Z=K），直接构造并核验
        if d == k:
            Z = [list(x) for x in Kc]
        elif d == 0:
            Z = [[] for _ in range(n)]
        else:
            return 'UNKNOWN', f'常数图卡（d={d}, k={k}）', None
        if d > 0 and ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            return 'INFEASIBLE', '常数图卡：Z 的秩不足', None
        L = ZG.L_from_Z(A, C, L0, Z, q)
        if L is None:
            return 'INFEASIBLE', '常数图卡：无法构造 L', None
        if not LQ.condA(A, C, L):
            return 'INFEASIBLE', '常数图卡：$(5a)$ 失败（唯一的 Z 不可容许）', None
        if TC.analyse(A, C, L)['five_b']:
            CC.check_candidate(A, C, L0, L, tag=f'q={q} 常数图卡', verbose=False)
            return 'FEASIBLE', '常数图卡：唯一的 Z 通过 (5a)+(5b)+七条检查', L
        return 'INFEASIBLE', '常数图卡：$(5b)$ 失败（唯一的 Z 谱不可行）', None
    Xc, Ba, Wrows = JS.build_chart(A, C, L0, q, rows, tam)
    VZ, Z, Vsym = RS.VZ_matrix(A, C, L0, q, rows, tam)
    Asym = CGA.to_sym(A)
    M_a = (Asym.T * Xc).row_join(Ba)
    ra = gen_rank(Ba, tam)
    rho = gen_rank(VZ, tam)
    conds = []
    conds += minors_of(M_a, ra + 1)                 # (5a)：rank M_a = rank B_a
    conds += minors_of(VZ, rho + 1)                 # 层：rank[V|Z] = rho
    mins, lam = RS.pen_minors(A, C, L0, q, rows, tam, rho)
    if not mins or len(mins) > CAP:
        return 'UNKNOWN', f'ρ-子式过多/为空（{len(mins)}）', None
    D = max(sp.degree(m, lam) for m in mins)
    if D == 0:
        return 'UNKNOWN', 'D=0', None
    M, e0 = RS.coeff_matrix_from_minors(mins, lam, D)
    Aug = M.row_join(e0)
    rM = gen_rank(M, tam)
    if rM >= Aug.rows:
        conds_b = []                                # 满行秩 ⟹ e0 自动在列空间
    else:
        conds_b = minors_of(Aug, rM + 1)            # (5b)：rank[M|e0] = rank M
    conds = [sp.expand(x) for x in conds + conds_b if sp.expand(x) != 0]
    if not conds:
        # 无任何条件 ⟹ 两个判据都自动成立 ⟹ 取一点验证即为见证
        for th in ([F(0)], [F(1)], [F(-1)], [F(1, 2)]):
            if len(tam) != len(th):
                break
            Zt = DS.Z_from_theta(A, C, L0, q, rows, th)
            if ZG.bool_rank(ZG.cols_to_rows(Zt)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Zt, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            if TC.analyse(A, C, L)['five_b']:
                CC.check_candidate(A, C, L0, L, tag=f'q={q} theta={th}', verbose=False)
                return 'FEASIBLE', f'无约束（ra={ra}, ρ={rho}, rM={rM}）⟹ 处处可行，θ={th}', L
        return 'UNKNOWN', f'无多项式条件（ra={ra}, ρ={rho}, rM={rM}）但未取到见证', None
    try:
        G = sp.groebner(conds, *tam, order='grevlex')
        els = list(G.exprs)
    except Exception as e:                          # noqa: BLE001
        return 'UNKNOWN', f'Gröbner 失败：{e}', None
    info = f'ra={ra} ρ={rho} rM={rM}，条件 {len(conds)} 条，基长 {len(els)}'
    if els == [sp.Integer(1)]:
        return 'INFEASIBLE_TYPICAL', f'{info}：理想 =(1) ⟹ 典型层无可行 θ', None
    # 非空：尝试取有理点
    for sol in sp.solve(conds, tam, dict=True):
        if all(s in sol for s in tam) and all(sp.simplify(sol[s]).is_rational for s in tam):
            th = [F(int(sp.Rational(sol[s]).p), int(sp.Rational(sol[s]).q)) for s in tam]
            Zt = DS.Z_from_theta(A, C, L0, q, rows, th)
            if ZG.bool_rank(ZG.cols_to_rows(Zt)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Zt, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            if TC.analyse(A, C, L)['five_b']:
                CC.check_candidate(A, C, L0, L, tag=f'q={q} theta={th}', verbose=False)
                return 'FEASIBLE', f'{info}，θ={th}', L
    return 'UNKNOWN', f'{info}：非空但未取到有理见证（基={[sp.factor(e) for e in els][:3]}）', None


def decide(A, C, L0, q):
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    if d < 0 or d > k:
        return 'UNKNOWN', 'd 越界', None
    outs = []
    for rows in itertools.combinations(range(k), d):
        v, why, w = analyse_chart(A, C, L0, q, rows)
        outs.append((rows, v, why))
        if v == 'FEASIBLE':
            return v, f'图卡 {rows}：{why}', w
    if outs and all(v in ('INFEASIBLE', 'INFEASIBLE_TYPICAL') for _, v, _ in outs):
        complete = all(v == 'INFEASIBLE' for _, v, _ in outs)
        return ('INFEASIBLE' if complete else 'INFEASIBLE_TYPICAL'), \
            '；'.join(f'{rr}:{yy}' for rr, _, yy in outs), None
    return 'UNKNOWN', '；'.join(f'{rr}:{vv}:{yy[:60]}' for rr, vv, yy in outs), None


def sweep(maxn=40):
    from collections import Counter
    stats = Counter()
    rows = []
    done = 0
    for n in (5, 6):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3010):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    v, why, w = decide(A, C, L0, q0)
                    stats[v] += 1
                    rows.append((n, p, r, seed, q0, v))
                    print(f'n={n} p={p} r={r} seed={seed} q0={q0}: {v}')
                    done += 1
                    if done >= maxn:
                        print('统计：', dict(stats))
                        return rows
    print('统计：', dict(stats))
    return rows


def main():
    import importlib.util as iu
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, _ = V4.build()
    print(f'C4 q0={q04}：')
    v, why, w = decide(A4, C4m, L04, q04)
    print(f'  → {v}：{why[:180]}')
    cases = [(5, 2, 1, 3023), (6, 2, 2, 3027), (5, 1, 2, 3003)]
    if '--sweep' in sys.argv:
        sweep(int(sys.argv[sys.argv.index('--sweep') + 1]) if '--sweep' in sys.argv and sys.argv[-1].isdigit() else 40)
        return
    for (n, p, r, seed) in cases:
        made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
        if made is None:
            continue
        A, C, L0 = made
        O = QR.observability_matrix(A, C)
        if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
            continue
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        print(f'n={n} p={p} r={r} seed={seed} q0={q0}：')
        v, why, w = decide(A, C, L0, q0)
        print(f'  → {v}：{why[:180]}')
        if w:
            print('   见证首行：', [str(x) for x in w[0]])


if __name__ == '__main__':
    main()
