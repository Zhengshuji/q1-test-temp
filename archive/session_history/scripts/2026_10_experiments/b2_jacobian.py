# -*- coding: utf-8 -*-
"""
b2_jacobian.py —— 引理 A 的显式结构验证

【推导出的结构】
  M(Θ) := [W(Θ); B; W(Θ)Ā]，W(Θ) = W(0) + V(Θ)（V 线性）
  子式 I_α(Θ) = det M(Θ)[rows, cols]，其线性部分 = Σ_a Θ_a · ∂I_α/∂Θ_a

  ∂I_α/∂Θ_a = 把 W(Θ) 的**可变行**换成 ∂V/∂Θ_a 那一行后，其余不变的行列式
             （行列式对某一行的多重线性）

  ⟹ 系数向量 = 由 {q_i} ∪ {q_i Ā} ∪ {v̇_a} ∪ {v̇_a Ā} 的**子式**组成
      （这里 q_i 取自 [W(0);B] 的行，v̇_a = ∂V/∂Θ_a）

【本脚本验证】
  ① 把 ∂I_α/∂Θ_a 用"替换一行后的行列式"**直接算出**，与 Poly 系数**逐项对比**
  ② 报告矩阵 K := [ [W(0);B] ; [W(0);B]Ā ; {v̇_a} ; {v̇_a Ā} ] 的秩
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


def main():
    print("=== 引理 A 的显式结构：系数 = 替换一行后的行列式 ===")
    for ss, n in [(3, 5), (4, 6)]:
        inst = get_instance(n, ss, 20360000 + ss)
        if inst is None: continue
        dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
        r, k = 1, 1; m = s - 1
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
        # M(0) 与 ∂M/∂Θ_a
        zsub = {v: 0 for v in th}
        M0 = [[sp.simplify(e.subs(zsub)) for e in row] for row in MBs]
        # 可变行在 MBs 中的位置：W 的最后一行 (index r+k-1) 与 WAs 的最后一行
        var_rows = [r + k - 1, len(W) + len(BATs) + r + k - 1]
        dM = []   # dM[a] = ∂M/∂Θ_a（只有可变行非零）
        for a in range(m):
            M_a = [[sp.Integer(0)] * nc for _ in range(nr)]
            for vr in var_rows:
                for j in range(nc):
                    M_a[vr][j] = sp.simplify(sp.diff(MBs[vr][j], th[a]))
            dM.append(M_a)
        # 验证：∂I/∂Θ_a 是否等于"替换一行"的行列式
        ok_cnt = 0; tot_cnt = 0
        polys = []
        for ri in itertools.combinations(range(nr), rho + 1):
            for cj in itertools.combinations(range(nc), rho + 1):
                d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
                if d != 0: polys.append((ri, cj, d))
        for (ri, cj, d) in polys:
            if sp.Poly(d, *th).total_degree() > 1: continue
            crow = [sp.nsimplify(sp.Poly(d, *th).coeff_monomial(v)) for v in th]
            # 直接由"替换一行"重算系数
            crow2 = []
            for a in range(m):
                val = sp.Integer(0)
                for pos, i in enumerate(ri):
                    sub_m = []
                    for q in range(len(ri)):
                        if q == pos:
                            sub_m.append([sp.nsimplify(dM[a][ri[q]][cj[t]]) for t in range(len(cj))])
                        else:
                            sub_m.append([sp.nsimplify(MBs[ri[q]][cj[t]]) for t in range(len(cj))])
                    val += sp.expand(sp.Matrix(sub_m).det())
                crow2.append(sp.nsimplify(val))
            tot_cnt += 1
            if crow == crow2: ok_cnt += 1
            else:
                print("   ⚠️ 不一致 rows=%s cols=%s: Poly=%s  替换法=%s" % (ri, cj, crow, crow2))
        print("\n--- (1,%d) : 线性子式 %d 个，'Poly系数 == 替换一行行列式' 一致 %d/%d ---"
              % (ss, tot_cnt, ok_cnt, tot_cnt))
        # 矩阵 K 的秩
        K = [[sp.simplify(e) for e in row] for row in WBs]
        K = K + [[sp.simplify(sum(WBs[i][a] * ATs[a][j] for a in range(len(ATs))))
                  for j in range(dC)] for i in range(len(WBs))]
        for a in range(m):
            K = K + [[dM[a][vr][j] for j in range(nc)] for vr in var_rows]
        print("   K := [[W(0);B]; [W(0);B]Ā; {v̇_a}] 的形状 %d×%d，秩 = %s"
              % (len(K), len(K[0]), sp.Matrix(K).rank()))
    print("\n【说明】K 的秩反映一阶信息能提供多少独立约束")


if __name__ == "__main__":
    main()
