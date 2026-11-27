# -*- coding: utf-8 -*-
"""
c6_rank_def.py -- c6′ 的更弱机制：rank(LAN) < rank(LN) ？

【动机】
  (A) ⟹ F = Λ∘H（F = LAN, H = LN）
  若 rank F < rank H，则 Λ|_im H 降秩 ⟹ im H ∩ ker Λ ≠ 0 ⟹ (S) 失败 ✓
  这比 "F = 0" 弱得多（F=0 只是 rank F = 0 的特例）

【检验】在 c6′ 实例（真平行 ∧ (A) ∧ T5a ∧ k≥1）上检查 rank(LAN) < rank(LN)
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
    print("=== c6′: rank(LAN) < rank(LN) ？ ===\n")
    print("%-10s %4s %4s %5s %5s %8s %8s %8s %7s" %
          ("trial", "n", "q0", "rkLN", "rkLAN", "rank<", "T5a", "平行", "判定"))
    print("-" * 68)
    rng = random.Random(20250101)
    ok = tot = 0
    lt_cnt = eq_cnt = 0
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
        # 真平行
        pv = lambda v: [sum(v[i] * N[i][j] for i in range(n)) for j in range(dCA)]
        pL0 = pv(L0[0]); pL0A = pv(mm(L0, Ac)[0])
        par = (rk([pL0, pL0A]) == 1) if any(pL0) else True
        if not par: continue
        # 找 (A) 成立的 q0 行 L（含 L0）
        found = None
        for _ in range(300):
            rows = [row[:] for row in L0]
            for _i in range(k):
                rows.append([F(rng.randint(-3, 3)) for _ in range(n)])
            L = rows
            if rk(mm(L, Ac) + L + W) != rk(L + W): continue
            H = mm(L, N)
            if rk(H) < q0:
                found = L; break
        if found is None: continue
        L = found
        H = mm(L, N); Fm = mm(mm(L, Ac), N)
        rH, rF = rk(H), rk(Fm)
        if rH == 0: continue
        tot += 1
        is_lt = rF < rH
        ok += 1 if is_lt else 0
        if is_lt: lt_cnt += 1
        else: eq_cnt += 1
        print("%-10d %4d %4d %5d %5d %8s %8d %8s %7s" %
              (trial, n, q0, rH, rF, "✓" if is_lt else "✗",
               q0, "T", "秩降" if is_lt else "**相等**"))
    print()
    print("⟹ rank(LAN) < rank(LN)：%d/%d" % (ok, tot))
    print("   其中严格小于 %d 个，相等 %d 个" % (lt_cnt, eq_cnt))


if __name__ == "__main__":
    main()
