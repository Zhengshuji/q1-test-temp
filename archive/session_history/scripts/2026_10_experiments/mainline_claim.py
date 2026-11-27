# -*- coding: utf-8 -*-
"""
mainline_claim.py —— 检验新猜想：**支 B 上 (A)∧(S) 恒空？**

对照 $k=1$ 与 $k\ge2$：
  · $k=1$：Ω*_J 是单点（[history/30]）⟹ (S) 是否在该点成立？
  · $k\ge2$：Ω*_J 正维数 ⟹ (S) 在其上是否可能成立？

用**小形状 + 穷举 ℓ**，逐实例精确判定。
"""
import os, io, contextlib, itertools, random
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


def checkA(Ac, Cc, L):
    W = Cc + mul(Cc, Ac)
    B = ker_basis(W)
    if not B or not B[0]: return False
    P = mm(L, B); PA = mm(mm(L, Ac), B)
    return rk(P + PA) == rk(P)


def make_inst(n, p, r, mpow, seed, tries=2500):
    rng = random.Random(seed)
    for _ in range(tries):
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        P = [row[:] for row in Cc]
        for _k in range(mpow): P = mul(P, Ac)
        if rk(P) != r or rk(P + Cc) != r + p: continue
        try: Lx, eta = p1(Ac, Cc, P)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - r
        if k < 1: continue
        if not (2 * p + q0 < n): continue
        return dict(n=n, p=p, r=r, q0=q0, k=k, Ac=Ac, Cc=Cc, Lc=P)
    return None


def scan(inst, max_l=400, vals=(-1, 0, 1)):
    Ac, Cc, Lc = inst['Ac'], inst['Cc'], inst['Lc']
    q0, k, r_, n_ = inst['q0'], inst['k'], inst['r'], inst['n']
    n_l = n_A = n_S = 0
    wit = None
    for combo in itertools.product(vals, repeat=q0*k):
        if n_l >= max_l: break
        if all(v == 0 for v in combo): continue
        ell = [[F(combo[i*k + j]) for j in range(k)] for i in range(q0)]
        try:
            rows, rhs, nv, meta = build_general(Ac, Cc, Lc, ell)
        except Exception:
            continue
        res = _ns["solve"](rows, rhs)
        if res is None: continue
        y, nsol = res
        for sol in ([y] + list(nsol))[:3]:
            if len(sol) != nv: continue
            R = [[sol[a*n_ + j] for j in range(n_)] for a in range(k)]
            L = Lc + R
            if len(L) != q0: continue
            n_l += 1
            if not checkA(Ac, Cc, L): continue
            n_A += 1
            W = Cc + mul(Cc, Ac); N = ker_basis(W)
            if not N or not N[0]: continue
            H = mul(L, N)
            if rk(H) == 0: continue
            got = False
            for Lam in solve_Lambda(Ac, Cc, L):
                if S_holds(Lam, H): got = True; break
            if got:
                n_S += 1
                if wit is None:
                    wit = ([[str(x) for x in row] for row in ell],
                           [[str(x) for x in row] for row in L])
    return n_l, n_A, n_S, wit


def main():
    print("=== 支 B 上 (A)∧(S) 是否恒空？（对照 k=1 与 k>=2）===\n")
    print("%-32s %6s %6s %6s %8s" % ("实例", "ℓ试", "(A)", "(S)", "结论"))
    print("-" * 64)
    shapes = [(6,1,1,1), (7,1,1,1), (6,1,1,2), (7,1,1,2), (8,1,1,3), (7,2,1,2)]
    totA = totS = 0
    for (n,p,r,mp) in shapes:
        inst = None
        for seed in range(8):
            inst = make_inst(n, p, r, mp, 20800000 + 1000*mp + 100*seed + n)
            if inst: break
        if not inst:
            print("%-32s 未找到实例" % ("n=%d p=%d CA^%d" % (n,p,mp))); continue
        q0, k = inst['q0'], inst['k']
        nl, nA, nS, wit = scan(inst, max_l=400)
        totA += nA; totS += nS
        tag = "n=%d p=%d r=%d q0=%d k=%d" % (n,p,r,q0,k)
        print("%-32s %6d %6d %6d %8s" % (tag, nl, nA, nS,
                                         "有见证!" if nS else "空"))
        if wit and nS:
            print("     ★ 见证：ℓ=%s" % wit[0])
            print("            L=%s" % wit[1])
    print()
    print("=== 汇总 ===")
    print("(A)-点 %d ；(A)∧(S) 成立 %d" % (totA, totS))
    if totA and totS == 0:
        print("⟹ **支 B 上 (A)∧(S) 未找到任何见证** ⟹ 支持猜想：支 B 恒空")
    elif totS:
        print("⟹ **支 B 可非空** ⟹ 支 B 是硬度候选 ✓")


if __name__ == "__main__":
    main()
