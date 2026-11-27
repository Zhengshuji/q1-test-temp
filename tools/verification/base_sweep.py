r"""基族扫描模块（A3-1/A3-2）：让 $S$ 动起来。

**背景**：此前所有工作都固定在**一个** $S$ 上。A3 要问的是
$$\exists S\in\operatorname{Gr}(s,D):\ \text{固定-}S\ \text{问题可行}\ ?$$

**本模块**（精确有理算术）：
- `geometry(A,C,L0)` —— 算 $V,W,H,G,D$ 及其维数，并**断言**自洽；
- `fixed_S(A,C,L0,d,S)` —— 对给定 $S$ 算 $(r,m,t,k,\ell,\dim B_S)$，枚举**可容许的 $U$**，逐个判 $(A)(S)$；
- 判据用 `spectral_gcd_Z`（独立的极大子式 gcd 判据），$(A)$ 用 $\operatorname{rank}[Z,AZR]=d$。

**方向约定**（项目踩过 4 次，CLAUDE §7.2）：本模块一切矩阵都是**列是向量**（$n\times k$）。
"""
import os
import sys
import itertools
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), 'exact_linalg'))

import audit_independent as AI
import spectral_gcd as SG


def cols2mat(cols, n):
    """列表的向量（每个长度 n）-> n×k 矩阵（列）."""
    return [[cols[j][i] for j in range(len(cols))] for i in range(n)]


def rref_canonical(rows, b):
    """整数行 -> RREF 规范形（tuple）；退化返回 None."""
    M = [[Fr(x) for x in r] for r in rows]
    r = 0
    for c in range(b):
        pr = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        inv = Fr(1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][k] - f * M[r][k] for k in range(b)]
        r += 1
        if r == len(M):
            break
    if r < len(M):
        return None
    return tuple(tuple(x for x in row) for row in M)


def enum_subspaces(b, s, bound=2):
    """枚举 Gr(s, b) 的整数格点（RREF 去重）。s=0 返回一个空基。"""
    if s == 0:
        return [[]]
    vecs = [v for v in itertools.product(range(-bound, bound + 1), repeat=b)
            if any(x != 0 for x in v)]
    seen = set()
    out = []
    for combo in itertools.combinations(range(len(vecs)), s):
        rows = [vecs[i] for i in combo]
        if AI.rank([[Fr(x) for x in r] for r in rows]) < s:
            continue
        key = rref_canonical(rows, b)
        if key is None or key in seen:
            continue
        seen.add(key)
        out.append([[int(x) if x.denominator == 1 else x for x in row] for row in key])
    return out


def mat_rank(cols):
    """列向量的秩."""
    if not cols:
        return 0
    n = len(cols[0])
    return AI.rank(cols2mat(cols, n))


def geometry(A, C, L0):
    """算 V, W, H, G, D（每个都是向量列表 = 列空间）."""
    n = len(A)
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    W = AI.nullspace([row[:] for row in C])
    H = AI.nullspace([row[:] for row in (C + L0)])
    # 交空间用**零化子**：G = V ∩ H = (V^⊥ + H^⊥)^⊥
    Vperp = AI.nullspace([list(x) for x in V])
    Hperp = AI.nullspace([list(x) for x in H])
    G = AI.nullspace(Vperp + Hperp)
    # D = G ∩ A^{-1}H = (G^⊥ + (H^⊥∘A))^⊥
    Gperp = AI.nullspace([list(x) for x in G])
    HA = AI.mul(Hperp, A)                       # (h^⊥)×n
    D = AI.nullspace(Gperp + HA)
    out = dict(n=n, p=len(C), V=V, W=W, H=H, G=G, D=D,
               v=len(V), w=len(W), h=len(H), b=len(G), dimD=len(D))
    assert out['v'] >= out['b'] >= out['dimD'], \
        f"维数链 V⊇G⊇D 被破坏: v={out['v']} b={out['b']} dimD={out['dimD']}"
    # 逐向量验证 D ⊆ G ⊆ V
    for name, sub, base in (('G', G, V), ('D', D, G)):
        base_rank = len(base)
        for x in sub:
            assert AI.rank([list(y) for y in base] + [list(x)]) == base_rank, f'{name} 的元素不在上一层里'
    for x in D:
        Ax = [sum(A[i][k] * x[k] for k in range(n)) for i in range(n)]
        assert AI.rank([list(y) for y in H] + [Ax]) == len(H), 'D 的像不在 H 里'
    return out


