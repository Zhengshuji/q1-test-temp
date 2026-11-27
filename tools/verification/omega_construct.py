"""omega_construct.py —— 在 $(5a)$ 的**可行集**内直接构造增广（WP2 第 2 步）

不用"在 $\\Theta$ 里盲抽"，改用 $(5a)$ 的**子空间形式**：

$$(5a)\\iff \\operatorname{row}(\\mathcal L A)\\subseteq\\operatorname{row}(\\mathcal L)+W,\\qquad W=\\operatorname{row}[C;CA].$$

于是：

1. **闭包** $V_{\\min}$：最小的 $V\\supseteq\\operatorname{row}L_0$ 且 $VA\\subseteq V+W$（贪心加行，直至封闭）。
   它的维数应当等于 $q_0$（`c208_q0_lower_bound.eta_and_q0`）——本脚本把它当**交叉验证**；
2. **一步前像**：$U=\\{x:\\ xA\\in V_{\\min}+W\\}$。任何 $u\\in U$ 加到 $V_{\\min}$ 上仍满足 $(5a)$
   （因为 $uA\\in V_{\\min}+W\\subseteq V'+W$）；
3. 抽样：$\\mathcal L$ 的行 = $V_{\\min}$ 的基 + 从 $U$ 中取的 $q-q_0$ 个模 $V_{\\min}$ 独立的向量；
4. 逐点 `assert` $(5a)$，再用 Toeplitz 判据判 $(5b)$。

这样**每个样本都是 $(5a)$-可行的真实增广**，$(5b)$ 的统计才有意义。

用法：python tools/verification/omega_construct.py
"""

import os
import random
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def row_basis(rows):
    out = []
    for r in rows:
        if LQ.rank(out + [r]) > len(out):
            out.append(list(r))
    return out


def rowA(x, A):
    n = len(x)
    return [sum(x[i] * A[i][j] for i in range(n)) for j in range(len(A[0]))]


def closure(A, C, L0):
    """最小 $V\\supseteq\\operatorname{row}L_0$ 且 $VA\\subseteq V+W$，返回行的基。"""
    CA = LQ.mul(C, A)
    W = row_basis([row[:] for row in C] + [row[:] for row in CA])
    V = row_basis([row[:] for row in L0])
    while True:
        VW = row_basis(V + W)
        grown = False
        for x in list(V):
            y = rowA(x, A)
            if LQ.rank(VW + [y]) > len(VW):
                V.append(y)
                VW = row_basis(VW + [y])
                grown = True
        if not grown:
            return V


def preimage(A, S):
    """$\\{x:\\ xA\\in\\operatorname{span}S\\}$ 的行的基。"""
    P = LQ.nullspace(S)                 # 与 S 的行正交的向量（行）
    if not P:
        return [list(e) for e in ([F(1) if i == j else F(0) for j in range(len(A))] for i in range(len(A)))]
    M = [[sum(P[i][k] * A[j][k] for k in range(len(A))) for j in range(len(A))] for i in range(len(P))]
    # M = P A^T，行；U = {x : M x^T = 0}
    return [list(r) for r in LQ.nullspace(M)]


def sample_omega_one_step(A, C, L0, q, n_samples, seed):
    """在 $V_{\\min}$ + $U$ 的构造族中抽样（返回合格 $L$ 的列表）。"""
    rng = random.Random(seed)
    Vmin = closure(A, C, L0)
    W = row_basis([row[:] for row in C] + [row[:] for row in LQ.mul(C, A)])
    U = preimage(A, row_basis(Vmin + W))
    need = q - len(Vmin)
    if need < 0:
        return []
    out, seen = [], set()
    for _ in range(n_samples * 8):
        if need == 0:
            L = [row[:] for row in Vmin]
        else:
            L = [row[:] for row in Vmin]
            for _t in range(need):
                u = [F(0)] * len(A)
                for coef_i in range(len(U)):
                    a = F(rng.randrange(-3, 4))
                    if a:
                        for j in range(len(A)):
                            u[j] += a * U[coef_i][j]
                if LQ.rank(L + [u]) > len(L):
                    L.append(u)
            if len(L) != q:
                continue
        key = tuple(tuple(str(x) for x in row) for row in L)
        if key in seen:
            continue
        seen.add(key)
        if LQ.rank([row[:] for row in L] + [row[:] for row in L0]) != LQ.rank(L):
            continue
        assert LQ.condA(A, C, L), '(5a) 应自动成立'
        out.append(L)
        if len(out) >= n_samples:
            break
    return out


