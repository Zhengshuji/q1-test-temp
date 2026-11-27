"""elimination.py —— 小型精确消元器（Gröbner + 单位理想判定），用于"图卡完整判定"

动机（专家 2026-11-03 §8.1）：有理网格**不**覆盖图卡，所以"网格 0 命中"不能当"不存在"。
本模块给出**精确**判定：对给定图卡，把 $(5a)$ 写成多项式方程组（变量 = 图卡参数 $\\Theta$），
用 Buchberger 判定该系统在 $\\mathbb C$ 上是否有解（等价于理想是否为单位理想）。

用法/接口：

* `exists_5a_chart(A, C, L0, q, chart)` → `True`（有解）/`False`（**certified 无解**）/`None`（预算内未决）；
* `exists_5a(A, C, L0, q)` → 对所有图卡做析取。

约定：$\\mathcal Z=K\\cdot W(\\Theta)$，$W=\\begin{pmatrix}I_d&\\Theta\\end{pmatrix}$；
$(5a)\\iff(\\mathcal Z^{\\perp})A\\subseteq\\mathcal Z^{\\perp}+W$。在 $K$ 的坐标下，$\\mathcal Z^{\\perp}$ 的一个基是
固定的 $K^{\\perp}$ 基 + $K\\cdot\\begin{pmatrix}-\\Theta^{\\mathsf T}\\\\ I\\end{pmatrix}$（对 $\\Theta$ 线性）。
于是 $(5a)$ 等价于"矩阵 $[(\\mathcal Z^{\\perp})A\\ |\\ \\mathcal Z^{\\perp}]$ 的秩等于 $\\mathcal Z^{\\perp}$ 的秩"，
按秩值 $h_0$ 分情形：$\\operatorname{rank}=h_0$ 且所有 $(h_0+1)$-子式为零。
"""

import os
import sys
import itertools
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402

F = Fraction

# ---------- 多项式：dict {指数元组: 系数} ----------


def pconst(c, nv):
    return {} if c == 0 else {(0,) * nv: F(c)}


def pvar(i, nv):
    e = [0] * nv
    e[i] = 1
    return {tuple(e): F(1)}


def padd(a, b):
    out = dict(a)
    for k, v in b.items():
        s = out.get(k, F(0)) + v
        if s:
            out[k] = s
        elif k in out:
            del out[k]
    return out


def pneg(a):
    return {k: -v for k, v in a.items()}


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    if not a or not b:
        return {}
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            out[k] = out.get(k, F(0)) + va * vb
    return {k: v for k, v in out.items() if v}


def pscale(a, c):
    return {k: v * c for k, v in a.items()} if c else {}


def is_zero(a):
    return not a


def is_const(a):
    return len(a) == 1 and all(x == 0 for x in next(iter(a)))


def lead(a, order='lex'):
    """返回首项 (mono, coeff)。"""
    if not a:
        return None, F(0)
    key = (lambda m: m) if order == 'lex' else (lambda m: (sum(m), m))
    m = max(a.keys(), key=key)
    return m, a[m]


def pdiv(a, b, order='lex'):
    """a 除以 b：返回 (商, 余)。只对单项式整除做。"""
    q, r = {}, dict(a)
    mb, cb = lead(b, order)
    while r:
        mr, cr = lead(r, order)
        if all(x >= y for x, y in zip(mr, mb)):
            diff = tuple(x - y for x, y in zip(mr, mb))
            term = {diff: cr / cb}
            q = padd(q, term)
            r = psub(r, pmul(term, b))
        else:
            break
    return q, r


def prem_multi(a, G, order='lex'):
    r = dict(a)
    while r:
        mr, _ = lead(r, order)
        reduced = False
        for g in G:
            mg, _ = lead(g, order)
            if all(x >= y for x, y in zip(mr, mg)):
                _, r = pdiv(r, g, order)
                reduced = True
                break
        if not reduced:
            break
    return r


def spol(f, g, order='lex'):
    mf, cf = lead(f, order)
    mg, cg = lead(g, order)
    lcm = tuple(max(x, y) for x, y in zip(mf, mg))
    tf = {tuple(x - y for x, y in zip(lcm, mf)): F(1) / cf}
    tg = {tuple(x - y for x, y in zip(lcm, mg)): F(1) / cg}
    return psub(pmul(tf, f), pmul(tg, g))


def groebner(eqs, nv, order='lex', max_pairs=4000, max_deg=24):
    """Buchberger；返回 (G, status)，status ∈ {'unit','done','budget'}。"""
    G = [e for e in eqs if not is_zero(e)]
    if not G:
        return [], 'done'
    budget = max_pairs
    changed = True
    while changed:
        changed = False
        pairs = list(itertools.combinations(range(len(G)), 2))
        for i, j in pairs:
            if budget <= 0:
                return G, 'budget'
            budget -= 1
            s = spol(G[i], G[j], order)
            r = prem_multi(s, G, order)
            if not is_zero(r):
                m, _ = lead(r, order)
                if sum(m) > max_deg:
                    return G, 'budget'
                G.append(r)
                changed = True
                if is_const(r):
                    return G, 'unit'
    # 最后检查是否有常数
    for g in G:
        if is_const(g):
            return G, 'unit'
    return G, 'done'


def solve_matrix_system(eqs, nv, **kw):
    """返回 'no_solution' / 'has_solution' / 'unknown'。"""
    G, status = groebner(eqs, nv, **kw)
    if status == 'unit':
        return 'no_solution'
    if status == 'done':
        return 'has_solution'
    return 'unknown'


# ---------- $(5a)$ 的方程 ----------


