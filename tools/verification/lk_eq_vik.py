r"""L5 的反例证书：LK ≠ L(V ∩ K)（专家第五轮的第一任务，结论：**不成立**）

固定一个可容许实例（满足 (5a)），逐条 assert：
  dim K = 2，dim(V ∩ K) = 1，dim LK = 2，dim L(V ∩ K) = 1  ⟹  两者不相等。
再跑随机扫描给出统计（默认 400 组）。

约定：列向量。K = ker[C;CA]，V = colspan([L;C]^T)，L 为 q×n。
"""

import os
import sys
import random
from fractions import Fraction as Fr

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ     # noqa: E402

F = Fr


def to_cols(M):
    if not M:
        return []
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def ker_cols(M):
    return to_cols(LQ.ker_basis_cols(M))


def span_dim(cols):
    if not cols:
        return 0
    m = len(cols[0])
    return LQ.rank([[cols[j][i] for j in range(len(cols))] for i in range(m)])


def image_cols(L, cols):
    q, n = len(L), len(L[0])
    return [[sum(L[i][j] * c[j] for j in range(n)) for i in range(q)] for c in cols]


def intersect_cols(Acols, Bcols):
    if not Acols or not Bcols:
        return []
    m = len(Acols[0])
    a, b = len(Acols), len(Bcols)
    M = [[Acols[j][i] for j in range(a)] + [-Bcols[j][i] for j in range(b)] for i in range(m)]
    out = []
    for z in ker_cols(M):
        coeffs = z[:a]
        vec = [sum(coeffs[j] * Acols[j][i] for j in range(a)) for i in range(m)]
        if any(v != 0 for v in vec):
            out.append(vec)
    return out


def sub_eq(U, W):
    if not U and not W:
        return True
    if not U or not W:
        return False
    du, dw = span_dim(U), span_dim(W)
    return du == dw and span_dim(U + W) == du


def admissible(A, C, L):
    LA, CA = LQ.mul(L, A), LQ.mul(C, A)
    big = [r[:] for r in LA] + [r[:] for r in L] + [r[:] for r in CA] + [r[:] for r in C]
    small = [r[:] for r in L] + [r[:] for r in CA] + [r[:] for r in C]
    return LQ.rank(big) == LQ.rank(small)


def data_of(A, C, L):
    n = len(A)
    CA = LQ.mul(C, A)
    K = ker_cols([row[:] for row in C] + [row[:] for row in CA])
    rows = [row[:] for row in L] + [row[:] for row in C]
    Vcols = [[row[i] for i in range(n)] for row in rows]
    VIK = intersect_cols(Vcols, K)
    return K, VIK, image_cols(L, K), image_cols(L, VIK)


def main():
    # ---- 固定实例（随机扫描发现的第一个反例）----
    A = [[F(0), F(-1), F(2), F(1)],
         [F(0), F(0), F(-1), F(2)],
         [F(0), F(-1), F(0), F(2)],
         [F(2), F(1), F(2), F(-1)]]
    C = [[F(1), F(1), F(-2), F(2)]]
    L = [[F(-1), F(-2), F(-2), F(0)],
         [F(0), F(-1), F(-1), F(1)]]
    assert admissible(A, C, L), '固定实例必须满足 (5a)'
    K, VIK, LK, LVK = data_of(A, C, L)
    dK, dVIK, dLK, dLVK = span_dim(K), span_dim(VIK), span_dim(LK), span_dim(LVK)
    print('固定实例：', f'dim K={dK}, dim(V∩K)={dVIK}, dim LK={dLK}, dim L(V∩K)={dLVK}')
    assert (dK, dVIK, dLK, dLVK) == (2, 1, 2, 1), '与本文件头声明不符，需重查'
    assert not sub_eq(LK, LVK), '本实例应给出 LK ≠ L(V∩K)'
    print('断言通过：LK ≠ L(V∩K)  ⟹  L5 不成立，主域应取 W_K = LK')

    # ---- 随机扫描统计 ----
    rng = random.Random(20261110)
    n, p, q, r = 4, 1, 2, 1
    tried = adm = eq = neq = 0
    for _ in range(400):
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L = [row[:] for row in L0] + [[F(rng.randrange(-2, 3)) for _ in range(n)]
                                      for _ in range(q - r)]
        tried += 1
        if not admissible(A, C, L):
            continue
        adm += 1
        _, _, LK, LVK = data_of(A, C, L)
        if sub_eq(LK, LVK):
            eq += 1
        else:
            neq += 1
    print(f'随机扫描：尝试 {tried}；可容许 {adm}；LK = L(V∩K) 的实例 {eq}；不相等 {neq}')
    print('结论：等式在一般可容许实例上**不成立**（本扫描 %d/%d 不相等）。' % (neq, adm))


if __name__ == '__main__':
    main()
