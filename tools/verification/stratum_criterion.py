"""stratum_criterion.py —— B.16（分层判据）的核验：按 s = dim(V∩Z) 分层

**B.16（分层判据）** 设 $\\mathcal Z\\in\\mathrm{Gr}(d,K)$ 可容许（$(5a)$ 成立），$S:=V\\cap\\mathcal Z$、$s=\\dim S$，
$$J_{\\mathcal Z}:V\\to X/\\mathcal Z,\\ x\\mapsto x+\\mathcal Z,\\qquad
T_{\\mathcal Z}:V\\to X/\\mathcal Z,\\ x\\mapsto Ax+\\mathcal Z,\\qquad N_{\\mathcal Z}(\\lambda)=T_{\\mathcal Z}-\\lambda J_{\\mathcal Z}.$$
则

* **(a)** 若 $S=V$（即 $V\\subseteq\\mathcal Z$）：**谱可行**（无 $x\\in V\\setminus\\mathcal Z$ 可言）；
* **(b)** 若 $S=0$：失败 $\\iff\\exists\\lambda:\\operatorname{rank}N_{\\mathcal Z}(\\lambda)<\\dim V$
  $\\iff$ 铅笔 $N_{\\mathcal Z}$ 的极大子式 gcd 有正次数（有**有限零点**）；
* **(c)** 一般情形：失败 $\\iff\\exists\\lambda:\\ker N_{\\mathcal Z}(\\lambda)\\not\\subseteq S$。

本脚本核验 (b)：在随机实例的随机可容许 $\\mathcal Z$（且 $V\\cap\\mathcal Z=0$）上，比较
"gcd 有正次数" 与 B.12 可观性判据（后者与 $(5b)$ 等价）。

用法：python -u tools/verification/stratum_criterion.py
"""

import os
import sys
import itertools
import random
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
import observability_test as OT           # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction
lam = sp.symbols('lam')


def N_pencil(A, C, L, Z):
    """N_Z(λ) = (A − λI) 在 V 上、模 Z 的像：取 V、Z 的基，返回 (dim X − dim Z) × dim V 的符号矩阵。"""
    n = len(A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    dV = len(V[0]) if (V and V[0]) else 0
    d = len(Z[0]) if (Z and Z[0]) else 0
    if dV == 0:
        return None
    # Z 的定义方程：P_Z 满行秩且 ker P_Z = Z ⟹ 取 Z^⊥ 的行
    Zt = [[Z[i][k] for i in range(n)] for k in range(d)]
    ns = ZG.ker_cols(Zt)                      # {y : y·Z = 0}
    dP = len(ns[0]) if (ns and ns[0]) else 0
    P = [[ns[i][j] for i in range(n)] for j in range(dP)]
    As = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A])
    Ps = sp.Matrix([[sp.Rational(F(x).numerator, F(x).denominator) for x in row] for row in P])
    Bs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in V])
    M = sp.expand(Ps * (As - lam * sp.eye(n)) * Bs)
    return M, dV


def gcd_degree(M, dV):
    rows = M.rows
    mins = []
    for rs in itertools.combinations(range(rows), dV):
        m = sp.expand(M[list(rs), :].det())
        if m != 0:
            mins.append(sp.Poly(m, lam))
    if not mins:
        return None
    g = mins[0]
    for mm in mins[1:]:
        g = sp.gcd(g, mm)
    return sp.degree(g.as_expr(), lam)


def main():
    rng = random.Random(20261104)
    st = Counter()
    for trial in range(40):
        n = rng.choice([5, 6, 7])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r > n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank(QR.observability_matrix(A, C)) != n:
            continue
        if LQ.rank(QR.observability_matrix(A, L0)) != n:
            continue
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        n0 = LQ.rank(QR.observability_matrix(A, C))
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not K or not K[0]:
            continue
        k = len(K[0])
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
        dV = len(V[0]) if (V and V[0]) else 0
        if dV == 0:
            continue
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d <= 0 or d > k or d > dV:
                continue
            for rows in itertools.combinations(range(k), d):
                for b in range(0, 3):
                    th = [F(b)] * (d * (k - d))
                    Z = DS.Z_from_theta(A, C, L0, q, rows, th)
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                        continue
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                    if L is None or not LQ.condA(A, C, L):
                        continue
                    # s = dim(V ∩ Z)
                    Vs = [[V[i][j] for j in range(dV)] + [Z[i][j] for j in range(d)] for i in range(n)]
                    rk = LQ.rank([[Vs[i][j] for i in range(n)] for j in range(dV + d)])
                    s = dV + d - rk
                    if s != 0:
                        st['skip_s>0'] += 1
                        continue
                    M, dV2 = N_pencil(A, C, L, Z)
                    if M is None:
                        continue
                    deg = gcd_degree(M, dV2)
                    if deg is None:
                        st['all_zero'] += 1
                        continue
                    fails_by_gcd = (deg > 0)
                    ok, _ = OT.observability_ok(A, C, L)     # (5a) 下等价于 (5b)
                    fails = (not ok)
                    st['tested'] += 1
                    if fails_by_gcd == fails:
                        st['agree'] += 1
                    else:
                        st['disagree'] += 1
                        if st['disagree'] <= 5:
                            print(f'  不一致：s=0，gcd 次数={deg}，B.12 失败={fails}（q={q}, d={d}）')
    print('统计：', dict(st))
    print('  agree = "s=0 层上 gcd 有正次数" == "(5b) 失败"；disagree 应为 0')


if __name__ == '__main__':
    main()
