r"""c290：坍缩问题——$\operatorname{span}(X)=L$ 何时成立？（新方向 C）

**问题**：$X=\operatorname{Gr}(r,m)\cap\mathbb P(K)$，$K$ 由 $D$ 条线性条件切出（$\dim K=\binom mr-D$）。
问：$\operatorname{span}(X)=\mathbb P(K)$（等价地，$\dim\operatorname{span}= \binom mr-D$）何时成立？

**已知**：
- $r=1$：$\operatorname{Gr}(1,m)=\mathbb P^{m-1}$ 是整空间 ⟹ 恒有 $X=\mathbb P(K)$ ⟹ **恒坍缩**；
- $(r,m)=(2,4)$：$\operatorname{rank}(Q|_K)\ge2$（A2 §29.2c）⟹ 二次型张成整空间 ⟹ **恒坍缩**；
- 一般 $(r,m)$：**空白**（本脚本的第一步）。

**做法**（对 $(2,m)$，$m=4,5,6$）：
1. 取 $D$ 个随机整数反对称矩阵 $\omega_1,\dots,\omega_D$；$K=\bigcap_i\ker(\omega_i\text{-作用})$；
2. **采样点**：随机 $u$，解线性方程组 $\omega_i(u,v)=0$ 得 $v$ ⟹ $U=\operatorname{span}(u,v)$ 是 $X$ 的点；
3. 累积 Plücker 向量，算秩 ⟹ $\operatorname{span}(X)$ 维数的**下界**；
4. 与 $\dim L=\binom m2-D$ 比较。

**警告**：采样只给下界；若达到满维则 $\operatorname{span}(X)=L$ ✓（确定）；若未达到，可能是退化，也可能是采样遗漏。

用法：python proof/layer_program/c290_collapse.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI


def pairs(m):
    return [(i, j) for i in range(m) for j in range(i + 1, m)]


def plucker(u, v, m):
    out = []
    for (i, j) in pairs(m):
        out.append(u[i] * v[j] - u[j] * v[i])
    return out


def random_skew(m, rng):
    M = [[Fr(0)] * m for _ in range(m)]
    for (i, j) in pairs(m):
        x = Fr(rng.randint(-2, 2))
        M[i][j] = x
        M[j][i] = -x
    return M


def sample_points(forms, m, rng, nsamp=400):
    """采样 X 的点（Plücker 向量）。

    **构造性改进**：对每个 u，不只取一个 v，而是取**整个** $V_u=\\bigcap_i\\ker\\omega_i(u,\\cdot)$
    的基（维数 $\\ge m-D$），把所有 $u\\wedge v_j$ 都加入。这样每个 u 贡献 $m-D$ 个方向，
    而不是 1 个 ⟹ 低维情形也能张满。
    """
    pts = []
    for _ in range(nsamp):
        u = [Fr(rng.randint(-3, 3)) for _ in range(m)]
        if all(x == 0 for x in u):
            continue
        eqs = []
        for F in forms:
            row = [sum(F[i][j] * u[j] for j in range(m)) for i in range(m)]
            eqs.append(row)
        ker = AI.nullspace(eqs) if eqs else [[Fr(1) if i == k else Fr(0) for k in range(m)] for k in range(m)]
        for base in ker:                      # 整个 V_u 的**每个**基向量
            v = list(base)
            if all(x == 0 for x in v):
                continue
            p = plucker(u, v, m)
            if all(x == 0 for x in p):
                continue
            # CLAUDE.md 7.21：先 assert 基本不变量（点必须在 L 里！）
            for F in forms:
                a = [F[i][j] for (i, j) in pairs(m)]
                val = sum(a[k] * p[k] for k in range(len(p)))
                assert val == 0, f"采样点不在 L 中：a·p = {val}"
            pts.append(p)
    return pts


def main():
    rng = random.Random(20261031)
    print("坍缩问题：span(X) 的下界 vs dim L = C(m,2) − D\n")
    print(f"{'m':<4}{'D':<4}{'dim L':<8}{'样本点':<7}{'span 下界':<10}结论")
    for m in (4, 5, 6):
        for D in range(1, m):
            forms = [random_skew(m, rng) for _ in range(D)]
            pts = sample_points(forms, m, rng, nsamp=300)
            if not pts:
                print(f"{m:<4}{D:<4}{'?':<8}{0:<7}{'-':<10}无样本")
                continue
            dimL = len(pairs(m)) - D
            rk = AI.rank(pts)
            if rk >= dimL:
                verdict = "**证书：span=L**（达到 ≥ dim L ⟹ 确定）"
            else:
                verdict = f"下界 {rk} < {dimL}（退化，或采样不足）"
            print(f"{m:<4}{D:<4}{dimL:<8}{len(pts):<7}{rk:<10}{verdict}")
    forms, K = find_degenerate_24()
    if forms is not None:
        print("\n**退化实例（2,4）,D=3**：找到 rank(Q|_K)=1（Q|_K = L^2）")
        print("  ⟹ X = Q ∩ P(K) = P^1 ⟹ span(X) 维数 = 2 < dim L = 3 ⟹ **退化**")
        print("  三形式：", [[str(forms[t][i][j]) for (i,j) in pairs(4)] for t in range(3)])
    else:
        print("\n未找到 (2,4),D=3 的 rank-1 实例（可能不存在）")
    print("\n已知的确定性结论：r=1 恒坍缩；m=4、D=2 恒坍缩（A2 §29.2c）。")
    print("本表是 (2,m) 的**下界**数据；若某行达到满维，则该情形确定非退化。")




# ---------- 退化实例：找 rank(Q|_K)=1（Q|_K = L^2）的 (2,4),D=3 情形 ----------
def find_degenerate_24(trials=20000, seed=20261031):
    """dim K = 3 时 rank(Q|_K) 可以到 1 ⟹ X = P^1 ⟹ span 只有 2 维 ⟹ **退化**。"""
    rng = random.Random(seed)
    m = 4
    for _ in range(trials):
        forms = [random_skew(m, rng) for _ in range(3)]
        A = [[forms[t][i][j] for t in range(3)] for (i, j) in pairs(m)]
        # K = {p : A^T p = 0}，p 是 6 维
        eqs = [[A[k][t] for k in range(6)] for t in range(3)]
        K = AI.nullspace(eqs)
        if len(K) != 3:
            continue
        d = len(K)
        M = [[Fr(0)] * d for _ in range(d)]
        for i in range(d):
            M[i][i] = 2 * pluckerQ(K[i])
            for j in range(i + 1, d):
                ss = [K[i][k] + K[j][k] for k in range(6)]
                M[i][j] = M[j][i] = pluckerQ(ss) - pluckerQ(K[i]) - pluckerQ(K[j])
        if AI.rank(M) == 1:
            return forms, K
    return None, None


def pluckerQ(p):
    p12, p13, p14, p23, p24, p34 = p
    return p12 * p34 - p13 * p24 + p14 * p23

if __name__ == '__main__':
    main()
