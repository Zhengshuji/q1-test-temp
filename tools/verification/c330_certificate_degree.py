#!/usr/bin/env python3
"""c330 — 固定 q 的变量账本 与 左逆证书最小次数（Bezout 界 2 omega - 2 的紧性）。

两部分都是**有限精确检验**，不是证明。

(A) 账本断言（纸面计数的算术核对）
    固定 q 的引理链（workspace/augmentation_family/attempts/312，含 314 的 G=FX 改写）
    量化的实变量是
        G = F X  in Q^{q x omega},   X in Q^{q x omega},   谱证书 x in Q^{2 omega},
    共 2 q omega + 2 omega 个；枢轴枚举 binom(k, omega) <= k^omega。
    r = 0 的线性系统（专家 85 号，attempts/317 与 c318）有
        (2 omega - 1) q omega 个未知量、2 omega^3 个方程。
    本脚本核对这几个计数公式，并断言 omega = q 时变量数 = 2 q^2 + 2 q。

(B) 左逆证书的最小次数 d_min
    Q(lam) = lam X - G（q x omega，X 满列秩，Q 对每个 lam 满列秩）。
        d_min = min { d : exists S(lam) = sum_{j<=d} S_j lam^j, S(lam) Q(lam) = I_omega }。
    已知（Bézout + 伴随）d_min <= 2 omega - 2。
    本脚本在规范形 X = [I;0] 上搜索 d_min，检验两个问题：
        (i)  d_min <= omega - 1 是否总成立（若是，证书系统的规模可减半）；
        (ii) d_min = 2 omega - 2 是否可达（若是，Bézout 界是紧的）。
    omega = q 不必测：det(lam X - G) 非常数，必有根，恒不可行。

(C) 规范形合法性：行/列左乘可逆常数矩阵不改变 d_min；随机对照。

全部在 Q 上做精确算术。gcd 判定按"极大子式 gcd 为非零常数"（公根在 C 上取），
与 c318 的口径一致。本脚本不证明任何界。
"""

from __future__ import annotations

import itertools
import os
import random
import sys
import time

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for _p in ("tools/verification",):
    _cand = os.path.join(_ROOT, _p)
    if _cand not in sys.path:
        sys.path.insert(0, _cand)

lam = sp.symbols("lam")


def unit_block(q: int, om: int) -> sp.Matrix:
    """[I_omega; 0] 形状的 q x omega 矩阵。"""
    return sp.Matrix(q, om, lambda i, j: 1 if i == j else 0)


# --------------------------------------------------------------------------
# 铅笔、gcd 判据、最小次数
# --------------------------------------------------------------------------
def pencil(X: sp.Matrix, G: sp.Matrix) -> sp.Matrix:
    q, om = X.shape
    assert G.shape == (q, om), (G.shape, (q, om))
    return sp.Matrix(q, om, lambda i, j: lam * X[i, j] - G[i, j])


def maximal_minors(X: sp.Matrix, G: sp.Matrix):
    q, om = X.shape
    Q = pencil(X, G)
    cols = list(range(om))
    return [sp.expand(Q.extract(list(rows), cols).det())
            for rows in itertools.combinations(range(q), om)]


def gcd_test(X: sp.Matrix, G: sp.Matrix) -> bool:
    """Q(lam) 对每个 lam in C 满列秩 <=> 极大子式的 gcd 是非零常数。"""
    ms = maximal_minors(X, G)
    g = ms[0]
    for m in ms[1:]:
        g = sp.gcd(g, m)
    g = sp.Poly(g, lam)
    return g.degree() <= 0 and g.eval(0) != 0


def build_system(X: sp.Matrix, G: sp.Matrix, d: int):
    """(R0.1)-(R0.3) 的整数系数矩阵与右端；未知量 S_j[a,b]，0 <= j <= d。

        k = 0       : -S_0 G             = I_omega
        1 <= k <= d :  S_{k-1} X - S_k G = 0
        k = d + 1   :  S_d X             = 0
    """
    q, om = X.shape
    den = 1
    for v in list(X) + list(G):
        den = sp.ilcm(den, sp.Rational(v).q)
    Xs = (sp.Matrix(X) * den).applyfunc(lambda v: sp.nsimplify(v))
    Gs = (sp.Matrix(G) * den).applyfunc(lambda v: sp.nsimplify(v))
    assert all(sp.Rational(v).q == 1 for v in list(Xs) + list(Gs)), "分母未清干净"
    nvar = (d + 1) * om * q
    neq = (d + 2) * om * om
    rows, rhs = [], []
    for k in range(d + 2):
        for a in range(om):
            for c in range(om):
                row = [0] * nvar
                if k == 0:
                    for b in range(q):
                        row[a * q + b] = -int(Gs[b, c])
                    rhs.append(1 if a == c else 0)
                elif k <= d:
                    for b in range(q):
                        row[(k - 1) * om * q + a * q + b] = int(Xs[b, c])
                        row[k * om * q + a * q + b] = -int(Gs[b, c])
                    rhs.append(0)
                else:
                    for b in range(q):
                        row[d * om * q + a * q + b] = int(Xs[b, c])
                    rhs.append(0)
                rows.append(row)
    M = sp.Matrix(rows)
    b = sp.Matrix(rhs)
    assert M.shape == (neq, nvar), (M.shape, (neq, nvar))
    return M, b


