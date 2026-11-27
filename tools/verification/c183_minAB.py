"""c183_minAB.py — 最小 (A,B)-不变子空间包含 S：精确值 vs 候选迭代（F_p 穷举）

问题：min dim W s.t. W ⊇ S, A W ⊆ W + B（在 F_p^n 上）。
在 F_3^4 上枚举所有子空间求精确最小，与 A-不变闭包（iter1）比较。

用法：python tools/verification/c183_minAB.py
"""
import itertools
import random


def rref(vecs, p, n):
    basis = []
    for v in vecs:
        v = [x % p for x in v]
        for b in basis:
            piv = next(i for i, x in enumerate(b) if x != 0)
            if v[piv] != 0:
                c = v[piv]
                v = [(v[j] - c * b[j]) % p for j in range(n)]
        if any(x != 0 for x in v):
            piv = next(i for i, x in enumerate(v) if x != 0)
            inv = pow(v[piv], p - 2, p)
            v = [(x * inv) % p for x in v]
            basis.append(v)
            basis.sort(key=lambda r: next(i for i, x in enumerate(r) if x != 0))
    return basis


def span_set(rows, p, n):
    k = len(rows)
    out = set()
    for coefs in itertools.product(range(p), repeat=k):
        v = tuple(sum(coefs[i] * rows[i][j] for i in range(k)) % p for j in range(n))
        out.add(v)
    return frozenset(out)


def all_subspaces(p, n):
    out = {}
    for k in range(n + 1):
        for piv in itertools.combinations(range(n), k):
            free = [j for j in range(n) if j > piv[-1]] if k else list(range(n))
            # 正确的 RREF 自由列：pivot 之间的与最后的列
            free = [j for j in range(n) if j not in piv]
            # 但 pivot 之前的列必须为 0；本函数用"pivot 列 + 其余列自由"会重复，
            # 靠最后按向量集去重。
            for vals in itertools.product(range(p), repeat=k * len(free)):
                rows = []
                for i in range(k):
                    row = [0] * n
                    row[piv[i]] = 1
                    for t, j in enumerate(free):
                        row[j] = vals[i * len(free) + t]
                    rows.append(row)
                S = span_set(rows, p, n)
                out[S] = (len(rref(rows, p, n)), S)
    return list(out.keys())


def main():
    for n, p in ((4, 3), (4, 5)):
        subs = all_subspaces(p, n)
        print("n=", n, "p=", p, " 子空间数:", len(subs))
        rng = random.Random(1)
        bad = 0
        tot = 0
        for t in range(120):
            A = [[rng.randrange(p) for _ in range(n)] for _ in range(n)]
            B = span_set(rref([[rng.randrange(p) for _ in range(n)] for _ in range(2)], p, n), p, n)
            S = rng.choice(subs)
            best = None
            for W in subs:
                if not S <= W:
                    continue
                Wb = rref([list(v) for v in W], p, n)
                WB = span_set(rref([list(v) for v in (W | B)], p, n), p, n)
                if all(tuple(sum(A[i][j] * w[j] for j in range(n)) % p for i in range(n)) in WB
                       for w in Wb):
                    if best is None or len(Wb) < best:
                        best = len(Wb)
            # iter1: A-不变闭包
            Wset = set(S)
            for _ in range(n + 1):
                Wb = rref([list(v) for v in Wset], p, n)
                new = set(Wset)
                for w in Wb:
                    new.add(tuple(sum(A[i][j] * w[j] for j in range(n)) % p for i in range(n)))
                if new == Wset:
                    break
                Wset = new
            it1 = len(rref([list(v) for v in Wset], p, n))
            tot += 1
            if best != it1:
                bad += 1
                if bad <= 5:
                    print("   精确", best, " iter1", it1)
        print("  实例", tot, " 精确与 iter1 不一致:", bad)


if __name__ == "__main__":
    main()
