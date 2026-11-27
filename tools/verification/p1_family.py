"""p1_family.py —— P1（Fernando, arXiv:2609.33615）§V 的**最小增广完备族**参数化（专家 WP2 第一步）

论文 §V 的构造（本文件只实现矩阵层面，完备性引用论文）：

1. $N_C$（$n\\times d_C$）= $\\ker C$ 的基，$d_C=n-p$；
2. 取 $T$（$d_C\\times d_C$）使 $L_0N_CT=[I_r\\ 0]$；$s:=d_C-r$；$k:=q_0-r$（$q_0=\\sum_j\\eta_j$）；
3. 对每个 $J\\subseteq\\{1..s\\}$、$|J|=k$，$Y_J(\\Theta)\\in\\mathbb R^{k\\times s}$ 的第 $J$ 列为 $I_k$、
   其余列为 $\\Theta$；$W_J(\\Theta)=\\operatorname{diag}(I_r,\\ Y_J(\\Theta))$；
4. 原坐标下的增广：$L(\\Theta)=W_J(\\Theta)\\,(N_CT)^{+}$（$(N_CT)^{+}$ 为左逆），
   于是 $L(\\Theta)(N_CT)=W_J(\\Theta)$ ⟹ $\\operatorname{row}L_0\\subseteq\\operatorname{row}L(\\Theta)$、
   $\\operatorname{rank}L(\\Theta)=q_0$。

**(A) 与 lift 无关**（$N_CT$ 看不见 $\\operatorname{row}C$ 的分量）；**(5b) 也与 lift 无关**：若把 $c\\in\\operatorname{row}C$
加到一行上，铅笔行空间只增加 $\\lambda c-cA\\in\\operatorname{span}_{\\mathbb C[\\lambda]}(C,CA)$。

本脚本：构造该族，逐点断言 $(5a)$ 与维数，并统计**可行 $\\Theta$ 的比例**（generic 可行性的操作化），
给出显式可行点（若有）。

用法：python tools/verification/p1_family.py
"""

import itertools
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger', 'tools/p_algorithm'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


# ---------------------------------------------------------------- 精确线性代数小工具

def left_inverse(M, name='M'):
    """$M$ 为 $n\\times k$ 满列秩；返回 $X$（$k\\times n$）使 $XM=I_k$。"""
    n = len(M)
    k = len(M[0])
    X = []
    for i in range(k):
        aug = [[M[t][j] for t in range(n)] + [F(1) if i == j else F(0)] for j in range(k)]
        R, piv = LQ.rref(aug)
        for row in R:
            assert not (all(row[t] == 0 for t in range(n)) and row[n] != 0), f'{name} 的左逆不存在'
        x = [F(0)] * n
        for r_i, p in enumerate(piv):
            if p < n:
                x[p] = R[r_i][n]
        for j in range(k):
            got = sum(x[t] * M[t][j] for t in range(n))
            assert got == (F(1) if i == j else F(0)), f'{name} 的左逆校验失败'
        X.append(x)
    return X


def right_inverse_rows(B, name='B'):
    """$B$ 为 $r\\times m$ 满**行**秩；返回 $T_1$（$m\\times r$）使 $BT_1=I_r$。"""
    r = len(B)
    m = len(B[0])
    T1 = [[F(0)] * r for _ in range(m)]
    for j in range(r):
        aug = [[B[i][t] for t in range(m)] + [F(1) if i == j else F(0)] for i in range(r)]
        R, piv = LQ.rref(aug)
        for row in R:
            assert not (all(row[t] == 0 for t in range(m)) and row[m] != 0), f'{name} 的右逆不存在'
        for r_i, p in enumerate(piv):
            if p < m:
                T1[p][j] = R[r_i][m]
    for i in range(r):
        for j in range(r):
            got = sum(B[i][t] * T1[t][j] for t in range(m))
            assert got == (F(1) if i == j else F(0)), f'{name} 的右逆校验失败'
    return T1


def nullspace_cols(M):
    """$\\ker M$ 的基，返回**列**（$m\\times k$）。"""
    rows = LQ.nullspace(M)
    m = len(M[0]) if M else 0
    if not rows:
        return [[] for _ in range(m)]
    return [[row[j] for row in rows] for j in range(m)]


# ---------------------------------------------------------------- P1 族

def family_data(A, C, L0):
    n = len(A)
    p = len(C)
    r = len(L0)
    assert LQ.rank([row[:] for row in C] + [row[:] for row in L0]) == p + r, '需 rank[C;L0]=p+r'
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    Nc = nullspace_cols(C)                       # n × dC（列）
    dC = len(Nc[0])
    assert dC == n - p, f'dim ker C = {dC} != n-p = {n - p}'
    B = [[sum(L0[i][t] * Nc[t][j] for t in range(n)) for j in range(dC)] for i in range(r)]
    assert LQ.rank(B) == r, f'rank(L0 Nc) = {LQ.rank(B)} != r = {r}'
    s = dC - r
    k = q0 - r
    assert 0 <= k <= s, f'k={k} 超出 [0, s={s}]'
    T1 = right_inverse_rows(B, 'L0*Nc')           # dC × r
    T2 = nullspace_cols(B)                        # dC × s
    assert (len(T2[0]) if s > 0 else 0) == s
    T = [[T1[i][j] for j in range(r)] + ([T2[i][j] for j in range(s)] if s > 0 else [])
         for i in range(dC)]
    assert LQ.rank(T) == dC, 'T 应可逆'
    NcT = [[sum(Nc[i][j] * T[j][t] for j in range(dC)) for t in range(dC)] for i in range(n)]
    assert LQ.rank(NcT) == dC, 'Nc T 应满列秩'
    P = left_inverse(NcT, 'Nc*T')                 # dC × n
    return dict(q0=q0, r=r, s=s, k=k, dC=dC, Nc=Nc, P=P, T=T)


