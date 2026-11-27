"""bezout_rank_test.py —— 专家的 $(*)$ 判据：Bézout 系数矩阵的秩等式（处理"跌落"）

专家的构型（2026-11-03 §6）：设 $m_1,\\dots,m_N$ 是 $P_{\\mathcal Z}(\\theta,\\lambda)$ 的极大子式，
$D=\\max_i\\deg_\\lambda m_i\\le\\dim V$。定义线性映射
$$\\Phi_\\theta:\\bigoplus_i \\mathbb C[\\lambda]_{\\le D-1}\\to\\mathbb C[\\lambda]_{\\le 2D-1},\\qquad
(u_i)\\mapsto \\sum_i u_i m_i,$$
其系数矩阵 $M(\\theta)\\in\\mathbb C[\\theta]^{2D\\times ND}$（列 = $\\lambda^k m_i$ 的系数向量，$k<D$），
$e_0$ = 常数多项式 1 的系数向量。则
$$(5b)\\ \\text{在 }\\theta\\text{ 处成立}\\iff \\operatorname{rank}M(\\theta)=\\operatorname{rank}[M(\\theta)\\mid e_0]
\\iff e_0\\in\\operatorname{col}M(\\theta).$$

**本模块给出的证书**：取 $M(\\theta)$ 在 $\\mathbb Q(\\theta)$ 上的**左零空间**基 $y_1,\\dots,y_k$（清分母成多项式），
令 $C_j(\\theta)=y_j(\\theta)^{\\mathsf T}e_0\\in\\mathbb Q[\\theta]$。由多项式恒等式 $y_j^{\\mathsf T}M\\equiv0$：
若 $C_j(\\theta_0)\\ne0$ 则 $e_0\\notin\\operatorname{col}M(\\theta_0)$。因此
$$\\text{理想 }(C_1,\\dots,C_k)=(1)\\ \\Longrightarrow\\ \\text{**没有任何 }\\theta\\text{ 可行**}$$
（$\\mathbb C$ 上由 Nullstellensatz）。这是把"跌落"自动考虑在内的**不可行证书**。

用法：python -u tools/verification/bezout_rank_test.py
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
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import chart_gcd_analysis as CGA          # noqa: E402

F = Fraction


def build_minors(A, C, L0, q, rows, max_minors=60):
    """返回 (minors, D, syms)。minors 是 $\\mathbb Q[\\theta,\\lambda]$ 的多项式列表。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    tam = CGA.chart_symbols(d, k)
    lam = sp.symbols('lam')
    Ksym = CGA.to_sym(Kc)
    Asym = CGA.to_sym(A)
    Vsym = CGA.to_sym(V)
    W = sp.zeros(d, k)
    rest = [i for i in range(k) if i not in rows]
    for a, r0 in enumerate(rows):
        W[a, r0] = 1
    idx = 0
    for a in range(d):
        for c in rest:
            W[a, c] = tam[idx]
            idx += 1
    Z = Ksym * W.T
    P = ((lam * sp.eye(n) - Asym) * Vsym).row_join(Z)
    size = P.shape[1]
    mins = []
    for rs in itertools.combinations(range(n), size):
        m = sp.expand(P[list(rs), :].det())
        if m != 0:
            mins.append(m)
        if len(mins) >= max_minors:
            break
    D = max((sp.degree(m, lam) for m in mins), default=0)
    return mins, D, tam, lam


def coefficient_matrix(mins, D, tam, lam):
    """$M(\\theta)$：行 = $\\lambda^0..\\lambda^{2D-1}$，列 = $\\lambda^k m_i$（$k<D$）。"""
    rows_n = 2 * D
    cols = []
    for m in mins:
        poly = sp.Poly(sp.expand(m), lam)
        cdict = poly.as_dict()
        cm = [sp.expand(cdict.get((j,), sp.Integer(0))) for j in range(0, poly.degree() + 1)]
        for k in range(D):
            col = [sp.Integer(0)] * rows_n
            for j, c in enumerate(cm):
                if j + k < rows_n:
                    col[j + k] = c
            cols.append(sp.Matrix(col))
    M = sp.Matrix.hstack(*cols) if cols else sp.zeros(rows_n, 0)
    e0 = sp.Matrix([1] + [0] * (rows_n - 1))
    return M, e0


