# -*- coding: utf-8 -*-
"""
mainline_structure.py —— 见证的**结构**分析：为什么 (A) 常见而 (A)∧(S) 罕见？

对若干支 B 实例：
  ① 若 (A) 成立 ⟹ (S) 失败，找出**失败的机制**（哪个 λ、im H ∩ ker(λI-Λ)）
  ② 对比"有见证"与"无见证"实例的结构差异
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
det_of = _ns["det_of"] if "det_of" in _ns else None

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


def collect_As(inst, budget=200, vals=(-1, 0, 1)):
    """收集 (A)-点（L 与 ΛH=F 的信息）"""
    Ac, Cc, Lc = inst['Ac'], inst['Cc'], inst['Lc']
    q0, k, n = inst['q0'], inst['k'], inst['n']
    out = []
    nl = 0
    for combo in itertools.product(vals, repeat=q0*k):
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
            if len(L) != q0: continue
            if not condA4(Ac, Cc, L): continue
            W = Cc + mul(Cc, Ac); N = ker_basis(W)
            if not N or not N[0]: continue
            H = mul(L, N)
            Fm = mul(mul(L, Ac), N)
            good = [Lm for Lm in solve_Lambda(Ac, Cc, L) if mul(Lm, H) == Fm]
            if not good: continue
            out.append(dict(L=L, H=H, F=Fm, Lam=good, N=N, ell=ell))
    return out


def main():
    print("=== 见证结构分析 ===\n")
    rng = random.Random(21000000)
    # 找 3 个有见证的实例 + 3 个无见证的，作对比
    n_wit = n_nowit = 0
    stats = {"wit": Counter(), "nowit": Counter()}
    for trial in range(60):
        inst = gen_branchB(6, 1, 1, 2, rng)
        if inst is None: continue
        As = collect_As(inst, budget=150)
        if not As: continue
        has_S = False; rminfo = []
        for a in As:
            H = a['H']
            for Lm in a['Lam']:
                if S_holds(Lm, H):
                    has_S = True; break
            rminfo.append((rk(H), inst['q0'], len(a['N'][0])))
        tag = "wit" if has_S else "nowit"
        if has_S and n_wit >= 3: continue
        if (not has_S) and n_nowit >= 3: continue
        if has_S: n_wit += 1
        else: n_nowit += 1
        # 统计
        for (rh, q0, dca) in rminfo:
            stats[tag][(rh, q0, dca)] += 1
        print("[%s] 实例 q0=%d k=%d ；(A)-点 %d ；有 (S) 见证 %s"
              % (tag, inst['q0'], inst['k'], len(As), has_S))
        if As:
            a = As[0]
            print("     rank H = %d ；q0 = %d ；d_CA = %d" %
                  (rk(a['H']), inst['q0'], len(a['N'][0])))
        if n_wit >= 3 and n_nowit >= 3: break
    print()
    print("=== 统计 ===")
    for tag in ("wit", "nowit"):
        print("%s: (rankH, q0, d_CA) 分布 = %s" % (tag, dict(stats[tag])))
    print()
    print("【判读】")
    print("  · 若 'wit' 的 rank H < q0 而 'nowit' 的 rank H = q0 ⟹ (S) 可满足 ⟺ 退化(rankH<q0)")
    print("    —— 与项目 T5a 的直觉一致（T5a 就是 rank(LN_CA) < q0）")


if __name__ == "__main__":
    main()
