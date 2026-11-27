r"""多项式标架（QA24 第一阶段）：单行 gcd 归一化 + Bézout 幺模补全 + 饱和。

**问题**：$I_\lambda=\operatorname{im}P(\lambda)\cap(H/S)$ 需要一个**多项式标架** $B(\lambda)$
（列数 = $\dim I_\lambda$，在**每个有限** $\lambda$ 上都满列秩）。

**专家 QA24 的算法**（$Q=\pi\circ P$，$\pi:W/S\to W/H$，本项目各实例 $w-h=1$ ⟹ $Q$ 是**单行**）：

1. $g=\gcd(q_1,\dots,q_t)$，$\bar q_i=q_i/g$（$\bar q$ 是 unimodular row）；
2. 用**扩展 Euclidean** 构造 $E\in\mathrm{GL}_t(R)$ 使 $\bar q\,E=(1,0,\dots,0)$；
3. 核标架 $V=E$ 的后 $t-1$ 列 ⟹ $\ker_R Q=\operatorname{im}_R V$；
4. $B_0=P\,V$ 生成 $I_\lambda$（可能冗余/在某点降秩）⟹ **饱和**：取出满列秩的点态标架；
5. 验证：$\operatorname{rank}B(\lambda)=\rho$ 对所有有限 $\lambda$。

**QA24 的关键提醒**：映射后的 $B_0$ **必须饱和**——否则像
$Q=(\lambda,0)$、$M=\begin{psmallmatrix}\lambda&0\\1&\lambda\end{psmallmatrix}$ 那样，
$\ker Q$ 的基映过去会在 $\lambda=0$ 处退化。

用 `poly_lin_alg.py` 的多项式工具。
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

ptrim, padd, psub, pmul, pdivmod, pgcd, pdeg = (
    SG.ptrim, SG.padd, SG.psub, SG.pmul, SG.pdivmod, SG.pgcd, SG.pdeg)


def pzero(p):
    return ptrim(p) == [Fr(0)]


def pconst(c):
    return [Fr(c)]


# ---------- 扩展 Euclidean（多项式） ----------
def egcd(a, b):
    """返回 (g, s, t) 使 s·a + t·b = g，g 首一。"""
    r0, r1 = ptrim(a), ptrim(b)
    s0, s1 = [Fr(1)], [Fr(0)]
    t0, t1 = [Fr(0)], [Fr(1)]
    while not pzero(r1):
        q, r = pdivmod(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, psub(s0, pmul(q, s1))
        t0, t1 = t1, psub(t0, pmul(q, t1))
    if pzero(r0):
        return ([Fr(0)], [Fr(0)], [Fr(0)])
    lead = r0[-1]
    inv = Fr(1) / lead
    return ([x * inv for x in r0], [x * inv for x in s0], [x * inv for x in t0])


def gcd_list(polys):
    g = [Fr(0)]
    for p in polys:
        g = pgcd(g, p)
    return g


def pdiv_exact(a, b):
    q, r = pdivmod(a, b)
    assert pzero(r), '除不尽'
    return q


# ---------- 单行：unimodular completion ----------
def unimodular_row_completion(q):
    """给单行 q（长度 t，非零），返回 E（t×t 多项式矩阵）使 q_normalized · E = (1,0,...,0)。

    用反复的 2×2 扩展 Euclidean：把 q_1 与 q_i 归约成 gcd，清掉 q_i。
    """
    t = len(q)
    assert t >= 1
    g = gcd_list(q)
    assert not pzero(g), '零行'
    qb = [pdiv_exact(x, g) for x in q]          # 去公因子 ⟹ unimodular row

    # E 初始为单位阵（列存储：E[j] 是第 j 列）
    E = [[[Fr(1)] if i == j else [Fr(0)] for i in range(t)] for j in range(t)]
    r = [ptrim(x) for x in qb]                   # 当前行（会随列操作变化）

    for i in range(1, t):
        if pzero(r[i]):
            continue
        d, s_, sp = egcd(r[0], r[i])
        a0, ai = r[0], r[i]
        q0 = pdiv_exact(ai, d)      # a_i / d
        q1 = pdiv_exact(a0, d)      # a_0 / d
        c0_new = [padd(pmul(s_, E[0][k]), pmul(sp, E[i][k])) for k in range(t)]
        ci_new = [psub(pmul(q1, E[i][k]), pmul(q0, E[0][k])) for k in range(t)]
        E[0], E[i] = c0_new, ci_new
        r[0] = d
        r[i] = [Fr(0)]
    assert all(pzero(r[i]) for i in range(1, t)), '未清零'
    return E, r[0], g


def pscale_neg(p):
    return [(-x) for x in p]


# ---------- 饱和：从生成列里取常秩点态标架 ----------
def saturate_frame(Bcols, m):
    """Bcols: 多项式列（每个是长度 m 的系数列表列表）。返回 (frame, rho) 或 (None, rho)。

    策略：先算 $\mathbb C(\lambda)$ 上的秩 $\rho$，再找 $\rho$ 列使某个 $\rho$ 阶子式是**非零常数**。
    """
    t = len(Bcols)
    if t == 0:
        return [], 0
    # 多项式矩阵（行 m × 列 t）
    M = [[Bcols[j][i] for j in range(t)] for i in range(m)]
    # C(λ) 上的秩：用 SG.pdet 的 gcd 判据（极大子式的 gcd 次数 = 0 说明有常数子式）
    rho = None
    best = None
    for k in range(min(m, t), 0, -1):
        found = None
        for rows in itertools.combinations(range(m), k):
            for cols in itertools.combinations(range(t), k):
                P = [[M[i][j] for j in cols] for i in rows]
                d = SG.pdet(P)
                if SG.pdeg(d) >= 0:
                    found = (rows, cols, d)
                    break
            if found:
                break
        if found:
            rho = k
            best = found
            break
    if rho is None:
        return [], 0
    rows, cols, d = best
    if pdeg(d) == 0 and not pzero(d):
        # 该 k 列已经是常秩标架
        return [Bcols[j] for j in cols], rho
    return None, rho
