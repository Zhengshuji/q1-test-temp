"""c175_realizable_J.py — 量化缺口 B：哪些子空间 J 可写成 row[C;CA]？

A = diag(1..n) 互异。J 可实现 ⟺ ∃C 使 row[C;CA] = J。
本脚本对随机的 2 维 J，在小整数范围内搜 C（p=1 与 p=2），统计可实现比例。

用法：python q1_true/scripts/c175_realizable_J.py
"""
import sys
import os
import itertools
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts", "core"))

from fractions import Fraction as Fr
import audit_independent as AI

mul = AI.mul


def same_span(X, Y):
    return len(AI.row_basis(X)) == len(AI.row_basis(Y)) and \
        len(AI.row_basis(X + Y)) == len(AI.row_basis(Y))


def realizable(J, A, n, box=2):
    # p=1
    for c in itertools.product(range(-box, box + 1), repeat=n):
        if all(x == 0 for x in c):
            continue
        cc = [Fr(x) for x in c]
        if same_span([cc] + mul([cc], A), J):
            return True, 1
    # p=2（小 box）
    for c1 in itertools.product(range(-1, 2), repeat=n):
        if all(x == 0 for x in c1):
            continue
        for c2 in itertools.product(range(-1, 2), repeat=n):
            if all(x == 0 for x in c2):
                continue
            C = [[Fr(x) for x in c1], [Fr(x) for x in c2]]
            if same_span(C + mul(C, A), J):
                return True, 2
    return False, None


def main():
    rng = random.Random(3)
    n = 4
    A = [[Fr(i + 1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    tot, ok = 0, 0
    for _ in range(40):
        J = AI.row_basis([[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(2)])
        if len(J) != 2:
            continue
        tot += 1
        r, p = realizable(J, A, n)
        ok += r
    print("随机 2 维 J 总数:", tot, " 可实现:", ok)
    # 对照：坐标 J 与 "循环" J
    print("坐标 J =", [[str(x) for x in r] for r in AI.row_basis(
        [[Fr(1), Fr(0), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0), Fr(0)]])])
    u = [Fr(1), Fr(1), Fr(0), Fr(0)]
    cyc = AI.row_basis([u] + mul([u], A))
    print("循环 J = span{u,uA} =", [[str(x) for x in r] for r in cyc],
          " 可实现?", realizable(cyc, A, n))


if __name__ == "__main__":
    main()
