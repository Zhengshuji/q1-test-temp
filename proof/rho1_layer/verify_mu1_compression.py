"""核对 mu=1 的**正确**判据：

  bar T := P_Pi (T|_Pi)，Pi = a^perp。
  结论（本次推导）：bad(s) 对所有 s 成立  <=>  bar T 是标量（= mu * id）。
  即：存在好 s  <=>  bar T 不是标量。

（此前记录的"T 有与 a 正交的特征向量"是**错的**代理判据 —— 它在样本上碰巧一致。
本脚本把两个判据都与"直接抽 s 测 (5b)"比较，看哪个对。）
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util
spec = importlib.util.spec_from_file_location('V', 'proof/rho1_layer/verify_mu1_criterion.py')
V = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)


def pi_basis(a):
    return AI.nullspace([[a[0], a[1], a[2]]])


def compression(T, a):
    """返回 bar T 在 Pi 的基下的 2x2 矩阵（若 Pi 不是 2 维返回 None）。"""
    Pi = pi_basis(a)
    if len(Pi) != 2:
        return None
    na2 = sum(a[i] * a[i] for i in range(3))
    def proj(v):
        c = sum(a[i] * v[i] for i in range(3)) / na2
        return [v[i] - c * a[i] for i in range(3)]
    parts = []
    for v in Pi:
        Tv = [sum(T[i][j] * v[j] for j in range(3)) for i in range(3)]
        parts.append(proj(Tv))
    # 把 parts 表示成 Pi 基的组合：解 coeffs
    M = [[Pi[0][i] for i in range(3)], [Pi[1][i] for i in range(3)]]
    cols = []
    for p in parts:
        sol = AI.lstsq2(M, p) if hasattr(AI, 'lstsq2') else None
        cols.append(sol)
    return cols, Pi


def is_scalar_compression(T, a):
    """bar T 是否标量（不做坐标变换的简易判定）：检查 P_Pi T v 与 v 成比例对所有 v in Pi。"""
    Pi = pi_basis(a)
    if len(Pi) != 2:
        return None
    na2 = sum(a[i] * a[i] for i in range(3))
    def proj(v):
        c = sum(a[i] * v[i] for i in range(3)) / na2
        return [v[i] - c * a[i] for i in range(3)]
    # 若 bar T = mu*id，则对任意 v：proj(Tv) = mu v。用两个基向量求 mu 并验证。
    mus = []
    for v in Pi:
        Tv = [sum(T[i][j] * v[j] for j in range(3)) for i in range(3)]
        p = proj(Tv)
        # mu = <p,v>/<v,v>
        num = sum(p[i] * v[i] for i in range(3))
        den = sum(v[i] * v[i] for i in range(3))
        mus.append(num / den)
        # 检查 p - mu v == 0
        if any(p[i] - mus[-1] * v[i] != 0 for i in range(3)):
            return False
    return all(m == mus[0] for m in mus)


def main():
    rng = random.Random(31415)
    agree_new = 0
    agree_old = 0
    total = 0
    for _ in range(200):
        T = [[Fr(rng.randint(-3, 3)) for _ in range(3)] for _ in range(3)]
        a = [Fr(rng.randint(-3, 3)) for _ in range(3)]
        if not any(a):
            continue
        beta = Fr(rng.randint(-2, 2) or 1)
        w = [beta * a[k] for k in range(3)]
        scalar = is_scalar_compression(T, a)
        if scalar is None:
            continue
        d = V.direct(T, a, w, 60, rng)              # True => 存在好 s
        new_crit = not scalar                       # 新判据：bar T 非标量 => 存在好 s
        old_crit = V.criterion(T, a)                # 旧判据（错的那个）
        total += 1
        if new_crit == d:
            agree_new += 1
        if old_crit == d:
            agree_old += 1
    print(f"总样本 {total}")
    print(f"  新判据（bar T 非标量 <=> 存在好 s）：{agree_new}/{total}")
    print(f"  旧判据（T 有与 a 正交的特征向量）：{agree_old}/{total}")


if __name__ == '__main__':
    main()