def consistent(X: sp.Matrix, G: sp.Matrix, d: int) -> bool:
    M, b = build_system(X, G, d)
    return M.rank() == M.row_join(b).rank()


def minimal_degree(X: sp.Matrix, G: sp.Matrix, cap: int):
    """返回 [0, cap] 中最小相容 d；都不相容返回 None。"""
    om = X.shape[1]
    cap = min(cap, 2 * om - 2)
    for d in range(cap + 1):
        if consistent(X, G, d):
            return d
    return None


# --------------------------------------------------------------------------
# 规范形
# --------------------------------------------------------------------------
def normalize(X: sp.Matrix, G: sp.Matrix):
    """求可逆 P 使 P X = [I;0]，返回 (P, Xn, Gn)。"""
    q, om = X.shape
    assert X.rank() == om, "X 不满列秩"
    basis = sp.Matrix(X)
    for i in range(q):
        if basis.shape[1] == q:
            break
        e = sp.zeros(q, 1)
        e[i] = 1
        if basis.row_join(e).rank() > basis.rank():
            basis = basis.row_join(e)
    assert basis.shape == (q, q) and basis.rank() == q
    P = basis.inv()
    assert sp.simplify(P * X - unit_block(q, om)) == sp.zeros(q, om), "PX != [I;0]"
    return P, sp.simplify(P * X), sp.simplify(P * G)


def random_x(q: int, om: int, rng: random.Random) -> sp.Matrix:
    X = sp.zeros(q, om)
    for i in range(om):
        X[i, i] = 1
    for i in range(om, q):
        for j in range(om):
            X[i, j] = rng.randint(-3, 3)
    assert X.rank() == om
    return X


def random_g(q: int, om: int, rng: random.Random, box: int) -> sp.Matrix:
    return sp.Matrix(q, om, lambda i, j: rng.randint(-box, box))


def random_unimodular(n: int, rng: random.Random) -> sp.Matrix:
    while True:
        M = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
        if M.rank() == n:
            return M


# --------------------------------------------------------------------------
# (A) 账本
# --------------------------------------------------------------------------
def part_A() -> None:
    print("=" * 74)
    print("(A) 账本：固定 q 的变量数 与 r=0 的系统规模")
    print("=" * 74)
    for q, om in [(3, 2), (4, 2), (5, 2), (6, 3), (8, 3), (6, 6), (10, 10)]:
        nvar = 2 * q * om + 2 * om
        print(f"  (q, omega) = ({q:2d},{om:2d}):  2q*omega + 2*omega = {nvar:4d}"
              f"    (omega = q 时 = 2q^2 + 2q)")
    for q in (2, 3, 5):
        assert 2 * q * q + 2 * q == 2 * q * (q + 1)
        print(f"  omega = q = {q}:  变量 = {2*q*q+2*q}, 是 q^2 的 {2 + 2/q:.2f} 倍")

    for q, om in [(3, 1), (4, 2), (6, 3), (8, 4)]:
        d = 2 * om - 2
        M, b = build_system(unit_block(q, om), sp.zeros(q, om), d)
        nvar = (2 * om - 1) * q * om
        neq = 2 * om ** 3
        assert M.shape == (neq, nvar), (M.shape, (neq, nvar))
        print(f"  (q, omega) = ({q},{om}):  r=0 系统 {neq} 方程 x {nvar} 未知量"
              f"   [=(2omega-1)q omega, 2 omega^3]")
    print("  => 若证书次数界从 2omega-2 降到 omega-1，r=0 系统未知量从 (2omega-1)q omega")
    print("     降到 omega^2 q，即约一半（omega=2: 3 -> 2 个 S 块）。")


# --------------------------------------------------------------------------
# (B) 搜索
# --------------------------------------------------------------------------
def scan_family(q, om, mode, box, n_random, budget, rng):
    cap = om - 1              # 只检验"能否 <= omega-1"
    Xi = unit_block(q, om)
    hist = {}
    feasible = 0
    scanned = 0
    worst = []                # 需要 d >= omega 的实例
    t0 = time.time()
    if mode == "exhaustive":
        it = itertools.product(range(-box, box + 1), repeat=q * om)
        total = (2 * box + 1) ** (q * om)
    else:
        it = (tuple(rng.randint(-box, box) for _ in range(q * om))
              for _ in range(n_random))
        total = n_random
    for flat in it:
        scanned += 1
        G = sp.Matrix(q, om, lambda i, j: flat[i * om + j])
        if not gcd_test(Xi, G):
            continue
        feasible += 1
        d = minimal_degree(Xi, G, cap=cap)
        hist[d] = hist.get(d, 0) + 1
        if d is None:
            worst.append(G)
        if time.time() - t0 > budget:
            print(f"    ... 预算用尽：已扫 {scanned}/{total}")
            break
    dt = time.time() - t0
    label = "穷举" if mode == "exhaustive" else "随机"
    hist_s = {(">%d" % cap if k is None else k): v for k, v in sorted(
        hist.items(), key=lambda kv: (kv[0] is None, kv[0]))}
    print(f"  (q,omega)=({q},{om}) {label} box={box}: 扫 {scanned}, 可行 {feasible},"
          f" 直方图 {hist_s}, 用时 {dt:.1f}s")
    return worst, cap, dt