def chart_basis(A, C, L0, q, d, k, rows, rest, nv):
    """$\\mathcal Z^{\\perp}$ 的基（列）作为 $\\Theta$ 的多项式：返回 list of columns，
    每列是长度 n 的 poly 列表。

    $W=[I_d\\ |\\ \\Theta]$（单位块在 `rows`、自由块在 `rest`），$\\mathcal Z=K\\cdot W$。
    则 $W M = 0$ 的解给出 $K$ 部分的零化子：$M[t][j] = -\\Theta[a][j]$（$t=rows[a]$），
    $M[t][j] = \\delta_{t,rest[j]}$（$t\\in rest$）。于是
    $\\mathcal Z^{\\perp} = K^{\\perp} \\oplus K\\cdot M$。
    """
    n = len(A)
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])   # n × k
    # 1) K^perp 部分：row[C;L0] 的基（作为常多项式列）
    Kp = [list(x) for x in C] + [list(x) for x in L0]
    basis = []
    for r0 in Kp:
        basis.append([pconst(v, nv) for v in r0])
    # 2) K·M 的列
    for j in range(k - d):
        col = [{} for _ in range(n)]
        for t in range(k):
            if t in rows:
                a = rows.index(t)
                v = pvar(a * (k - d) + j, nv)
                coefpoly = pscale(v, F(-1))
            elif t == rest[j]:
                coefpoly = pconst(F(1), nv)
            else:
                continue
            for i in range(n):
                col[i] = padd(col[i], pscale(coefpoly, Kc[i][t]))
        basis.append(col)
    return basis


def minors_poly(M, size, nv):
    """M: list of columns（每个是 poly 的 list，长度 = 行数）。返回所有 size×size 子式的多项式。"""
    nrow = len(M[0]) if M else 0
    ncol = len(M)
    out = []
    for rs in itertools.combinations(range(nrow), size):
        for cs in itertools.combinations(range(ncol), size):
            # 行列式（Laplace 展开）
            det = {}
            for perm in itertools.permutations(range(size)):
                # 符号
                inv = 0
                for a in range(size):
                    for b in range(a + 1, size):
                        if perm[a] > perm[b]:
                            inv += 1
                sign = F(-1) ** inv
                term = pconst(sign, nv)
                for a in range(size):
                    term = pmul(term, M[cs[a]][rs[perm[a]]])
                    if not term:
                        break
                det = padd(det, term)
            if not is_zero(det):
                out.append(det)
    return out


def exists_5a_chart(A, C, L0, q, rows, rest, rowspace_dim, max_pairs=3000):
    """在单个图卡上判 $(5a)$ 是否有解。返回 'yes'/'no'/'unknown'。"""
    n = len(A)
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    d = n - len(C) - q
    nv = d * (k - d)
    # 基（列）作为多项式
    basis = chart_basis(A, C, L0, q, d, k, rows, rest, nv)
    # 把基向量左乘 A（系数为有理数）
    Abasis = []
    for col in basis:
        newcol = []
        for i in range(n):
            p = {}
            for t in range(n):
                c = A[i][t]
                if c:
                    p = padd(p, pscale(col[t], c))
            newcol.append(p)
        Abasis.append(newcol)
    M = Abasis + basis          # 列：先是 (Z^⊥)A，再是 Z^⊥
    # 对每个可能的秩 h0 分情形：rank(Z^⊥)=h0 且所有 (h0+1)-子式为零
    # 先用数值确定 Z^⊥ 的秩的典型值范围
    Zp_num = [[F(0)] * len(basis) for _ in range(n)]
    for jc, col in enumerate(basis):
        for i in range(n):
            Zp_num[i][jc] = sum(v for m, v in col[i].items()) if col[i] else F(0)
    r_base = LQ.rank([[Zp_num[i][j] for i in range(n)] for j in range(len(basis))])
    verdicts = []
    for h0 in range(r_base, r_base + 1):
        eqs = []
        # rank(Z^⊥) ≥ h0：某个 h0-子式非零 ⟹ 用"非零"无法直接表达；改为：要求某个特定 h0-子式 = 1（归一化）
        # 这里用必要条件：所有 (h0+1)-子式为零（秩 ≤ h0），且该阶的 (5a) 需要 rank ≤ h0；非空性由图表本身给出
        allm = minors_poly(M, h0 + 1, nv)
        eqs.extend(allm)
        if not eqs:
            return 'yes'
        st = solve_matrix_system(eqs, nv, max_pairs=max_pairs)
        verdicts.append((h0, st))
    if any(st == 'has_solution' for _, st in verdicts):
        return 'yes'
    if all(st == 'no_solution' for _, st in verdicts):
        return 'no'
    return 'unknown'


def main():
    import importlib.util as iu
    print('=== 在公开例子 $q=3$ 上测试消元器（已知存在显式可行 $\\mathcal L$）===')
    spec = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m = iu.module_from_spec(spec)
    spec.loader.exec_module(m)
    A, C, L0 = m.A, m.C, m.L0
    n = len(A)
    q = 3
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    d = n - len(C) - q
    print(f'  n={n} p={len(C)} r={len(L0)} q={q} d={d} k={k}')
    for rows in itertools.combinations(range(k), d):
        rest = [i for i in range(k) if i not in rows]
        if d * (k - d) > 3:
            print('  （参数过多，跳过）')
            return
        v = exists_5a_chart(A, C, L0, q, rows, rest, k)
        print(f'  图卡 rows={rows}（参数 {d * (k - d)}）：{v}')


if __name__ == '__main__':
    main()
