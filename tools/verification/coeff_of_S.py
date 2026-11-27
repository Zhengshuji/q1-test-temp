r"""固定 $S$ 的系数形式：**三个入口，三个域**（2026-11-01 重写，止血 + 域断言）。

**状态：工具（不是判据）**。本模块只负责把"某一行选择下的 $(r+t)$-子式"展开成系数形式
$a_0,\dots,a_D$（对 Plücker 坐标 $p_U$ 线性）。它**不**判定 $\mathrm{DEC}(q)$；
$\mathrm{DEC}(q)$ 的唯一判据是 `base_sweep.check_Z`（$(A)+(S)$ 都查）。

## 三个入口（域不重叠）

| 入口 | 对象 | 域（assert） | 用途 |
|---|---|---|---|
| `coeff_forms_full` | **真铅笔行列式** $\det[U\mid P(\lambda)]$，$(w_m\times w_m)$ | $q=t$（即 $r+t=w_m$）| $q=t$ 域的精确系数判据（C1）|
| `coeff_forms_balanced`（旧名 `coeff_forms_of_S`）| $m$ 行**截断**对象 $\det[U\mid P_H(\lambda)]$，$(m\times m)$ | $m=r+t$ | 只在 $m=w_m$（$H=W$ 退化）时与真铅笔一致 |
| `feasible_by_minors` | 全部 $(r+t)$-子式的 gcd | $r+t\le w_m$ | **任意 $q$** 的 $(S)$ 判据 |

$$r=d-s=w-q-s,\qquad t=v-s,\qquad m=h-s,\qquad w_m=w-s,\qquad r+t=w-q+v-2s .$$
$$\text{方阵}\iff r+t=w_m\iff q=t;\qquad m=r+t\iff h=w-q+v-s\ (\text{不是 }q=t).$$

**历史坑（2026-11-01，HANDOVER2 §3.1 / 专家 §3）**：本文件曾有两个同名 `coeff_forms_of_S`，
活版本用 $m$ 行，却在 `coeff_space.coeff_forms([P0,P1], m, r)` 里要求列数 $t=m-r$；
$m<r+t$ 时**静默**只读前 $m-r$ 列、$m>r+t$ 时 IndexError。四个调用者（c296/c297/c299/c300）
把它当"精确判据"用 $\Longrightarrow$ 支 5 的 58 例结论只对截断对象成立。
现在：域断言齐全，重复定义删除，$h$ 的两个含义分开（$h=\dim H$ 与 $h_\Theta=\dim(V+Z)=r+t+s$）。

## 记号

$W=\ker C$、$V=\ker[C;CA]$、$H=\ker[C;L_0]$、$Z=\ker[C;\mathcal L]$、$S=Z\cap V$；
$E=H/S$、$W_m=W/S$、$U=Z/S$、$\overline V=V/S$；坐标一律用 $W_m$ 的基
`st['WB']`（前 $s$ 个是 $S$ 的基，其余是 $W_m$ 的基）。

## 用法

```python
import coeff_of_S as CS
a, (P0, P1), info = CS.coeff_forms_full(A, C, L0, q, S)   # 仅 q=t
forms = [a[j] for j in range(1, len(a)) if any(a[j])]
K = AI.nullspace(forms)                                     # C2：a_0|_K != 0 ?
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
import coeff_space as CS

# 复用多项式工具
ptrim, padd, psub, pmul, pdivmod, pgcd, pdeg = (
    SG.ptrim, SG.padd, SG.psub, SG.pmul, SG.pdivmod, SG.pgcd, SG.pdeg)


def pzero(p):
    return ptrim(p) == [Fr(0)]


def pmake(c):
    return [Fr(c)]


# ---------------- 有理函数 (num, den) ----------------
def rf_make(n, d=None):
    """规范化：den 首一、gcd 约掉。"""
    n = ptrim(n)
    if d is None:
        d = [Fr(1)]
    d = ptrim(d)
    assert not pzero(d), '有理函数分母为零'
    if pzero(n):
        return ([Fr(0)], [Fr(1)])
    g = pgcd(n, d)
    if not pzero(g) and pdeg(g) > 0:
        n, r1 = pdivmod(n, g)
        d, r2 = pdivmod(d, g)
    # 首一化
    lead = d[-1]
    if lead != 0 and lead != 1:
        n = [x / lead for x in n]
        d = [x / lead for x in d]
    return (ptrim(n), ptrim(d))


def rf_zero(x):
    return pzero(x[0])


def rf_add(a, b):
    return rf_make(padd(pmul(a[0], b[1]), pmul(b[0], a[1])), pmul(a[1], b[1]))


def rf_neg(a):
    return ([-x for x in a[0]], a[1])


def rf_sub(a, b):
    return rf_add(a, rf_neg(b))


def rf_mul(a, b):
    return rf_make(pmul(a[0], b[0]), pmul(a[1], b[1]))


def rf_div(a, b):
    assert not rf_zero(b), '除以零有理函数'
    return rf_make(pmul(a[0], b[1]), pmul(a[1], b[0]))


RF0 = ([Fr(0)], [Fr(1)])
RF1 = ([Fr(1)], [Fr(1)])


# ---------------- 有理函数矩阵 ----------------
def rf_rref(M):
    """M: list of rows of RF。返回 (rref, pivots)。"""
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if not rf_zero(M[i][c])), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = rf_div(RF1, M[r][c])
        M[r] = [rf_mul(inv, x) for x in M[r]]
        for i in range(rows):
            if i != r and not rf_zero(M[i][c]):
                f = M[i][c]
                M[i] = [rf_sub(M[i][k], rf_mul(f, M[r][k])) for k in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M, piv


def rf_nullspace(M):
    """M: m×n 有理函数矩阵。返回零空间基（长度 n 的 RF 向量列表）。"""
    if not M or not M[0]:
        return []
    rows, cols = len(M), len(M[0])
    R, piv = rf_rref(M)
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [RF0] * cols
        v[f] = RF1
        for i, p in enumerate(piv):
            v[p] = rf_neg(R[i][f])
        basis.append(v)
    return basis


def rf_rank(M):
    if not M or not M[0]:
        return 0
    return len(rf_rref(M)[1])


# ---------------- 铅笔与交 ----------------
def _solve_in_basis(basis, x):
    """x = sum c_i basis_i；返回 c（有理数列表）。basis 必须线性无关且 x 在 span 里。"""
    n = len(x)
    M = [[basis[i][k] for i in range(len(basis))] + [x[k]] for k in range(n)]
    R, piv = AI.rref(M)
    sol = [Fr(0)] * len(basis)
    rows = len(R)
    # 检查相容
    for i in range(rows):
        if all(R[i][j] == 0 for j in range(len(basis))) and R[i][-1] != 0:
            raise ValueError('solve_in_basis: 无解')
    for i, p in enumerate(piv):
        if p < len(basis):
            sol[p] = R[i][-1]
    return sol


def setup(A, C, L0, q, S):
    """建 V, W, H 与 W/S 的基；断言 S ⊆ V、S 线性无关、维数公式。

    返回 dict：n, s, w, v, h, m, d, wm, r, t, V, W, H, WB, VS, HS。
    """
    n = len(A)
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    W = AI.nullspace([row[:] for row in C])
    H = AI.nullspace([row[:] for row in (C + L0)])
    s = len(S)
    if s > 0:
        assert AI.rank([list(x) for x in S]) == s, 'S 的向量线性相关'
        assert AI.rank(V + [list(x) for x in S]) == len(V), 'S 不在 V 里（S=Z∩V 必须 ⊆V）'
        assert AI.rank(H + [list(x) for x in S]) == len(H), 'S 不在 H 里（S=Z∩V ⊆ Z ⊆ H）'
    # W 的基，前 s 个是 S 的基
    WB = [list(x) for x in S]
    for w in W:
        if AI.rank(WB + [list(w)]) > len(WB):
            WB.append(list(w))
    assert len(WB) == len(W), f'W 的基维数 {len(WB)} != {len(W)}'
    w = len(W)

    def coords_in_WS(x):
        return _solve_in_basis(WB, x)[s:]

    VS = [coords_in_WS(v) for v in V]
    HS = [coords_in_WS(h) for h in H]

    def prune(vecs):
        out = []
        for v in vecs:
            if AI.rank(out + [v]) > len(out):
                out.append(v)
        return out

    VS = prune(VS)
    HS = prune(HS)
    assert len(VS) == len(V) - s, f'V/S 维数 {len(VS)} != {len(V)-s}'
    assert len(HS) == len(H) - s, f'H/S 维数 {len(HS)} != {len(H)-s}（h={len(H)}, s={s}）'
    # D = {x : Ax ∈ H}（(A) 的可行域；S 必须落在里面）
    Ht = [list(x) for x in H]
    Vperp = AI.nullspace([list(x) for x in V])
    Hperp0 = AI.nullspace(Ht)
    G = AI.nullspace(Vperp + Hperp0)
    Gt = [list(x) for x in G]
    Hperp = AI.nullspace(Ht)
    Gperp = AI.nullspace(Gt)
    D = AI.nullspace(Gperp + AI.mul(Hperp, A))
    for x in S:
        assert AI.rank(D + [list(x)]) == len(D), 'S 不在 D 里'
    d = w - q
    assert d >= 0, f'd = w - q = {d} < 0'
    assert d >= s, f'd = {d} < s = {s}（Z 必须包含 S）'
    out = dict(n=n, s=s, w=w, v=len(V), h=len(H), m=len(H) - s, d=d,
               wm=w - s, r=d - s, t=len(VS),
               V=V, W=W, H=H, WB=WB, VS=VS, HS=HS, G=G, D=D)
    assert out['r'] + out['t'] == w - q + len(V) - 2 * s, '恒等式 r+t=w-q+v-2s 被违反'
    return out


def pencil_cols(A, st):
    r"""$P(\lambda)=(A-\lambda I)|_{V/S}$ 的列（$W_m$ 坐标）：每列是 (常数, λ 系数)。"""
    WB, s = st['WB'], st['s']
    cols = []
    n = st['n']
    for c in st['VS']:
        # 还原成 n 维向量：x = Σ c_i WB[s+i]
        v = [sum(c[i] * WB[s + i][k] for i in range(len(c))) for k in range(n)]
        Av = [sum(A[i][k] * v[k] for k in range(n)) for i in range(n)]
        assert AI.rank(WB + [Av]) == len(WB), 'A(V) ⊄ W（不该发生：V=ker[C;CA]）'
        cA = _solve_in_basis(WB, Av)[s:]
        cols.append((cA, [-x for x in c]))   # P(λ) = A − λ·I
    return cols


def intersection_basis(cols, HS):
    """在 C(λ) 上算 im P(λ) ∩ span(HS)。返回 RF 向量列表（长度 wm 的向量）。"""
    wm = len(HS[0]) if HS else 0
    t = len(cols)
    rows = []
    for i in range(wm):
        row = []
        for (c0, c1) in cols:
            row.append(([c0[i], c1[i]], [Fr(1)]))       # c0 + λ c1
        for h in HS:
            row.append(([-x for x in [h[i]]], [Fr(1)]))
        rows.append(row)
    ns = rf_nullspace(rows)
    basis = []
    for vec in ns:
        a = vec[:t]
        out = []
        for i in range(wm):
            acc = RF0
            for j, (c0, c1) in enumerate(cols):
                acc = rf_add(acc, rf_mul(a[j], ([c0[i], c1[i]], [Fr(1)])))
            out.append(acc)
        if any(not rf_zero(x) for x in out):
            basis.append(out)
    out = []
    for v in basis:
        if rf_rank([list(x) for x in out] + [v]) > len(out) if out else True:
            out.append(v)
    return out


def _solve_rf_in_basis(basis, x):
    """在 C(λ) 上解 x = Σ c_i basis_i，返回 c（RF 列表）。"""
    m = len(x)
    k = len(basis)
    M = [[RF0] * k + [x[i]] for i in range(m)]
    for i in range(m):
        for j in range(k):
            b = basis[j][i]
            M[i][j] = b if isinstance(b, tuple) else ([Fr(b)], [Fr(1)])
    R, piv = rf_rref(M)
    c = [RF0] * k
    for i, p in enumerate(piv):
        if p < k:
            c[p] = R[i][k]
        else:
            if not rf_zero(R[i][k]):
                raise ValueError('_solve_rf_in_basis: 无解')
    return c


def clear_denoms(vec):
    """把 RF 向量乘上公分母，得多项式向量（系数列表）。"""
    dens = [x[1] for x in vec]
    lcm = [Fr(1)]
    for d in dens:
        g = pgcd(lcm, d)
        if pdeg(g) > 0:
            q, _r = pdivmod(lcm, g)
            lcm = pmul(q, d)
        else:
            lcm = pmul(lcm, d)
        lcm = ptrim(lcm)
    polys = []
    for (num, den) in vec:
        q, _r = pdivmod(pmul(num, lcm), den)
        polys.append(ptrim(q))
    return polys


def _to_WScorr(U, st):
    """把 U（n 维向量列表，⊆ H）转成 W/S 坐标（长度 wm）。"""
    WB, s = st['WB'], st['s']
    out = []
    for u in U:
        out.append(_solve_in_basis(WB, u)[s:])
    return out


def adapted_basis(st):
    """返回 T（wm×wm），使 T^{-1}(H/S) = span(e_1..e_m)（列 = 补基）。"""
    wm = st['w'] - st['s']
    cols_ = [list(h) for h in st['HS']]
    for i in range(wm):
        e = [Fr(1) if k == i else Fr(0) for k in range(wm)]
        if AI.rank(cols_ + [e]) > len(cols_):
            cols_.append(e)
    assert len(cols_) == wm, f'补基失败 {len(cols_)} != {wm}'
    return [[cols_[j][i] for j in range(wm)] for i in range(wm)]


def hquot_rows(st):
    r"""挑出 $H/S$ 对应的行索引（使嵌入 $H/S\hookrightarrow W_m$ 为单射）。"""
    wm = st['w'] - st['s']
    m = st['m']
    rows = []
    for i in range(wm):
        if AI.rank([[h[k] for k in rows + [i]] for h in st['HS']]) > len(rows):
            rows.append(i)
        if len(rows) == m:
            break
    return rows


def _invert(M):
    n = len(M)
    aug = [list(M[i]) + [Fr(1) if k == i else Fr(0) for k in range(n)] for i in range(n)]
    R, piv = AI.rref(aug)
    assert len(piv) == n, '矩阵不可逆'
    return [[R[i][n + j] for j in range(n)] for i in range(n)]


def laplace_sign(I, r, m):
    """$\\det[U\\mid B]=\\sum_I s_I\\det(U_I)\\det(B_{I^c})$ 的 $s_I$（0-based 行号）。"""
    s = 1 if ((sum(i + 1 for i in I) + r * (r + 1) // 2) % 2 == 0) else -1
    return s


# ---------------- 入口 1：真铅笔行列式（仅 q=t）----------------
def quotient_pencil(A, C, L0, q, S):
    """返回 $(P_0,P_1,\\mathrm{info})$：$P(\\lambda)=P_0+\\lambda P_1$ 是 $w_m\\times t$ 的 $W_m$ 坐标矩阵。"""
    st = setup(A, C, L0, q, S)
    cols = pencil_cols(A, st)
    wm, t = st['wm'], len(cols)
    P0 = [[cols[j][0][i] for j in range(t)] for i in range(wm)]
    P1 = [[cols[j][1][i] for j in range(t)] for i in range(wm)]
    info = dict(wm=wm, t=t, r=st['r'], m=st['m'], s=st['s'], d=st['d'],
                q=q, v=st['v'], h=st['h'], rows=list(range(wm)))
    info['square'] = (st['r'] + t == wm)
    return [P0, P1], info


def coeff_forms_full(A, C, L0, q, S):
    """**真铅笔行列式**的系数形式：$\\det[U\\mid P(\\lambda)]=\\sum_j\\lambda^j\\langle a_j,p_U\\rangle$。

    域：$q=t$（即 $r+t=w_m$，方阵）。返回 $a$ 为 `len(a) x C(wm,r)`，列按 $r$-子集字典序
    （与 `coeff_space.coeff_forms` 一致）。符号约定见 `laplace_sign`：
    $\\det[U\\mid P]=\\sum_I s_I\\,p_U(I)\\,a_j[I]$。
    """
    st = setup(A, C, L0, q, S)
    wm, t, r = st['wm'], st['t'], st['r']
    assert q == t, f'coeff_forms_full 只在 q=t 域有效（q={q}, t={t}）'
    assert r + t == wm, f'方阵条件 r+t=w_m 不成立（{r}+{t} != {wm}）'
    cols = pencil_cols(A, st)
    P0 = [[cols[j][0][i] for j in range(t)] for i in range(wm)]
    P1 = [[cols[j][1][i] for j in range(t)] for i in range(wm)]
    a, idxs = CS.coeff_forms([P0, P1], wm, r)
    info = dict(wm=wm, t=t, r=r, m=st['m'], s=st['s'], d=st['d'], q=q,
                v=st['v'], h=st['h'], rows=list(range(wm)),
                idxs=idxs, square=True)
    return a, [P0, P1], info


# ---------------- 入口 2：m 行截断对象（仅 m=r+t）----------------
def coeff_forms_balanced(A, C, L0, q, S):
    """$m$ 行**截断**对象：$\\det[U\\mid P_H(\\lambda)]$（$m\\times m$）。

    **这不是铅笔行列式**，除非 $m=w_m$（即 $H=W$，$L_0\\subseteq\\mathrm{row}\\,C$ 的退化情形）。
    域断言 $m=r+t$；$q=t$ 且 $m\\neq r+t$ 时必须改用 `coeff_forms_full`。
    """
    st = setup(A, C, L0, q, S)
    cols = pencil_cols(A, st)
    rows = hquot_rows(st)
    m, t, r = st['m'], len(cols), st['r']
    assert t == m - r, (
        f'coeff_forms_balanced 要求 m=r+t（m={m}, r={r}, t={t}）；'
        f'q=t 时请用 coeff_forms_full')
    P0 = [[cols[j][0][i] for j in range(t)] for i in rows]
    P1 = [[cols[j][1][i] for j in range(t)] for i in rows]
    a, idxs = CS.coeff_forms([P0, P1], m, r)
    info = dict(wm=st['wm'], t=t, r=r, m=m, s=st['s'], d=st['d'], q=q,
                v=st['v'], h=st['h'], rows=rows, idxs=idxs, square=(r + t == st['wm']))
    return a, [P0, P1], info


# 旧名（保留以兼容 c296/c297/c299/c300/check_handover2）；语义 = coeff_forms_balanced
coeff_forms_of_S = coeff_forms_balanced


def restrict_to_E(a, idxs, m):
    """把全行 $a_j$ 限制到 $\\Lambda^r E$（只保留 $I\\subseteq[m]$ 的坐标）。

    $U\\subseteq H/S=E$ ⟹ $p_U$ 支持在 $I\\subseteq[m]$ 上 ⟹ 只有这些坐标参与 $\\langle a_j,p_U\\rangle$。
    """
    keep = [k for k, I in enumerate(idxs) if max(I) < m]
    return [[row[k] for k in keep] for row in a], [idxs[k] for k in keep]


# ---------------- 入口 3：全部极大子式的 gcd（任意 q）----------------
def feasible_by_minors(A, C, L0, q, S, U):
    r"""**无基判据**（任意 $q$，验证等级：精确）：

    $$U\\subseteq H/S\\ \\Longrightarrow\\ U\\cap I_\\lambda=U\\cap\\operatorname{im}P(\\lambda),$$
    故 "$U$ 与所有 $I_\\lambda$ 不交" $\\iff$ "$[U\\mid P(\\lambda)]$ 的 $(r+t)$ 阶子式的 gcd 是非零常数"。
    不需要 $I_\\lambda$ 的多项式基。

    S, U: n 维向量列表（U ⊆ H，线性无关，$\dim U=s+r$）。
    """
    st = setup(A, C, L0, q, S)
    cols = pencil_cols(A, st)
    wm = st['wm']
    Uc = _to_WScorr(U, st)
    r, t = len(Uc), len(cols)
    k = r + t
    assert r == st['r'], f'U/S 的维数 {r} != r = {st["r"]}'
    assert k <= wm, f'r+t={k} > w_m={wm}（恒不可行，不该调用本函数）'
    g = None
    for rows in itertools.combinations(range(wm), k):
        P = []
        for i in rows:
            row = [[Uc[j][i]] for j in range(r)]
            row += [[cols[j][0][i], cols[j][1][i]] for j in range(t)]
            P.append(row)
        d = SG.pdet(P)
        if SG.pdeg(d) >= 0:
            g = d if g is None else SG.pgcd(g, d)
    return (SG.pdeg(g) == 0 if g is not None else False), g
