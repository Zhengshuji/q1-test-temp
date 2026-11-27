"""kr_ranks.py —— 落实专家 §8.2：高阶秩增长 $\\Delta_k$ 与阶差的关系

定义 $r_k=\\operatorname{rank}[C;CA;\\dots;CA^k]$、$\\Delta_k:=r_k-r_{k-1}$（$r_0=p$），
故 $\\Delta_1=r_1-p=\\rho$；$\\Delta_k$ 的数等于"可观测指标 $\\ge k$ 的个数"（对偶于可控性指标）。

问题（专家 §8.2）：两个系统若 $(p,r,r_1)$ 相同、但 $\\Delta_k$ 分布不同（例如一个前几步增长快、另一个集中在少数
Krylov 链上），最小阶行为是否不同？

本脚本：对 $\\rho=2$ 的实例，记录 $\\Delta$ 剖面与 $q_{\\min}-q_0$，做列联表。

用法：python -u tools/verification/kr_ranks.py
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
import decide_symbolic as DS              # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction


def delta_profile(A, C, n, p):
    """$\\Delta_k$（$k=1..$），$r_k=\\operatorname{rank}[C;CA;\\dots;CA^k]$ 逐次堆叠。"""
    stacked = [list(x) for x in C]
    prev = LQ.rank(stacked)
    prof = []
    Ak = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for k in range(1, n + 1):
        Ak = LQ.mul(Ak, A)
        stacked = stacked + [list(x) for x in LQ.mul(C, Ak)]
        rk = LQ.rank(stacked)
        prof.append(rk - prev)
        prev = rk
        if rk == n:
            break
    return tuple(prof)


def _matpow(A, k, n):
    """$A^k$（精确）。"""
    M = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        M = LQ.mul(M, A)
    return M


def terminal_L(A, C, L0, n, p, r, rng):
    q = n - p
    need = q - r
    for _ in range(200):
        extra = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(need)]
        L = [list(x) for x in L0] + extra
        if LQ.rank(L) != q and q > 0:
            continue
        if LQ.rank([list(x) for x in C] + L) != n:
            continue
        return L
    return None


def main():
    rng = random.Random(20261130)
    tab = defaultdict(lambda: [0, 0])     # profile -> [samples, sum(gap)]
    for trial in range(1500):
        n = rng.choice([6, 7])
        p = 2
        r = rng.choice([1, 2])
        if p + r >= n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank([list(x) for x in C] + L0) != p + r:
            continue
        O = QR.observability_matrix(A, C)
        n0 = LQ.rank(O)
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        r1 = LQ.rank([list(x) for x in CA] + [list(x) for x in C])
        if r1 != p + 2:                    # 只看 rho=2
            continue
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        prof = delta_profile(A, C, n, p)
        qmin = None
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d < 0 or d > k:
                continue
            if d == 0:
                L = terminal_L(A, C, L0, n, p, r, rng)
                cands = [L] if L is not None else []
            else:
                cands = []
                for rows in itertools.combinations(range(k), d):
                    Z = DS.Z_from_theta(A, C, L0, q, rows, [F(0)] * (d * (k - d)))
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                        continue
                    try:
                        L = ZG.L_from_Z(A, C, L0, Z, q)
                    except AssertionError:
                        continue
                    cands.append(L)
            for L in cands:
                if L is None or not LQ.condA(A, C, L):
                    continue
                V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
                ok = True if not (V and V[0]) else bool(OT.observability_ok(A, C, L)[0])
                if ok:
                    qmin = q
                    break
            if qmin is not None:
                break
        if qmin is None:
            continue
        tab[prof][0] += 1
        tab[prof][1] += qmin - q0
    print('rho=2 实例：$\\Delta$ 剖面 vs 阶差')
    print(f'{"profile":>28} {"样本":>5} {"平均阶差":>8}')
    for prof in sorted(tab):
        s_, gsum = tab[prof]
        print(f'{str(prof):>28} {s_:>5} {gsum/s_:>8.2f}')


if __name__ == '__main__':
    main()
