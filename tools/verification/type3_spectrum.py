"""type3_spectrum.py —— 坏 $\\lambda$ 是否落在 $\\operatorname{spec}\\Lambda$ 里？

C4 的反例里，坏 $\\lambda$（$\\operatorname{rank}Q_{\\mathcal L}(\\lambda)<h$ 的有理点）已定位为
$5/3$、$3$（及另一候选的 $\\lambda=1$ 重根）。本脚本用**精确**方法核对它们与
因子化矩阵 $\\Lambda$（由 $\\mathcal LA=\\Lambda\\mathcal L+G_0C+G_1CA$ 解出）的谱的关系：

1. 解线性系统得 $\\Lambda$（[type3_structured](type3_structured.py) 的反例实例）；
2. 用 **Leverrier–Faddeev**（只用迹与矩阵乘，全部精确有理运算）算 $\\chi_\\Lambda$；
3. 用有理根定理找 $\\chi_\\Lambda$ 的有理根；
4. 与"直接扫有理 $\\lambda$ 得到的坏点"比较。

**预期**：坏点 $\\subseteq\\operatorname{spec}\\Lambda$（这是 $(\\star)$ 的直接推论：
特征值之外 $\\lambda I-\\Lambda$ 可逆，$Q$ 的秩不降）。

用法：python -u tools/verification/type3_spectrum.py
"""

import os
import sys
from fractions import Fraction
from math import gcd as _gcd

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import type3_structured as T3             # noqa: E402
import importlib.util as iu               # noqa: E402

F = Fraction


def solve_lambda(A, C, L):
    """解 $\\mathcal LA=\\Lambda\\mathcal L+G_0C+G_1CA$。"""
    q, p, n = len(L), len(C), len(A)
    LA = LQ.mul(L, A)
    CA = LQ.mul(C, A)
    nu = q * q + 2 * q * p
    rows = []
    for i in range(q):
        for j in range(n):
            row = [F(0)] * (nu + 1)
            for k in range(q):
                row[i * q + k] = L[k][j]
            for s in range(p):
                row[q * q + i * p + s] = C[s][j]
                row[q * q + q * p + i * p + s] = CA[s][j]
            row[nu] = LA[i][j]
            rows.append(row)
    R, piv = LQ.rref(rows)
    for row in R:
        assert not (all(row[t] == 0 for t in range(nu)) and row[nu] != 0), '因子化无解'
    sol = [F(0)] * nu
    for r_i, pc in enumerate(piv):
        if pc < nu:
            sol[pc] = R[r_i][nu]
    Lam = [[sol[i * q + k] for k in range(q)] for i in range(q)]
    # 校验
    rhs = [[sum(Lam[i][k] * L[k][j] for k in range(q))
            + sum(sol[q * q + i * p + s] * C[s][j] for s in range(p))
            + sum(sol[q * q + q * p + i * p + s] * CA[s][j] for s in range(p))
            for j in range(n)] for i in range(q)]
    assert rhs == LA, '因子化校验失败'
    return Lam


def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def trace(X):
    return sum(X[i][i] for i in range(len(X)))


def leverrier(Lam):
    """$\\chi(\\lambda)=\\det(\\lambda I-\\Lambda)$ 的系数（降幂，含首一）。"""
    q = len(Lam)
    I = [[F(1) if i == j else F(0) for j in range(q)] for i in range(q)]
    M = [row[:] for row in I]
    coeffs = [F(1)]                    # λ^q
    for k in range(1, q + 1):
        AM = matmul(Lam, M)
        c = -trace(AM) / k             # c_{q-k}
        coeffs.append(c)
        M = [[AM[i][j] + (c if i == j else F(0)) for j in range(q)] for i in range(q)]
    return coeffs                      # [1, c_{q-1}, ..., c_0]（降幂）


def divisors(n):
    n = abs(int(n))
    if n == 0:
        return [0]
    return [d for d in range(1, n + 1) if n % d == 0]


def rational_roots(coeffs):
    """降幂系数的有理根（有理根定理）。"""
    cs = [F(c) for c in coeffs]
    while cs and cs[0] == 0:
        cs = cs[1:]
    if len(cs) <= 1:
        return []
    from math import lcm
    m = 1
    for c in cs:
        m = lcm(m, c.denominator)
    ip = [int(c * m) for c in cs]
    an, a0 = abs(ip[0]), abs(ip[-1])
    roots = []
    for p in divisors(a0) or [0]:
        for q_ in divisors(an):
            for s in (1, -1):
                x = F(s * p, q_)
                acc = F(0)
                for c in ip:
                    acc = acc * x + c
                if acc == 0 and x not in roots:
                    roots.append(x)
    return sorted(roots)


def main():
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A, C, L0, q0, cands = V4.build()
    CA = LQ.mul(C, A)
    r1 = LQ.rank([x[:] for x in C] + [x[:] for x in CA])
    lam_list = [F(k) for k in range(-6, 7)] + [F(a, b) for a in range(-9, 10) for b in (2, 3, 4, 5)]
    shown = 0
    for L in cands:
        h, s, m, d_fin = T3.fast_dfin(A, C, L)
        if not (h < q0 + r1 and d_fin > 0):
            continue
        Lam = solve_lambda(A, C, L)
        chi = leverrier(Lam)
        roots = rational_roots(chi)
        LA = LQ.mul(L, A)
        bad = []
        for lam in lam_list:
            Qm = [[lam * L[i][j] - LA[i][j] for j in range(len(A))] for i in range(len(L))]
            Qm = Qm + [list(r) for r in CA] + [list(r) for r in C]
            if LQ.rank(Qm) < h:
                bad.append(lam)
        print(f'\n=== 候选：h={h} d_fin={d_fin} ===')
        print('  Λ =', [[str(x) for x in row] for row in Lam])
        print('  χ_Λ（降幂）=', [str(x) for x in chi])
        print('  有理根：', [str(x) for x in roots])
        print('  直接扫到的坏 λ：', [str(x) for x in bad])
        missing = [x for x in bad if x not in roots]
        print('  坏 λ 是否都在 spec Λ 里：', '是' if not missing else f'否（缺 {missing}）')
        shown += 1
        if shown >= 3:
            break


if __name__ == '__main__':
    main()