def part_B() -> None:
    print()
    print("=" * 74)
    print("(B) d_min 的搜索：能否 <= omega-1？（cap = omega-1）")
    print("=" * 74)
    rng = random.Random(20261116)

    # 基准例：q = omega + 1，含常数极大子式但无常数左逆（S_0 X = 0 把秩卡在 q-omega = 1 < omega）
    X0, G0 = unit_block(3, 2), sp.Matrix([[0, 1], [1, 0], [0, 1]])
    assert gcd_test(X0, G0), "基准例应可行"
    assert minimal_degree(X0, G0, cap=0) is None, "基准例不应有常数左逆"
    print(f"  基准 (q,omega)=(3,2): gcd_test={gcd_test(X0, G0)},"
          f" d_min(cap=2)={minimal_degree(X0, G0, cap=2)}  (期望 1)")

    families = [
        (3, 2, "exhaustive", 1, 0, 90.0),
        (3, 2, "random", 2, 1500, 60.0),
        (4, 2, "random", 2, 1500, 60.0),
        (5, 2, "random", 2, 800, 60.0),
        (4, 3, "random", 1, 600, 90.0),
        (5, 3, "random", 1, 300, 90.0),
        # omega = 4, 5：q = omega + 1 是否仍处处取到 omega - 1
        (5, 4, "random", 1, 60, 240.0),
        (6, 4, "random", 1, 40, 150.0),
        (6, 5, "random", 1, 20, 420.0),
    ]
    all_worst = []
    for q, om, mode, box, nrand, budget in families:
        worst, cap, dt = scan_family(q, om, mode, box, nrand, budget, rng)
        all_worst.extend([(q, om, G) for G in worst])
        if dt > budget:
            break

    # q = omega + 1 上"全族取到上界"的检验（(3,2) 与 (4,3) 的直方图应只有一个非空桶 omega-1）
    print()
    print("  q = omega + 1 的族：直方图若只有 {omega-1} 一个桶，说明该族处处取到 ω-1。")

    print()
    if not all_worst:
        print("  结论（有限搜索）：所有可行铅笔都满足 d_min <= omega - 1；")
        print("  尤其 omega = 2 时从未出现 d_min = 2（Bézout 界 2omega-2 = 2 未被达到）。")
    else:
        print(f"  有 {len(all_worst)} 个可行铅笔不满足 d_min <= omega-1，逐个算真实 d_min：")
        for q, om, G in all_worst[:10]:
            d_true = minimal_degree(unit_block(q, om), G, cap=2 * om - 2)
            print(f"    (q,omega)=({q},{om}) G={G.tolist()}  d_min={d_true}"
                  f"  (Bézout 界 {2*om-2})")


# --------------------------------------------------------------------------
# (C) 规范形合法性
# --------------------------------------------------------------------------
def part_C() -> None:
    print()
    print("=" * 74)
    print("(C) 等价形式不改变 d_min（行变换 / 列变换 / 规范形）")
    print("=" * 74)
    rng = random.Random(7)
    ok = trials = 0
    for (q, om) in [(3, 2), (4, 2), (4, 3)]:
        for _ in range(60):
            X, G = random_x(q, om, rng), random_g(q, om, rng, 2)
            if not gcd_test(X, G):
                continue
            trials += 1
            cap = 2 * om - 2
            d_raw = minimal_degree(X, G, cap=cap)
            P, Xn, Gn = normalize(X, G)
            d_norm = minimal_degree(Xn, Gn, cap=cap)
            R, T = random_unimodular(q, rng), random_unimodular(om, rng)
            d_mix = minimal_degree(R * X * T, R * G * T, cap=cap)
            if d_raw == d_norm == d_mix:
                ok += 1
            else:
                print(f"  !! 不一致 ({q},{om}): {d_raw} {d_norm} {d_mix}")
    print(f"  {ok}/{trials} 个可行实例的 d_min 在三种等价形式下一致。")
    assert ok == trials, "等价形式不保 d_min"


def main() -> None:
    part_A()
    part_B()
    part_C()
    print()
    print("=" * 74)
    print("c330 完成。账本已核对；(B)(C) 是有限精确检验，不构成定理。")
    print("=" * 74)


if __name__ == "__main__":
    main()