def fixed_S(A, C, L0, geo, d, S, ucoeffs=None):
    """给定 S（向量列表，须 ⊆ D），返回该 S 的完整数据 + 所有可容许 U 的判定."""
    n = geo['n']
    s = len(S)
    r = d - s
    assert r >= 0, f'r = d - s = {r} < 0'
    # S ⊆ D ?
    Dt = [list(x) for x in geo['D']]
    for x in S:
        assert AI.rank(Dt + [x]) == geo['dimD'], 'S 不在 D 里（枚举空间写错）'
    m = geo['h'] - s
    t = geo['v'] - s
    AS = [[sum(A[i][k] * x[k] for k in range(n)) for i in range(n)] for x in S]
    # k = dim T_S = dim(A(S)+S) - s
    k = AI.rank(cols2mat(S + AS, n)) - s
    # ℓ = dim φ(S) = dim(A(S)+G)/G
    ell = AI.rank(cols2mat(S + AS + geo['G'], n)) - geo['b']
    # dim B_S = b - dim(S∩G)
    dimSG = AI.rank(cols2mat(S, n)) + geo['b'] - AI.rank(cols2mat(S + geo['G'], n))
    out = dict(s=s, r=r, m=m, t=t, k=k, ell=ell, dimBS=geo['b'] - dimSG)

    # A2 剪枝：k > r ⟹ 必空（不枚举 U）
    if k > r:
        out['candidates'] = []
        out['feasible'] = []
        out['ok'] = False
        return out

    # ---- 可容许的 U ----
    # 理论（A2）：S ⊆ U ⊆ H，dim U = d，A(S) ⊆ U，U ∩ G = S
    H_basis = geo['H']
    HS = []
    for w in H_basis:
        if AI.rank(cols2mat(S + HS + [w], n)) > s + len(HS):
            HS.append(w)
    assert len(HS) == m, f'H/S 的基维数 {len(HS)} != m={m}'

    def in_span(basis, x):
        return AI.rank(cols2mat(basis, n)) == AI.rank(cols2mat(basis + [x], n))

    cand = []
    seen_u = set()
    if ucoeffs is None:
        ucoeffs = enum_subspaces(m, r, bound=1)
    for coefs in ucoeffs:
        Ucols = list(S)
        for row in coefs:
            v = [sum(Fr(c) * HS[j][i] for j, c in enumerate(row)) for i in range(n)]
            Ucols.append(v)
        if mat_rank(Ucols) != d:
            continue
        key = rref_canonical([[x for x in v] for v in Ucols], n)
        if key in seen_u:
            continue
        seen_u.add(key)
        if not all(in_span(Ucols, AS[i]) for i in range(s)):
            continue
        UG = Ucols + geo['G']
        if d + geo['b'] - AI.rank(cols2mat(UG, n)) != s:
            continue
        cand.append(Ucols)

    # 逐个判 (A)(S)
    results = []
    for Ucols in cand:
        okA, okS, g = check_Z(A, C, cols2mat(Ucols, n))
        results.append(dict(U=Ucols, okA=okA, okS=okS,
                            gdeg=(SG.pdeg(g) if g is not None else None)))
        if okA and okS:
            break                      # 找到一个就够（存在性）
    out['candidates'] = results
    out['feasible'] = [c for c in results if c['okA'] and c['okS']]
    out['ok'] = len(out['feasible']) > 0
    # 剪枝断言：k>r 时必空（A2 的剪枝）
    if k > r:
        assert not out['ok'], f'k={k} > r={r} 却找到可行 U（剪枝被违反）'
    return out


def check_Z(A, C, Z):
    """对给定的 Z（n×d，列基）判 (A) 与 (S)。"""
    n = len(A)
    d = len(Z[0])
    CA = AI.mul(C, A)
    CAZ = AI.mul(CA, Z)
    Rv = AI.nullspace(CAZ)
    R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZ = SG.apply_col(A, Z)
    AZR = AI.mul(AZ, R) if R and R[0] else [[Fr(0)] * d for _ in range(n)]
    M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
    okA = AI.rank(M1) == d
    if not okA:
        return False, False, None          # (S) 很贵，先被 (A) 剪掉
    g, h, _c = SG.spectral_gcd_Z(A, C, Z)
    okS = (SG.pdeg(g) == 0)
    return okA, okS, g
