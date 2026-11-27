# -*- coding: utf-8 -*-
"""
mainline_witness_pin.py —— 钉死一个支 B 的 (A)∧(S) 见证，并逐项独立核验

1. 用与 mainline_claim **完全一致**的实例搜索（randint 立即转 F）
2. 枚举 ℓ 找 (A)∧(S) 见证
3. 打印 (A,C,L0,L,R,ℓ,Λ,H) 全部数据
4. 独立重验 (A)（4 块）、分解 ΛH=F、(S)（子式 gcd）、支 B
"""
import os, io, contextlib, itertools, random, json
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


def condA4(A, C, L):
    LA = mul(L, A); CA = mul(C, A)
    return rk(LA + L + CA + C) == rk(L + CA + C)


def find_inst():
    rng = random.Random(20800000 + 1000*1 + 100*0 + 6)
    for _ in range(2500):
        Ac = [[F(rng.randint(-1, 1)) for _ in range(6)] for _ in range(6)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(6)]]
        if rk(Cc) != 1: continue
        P = [row[:] for row in Cc]
        if rk(P) != 1 or rk(P + Cc) != 2: continue
        try: Lx, eta = p1(Ac, Cc, P)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - 1
        if k < 1 or not (2 + q0 < 6): continue
        return dict(Ac=Ac, Cc=Cc, Lc=P, q0=q0, k=k)
    return None


def main():
    print("=== 钉死支 B 的 (A)∧(S) 见证 ===\n")
    inst = find_inst()
    if not inst:
        print("未找到实例"); return
    Ac, Cc, Lc = inst['Ac'], inst['Cc'], inst['Lc']
    q0, k, n = inst['q0'], inst['k'], 6
    print("实例：n=6 p=1 r=1 q0=%d k=%d ；支 B？ 2p+q0=%d < 6 ： %s"
          % (q0, k, 2+q0, 2+q0 < 6))
    print("A  =", [[str(x) for x in row] for row in Ac])
    print("C  =", [[str(x) for x in row] for row in Cc])
    print("L0 =", [[str(x) for x in row] for row in Lc])
    print()
    # 枚举 ℓ
    for combo in itertools.product((-1, 0, 1), repeat=q0*k):
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
            R = [[sol[a*n + j] for j in range(n)] for a in range(k)]
            L = Lc + R
            if len(L) != q0: continue
            if not condA4(Ac, Cc, L): continue
            W = Cc + mul(Cc, Ac); N = ker_basis(W)
            H = mul(L, N)
            if rk(H) == 0: continue
            S_lams = [Lm for Lm in solve_Lambda(Ac, Cc, L) if S_holds(Lm, H)]
            if not S_lams: continue
            # ★ 找到见证
            print("★ 见证找到 ✓")
            print("  ℓ  =", [[str(x) for x in row] for row in ell])
            print("  R  =", [[str(x) for x in row] for row in R])
            print("  L  =", [[str(x) for x in row] for row in L])
            print("  N_CA =", [[str(x) for x in row] for row in N])
            print("  H = L·N_CA =", [[str(x) for x in row] for row in H], " rank =", rk(H))
            print()
            print("── 独立核验 ──")
            LA = mul(L, Ac); CA = mul(Cc, Ac)
            print("  (A) 4块： rank[LA;L;CA;C]=%d , rank[L;CA;C]=%d ⟹ %s"
                  % (rk(LA + L + CA + Cc), rk(L + CA + Cc), condA4(Ac, Cc, L)))
            Fm = mul(LA, N)
            allL = solve_Lambda(Ac, Cc, L)
            goodL = [Lm for Lm in allL if mul(Lm, H) == Fm]
            print("  ΛH = F 的解： %d / %d 个 Λ" % (len(goodL), len(allL)))
            nS = sum(1 for Lm in goodL if S_holds(Lm, H))
            print("  其中 (S) 成立： %d" % nS)
            if goodL:
                print("  Λ（第一个）+ (S)=%s" % S_holds(goodL[0], H))
                print("     ", [[str(x) for x in row] for row in goodL[0]])
            # 保存
            out = dict(n=n, p=1, r=1, q0=q0, k=k,
                       A=[[str(x) for x in row] for row in Ac],
                       C=[[str(x) for x in row] for row in Cc],
                       L0=[[str(x) for x in row] for row in Lc],
                       ell=[[str(x) for x in row] for row in ell],
                       L=[[str(x) for x in row] for row in L],
                       H=[[str(x) for x in row] for row in H])
            with open(os.path.join(_HERE, "witness_branchB.json"), "w", encoding="utf-8") as fh:
                json.dump(out, fh, ensure_ascii=False, indent=1)
            print("\n  已保存到 scripts/core/witness_branchB.json")
            return
    print("未找到见证")


if __name__ == "__main__":
    main()
