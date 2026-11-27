# -*- coding: utf-8 -*-
"""P2'：暴力枚举独立验证 q0 = Ση_j（完全不用 p1 的 η）

方法：
  候选行集合 S = { C A^k 的各行, L0 A^k 的各行 : k = 0..n-1 }
  对 m = 0,1,2,... 枚举 S 的所有 m 元子集，令 V = row(L0) + span(所选)，
  检验 (A)：rank[V·A; V; C; CA] == rank[V; C; CA]
  最小行数 = r + 最小可行 m；  与 q0 比较。
"""
import itertools
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random")[0]
exec(head)


def satisfies_A(Ac, Cc, V):
    """(A): row(V·A) ⊆ row(V, C, CA)"""
    VA = mm(V, Ac); W = V + Cc + mm(Cc, Ac)
    return rk(W + VA) == rk(W)


def brute_min_rows(Ac, Cc, Lc):
    """暴力求最小行数（返回 (最小行数, m) 或 None）"""
    n = len(Ac); r = len(Lc)
    cand = []
    curC = Cc[:]; curL = Lc[:]
    for k in range(n):
        cand += curC; cand += curL
        curC = mm(curC, Ac); curL = mm(curL, Ac)
    # 去重（按行向量）
    uniq = []
    for row in cand:
        if all(any(x != 0 for x in row) for _ in [0]) and row not in uniq:
            uniq.append(row)
    N = len(uniq)
    for m in range(0, min(N, 5) + 1):
        for comb in itertools.combinations(range(N), m):
            V = Lc[:] + [uniq[i] for i in comb]
            # 去掉线性相关的多余行（不影响 (A) 的检验）
            if satisfies_A(Ac, Cc, V):
                return r + m, m
    return None, None


rng = random.Random(13579)
print("P2'：暴力枚举 vs  p1 的 q0  （完全独立的两条路径）")
print()
print(f"{'类型':>18} | {'r/p/n':>8} | {'η':>12} {'q0':>4} | "
      f"{'候选行数':>8} {'暴力最小行数':>12} {'一致?':>7}")
print("-" * 92)
agree = 0; total = 0; mismatch = 0
shown = 0
for t in range(20000):
    if shown >= 10: break
    n = 4
    p = 1
    r = 1
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
    Lmat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
    Ac, Cc, Lc = toF(Amat), toF(Cmat), toF(Lmat)
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
    bmin, bm = brute_min_rows(Ac, Cc, Lc)
    shown += 1
    total += 1
    ok = (bmin == q0)
    if ok: agree += 1
    else: mismatch += 1
    print(f"{'随机构造':>18} | {r}/{p}/{n:>1} | {str(eta):>12} {q0:>4} | "
          f"{'':>8} {str(bmin):>12} {str(ok):>7}")
    if mismatch >= 3: break

print()
print(f"=== 汇总 ===  一致 {agree} / {total}   不一致 {mismatch}")
print()
print("判读：")
print("  · 全部一致 ⟹ q0 = Ση_j 得到独立验证 ⟹ η 可信")
print("  · 出现不一致 ⟹ η 有误，q0 需重算（影响全项目的阈值表述）")
