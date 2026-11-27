r"""Smith 形（行列式因子）与"枚举极大子式 + gcd"的**交叉验证**。

三条独立路径，全部精确有理算术：

1. **Smith 路径**（`poly_smith.full_col_rank_constant`）：$\Delta_b$ 的分数次数是否为 0；
2. **子式路径**（`poly_smith.det_divisor_by_minors` = 枚举全部 $b$ 行子集 + `pdet` + gcd）；
3. **点路径**：在 $\lambda\in\{0,\pm1,\pm2,3,1/2\}$ 上直接算数值秩（`poly_smith.rank_at`）。

三层覆盖：

| 层 | 对象 | 数量 |
|---|---|---|
| L1 | 随机多项式矩阵（$a\le8,b\le a$，$\deg\le3$）| ≥80 |
| L2 | L1 的逐点秩检查 | 每个矩阵 6 个 $\lambda$ |
| L3 | 真实实例的铅笔 $[U\mid P(\lambda)]$（R17 $q=3,2$；c282 $q=4$；第二实例 $q=2$）| ≥60 |

**等级**：精确验证。它验证的是"两条实现算的是同一个 $\Delta_b$"以及"$\Delta_b$ 常数 $\iff$ 处处满秩"的**实例**；
定理本身是 Smith 标准形 + "$b\times b$ 极大子式的 gcd = $d_1\cdots d_b$"（[已证-纸面]，见
[proof/quotient_equivalence/README.md](../../proof/quotient_equivalence/README.md) §9）。
**验证不是证明**。

用法：python tools/verification/verify_smith.py
"""
import itertools
import math
import os
import random
import sys
import time
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import base_sweep as BS
import coeff_of_S as CS
import poly_smith as PS
import verify_quotient_equivalence as VQ

LAMBDAS = [Fr(0), Fr(1), Fr(-1), Fr(2), Fr(-2), Fr(3), Fr(1, 2)]


# ---------------- L1/L2：随机多项式矩阵 ----------------
def random_poly(rng, deg):
    return PS.ptrim([Fr(rng.randint(-2, 2)) for _ in range(deg + 1)])


def random_matrix(rng, a, b, deg):
    while True:
        Q = [[random_poly(rng, rng.randint(0, deg)) for _ in range(b)] for _ in range(a)]
        if any(not PS.pzero(x) for row in Q for x in row):
            return Q


def check_random_layer(seed=20261101, n_mat=120):
    rng = random.Random(seed)
    ok = 0
    skip = 0
    bad = []
    for t in range(n_mat):
        a = rng.randint(1, 8)
        b = rng.randint(0, a)
        if b == 0:
            continue
        Q = random_matrix(rng, a, b, rng.choice([0, 1, 2, 3]))
        ok_s, delta_s, info = PS.full_col_rank_constant(Q)
        delta_m = PS.det_divisor_by_minors(Q)
        if delta_s != delta_m:
            bad.append(('Δ 不一致', a, b, delta_s, delta_m))
            continue
        # 点路径只能单向核对：常数 ⟹ 处处满秩；某点降秩 ⟹ 非常数。
        ranks = [PS.rank_at(Q, lam) for lam in LAMBDAS]
        if ok_s and not all(rr == b for rr in ranks):
            bad.append(('常数但有点降秩', a, b, ranks))
            continue
        if (not ok_s) and all(rr == b for rr in ranks) and info['rank'] == b:
            skip += 1          # 根不在采样点（例：公根是 1/3 或复数）——不是矛盾
            continue
        ok += 1
    return ok, skip, bad


# ---------------- L3：真实实例的铅笔 ----------------
def vdh(A, V, H):
    r"""$V\cap D\cap H$ 的基（$D=\{x:Ax\in H\}$）。"""
    VD = VQ.intersect_V_D(A, V, H)
    return AI.nullspace(AI.nullspace([list(x) for x in VD]) + AI.nullspace([list(x) for x in H]))


def cases():
    return [('R17', VQ.r17(), 3, 2), ('R17', VQ.r17(), 2, 2),
            ('c282', VQ.c282(), 4, 1), ('second', VQ.second(), 2, 2)]