def chart_L(fd, J, theta, k=None):
    """图卡 $J$ 与参数 $\\Theta$（行优先展平的长度 $k(s-k)$ 向量）→ $L(\\Theta)$（$(r+k)\\times n$）。

    $k$ 缺省取 $q_0-r$（最小增广）；给 $k=q-r$ 即得**任意阶 $q$** 的候选族（同一构造）。
    """
    k = fd['k'] if k is None else k
    s, r, dC = fd['s'], fd['r'], fd['dC']
    q0 = r + k
    Y = [[F(0)] * s for _ in range(k)]
    rest = [j for j in range(s) if j not in J]
    for i, j in enumerate(J):
        Y[i][j] = F(1)
    for i in range(k):
        for t, j in enumerate(rest):
            Y[i][j] = theta[i * len(rest) + t]
    W = [[F(0)] * dC for _ in range(q0)]
    for i in range(r):
        W[i][i] = F(1)
    for i in range(k):
        for j in range(s):
            W[r + i][r + j] = Y[i][j]
    n = len(fd['P'][0])
    return [[sum(W[i][j] * fd['P'][j][t] for j in range(dC)) for t in range(n)] for i in range(q0)]


def check_L(A, C, L0, L):
    """断言**维数/包含**（这是族的定义），**测** $(5a)$ 与 $(5b)$（它们是对 $\\Theta$ 的条件）。"""
    assert LQ.rank(L) == len(L), f'rank L = {LQ.rank(L)} != {len(L)}'
    assert LQ.rank([row[:] for row in L] + [row[:] for row in L0]) == len(L), 'row L0 ⊆ row L 失败'
    cond_a = LQ.condA(A, C, L)
    res = TC.analyse(A, C, L) if cond_a else None
    return cond_a, res


def main():
    print('=== P1 最小增广族：逐点核验 (5a) 与可行性密度 ===')
    tot = dict(inst=0, charts=0, sampled=0, feasible=0)
    for n in (5, 6, 7):
        for seed in (1000, 1001, 1002):
            A, C, L0 = make_instance(n, seed)
            try:
                fd = family_data(A, C, L0)
            except AssertionError as e:
                print(f'  n={n} seed={seed}: 跳过（{e}）')
                continue
            tot['inst'] += 1
            k, s, q0 = fd['k'], fd['s'], fd['q0']
            charts = list(itertools.combinations(range(s), k))
            tot['charts'] += len(charts)
            witness, feas_ct, samp_ct = None, 0, 0
            for J in charts:
                nrest = k * (s - k)
                thetas = [[F(0)] * nrest]
                for m in range(1, 6):
                    thetas.append([F((m * 7 + t * 3) % 5 - 2) for t in range(nrest)])
                for th in thetas:
                    L = chart_L(fd, J, th)
                    samp_ct += 1
                    cond_a, res = check_L(A, C, L0, L)
                    if cond_a:
                        feas_ct += 1          # 先数 (5a) 成立的比例
                        if res['five_b'] and witness is None:
                            witness = (J, th, res['eps_smith'])
            tot['sampled'] += samp_ct
            tot['feasible'] += feas_ct
            if witness:
                tail = f'；首个 (5b) 可行点 J={witness[0]} eps={witness[2]}'
            elif feas_ct:
                tail = '；有 (5a) 点但无 (5b) 点'
            else:
                tail = '；(5a) 全不成立'
            print(f'  n={n} seed={seed}: q0={q0} r={fd["r"]} s={s} k={k} 图卡 {len(charts)}；'
                  f'采样 {samp_ct}，(5a) 成立 {feas_ct}' + tail)
    print(f'\n合计：实例 {tot["inst"]}，图卡 {tot["charts"]}，采样 {tot["sampled"]}，'
          f'(5a) 成立 {tot["feasible"]}（密度 {tot["feasible"]/max(1,tot["sampled"]):.2%}）')
    print('注：采样只用于估计密度与找见证；"全部可行/全部不可行"都不是结论。')


if __name__ == '__main__':
    main()


def sample_q(A, C, L0, q, n_per_chart=6, seed=0):
    """在**任意阶** $q$ 的候选族上抽样：返回 [(J, theta, L)]（只保证维数/包含，不保证 $(5a)$）。"""
    fd = family_data(A, C, L0)
    r, s = fd['r'], fd['s']
    k = q - r
    if k < 0 or k > s:
        return []
    out = []
    charts = list(itertools.combinations(range(s), k))
    for J in charts:
        nrest = k * (s - k)
        thetas = [[F(0)] * nrest]
        for m in range(1, n_per_chart):
            thetas.append([F((seed * 13 + m * 7 + t * 3) % 5 - 2) for t in range(nrest)])
        for th in thetas:
            out.append((J, th, chart_L(fd, J, th, k=k)))
    return out
