"""middle_counterexample.py —— **定向搜索**中间层（s>0）上"失败"的实例，检验"中间层永不失败"猜想

**猜想（待检验）**：可容许（$(5a)$）且 $s=\\dim(V\\cap\\mathcal Z)>0$ 的 $\\mathcal Z$ **永不失败**。
等价形式（用 B.12）：若 $\\dim\\ker(\\mathcal L|_V)=s>0$，则 $U=\\mathcal L(V)$ 不含 $\\Lambda$ 的特征向量。

**定向构造**（利用 B.16b 的必要条件 $A(S)\\subseteq\\mathcal Z$）：
1. $W=V\\cap K$，取 $W'=\\{s\\in W: As\\in K\\}$；
2. 取 $s$ 维 $S\\subseteq W'$；
3. 把 $S$ **和** $A(S)$ 一起扩成 $\\dim d$ 的 $\\mathcal Z\\subseteq K$（要求 $AS\\subseteq\\mathcal Z$）；
4. 检查 $(5a)$；成立则检查 $(5b)$（B.12），统计 (s, 可容许, 失败)。

若找到 可容许 ∧ 失败 且 s>0 的实例 ⟹ **猜想被推翻**。

用法：python -u tools/verification/middle_counterexample.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter, defaultdict

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction


def basis_of(M, n):
    """返回矩阵（n×k）的列空间的一组基（n×rk）。"""
    k = len(M[0]) if (M and M[0]) else 0
    rk = ZG.bool_rank(ZG.cols_to_rows(M)) if k else 0
    if rk == 0:
        return [[] for _ in range(n)]
    # 取线性无关的子集
    keep = []
    for j in range(k):
        cand = keep + [j]
        sub = [[M[i][t] for t in cand] for i in range(n)]
        if ZG.bool_rank(ZG.cols_to_rows(sub)) == len(cand):
            keep = cand
    return [[M[i][j] for j in keep] for i in range(n)]


def rand_combo(pool, k, rng):
    n = len(pool)
    m = len(pool[0]) if (pool and pool[0]) else 0
    out = [[F(0)] * k for _ in range(n)]
    for j in range(k):
        coef = [F(rng.randrange(-2, 3)) for _ in range(m)]
        for i in range(n):
            out[i][j] = sum(pool[i][t] * coef[t] for t in range(m))
    return out


def extend_with_AS(S, AS, K, d, rng, tries=60):
    """把 S 与 A(S) 一起扩成 dim d 的 Z ⊆ K。"""
    n = len(K)
    s = len(S[0]) if (S and S[0]) else 0
    for _ in range(tries):
        base = [[S[i][j] for j in range(s)] for i in range(n)]
        extra_pool = K
        need = d - s
        if need <= 0:
            Z = base
        else:
            R = rand_combo(extra_pool, need, rng)
            Z = [[base[i][j] for j in range(s)] + [R[i][j] for j in range(need)] for i in range(n)]
        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            continue
        # 要求 A S ⊆ Z
        rkZ = LQ.rank(Z)
        aug = [Z[i][:] + AS[i][:] for i in range(n)]
        if LQ.rank(aug) != rkZ:
            continue
        return Z
    return None


def main():
    rng = random.Random(20261104)
    st = Counter()
    per_s = defaultdict(lambda: [0, 0, 0])
    counter = None
    for trial in range(30000):
        n = rng.choice([6, 7, 8])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if 2 * p + r >= n:          # 需要 2p+r < n 才有 V∩K ≠ 0 的可能
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank(QR.observability_matrix(A, C)) != n:
            continue
        if LQ.rank(QR.observability_matrix(A, L0)) != n:
            continue
        CA = LQ.mul(C, A)
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (V and V[0] and K and K[0]):
            continue
        dV, dK = len(V[0]), len(K[0])
        W = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA] + [list(x) for x in L0])
        w = len(W[0]) if (W and W[0]) else 0
        if w == 0:
            continue
        st['W_ne0'] += 1
        # W' = {s ∈ W : As ∈ K}：取 W 的基，求 A s ∈ K 的线性条件
        AW = LQ.mul(A, W)
        rkK = LQ.rank(K)
        aug = [K[i][:] + AW[i][:] for i in range(n)]
        if LQ.rank(aug) != rkK:
            st['A_W_not_in_K'] += 1
            continue
        # 取 S = W 的随机 s 维子空间（s 从 1 到 min(dK, w)）
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        n0 = LQ.rank(QR.observability_matrix(A, C))
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d <= 0 or d > dK:
                continue
            for s in range(1, min(d, w) + 1):
                S = rand_combo(W, s, rng)
                if S is None or ZG.bool_rank(ZG.cols_to_rows(S)) != s:
                    continue
                AS = LQ.mul(A, S)
                Z = extend_with_AS(S, AS, K, d, rng)
                if Z is None:
                    st['extend_fail'] += 1
                    continue
                L = ZG.L_from_Z(A, C, L0, Z, q)
                if L is None:
                    continue
                st['built'] += 1
                per_s[s][0] += 1
                if not LQ.condA(A, C, L):
                    continue
                per_s[s][1] += 1
                ok, why = OT.observability_ok(A, C, L)
                if not ok:
                    per_s[s][2] += 1
                    if counter is None:
                        # 只记录"非平凡"反例：q ≥ 2 且 U = L(V) 真包含于 C^q
                        rkL = LQ.rank(L)
                        if q >= 2 and rkL < q:
                            counter = (A, C, L0, Z, q, s, why)
                            print(f'★ 非平凡反例：s={s}, q={q}, rank L={rkL}, (5a)成立, (5b)失败（{why}）')
                            print('  A =', [[str(x) for x in row] for row in A])
                            print('  C =', [[str(x) for x in row] for row in C])
                            print('  L0=', [[str(x) for x in row] for row in L0])
                            print('  Z =', [[str(x) for x in row] for row in Z])
                        else:
                            st['trivial_counter(q=1 or U=C^q)'] += 1
        if counter is not None:
            break
    print('\n统计：', dict(st))
    print(f'{"s":>2} {"样本":>7} {"可容许":>7} {"失败":>6}')
    for s in sorted(per_s):
        n_, adm, fail = per_s[s]
        print(f'{s:>2} {n_:>7} {adm:>7} {fail:>6}')
    if counter is None:
        print('\n未找到反例（s>0 且可容许且失败）——与猜想一致（但这是搜索，不是证明）')


if __name__ == '__main__':
    main()
