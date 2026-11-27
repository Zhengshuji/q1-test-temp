r"""系数空间模块（QA22 §4.3 的"中心计算模块"）。

把"固定 $S$ 的谱可行性"化成**系数线性系统**：

    q_U(lam) = det[U | B(lam)] = sum_j lam^j * <a_j, p_U>,

其中 $B(\lambda)$ 是 $I_\lambda$ 的多项式基（$m\times(m-r)$，元素为多项式），$p_U$ 是 $U$ 的 Plücker 坐标。
（A2 §25 定理 B）

    谱可行  <=>  Gr ∩ P(K) ⊄ P(ker a_0),   K = ∩_{j>=1} ker a_j .

精确有理算术。多项式用系数列表表示（低次在前）。
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), 'exact_linalg'))

import audit_independent as AI


# ---------- 多项式工具 ----------
def ptrim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pzero(p):
    return all(x == 0 for x in p)


def padd(p, q):
    n = max(len(p), len(q))
    return ptrim([(p[i] if i < len(p) else Fr(0)) + (q[i] if i < len(q) else Fr(0)) for i in range(n)])


def psub(p, q):
    n = max(len(p), len(q))
    return ptrim([(p[i] if i < len(p) else Fr(0)) - (q[i] if i < len(q) else Fr(0)) for i in range(n)])


def pmul(p, q):
    out = [Fr(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] += a * b
    return ptrim(out)


def pneg(p):
    return [(-x) for x in p]


def poly_det(mat):
    """多项式矩阵行列式（余子式展开，n 小）。"""
    n = len(mat)
    if n == 0:
        return [Fr(1)]
    if n == 1:
        return ptrim(mat[0][0])
    total = [Fr(0)]
    for j in range(n):
        minor = [[mat[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = pmul(mat[0][j], poly_det(minor))
        total = padd(total, term if j % 2 == 0 else pneg(term))
    return ptrim(total)


def coeff_forms(Bpolys, m, r):
    """Bpolys[k]: m×(m−r) 的 Fr 矩阵（λ^k 的系数）。返回 (a, idxs)。"""
    q = m - r
    D = len(Bpolys) - 1
    idxs = list(itertools.combinations(range(m), r))
    amax = q * D
    a = [[Fr(0)] * len(idxs) for _ in range(amax + 1)]
    for idx, I in enumerate(idxs):
        J = [i for i in range(m) if i not in I]
        mat = []
        for i in J:
            row = []
            for j in range(q):
                coef = [Fr(0)] * (D + 1)
                for k in range(D + 1):
                    coef[k] = Bpolys[k][i][j]
                row.append(ptrim(coef))
            mat.append(row)
        d = poly_det(mat)
        for j, c in enumerate(d):
            if j <= amax:
                a[j][idx] += c
    return a, idxs


# ---------- 线性数据与判据 ----------
def linear_data(a):
    d = len(a) - 1
    forms = [a[j] for j in range(1, d + 1) if not pzero(a[j])]
    rk = AI.rank(forms) if forms else 0
    return dict(d=d, rank_ge1=rk, dimK=len(a[0]) - rk,
                rank_a0=0 if pzero(a[0]) else 1, dimPlucker=len(a[0]))


def feasible_r1(a, m):
    """r=1：Gr = P^{m−1}，可行 ⟺ a_0|_K ≠ 0（纯线性代数）。"""
    d = len(a) - 1
    forms = [a[j] for j in range(1, d + 1) if not pzero(a[j])]
    K = AI.nullspace(forms) if forms else [[Fr(1) if i == k else Fr(0) for i in range(m)] for k in range(m)]
    if not K:
        return dict(feasible=False, dimK=0, vals=[])
    vals = [sum(a[0][i] * u[i] for i in range(m)) for u in K]
    return dict(feasible=any(v != 0 for v in vals), dimK=len(K), vals=vals)


def feasible_24(a, max_coef=2):
    """(r,m)=(2,4)：6 维 Plücker 空间，Gr = Q（单个二次型）的零点。"""
    def Q(x):
        p12, p13, p14, p23, p24, p34 = x
        return p12 * p34 - p13 * p24 + p14 * p23

    d = len(a) - 1
    forms = [a[j] for j in range(1, d + 1) if not pzero(a[j])]
    K = AI.nullspace(forms) if forms else [[Fr(1) if i == k else Fr(0) for i in range(6)] for k in range(6)]
    if not K:
        return dict(feasible=False, dimK=0)
    dimK = len(K)
    rng = range(-max_coef, max_coef + 1)
    found = None
    for coefs in itertools.product(rng, repeat=dimK):
        if all(c == 0 for c in coefs):
            continue
        u = [sum(Fr(coefs[i]) * K[i][j] for i in range(dimK)) for j in range(6)]
        if Q(u) == 0 and sum(a[0][j] * u[j] for j in range(6)) != 0:
            found = coefs
            break
    return dict(feasible=found is not None, dimK=dimK, witness=found)


# ---------- 几何：dim X、dim F、分量（QA23 Prop 1） ----------
def geometry_r1(a, m):
    """r=1：X = P(K)（射影空间），F = X \\ P(ker a_0 ∩ K)。"""
    d = len(a) - 1
    forms = [a[j] for j in range(1, d + 1) if not pzero(a[j])]
    K = AI.nullspace(forms) if forms else [[Fr(1) if i == k else Fr(0) for i in range(m)] for k in range(m)]
    if not K:
        return dict(dimX=None, dimF=None, components=0, note='K=0 ⟹ X=∅')
    dimK = len(K)
    dimX = dimK - 1
    a0K = [sum(a[0][i] * u[i] for i in range(m)) for u in K]
    nonzero = any(v != 0 for v in a0K)
    return dict(dimX=dimX, dimF=(dimX if nonzero else None), components=1,
                note=('F 是 X 的开子集，维数 = dim X' if nonzero else 'a_0 在 K 上恒零 ⟹ F=∅'))


def geometry_24(a):
    """(r,m)=(2,4)：X = Q ∩ P(K)（二次超曲面），按 Q|_K 的秩分类。"""
    def Q(x):
        p12, p13, p14, p23, p24, p34 = x
        return p12 * p34 - p13 * p24 + p14 * p23

    d = len(a) - 1
    forms = [a[j] for j in range(1, d + 1) if not pzero(a[j])]
    K = AI.nullspace(forms) if forms else [[Fr(1) if i == k else Fr(0) for i in range(6)] for k in range(6)]
    if not K:
        return dict(dimX=None, dimF=None, rankQ=0, components=0, note='K=0 ⟹ X=∅')
    dimK = len(K)
    # Q|_K 的对称矩阵
    dK = len(K)
    M = [[Fr(0)] * dK for _ in range(dK)]
    for i in range(dK):
        M[i][i] = 2 * Q(K[i])
        for j in range(i + 1, dK):
            s = [K[i][k] + K[j][k] for k in range(6)]
            M[i][j] = M[j][i] = Q(s) - Q(K[i]) - Q(K[j])
    rk = AI.rank(M)
    if rk == 0:
        dimX, comp = dimK - 1, 1
    elif rk == 1:
        dimX, comp = dimK - 2, 1          # 超平面（重数 2）
    elif rk == 2:
        dimX, comp = dimK - 2, 2          # 两个不同超平面
    else:
        dimX, comp = dimK - 2, 1          # 不可约二次超曲面
    # F 是否非空：找 u∈K, Q(u)=0, <a0,u>≠0
    import itertools as _it
    feas = False
    for coefs in _it.product((-2, -1, 0, 1, 2), repeat=min(dK, 5)):
        if all(c == 0 for c in coefs):
            continue
        u = [sum(Fr(coefs[i]) * K[i][j] for i in range(len(coefs))) for j in range(6)]
        if Q(u) == 0 and sum(a[0][j] * u[j] for j in range(6)) != 0:
            feas = True
            break
    return dict(dimX=dimX, dimF=(dimX if feas else None), rankQ=rk, components=comp,
                note=('F 开于 X' if feas else 'F=∅（a_0 在 X 上恒零）'))


# ---------- 根式成员（QA23 优先级 5）：精确判定 a_0 in sqrt(I) ----------
def radical_membership_r1(a, m):
    """r=1：I = I_K 是线性的，故 a_0 in sqrt(I) <=> a_0 in I = span{a_j}_{j>=1} <=> a_0|_K = 0。"""
    d = len(a) - 1
    forms = [a[j] for j in range(1, d + 1) if not pzero(a[j])]
    if not forms:
        return dict(in_radical=pzero(a[0]), how='I=0；a_0 in sqrt(I) <=> a_0=0')
    rk_forms = AI.rank(forms)
    rk_all = AI.rank(forms + [a[0]])
    return dict(in_radical=(rk_all == rk_forms), how='线性代数：a_0 in span{a_j}')


def radical_membership_24(a):
    """(r,m)=(2,4)：I = (Q) + I_K。a_0 in sqrt(I) 的精确判据（按 Q|_K 的秩分类）。

    - rank(Q|_K)=0：Q|_K=0 => X=P(K) => a_0 in sqrt(I) <=> a_0|_K=0
    - rank=1：Q|_K=L^2 => X={L=0} => a_0 in sqrt(I) <=> a_0|_K in span{L}
    - rank>=2：Q|_K 不可约（rank=2 时分裂为两个不同超平面）=> a_0 in sqrt(I) <=> a_0|_K=0
    """
    d = len(a) - 1
    forms = [a[j] for j in range(1, d + 1) if not pzero(a[j])]
    K = AI.nullspace(forms) if forms else [[Fr(1) if i == k else Fr(0) for i in range(6)] for k in range(6)]
    if not K:
        return dict(in_radical=True, how='K=0 ⟹ X=∅ ⟹ 空真')
    dK = len(K)
    M = [[Fr(0)] * dK for _ in range(dK)]
    for i in range(dK):
        M[i][i] = 2 * pluckerQ(K[i])
        for j in range(i + 1, dK):
            s_ = [K[i][k] + K[j][k] for k in range(6)]
            M[i][j] = M[j][i] = pluckerQ(s_) - pluckerQ(K[i]) - pluckerQ(K[j])
    rk = AI.rank(M)
    # a_0 在 K 坐标下的限制向量
    a0K = [sum(a[0][i] * K[j][i] for i in range(6)) for j in range(dK)]
    if rk == 0:
        return dict(in_radical=all(x == 0 for x in a0K), rankQK=0, how='Q|_K=0：a_0|_K=0?')
    if rk == 1:
        v = next((M[i] for i in range(dK) if any(x != 0 for x in M[i])), None)
        if v is None:
            return dict(in_radical=True, rankQK=1, how='退化')
        rk_span = AI.rank([list(v)] + ([a0K] if any(x != 0 for x in a0K) else []))
        return dict(in_radical=(rk_span == 1), rankQK=1, how='Q|_K=L^2：a_0|_K in span{L}?')
    return dict(in_radical=all(x == 0 for x in a0K), rankQK=rk, how='rank>=2：a_0|_K=0?')


def pluckerQ(p):
    p12, p13, p14, p23, p24, p34 = p
    return p12 * p34 - p13 * p24 + p14 * p23
