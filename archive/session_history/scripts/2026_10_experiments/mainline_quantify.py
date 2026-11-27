# -*- coding: utf-8 -*-
"""
mainline_quantify.py —— 支 B 上 (A)∧(S) 非空的**频率**与**结构**

量化（200+ 实例）：
  ① 支 B 实例总数
  ② 有 (A)-点的实例数
  ③ 有 (A)∧(S) 见证的实例数（**关键**）
  ④ 每实例的 (A)-点数 与 (S)-点数
结构：
  ⑤ 见证的 Λ 的特征值、H 的秩（rank H < q0 是否总成立）
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


def gen_branchB(n, p, r, max_mpow, rng, tries=1500):
    """随机参数下生成一个支 B 实例（尝试多个 mpow）"""
    for _ in range(tries):
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        mp = rng.randint(1, max_mpow)
        P = [row[:] for row in Cc]
        for _k in range(mp): P = mul(P, Ac)
        if rk(P) != r or rk(P + Cc) != r + p: continue
        try: Lx, eta = p1(Ac, Cc, P)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - r
        if k < 1: continue
        if not (2*p + q0 < n): continue
        return dict(n=n, p=p, r=r, mp=mp, q0=q0, k=k, Ac=Ac, Cc=Cc, Lc=P)
    return None


def scan_instance(inst, ell_budget=250, vals=(-1, 0, 1)):
    Ac, Cc, Lc = inst['Ac'], inst['Cc'], inst['Lc']
    q0, k, n = inst['q0'], inst['k'], inst['n']
    n_ell = nA = nS = 0
    H_ranks = []
    for combo in itertools.product(vals, repeat=q0*k):
        if n_ell >= ell_budget: break
        if all(v == 0 for v in combo): continue
        n_ell += 1
        ell = [[F(combo[i*k+j]) for j in range(k)] for i in range(q0)]
        try:
            rows, rhs, nv, meta = build_general(Ac, Cc, Lc, ell)
        except Exception: continue
        res = _ns["solve"](rows, rhs)
        if res is None: continue
        y, nsol = res
        for sol in ([y] + list(nsol))[:2]:
            if len(sol) != nv: continue
            R = [[sol[a*n+j] for j in range(n)] for a in range(k)]
            L = Lc + R
            if len(L) != q0: continue
            if not condA4(Ac, Cc, L): continue
            nA += 1
            W = Cc + mul(Cc, Ac); N = ker_basis(W)
            if not N or not N[0]: continue
            H = mul(L, N)
            if rk(H) == 0: continue
            Fm = mul(mul(L, Ac), N)
            for Lm in solve_Lambda(Ac, Cc, L):
                if mul(Lm, H) == Fm and S_holds(Lm, H):
                    nS += 1
                    H_ranks.append(rk(H))
                    break
    return n_ell, nA, nS, H_ranks


def main():
    print("=== 支 B 上 (A)∧(S) 非空的频率（大样本）===\n")
    rng = random.Random(20900000)
    shapes = [(6,1,1,2), (7,1,1,3), (8,1,1,3), (7,2,1,3), (8,2,1,3), (9,1,1,4), (6,1,2,2)]
    print("%-16s %6s %6s %8s %8s %10s" %
          ("(n,p,r)", "实例", "有(A)", "有(A)∧(S)", "频率", "rankH分布"))
    print("-" * 64)
    tot = totA = totS = 0
    allH = Counter()
    for (n,p,r,mm_) in shapes:
        cnt = cntA = cntS = 0
        Hr = []
        for _ in range(40):
            inst = gen_branchB(n, p, r, mm_, rng)
            if inst is None: continue
            cnt += 1
            nl, nA, nS, Hs = scan_instance(inst)
            if nA: cntA += 1
            if nS: cntS += 1
            Hr += Hs
        if cnt == 0:
            print("%-16s 无实例" % ("n=%d p=%d r=%d" % (n,p,r))); continue
        freq = cntS / cnt
        hc = Counter(Hr)
        print("%-16s %6d %6d %8d %8.2f %10s"
              % ("n=%d p=%d r=%d" % (n,p,r), cnt, cntA, cntS, freq,
                 dict(sorted(hc.items()))))
        tot += cnt; totA += cntA; totS += cntS
        allH.update(Hr)
        print()
    print("=== 汇总 ===")
    print("支 B 实例 %d ；有 (A)-点 %d (%.1f%%) ；有 (A)∧(S) %d (%.1f%%)"
          % (tot, totA, 100*totA/tot if tot else 0,
             totS, 100*totS/tot if tot else 0))
    print("见证中 rank H 的分布：", dict(sorted(allH.items())))
    print()
    print("【判读】")
    print("  · 若 (A)∧(S) 频率很高 ⟹ 支 B 常见可满足 ⟹ 更可能是硬度源")
    print("  · 若频率低 ⟹ 支 B 稀疏可满足 ⟹ 复杂度仍开放")


if __name__ == "__main__":
    main()
