# -*- coding: utf-8 -*-
"""
verify_T12_full.py -- D8: 用**完整平行判据**复核 T12（含 r>=2）

【T12】(q0 = r+k, k=1)：若 pi(L0) != 0 且 rank[pi(L0); pi(L0 A)] >= 2（不平行），
        则**不存在**满足 (A) 且 rank(L N_CA) < q0 的 L。
        ⟹ 由 T6，(S) 必失败 ⟹ 判定恒 NO。

【为什么重做】verify_T12.py 用 r=1（此时"第一行"即"全部行"，故判据等价）。
             但项目第 20 处教训指出：r>=2 时"只看第一行"是**错的** ✗
             ⟹ 本脚本对 r>=2 也判定，且严格用全部 r 行的 pi。

【验证】对每个实例：
   · 算 rank[pi(L0); pi(L0 A)]（全部 r 行）
   · 大量采样含 L0 的 q0 行 L
   · 统计 "(A) 成立" 与 "(A) 成立 且 rank(L N_CA) < q0"
   · 断言：不平行 且 pi(L0)!=0 ⟹ 后者恒为 0
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; toF = _ns["toF"]; orb = _ns["orb"]
ker_basis = _ns["ker_basis"]; condA = _ns["condA"]

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
    print("=== D8: T12 的完整判据复核（含 r>=2）===\n")
    print(f"{'#':>3} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} {'rk[piL0;piL0A]':>14} "
          f"{'piL0=0?':>8} | {'含(A)':>6} {'其中秩降':>8} {'符合?':>6}")
    print("-" * 84)
    rng = random.Random(778899)
    shown = 0; bad = 0; tested = 0; n_r2 = 0
    for t in range(400000):
        if shown >= 12: break
        # 定向：优先找 r=2（前 200 个样本中 r=2 不足时强制）
        r = 2 if (n_r2 < 6) else (1 if (t % 3) else 2)
        n, p = 6, 1
        Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cmat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Ac, Cc = toF(Amat), toF(Cmat)
        if rk(Cc) != p: continue
        mp = rng.randint(1, 3)
        Lc = mm(Cc, matpow(Ac, mp))
        if rk(Lc) != r: continue
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
        # **完整** pi 判据：全部 r 行
        def pv(v):
            return [sum(v[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
        pL0 = [pv(Lc[i]) for i in range(r)]
        pL0A = [pv(L0A[i]) for i in range(r)]
        pL0_zero = all(all(x == 0 for x in row) for row in pL0)
        rpar = rk(pL0 + pL0A) if not pL0_zero else 1
        par = (rpar <= 1)
        # 采样
        nA = 0; nlt = 0
        for _ in range(300):
            rows = [row[:] for row in Lc]
            for _i in range(k):
                rows.append([F(rng.randint(-4, 4)) for _ in range(n)])
            L = rows
            if rk(mm(L, Ac) + L + W) != rk(L + W):
                continue
            nA += 1
            H = mm(L, NCA)
            if rk(H) < q0:
                nlt += 1
        tested += 1
        if r == 2: n_r2 += 1
        expect_zero = (not par) and (not pL0_zero)
        ok = (not expect_zero) or (nlt == 0)
        if not ok: bad += 1
        shown += 1
        print(f"{shown:>3} {r:>2} {q0:>3} {k:>2} {dCA:>4} {rpar:>14} "
              f"{str(pL0_zero):>8} | {nA:>6} {nlt:>8} {str(ok):>6}")
    print()
    print(f"=== 测试 {tested} 个实例；不符合数：{bad} ===")
    print()
    print("判读：")
    print("  · 全部符合 ⟹ T12 在 r>=2 下也成立（用**完整**判据）")
    print("  · 出现不符合 ⟹ T12 需撤回或限定到 r=1")


if __name__ == "__main__":
    main()