def sample_chains(A, C, L0, q, n_chains, seed):
    """链式抽样：每次加入 $U=\\{x: xA\\in V+W\\}$ 中的方向，**逐维重算** $U$。

    这样能覆盖"某方向只有在 $V$ 变大之后才可行"的情形（比一步前像更广）。
    """
    rng = random.Random(seed)
    Vmin = closure(A, C, L0)
    W = row_basis([row[:] for row in C] + [row[:] for row in LQ.mul(C, A)])
    need = q - len(Vmin)
    if need < 0:
        return []
    out, seen = [], set()
    for _ in range(n_chains):
        V = [row[:] for row in Vmin]
        ok = True
        while len(V) < q:
            U = preimage(A, row_basis(V + W))
            placed = False
            for _try in range(40):
                u = [F(0)] * len(A)
                for i in range(len(U)):
                    a = F(rng.randrange(-3, 4))
                    if a:
                        for j in range(len(A)):
                            u[j] += a * U[i][j]
                if LQ.rank(V + [u]) > len(V):
                    V.append(u)
                    placed = True
                    break
            if not placed:
                ok = False
                break
        if not ok:
            continue
        key = tuple(tuple(str(x) for x in row) for row in V)
        if key in seen:
            continue
        seen.add(key)
        if LQ.rank([row[:] for row in V] + [row[:] for row in L0]) != LQ.rank(V):
            continue
        assert LQ.condA(A, C, V), '(5a) 应自动成立'
        out.append(V)
    return out


def main():
    print('=== 在 (5a) 可行集内构造式抽样（链式前像），再判 (5b) ===')
    tot = dict(inst=0, qmin_hit=0, samples=0, feasible=0)
    for n in (5, 6, 7):
        for seed in (1000, 1001, 1002, 1003):
            A, C, L0 = make_instance(n, seed)
            q0 = Q0.eta_and_q0(A, C, L0)[0]          # 功能维数（P1 的 Ση_j）
            Vmin = closure(A, C, L0)                  # $(5a)$ 下的最小**行数**
            tot['inst'] += 1
            # q0 是下界；闭包给出精确的最小行数，二者可以严格不等（见 attempt 文档）
            assert len(Vmin) >= q0, f'闭包维数 {len(Vmin)} < q0 {q0}（n={n}, seed={seed}）'
            qlo = len(Vmin)
            line = []
            first_hit = None
            for q in range(qlo, n + 1):
                samples = sample_chains(A, C, L0, q, 10, seed * 31 + q)
                if not samples:
                    continue
                tot['samples'] += len(samples)
                feas = []
                for L in samples:
                    res = TC.analyse(A, C, L)
                    if res['five_b']:
                        feas.append((L, res['eps_smith']))
                tot['feasible'] += len(feas)
                line.append(f'q={q}:{len(feas)}/{len(samples)}')
                if feas and first_hit is None:
                    first_hit = q
            verdict = (f'q_min={first_hit}（精确）' if first_hit == qlo + 1 else
                       f'q_min<={first_hit}（上界）' if first_hit else 'q_min 未知（≤n 内未找到见证）')
            print(f'  n={n} seed={seed} q0={q0} 闭包={len(Vmin)}  ' + ' '.join(line) + '  → ' + verdict)
            if first_hit == qlo + 1:
                tot['qmin_hit'] += 1
    print(f'\n合计：实例 {tot["inst"]}，样本 {tot["samples"]}，其中 (5b) 成立 {tot["feasible"]}；'
          f'精确确定 q_min 的实例 {tot["qmin_hit"]} 个')
    print('注：这是 $\\Omega$ 的一个**构造性子族**（$V_{\\min}$ + 一步前像），不是整个 $\\Omega$。')


if __name__ == '__main__':
    main()
