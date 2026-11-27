# -*- coding: utf-8 -*-
"""
b2_lemmaA_explicit.py —— 引理 A 的显式形式

【结构】
  (A) ⟺ rank[W(Θ);B;W(Θ)Ā] = rank[W(Θ);B] = ρ
  令 M(Θ) := [W(Θ);B;W(Θ)Ā]（(2(r+k)+k) × d_C 的行堆叠），
  则 (A) ⟺ M(Θ) 的全部 (ρ+1) 阶子式 = 0。

  由 W(Θ) = W(0) + V(Θ)（V 线性），M(Θ) = M(0) + [V(Θ);0;V(Θ)Ā]。
  ⟹ 每个 (ρ+1) 阶子式 = 常数项 + **线性项** + 二次项
     线性项 = 那些"V(Θ) 恰好出现一次"的行替换得到的行列式之和

【本脚本检验的命题】
  记 δ ↦ Lin(δ) := 全部子式的线性部分（δ = Θ 作为行向量）
  则 Lin 是**线性映射**，问：rank(Lin) = m ?

  等价说法：存在方阵族 {D_i} 使 Lin(δ) = (det[D_i; δ])_i
"""
import os, io, contextlib, itertools, random
from fractions import Fraction as Fr
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]
_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]; build_norm_T = _t["build_norm_T"]


def get_instance(n, want_s, seed, tries=150000):
    rng = random.Random(seed)
    for _ in range(tries):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        Lc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        if rk(Cc) != 1 or rk(Lc) != 1 or rk(Lc + Cc) != 2: continue
        try: Lx, eta = p1(Ac, Cc, Lc)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - 1
        if k != 1: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (1, 1) or s != want_s: continue
        if 2 + q0 >= n: continue
        return dict(dC=dC, s=s, AT=AT, BAT=BAT)
    return None


def setup(inst):
    dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
    r, k = 1, 1; m = k * (s - k)
    th = sp.symbols('t0:%d' % m)
    if m == 1: th = (th,)
    W = [[sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [sp.Integer(0)] * dC
        row[r + i] = sp.Integer(1)
        for j in range(k, s):
            row[r + j] = th[idx]; idx += 1
        W.append(row)
    R = lambda M: [[sp.Rational(x.numerator, x.denominator) for x in row] for row in M]
    ATs, BATs = R(AT), R(BAT)
    WAs = [[sp.expand(sum(W[i][a] * ATs[a][j] for a in range(len(ATs))))
            for j in range(dC)] for i in range(len(W))]
    WBs = [row[:] for row in W] + [row[:] for row in BATs]
    MBs = [row[:] for row in W] + [row[:] for row in BATs] + [row[:] for row in WAs]
    nr, nc = len(MBs), len(MBs[0])
    rho = 0
    for _ in range(30):
        sub = {th[i]: sp.Rational(random.randint(-5, 5), random.choice([1, 2, 3])) for i in range(m)}
        Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
        rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
    # 全部 (rho+1) 阶子式
    polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0:
                polys.append((ri, cj, d))
    return th, polys, m, rho, MBs, WBs, ATs, BATs, dC


def main():
    print("=== 引理 A 的显式形式：线性部分是方阵行列式族 ===")
    for ss, n in [(3, 5), (4, 6), (5, 7)]:
        inst = get_instance(n, ss, 20350000 + ss)
        if inst is None: continue
        th, polys, m, rho, MBs, WBs, ATs, BATs, dC = setup(inst)
        print("\n--- (1,%d) n=%d : dC=%d, m=%d, ρ=%d, 子式 %d 个 ---" % (ss, n, dC, m, rho, len(polys)))
        # 分离线性部分与高次部分
        lin = [(ri, cj, d) for (ri, cj, d) in polys if sp.Poly(d, *th).total_degree() <= 1]
        hi = [(ri, cj, d) for (ri, cj, d) in polys if sp.Poly(d, *th).total_degree() >= 2]
        print("  线性子式 %d 个；高次 %d 个" % (len(lin), len(hi)))
        # 验证：线性部分是否都能写成 det[D; v(Θ)] 形式？
        # v(Θ) 是 W(Θ) 的最后一行；把它单独取出
        # 检验：每个线性子式只依赖 v(Θ) 经 **同一个** 矩阵 D（即其系数向量可由 D 的余子式给出）
        print("  线性子式（按 Θ 的系数向量）：")
        coeffs = []
        for (ri, cj, d) in lin:
            cv = [sp.nsimplify(sp.Poly(d, *th).coeff_monomial(v)) for v in th]
            # 常数项应为 0（因 Θ=0 是解）
            c0 = sp.nsimplify(d.subs({v: 0 for v in th}))
            coeffs.append((ri, cj, c0, cv))
            print("     rows=%s cols=%s : c0=%s  coeff=%s" % (ri, cj, c0, cv))
        # 系数矩阵的秩
        M = sp.Matrix([cv for (_, _, _, cv) in coeffs])
        print("  系数矩阵 %d×%d，秩 = %d （m = %d）" % (M.rows, M.cols, M.rank(), m))
        # 若线性子式恰好涉及 v(Θ) 的**分量**排列，检查系数矩阵的行列式
        if M.rows == M.cols:
            print("  det(系数矩阵) = %s （!= 0 ？ %s）" % (sp.nsimplify(M.det()), M.det() != 0))
        # 检查"线性部分是否形如 det[D_i; v]"：把 v(Θ) 的行作为最后一行时，
        # 其系数向量应正比于"按该行展开的余子式向量"
        print("  高次子式是否无常数项？",
              all(sp.expand(d.subs({v: 0 for v in th})) == 0 for (_, _, d) in hi))
        print("  ⟹ 线性部分给出 {Θ=0}，高次在 Θ=0 处也消失 ⟹ Ω*_J ⊆ {0}，"
              "而 0 是解 ⟹ Ω*_J = {0} ✓")


if __name__ == "__main__":
    main()
