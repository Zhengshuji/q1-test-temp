# -*- coding: utf-8 -*-
"""
c6_validate.py -- ⭐ 用**独立判据**验证 (S)

【当 q0=2, rho=1 时的简单判据】
  im H 是一维直线 L = span{v}
  (S) 失败 ⟺ ∃λ: L ∩ ker(λI − Λ) ≠ 0
  ⟺ Λ(L) ⊆ L   （因 (Λv = λv) ⟺ Λv ∈ L）
  ⟺ im F ⊆ im H   （因 F = Λ∘H ⟹ im F = Λ(im H)）
  判据：**列拼接** rk[H | F] == rk(H)

【验证策略】
  ① 在**已知 (S) 失败**的不变族（A^2=0，退化）上跑：应得"im F ⊆ im H" ✓
  ② 在**非退化平行 k=0** 族上跑：看是否"im F ⊄ im H"（⟹ (S) 成立）
  ③ 与 gcd 判据对照
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


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


def im_sub(H, Fm):
    """im F ⊆ im H ？（**列拼接**）"""
    dH = len(H[0]); dF = len(Fm[0])
    cj = [[H[i][j] for j in range(dH)] + [Fm[i][j] for j in range(dF)]
          for i in range(len(H))]
    return rk(cj) == rk(H)


def family_invariant(cnt, seed=111):
    """族 1：A^2=0（不变），L0=CA^m（退化）—— 已知 (S) 失败"""
    rng = random.Random(seed)
    out = []
    while len(out) < cnt:
        n, p = 6, 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        if mm(Ac, Ac) != [[F(0)] * n for _ in range(n)]: continue
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        mp = rng.randint(1, 2)
        L0 = mm(Cc, matpow(Ac, mp))
        if rk(L0) != 1: continue
        if rk(L0 + Cc) != 2: continue
        W = Cc + mm(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta); k = q0 - 1
        if k < 1: continue
        # 找 (A) ∧ T5a 的 L
        found = None
        for _ in range(300):
            rows = [r[:] for r in L0]
            for _i in range(k):
                rows.append([F(rng.randint(-3, 3)) for _ in range(n)])
            L = rows
            if rk(mm(L, Ac) + L + W) != rk(L + W): continue
            if rk(mm(L, N)) < q0: found = L; break
        if found is None: continue
        H = mm(found, N); Fm = mm(mm(found, Ac), N)
        if rk(H) == 0: continue
        out.append((H, Fm, "不变+退化", q0, rk(H)))
    return out


def family_nondeg(cnt, seed=222):
    """族 2：非退化平行 + k=0"""
    rng = random.Random(seed)
    out = []
    trials = 0
    while len(out) < cnt and trials < 900000:
        trials += 1
        n, p = 6, 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        d = len(N[0])
        pv = lambda v: [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]
        for _ in range(150):
            row1 = mm(Cc, Ac)[0]
            row2 = [F(rng.randint(-2, 2)) for _ in range(n)]
            L0 = [row1, row2]
            if rk(L0) != 2: continue
            if rk(L0 + Cc) != 3: continue
            if rk(mm(L0, Ac) + L0 + W) != rk(L0 + W): continue
            pL = [pv(L0[0]), pv(L0[1])]
            if all(all(x == 0 for x in w) for w in pL): continue
            pLA = [pv(mm([L0[0]], Ac)[0]), pv(mm([L0[1]], Ac)[0])]
            if rk(pL + pLA) != 1: continue
            try:
                _Lx, eta = p1(Ac, Cc, L0)
            except Exception:
                continue
            if not eta: continue
            q0 = sum(eta); k = q0 - 2
            if k != 0: continue
            H = mm(L0, N)
            if rk(H) == 0 or rk(H) >= q0: continue
            Fm = mm(mm(L0, Ac), N)
            out.append((H, Fm, "非退化+k0", q0, rk(H)))
            break
    return out


def main():
    print("=== 独立判据验证：(S) 失败 ⟺ im F ⊆ im H（q0=2,ρ=1）===\n")
    for label, fam in [("族1 不变+退化（已知 (S) 失败）", family_invariant(8)),
                       ("族2 非退化+平行+k=0", family_nondeg(8))]:
        print("--- %s ---" % label)
        print("%-4s %5s %5s %8s %12s %s" % ("#", "q0", "rkH", "rk[H|F]", "imF⊆imH?", "(S) 判定"))
        print("-" * 56)
        for i, (H, Fm, tag, q0, rH) in enumerate(fam, 1):
            dH = len(H[0]); dF = len(Fm[0])
            cj = [[H[i1][j] for j in range(dH)] + [Fm[i1][j] for j in range(dF)]
                  for i1 in range(len(H))]
            cont = (rk(cj) == rk(H))
            print("%-4d %5d %5d %8d %12s %s" %
                  (i, q0, rH, rk(cj), "✓" if cont else "**✗**",
                   "失败" if cont else "**成立**"))
        print()
    print("【判读】")
    print("  族1 若全部 'imF⊆imH ✓' ⟹ 与 batch 的 (S) 失败一致 ⟹ 判据可信 ✓")
    print("  族2 若全部 'imF⊄imH'  ⟹ (S) 成立 ⟹ **c6′ 假**（在这些实例上）")


if __name__ == "__main__":
    main()
