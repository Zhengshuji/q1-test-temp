# -*- coding: utf-8 -*-
"""
mainline_B2.py —— 主线：**支 B（2p+q0 < n）上 (A)∧(S) 能否成立？**

【流水线（全部复用项目已验证的部件）】
  1. 造支 B 实例：L0 用 CA^m 生成器（随机 L0 几乎总给 eta=1，项目已记录）
  2. 对候选 ℓ（Λ 的后 k 列，枚举小整数矩阵）：
       gen_A_system.build_general ⟹ 线性系统 ⟹ 解出 L = [L0; R]
  3. 检验 (A)（原坐标）⟹ 得 (A)-点
  4. 对每个 (A)-点：solve_Lambda 求 Λ，S_holds 检验 (S)
  5. 报告：找到 (A)∧(S) 见证的实例数

【判读】
  · 找到见证 ⟹ 支 B 可为 YES ⟹ 支 B 是硬度候选（**强结论**）
  · 全空 ⟹ 支 B（数值上）无 (A)∧(S) ⟹ 支持"支 B 非硬度源"
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
p1 = _t["p1"]; build_norm_T = _t["build_norm_T"]

_b = {"__file__": os.path.join(_HERE, "batch_c6p_k.py"), "__name__": "b"}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    srcb = fh.read()
head = srcb.split("def main(")[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(head, "b", "exec"), _b)
solve_Lambda = _b["solve_Lambda"]; S_holds = _b["S_holds"]

_g = {"__file__": os.path.join(_HERE, "gen_A_system.py"), "__name__": "g"}
with open(os.path.join(_HERE, "gen_A_system.py"), encoding="utf-8") as fh:
    srcg = fh.read()
headg = srcg.split("def main(")[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(headg, "g", "exec"), _g)
build_general = _g["build_general"]


def mul(X, Y):
    return [[sum(X[i][a] * Y[a][j] for a in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def checkA_norm(Ac, Cc, L):
    """原坐标 (A)：rank[L;B;LA] == rank[L;B]，B = ker[C;CA]"""
    W = Cc + mm(Cc, Ac)
    B = ker_basis(W)
    if not B or not B[0]: return False
    P = mm(L, B); PA = mm(mm(L, Ac), B)
    return rk(P + PA) == rk(P)


def make_inst(n, p, r, mpow, seed, tries=3000):
    """L0 = C A^mpow 造实例；要求支 B"""
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


def main():
    print("=== 支 B：(A)∧(S) 能否成立？（复用项目流水线）===\n")
    shapes = [(6,1,1,2), (7,1,1,2), (8,1,1,3), (7,2,1,2), (8,2,1,2), (9,1,1,4)]
    tot_inst = tot_A = tot_S = 0
    for (n, p, r, mp) in shapes:
        inst = None
        for seed in range(8):
            inst = make_inst(n, p, r, mp, 20700000 + 1000*mp + 100*seed + n)
            if inst: break
        if not inst:
            print("(n=%d,p=%d,r=%d,CA^%d) 未找到支 B 实例" % (n, p, r, mp)); continue
        Ac, Cc, Lc = inst['Ac'], inst['Cc'], inst['Lc']
        q0, k, r_, n_ = inst['q0'], inst['k'], inst['r'], inst['n']
        print("实例 n=%d p=%d r=%d L0=CA^%d : q0=%d k=%d  支B ✓ (2p+q0=%d < n=%d)"
              % (n, p, r_, mp, q0, k, 2*p+q0, n_))
        tot_inst += 1
        # 枚举 ℓ（q0×k，小整数）
        vals = [-1, 0, 1]
        n_l = 0; n_A = 0; n_S = 0
        for combo in itertools.product(vals, repeat=q0*k):
            if all(v == 0 for v in combo): continue
            ell = [[F(combo[i*k + j]) for j in range(k)] for i in range(q0)]
            try:
                rows, rhs, nv, meta = build_general(Ac, Cc, Lc, ell)
            except Exception:
                continue
            res = _ns["solve"](rows, rhs)
            if res is None: continue
            y, nsol = res
            sols = [y] + list(nsol)
            for sol in sols[:4]:
                if len(sol) != nv: continue
                R = [[sol[a*n_ + j] for j in range(n_)] for a in range(k)]
                L = Lc + R
                if len(L) != q0: continue
                n_l += 1
                if not checkA_norm(Ac, Cc, L): continue
                n_A += 1
                # (S) 检验
                Wc = Cc + mm(Cc, Ac); N = ker_basis(Wc)
                if not N or not N[0]: continue
                H = mm(L, N)
                if rk(H) == 0: continue
                found = False
                for Lam in solve_Lambda(Ac, Cc, L):
                    if S_holds(Lam, H): found = True; break
                if found:
                    n_S += 1
                    if n_S == 1:
                        print("   ★★★ 找到 (A)∧(S) 见证！ℓ=%s" % [[str(x) for x in row] for row in ell])
                        print("       L = %s" % [[str(x) for x in row] for row in L])
            if n_S >= 3: break
        tot_A += n_A; tot_S += n_S
        print("   ℓ 尝试 %d ；(A)-点 %d ；(S) 成立 %d" % (n_l, n_A, n_S))
        print()
    print("=== 汇总 ===")
    print("支 B 实例 %d ；(A)-点 %d ；(A)∧(S) 成立 %d" % (tot_inst, tot_A, tot_S))
    if tot_A and tot_S == 0:
        print("⟹ 支 B 上 (A)∧(S) **未找到见证** ⟹（数值上）支持'支 B 无解'")
    elif tot_S:
        print("⟹ **支 B 可为 YES** ⟹ 支 B 是硬度候选（需进一步确认）✓✓")


if __name__ == "__main__":
    main()
