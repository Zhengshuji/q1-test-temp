r"""$r=2$ 的双向量问题：线性空间 $K\subseteq\Lambda^2E$ 是否含**可分解**元。

## 问题

$E=\mathbb C^m$，$K\subseteq\Lambda^2E$ 线性（$\dim K=\ell$）。判定

$$\exists\,0\ne p\in K:\ p\ \text{可分解}\quad(\iff\ \text{斜对称矩阵 } M(p)\ \text{的秩}\le2).$$

这出现在 $r=2$ 的 $\mathrm{DEC}(q)$ 里：$K=\bigcap_{j\ge1}\ker a_j$，$p=p_U$ 是 $U$ 的 Plücker 坐标。

## 分档（每条都有证明或明确标注）

| 情形 | 判定 | 依据 |
|---|---|---|
| $m=3$ | **恒真** | $\Lambda^2\mathbb C^3$ 维 3，$\mathrm{Gr}(2,3)=\mathbb P^2$ 是整个空间 |
| $m=4$，$\ell\ge2$ | **恒真** | $q|_K$ 是 $\ge2$ 元二次型；代数闭域上必有非零零点（各向同性）|
| $m=4$，$\ell=1$ | $q(p_0)=0$ | 直接算 Klein 二次型 |
| $m\ge5$，$\ell\ge N-(2m-4)$ | **恒真** | 投影维数计数：$\mathrm{Gr}(2,m)\subset\mathbb P^{N-1}$ 维 $2m-4$ |
| $\ell=1$ | $M(p_0)$ 秩 $\le2$ | 直接算 |
| $\ell=2$ | 一元 gcd | $q_i(p_0+t p_1)$ 是 $t$ 的二次式；5 个的 gcd $\ne1$（+ 检查 $t=\infty$）|
| $\ell=3$（$m=5$）| 理想成员判定 | $\mathbb P^2$ 上 5 个二次型：$(x,y,z)^s\subseteq I$ ⟹ 无公共零点（**可靠地判 NO**）；找到有理点 ⟹ **可靠地判 YES**；都不是 ⟹ `None`（未决）|

**等级**：本模块是工具；上面的定理部分（$m=3,4$ 与维数计数）是纸面命题，
$\ell=2,3$ 的算法由 [verify_bivector.py](verify_bivector.py) 与暴力枚举交叉核对。

## 表示

双向量 $p\in\Lambda^2\mathbb C^m$ 是长度 $N=\binom m2$ 的 `Fraction` 列表，
下标按 $(i,j)$（$i<j$）的字典序。二次型用"单项式字典"表示：`{(i, j): c}` 表示 $c\,p_i p_j$（$i\le j$）。

用法：

```python
import bivector as BV
ok, witness, info = BV.has_decomposable(K, m)   # K: 基向量列表（每个长 N）
```
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG
import poly_smith as PS

ptrim, pmul, pdivmod, pgcd, pdeg = (SG.ptrim, SG.pmul, SG.pdivmod, SG.pgcd, SG.pdeg)


# ---------------- 基本对象 ----------------
def pairs(m):
    return list(itertools.combinations(range(m), 2))


def index_map(m):
    return {ij: k for k, ij in enumerate(pairs(m))}


def skew(p, m):
    """双向量 -> $m\times m$ 斜对称矩阵。"""
    idx = index_map(m)
    M = [[Fr(0)] * m for _ in range(m)]
    for (i, j), k in idx.items():
        M[i][j] = p[k]
        M[j][i] = -p[k]
    return M


def decomposable(p, m):
    r"""$M(p)$ 的秩 $\le2$（$p\ne0$ 时可分解）。"""
    if all(x == 0 for x in p):
        return False
    return AI.rank(skew(p, m)) <= 2


def quadrics(m):
    r"""$\mathrm{Gr}(2,m)$ 的 Plücker 二次型（主 $4\times4$ Pfaffian）：对每个 4-子集 $\{i<j<k<l\}$
    $$p_{ij}p_{kl}-p_{ik}p_{jl}+p_{il}p_{jk}.$$
    $m=4$ 时只有 1 个（Klein）。
    """
    idx = index_map(m)
    out = []
    for I in itertools.combinations(range(m), 4):
        i, j, k, l = I
        out.append({(idx[(i, j)], idx[(k, l)]): Fr(1),
                    (idx[(i, k)], idx[(j, l)]): Fr(-1),
                    (idx[(i, l)], idx[(j, k)]): Fr(1)})
    return out


def qeval(q, p):
    """二次型在 $p$ 处的值。"""
    total = Fr(0)
    for (a, b), c in q.items():
        if a == b:
            total += c * p[a] * p[b]
        else:
            total += c * p[a] * p[b]
    return total


def qpolar(q, p0, p1):
    """极形式 $B(p_0,p_1)=q(p_0+p_1)-q(p_0)-q(p_1)$（$=2B$ 的约定）。"""
    s = [p0[i] + p1[i] for i in range(len(p0))]
    return qeval(q, s) - qeval(q, p0) - qeval(q, p1)


# ---------------- 主判定 ----------------
def _restrict_pencil(q, p0, p1):
    """$q(p_0+t p_1)=a t^2+b t+c$，返回 (a,b,c)。"""
    return qeval(q, p1), qpolar(q, p0, p1), qeval(q, p0)


def _gcd_nonconst(polys):
    g = None
    for f in polys:
        if f is None:
            continue
        g = f if g is None else pgcd(g, f)
        if g is not None and pdeg(g) == 0:
            return False
    return g is not None and pdeg(g) >= 1


def rational_root(poly, max_int=2000):
    r"""有理根（有理根定理）。系数整数值超过 `max_int` 时放弃（避免枚举爆炸），返回 None。"""
    p = ptrim(poly)
    if pdeg(p) < 1:
        return None
    a0, an = p[0], p[-1]
    if a0 == 0:
        return Fr(0)

    def small(x):
        # x 是有理数；约分后分子分母都不大才枚举
        return abs(int(x.numerator)) <= max_int and abs(int(x.denominator)) <= max_int

    if not (small(a0) and small(an)):
        return None

    def divisors(x):
        x = abs(int(x))
        return [d for d in range(1, x + 1) if x % d == 0] if x else [1]

    for num in divisors(a0):
        for den in divisors(an):
            for sgn in (1, -1):
                t = Fr(sgn * num, den)
                acc = Fr(0)
                for c in reversed(p):
                    acc = acc * t + c
                if acc == 0:
                    return t
    return None


def subspace_from_plucker(p, m):
    r"""由 Plücker 坐标还原 $U$：$U=\ker M(p)$（$M(p)_{ij}=p_{ij}$，斜对称）。"""
    return AI.nullspace(skew(p, m))


def has_decomposable_l2(K, m):
    r"""$\ell=2$：$K=\langle p_0,p_1\rangle$。返回 (bool, info)（info 里带 `witness`，可能为 None）。"""
    p0, p1 = K[0], K[1]
    qs = quadrics(m)
    # 无穷远点 p1 本身
    if all(qeval(q, p1) == 0 for q in qs):
        return True, dict(reason='p1 可分解（t=∞）', witness=list(p1))
    polys = []
    for q in qs:
        a, b, c = _restrict_pencil(q, p0, p1)
        polys.append(ptrim([c, b, a]))
    g = None
    for f in polys:
        g = f if g is None else pgcd(g, f)
        if g is not None and pdeg(g) == 0:
            return False, dict(reason='gcd=1 且 t=∞ 不可分解', witness=None)
    if g is None or pdeg(g) < 1:
        return False, dict(reason='gcd 平凡', witness=None)
    t0 = rational_root(g)
    wit = None if t0 is None else [p0[i] + t0 * p1[i] for i in range(len(p0))]
    return True, dict(reason='gcd 非平凡（有限 t 有公根）'
                             + ('' if t0 is None else f'，有理根 t={t0}'),
                      witness=wit, gcd_deg=pdeg(g))


def has_decomposable(K, m, smax=8, grid=3):
    r"""主入口：$K$（基向量列表）里是否有非零可分解元。

    返回 `(verdict, witness, info)`，`verdict` 是 `True` / `False` / `None`（未决，只在 $\ell=3$ 出现）。
    """
    N = m * (m - 1) // 2
    l = len(K)
    assert all(len(p) == N for p in K), 'K 的向量长度应为 C(m,2)'
    if l == 0:
        return False, None, dict(reason='K=0')
    if m == 3:
        return True, list(K[0]), dict(reason='Λ²C³ 全可分解')
    if m == 4:
        q = quadrics(4)[0]
        if l == 1:
            ok = (qeval(q, K[0]) == 0)
            return ok, (list(K[0]) if ok else None), dict(reason='ℓ=1 直接判定')
        return True, None, dict(reason='q|_K 是 ≥2 元二次型 ⟹ 各向同性（见证需代数数）')
    if l == 1:
        ok = decomposable(K[0], m)
        return ok, (list(K[0]) if ok else None), dict(reason='ℓ=1 直接判定')
    if l >= N - (2 * m - 4):
        return True, None, dict(reason=f'维数计数：ℓ={l} ≥ N-(2m-4)={N - (2 * m - 4)}')
    if l == 2:
        ok, info = has_decomposable_l2(K, m)
        return ok, info.get('witness'), info
    if l == 3:
        return _has_decomposable_l3(K, m, smax=smax, grid=grid)
    return None, None, dict(reason=f'ℓ={l} 未实现（>3）')


# ---------------- ℓ=3：理想成员 + 有理点搜索 ----------------
def _homog_mul(f, g, nvars=3):
    """两个齐次多项式的乘积（字典表示）。"""
    out = {}
    for a, ca in f.items():
        for b, cb in g.items():
            key = tuple(a[i] + b[i] for i in range(nvars))
            out[key] = out.get(key, Fr(0)) + ca * cb
    out = {k: v for k, v in out.items() if v != 0}
    return out


def _homog_pow_linear(lin, s, nvars=3):
    r"""线性形式（系数列表）的 $s$ 次幂，返回齐次多项式（字典表示）。"""
    base = {}
    for i, c in enumerate(lin):
        if c != 0:
            key = [0] * nvars
            key[i] = 1
            base[tuple(key)] = Fr(c)
    out = {(0,) * nvars: Fr(1)}
    for _ in range(s):
        out = _homog_mul(out, base, nvars)
    return out


def _monomials(deg, nvars=3):
    out = []
    for c in itertools.combinations_with_replacement(range(nvars), deg):
        v = [0] * nvars
        for x in c:
            v[x] += 1
        out.append(tuple(v))
    return out


def in_homog_ideal(f, gens, nvars=3, max_deg=None):
    r"""$f$ 是否在 gens 生成的齐次理想里（**按次数匹配**：$f=\sum g_ih_i$ 且每项次数都等于 $\deg f$）。"""
    df = max(sum(k) for k in f) if f else 0
    cols = []
    for g in gens:
        dg = max(sum(k) for k in g)
        if dg > df:
            continue
        for mono in _monomials(df - dg, nvars):
            cols.append(_homog_mul(g, {mono: Fr(1)}, nvars))
    if not cols:
        return all(v == 0 for v in f.values())
    mons = _monomials(df, nvars)
    M = [[col.get(m, Fr(0)) for col in cols] for m in mons]
    b = [f.get(m, Fr(0)) for m in mons]
    return _consistent(M, b)


def _consistent(M, b):
    """线性系统 $Mx=b$ 是否相容（精确）。"""
    if not M:
        return all(x == 0 for x in b)
    Aug = [list(M[i]) + [b[i]] for i in range(len(M))]
    R, piv = AI.rref(Aug)
    ncol = len(M[0])
    for i in range(len(R)):
        if all(R[i][j] == 0 for j in range(ncol)) and R[i][ncol] != 0:
            return False
    return True


def _point_verdict(K, m):
    """在小整数格点上找一个有理可分解点（找到了就是 YES 证书；找不到不说明任何事）。"""
    l = len(K)
    rng = range(-3, 4)
    for coefs in itertools.product(rng, repeat=l):
        if all(c == 0 for c in coefs):
            continue
        p = [sum(Fr(coefs[j]) * K[j][i] for j in range(l)) for i in range(len(K[0]))]
        if decomposable(p, m):
            return p
    return None


def _has_decomposable_l3(K, m, smax=8, grid=3):
    p0, p1, p2 = K
    basis = [p0, p1, p2]
    qs = quadrics(m)
    N = m * (m - 1) // 2
    # 在 (x,y,z) 坐标下的 5 个齐次二次型
    gens = []
    for q in qs:
        poly = {}
        for (a, b), c in q.items():
            # (x p0 + y p1 + z p2) 的 a,b 分量
            for u in range(3):
                for v in range(3):
                    coef = c * basis[u][a] * basis[v][b]
                    if coef == 0:
                        continue
                    key = [0, 0, 0]
                    key[u] += 1
                    key[v] += 1
                    key = tuple(key)
                    poly[key] = poly.get(key, Fr(0)) + coef
        poly = {k: v for k, v in poly.items() if v != 0}
        if poly:
            gens.append(poly)
    if not gens:
        return True, list(basis[0]), dict(reason='所有二次型在 K 上恒零 ⟹ K 整条落在 Grassmannian 里')
    # 1) 可靠性 NO：检测 (x,y,z)^s ⊆ I
    for s in range(1, smax + 1):
        if all(in_homog_ideal(_homog_pow_linear(e, s), gens, max_deg=s + 2)
               for e in ([Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)])):
            return False, None, dict(reason=f'(x,y,z)^{s} ⊆ I ⟹ P² 上无公共零点')
    # 2) 可靠性 YES：找有理点
    w = _point_verdict(K, m)
    if w is not None:
        return True, w, dict(reason='找到有理可分解点')
    # 3) 未决
    return None, None, dict(reason='既未证空、也未找到有理点（未决）')
