"""epsilon_zero_characterization.py —— 核验专家 2026-11-04 §B/§Q6 的 epsilon=0 三情形刻画

**命题（专家给出，本项目核验）**：设 U0 = L0|_V、U1 = L0A|_V : V -> C^r，比例性轨迹
P = {x in V : U0x ∧ U1x = 0}，epsilon = dim V - dim P。则 epsilon = 0 <=> P = V，且

1. rank U0 = 0：条件自动成立；
2. rank U0 = 1：epsilon = 0 <=> im U1 ⊆ im U0；
3. rank U0 >= 2：epsilon = 0 <=> U1 = alpha · U0 对某个 alpha in C。

**核验方法（精确有理算术）**：q(x) = U1x ∧ U0x 是二次型（q(0)=0），故
    q ≡ 0 on V  <=>  q(e_a) = 0 对所有基向量 且 q(e_a + e_b) = 0 对所有 a < b
这与 "epsilon = 0" 等价。两侧独立算出后比较。

用法：python -u tools/verification/epsilon_zero_characterization.py
"""

import os
import sys
import random
import itertools
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402

F = Fraction


def restrict(U, V, n):
    """把 r x n 的 U 限制到 V（V 为 n x dV 的列基），返回 r x dV。"""
    dV = len(V[0]) if (V and V[0]) else 0
    if dV == 0:
        return []
    return [[sum(U[i][j] * V[j][k] for j in range(n)) for k in range(dV)]
            for i in range(len(U))]


def q_form(M0, M1, dV, r):
    """对 V 的坐标向量 c，算 q(Vc) 的全部分量（需要 M0 c、M1 c）。"""
    def q_of(c):
        u = [sum(M0[i][k] * c[k] for k in range(dV)) for i in range(r)]
        v = [sum(M1[i][k] * c[k] for k in range(dV)) for i in range(r)]
        return [v[i] * u[j] - v[j] * u[i] for i in range(r) for j in range(i + 1, r)]
    return q_of


def q_vanishes(M0, M1, dV, r):
    """q ≡ 0 on V ？（检验基向量与两两基和）"""
    q_of = q_form(M0, M1, dV, r)
    for k in range(dV):
        c = [F(0)] * dV
        c[k] = F(1)
        if any(t != 0 for t in q_of(c)):
            return False
    for a, b in itertools.combinations(range(dV), 2):
        c = [F(0)] * dV
        c[a] = F(1)
        c[b] = F(1)
        if any(t != 0 for t in q_of(c)):
            return False
    return True


def case_condition(M0, M1, r, dV):
    """三情形判据。返回 (rank U0, 判据成立?, 说明)。"""
    if dV == 0:
        return 0, True, 'dim V = 0'
    rk0 = LQ.rank(M0) if M0 else 0
    if rk0 == 0:
        return 0, True, 'rank U0 = 0：自动'
    if rk0 == 1:
        # im U1 ⊆ im U0（都是 C^r 的子空间）⟺ 列拼接后秩不变
        stacked = [M0[i][:] + M1[i][:] for i in range(r)]
        return 1, LQ.rank(stacked) == rk0, 'rank U0 = 1：im U1 ⊆ im U0'
    # rank U0 >= 2：找 α 使 M1 = α M0
    alpha = None
    for i in range(r):
        for k in range(dV):
            if M0[i][k] != 0:
                alpha = M1[i][k] / M0[i][k]
                break
        if alpha is not None:
            break
    ok = alpha is not None and all(M1[i][k] == alpha * M0[i][k]
                                   for i in range(r) for k in range(dV))
    return rk0, ok, f'rank U0 ≥ 2：U1 = {alpha}·U0'


def main():
    rng = random.Random(20261104)
    stat = Counter()
    seen = Counter()
    for _ in range(6000):
        n = rng.choice([5, 6, 7])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r > n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank([list(x) for x in C] + L0) != p + r:
            continue
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
        dV = len(V[0]) if (V and V[0]) else 0
        if dV == 0:
            continue
        U1 = LQ.mul(L0, A)
        M0 = restrict(L0, V, n)
        M1 = restrict(U1, V, n)
        zero = q_vanishes(M0, M1, dV, r)
        rk0, cond, why = case_condition(M0, M1, r, dV)
        stat['samples'] += 1
        seen[f'rankU0={min(rk0, 2)}'] += 1
        if zero == cond:
            stat['agree'] += 1
        else:
            stat['disagree'] += 1
            if stat['disagree'] <= 5:
                print(f'  不一致 n={n} p={p} r={r}：q≡0 = {zero}，判据 = {cond}（{why}）')
    print('统计：', dict(stat))
    print('rank U0 分布：', dict(seen))
    print('  agree = "q≡0 on V" 与专家三情形判据一致；disagree 应为 0')


if __name__ == '__main__':
    main()
