# -*- coding: utf-8 -*-
"""
(C2) 的 k>=2 检验（锁定形状，搜索快）

形状：n=5, p=1, r=1, q0=3  ⟹  k = q0−r = 2,  s = dC−r = 3,  dimΘ = k(s−k) = 2
     且 p=1 ⟹ rank[C;CA] ≤ 2 ⟹ d_CA = 5 − rank[C;CA] ≥ 3 = q0  ⟹ **情形 II**
     且 2p+q0 = 5 ≥ 5 = n ⟹ 也在分支 A 内

检验：在 {rank H < q0} 上取点，精确检验 (A) 与 (S)。
  · 若 (S) 全部成立 ⟹ 支持 (C2)
  · 若出现 (S) 失败 ⟹ (C2) 被证伪
"""
import itertools
import random
from fractions import Fraction as F
import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_C2_kge2.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(77777777)")[0]
exec(head)


rng = random.Random(31313131)
print("(C2) 的 k>=2 检验（n=5,p=1,r=1,q0=3 ⟹ k=2, d_CA>=q0=3, 情形 II）")
print()
print(f"{'#':>2} {'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} {'dCA':>4} {'dimT':>4} | "
      f"{'找到rankH<q0':>12} {'(A)∧(S)':>9} {'结论':>10}")
print("-" * 92)
n_inst = 0
yes = 0
no = 0
unfound = 0
for trial in range(400000):
    if n_inst >= 12:
        break
    n, p, r = 5, 1, 1
    for _ in range(60):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
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
        if D is None: continue
        if not (D['dCA'] >= q0): continue
        dim = k * (s - k)
        # 多起点优化（dim=2，多起点）
        best = (float('inf'), None)
        for _s2 in range(1500):
            x = np.random.randn(dim) * 2.5
            for _it in range(400):
                f = q0minors(x, D)
                if f.size == 0: break
                val = float(f @ f)
                if val < 1e-28: break
                J = np.zeros((f.size, dim)); h = 1e-6
                for a in range(dim):
                    xp = x.copy(); xp[a] += h
                    J[:, a] = (q0minors(xp, D) - f) / h
                try:
                    step = np.linalg.lstsq(J, f, rcond=None)[0]
                except Exception:
                    break
                x = x - 0.7 * step
            try:
                v = float(q0minors(x, D) @ q0minors(x, D))
            except Exception:
                continue
            if v < best[0]:
                best = (v, x.copy())
            if best[0] < 1e-26:
                break
        gotA = gotS = False
        found_lt = False
        if best[1] is not None and best[0] < 1e-16:
            tf = [F(v).limit_denominator(10 ** 6) for v in best[1]]
            # 也可能需要微调：试几个附近的有理点
            tried = [tf]
            for _q in range(30):
                t2 = [c + F(rng.randint(-3, 3), rng.randint(10, 300)) for c in tf]
                tried.append(t2)
            for t2 in tried:
                Lred, Hm = exact_H(t2, D)
                rH = rk(Hm) if (Hm and Hm[0]) else 0
                if rH >= q0: continue
                found_lt = True
                gotA = exact_A(t2, D)
                if gotA:
                    gotS = S_holds(Hm, mm(mm(Lred, Ac), D['NCA']))
                break
        n_inst += 1
        if found_lt and gotA and gotS:
            yes += 1; concl = "YES"
        elif found_lt:
            no += 1; concl = "**NO**"
        else:
            unfound += 1; concl = "未找到"
        print(f"{n_inst:>2} {n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} {D['dCA']:>4} {dim:>4} | "
              f"{str(found_lt):>12} {str(gotS) if found_lt else '-':>9} {concl:>10}")
        break

print()
print(f"=== 汇总 ===  YES: {yes}    found 但 (S) 失败: {no}    未找到退化点: {unfound}")
print()
print("判读：")
print("  · 全部 YES ⟹ (C2) 在 k=2 亦成立 ⟹ (C1)/(C2) 证据链基本完备")
print("  · 出现 NO   ⟹ (C2) 被证伪 ⟹ 情形 II 需真正的代数判定（那本身是重要结论）")
