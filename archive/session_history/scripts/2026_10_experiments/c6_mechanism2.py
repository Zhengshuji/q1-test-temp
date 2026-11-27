# -*- coding: utf-8 -*-
"""
c6_mechanism2.py -- 正确的机制检验（强制 A-不变性）

【关键推导】
  若 A(range N) ⊆ range N（记 A' = A|_range N），则
      F = L∘A∘N = L∘N∘A' = H∘A'
  ⟹ Λ∘H = H∘A' ⟹ Λ(im H) = H(A'(K)) ⊆ H(K) = im H ✓
  ⟹ Λ|_im H 是 im H 上的自同态
  ⟹ 代数闭域上必有特征值 λ、特征向量 v ∈ im H (v≠0)
  ⟹ im H ∩ ker(λI − Λ) ≠ 0 ⟹ (S) 失败 ✓

【检验】在 A^2=0（⟹ A-不变）的实例上：
   (i) A(range N) ⊆ range N ？
   (ii) F = H∘A' ？
   (iii) im F ⊆ im H ？   ← 之前测错的就是这条
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


def solve_cols(Amat, Bmat):
    """解 Amat · X = Bmat（逐列）"""
    out = []
    for j in range(len(Bmat[0])):
        b = [[Bmat[i][j]] for i in range(len(Bmat))]
        r = solve_exact(Amat, b)
        if r is None: return None
        y = r[0] if isinstance(r, tuple) else r
        for i in range(len(Amat)):
            if sum(Amat[i][k] * y[k] for k in range(len(Amat[0]))) != b[i][0]:
                return None
        out.append(y)
    if not out: return None
    return [[out[j][i] for j in range(len(out))] for i in range(len(out[0]))]


def main():
    print("=== 正确机制：A-不变 ⟹ im F ⊆ im H ⟹ Λ|_imH 自同态 ===\n")
    print("%-8s %4s %4s %10s %10s %10s" %
          ("trial", "n", "q0", "A-不变?", "F=H∘A'?", "imF⊆imH?"))
    print("-" * 56)
    rng = random.Random(31415)
    tot = inv_ok = fact_ok = cont_ok = 0
    for trial in range(400000):
        if tot >= 12: break
        n, p = 6, 1
        r = 1
        # A^2 = 0 的构造：取 A = u·v^T 且 v^T u = 0
        u = [F(rng.randint(-1, 1)) for _ in range(n)]
        v = [F(rng.randint(-1, 1)) for _ in range(n)]
        if sum(u[i] * v[i] for i in range(n)) != 0: continue     # v^T u = 0
        Ac = [[u[i] * v[j] for j in range(n)] for i in range(n)]  # A = u v^T, A^2 = 0
        if rk(Ac) != 1: continue
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        L0 = mm(Cc, Ac)
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
        # (i) A-不变
        AN = mm(Ac, N)
        inv = (rk(N + AN) == rk(N))
        # 找 A' : 解 N·X = A·N
        Ap = solve_cols(N, AN) if inv else None
        # 找 (A) ∧ T5a 的 L
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
        tot += 1
        inv_ok += 1 if inv else 0
        # (ii) F = H∘A'
        f_ok = False
        if Ap is not None:
            f_ok = (mm(H, Ap) == Fm)
        fact_ok += 1 if f_ok else 0
        # (iii) im F ⊆ im H  （列拼接）
        coljoin = [[H[i][j] for j in range(d)] + [Fm[i][j] for j in range(d)]
                   for i in range(len(H))]
        cont = (rk(coljoin) == rk(H))
        cont_ok += 1 if cont else 0
        print("%-8d %4d %4d %10s %10s %10s" %
              (trial, n, q0, "✓" if inv else "✗", "✓" if f_ok else "✗",
               "✓" if cont else "**✗**"))
    print()
    print("A-不变：      %d/%d" % (inv_ok, tot))
    print("F = H∘A'：    %d/%d" % (fact_ok, tot))
    print("im F ⊆ im H： %d/%d" % (cont_ok, tot))
    print()
    if tot and cont_ok == tot and fact_ok == tot:
        print("⟹ **机制成立**：A-不变 ⟹ F = H∘A' ⟹ Λ 保持 im H ✓")
        print("   ⟹ 代数闭域上 Λ|_imH 有特征值 ⟹ (S) 失败 ✓")


if __name__ == "__main__":
    main()
