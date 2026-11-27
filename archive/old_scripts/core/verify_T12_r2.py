# -*- coding: utf-8 -*-
"""
verify_T12_r2.py -- D8: 定向搜 r>=2 的 T12 实例（用完整判据）

策略：小 n + L0 = C A^m 构造，放宽 seed 范围，先**找到** r>=2 且 k=1 的实例。
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; toF = _ns["toF"]; ker_basis = _ns["ker_basis"]
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
    print("=== D8: 定向搜 r>=2 的 T12 实例 ===\n")
    found = 0
    rng = random.Random(20260101)
    for trial in range(60000):
        if found >= 6: break
        r = 2
        n, p = 5, 1
        mp = rng.randint(1, 2)
        Amat = [[rng.randint(-1, 1) for _ in range(n)] for _ in range(n)]
        Cmat = [[rng.randint(-1, 1) for _ in range(n)] for _ in range(p)]
        Ac, Cc = toF(Amat), toF(Cmat)
        if rk(Cc) != p: continue
        Lc = mm(Cc, matpow(Ac, mp))
        rr = rk(Lc)
        if rr != r: continue
        if rk(Lc + Cc) != r + p: continue
        try:
            Lx, eta = p1(Ac, Cc, Lc)
        except Exception:
            continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - r
        if k != 1: continue
        W = Cc + mm(Cc, Ac)
        NCA = ker_basis(W)
        if not NCA or not NCA[0]: continue
        dCA = len(NCA[0])
        L0A = mm(Lc, Ac)

        def pv(v):
            return [sum(v[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
        pL0 = [pv(Lc[i]) for i in range(r)]
        pL0A = [pv(L0A[i]) for i in range(r)]
        pL0_zero = all(all(x == 0 for x in row) for row in pL0)
        rpar = rk(pL0 + pL0A) if not pL0_zero else 1
        par = (rpar <= 1)
        nA = 0; nlt = 0
        for _ in range(300):
            rows = [row[:] for row in Lc]
            for _i in range(k):
                rows.append([F(rng.randint(-4, 4)) for _ in range(n)])
            L = rows
            if rk(mm(L, Ac) + L + W) != rk(L + W): continue
            nA += 1
            if rk(mm(L, NCA)) < q0: nlt += 1
        found += 1
        print(f"[{found}] n={n} p={p} r={r} q0={q0} k={k} d_CA={dCA} | "
              f"rk[piL0;piL0A]={rpar} piL0=0? {pL0_zero} par={par} | "
              f"含(A)={nA} 秩降={nlt} | 断言(不平行⟹秩降=0) "
              f"{'成立' if (par or pL0_zero or nlt == 0) else '✗违背'}")
    print()
    if found == 0:
        print("未找到 r>=2 且 k=1 的实例（该组合很稀有）")
    else:
        print(f"共 {found} 个 r>=2 实例；断言全部成立 ⟹ T12 在 r>=2 下也有效 ✓")


if __name__ == "__main__":
    main()
