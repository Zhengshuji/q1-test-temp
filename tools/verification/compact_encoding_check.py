"""compact_encoding_check.py —— 验证**紧凑（结构化）编码**与既有判据等价

**背景**：$(5b)$ 的"逐 $\\lambda$ 秩"条件若要展开极大子式 $m_i$，个数随 $n$ 指数增长。
专家建议的隐式路线：不展开 $m_i$，直接写**矩阵等式**

$$\\exists X(\\lambda)\\in\\mathbb C[\\lambda]^{\\rho\\times n},\\ \\deg X\\le\\rho-1:\\quad X(\\lambda)\\,P_{\\mathcal Z}(\\lambda)=I_\\rho .$$

在 $\\operatorname{rank}[V|Z]=\\dim V+d=:\\rho$（即 $V\\cap Z=0$，典型层）时，
$\\operatorname{rank}P_{\\mathcal Z}(\\lambda)=\\rho\\ \\forall\\lambda\\iff$ 极大子式的 gcd 为常数 $\\iff\\exists X:\\ XP=I_\\rho$。
关键：$XP=I_\\rho$ 对 $X$ 的系数是**线性**的，未知数 $\\rho\\cdot n\\cdot\\rho=O(n^3)$；
朴素 Bézout $\\sum u_im_i=1$ 的未知数是指数的 $\u2014\u2014$ 故**结构化写法把编码规模从指数降到多项式**。

本脚本：逐实例、逐图卡、逐有理 $\\theta$，比较 (a) 紧凑线性系统的可解性；
(b) 既有精确判据（Toeplitz 零度）；二者应完全一致。

用法：python -u tools/verification/compact_encoding_check.py
"""

import os
import sys
import itertools
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import chart_gcd_analysis as CGA          # noqa: E402
import decide_symbolic as DS              # noqa: E402
import toeplitz_criterion as TC           # noqa: E402

F = Fraction


def Wsym_op(rows, d, k, theta):
    """把图卡参数 theta 填进 d×k 的 W（第 a 行在 rows[a] 处为 1，其余按 theta）。"""
    W = sp.zeros(d, k)
    rest = [i for i in range(k) if i not in rows]
    for a, r0 in enumerate(rows):
        W[a, r0] = 1
    idx = 0
    for a in range(d):
        for c in rest:
            W[a, c] = sp.Rational(theta[idx].numerator, theta[idx].denominator)
            idx += 1
    return W


def compact_solvable(A, C, L0, q, rows, theta, rho):
    """在给定 $\\theta$：判 $\\exists X$（$\\deg X\\le\\rho-1$）使 $X P(\\lambda)=I_\\rho$。

    返回 (可解?, 说明)。若 $V\\cap Z\\ne0$（$P$ 的列数 $\\ne\\rho$）则返回 (None, 原因)。
    """
    n = len(A)
    d = n - len(C) - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    lam = sp.symbols('lam')
    tam = CGA.chart_symbols(d, k)
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
            W[a, c] = sp.Rational(theta[idx].numerator, theta[idx].denominator)
            idx += 1
    Z = Ksym * W.T
    P = ((lam * sp.eye(n) - Asym) * Vsym).row_join(Z)
    m = P.cols
    # 真正的 rank[V|Z]：若 < m（即 V∩Z≠0），左逆编码不适用（需一般秩 ρ 的形式，未实现）
    VZ = Vsym.row_join(Z)
    rho_true = sp.Matrix(VZ).rank()
    if rho_true != m:
        return None, f'V∩Z≠0（rank[V|Z]={rho_true} < 列数 {m}）：左逆编码不适用'
    rho = m
    D = max(1, rho - 1)
    xs = [[[sp.Symbol(f'x_{a}_{b}_{t}') for t in range(D + 1)] for b in range(n)]
          for a in range(rho)]
    degP = max(sp.degree(sp.expand(P[i, j]), lam) for i in range(n) for j in range(m))
    eqs = []
    for kk in range(D + degP + 1):
        for a in range(rho):
            for j in range(m):
                acc = sp.Integer(0)
                for b in range(n):
                    pj = sp.Poly(sp.expand(P[b, j]), lam).as_dict()
                    for t in range(D + 1):
                        c = pj.get((kk - t,), sp.Integer(0))
                        if c != 0:
                            acc += xs[a][b][t] * c
                rhs = sp.Integer(1) if (kk == 0 and a == j) else sp.Integer(0)
                eqs.append(sp.expand(acc - rhs))
    eqs = [e for e in eqs if e != 0]
    vars_ = [xs[a][b][t] for a in range(rho) for b in range(n) for t in range(D + 1)]
    M = sp.Matrix([[sp.expand(e).coeff(v) for v in vars_] for e in eqs])
    b = sp.Matrix([-sp.expand(e).subs({v: 0 for v in vars_}) for e in eqs])
    r1, r2 = M.rank(), M.row_join(b).rank()
    return r1 == r2, f'秩 M={r1}，增广={r2}，未知数 {len(vars_)}，方程 {len(eqs)}'


def main():
    stat = Counter()
    for n in (5, 6):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3004):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [list(x) for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    d = n - p - q0
                    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    k = len(Kc[0])
                    if d <= 0 or d > k:
                        continue
                    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
                    rho = len(V[0]) + d
                    rng = __import__('random').Random(seed + n * 31 + d)
                    for rows in itertools.combinations(range(k), d):
                        nv = d * (k - d)
                        for _ in range(4):
                            th = [F(rng.randrange(-4, 5)) for _ in range(nv)]
                            Z = DS.Z_from_theta(A, C, L0, q0, rows, th)
                            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                                continue
                            Lm = ZG.L_from_Z(A, C, L0, Z, q0)
                            if Lm is None:
                                stat['no_L'] += 1
                                continue
                            # 注意：这里**不**要求 (5a)——先单独验证数学等价：
                            # "rank P = ρ ∀λ" ⟺ "存在多项式左逆"，与 (5a) 无关
                            # 参考判据：P 的全部极大子式的 gcd 次数是否为 0（与 P 直接相关，不依赖 (5a)）
                            Pm = ((sp.symbols('lam') * sp.eye(n) - CGA.to_sym(A)) * CGA.to_sym(V))
                            Pm = Pm.row_join(CGA.to_sym(Kc) * (Wsym_op(rows, d, k, th)).T)
                            mins_p = []
                            for rs in itertools.combinations(range(n), Pm.cols):
                                m0 = sp.expand(Pm[list(rs), :].det())
                                if m0 != 0:
                                    mins_p.append(sp.Poly(m0, sp.symbols('lam')))
                            if not mins_p:
                                stat['all_zero'] += 1
                                continue
                            g = mins_p[0]
                            for mm in mins_p[1:]:
                                g = sp.gcd(g, mm)
                            fiveb = (sp.degree(g.as_expr(), sp.symbols('lam')) == 0)
                            ok, why = compact_solvable(A, C, L0, q0, rows, th, rho)
                            if ok is None:
                                stat['skip'] += 1
                                continue
                            stat['samples'] += 1
                            if ok == fiveb:
                                stat['agree'] += 1
                            else:
                                stat['disagree'] += 1
                                print(f'  不一致：n={n} p={p} r={r} seed={seed} rows={rows} θ={base} '
                                      f'紧凑={ok} Toeplitz={fiveb}（{why}）')
    print('\n统计：', dict(stat))
    print('  agree = 紧凑系统可解性 == Toeplitz 的 (5b)；disagree 应为 0')


if __name__ == '__main__':
    main()
