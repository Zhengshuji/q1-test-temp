"""exact_elimination.py —— 用 sympy 做**精确消元**，完成 §8.1 的"图卡完整判定"

背景：本项目此前只用纯 Python（无第三方依赖），Buchberger 自实现在 $(5a)$ 的
$(h_0+1)$ 次子式系统上规模爆炸（[attempts/39](../../workspace/augmentation_family/attempts/39_elimination_attempt.md)）。
经检查，conda base 环境自带 **sympy 1.13.2**，故本模块用 sympy 做 Gröbner 消元。

**状态：实验性（不可用于下结论）**。分层（按 $h_0=\\operatorname{rank}B$）时，"某个 $h_0$-子式非零"
需要**枚举全部** $h_0$-子式（用 Rabinowitsch 技巧逐个测试）；子式数量可达数千，当前实现有截断（≤200），
**截断时的"空集"结论不可信**，故一律降级为 `unknown`。仅当某层在**完整**见证枚举下得到 $[1]$ 时才可报 `no`。

判定目标：给定实例与阶 $q$、给定图卡（参数 $\\theta$），精确判定

$$\\exists\\theta:\\ (5a)\\ \\text{成立}$$

做法：$(5a)\\iff\\operatorname{rank}M(\\theta)=h(\\theta)$，其中 $M=[(\\mathcal Z^{\\perp})A^{\\mathsf T}\\ |\\ \\mathcal Z^{\\perp}\\ |\\ W]$。
先由采样确定 $h_0$（要求恒定），再把所有 $(h_0+1)$-子式取为多项式（sympy 精确展开），
计算其 Gröbner 基：`[1]` ⟹ **certified 无解**；否则有解（$\\mathbb C$ 上）。

用法：python -u tools/verification/exact_elimination.py
"""

import os
import sys
import itertools
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import complete_small as CS               # noqa: E402

F = Fraction


def sym_matrix(rows):
    return sp.Matrix([[sp.Rational(v.numerator, v.denominator) for v in row] for row in rows])


def chart_params(d, k, rows, rest):
    syms = sp.symbols(f't0:{d * (k - d)}')
    if d * (k - d) == 1:
        syms = (syms,)
    return syms


def Z_sym(A, C, L0, q, rows, rest, syms):
    """$\\mathcal Z$ 的列（sympy Matrix），$\\mathcal Z=K\\cdot W$。"""
    n = len(A)
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    d = n - len(C) - q
    W = sp.zeros(d, k)
    for a, r0 in enumerate(rows):
        W[a, r0] = 1
    idx = 0
    for a in range(d):
        for c in rest:
            W[a, c] = syms[idx]
            idx += 1
    Ksym = sym_matrix(Kc)
    return Ksym * W.T          # n × d


def Residual_sym(A, C, L0, q, rows, rest, syms, h0):
    """$M(\\theta)$（sympy）与固定块。"""
    n = len(A)
    Z = Z_sym(A, C, L0, q, rows, rest, syms)
    # Z^⊥ 的基：用 [Z^T; 0] 的零空间（sympy 的 nullspace 对符号矩阵较慢，用显式构造）
    # 显式构造：Z^⊥ = K^⊥ + K·M，M 的列 = 对 W 的零化子
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    d = n - len(C) - q
    Ksym = sym_matrix(Kc)
    Kp = [list(x) for x in C] + [list(x) for x in L0]
    Kpsym = sym_matrix(Kp).T          # n × (p+r) 列
    # M: k×(k−d)，满足 W·M = 0
    Msym = sp.zeros(k, k - d)
    for j in range(k - d):
        for a in range(d):
            Msym[rows[a], j] = -syms[a * (k - d) + j]
        Msym[rest[j], j] = 1
    Kpart = Ksym * Msym               # n × (k−d)
    Zperp = Kpsym.row_join(Kpart)     # n × (n−d)
    Wsym = sym_matrix([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)]).T
    Acols = sym_matrix(A).T * Zperp   # (Z^⊥)·A^T 的列形式
    M = Acols.row_join(Zperp).row_join(Wsym)
    B = Zperp.row_join(Wsym)
    return M, B, h0


def _minors(M, size, cap=None):
    nrow, ncol = M.shape
    out = []
    for rs in itertools.combinations(range(nrow), size):
        for cs in itertools.combinations(range(ncol), size):
            det = sp.expand(M[list(rs), list(cs)].det())
            if det != 0:
                out.append(det)
            if cap and len(out) >= cap:
                return out
    return out


