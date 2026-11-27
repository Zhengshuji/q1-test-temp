r"""Bézout 证书：把"极大子式 gcd 是单位"变成**有限多项式方程**（QA24 阶段 2 / A3-4a）。

**判据**（无基判据，`coeff_of_S.feasible_by_minors`）：
$$U\cap I_\lambda=0\ \ \forall\lambda\in\mathbb C
\iff \gcd(f_1,\dots,f_N)\in\mathbb C^\times,$$
其中 $f_i$ 是 $[U\mid P(\lambda)]$ 的 $(r+t)$ 阶极大子式（$N=\binom{m}{r+t}$，$\deg f_i\le t$）。

**Bézout 证书**：$\gcd=\text{unit}\iff\exists\,g_i(\lambda)$ 使
$$\boxed{\ \sum_i g_i(\lambda)f_i(\lambda)=1\ }$$
比较 $\lambda$ 的系数 ⟹ 有限个关于 $(S,U,\{g_{ij}\})$ 的**多项式方程** ⟹ $\exists\mathbb R$ 编码。

**次数界**（保守）：$\deg g_i\le(N-1)\cdot\max_i\deg f_i$。

用法见 `proof/layer_program/c295_bezout.py`。
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
import poly_frame as PF

ptrim, padd, psub, pmul, pdivmod, pgcd, pdeg = (
    SG.ptrim, SG.padd, SG.psub, SG.pmul, SG.pdivmod, SG.pgcd, SG.pdeg)
pzero = PF.pzero


def minors_of(Uc, Pcols, m, r):
    """$[U\\mid P(\\lambda)]$ 的全部 $(r+t)$ 阶极大子式（多项式列表）."""
    t = len(Pcols)
    k = r + t
    fs = []
    for rows in itertools.combinations(range(m), k):
        P = []
        for i in rows:
            row = [[Uc[j][i]] for j in range(r)]
            row += [[Pcols[j][0][i], Pcols[j][1][i]] for j in range(t)]
            P.append(row)
        d = SG.pdet(P)
        if pdeg(d) >= 0:
            fs.append(ptrim(d))
    return fs


def gcd_and_certificate(fs):
    """返回 (g, gs)：g = gcd(fs)，gs 满足 Σ gs_i·fs_i = g（规范化到首一）."""
    if not fs:
        return [Fr(0)], []
    g = ptrim(fs[0])
    gs = [[Fr(1)]]
    for i in range(1, len(fs)):
        f = ptrim(fs[i])
        d, s_, t_ = PF.egcd(g, f)
        # 新 gcd d = s_·g + t_·f
        gs = [pmul(s_, x) for x in gs] + [t_]
        g = d
    return g, gs


def verify_certificate(fs, gs, target=None):
    """验证 Σ gs_i·fs_i == target（或 1）."""
    acc = [Fr(0)]
    for i, f in enumerate(fs):
        acc = padd(acc, pmul(gs[i], f))
    want = target if target is not None else [Fr(1)]
    return acc == ptrim(want), acc


def degree_bound(fs):
    N = len(fs)
    D = max((pdeg(f) for f in fs), default=0)
    return (N - 1) * D, N, D


def analyse(Uc, Pcols, m, r):
    """完整分析一个 $U$：子式、gcd、证书、次数界。"""
    fs = minors_of(Uc, Pcols, m, r)
    g, gs = gcd_and_certificate(fs)
    ok, acc = verify_certificate(fs, gs, target=g)
    bound, N, D = degree_bound(fs)
    is_unit = (pdeg(g) == 0 and not pzero(g))
    degs = [pdeg(x) for x in gs]
    return dict(N=N, D=D, deg_g=pdeg(g), is_unit=is_unit,
                cert_ok=ok, cert_degree=max(degs) if degs else 0,
                bound=bound, fs=fs, gs=gs, g=g)
