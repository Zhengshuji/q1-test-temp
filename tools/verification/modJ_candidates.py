"""modJ_candidates.py —— 扩大候选族：只满足 $(5a)$（模 $\\mathcal J$ 不变）的子空间

之前 `observer_pencils.candidate_Ls` 只给 **A-不变** 的 $\\mathcal V$（太窄）。
$(5a)$ 实际只要求 $\\mathcal V A\\subseteq\\mathcal V+\\mathcal J$（模 $\\mathcal J$ 不变），
所以合法候选多得多。

做法（商空间 $X=\\mathbb C^n/\\mathcal J$ 上做，再提升）：
  1. $\\mathcal J=\\operatorname{row}[C;CA]$、补空间 $W$、投影 $\\pi$、$T=\\pi\\circ A|_W$、$U_0=\\pi(\\operatorname{row}L_0)$（复用 `min_layer_closure`）；
  2. 在 $X$ 里取 $T$-不变子空间 $\\tilde U\\supseteq U_0$（闭包 + 随机 $T$-不变扩张）；
  3. 提升：$\\mathcal V=\\operatorname{span}(\\operatorname{row}L_0\\ \\cup\\ \\text{各基向量的原像})$；
  4. **用精确 $(5a)$ 检验**（`linalg_q.condA`）——不通过就丢弃并计数。

这样得到的 $L$ 不一定 $A$-不变，但满足 $(5a)$ ⟹ 仍是合法观测器候选。
"""

import os
import random
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
import min_layer_closure as MLC           # noqa: E402

F = Fraction


def lift_rows(A, C, Ucoords, L0, info):
    """把 W-坐标下的子空间（基 = Ucoords）提升为 $\\mathbb C^n$ 的行，再并上 $L_0$。"""
    n = len(A)
    # 重建 W 的基与 J，用于提升
    CA = LQ.mul(C, A)
    Jrows = []
    for r in LQ.stack(C, CA):
        if LQ.rank(Jrows + [r]) > len(Jrows):
            Jrows.append(r)
    d = info['d']
    # 补空间：把 J 的基补成 n 维满秩
    W = []
    for e in [[F(1) if k == i else F(0) for k in range(n)] for i in range(n)]:
        if LQ.rank(W + [e]) > len(W):
            W.append(e)
        if len(W) == n - len(Jrows):
            break
    # 与 min_layer_closure 一致的 W 基：先 S（空）再 W 的余维基
    # 这里直接用补空间 W 的坐标：Ucoords 是 W-坐标下的向量
    rows = [list(r) for r in L0]
    for u in Ucoords:
        # u 是 W-坐标；映射回 C^n
        vec = [F(0)] * n
        for k, c in enumerate(u):
            for j in range(n):
                vec[j] += c * W[k][j]
        rows.append(vec)
    # rref 化简
    out = []
    for r in rows:
        if LQ.rank(out + [r]) > len(out):
            out.append(r)
    return out


def candidate_Ls_modJ(A, C, L0, trials=40, seed=0, n_extra=1):
    """产生只满足 $(5a)$（模 J 不变）的候选 L。"""
    # 商数据：U0 = π(L0)、T、B
    T2, B2, U0, info2 = MLC.quotient_data(A, C, [list(r) for r in L0])
    d = info2['d']
    base = MLC.closure(T2, B2, U0, verbose=False)
    rng = random.Random(seed)
    tested = passed = 0
    cands = [base]
    for t in range(trials):
        extra = [[F(rng.choice([-1, 0, 1, 2])) for _ in range(d)] for _ in range(n_extra)]
        V = MLC.closure(T2, B2, base + extra, verbose=False)
        cands.append(V)
    for Ucoords in cands:
        L = lift_rows(A, C, Ucoords, L0, info2)
        tested += 1
        # (5a) 的精确检验（原始 4 块形式）
        if not LQ.condA(A, C, L):
            continue
        passed += 1
        yield L
    print(f'    modJ 候选：测试 {tested} 个，通过 (5a) {passed} 个')


if __name__ == '__main__':
    from find_layer_instance import make_instance
    A, C, L0 = make_instance(6, 1002)
    cnt = 0
    for L in candidate_Ls_modJ(A, C, L0, trials=10, seed=1):
        cnt += 1
        print(f'  q={len(L)} (5a)=True')
    if cnt == 0:
        print('  没有通过 (5a) 的提升（记录）')