def check_instance_layer(seed=20261101, n_s=3, n_u=8):
    rng = random.Random(seed)
    ok = 0
    skipped = 0
    bad = []
    detail = []
    for name, (A, C, L0), q, s in cases():
        geo = BS.geometry(A, C, L0)
        n = geo['n']
        pool = vdh(A, geo['V'], geo['H'])
        if s > 0 and len(pool) < s:
            continue
        Ss = []
        for _ in range(400):
            if len(Ss) >= n_s:
                break
            combos = [[rng.randint(-2, 2) for _ in range(len(pool))] for _ in range(s)] if s else []
            S = [[sum(Fr(c[j]) * pool[j][i] for j in range(len(pool))) for i in range(n)]
                 for c in combos] if s else []
            if s and VQ.rank_of(S) != s:
                continue
            key = tuple(tuple(x) for x in S)
            if key in {tuple(tuple(x) for x in y) for y in Ss}:
                continue
            Ss.append(S)
        for S in Ss:
            st = CS.setup(A, C, L0, q, S)
            wm, t, r = st['wm'], st['t'], st['r']
            cols = CS.pencil_cols(A, st)
            P0 = [[cols[j][0][i] for j in range(t)] for i in range(wm)]
            P1 = [[cols[j][1][i] for j in range(t)] for i in range(wm)]
            for _u in range(n_u):
                if r == 0:
                    U = []
                else:
                    U = []
                    while len(U) < r:
                        cand = [Fr(rng.randint(-2, 2)) for _ in range(wm)]
                        if VQ.rank_of(U + [cand]) > len(U):
                            U.append(cand)
                Q = PS.make_pencil(U, P0, P1)
                b = len(Q[0]) if Q else 0
                ok_s, delta_s, info = PS.full_col_rank_constant(Q)
                delta_m = PS.det_divisor_by_minors(Q)
                if delta_s != delta_m:
                    bad.append((name, q, s, 'Δ', delta_s, delta_m))
                    continue
                ranks = [PS.rank_at(Q, lam) for lam in LAMBDAS]
                if ok_s and not all(rr == b for rr in ranks):
                    bad.append((name, q, s, '常数但有点降秩', ranks))
                    continue
                if (not ok_s) and all(rr == b for rr in ranks) and info['rank'] == b:
                    skipped += 1
                    continue
                ok += 1
            detail.append((name, q, s, wm, t, r))
    return ok, skipped, bad, detail


def timing_layer():
    """一个 $8\times8$ 铅笔：Smith 路径必须跑完并打印耗时。"""
    rng = random.Random(7)
    Q = [[PS.ptrim([Fr(rng.randint(-3, 3)), Fr(rng.randint(-3, 3))]) for _ in range(8)]
         for _ in range(8)]
    t0 = time.time()
    ok_s, delta, info = PS.full_col_rank_constant(Q)
    t1 = time.time()
    return ok_s, delta, info, t1 - t0


def main():
    print('Smith 形 vs 枚举子式 vs 逐点秩：交叉验证\n')
    t0 = time.time()
    ok1, skip1, bad1 = check_random_layer()
    print(f'L1/L2 随机矩阵：通过 {ok1} 个；跳过（公根不在采样点）{skip1} 个；不一致 {len(bad1)}')
    for b in bad1[:5]:
        print('   !!', b)
    ok3, skip3, bad3, detail = check_instance_layer()
    print(f'L3 实例铅笔：通过 {ok3} 个；跳过 {skip3} 个；不一致 {len(bad3)}')
    for b in bad3[:5]:
        print('   !!', b)
    print('   覆盖：', sorted({(d[0], d[1], d[2]) for d in detail}))
    ok_s, delta, info, dt = timing_layer()
    print(f'规模：8×8 铅笔 Smith 用时 {dt:.3f}s；常数? {ok_s}；rank={info["rank"]}；'
          f'deg(Δ)={info["deg"]}；max_bits={info["max_bits"]}')
    total_bad = len(bad1) + len(bad3)
    print(f'\n合计不一致：{total_bad}；总用时 {time.time() - t0:.1f}s')
    assert total_bad == 0, 'Smith 路径与子式路径不一致——实现有问题'
    assert ok1 >= 60, f'L1 覆盖不足（{ok1} < 60）'
    assert ok3 >= 60, f'L3 覆盖不足（{ok3} < 60）'
    print('交叉验证 ✓（0 不一致）')


if __name__ == '__main__':
    main()
