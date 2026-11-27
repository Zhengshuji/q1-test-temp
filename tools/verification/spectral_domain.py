"""spectral_domain.py —— 把"谱域"做成显式参数（专家 2026-11-03 §8.4）

$(5b)$ 的**精确**判据是恒等式（极大子式 gcd 为常数），与谱域无关；
"在哪些 $\\lambda$ 上检查"只影响**抽样型**预筛。本模块把这一点写成显式参数，避免混淆：

* `DOMAIN_C`：全 $\\mathbb C$（含 $0$）—— $(5b)$ 的定义域；
* `DOMAIN_SPEC_A`：只在 $\\operatorname{spec}(A)$ 上（某些文献式表述）；
* `DOMAIN_SPEC_LAMBDA`：只在 $\\operatorname{spec}(\\Lambda)$ 上（B.10 的定位）。

`sample_lambdas(A, domain)` 返回抽样点（`DOMAIN_C` 必含 $0$）；
`decide(A, C, L, domain='C')` 返回**精确**结论，并注明该域下抽样是否已足以发现掉秩。

用法：python tools/verification/spectral_domain.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import spectral_gcd as SG                 # noqa: E402

F = Fraction
DOMAIN_C = 'C'
DOMAIN_SPEC_A = 'spec(A)'
DOMAIN_SPEC_LAMBDA = 'spec(Lambda)'
DOMAINS = (DOMAIN_C, DOMAIN_SPEC_A, DOMAIN_SPEC_LAMBDA)


def char_poly_via_leverrier(M):
    """特征多项式系数（升幂，[c0..cn]），精确有理。"""
    n = len(M)
    A = [row[:] for row in M]
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    B = [row[:] for row in I]
    coeffs = [F(1)]
    for k in range(1, n + 1):
        AB = [[sum(A[i][t] * B[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        c = -sum(AB[i][i] for i in range(n)) / k
        coeffs.append(c)
        B = [[AB[i][j] + (c if i == j else F(0)) for j in range(n)] for i in range(n)]
    return coeffs          # det(λI - M) = λ^n + c1 λ^{n-1} + ... + cn


def rational_roots(coeffs):
    """有理根（升幂系数），有理根定理 + 逐一验证。"""
    from fractions import Fraction as Fr
    c = list(coeffs)
    while c and c[-1] == 0:
        c.pop()
    if not c:
        return []
    if len(c) == 1:
        return []
    # 去分母
    dens = [x.denominator for x in c]
    from math import lcm
    L = 1
    for d in dens:
        L = lcm(L, int(d))
    ints = [int(x * L) for x in c]
    from math import gcd
    g = 0
    for v in ints:
        g = gcd(g, abs(v))
    if g == 0:
        return []
    ints = [v // g for v in ints]
    a0 = ints[0]
    an = ints[-1]
    if a0 == 0:
        roots = [Fr(0)]
        # 去掉 λ 因子后递归
        shifted = ints[1:]
        for r in rational_roots([Fr(v) for v in shifted]):
            roots.append(r)
        return roots
    pdivs = [d for d in range(1, abs(a0) + 1) if a0 % d == 0]
    qdivs = [d for d in range(1, abs(an) + 1) if an % d == 0]
    out = []
    for pp in pdivs:
        for qq in qdivs:
            for s in (1, -1):
                r = Fr(s * pp, qq)
                val = F(0)
                for k, co in enumerate(ints):
                    val += co * r ** k
                if val == 0 and r not in out:
                    out.append(r)
    return out


def sample_lambdas(A, domain=DOMAIN_C):
    assert domain in DOMAINS, f'未知谱域 {domain}'
    base = [F(k) for k in range(-3, 4)] + [F(a, b) for a in (-3, 3) for b in (2, 3)]
    if domain == DOMAIN_C:
        s = set(base)
        s.add(F(0))                     # 显式包含 0
        return sorted(s)
    if domain == DOMAIN_SPEC_A:
        return sorted(set(rational_roots(char_poly_via_leverrier(A))))
    # spec(Λ)：Λ 依赖 L，调用方需自行提供；此处返回空并提示
    return []


def decide(A, C, L, domain=DOMAIN_C, Lambda=None):
    """精确结论 + 该谱域下抽样是否够用的诊断。"""
    res = TC.analyse(A, C, L)
    exact = res['five_b']
    h = res['h']
    diag = {'h': h, 'domain': domain, 'exact_five_b': exact}
    if domain == DOMAIN_SPEC_LAMBDA and Lambda is not None:
        lams = sorted(set(rational_roots(char_poly_via_leverrier(Lambda))))
    else:
        lams = sample_lambdas(A, domain)
    missed = None
    if lams and not exact:
        # 若该域上的抽样都"通过"，说明真实掉秩点在域外
        LA = LQ.mul(L, A)
        passes = True
        for lam in lams:
            Qm = [[lam * L[i][j] - LA[i][j] for j in range(len(A))] for i in range(len(L))]
            Qm = Qm + [x[:] for x in LQ.mul(C, A)] + [x[:] for x in C]
            if LQ.rank(Qm) < h:
                passes = False
                break
        missed = passes
    diag['samples_would_miss'] = missed
    return diag


def main():
    import importlib.util as iu
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A, C, L0, q0, cands = V4.build()
    for i, L in enumerate(cands[:2]):
        for dom in (DOMAIN_C, DOMAIN_SPEC_A):
            dg = decide(A, C, L, dom)
            print(f'C4#{i} [{dom}]: 精确 (5b)={dg["exact_five_b"]}，h={dg["h"]}，'
                  f'该域抽样会漏掉掉秩={dg["samples_would_miss"]}')


if __name__ == '__main__':
    main()
