# -*- coding: utf-8 -*-
"""
检验 (C2) 在 k >= 2 时是否仍成立：
  情形 II（d_CA >= q0）中，{rank H < q0} 上的点是否也满足 (A)∧(S)？

同时检验猜想 (C1)：该集合非空时是否总能找到好点。
"""
import itertools
import random
from fractions import Fraction as F

import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_caseII_YES.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(11223344)")[0]
exec(head)


def find_degenerate(D, dim, nstarts=600):
    """多起点优化找 {rank H < q0} 上的点，返回 (best_val, x)"""
    best = (float('inf'), None)
    for _ in range(nstarts):
        x = np.random.randn(dim) * 2.0
        for _it in range(400):
            f = q0minors(x, D)
            if f.size == 0: break
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
        if best[0] < 1e-24:
            break
    return best


rng = random.Random(77777777)
print("检验 (C2) 在 k >= 2 的情形（情形 II, d_CA >= q0）")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} {'dCA':>4} {'dimT':>4} | "
      f"{'min':>10} {'rankH<q0':>9} {'(A)':>5} {'(S)':>5} {'结论':>10}")
print("-" * 96)
n_inst = 0
yes = 0
no = 0
for trial in range(120000):
    if n_inst >= 10:
        break
    n = rng.randint(4, 7)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    for _ in range(20):
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
        if k < 2 or k > s: continue
        dim = k * (s - k)
        if dim > 3: continue
        D = build(Ac, Cc, Lc, Lx)
        if D is None: continue
        if not (D['dCA'] >= q0): continue
        best = find_degenerate(D, dim, nstarts=500)
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
        elif found_lt: no += 1
        print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} {D['dCA']:>4} {dim:>4} | "
              f"{best[0]:>10.2e} {str(found_lt):>9} "
              f"{str(gotA) if found_lt else '-':>5} {str(gotS) if found_lt else '-':>5} "
              f"{('YES' if ok else ('NO' if found_lt else '未找到')):>10}")
        break

print()
print(f"=== 汇总 ===  YES: {yes}   找到但(S)失败: {no}   未找到退化点: {n_inst-yes-no}")
print()
print("判读：")
print("  · 若 YES 全部且无 NO ⟹ (C1)(C2) 在 k>=2 亦成立 ⟹ 情形 II 很可能恒 YES ⟹ 判定平凡")
print("  · 若出现 NO（退化点上 (S) 失败）⟹ (C2) 被证伪 ⟹ 需真正的代数判定")
