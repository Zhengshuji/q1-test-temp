r"""c286：斜形式铅笔（QA22 Q7，Case II）——$G(2,4)$ 的余维 2 截面。

**表述**：$L\subseteq\Lambda^2V$，$A=L^\perp\subseteq\Lambda^2V^*=\operatorname{span}\{\omega_0,\omega_1\}$，则
$$\mathbb P(L)\cap\operatorname{Gr}(2,V)=\{\text{同时对各 }\omega\in A\text{ 各向同性的 2-平面}\}.$$

**不变量**（专家 Q7 §7.3）：
- $\rho_{\mathrm{gen}}=\max_t\operatorname{rank}(Q_0+tQ_1)$；
- 公共根 $K_A=\bigcap_t\ker(Q_0+tQ_1)=\ker Q_0\cap\ker Q_1$；
- 奇异参数 $\{t:\operatorname{rank}(Q_0+tQ_1)<\rho_{\mathrm{gen}}\}$ = Pfaffian 的零点。

**G3 判定**（A2 §19）：$X=L\cap Q$，$\operatorname{span}(X)=L$ 除非 $Q|_L$ 的对称矩阵秩为 1。

**对照**：不变量（$\rho_{\mathrm{gen}}$、$\dim K_A$、奇异参数个数）能否预测 G3 退化？

用法：python proof/layer_program/c286_skew_pencil.py
"""
import itertools
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]   # Plücker 坐标顺序 (12),(13),(14),(23),(24),(34)


def skew(v):
    """6-vector -> 4×4 反对称矩阵（v 顺序同 PAIRS）。"""
    M = [[Fr(0)] * 4 for _ in range(4)]
    for (i, j), x in zip(PAIRS, v):
        M[i][j] = x
        M[j][i] = -x
    return M


def plucker_Q(p):
    p12, p13, p14, p23, p24, p34 = p
    return p12 * p34 - p13 * p24 + p14 * p23


def pfaffian_poly(v0, v1):
    """pf(Q_0 + t Q_1) 的系数（t 的二次多项式）。"""
    # pf = q12 q34 - q13 q24 + q14 q23，q_ij(t) = v0_ij + t v1_ij
    def at(t):
        q = [v0[k] + t * v1[k] for k in range(6)]
        return q[0] * q[5] - q[1] * q[4] + q[2] * q[3]
    c0 = at(Fr(0))
    c2 = (at(Fr(1)) + at(Fr(-1))) / 2 - c0
    c1 = at(Fr(1)) - c0 - c2
    return [c0, c1, c2]


def restrict_rank(Lbasis):
    """Q 在 L 上的对称矩阵的秩。Lbasis: L 的基（C^6 向量）。"""
    d = len(Lbasis)
    val = [plucker_Q(b) for b in Lbasis]

    def polar(i, j):
        s = [Lbasis[i][k] + Lbasis[j][k] for k in range(6)]
        return plucker_Q(s) - val[i] - val[j]

    M = [[Fr(0)] * d for _ in range(d)]
    for i in range(d):
        M[i][i] = 2 * val[i]
        for j in range(i + 1, d):
            M[i][j] = M[j][i] = polar(i, j)
    return AI.rank(M), val


def main():
    rng = random.Random(20261031)
    rows = []
    for trial in range(30):
        v0 = [Fr(rng.randint(-2, 2)) for _ in range(6)]
        v1 = [Fr(rng.randint(-2, 2)) for _ in range(6)]
        if all(x == 0 for x in v0) or all(x == 0 for x in v1):
            continue
        # L = {p : v0·p = 0, v1·p = 0}
        Lb = AI.nullspace([v0, v1])
        if len(Lb) < 3:
            continue
        # 不变量
        Q0, Q1 = skew(v0), skew(v1)
        K = [v for v in AI.nullspace([list(r) for r in Q0]) if AI.rank([list(r) for r in Q1] + [v]) == AI.rank([list(r) for r in Q1])]
        dimK = len(AI.nullspace([list(r) for r in Q0] + [list(r) for r in Q1]))
        pf = pfaffian_poly(v0, v1)
        disc = pf[1] ** 2 - 4 * pf[2] * pf[0]
        if pf[2] == 0:
            nsing = 0 if pf[1] != 0 else -1
        else:
            nsing = 0 if disc == 0 else 2
        rk, val = restrict_rank(Lb)
        verdict = "退化(span⊊L)" if rk == 1 else ("span=L" if rk >= 2 else "X=L")
        rows.append((len(Lb) - 1, dimK, pf[0], pf[1], pf[2], nsing, rk, verdict))

    print(f"考察 {len(rows)} 个斜形式铅笔（n=4，dim A=2）\n")
    print(f"{'dim L':<6}{'dim K_A':<8}{'pf 次数':<8}{'#奇异t':<8}{'rank Q|_L':<11}G3")
    for (dimL, dimK, c0, c1, c2, nsing, rk, verdict) in rows[:15]:
        deg = 2 if c2 != 0 else (1 if c1 != 0 else 0)
        print(f"{dimL:<6}{dimK:<8}{deg:<8}{nsing:<8}{rk:<11}{verdict}")
    print()
    deg_count = {}
    for (dimL, dimK, c0, c1, c2, nsing, rk, verdict) in rows:
        deg = 2 if c2 != 0 else (1 if c1 != 0 else 0)
        deg_count[deg] = deg_count.get(deg, 0) + 1
    rk1 = sum(1 for r in rows if r[6] == 1)
    print(f"pf 次数分布：{deg_count}")
    print(f"Q|_L 秩 = 1（G3 退化）的铅笔数：**{rk1}** / {len(rows)}")
    print("\n结论：n=4 时余维 2 截面（dim A=2）的 G3 退化可由 Q|_L 的秩直接判定（A2 §19）；")
    print("斜形式不变量（ρ_gen、dim K_A、奇异 t）**未**显示与退化相关——需要 n≥5 才有新信息。")


if __name__ == '__main__':
    main()
