r"""
c20_diff_invariants.py -- ⭐⭐⭐⭐ 对比 Type II 与 Type I 实例的细不变量

【思路】前面测过的 (q0,d,m,ρ0) 全都相同 ⟹ 需要**更细**的代数不变量
【测】
  · rank(AN), dim(row N ∩ row AN), rank[N;AN]
  · 基础铅笔的"特征值集合"：s ∈ {-5..5} 使 rank(s·H0 − F0) < rank(H0)
  · 广铅笔的"特征值"：s 使 row(N) ⊄ row(sN − AN)
  · M 的基 B 的具体结构
"""
import os
import io
import contextlib
import random
import itertools
import time
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    _src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]


def invariants(A, Cc, L0, N, d, tag):
    n = len(A)
    AN = mm(A, N)
    Mcol = [N[i][:] + AN[i][:] for i in range(n)]
    m = rk(Mcol)
    rN = rk(N); rAN = rk(AN)
    Mrow = [r[:] for r in N] + [r[:] for r in AN]
    rRow = rk(Mrow)
    # dim(row N ∩ row AN) = rN + rAN − rRow
    inter = rN + rAN - rRow
    H0 = mm(L0, N); F0 = mm(mm(L0, A), N)
    rho0 = rk(H0)
    # 基础铅笔的"特征值"（s ∈ {-3..3}）
    base_eigs = []
    for s in range(-3, 4):
        P = [[Fr(s) * H0[i][j] - F0[i][j] for j in range(d)] for i in range(len(H0))]
        if rk(P) < rho0:
            base_eigs.append(s)
    # 广铅笔：s 使 row(N) ⊄ row(sN − AN)
    wide = []
    for s in range(-3, 4):
        P = [[Fr(s) * N[i][j] - AN[i][j] for j in range(d)] for i in range(n)]
        Prow = [r[:] for r in P] + [r[:] for r in N]
        if rk(Prow) > rk(P):
            wide.append(s)
    print("  %-8s d=%d m=%d rN=%d rAN=%d inter=%d rRow=%d ρ0=%d" %
          (tag, d, m, rN, rAN, inter, rRow, rho0))
    print("           基础铅笔特征值(s∈[-3,3]) = %s ; 广铅笔 = %s" %
          (base_eigs if base_eigs else "无", wide if wide else "无"))
    return dict(m=m, inter=inter, rRow=rRow, rho0=rho0,
                be=tuple(base_eigs), wide=tuple(wide))


def main():
    n = 5
    rng = random.Random(123455)
    want = {0: "I", 1: "I", 2: "I", 3: "II", 4: "II", 5: "I"}
    print("=== Type I vs Type II 的细不变量（n=5，种子 123455）===\n")
    out = {}
    for trial in range(80000):
        A = [[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc) != 1: continue
        CA = mm(Cc, A)
        if rk(CA) != 1: continue
        W = Cc + CA
        N = ker_basis(W)
        if not N or not N[0]: continue
        d = len(N[0])
        L0 = None
        for _x in range(40):
            cand = [[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand) != 1: continue
            if rk(cand + Cc) != 2: continue
            pv = [sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(len(N[0]))]
            if all(x == 0 for x in pv): continue
            L0 = cand; break
        if L0 is None: continue
        if rk(L0 + Cc) != 2: continue
        try:
            _Lx, eta = p1(A, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        if trial in want:
            tag = "%s(tr%d)" % (want[trial], trial)
            out[trial] = invariants(A, Cc, L0, N, d, tag)
            print()
        if len(out) >= len(want):
            break
    print("=" * 62)
    print("【对比】")
    for lab in ["I", "II"]:
        sel = [v for t, v in out.items() if want[t] == lab]
        if not sel: continue
        print("  Type %s: be=%s wide=%s" %
              (lab, sorted(set(x for v in sel for x in v["be"])),
               sorted(set(x for v in sel for x in v["wide"]))))
    print()
    print("  若 Type I 与 II 的 be / wide 有系统差异 ⟹ 找到判据")


if __name__ == "__main__":
    main()
