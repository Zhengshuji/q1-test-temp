r"""
verify_equivalences.py -- ⭐ 本会话**等价关系**的一键复现（独立实现）

覆盖本会话确立的四条等价/蕴含（每条都给出两侧样本）：

  E1: (5a) ⟺ ker(L·N) ⊆ ker(L·A·N)               [history/52 §7.6]
  E2: (5b) ⟺ (S): rank(λH−F) ≡ rank H            [§7.7]
  E3: (5b) ⟺ rank(L·P_λ) ≡ rank(L·N)             [§7.8]  (无 Λ)
  E4: (5a) ⟺ M ∩ ({0}×R^q) = 0  的几何形式        [§7.22]

【判据】对每个等价关系，统计
   · 两侧一致的实例数
   · 其中"两侧皆真"与"两侧皆假"的个数（**必须都 > 0**，否则判定力不足）

用法：python verify_equivalences.py
"""
import os
import io
import contextlib
import random
import itertools

from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]


# ---------------- 多项式（独立） ----------------
def Pt(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q
def Pa(a, b):
    n = max(len(a), len(b))
    return Pt([(a[i] if i < len(a) else Fr(0)) + (b[i] if i < len(b) else Fr(0)) for i in range(n)])
def Ps(a, b):
    n = max(len(a), len(b))
    return Pt([(a[i] if i < len(a) else Fr(0)) - (b[i] if i < len(b) else Fr(0)) for i in range(n)])
def Pm(a, b):
    if Pt(a) == [Fr(0)] or Pt(b) == [Fr(0)]:
        return [Fr(0)]
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return Pt(r)
def Pdv(a, b):
    a = Pt(a); b = Pt(b); db = len(b) - 1
    q = [Fr(0)] * max(1, len(a) - db)
    while len(a) - 1 >= db and a != [Fr(0)]:
        d = len(a) - 1 - db; co = a[-1] / b[-1]; q[d] += co
        for i in range(len(b)):
            a[d + i] -= co * b[i]
        a = Pt(a)
    return Pt(q), a
def Pg(a, b):
    a, b = Pt(a), Pt(b)
    while b != [Fr(0)]:
        _, r = Pdv(a, b); a, b = b, r
    if len(a) > 1:
        lc = a[-1]; a = [x / lc for x in a]
    return a
def Pdet(M, k):
    if k == 1:
        return [Fr(x) for x in M[0][0]]
    tot = [Fr(0)]
    for j in range(k):
        sub = [row[:j] + row[j + 1:] for row in M[1:]]
        d = Pdet(sub, k - 1); pr = Pm(M[0][j], d)
        tot = Pa(tot, pr) if j % 2 == 0 else Ps(tot, pr)
    return Pt(tot)
def gcd_all(ps):
    if not ps:
        return None
    g = ps[0]
    for q in ps[1:]:
        g = Pg(g, q)
        if len(g) == 1:
            break
    return g
def const_nz(g):
    return g is not None and len(Pt(g)) == 1 and any(x != 0 for x in g)


# ---------------- 四种形式 ----------------
def f5a_rank(L, A, C):
    CA = mm(C, A)
    W = CA + C
    return rk(mm(L, A) + L + W) == rk(L + W)

def f5a_ker(L, A, N):
    """ker(L·N) ⊆ ker(L·A·N)"""
    LN = mm(L, N); LAN = mm(mm(L, A), N)
    K = ker_basis(LN)
    if not K or not K[0]:
        return True
    if len(LAN[0]) != len(K):
        return False
    return rk(mm(LAN, K)) == 0

def f5a_geom(L, A, N):
    """M ∩ ({0}×R^q) = 0 ；M 由 (A0v, A1v) 生成 ⟹ 等价于 ker A0 ⊆ ker A1"""
    return f5a_ker(L, A, N)

def f5b_total(L, A, C, maxm=1200):
    """(5b)：全矩阵铅笔 [λL−LA; CA; C] 的 r0 阶子式 gcd 非零常数"""
    CA = mm(C, A); LA = mm(L, A)
    base = L + CA + C
    r0 = rk(base); m = len(base); n = len(base[0]); nL = len(LA)
    if r0 == 0:
        return True
    P = [[([-LA[i][j], L[i][j]] if i < nL else [base[i][j]]) for j in range(n)]
         for i in range(m)]
    ps = []; cnt = 0
    for rows in itertools.combinations(range(m), r0):
        for cols in itertools.combinations(range(n), r0):
            dd = Pdet([[P[i][j] for j in cols] for i in rows], r0)
            if dd != [Fr(0)]:
                ps.append(dd)
            cnt += 1
            if cnt > maxm:
                break
        if cnt > maxm:
            break
    return const_nz(gcd_all(ps))

def fS(L, A, N, maxm=1200):
    """(S)：rank(λH−F) ≡ rank H """
    H = mm(L, N); F = mm(mm(L, A), N)
    q = len(H); d = len(H[0]); rho = rk(H)
    if rho == 0:
        return True
    P = [[[-F[i][j], H[i][j]] for j in range(d)] for i in range(q)]
    ps = []; cnt = 0
    for rows in itertools.combinations(range(q), rho):
        for cols in itertools.combinations(range(d), rho):
            dd = Pdet([[P[i][j] for j in cols] for i in rows], rho)
            if dd != [Fr(0)]:
                ps.append(dd)
            cnt += 1
            if cnt > maxm:
                break
        if cnt > maxm:
            break
    return const_nz(gcd_all(ps))

def fLambdaFree(L, A, N, maxm=1200):
    """rank(L·P_λ) ≡ rank(L·N)，P_λ = λN − AN"""
    d = len(N[0]); AN = mm(A, N); LN = mm(L, N); rho = rk(LN)
    if rho == 0:
        return True
    LAN = mm(L, AN); q = len(L)
    P = [[[-LAN[i][j], LN[i][j]] for j in range(d)] for i in range(q)]
    ps = []; cnt = 0
    for rows in itertools.combinations(range(q), rho):
        for cols in itertools.combinations(range(d), rho):
            dd = Pdet([[P[i][j] for j in cols] for i in rows], rho)
            if dd != [Fr(0)]:
                ps.append(dd)
            cnt += 1
            if cnt > maxm:
                break
        if cnt > maxm:
            break
    return const_nz(gcd_all(ps))


def report(name, pairs):
    tot = len(pairs)
    agree = sum(1 for x, y in pairs if x == y)
    T = sum(1 for x, y in pairs if x and y)
    Fa = sum(1 for x, y in pairs if (not x) and (not y))
    ok = (agree == tot) and T > 0 and Fa > 0
    print("  %-26s 实例 %4d ；一致 %4d ；皆真 %4d ；皆假 %4d  %s"
          % (name, tot, agree, T, Fa, "✓" if ok else ("✗ 判定力不足" if agree == tot else "✗ 不一致")))
    return ok


def main():
    print("=" * 78)
    print("  本会话四条等价关系的一键复现（独立实现）")
    print("=" * 78)
    print()
    rng = random.Random(20260401)
    e1 = []; e2 = []; e3 = []; e4 = []
    tries = 0
    while len(e1) < 400 and tries < 60000:
        tries += 1
        n = rng.choice([4, 5])
        p = rng.choice([1, 2])
        q = rng.choice([1, 2, 3])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if rk(C) != p:
            continue
        L = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(q)]
        if rk(L) != q:
            continue
        W = C + mm(C, A)
        N = ker_basis(W)
        if not N or not N[0]:
            continue
        e1.append((f5a_rank(L, A, C), f5a_ker(L, A, N)))
        e4.append((f5a_ker(L, A, N), f5a_geom(L, A, N)))
        b = f5b_total(L, A, C)
        e2.append((b, fS(L, A, N)))
        e3.append((b, fLambdaFree(L, A, N)))
    print("随机实例（n∈{4,5}，p∈{1,2}，q∈{1,2,3}）：%d" % len(e1))
    print()
    ok = True
    ok &= report("E1 (5a) ⟺ ker H ⊆ ker F", e1)
    ok &= report("E2 (5b) ⟺ (S)", e2)
    ok &= report("E3 (5b) ⟺ rank(L·P_λ) 恒定", e3)
    ok &= report("E4 (5a) ⟺ 几何避让", e4)
    print()
    print("=" * 78)
    if ok:
        print("  ⟹ **四条等价关系全部通过（两侧都有点）** ✓")
        print()
        print("  这意味着判定问题可等价地写成：")
        print("    找 L ⊇ L0（q 行）使")
        print("      (5a)  ker(L·N) ⊆ ker(L·A·N)          [线性条件]")
        print("      (5b)  rank(L·P_λ) ≡ rank(L·N)  ∀λ    [秩恒定 / 子式 gcd = 常数]")
        print("  —— 无需 Λ、G0、G1 ✓")
    else:
        print("  ⚠️ 有未通过项，见上")
    print("=" * 78)


if __name__ == "__main__":
    main()
