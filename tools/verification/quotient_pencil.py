"""quotient_pencil.py —— B.17（永久核 + 商铅笔判据）的核验

**命题（B.17；专家 2026-11-04 §2.1/§5 的更正与建议）** 设 $\\mathcal L$ 满足 $(5a)$，$\\mathcal Z=\\ker[C;\\mathcal L]$，
$S=V\\cap\\mathcal Z$，$N_{\\mathcal Z}(\\lambda)=T_{\\mathcal Z}-\\lambda J_{\\mathcal Z}$。则

1. **永久核**：$S\\subseteq\\ker N_{\\mathcal Z}(\\lambda)$ 对**一切** $\\lambda$ 成立
   （因 $S\\subseteq\\mathcal Z$ 给 $J_{\\mathcal Z}|_S=0$，而 $(5a)\\Rightarrow A(S)\\subseteq\\mathcal Z$ 给 $T_{\\mathcal Z}|_S=0$）；
2. **商铅笔判据**：令 $\\overline N_{\\mathcal Z}(\\lambda):V/S\\to X/\\mathcal Z$ 为诱导映射，则
$$(5b)\\ \\text{成立}\\iff\\ker N_{\\mathcal Z}(\\lambda)=S\\ \\ \\forall\\lambda
\\iff\\overline N_{\\mathcal Z}(\\lambda)\\ \\text{对一切}\\ \\lambda\\ \\text{单射};$$
3. **可计算形式**：取 $V'$ 为 $S$ 在 $V$ 中的补、$P_{\\mathcal Z}$ 满足 $\\ker P_{\\mathcal Z}=\\mathcal Z$，则
$\\overline N_{\\mathcal Z}(\\lambda)$ 的矩阵为 $P_{\\mathcal Z}(A-\\lambda I)V'$（$(n-d)\\times\\dim(V/S)$），
单射 $\\iff$ 其极大子式 gcd 为**非零常数**（$\\dim(V/S)=0$ 时条件空、自动可行）。

**本脚本**：在随机可容许 $(\\mathcal Z,q)$ 上比较"商铅笔判据"与 B.12 可观性判据（后者与 $(5b)$ 等价）。

用法：python -u tools/verification/quotient_pencil.py
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


def quotient_pencil_injective(A, C, L, Z):
    """商铅笔判据：返回 (是否单射 ∀λ, gcd 次数, dim(V/S), 说明)。"""
    n = len(A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    dV = len(V[0]) if (V and V[0]) else 0
    d = len(Z[0]) if (Z and Z[0]) else 0
    if dV == 0:
        return True, None, 0, 'V=0，条件空'
    # S = V ∩ Z
    VZ = [[V[i][k] for k in range(dV)] + [Z[i][j] for j in range(d)] for i in range(n)]
    rk = LQ.rank([[VZ[i][j] for i in range(n)] for j in range(dV + d)])
    s = dV + d - rk
    rho = dV - s
    if rho == 0:
        return True, None, 0, 'V/S=0，条件空（自动可行）'
    # S 的基：取 V 的列中落在 span(Z)+... 用数值方法求 V ∩ Z 的基：
    # 解 V a = Z b（存在非零 (a,b)）
    # 用零空间：构造 (dV + d) 行、dV+d 列的矩阵 [V | -Z]，求其零空间
    M = [[V[i][k] for k in range(dV)] + [-Z[i][j] for j in range(d)] for i in range(n)]
    # 求 (a,b) 使 M (a;b) = 0
    Mt = [[M[i][j] for i in range(n)] for j in range(dV + d)]
    ns = ZG.ker_cols(Mt)          # (dV+d) × 维数
    dS = len(ns[0]) if (ns and ns[0]) else 0
    Scols = [[sum(V[i][k] * ns[i][k2] for k in range(dV)) for k2 in range(dS)] for i in range(n)] if dS else [[] for _ in range(n)]
    # V' = V 的一个补：把 S 的列扩成 V 的基，取新增列
    basis = [list(V[i][j] for i in range(n)) for j in range(dV)]
    picks = []
    for j in range(dV):
        cand = picks + [j]
        sub = [[basis[t][i] for t in cand] for i in range(n)]
        if ZG.bool_rank(ZG.cols_to_rows(sub)) == len(cand):
            picks = cand
    # 需要 ρ = dV - s 个与 S 线性无关的列
    VScols = []
    if dS:
        Slist = [[Scols[i][k] for k in range(dS)] for i in range(n)]
        cur = Slist
    else:
        cur = [[] for _ in range(n)]
    for j in picks:
        if len(VScols) >= rho:
            break
        coltrial = [cur[i] + [basis[j][i]] for i in range(n)]
        rk_old = LQ.rank(cur) if (cur and cur[0]) else 0
        rk_new = LQ.rank(coltrial)
        if rk_new > rk_old:
            VScols.append(basis[j])
            cur = coltrial
    if len(VScols) < rho:
        return None, None, rho, 'V\' 构造失败'
    Vp = [[VScols[k][i] for k in range(rho)] for i in range(n)]
    # P_Z：满行秩、ker = Z
    Zt = [[Z[i][j] for i in range(n)] for j in range(d)] if d else []
    nsP = ZG.ker_cols(Zt) if d else [[F(1) if i == j else F(0) for i in range(n)] for j in range(n)]
    dP = len(nsP[0]) if (nsP and nsP[0]) else 0
    P = [[nsP[i][j] for i in range(n)] for j in range(dP)]
    As = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A])
    Ps = sp.Matrix([[sp.Rational(F(x).numerator, F(x).denominator) for x in row] for row in P])
    Bs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in Vp])
    Mm = sp.expand(Ps * (As - lam * sp.eye(n)) * Bs)      # (n-d) × ρ
    mins = []
    for rs in itertools.combinations(range(Mm.rows), rho):
        m = sp.expand(Mm[list(rs), :].det())
        if m != 0:
            mins.append(sp.Poly(m, lam))
    if not mins:
        return False, None, rho, '全部极大子式恒零'
    g = mins[0]
    for mm in mins[1:]:
        g = sp.gcd(g, mm)
    deg = sp.degree(g.as_expr(), lam)
    return (deg == 0), deg, rho, f'ρ={rho}, s={s}, gcd 次数={deg}'


def main():
    rng = random.Random(20261104)
    st = Counter()
    for trial in range(120):
        n = rng.choice([5, 6, 7])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r >= n:
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
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        n0 = LQ.rank(QR.observability_matrix(A, C))
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d <= 0 or d > k:
                continue
            for rows in itertools.combinations(range(k), d):
                for b in range(0, 3):
                    Z = DS.Z_from_theta(A, C, L0, q, rows, [F(b)] * (d * (k - d)))
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                        continue
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                    if L is None or not LQ.condA(A, C, L):
                        continue
                    inj, deg, rho, why = quotient_pencil_injective(A, C, L, Z)
                    if inj is None:
                        st['构造失败'] += 1
                        continue
                    ok, _ = OT.observability_ok(A, C, L)    # (5a) 下等价于 (5b)
                    st['samples'] += 1
                    if inj == ok:
                        st['agree'] += 1
                    else:
                        st['disagree'] += 1
                        if st['disagree'] <= 6:
                            print(f'  不一致：商铅笔单射={inj}（{why}），B.12={ok}')
    print('统计：', dict(st))
    print('  agree = 商铅笔判据 ⟺ B.12（即 (5b)）；disagree 应为 0')


if __name__ == '__main__':
    main()
