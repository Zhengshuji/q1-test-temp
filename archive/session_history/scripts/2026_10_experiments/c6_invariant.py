# -*- coding: utf-8 -*-
"""
c6_invariant.py -- c6′ 的真正机制：im(LAN) ⊆ im(LN) ？

【机制】
  (A) ⟹ F = Λ∘H（F = LAN, H = LN）
  若 im F ⊆ im H，则 Λ(im H) ⊆ im H ⟹ Λ|_im H 是 im H 上的自同态
  ⟹ 在**代数闭域**上必有特征值 λ 与特征向量 v ∈ im H
  ⟹ (S) 失败 ✓

  —— 这与数值一致（rank(LAN)=rank(LN) 且 (S) 失败）

【检验】rk[LN | LAN] == rk(LN)   （**列拼接**）
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


def main():
    print("=== c6′: im(LAN) ⊆ im(LN) ? ===\n")
    print("%-10s %4s %4s %6s %6s %10s %8s" %
          ("trial", "n", "q0", "rkLN", "rkLN|LAN", "包含?", "T5a"))
    print("-" * 56)
    rng = random.Random(777001)
    ok = tot = 0
    for trial in range(400000):
        if tot >= 14: break
        n, p = 6, 1
        r = 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        mp = rng.randint(1, 3)
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
        dCA = len(N[0])
        pv = lambda v: [sum(v[i] * N[i][j] for i in range(n)) for j in range(dCA)]
        pL0 = pv(L0[0]); pL0A = pv(mm(L0, Ac)[0])
        if any(pL0) and rk([pL0, pL0A]) != 1: continue      # 真平行
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
        # 列拼接 rk[LN | LAN]
        d = len(H[0])
        coljoin = [[H[i][j] for j in range(d)] + [Fm[i][j] for j in range(d)]
                   for i in range(len(H))]
        contained = (rk(coljoin) == rk(H))
        tot += 1
        ok += 1 if contained else 0
        print("%-10d %4d %4d %6d %6d %10s %8d" %
              (trial, n, q0, rk(H), rk(coljoin),
               "✓" if contained else "**✗**", q0))
    print()
    print("⟹ im(LAN) ⊆ im(LN)：%d/%d" % (ok, tot))
    if tot and ok == tot:
        print("⟹ **机制成立**：Λ 保持 im H ⟹ 代数闭域上 (S) 必失败 ✓")
        print("   ⟹ 这是可 Lean 化的路线（需 `IsAlgClosed` + 特征值存在性）")


if __name__ == "__main__":
    main()
