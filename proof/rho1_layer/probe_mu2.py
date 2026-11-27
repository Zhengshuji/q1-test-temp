"""CQ-(3,1) 在 mu = 2 时的探测：C 的**第三列固定**（=T 的第三列），前两列自由。

模型（rho3c1_spectral.md 的归一化）：
  U = Q^3（基 = e1,e2,e3），w ∈ U（beta(h)），行 = lam*e_i - C_i（i=1..3），第 4 行 = w。
  mu = dim(B∩U) = 2  =>  tau 的自由度给出 C 的前两列自由、第三列固定为 gamma。
  (5b) <=> gcd(p0,p1,p2,p3) 为非零常数（p0 = det(lam I - C)，p_i 把第 i 行换成 w）。

对每个实例：随机抽若干个允许的 C，直接测 (5b)。
  * 一旦有一个 C 使 (5b) 成立  => 型层**不被**覆盖（该实例可行）。
  * 全部失败 => 该实例在抽样意义上"疑似被覆盖"。
同时用谱判据做交叉检查（当 C 单谱且特征值全有理时）：(5b) <=> 对所有 k，w^T v_k != 0。
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


def cond_5b(C, w):
    M = [[ptrim([-C[i][j], Fr(1) if i == j else Fr(0)]) for j in range(3)] for i in range(3)]
    p0 = det_poly(M)
    ps = []
    for i in range(3):
        MM = [[ptrim([-C[r][c], Fr(1) if r == c else Fr(0)]) for c in range(3)] for r in range(3)]
        MM[i] = [[x] for x in w]
        ps.append(det_poly(MM))
    g = p0
    for p in ps:
        g = pgcd(g, p)
    return len(g) == 1 and g[0] != 0


def main():
    """E 的方向随机化，且 w ∈ E（mu = 2）。"""
    rng = random.Random(24680)
    found_n = 0
    none_n = 0
    for inst in range(150):
        # E = span(a,b) 随机 2 维；w ∈ E 非零
        while True:
            a = [Fr(rng.randint(-3, 3)) for _ in range(3)]
            b = [Fr(rng.randint(-3, 3)) for _ in range(3)]
            if AI.rank([a, b]) == 2:
                break
        w = [a[i] + Fr(rng.randint(-2, 2)) * b[i] for i in range(3)]
        if not any(w):
            continue
        # T 的作用：t_i 随机
        T = [[Fr(rng.randint(-3, 3)) for _ in range(3)] for _ in range(3)]
        found = False
        for _t in range(40):
            C = []
            for i in range(3):
                e = [a[k] * Fr(rng.randint(-3, 3)) + b[k] * Fr(rng.randint(-3, 3)) for k in range(3)]
                C.append([T[i][k] + e[k] for k in range(3)])
            if cond_5b(C, w):
                found = True
                break
        if found:
            found_n += 1
        else:
            none_n += 1
    print(f"mu=2（E 随机方向、w ∈ E）：{found_n} 个找到好 C；{none_n} 个 40 次全失败")




def main_d4():
    """同样的探测，但 d = 4（U 是 Q^4 的 3 维子空间）—— 与 PROBE_31 的 (4,2,2) 对齐。"""
    rng = random.Random(13572468)
    found_n = none_n = 0
    for inst in range(150):
        while True:
            U = AI.row_basis([[Fr(rng.randint(-3, 3)) for _ in range(4)] for _ in range(5)])
            if len(U) == 3:
                break
        # E ⊆ U：2 维
        while True:
            a = [sum(Fr(rng.randint(-3, 3)) * U[i][k] for i in range(3)) for k in range(4)]
            b = [sum(Fr(rng.randint(-3, 3)) * U[i][k] for i in range(3)) for k in range(4)]
            if AI.rank([a, b]) == 2:
                break
        w = [a[k] + Fr(rng.randint(-2, 2)) * b[k] for k in range(4)]
        if not any(w):
            continue
        T = [[Fr(rng.randint(-3, 3)) for _ in range(3)] for _ in range(3)]
        found = False
        for _t in range(40):
            rows = []
            for i in range(3):
                e = [a[k] * Fr(rng.randint(-3, 3)) + b[k] * Fr(rng.randint(-3, 3)) for k in range(4)]
                ci = [sum(T[i][j] * U[j][k] for j in range(3)) + e[k] for k in range(4)]
                rows.append((U[i], ci))
            rows.append(([Fr(0)] * 4, list(w)))
            if cond_5b_rows(rows):
                found = True
                break
        if found:
            found_n += 1
        else:
            none_n += 1
    print(f"mu=2, d=4：{found_n} 个找到好配置；{none_n} 个 40 次全失败")


def cond_5b_rows(rows):
    polys = []
    for rs in itertools.combinations(range(len(rows)), 3):
        for cs in itertools.combinations(range(4), 3):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            v = det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return False
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
    return len(g) == 1 and g[0] != 0


def main_mu1():
    """mu = 1：E 是 1 维（tau 只能沿一条线动），d = 3 与 d = 4 两种构型。"""
    rng = random.Random(112233)
    for d in (3, 4):
        found_n = none_n = 0
        for inst in range(120):
            while True:
                U = AI.row_basis([[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(5)])
                if len(U) == 3:
                    break
            a = [sum(Fr(rng.randint(-3, 3)) * U[i][k] for i in range(3)) for k in range(d)]
            if not any(a):
                continue
            w = [a[k] * Fr(rng.randint(-2, 2) or 1) for k in range(d)]
            T = [[Fr(rng.randint(-3, 3)) for _ in range(3)] for _ in range(3)]
            found = False
            for _t in range(60):
                rows = []
                for i in range(3):
                    s_i = Fr(rng.randint(-4, 4))
                    ci = [sum(T[i][j] * U[j][k] for j in range(3)) + s_i * a[k] for k in range(d)]
                    rows.append((U[i], ci))
                rows.append(([Fr(0)] * d, list(w)))
                polys = []
                for rs in itertools.combinations(range(4), 3):
                    for cs in itertools.combinations(range(d), 3):
                        M = [[[-rows[i_][1][j], rows[i_][0][j]] for j in cs] for i_ in rs]
                        v = det_poly(M)
                        if not (len(v) == 1 and v[0] == 0):
                            polys.append(v)
                if not polys:
                    continue
                g = polys[0]
                for q in polys[1:]:
                    g = pgcd(g, q)
                if len(g) == 1 and g[0] != 0:
                    found = True
                    break
            if found:
                found_n += 1
            else:
                none_n += 1
        print(f"mu=1, d={d}: 找到好配置 {found_n}；60 次全失败 {none_n}")


if __name__ == '__main__':
    import sys as _s
    if len(_s.argv) > 1 and _s.argv[1] == 'mu1':
        main_mu1()
    elif len(_s.argv) > 1 and _s.argv[1] == 'd4':
        main_d4()
    else:
        main()

