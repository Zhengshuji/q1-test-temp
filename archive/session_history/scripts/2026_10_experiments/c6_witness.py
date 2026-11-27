# -*- coding: utf-8 -*-
"""
c6_witness.py -- ⭐⭐⭐ 提取并**独立验证**"情形 II 平行 + (5a) ∧ (5b) 可为 YES"的显式见证

【独立验证】
  ① H1–H4
  ② (5a)  直接算 rank[LA;L;CA;C] vs rank[L;CA;C]
  ③ (5b)  对**多个具体 λ** 直接算 rank[λL−LA;CA;C] vs rank[L;CA;C]
          （不用多项式 gcd —— 完全独立的判据）
  ④ 情形 II：d_CA ≥ q0
  ⑤ 平行：rank[π(L0); π(L0A)] = 1 且 π(L0) ≠ 0
"""
import os, io, contextlib, random, json
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


def obs(M, A, n):
    rows = [r[:] for r in M]; cur = [r[:] for r in M]
    for _ in range(n - 1):
        cur = mm(cur, A); rows = rows + cur
    return rows


def h4_ok(L0, Cc, Ac, n):
    return rk(obs(L0, Ac, n) + obs(Cc, Ac, n)) == rk(obs(Cc, Ac, n))


def scalar_mul_rows(M, c):
    return [[c * x for x in row] for row in M]


def verify(A, C, L0, n):
    p = len(C)
    Q0 = len(L0)
    CA = mm(C, A)
    W = C + CA
    out = {}
    out["H1_rankC"] = rk(C) == p
    out["H2_rankL0"] = rk(L0) == Q0
    out["H3_rankL0C"] = rk(L0 + C) == Q0 + p
    out["H4_funobs"] = h4_ok(L0, C, A, n)
    # (5a)
    out["5a"] = (rk(mm(L0, A) + L0 + W) == rk(L0 + W))
    # (5b)：对多个具体 λ 直接算
    r0 = rk(L0 + W)
    lam_list = [F(0), F(1), F(-1), F(2), F(-2), F(3), F(1, 2), F(-1, 2),
                F(5), F(7), F(11), F(1, 3), F(-3, 2)]
    ok5b = True
    detail = []
    LA = mm(L0, A)
    for lam in lam_list:
        M = [[lam * L0[i][j] - LA[i][j] for j in range(n)] for i in range(Q0)]
        M = M + [r[:] for r in CA] + [r[:] for r in C]
        rr = rk(M)
        detail.append((str(lam), rr, r0))
        if rr != r0:
            ok5b = False
    out["5b_atsampled"] = ok5b
    out["5b_detail"] = detail
    out["r0"] = r0
    # 情形 II
    N = ker_basis(W)
    dCA = n - rk(W)
    out["d_CA"] = dCA
    H = mm(L0, N)
    out["rankH"] = rk(H)
    out["q0"] = Q0
    out["caseII"] = dCA >= Q0
    out["T5a"] = rk(H) < Q0
    # 平行
    pv = lambda v: [sum(v[i] * N[i][j] for i in range(n)) for j in range(dCA)]
    pL = [pv(L0[i]) for i in range(Q0)]
    pLA = [pv(mm([L0[i]], A)[0]) for i in range(Q0)]
    out["parallel"] = (rk(pL + pLA) <= 1)
    out["nonDegenerate"] = any(any(x != 0 for x in w) for w in pL)
    return out


def main():
    print("=== 提取见证：情形 II 平行 + (5a)∧(5b) ===")
    rng = random.Random(246813579)
    for trial in range(200000):
        n, p = 6, 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        d = len(N[0])
        pv = lambda v: [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]
        found = None
        for _ in range(150):
            row1 = mm(Cc, Ac)[0]
            row2 = [F(rng.randint(-2, 2)) for _ in range(n)]
            L0 = [row1, row2]
            if rk(L0) != 2: continue
            if rk(L0 + Cc) != 3: continue
            if not h4_ok(L0, Cc, Ac, n): continue
            if rk(mm(L0, Ac) + L0 + W) != rk(L0 + W): continue
            pL = [pv(L0[0]), pv(L0[1])]
            if all(all(x == 0 for x in w) for w in pL): continue
            pLA = [pv(mm([L0[0]], Ac)[0]), pv(mm([L0[1]], Ac)[0])]
            if rk(pL + pLA) != 1: continue
            found = L0; break
        if found is None: continue
        L0 = found
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta)
        if q0 != 2: continue
        v = verify(Ac, Cc, L0, n)
        if not (v["H1_rankC"] and v["H2_rankL0"] and v["H3_rankL0C"] and v["H4_funobs"]):
            continue
        if not (v["5a"] and v["5b_atsampled"] and v["caseII"] and v["parallel"]
                and v["nonDegenerate"] and v["T5a"]):
            continue
        print("\n*** 找到见证（trial=%d）***\n" % trial)
        print("n = %d, p = %d, r = %d, q0 = %d, d_CA = %d"
              % (n, p, 2, q0, v["d_CA"]))
        print("A =", [[str(x) for x in row] for row in Ac])
        print("C =", [[str(x) for x in row] for row in Cc])
        print("L0 =", [[str(x) for x in row] for row in L0])
        print()
        for k in ["H1_rankC", "H2_rankL0", "H3_rankL0C", "H4_funobs", "5a",
                  "5b_atsampled", "caseII", "parallel", "nonDegenerate", "T5a"]:
            print("  %-16s : %s" % (k, v[k]))
        print("  r0 = rank[L0;CA;C] = %d ; rankH = %d" % (v["r0"], v["rankH"]))
        print("\n  (5b) 逐 λ 验证（rank[λL−LA;CA;C] 应恒 = %d）:" % v["r0"])
        for lam, rr, r0 in v["5b_detail"]:
            print("     λ=%-6s -> rank=%d %s" % (lam, rr, "✓" if rr == r0 else "**✗**"))
        # 存 JSON
        w = {"n": n, "p": p, "A": [[str(x) for x in r] for r in Ac],
             "C": [[str(x) for x in r] for r in Cc],
             "L0": [[str(x) for x in r] for r in L0],
             "q0": q0, "d_CA": v["d_CA"], "rankH": v["rankH"],
             "checks": {k: bool(v[k]) for k in
                        ["H1_rankC","H2_rankL0","H3_rankL0C","H4_funobs","5a",
                         "5b_atsampled","caseII","parallel","nonDegenerate","T5a"]}}
        with open(os.path.join(_HERE, "witness_caseII_parallel_YES.json"), "w",
                  encoding="utf-8") as f:
            json.dump(w, f, ensure_ascii=False, indent=1)
        print("\n已存 witness_caseII_parallel_YES.json")
        return
    print("未找到")


if __name__ == "__main__":
    main()
