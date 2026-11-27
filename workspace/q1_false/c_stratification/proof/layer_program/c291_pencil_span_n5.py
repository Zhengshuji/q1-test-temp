r"""c291：$n=5$ 的 pencil-span 问题（QA23 优先级 4）。

**专家给的精确提法**：给定交替形式对 $(\omega_0,\omega_1)$，判定
$$\operatorname{span}\{u\wedge v:\ \omega_0(u,v)=\omega_1(u,v)=0\}\overset{?}{=}A^\perp,\qquad A=\operatorname{span}\{\omega_0,\omega_1\}\subseteq\Lambda^2V^*.$$
用**齐次**铅笔 $s\omega_0+t\omega_1$（含 $\infty$）。

**本脚本**：对 $n=5$（$\dim\Lambda^2V=10$、$\dim A^\perp=8$），考察五类铅笔：
1. generic；2. 同余（$\omega_1=A\omega_0A^{\mathsf T}$）；3. 两个都 rank 2；
4. 共享核方向；5. rank 4 + rank 2。
对每类算 $\operatorname{span}(X)$（构造性采样：整个 $V_u$），与 $8$ 比较。

**证书**：若 span 达到 8（$\dim A^\perp$），则 $\operatorname{span}(X)=A^\perp$ **确定**。

用法：python proof/layer_program/c291_pencil_span_n5.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI

m = 5
PAIRS = [(i, j) for i in range(m) for j in range(i + 1, m)]


def skew_from(vec):
    F = [[Fr(0)] * m for _ in range(m)]
    for (i, j), x in zip(PAIRS, vec):
        F[i][j] = x
        F[j][i] = -x
    return F


def wedge_form(a, b):
    """2-形式 a∧b：F_ij = a_i b_j - a_j b_i。"""
    return [[a[i] * b[j] - a[j] * b[i] for j in range(m)] for i in range(m)]


def rank_skew(F):
    return AI.rank([row[:] for row in F])


def plucker(u, v):
    return [u[i] * v[j] - u[j] * v[i] for (i, j) in PAIRS]


def span_of_X(forms, rng, nsamp=300):
    """构造性采样：每个 u 取整个 V_u 的基。"""
    pts = []
    for _ in range(nsamp):
        u = [Fr(rng.randint(-3, 3)) for _ in range(m)]
        if all(x == 0 for x in u):
            continue
        eqs = [[sum(F[i][j] * u[j] for j in range(m)) for i in range(m)] for F in forms]
        ker = AI.nullspace(eqs)
        for base in ker:
            v = list(base)
            if all(x == 0 for x in v):
                continue
            p = plucker(u, v)
            if all(x == 0 for x in p):
                continue
            for F, a in zip(forms, [[F[i][j] for (i, j) in PAIRS] for F in forms]):
                val = sum(a[k] * p[k] for k in range(10))
                assert val == 0, f"点不在 L 中：a·p = {val}"
            pts.append(p)
    return pts


def main():
    rng = random.Random(20261031)
    print("n=5 的 pencil-span：span(X) 是否 = A^⊥（dim 8）？\n")
    print(f"{'类型':<28}{'rank(w0)':<10}{'rank(w1)':<10}{'点数':<7}{'span':<7}结论")

    cases = []
    # 1. generic
    for _ in range(3):
        v0 = [Fr(rng.randint(-2, 2)) for _ in range(10)]
        v1 = [Fr(rng.randint(-2, 2)) for _ in range(10)]
        cases.append(("generic", skew_from(v0), skew_from(v1)))
    # 2. 同余：w1 = A w0 A^T
    for _ in range(2):
        v0 = [Fr(rng.randint(-2, 2)) for _ in range(10)]
        F0 = skew_from(v0)
        A = [[Fr(rng.randint(-1, 1)) for _ in range(m)] for _ in range(m)]
        if AI.rank(A) < m:
            continue
        F1 = [[sum(A[i][k] * F0[k][l] * A[j][l] for k in range(m) for l in range(m)) for j in range(m)]
              for i in range(m)]
        cases.append(("同余 A w0 A^T", F0, F1))
    # 3. 两个都 rank 2（都是 a∧b）
    for _ in range(2):
        a = [Fr(rng.randint(-2, 2)) for _ in range(m)]
        b = [Fr(rng.randint(-2, 2)) for _ in range(m)]
        c = [Fr(rng.randint(-2, 2)) for _ in range(m)]
        d = [Fr(rng.randint(-2, 2)) for _ in range(m)]
        cases.append(("两个 rank 2", wedge_form(a, b), wedge_form(c, d)))
    # 4. 共享核方向 e0
    for _ in range(2):
        v0 = [Fr(rng.randint(-2, 2)) for _ in range(10)]
        v1 = [Fr(rng.randint(-2, 2)) for _ in range(10)]
        F0 = skew_from(v0)
        F1 = skew_from(v1)
        # 使 e0 同时是核：把第 0 行/列清零
        for j in range(m):
            F0[0][j] = Fr(0); F0[j][0] = Fr(0)
            F1[0][j] = Fr(0); F1[j][0] = Fr(0)
        cases.append(("共享核 e0（rank<=4）", F0, F1))
    # 5. rank 4 + rank 2
    for _ in range(2):
        a = [Fr(rng.randint(-2, 2)) for _ in range(m)]
        b = [Fr(rng.randint(-2, 2)) for _ in range(m)]
        v1 = [Fr(rng.randint(-2, 2)) for _ in range(10)]
        cases.append(("rank4 + rank2", skew_from(v1), wedge_form(a, b)))

    for name, F0, F1 in cases:
        pts = span_of_X([F0, F1], rng)
        rk = AI.rank(pts) if pts else 0
        verdict = "**证书：span = A^⊥** ✓" if rk >= 8 else f"下界 {rk} < 8（可能退化或采样不足）"
        print(f"{name:<28}{rank_skew(F0):<10}{rank_skew(F1):<10}{len(pts):<7}{rk:<7}{verdict}")

    print("\n注：A^⊥ 的维数是 10 − dim A；若 w0,w1 线性无关则 = 8，否则 = 9（此时是 D=1 情形）。")


if __name__ == '__main__':
    main()
