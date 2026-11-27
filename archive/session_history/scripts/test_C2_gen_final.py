# -*- coding: utf-8 -*-
"""
B-1 最终版：(C2) 的 k=2 检验 —— 用生成器 L0 = C·A^m 直接造实例

形状：n=5, p=1, r=1 ⟹ 需 η1=3 ⟹ q0=3, k=2, s=3, dimΘ=2
      d_CA = 5 − rank[C;CA] = 5 − 2 = 3 = q0  （方阵！）
      {rank H < q0} = {det H = 0} 是二次曲线（定理 D1：次数 ≤ k = 2）

在曲线上取**有理点**（精确算术），逐点检验 rankH<q0、(A)、(S)。
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_C2_conic_sq.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(90090009)")[0]
exec(head)

g2 = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\gen_check_eta.py",
          encoding="utf-8").read()
ghead = g2.split("MPOW = None")[0]
exec(ghead)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


rng = random.Random(11235813)
print("(C2) 的 k=2 检验 —— 生成器 L0 = C·A^m 版（n=5,p=1,r=1,q0=3,d_CA=3）")
print()
print(f"{'#':>2} {'m':>2} {'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} {'dCA':>4} | "
      f"{'有理点':>7} {'rankH<q0':>9} {'(A)':>5} {'(S)成':>6} {'(S)败':>6} {'结论':>8}")
print("-" * 100)
n_inst = 0; yes = 0; bad = 0; noA = 0; tried = 0
while n_inst < 3 and tried < 200:
    tried += 1
    m = 2
    n, p, r = 5, 1, 1
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    Lc = mm(Cc, matpow(Ac, m))
    if rk(Lc) != r: continue
    if rk(Lc + Cc) != r + p: continue
    if rk(Cc + mm(Cc, Ac)) != 2: continue
    Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
    if rk(Z + OC) != rk(OC): continue
    try:
        Lx, eta = p1(Ac, Cc, Lc)
    except Exception:
        continue
    if not condA(Ac, Cc, Lx): continue
    q0 = sum(eta)
    if q0 != 3: continue
    dC = n - p; s = dC - r; k = q0 - r
    if k != 2 or s != 3: continue
    D = build(Ac, Cc, Lc, Lx)
    print('  [dbg] build -> None? %s' % (D is None))
    if D is None: continue
    print('  [dbg] dCA=%s q0=%s' % (D['dCA'], q0))
    if D['dCA'] != q0: continue
    print('  [debug] 通过前置过滤: q0=%d k=%d s=%d dCA=%d'%(q0,k,s,D['dCA']))
    co = q2_coeffs(D)
    print('  [dbg] dCA=%d q0=%d co=%s'%(D['dCA'], q0, 'None' if co is None else [str(z) for z in co]))
    if co is None: continue
    pts = conic_pts(co, lim=12)
    print('  [dbg] 有理点数=%d'%len(pts))
    if not pts: continue
    nlt = nA = nS = nFail = 0
    for (x, y) in pts[:30]:
        Lred, Hm = exact_H([x, y], D)
        rH = rk(Hm) if (Hm and Hm[0]) else 0
        if rH >= q0: continue
        nlt += 1
        if exact_A([x, y], D):
            nA += 1
            if S_holds(Hm, mm(mm(Lred, Ac), D['NCA'])):
                nS += 1
            else:
                nFail += 1
    n_inst += 1
    if nS >= 1 and nFail == 0: yes += 1; concl = "YES"
    elif nFail > 0: bad += 1; concl = "**NO**"
    else: noA += 1; concl = "无A点"
    print(f"{n_inst:>2} {m:>2} {n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} {D['dCA']:>4} | "
          f"{len(pts):>7} {nlt:>9} {nA:>5} {nS:>6} {nFail:>6} {concl:>8}")

print()
print(f"=== 汇总 ===  YES: {yes}   (S) 失败: {bad}   无 A 点: {noA}   共 {n_inst} 实例（尝试 {tried}）")
print()
print("判读：")
print("  · 全部 YES 且 bad=0 ⟹ (C2) 在 k=2 亦成立（整条曲线上 (S) 成立）")
print("  · bad>0 ⟹ (C2) 被证伪 ⟹ 情形 II 需真正的代数判定")
