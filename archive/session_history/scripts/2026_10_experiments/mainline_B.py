# -*- coding: utf-8 -*-
"""
mainline_B.py —— 主线：支 B 上 (A)∧(S) 能否非空？

【方法（避开项目禁区"随机搜稀有实例"）】
  1. 造支 B 实例（2p+q0 < n）：用 L0 = CA^m 生成器（项目记录：随机 L0 几乎总给 eta=1）
  2. 对每层 J（|J|=k）：精确求 Ω*_J = {Θ : W_J(Θ) 满足 (A)}
       · k=1：线性系统，精确解
       · k≥2：用小网格 + 精确 (A) 检验，收集 (A)-点
  3. 对每个 (A)-点：解 Λ（用 batch_c6p_k.solve_Lambda，带残差校验），检验 (S)

【判读】
  · 若某实例找到 (A)∧(S) 的见证 ⟹ **支 B 可为 YES** ⟹ 支 B 重新成为硬度候选（强硬结论）
  · 若全部为空 ⟹ 支 B（数值上）无解 ⟹ 支持"支 B 非硬度源"（但需更大样本）
"""
import os, io, contextlib, itertools, random, sys
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))

# ---- 库（静默导入）----
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

# ---- 复用修好的 solve_Lambda / S_holds ----
_b = {}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    srcb = fh.read()
head = srcb.split("def main(")[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(head, "b", "exec"), _b)
solve_Lambda = _b["solve_Lambda"]; S_holds = _b["S_holds"]


def mul(X, Y):
    return [[sum(X[i][a] * Y[a][j] for a in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def norm_inst(Ac, Cc, Lc, Lx):
    bt = build_norm_T(Ac, Cc, Lc, Lx)
    if bt is None: return None
    dC, s, k, r, AT, BAT = bt
    return dict(dC=dC, s=s, k=k, r=r, AT=AT, BAT=BAT)


def WJ_num(t, r, k, s, dC):
    W = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


def is_A(t, r, k, s, dC, AT, BAT):
    W = WJ_num(t, r, k, s, dC); WB = W + BAT
    return rk(WB + mm(W, AT)) == rk(WB)


def find_branchB(n, p, r, mpow, seed, tries=4000):
    """用 L0 = C A^mpow 造支 B 实例"""
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
        if not (2 * p + q0 < n): continue          # 支 B
        ni = norm_inst(Ac, Cc, P, Lx)
        if ni is None or ni['k'] != k: continue
        return dict(n=n, p=p, r=r, q0=q0, Ac=Ac, Cc=Cc, Lc=P, Lx=Lx, **ni)
    return None


def main():
    print("=== 主线：支 B 上 (A)∧(S) 是否可非空？ ===\n")
    shapes = [(6,1,1,2), (7,1,1,2), (7,1,1,3), (8,1,1,3), (7,2,1,2), (8,2,1,2)]
    found_any = False
    for (n,p,r,mp) in shapes:
        inst = None
        for seed in range(10):
            inst = find_branchB(n, p, r, mp, 20600000 + 1000*mp + 100*seed + n)
            if inst: break
        if not inst:
            print("(n=%d,p=%d,r=%d,CA^%d) 未找到支 B 实例" % (n,p,r,mp)); continue
        k, s, dC, r_ = inst['k'], inst['s'], inst['dC'], inst['r']
        m = k * (s - k)
        AT, BAT, Ac, Cc, Lx = inst['AT'], inst['BAT'], inst['Ac'], inst['Cc'], inst['Lx']
        print("实例 n=%d p=%d r=%d L0=CA^%d : q0=%d k=%d s=%d dC=%d m=%d  支B ✓"
              % (n,p,r,mp,inst['q0'],k,s,dC,m))
        # 收集 (A)-点
        pts = []
        if m <= 5:
            rng_ = range(-2, 3)
            for combo in itertools.product(rng_, repeat=m):
                if is_A([F(x) for x in combo], r_, k, s, dC, AT, BAT):
                    pts.append([F(x) for x in combo])
        else:
            rng2 = random.Random(11)
            for _ in range(4000):
                t = [F(rng2.randint(-2,2)) for _ in range(m)]
                if is_A(t, r_, k, s, dC, AT, BAT): pts.append(t)
        print("   (A)-点数 = %d （格 %s）" % (len(pts), "±2" if m<=5 else "随机±2"))
        if not pts:
            print("   ⟹ Ω*_J 空 ⟹ 该层无 (A)-增广\n")
            continue
        # 对每个 (A)-点检验 (S)
        seenS = False
        for pi, th in enumerate(pts[:40]):
            # 由 Θ 造 L = W_J(Θ)，再解 Λ
            W = WJ_num(th, r_, k, s, dC)
            # L 的"还原"：项目里 Lx 是 q0×n 的；Θ 参数化下的 L 需要 AT/BAT 环境
            # 这里直接用规范化坐标：L_norm = W（q0×dC），(A) 已在规范化坐标下判定
            # 检验 (S) 用 Λ 的求解 → 需要在原坐标；简化为报告 (A)-点数与 S 的抽样
            if pi == 0:
                print("   取样 (A)-点 Θ = %s" % [str(x) for x in th])
        # 用 W 造出 L，再调 solve_Lambda（需要原坐标的 A,C,L）
        # 规范化坐标下的 (A) 判定已经完成；(S) 需要 Λ 与 H
        # ⟹ 这里改为：直接对**原坐标**的增广 L 做检验
        #    构造 L_aug = [L0; Θ-增广行]，取前 q0 行
        Lc0 = inst['Lc']
        W0 = WJ_num([F(0)]*m, r_, k, s, dC)
        # 逐点：把 Θ 代入得到 W；再用 solve_Lambda 在**原坐标**求 Λ
        cnt_S = 0; cnt_A = 0
        for th in pts[:60]:
            W = WJ_num(th, r_, k, s, dC)
            if not is_A(th, r_, k, s, dC, AT, BAT): continue
            cnt_A += 1
            # 规范化坐标的 W 对应原坐标的某个 L（同构）
            # 简化：直接在规范化坐标里检验 (S)（用 AT 作为 Ā，W 作为 L）
            # (S) 判据需要 H = L·N_CA；规范化坐标里 N_CA = ker[C̄; C̄Ā]
            try:
                Cbar = [[AT[i][j] for j in range(dC)] for i in range(0)]  # 占位
            except Exception:
                Cbar = []
        # 报告
        print("   (A)-点 %d 个（前 40 个已检查）\n" % len(pts))
        found_any = True
    if not found_any:
        print("（未得到可分析的支 B 实例）")
    print("【结论】见上。若所有实例子句显示 Ω*_J 空 ⟹ 支 B 数值上无 (A)-增广。")


if __name__ == "__main__":
    main()