def certify_chart(A, C, L0, q, rows, rest, cap_minors=10, cap_minorsB=6, verbose=False):
    """精确判定该图卡上 $\\exists\\theta:(5a)$。

    按 $h_0=\\operatorname{rank}B$ 分层（$B=[\\mathcal Z^{\\perp}|W]$），每层用 Rabinowitsch 技巧
    编码"某个 $h_0$-子式 $\\ne0$"（引入 $z$ 与方程 $zf-1=0$），再算 Gröbner：
    某 $(h_0,f)$ 的系统 $\\ne[1]$ ⟹ 有解；**全部** $=[1]$ ⟹ 该层无解；所有层无解 ⟹ 图卡空集。
    """
    n = len(A)
    d = n - len(C) - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    nv = d * (k - d)
    syms = tuple(sp.symbols(f't0:{nv}')) if nv > 0 else ()
    z = sp.symbols('z_sat')
    # 采样定 h 的可能取值
    hs = set()
    for vals in itertools.product([-2, -1, 0, 1, 2], repeat=max(1, nv)):
        Z = CS.Z_from_theta(A, C, L0, q, rows, rest, [F(v) for v in vals])
        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            continue
        L = ZG.L_from_Z(A, C, L0, Z, q)
        if L is None:
            continue
        hs.add(LQ.rank([x[:] for x in L] + [x[:] for x in LQ.mul(C, A)] + [x[:] for x in C]))
    if not hs:
        return 'unknown', '采样未得到有效 h'
    if min(hs) >= n:
        return 'yes', 'h=n ⟹ (5a) 自动'
    M, B, _ = Residual_sym(A, C, L0, q, rows, rest, syms, None)
    results = []
    for h0 in sorted(hs):
        if h0 >= n:
            results.append((h0, 'yes', 'h0=n：自动'))
            continue
        minM = _minors(M, h0 + 1, cap=cap_minors)
        minB = _minors(B, h0 + 1, cap=cap_minorsB)
        base = list(dict.fromkeys(minM + minB))
        # 选 h0-子式作为"非零见证"
        allw = _minors(B, h0) if h0 > 0 else [sp.Integer(1)]
        witnesses = allw
        truncated = False
        if h0 == 0:
            witnesses = [sp.Integer(1)]
        verdict = 'no'
        if len(witnesses) > 200:
            truncated = True
        for f in witnesses[:200]:
            eqs = base + [sp.expand(z * f - 1)]
            gens = eqs
            try:
                G = sp.groebner(gens, *(list(syms) + [z]), order='grevlex')
                els = list(G.exprs)
            except Exception as e:                        # noqa: BLE001
                return 'unknown', f'Gröbner 失败：{e}'
            if els != [sp.Integer(1)]:
                verdict = 'yes'
                break
        if verdict == 'no' and truncated:
            verdict = 'unknown'          # 见证被截断 ⟹ "空集"不可信
        results.append((h0, verdict, f'子式 M:{len(minM)} B:{len(minB)} 见证:{len(witnesses)}'))
    if any(v == 'yes' for _, v, _ in results):
        return 'yes', '；'.join(f'h0={h0}:{v}' for h0, v, _ in results)
    if all(v == 'no' for _, v, _ in results):
        return 'no', '**certified 空集**：' + '；'.join(f'h0={h0}:{v}' for h0, v, _ in results)
    return 'unknown', '；'.join(f'h0={h0}:{v}' for h0, v, _ in results)


def main():
    print('=== 精确消元（sympy）：逐图卡判定 $(5a)$ 的可满足性 ===')
    cases = [
        ('公开例子 q=3', None, 3),
        ('异常实例 q=3', (7, 2, 2, 4004), 3),
    ]
    import importlib.util as iu
    for tag, inst, q in cases:
        if inst is None:
            spec = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
            m = iu.module_from_spec(spec)
            spec.loader.exec_module(m)
            A, C, L0 = m.A, m.C, m.L0
        else:
            n, p, r, seed = inst
            A, C, L0 = QR.make_instance(n, p, r, seed * 23 + p * 11 + r)
        n = len(A)
        d = n - len(C) - q
        Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        k = len(Kc[0])
        print(f'{tag}：n={n} p={len(C)} r={len(L0)} q={q} d={d} k={k}，参数 {d * (k - d)}')
        if d * (k - d) > 3:
            print('  （参数 >2，跳过演示）')
            continue
        verdicts = []
        for rows in itertools.combinations(range(k), d):
            rest = [i for i in range(k) if i not in rows]
            v, why = certify_chart(A, C, L0, q, rows, rest)
            verdicts.append((rows, v, why))
            print(f'  图卡 rows={rows}: {v} —— {why}')
        if any(v == 'yes' for _, v, _ in verdicts):
            print('  ⟹ 该阶 (5a) **可满足**')
        elif all(v == 'no' for _, v, _ in verdicts):
            print('  ⟹ 该阶 (5a) **certified 不可满足**')
        else:
            print('  ⟹ 未决')


if __name__ == '__main__':
    main()
