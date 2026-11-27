"""reverse_construct.py —— 按构造生成 $\\varepsilon=0$ 的实例（专家 2026-11-04 §Step 2 的"反向设计"）

**目标**：不靠筛选，而是从结构出发造出满足
$$U_1=L_0A|_V=\\alpha\\,U_0=\\alpha L_0|_V\\quad(\\text{等价于 }(A-\\alpha I)V\\subseteq\\ker L_0)$$
的实例，同时保持 $(C,A)$ 可观测、$V=\\ker[C;CA]$ 恰好、且**非平凡**（$V\\not\\subseteq\\ker(A-\\alpha I)$，
否则 $V$ 含特征向量 ⟹ $q_{\\min}=\\infty$）。

**构造步骤**（全部在 $\\mathbb Q$ 上精确进行）：
1. 取定 $V=\\langle e_1,\\dots,e_{d_V}\\rangle$；
2. 取 $C$ 使 $\\ker C\\supseteq V$（$C$ 在前 $d_V$ 列为 0）且 $\\operatorname{rank}C=p$；
3. 取 $A$ 使 $A(V)\\subseteq\\ker C$（于是 $CA|_V=0$，$V\\subseteq\\ker[C;CA]$）；
4. 取 $\\alpha$，令 $K=(A-\\alpha I)V$；取 $L_0$ 满足 $L_0K=0$、$\\operatorname{rank}L_0=r$、
   $\\operatorname{row}L_0\\subseteq\\operatorname{row}\\mathcal O(C,A)$（用 $L_0=S\\,\\mathcal O$ 参数化 $S$）；
5. 检验：$\\dim\\ker[C;CA]=d_V$（恰好）、$(C,A)$ 与 $(L_0,A)$ 可观测、$\\varepsilon=0$（B.13d）、
   $V\\not\\subseteq\\ker(A-\\alpha I)$；
6. 在 $q_0$ 阶做整族检验并把候选分成 可行 / Type I / Type III。

用法：python -u tools/verification/reverse_construct.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import decide_symbolic as DS              # noqa: E402
from epsilon_zero_characterization import q_vanishes, restrict   # noqa: E402

F = Fraction


def nullspace_rows(Amat, ncols):
    """Amat x = 0 的解空间基（列表的列表）。"""
    return ZG.ker_cols_cols(Amat, ncols) if hasattr(ZG, 'ker_cols_cols') else _null(Amat, ncols)


def _null(Amat, ncols):
    Aq = [list(map(F, row)) for row in Amat]
    rows = len(Aq)
    piv = []
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, rows) if Aq[i][c] != 0), None)
        if p is None:
            continue
        Aq[r], Aq[p] = Aq[p], Aq[r]
        inv = Aq[r][c]
        Aq[r] = [v / inv for v in Aq[r]]
        for i in range(rows):
            if i != r and Aq[i][c] != 0:
                f = Aq[i][c]
                Aq[i] = [v - f * w for v, w in zip(Aq[i], Aq[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -Aq[i][fc]
        basis.append(v)
    return basis


def build_instance(n, p, r, dV, rng, bound=2):
    """按构造造一个实例；返回 (A, C, L0, 信息) 或 None。"""
    # 1) V = span(e_1..e_dV)（前 dV 个标准基向量）
    # 2) C：前 dV 列为 0，其余随机，rank p
    C = [[F(0)] * dV + [F(rng.randrange(-bound, bound + 1)) for _ in range(n - dV)]
         for _ in range(p)]
    if LQ.rank(C) != p:
        return None
    kerC = ZG.ker_cols(C)                      # n × (n-p)
    dK = len(kerC[0]) if (kerC and kerC[0]) else 0
    if dK < dV:
        return None
    # 3) A：A(V) ⊆ kerC。取 A 的前 dV 列（列 j<dV 就是 A e_j）落在 kerC 里，
    #    其余列随机。
    kerCv = [[kerC[i][k] for k in range(dK)] for i in range(n)]     # n × dK
    Acols = []
    for j in range(n):
        if j < dV:
            c = [F(rng.randrange(-bound, bound + 1)) for _ in range(dK)]
            col = [sum(kerCv[i][k] * c[k] for k in range(dK)) for i in range(n)]
        else:
            col = [F(rng.randrange(-bound, bound + 1)) for _ in range(n)]
        Acols.append(col)
    A = [[Acols[j][i] for j in range(n)] for i in range(n)]          # A[i][j]
    # 检验 V ⊆ ker[C;CA]
    CA = LQ.mul(C, A)
    Vc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
    dVk = len(Vc[0]) if (Vc and Vc[0]) else 0
    if dVk != dV:                              # 要求恰好
        return None
    O = QR.observability_matrix(A, C)
    n0 = LQ.rank(O)
    if n0 != n:
        return None
    # 4) α 与 K = (A − αI)V
    alpha = F(rng.randrange(-2, 3))
    Vb = [[F(1) if i == j else F(0) for i in range(n)] for j in range(dV)]   # 列 = e_j
    Kcols = []
    for j in range(dV):
        col = [A[i][j] - (alpha if i == j else F(0)) for i in range(n)]
        Kcols.append(col)
    Kr = [[Kcols[j][i] for j in range(dV)] for i in range(n)]        # n × dV
    rkK = LQ.rank(Kr)
    if rkK == 0:                               # V ⊆ ker(A−αI)：平凡（q_min=∞）
        return None
    # 取 L0 = S·O（保证 row L0 ⊆ row O），并要求 L0 K = 0、rank L0 = r
    Ot = [[O[i][j] for i in range(n)] for j in range(n0)]            # n0 × n（行空间基）
    # 未知数 S: r × n0；条件：对 Kr 的每一列 k，sum_s S[a][s] * (Ot[s]·k) = 0
    Amat = []
    for j in range(dV):
        Ok = [sum(Ot[s][i] * Kr[i][j] for i in range(n)) for s in range(n0)]
        for a in range(r):
            row = [F(0)] * (r * n0)
            for s in range(n0):
                row[a * n0 + s] = Ok[s]
            Amat.append(row)
    sol = _null(Amat, r * n0)
    if not sol:
        return None
    # 随机取组合，直到 rank L0 = r
    for _ in range(20):
        S = [sol[rng.randrange(len(sol))] for _ in range(1)]
        # 用随机线性组合造 r 行
        rows = []
        for a in range(r):
            coef = [F(rng.randrange(-2, 3)) for _ in range(len(sol))]
            rows.append([sum(coef[t] * sol[t][i] for t in range(len(sol))) for i in range(r * n0)])
        # 转成 r × n0
        Smat = [[rows[a][s] for s in range(n0)] for a in range(r)]
        L0 = [[sum(Smat[a][s] * Ot[s][j] for s in range(n0)) for j in range(n)] for a in range(r)]
        if LQ.rank(L0) != r:
            continue
        if LQ.rank([list(x) for x in C] + L0) != p + r:
            continue
        # 比例性（B.13d）与可观测性
        M0 = restrict(L0, Vc, n)
        M1 = restrict(LQ.mul(L0, A), Vc, n)
        if not q_vanishes(M0, M1, dV, r):
            continue
        if LQ.rank(QR.observability_matrix(A, L0)) != n:
            continue
        return A, C, L0, {'alpha': alpha, 'dV': dV, 'r1': LQ.rank([list(x) for x in C] + [list(x) for x in CA])}
    return None


def classify_family(A, C, L0, q, max_theta=4):
    """在 q 阶做整族检验；返回 (总数, 可行, TypeI, TypeIII) 或 None。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0]) if (Kc and Kc[0]) else 0
    if d <= 0 or d > k:
        return None
    r1 = LQ.rank([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    tot = feas = tI = tIII = 0
    for rows in itertools.combinations(range(k), d):
        for b in range(1, max_theta + 1):
            Z = DS.Z_from_theta(A, C, L0, q, rows, [F(b)] * (d * (k - d)))
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            tot += 1
            try:
                res = TC.analyse(A, C, L)
            except AssertionError:
                continue
            if res['five_b']:
                feas += 1
            elif res['h'] >= q + r1:
                tI += 1
            else:
                tIII += 1
    return (tot, feas, tI, tIII) if tot else None


def main():
    rng = random.Random(20261104)
    st = Counter()
    for trial in range(400):
        n = rng.choice([6, 7])
        p = 2
        r = 2
        dV = rng.choice([1, 2])
        made = build_instance(n, p, r, dV, rng)
        if made is None:
            st['build_fail'] += 1
            continue
        A, C, L0, info = made
        st['built'] += 1
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        out = classify_family(A, C, L0, q0)
        if out is None:
            st['no_candidates'] += 1
            continue
        tot, feas, tI, tIII = out
        st['tested'] += 1
        st[f'q0={q0}'] += 1
        if feas == 0 and tIII == tot:
            st['whole_family_typeIII'] += 1
            print(f'  ★ 整族 Type III：n={n} p={p} r={r} dV={dV} α={info["alpha"]} '
                  f'q0={q0} r1={info["r1"]}（{tot} 个候选全 Type III）')
        elif feas == 0:
            st['whole_family_typeI'] += 1
        else:
            st['feasible_exists'] += 1
    print('\n统计：', dict(st))


if __name__ == '__main__':
    main()
