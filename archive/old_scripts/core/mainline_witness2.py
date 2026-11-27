# -*- coding: utf-8 -*-
"""
mainline_witness2.py —— 稳健地找并核验一个支 B 的 (A)∧(S) 见证

策略：从实例端搜索（多种 n/p/mpow/seed），对每个支 B 实例枚举 ℓ，
      一旦找到 (A)∧(S) 见证就**打印全部数据**并独立核验。
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


def candidate_instances(n, p, r, mpow, n_seed):
    """生成若干支 B 实例"""
    out = []
    for seed in range(n_seed):
        rng = random.Random(30000000 + 7777*mpow + 131*seed + 17*n)
        for _ in range(600):
            Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
            Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
            if rk(Cc) != p: continue
            P = [row[:] for row in Cc]
            for _k in range(mpow):
                P = mul(P, Ac)
            if rk(P) != r or rk(P + Cc) != r + p: continue
            try: Lx, eta = p1(Ac, Cc, P)
            except Exception: continue
            if not Lx: continue
            q0 = sum(eta); k = q0 - r
            if k < 1: continue
            if not (2*p + q0 < n): continue
            out.append(dict(n=n, p=p, r=r, mpow=mpow, q0=q0, k=k,
                            Ac=Ac, Cc=Cc, Lc=P))
            break
    return out


def main():
    print("=== 稳健搜索支 B 的 (A)∧(S) 见证 ===\n")
    shapes = [(6,1,1,1,6), (6,1,1,2,6), (7,1,1,2,6), (7,1,1,3,6), (6,2,1,2,6), (8,1,1,3,6)]
    tot_inst = tot_A = tot_S = 0
    for (n,p,r,mp,ns) in shapes:
        insts = candidate_instances(n, p, r, mp, ns)
        if not insts:
            print("(n=%d p=%d CA^%d) 无支 B 实例" % (n,p,mp)); continue
        for inst in insts[:3]:
            Ac, Cc, Lc = inst['Ac'], inst['Cc'], inst['Lc']
            q0, k, n_ = inst['q0'], inst['k'], inst['n']
            tot_inst += 1
            nA = nS = 0; wit = None
            for combo in itertools.product((-1,0,1), repeat=q0*k):
                if all(v == 0 for v in combo): continue
                ell = [[F(combo[i*k+j]) for j in range(k)] for i in range(q0)]
                try:
                    rows, rhs, nv, meta = build_general(Ac, Cc, Lc, ell)
                except Exception: continue
                res = _ns["solve"](rows, rhs)
                if res is None: continue
                y, nsol = res
                for sol in ([y] + list(nsol))[:2]:
                    if len(sol) != nv: continue
                    R = [[sol[a*n_+j] for j in range(n_)] for a in range(k)]
                    L = Lc + R
                    if len(L) != q0: continue
                    if not condA4(Ac, Cc, L): continue
                    nA += 1
                    W = Cc + mul(Cc, Ac); N = ker_basis(W)
                    if not N or not N[0]: continue
                    H = mul(L, N)
                    if rk(H) == 0: continue
                    good = [Lm for Lm in solve_Lambda(Ac, Cc, L)
                            if mul(Lm, H) == mul(mul(L, Ac), N) and S_holds(Lm, H)]
                    if good:
                        nS += 1
                        if wit is None and nS == 1:
                            wit = (ell, R, L, H, N, good[0])
            tot_A += nA; tot_S += nS
            tag = "n=%d p=%d q0=%d k=%d" % (n,p,q0,k)
            print("%-22s ℓ试 %4d | (A) %4d | (S) %4d %s"
                  % (tag, 3**(q0*k)-1, nA, nS, "★有见证" if nS else ""))
            if wit and nS:
                ell, R, L, H, N, Lam = wit
                print("\n★★★ 见证数据 ★★★")
                print("A  =", [[str(x) for x in row] for row in Ac])
                print("C  =", [[str(x) for x in row] for row in Cc])
                print("L0 =", [[str(x) for x in row] for row in Lc])
                print("ℓ  =", [[str(x) for x in row] for row in ell])
                print("L  =", [[str(x) for x in row] for row in L])
                print("H  =", [[str(x) for x in row] for row in H], "rankH =", rk(H))
                print("Λ  =", [[str(x) for x in row] for row in Lam])
                print()
                print("── 独立核验 ──")
                print("  支 B: 2p+q0 = %d < n = %d ✓" % (2*p+inst['q0'], n))
                print("  (A) 4块 : %s" % condA4(Ac, Cc, L))
                print("  ΛH = LAN: %s" % (mul(Lam, H) == mul(mul(L, Ac), N)))
                print("  (S)     : %s" % S_holds(Lam, H))
                out = dict(n=n, p=p, r=r, q0=inst['q0'], k=inst['k'],
                           A=[[str(x) for x in row] for row in Ac],
                           C=[[str(x) for x in row] for row in Cc],
                           L0=[[str(x) for x in row] for row in Lc],
                           L=[[str(x) for x in row] for row in L],
                           Lam=[[str(x) for x in row] for row in Lam],
                           H=[[str(x) for x in row] for row in H])
                with open(os.path.join(_HERE, "witness_branchB.json"), "w",
                          encoding="utf-8") as fh:
                    json.dump(out, fh, ensure_ascii=False, indent=1)
                print("\n  已保存 scripts/core/witness_branchB.json")
                return
        print()
    print("=== 汇总：实例 %d ；(A) %d ；(S) %d ===" % (tot_inst, tot_A, tot_S))


if __name__ == "__main__":
    main()