def left_null_Cs(M, tam, e0):
    """左零空间基 $y_j$（清分母）→ $C_j=y_j^{\\mathsf T}e_0$ 的多项式列表。"""
    if M.cols == 0:
        return []
    # 求 $M^{\\mathsf T} y = 0$
    MT = M.T
    ns = MT.nullspace()
    outs = []
    for yv in ns:
        # 清分母
        entries = list(yv)
        dens = [sp.denom(sp.together(e)) for e in entries]
        lcmden = sp.Integer(1)
        for dnm in dens:
            lcmden = sp.lcm(sp.expand(lcmden), sp.expand(dnm)) if tam else sp.Integer(1)
        poly = [sp.expand(sp.together(e * lcmden)) for e in entries]
        C = sp.expand(sum(p * q0 for p, q0 in zip(poly, list(e0))))
        outs.append(C)
    return outs


def rank_is_constant(A, C, L0, q, rows, size):
    """抽样检查 $\\operatorname{rank}[V|Z]$ 在该图卡上恒等于 size。"""
    import random
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    rng = random.Random(7)
    for _ in range(24):
        tv = [F(rng.randrange(-3, 4)) for _ in range(d * (k - d))]
        Z = [[0] * d for _ in range(n)]
        # 用完整 chart 参数构造
        W = [[F(0)] * k for _ in range(d)]
        rest = [i for i in range(k) if i not in rows]
        for a, r0 in enumerate(rows):
            W[a][r0] = F(1)
        idx = 0
        for a in range(d):
            for c in rest:
                W[a][c] = tv[idx]
                idx += 1
        Z = [[sum(Kc[i][t] * W[j][t] for t in range(k)) for j in range(d)] for i in range(n)]
        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            continue
        VZ = [[V[i][j] for j in range(len(V[0]))] + [Z[i][j] for j in range(d)] for i in range(n)]
        rk = LQ.rank([[VZ[i][j] for i in range(n)] for j in range(len(VZ[0]))])
        if rk != size:
            return False
    return True


def certify_chart(A, C, L0, q, rows, verbose=True):
    """返回 ('good_exists'/'certified_infeasible'/'unknown', 说明)。

    **适用条件**：$\\operatorname{rank}[V|Z]$ 在该图卡上恒定（否则需按秩做析取，未实现）。
    """
    mins, D, tam, lam = build_minors(A, C, L0, q, rows)
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    size = len(V[0]) + d
    if not rank_is_constant(A, C, L0, q, rows, size):
        return 'unknown', 'rank[V|Z] 在该图卡上不恒定 ⟹ 需按秩析取（未实现）'
    if not mins:
        return 'unknown', '无极大子式'
    if D == 0:
        return 'unknown', 'D=0（子式与 λ 无关）'
    M, e0 = coefficient_matrix(mins, D, tam, lam)
    if not tam:
        return 'unknown', '常数图卡未处理'
    Cs = left_null_Cs(M, tam, e0)
    if not Cs:
        # 左零空间为空 ⟹ M 满行秩 ⟹ e0 自动在列空间 ⟹ 处处可行
        return 'good_exists', '左零空间为空（M 满行秩）⟹ 处处 (5b) 成立'
    if verbose:
        print(f'      子式 {len(mins)} 个，D={D}，M 形状 {M.shape}；左零维数 {len(Cs)}')
        for c in Cs:
            print(f'      C_j = {sp.factor(c)}')
    try:
        G = sp.groebner(Cs, *tam, order='grevlex')
        els = list(G.exprs)
    except Exception as e:                      # noqa: BLE001
        return 'unknown', f'Gröbner 失败：{e}'
    if els == [sp.Integer(1)]:
        return 'certified_infeasible', '理想 (C_1..C_k) = (1) ⟹ 无任何 θ 使 e_0∈col M ⟹ (5b) 处处失败'
    return 'good_exists', f'理想非 (1)：z_C = {[sp.factor(e) for e in els]}（存在候选 θ）'


def main():
    import importlib.util as iu
    print('=== $(*)$ 判据：Bézout 系数矩阵的秩等式 ===')
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, _ = V4.build()
    n = len(A4); d = n - len(C4m) - q04
    Kc = ZG.ker_cols([list(x) for x in C4m] + [list(x) for x in L04])
    k = len(Kc[0])
    print(f'C4 反例 q={q04}（d={d}, k={k}）：')
    for rows in itertools.combinations(range(k), d):
        v, why = certify_chart(A4, C4m, L04, q04, rows)
        print(f'  图卡 {rows}: {v} —— {why}')


if __name__ == '__main__':
    main()
