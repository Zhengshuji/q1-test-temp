# -*- coding: utf-8 -*-
"""
decide_parallel.py —— 对**构造出的真平行实例**判定 (A) ∧ T5a

判据（全部为秩条件，线性 ✓）：
  (A)  ⟺ rank[LA; L; C; CA] == rank[L; C; CA]          （4-块条件，见 FINAL.md T1）
  T5a  ⟺ rank(L·N_CA) < r                               （行空间交非平凡）
  真平行 ⟺ rank[Π(L); Π(LA)] == 1
"""
import os, io, contextlib
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    s = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s, "lib", "exec"), _ns)
mm, ker, condA = _ns["mm"], _ns["ker_basis"], _ns["condA"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rk2, se, mm2 = _ns2["rank_exact"], _ns2["solve_exact"], _ns2["matmul"]


def mat(r):
    return [[F(x) for x in q] for q in r]


def condA_rank(A, C, L):
    """(A) 的 4-块秩判据"""
    LA = mm2(L, A)
    lhs = LA + L + C + mm2(C, A)
    rhs = L + C + mm2(C, A)
    return rk2(lhs) == rk2(rhs), rk2(lhs), rk2(rhs)


def main():
    print("=== 对构造出的真平行实例判定 (A) ∧ T5a ===\n")
    A = mat([[0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]])
    C = mat([[0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0]])
    CA = mm2(C, A)
    B = ker(C + CA)
    n, d = len(B), len(B[0])
    print("n=%d p=%d d_CA=%d" % (n, len(C), d))

    # 收集所有可用的行（l 使 lB = u，u 为 B 的列）
    allrows = []
    for j in range(d):
        u = [B[i][j] for i in range(n)]
        DesL = [[B[i][t] for i in range(n)] for t in range(d)]
        r3 = se(DesL, [[u[t]] for t in range(d)])
        if r3 is None:
            continue
        l0, nsol = r3
        cands = ([l0] if any(x != 0 for x in l0) else []) + [w for w in nsol if any(x != 0 for x in w)]
        for w in cands:
            if all(x == 0 for x in mm2([w], B)[0]):
                continue
            if w not in allrows:
                allrows.append(w)
    print("可用行（Pi(l) ≠ 0）共 %d 条\n" % len(allrows))

    # 逐行 + 逐对检查
    print("--- 单行实例 (r=1) ---")
    for i, l in enumerate(allrows):
        L = [l]
        P = mm2(L, B)
        tp = rk2(P + mm2(mm2(L, A), B)) == 1
        t5a = rk2(P) < 1
        okA, r1, r2_ = condA_rank(A, C, L)
        print("  l%-2d TP=%-5s T5a=%-5s (A)=%-5s  Pi(l)=%s" %
              (i, tp, t5a, okA, [str(x) for x in P[0]]))

    print("\n--- 两行实例 (r=2) ---")
    import itertools
    hits = []
    for i, j in itertools.combinations(range(len(allrows)), 2):
        L = [allrows[i], allrows[j]]
        P = mm2(L, B)
        tp = rk2(P + mm2(mm2(L, A), B)) == 1
        if not tp:
            continue
        t5a = rk2(P) < 2
        okA, r1, r2_ = condA_rank(A, C, L)
        tag = ""
        if t5a and okA:
            tag = "   <=== (A) ∧ T5a 同时成立 ✓✓"
            hits.append((i, j, L, P))
        print("  (l%d,l%d) TP=%-5s T5a=%-5s (A)=%-5s  ranks(%d,%d)%s" %
              (i, j, tp, t5a, okA, r1, r2_, tag))

    print("\n=== 结论 ===")
    print("同时满足 真平行 ∧ (A) ∧ T5a 的两行实例：%d 个" % len(hits))
    for i, j, L, P in hits[:5]:
        print("  L0 = %s" % [[str(x) for x in r] for r in L])
        print("      Pi(L0) = %s" % [[str(x) for x in r] for r in P])
    return hits


if __name__ == "__main__":
    main()
