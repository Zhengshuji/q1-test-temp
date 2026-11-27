"""type3_structured.py —— 按专家 2026-11-03 §Q6 的定向策略搜索 Type III 反例

目标：找**精确**的 $q_0$ 阶例子满足
$$(5a),\\qquad h<q_0+r_1,\\qquad d_{\\rm fin}>0 .$$
若有，猜想 T 被推翻；若无，则为 T 增加证据。

专家的定向建议（§Q6）：

1. 优先选**代数可行族正维数**的实例（便于在解集内探索多个精确候选）；
2. 增大测量维数 $p\\ge3$；
3. 用**结构化 $A$**：对角（互异/重复特征值）、含非平凡 Jordan 块；
4. 精确有理数据，最终候选要有精确秩证书与非常数 gcd；
5. 记录完整指标数据（正左指标与 $d_{\\rm fin}$），而不只是"$(5b)$ 失败"。

本脚本实现 1–5 的轻量版（$n\\le8$，$p\\in\\{2,3\\}$，两族结构化 $A$），
$d_{\\rm fin}$ 用 Toeplitz 零度快速算。

用法：python -u tools/verification/type3_structured.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import descriptor_pencil as DP            # noqa: E402
import observer_pencils as OP             # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import z_generator as ZG                  # noqa: E402

F = Fraction


def obs_matrix(A, C):
    rows = [r[:] for r in C]
    cur = [r[:] for r in C]
    for _ in range(len(A) - 1):
        cur = LQ.mul(cur, A)
        rows += [r[:] for r in cur]
    return rows


def diag_family(n, vals):
    A = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = F(vals[i % len(vals)])
    return A


def jordan_family(n, lam):
    """块对角：每 2×2 一个 Jordan 块 $\\lambda I+N$，剩下一维补 $\\lambda$。"""
    A = [[F(0)] * n for _ in range(n)]
    i = 0
    while i + 1 < n:
        A[i][i] = F(lam[i // 2 % len(lam)])
        A[i][i + 1] = F(1)
        A[i + 1][i + 1] = F(lam[i // 2 % len(lam)])
        i += 2
    if i < n:
        A[i][i] = F(lam[0])
    return A


def pick_L0(A, C, r, seed):
    import random
    rng = random.Random(seed)
    O = obs_matrix(A, C)
    if LQ.rank(O) < len(O):
        O = [row for row in O]
    base = [row[:] for row in C]
    L0 = []
    cand = [row[:] for row in O[len(C):]]
    rng.shuffle(cand)
    for row in cand:
        if LQ.rank(base + L0 + [row]) > len(base) + len(L0):
            L0.append(row[:])
        if len(L0) == r:
            break
    if len(L0) != r:
        return None
    if LQ.rank([x[:] for x in C] + [x[:] for x in L0]) != len(C) + r:
        return None
    return L0


def fast_dfin(A, C, L):
    P0, P1, h = OP.pencil_from_L(A, C, L)
    q, p = len(L), len(C)
    s = LQ.rank(L)
    m = q + 2 * p - h
    Q0m, Q1m, _ = DP.descriptor_pencil(A, C, L)
    E, Fm, B = TC.split_R(Q0m, Q1m, q)
    nus = TC.toeplitz_nullities(E, Fm, B, s)
    return h, s, m, s - ((s + 1) * m - nus[s])


def main():
    found = []
    stats = dict(inst=0, sub=0, iii=0, samples=0)
    families = []
    for n in (5, 6, 7):
        families.append((f'diag-distinct-n{n}', diag_family(n, [0, 1, 2, 3])))
        families.append((f'diag-repeat-n{n}', diag_family(n, [1, 1, 2])))
        families.append((f'jordan-n{n}', jordan_family(n, [1, 2])))
    for name, A in families:
        n = len(A)
        for p in (2, 3):
            if p >= n:
                continue
            # C：随机 0/1 行，要求 rank C = p 且 (A,C) 可观测（否则实例无效）
            import random as _rnd
            rngC = _rnd.Random((sum(ord(ch) for ch in name) * 13 + p * 17))
            C = None
            for _try in range(60):
                cand = [[F(rngC.randrange(2)) for _ in range(n)] for _ in range(p)]
                if LQ.rank(cand) != p:
                    continue
                if LQ.rank(obs_matrix(A, cand)) != n:
                    continue
                C = cand
                break
            if C is None:
                continue
            for r in (1, 2):
                if p + r > n:
                    continue
                L0 = pick_L0(A, C, r, seed=(sum(ord(ch) for ch in name) * 7 + p * 31 + r))
                if L0 is None:
                    continue
                O = obs_matrix(A, C)
                if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                    continue
                q0 = Q0.eta_and_q0(A, C, L0)[0]
                CA = LQ.mul(C, A)
                r1 = LQ.rank([x[:] for x in C] + [x[:] for x in CA])
                stats['inst'] += 1
                cands = ZG.sample_L_at_order(A, C, L0, q0, 80, seed=(sum(ord(ch) for ch in name) * 11 + q0 * 29))
                for L in cands:
                    stats['samples'] += 1
                    h, s, m, d_fin = fast_dfin(A, C, L)
                    if h < q0 + r1:
                        stats['sub'] += 1
                        if d_fin > 0:
                            stats['iii'] += 1
                            found.append((name, n, p, r, q0, r1, h, s, m, d_fin))
                if cands:
                    hs = sorted({fast_dfin(A, C, L)[0] for L in cands})
                    print(f'  {name} p={p} r={r}: q0={q0} r1={r1} 样本={len(cands)} '
                          f'h 取值={hs} q0+r1={q0 + r1}')
    print(f'\n实例 {stats["inst"]}，样本 {stats["samples"]}，h<q0+r1 的 {stats["sub"]}，'
          f'其中 Type III（d_fin>0）{stats["iii"]}')
    if found:
        print('** 找到 Type III ⟹ 猜想 T 被推翻：')
        for row in found[:10]:
            print('  ', row)
    else:
        print('未找到 Type III（不是证明）')


if __name__ == '__main__':
    main()
