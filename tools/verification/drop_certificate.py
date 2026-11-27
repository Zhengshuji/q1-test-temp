"""drop_certificate.py —— B.13c 的可构造证书：对 C4 的 $q_0=3$ 阶，显式给出 $(x,\\lambda)$ 使
$x\\in V\\setminus\\mathcal Z$ 且 $(\\lambda I-A)x\\in\\mathcal Z$，并核验 $\\operatorname{rank}Q(\\lambda)<h$

**B.13c（等价刻画，$(5a)$ 下）**：$(5b)$ 在 $\\mathcal Z$ 处失败 $\\iff\\exists x\\in V\\setminus\\mathcal Z$ 与 $\\lambda$ 使
$(\\lambda I-A)x\\in\\mathcal Z$。
*证明*：设 $\\mathcal LA=\\Lambda\\mathcal L+G_0C+G_1CA$。因 $x\\in V$，$Cx=CAx=0$，故
$\\mathcal L(\\lambda I-A)x=(\\lambda I-\\Lambda)\\mathcal Lx$。又 $x\\in V\\setminus\\mathcal Z\\iff\\mathcal Lx\\ne0$（$x\\in V$ 时
$\\mathcal Lx=0\\iff Cx=\\mathcal Lx=0\\iff x\\in\\ker[C;\\mathcal L]=\\mathcal Z$）。而 $(\\lambda I-A)x\\in\\mathcal Z
\\iff\\mathcal L(\\lambda I-A)x=0$（$C(\\lambda x-Ax)=\\lambda Cx-CAx=0$ 自动）。于是两侧都等价于
$\\exists\\lambda:\\ker(\\lambda I-\\Lambda)\\cap\\operatorname{im}\\mathcal L\\ni\\mathcal Lx\\ne0$，即 B.12 的掉秩条件。$\\square$

本脚本在 C4 上把 $x,\\lambda$ 算出来（$Z$ 取各图卡），并核验 $\\operatorname{rank}Q(\\lambda)<h$。

用法：python -u tools/verification/drop_certificate.py
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
import decide_symbolic as DS              # noqa: E402
import importlib.util as iu               # noqa: E402

F = Fraction
lam = sp.symbols('lam')


def drop_certificate(A, C, L, tag=''):
    """对给定 $L$（须满足 $(5a)$）构造 $(x,\\lambda)$；返回 (成功?, 报告)。"""
    n = len(A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    Z = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L])
    dV = len(V[0]) if (V and V[0]) else 0
    d = len(Z[0]) if (Z and Z[0]) else 0
    if dV == 0 or d == 0:
        return False, f'退化（dV={dV}, d={d}）'
    As = sp.Matrix(A)
    Vs = sp.Matrix(V)                     # n × dV
    Zs = sp.Matrix(Z)                     # n × d
    # 投影到 Z：P = Z (Z^T Z)^{-1} Z^T
    ZtZ = (Zs.T * Zs)
    P = Zs * ZtZ.inv() * Zs.T
    I = sp.eye(n)
    # M(λ) = (I−P)(λV − AV)，n × dV
    M = (I - P) * (lam * Vs - As * Vs)
    # 取一个 dV×dV 子式，求根
    for rows in itertools.combinations(range(n), dV):
        sub = M[list(rows), :]
        det = sp.expand(sub.det())
        if det == 0 or not det.has(lam):
            continue
        roots = sp.Poly(det, lam).all_roots() if sp.degree(det, lam) >= 1 else []
        for r0 in roots:
            if not r0.is_real:
                pass
            # 代入 λ0
            l0 = sp.nsimplify(r0)
            M0 = sub.subs(lam, l0)
            ns = M0.nullspace()
            if not ns:
                continue
            b = ns[0]
            x = Vs * b
            x = [sp.nsimplify(t) for t in x]
            # 检查 x ∉ Z：即 Lx ≠ 0
            Lx = [sum(sp.Rational(L[i][j]) * x[j] for j in range(n)) for i in range(len(L))]
            if all(sp.simplify(t) == 0 for t in Lx):
                continue
            # 检查 (λ0 I − A)x ∈ Z：即 L((λ0 I−A)x) = 0 且 C((λ0I−A)x)=0
            lamx = [sp.simplify(l0 * x[j] - sum(sp.Rational(A[j][k]) * x[k] for k in range(n)))
                    for j in range(n)]
            Lz = [sp.simplify(sum(sp.Rational(L[i][j]) * lamx[j] for j in range(n))) for i in range(len(L))]
            Cz = [sp.simplify(sum(sp.Rational(C[i][j]) * lamx[j] for j in range(n))) for i in range(len(C))]
            ok = all(t == 0 for t in Lz + Cz)
            # 核验 rank Q(λ0) < h
            h = TC.analyse(A, C, L)['h']
            Q0 = [[sp.simplify(l0 * sp.Rational(L[i][j]) - sp.Rational(LQ.mul(L, A)[i][j]))
                   for j in range(n)] for i in range(len(L))]
            Q0 += [[sp.Rational(C[i][j]) for j in range(n)] for i in range(len(C))]
            Q0 += [[sp.Rational(LQ.mul(C, A)[i][j]) for j in range(n)] for i in range(len(C))]
            rk = sp.Matrix(Q0).rank()
            return ok and rk < h, (f'{tag}λ0 = {l0}；x 的支撑 = '
                                   f'{[j for j in range(n) if x[j] != 0]}；'
                                   f'rank Q(λ0) = {rk} < h = {h}：{rk < h}')
    return False, f'{tag}未找到掉秩点'


def main():
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A, C, L0, q0, _ = V4.build()
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q0
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    print(f'C4：n={n}, p={p}, r={r}, q0={q0}, d={d}, k={k}')
    ok_cnt = tot = 0
    for rows in list(itertools.combinations(range(k), d))[:4]:
        for base in (F(0), F(1), F(2)):
            th = [base] * (d * (k - d))
            Zv = DS.Z_from_theta(A, C, L0, q0, rows, th)
            if ZG.bool_rank(ZG.cols_to_rows(Zv)) != d:
                continue
            Lw = ZG.L_from_Z(A, C, L0, Zv, q0)
            if Lw is None or not LQ.condA(A, C, Lw):
                continue
            tot += 1
            ok, rep = drop_certificate(A, C, Lw, tag=f'rows={rows} θ={base}: ')
            print(('  ✓ ' if ok else '  ✗ ') + rep)
            ok_cnt += 1 if ok else 0
    print(f'\n证书成功 {ok_cnt}/{tot}（每个都给出显式 (x, λ0) 并核验 rank Q(λ0) < h）')


if __name__ == '__main__':
    main()
