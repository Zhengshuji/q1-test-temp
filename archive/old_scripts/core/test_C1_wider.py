# -*- coding: utf-8 -*-
"""
推广检验猜想 (C1)：情形 II（d_CA >= q0）中是否**恒存在** (A)∧(S)∧rank H < q0 的点？
（即 ν_min = q0 恒为 YES）

形状不锁定，dimTheta <= 2，多起点优化找 {rank H < q0} 上的点，再精确检验 (A) 与 (S)。
"""
import itertools
import random
from fractions import Fraction as F

import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_caseII_YES.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(11223344)")[0]
exec(head)


rng = random.Random(99887766)
print("推广检验猜想 (C1)：情形 II 中 ν_min = q0 是否恒为 YES")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'dCA':>4} {'dimT':>4} | "
      f"{'找到rankH<q0':>12} {'(A)∧(S)':>9} {'结论':>16}")
print("-" * 78)
n_inst = 0
yes = 0
no = 0
for trial in range(200000):
    if n_inst >= 14:
        break
    n = rng.randint(3, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    for _ in range(30):
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
        dC = n - p; s = dC - r; k = q0 - r
        if k < 1 or k > s or k * (s - k) > 2: continue
        if 2 * p + q0 < n: continue
        D = build(Ac, Cc, Lc, Lx)
        if D is None: continue
        if not (D['dCA'] >= q0): continue
        dim = k * (s - k)
        best = (float('inf'), None)
        for _s2 in range(500):
            x = np.random.randn(dim) * 2.0
            for _it in range(400):
                f = q0minors(x, D)
                if f.size == 0:
                    break
                val = float(f @ f)
                if val < 1e-26: break
                J = np.zeros((f.size, dim)); h = 1e-6
                for a in range(dim):
                    xp = x.copy(); xp[a] += h
                    J[:, a] = (q0minors(xp, D) - f) / h
                try:
                    step = np.linalg.lstsq(J, f, rcond=None)[0]
                except Exception:
                    break
                x = x - 0.7 * step
            v = float(q0minors(x, D) @ q0minors(x, D))
            if v < best[0]:
                best = (v, x.copy())
        gotA = gotS = False
        found_lt = False
        if best[1] is not None and best[0] < 1e-18:
            tf = [F(v).limit_denominator(10 ** 6) for v in best[1]]
            Lred, Hm = exact_H(tf, D)
            rH = rk(Hm) if (Hm and Hm[0]) else 0
            if rH < q0:
                found_lt = True
                gotA = exact_A(tf, D)
                if gotA:
                    gotS = S_holds(Hm, mm(mm(Lred, Ac), D['NCA']))
        n_inst += 1
        ok = (found_lt and gotA and gotS)
        if ok: yes += 1
        else: no += 1
        print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {D['dCA']:>4} {dim:>4} | "
              f"{str(found_lt):>12} {str(gotS):>9} "
              f"{('YES' if ok else '未找到'):>16}")
        break

print()
print(f"=== 汇总 ===  好点找到：{yes} / {n_inst}   未找到：{no}")
print()
print("判读：")
print("  · 若几乎全部 YES ⟹ 支持猜想 (C1)：情形 II 中 ν_min = q0 恒成立 ⟹ 该情形可判定（甚至平凡）")
print("  · 若出现『未找到』⟹ 需区分是优化器失败还是真的好点不存在（应改用精确消元）")
