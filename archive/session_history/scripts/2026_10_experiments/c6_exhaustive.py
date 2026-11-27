r"""
c6_exhaustive.py -- ⭐⭐⭐ **穷举判定**：小规模实例上完全判定 (5a)∧(5b)

【为什么现在可行】
  本会话已把条件化简为（history/52 §7.6–7.8）：
     (5a) ⟺ ker(L·N) ⊆ ker(L·A·N)
     (5b) ⟺ rank(L·P_λ) ≡ rank(L·N),   P_λ = λN − AN
   ⟹ **无需解 Λ, G0, G1** ⟹ 可以对 R 直接穷举！

【做法】
  对每个实例：固定 A, C, L0 ⟹ 求 q0（用 p1）；k = q0 − r
  穷举 R ∈ {−1,0,1}^{k×n}（若 k·n ≤ 6 ⟹ ≤ 729 个）
  统计：满足 (5a) 的个数 / 满足 (5a)∧(5b) 的个数
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

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    _src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]

# ---------- 多项式 ----------
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
def Pd(a, b):
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
        _, r = Pd(a, b); a, b = b, r
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


# ---------- 化简后的判据 ----------
def cond_5a(L, A, N):
    """ker(L·N) ⊆ ker(L·A·N)"""
    LN = mm(L, N)
    LAN = mm(mm(L, A), N)
    K = ker_basis(LN)                  # d×e，列张 ker(LN)
    if not K or not K[0]:
        return True
    # K 是 d×e（行=坐标）⟹ LAN·K 应 = 0
    assert len(LAN[0]) == len(K), "维数不匹配 5a"
    return rk(mm(LAN, K)) == 0


def cond_5b(L, A, N, maxminors=800):
    """rank(L·P_λ) ≡ rank(L·N),  P_λ = λN − AN"""
    d = len(N[0])
    AN = mm(A, N)
    LN = mm(L, N)
    rho = rk(LN)
    if rho == 0:
        return True
    LAN = mm(L, AN)
    q = len(L)
    P = [[[-LAN[i][j], LN[i][j]] for j in range(d)] for i in range(q)]
    ps = []; cnt = 0
    for rows in itertools.combinations(range(q), rho):
        for cols in itertools.combinations(range(d), rho):
            dd = Pdet([[P[i][j] for j in cols] for i in rows], rho)
            if dd != [Fr(0)]:
                ps.append(dd)
            cnt += 1
            if cnt > maxminors:
                break
        if cnt > maxminors:
            break
    return const_nz(gcd_all(ps))


def is_invariant(A, N):
    AN = mm(A, N)
    if not N or not N[0]:
        return True
    cj = [N[i][:] + AN[i][:] for i in range(len(N))]
    return rk(cj) == rk(N)


def main():
    print("=== 穷举判定：(5a) ∧ (5b) 在 R 的完整枚举下 ===")
    print("=== ⭐ 分组：K 非不变 vs K 不变（CA²=0）===\n")
    print("%-6s %3s %3s %3s %4s %6s %8s %8s %8s %8s" %
          ("inst", "n", "q0", "k", "dCA", "K不变", "枚举数", "(5a)个数", "(5a∧5b)", "结论"))
    print("-" * 76)
    rng = random.Random(987654321)

    def run_group(force_invariant, want):
        """force_invariant: 是否强制 CA²=0（K 不变）"""
        found_yes = 0; found_no = 0; rows = []
        for trial in range(400000):
            if found_yes + found_no >= want:
                break
            n = 4
            p = 1
            A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
            # 选 C
            if force_invariant:
                # 需 C·A² = 0 ⟹ C 的行 ∈ 左核 of A² ⟹ 用 (A²)ᵀ 的零空间
                A2 = mm(A, A)
                A2T = [[A2[j][i] for j in range(n)] for i in range(n)]
                kerA2T = ker_basis(A2T)          # n×e
                if not kerA2T or not kerA2T[0] or len(kerA2T[0]) == 0:
                    continue
                e = len(kerA2T[0])
                Cc = [[kerA2T[j][rng.randrange(e)] for j in range(n)]]
            else:
                Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
            if rk(Cc) != p:
                continue
            if force_invariant:
                CA2 = mm(mm(Cc, A), A)
                if not all(all(x == 0 for x in r) for r in CA2):
                    continue
            else:
                CA2 = mm(mm(Cc, A), A)
                if all(all(x == 0 for x in r) for r in CA2):
                    continue          # 要**非**不变
            CA = mm(Cc, A)
            if rk(CA) != 1:
                continue
            # L0：**随机行**（不要 CA —— 那样 k=0），但要与 C 独立
            L0 = None
            for _x in range(30):
                cand = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
                if rk(cand) != 1:
                    continue
                if rk(cand + Cc) != 2:
                    continue
                L0 = cand; break
            if L0 is None:
                continue
            W = Cc + CA
            N = ker_basis(W)
            if not N or not N[0]:
                continue
            dCA = len(N[0])
            try:
                _Lx, eta = p1(A, Cc, L0)
            except Exception:
                continue
            if not eta:
                continue
            q0 = sum(eta); k = q0 - 1
            if k < 1 or k * n > 6:
                continue
            inv = is_invariant(A, N)
            if inv != force_invariant:
                continue                      # 严格分组
            n_enum = 0; n5a = 0; nboth = 0
            for vals in itertools.product([-1, 0, 1], repeat=k * n):
                R = [[Fr(vals[i * n + j]) for j in range(n)] for i in range(k)]
                L = L0 + R
                n_enum += 1
                if not cond_5a(L, A, N):
                    continue
                n5a += 1
                if cond_5b(L, A, N):
                    nboth += 1
            concl = "**YES ✓**" if nboth else ("NO（(5b)全失败）" if n5a else "无(5a)点")
            if nboth:
                found_yes += 1
            else:
                found_no += 1
            rows.append((trial, n, q0, k, dCA, "T" if inv else "F",
                         n_enum, n5a, nboth, concl))
        return rows, found_yes, found_no

    print("--- 组 1：K **非** A-不变（CA² ≠ 0）---")
    rows1, y1, n1 = run_group(False, 8)
    for rr in rows1:
        print("%-6d %3d %3d %3d %4d %6s %8d %8d %8d %8s" % rr)
    print("  小结：YES %d ；NO %d" % (y1, n1))
    print()
    print("--- 组 2：K **是** A-不变（CA² = 0）---")
    rows2, y2, n2 = run_group(True, 6)
    for rr in rows2:
        print("%-6d %3d %3d %3d %4d %6s %8d %8d %8d %8s" % rr)
    print("  小结：YES %d ；NO %d" % (y2, n2))
    print()
    print("=" * 76)
    print("【判读】")
    print("  若组 1 全 YES 且组 2 全 NO ⟹ **(5a)∧(5b) 可满足 ⟺ K 非 A-不变**")
    print("     ⟹ 判定 **多项式**（只需算一个秩）⟹ **q1 为假（非 NP-hard）** ⭐⭐⭐")
    if y1 > 0 and n1 == 0 and y2 == 0 and n2 > 0:
        print("\n⟹⟹⟹ **正是如此！** 判定 = 检查 K 的 A-不变性 ⟹ **q1 假** ⭐⭐⭐")
    elif y1 > 0 and n2 > 0:
        print("\n⟹ 组 2 也有 YES ⟹ 不变性不是精确判据（需再看）")
    else:
        print("\n⟹ 需更多数据")


if __name__ == "__main__":
    main()
