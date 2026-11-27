# -*- coding: utf-8 -*-
"""
mainline_quant_fast.py —— 支 B 上 (A)∧(S) 非空频率的**快速量化**

缩小 ℓ 预算 + 少量实例，快速给出频率量级。
关键指标：**(A)∧(S) 可满足 ⟺ 存在 (A)-点使 rank H < q0**（[history/33]）
"""
import os, io, contextlib, itertools, random
from fractions import Fraction as F
from collections import Counter

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

_b = {"__file__": os.path.join(_HERE, "batch_c6p_k.py"), "__name__": "b"}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    srcb = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(srcb.split("def main(")[0], "b", "exec"), _b)
solve_Lambda = _b["solve_Lambda"]; S_holds = _b["S_holds"]

_g = {"__file__": os.path.join(_HERE, "gen_A_system.py"), "__name__": "g"}
with open(os.path.join(_HERE, "gen_A_system.py"), encoding="utf-8") as fh:
    srcg = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(srcg.split("def main(")[0], "g", "exec"), _g)
build_general = _g["build_general"]


def mul(X, Y):
    return [[sum(X[i][a] * Y[a][j] for a in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def condA4(A, C, L):
    LA = mul(L, A); CA = mul(C, A)
    return rk(LA + L + CA + C) == rk(L + CA + C)


def gen(n, p, r, max_mp, rng, tries=800):
    for _ in range(tries):
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        mp = rng.randint(1, max_mp)
        P = [row[:] for row in Cc]
        for _k in range(mp): P = mul(P, Ac)
        if rk(P) != r or rk(P + Cc) != r + p: continue
        try: Lx, eta = p1(Ac, Cc, P)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - r
        if k < 1 or not (2*p + q0 < n): continue
        return dict(n=n, p=p, r=r, q0=q0, k=k, Ac=Ac, Cc=Cc, Lc=P)
    return None


def scan(inst, budget=60):
    Ac, Cc, Lc = inst['Ac'], inst['Cc'], inst['Lc']
    q0, k, n = inst['q0'], inst['k'], inst['n']
    nl = nA = nS = nDeg = 0
    rhoH = []
    for combo in itertools.product((-1, 0, 1), repeat=q0*k):
        if nl >= budget: break
        if all(v == 0 for v in combo): continue
        nl += 1
        ell = [[F(combo[i*k+j]) for j in range(k)] for i in range(q0)]
        try:
            rows, rhs, nv, meta = build_general(Ac, Cc, Lc, ell)
        except Exception: continue
        res = _ns["solve"](rows, rhs)
        if res is None: continue
        y, nsol = res
        for sol in ([y] + list(nsol))[:1]:
            if len(sol) != nv: continue
            R = [[sol[a*n+j] for j in range(n)] for a in range(k)]
            L = Lc + R
            if len(L) != q0 or not condA4(Ac, Cc, L): continue
            nA += 1
            W = Cc + mul(Cc, Ac); N = ker_basis(W)
            if not N or not N[0]: continue
            H = mul(L, N)
            rhoH.append(rk(H))
            if rk(H) < q0: nDeg += 1
            Fm = mul(mul(L, Ac), N)
            for Lm in solve_Lambda(Ac, Cc, L):
                if mul(Lm, H) == Fm and S_holds(Lm, H):
                    nS += 1; break
    return nl, nA, nDeg, nS, rhoH


def main():
    print("=== 支 B：(A)∧(S) 非空频率（快速版）===\n")
    print("%-16s %5s %6s %6s %8s %8s %10s" %
          ("(n,p,r)", "实例", "(A)点", "退化点", "(S)", "频率", "rankH"))
    print("-" * 66)
    rng = random.Random(21100000)
    tot = totA = totDeg = totS = 0
    for (n,p,r,mm_) in [(6,1,1,2), (7,1,1,3), (8,1,1,3), (7,2,1,3), (9,1,1,4)]:
        cnt = cA = cDeg = cS = 0
        Hc = Counter()
        for _ in range(12):
            inst = gen(n, p, r, mm_, rng)
            if inst is None: continue
            cnt += 1
            nl, nA, nDeg, nS, rhoH = scan(inst, budget=60)
            if nA: cA += 1
            if nDeg: cDeg += 1
            if nS: cS += 1
            Hc.update(rhoH)
        if cnt == 0:
            print("%-16s 无实例" % ("n=%d p=%d" % (n,p))); continue
        print("%-16s %5d %6d %6d %8d %8.2f %10s"
              % ("n=%d p=%d r=%d" % (n,p,r), cnt, cA, cDeg, cS, cS/cnt,
                 dict(sorted(Hc.items()))))
        tot += cnt; totA += cA; totDeg += cDeg; totS += cS
    print()
    print("=== 汇总 ===")
    print("支 B 实例 %d ；有 (A)点 %d ；有退化点 %d ；有 (S) %d" % (tot, totA, totDeg, totS))
    print()
    print("【判读】")
    print("  · (A) 频率 vs (S) 频率的差距 ⟹ (S) 是主要障碍")
    print("  · 若 '有退化点' 数 == '有 (S)' 数 ⟹ 印证『(S) 可满足 ⟺ 退化点存在』")


if __name__ == "__main__":
    main()
