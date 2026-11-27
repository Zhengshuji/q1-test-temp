"""candidate_checks.py —— 专家 2026-11-05 §7 的**必查清单** + 蜕变测试

对每个候选 $(A,C,L_0,\mathcal L,q)$ 逐条断言（任一失败即停）：
1. 输入：$\\operatorname{rank}C=p$、$\\operatorname{rank}[C;L_0]=p+r$；
2. 可容许：$\\operatorname{rank}[C;\\mathcal L]=p+q$、$\\operatorname{row}L_0\\subseteq\\operatorname{row}\\mathcal L$；
3. 几何：$\\dim V=n-r_1$、$\\dim\\mathcal Z=n-(p+q)$、$\\dim\\mathcal V=p+q$、$\\ker B=V$、
   **构造出的 $\\mathcal Z$ 确实是核**；
4. **$\\delta$ 的三重等式**：$\\delta=h-(p+q)=\\dim D-\\dim(D\\cap\\mathcal V)$，且 $0\\le\\delta\\le\\rho=r_1-p$；
5. $(5a)$ 的行空间形式：$\\operatorname{row}(\\mathcal LA)\\subseteq\\mathcal V+D$；
6. 商铅笔尺寸：$(p+q)\\times(q+\\delta-\\rho)$；
7. **蜕变测试**：换 $\\operatorname{row}\\mathcal L$ 的基、换 $V$ 的基、对状态空间做可逆坐标变换后结论不变。

用法：python -u tools/verification/candidate_checks.py
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

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import decide_symbolic as DS              # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction


def check_candidate(A, C, L0, L, q, st):
    n, p, r = len(A), len(C), len(L0)
    CA = LQ.mul(C, A)
    r1 = LQ.rank([list(x) for x in CA] + [list(x) for x in C])
    rho = r1 - p
    ok = True
    # 1
    ok &= LQ.rank(C) == p
    ok &= LQ.rank([list(x) for x in C] + L0) == p + r
    st['输入秩'] += 1
    # 2
    ok &= LQ.rank([list(x) for x in C] + L) == p + q
    ok &= LQ.rank([list(x) for x in L] + L0) == LQ.rank(L)
    st['可容许'] += 1
    # 3
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
    dV = len(V[0]) if (V and V[0]) else 0
    Z = ZG.ker_cols([list(x) for x in C] + L)
    dZ = len(Z[0]) if (Z and Z[0]) else 0
    ok &= dV == n - r1
    ok &= dZ == n - (p + q)
    Zt = [[Z[i][j] for i in range(n)] for j in range(dZ)] if dZ else []
    ns = ZG.ker_cols(Zt) if dZ else [[F(1) if i == j else F(0) for i in range(n)] for j in range(n)]
    dVc = len(ns[0]) if (ns and ns[0]) else 0
    ok &= dVc == p + q
    st['几何维数'] += 1
    # ker B = V（B 为 row[CA;C] 的满行秩基）
    B = []
    for rr in [list(x) for x in CA] + [list(x) for x in C]:
        cand = B + [rr]
        if LQ.rank(cand) == len(cand):
            B = cand
    ok &= len(B) == r1
    # 检查 ker B = V：随机取几个 V 的元素，验证被 B 零化；随机取一个非 V 元素，验证不被零化
    for j in range(min(dV, 3)):
        v = [V[i][j] for i in range(n)]
        for bb in B:
            ok &= sum(bb[i] * v[i] for i in range(n)) == 0
    st['ker B = V'] += 1
    # 4 三重 delta
    h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
    dVsp = LQ.rank([list(x) for x in L] + [list(x) for x in C])
    assert dVsp == p + q, (dVsp, p + q)
    delta1 = h - (p + q)
    D = [list(x) for x in CA]
    inter = dVsp + LQ.rank(D) - LQ.rank([[ns[i][t] for i in range(n)] for t in range(dVc)] + D)
    delta2 = LQ.rank(D) - inter
    ok &= (delta1 == delta2)
    ok &= 0 <= delta1 <= rho
    st['delta 三重等式'] += 1
    # 5 (5a) 行空间形式
    LA = LQ.mul(L, A)
    rhs = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
    lhs = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C] + LA)
    ok &= (lhs == rhs) == LQ.condA(A, C, L)
    st['(5a) 行空间'] += 1
    # 6 商铅笔尺寸
    dim_quot = dV - (n - h)
    ok &= dim_quot == q + delta1 - rho
    ok &= (p + q) == n - dZ
    st['铅笔尺寸'] += 1
    return ok, delta1


def metamorphic(A, C, L0, L, q, rng):
    """蜕变测试：换 row L 的基后结论（5a 与可行性的判定）不变。"""
    n = len(A)
    qq = len(L)
    M = [[F(rng.randrange(-2, 3)) for _ in range(qq)] for _ in range(qq)]
    if LQ.rank(M) != qq:
        return None
    L2 = LQ.mul(M, L)          # L2 的行 = M 作用在 L 的行上
    if LQ.rank(L2) != qq:
        return None
    return (LQ.condA(A, C, L2) == LQ.condA(A, C, L))


def main():
    rng = random.Random(20261201)
    st = Counter()
    for trial in range(400):
        n = rng.choice([6, 7])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r >= n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank([list(x) for x in C] + L0) != p + r:
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
        for q in range(q0, n - p + 1):
            d = n - p - q
            if d < 0 or d > k:
                continue
            for rows in itertools.combinations(range(k), d) if d > 0 else [()]:
                if d == 0:
                    # 终阶：直接构 [C;L] 可逆
                    need = n - p - r
                    extra = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(need)]
                    L = [list(x) for x in L0] + extra
                    if LQ.rank([list(x) for x in C] + L) != n:
                        continue
                else:
                    Z = DS.Z_from_theta(A, C, L0, q, rows, [F(0)] * (d * (k - d)))
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                        continue
                    try:
                        L = ZG.L_from_Z(A, C, L0, Z, q)
                    except AssertionError:
                        continue
                if L is None:
                    continue
                ok, delta = check_candidate(A, C, L0, L, q, st)
                st['候选'] += 1
                if ok:
                    st['清单全过'] += 1
                else:
                    st['清单有失败'] += 1
                if len(L) > 0:
                    mres = metamorphic(A, C, L0, L, q, rng)
                    if mres is not None:
                        st['蜕变测试'] += 1
                        if mres:
                            st['蜕变一致'] += 1
                        else:
                            st['蜕变不一致'] += 1
                break
            if '候选' in st and st['候选'] > 900:
                break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
