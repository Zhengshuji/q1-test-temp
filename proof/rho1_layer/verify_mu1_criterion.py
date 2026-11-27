"""验证 mu = 1 的**判据**（rho3c1_mu1.md）：

当 mu = 1 时 C = T + a s^T（a 是 E 的生成元、s ∈ Q^3 自由）。断言：

    存在 s 使 (5b) 成立   <=>   T **没有**（单）特征向量与 a 正交。

等价写法：令 M(lam) = [[T - lam I],[a^T]]（4x3），
"T 有特征向量 v ⟂ a"  <=>  M(lam) 对某个 lam 的秩 <= 2  <=>  M(lam) 的 3x3 子式的 gcd != 1。

本脚本对随机实例同时算两件事并比较：
  * 判据侧：gcd(3x3 子式 of M(lam)) 是否为非零常数；
  * 直接侧：随机抽 s，测 (5b)。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pdivmod(a, b):
    a, b = ptrim(list(a)), ptrim(list(b))
    q = [Fr(0)] * max(1, len(a) - len(b) + 1)
    r = list(a)
    while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
        c = r[-1] / b[-1]
        dd = len(r) - len(b)
        q[dd] = c
        for i, bi in enumerate(b):
            r[i + dd] -= c * bi
        r = ptrim(r)
    return q, r


def pgcd(a, b):
    a, b = ptrim(list(a)), ptrim(list(b))
    while not (len(b) == 1 and b[0] == 0):
        _, r = pdivmod(a, b)
        a, b = b, r
    return a


def pmul(a, b):
    o = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return ptrim(o)


def padd(a, b):
    o = [Fr(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        o[i] += x
    for i, y in enumerate(b):
        o[i] += y
    return ptrim(o)


def det_poly(M):
    n = len(M)
    if n == 1:
        return ptrim(list(M[0][0]))
    acc = [Fr(0)]
    for j in range(n):
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        t = pmul(M[0][j], det_poly(sub))
        if j % 2:
            t = [-c for c in t]
        acc = padd(acc, t)
    return ptrim(acc)


def gcd_is_one(polys):
    if not polys:
        return False
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
    return len(g) == 1 and g[0] != 0


def criterion(T, a):
    """T 是否有特征向量 v ⟂ a ？ -> 返回 (has_orth_eig, gcd_is_one_of_M)"""
    rows = []
    for i in range(3):
        rows.append([[-T[i][j], Fr(1) if i == j else Fr(0)] for j in range(3)])
    rows.append([[a[j]] for j in range(3)])       # 常系数行 a^T
    polys = []
    for rs in itertools.combinations(range(4), 3):
        for cs in itertools.combinations(range(3), 3):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    return gcd_is_one(polys)


def direct(T, a, w, samples=60, rng=None):
    """抽 s，测 (5b)；返回是否找到成功的 s。"""
    for _t in range(samples):
        s = [Fr(rng.randint(-4, 4)) for _ in range(3)]
        C = [[T[i][j] + a[j] * s[i] for j in range(3)] for i in range(3)]
        rows = [([Fr(1) if i == j else Fr(0) for j in range(3)], [C[i][j] for j in range(3)])
                for i in range(3)]
        rows.append(([Fr(0)] * 3, list(w)))
        polys = []
        for rs in itertools.combinations(range(4), 3):
            for cs in itertools.combinations(range(3), 3):
                M = [[[-rows[i_][1][j], rows[i_][0][j]] for j in cs] for i_ in rs]
                v = det_poly(M)
                if not (len(v) == 1 and v[0] == 0):
                    polys.append(v)
        if gcd_is_one(polys):
            return True
    return False


def main():
    rng = random.Random(778899)
    agree = 0
    total = 0
    for _ in range(150):
        T = [[Fr(rng.randint(-3, 3)) for _ in range(3)] for _ in range(3)]
        a = [Fr(rng.randint(-3, 3)) for _ in range(3)]
        if not any(a):
            continue
        beta = Fr(rng.randint(-2, 2) or 1)
        w = [beta * a[k] for k in range(3)]
        crit = criterion(T, a)               # True => 判据说"没有正交特征向量" => 存在好 s
        d = direct(T, a, w, 60, rng)
        total += 1
        if crit == d:
            agree += 1
    print(f"mu=1 判据核对：{agree}/{total} 一致（判据: 存在好 s <=> T 无正交特征向量）")


if __name__ == '__main__':
    main()
