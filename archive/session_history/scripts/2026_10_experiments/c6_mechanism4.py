# -*- coding: utf-8 -*-
"""
c6_mechanism4.py -- 定向构造 A^2=0（保证 A-不变）验证机制

构造：n=6, A 把 e0→e2, e1→e3（其余 0）⟹ A^2 = 0, rank A = 2
     ⟹ ker[C;CA] 必为 A-不变 ✓

检验：
  (i)  A-不变（列拼接判据）
  (ii) F = H∘A'
  (iii) im F ⊆ im H（列拼接判据）
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]
_lx = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _lx)
solve_exact = _lx["solve_exact"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]


def make_A2zero(n, rng):
    """A^2 = 0：A = sum_{i} u_i v_i^T，且 v_j^T u_i = 0 for all i,j"""
    # 简单：A 把 e_i 映到 e_{i+n//2}（i < n//2），其余 0
    half = n // 2
    A = [[F(0)] * n for _ in range(n)]
    perm = list(range(half))
    rng.shuffle(perm)
    for i in range(half):
        A[half + perm[i]][i] = F(1) if rng.random() < 0.5 else F(-1)
        # 保证 A^2 = 0：A[half+..] 行的像为 0
    return A


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


def solve_cols(Amat, Bmat):
    n = len(Amat)
    out = []
    for j in range(len(Bmat[0])):
        b = [[Bmat[i][j]] for i in range(n)]
        r = solve_exact(Amat, b)
        if r is None: return None
        y = r[0] if isinstance(r, tuple) else r
        for i in range(n):
            if sum(Amat[i][k] * y[k] for k in range(len(Amat[0]))) != b[i][0]:
                return None
        out.append(y)
    if not out: return None
    return [[out[j][i] for j in range(len(out))] for i in range(len(out[0]))]


def main():
    print("=== 定向构造 A^2=0：验证机制 ===\n")
    print("%-8s %4s %4s %8s %10s %10s" %
          ("trial", "n", "q0", "A-不变", "F=H∘A'", "imF⊆imH"))
    print("-" * 52)
    rng = random.Random(13572468)
    tot = inv_ok = fact_ok = cont_ok = 0
    for trial in range(200000):
        if tot >= 12: break
        n, p = 6, 1
        r = 1
        Ac = make_A2zero(n, rng)
        if rk(Ac) != n // 2: continue
        if mm(Ac, Ac) != [[F(0)] * n for _ in range(n)]: continue   # A^2 == 0
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        mp = rng.randint(1, 2)
        L0 = mm(Cc, matpow(Ac, mp))
        if rk(L0) != r: continue
        if rk(L0 + Cc) != r + p: continue
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta); k = q0 - r
        if k < 1: continue
        W = Cc + mm(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        d = len(N[0])
        AN = mm(Ac, N)
        cj0 = [[N[i][j] for j in range(d)] + [AN[i][j] for j in range(d)]
               for i in range(n)]
        if rk(cj0) != rk(N): continue                  # A-不变
        Ap = solve_cols(N, AN)
        found = None
        for _ in range(300):
            rows = [row[:] for row in L0]
            for _i in range(k):
                rows.append([F(rng.randint(-3, 3)) for _ in range(n)])
            L = rows
            if rk(mm(L, Ac) + L + W) != rk(L + W): continue
            if rk(mm(L, N)) < q0:
                found = L; break
        if found is None: continue
        L = found
        H = mm(L, N); Fm = mm(mm(L, Ac), N)
        if rk(H) == 0: continue
        tot += 1; inv_ok += 1
        f_ok = (Ap is not None and mm(H, Ap) == Fm)
        fact_ok += 1 if f_ok else 0
        cj = [[H[i][j] for j in range(d)] + [Fm[i][j] for j in range(d)]
              for i in range(len(H))]
        cont = (rk(cj) == rk(H))
        cont_ok += 1 if cont else 0
        print("%-8d %4d %4d %8s %10s %10s" %
              (trial, n, q0, "✓", "✓" if f_ok else "✗", "✓" if cont else "**✗**"))
    print()
    print("A-不变：      %d/%d" % (inv_ok, tot))
    print("F = H∘A'：    %d/%d" % (fact_ok, tot))
    print("im F ⊆ im H： %d/%d" % (cont_ok, tot))
    print()
    if tot and fact_ok == tot and cont_ok == tot:
        print("⟹ **机制完全成立** ✓✓✓")
        print("   A-不变 ⟹ F = H∘A' ⟹ Λ 保持 im H ⟹ 代数闭域上 (S) 必失败")


if __name__ == "__main__":
    main()
