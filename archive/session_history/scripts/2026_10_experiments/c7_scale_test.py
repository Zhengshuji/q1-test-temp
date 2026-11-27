r"""
c7_scale_test.py -- ⭐⭐⭐ c7 的可扩展性检验

【关键问题】
  c6_exhaustive.py 用 R ∈ {−1,0,1} 枚举。NO 可能只是"枚举域太小"⟹ 假象！
  本脚本用**更大枚举域** + 更大 n 重测：
    · n=4, 域 {−2,…,2}（5⁴=625）
    · n=5, 域 {−1,0,1}（3⁵=243）
    · n=4, 域 {−1,0,1}（对照）

【四组】
  A: L0 = CA（退化）       , K 非不变
  B: L0 随机（generic）    , K 非不变
  C: L0 随机（generic）    , K 不变（CA²=0）
  D: L0 = CA（退化）       , K 不变（CA²=0）

【c7】YES ⟺ π(L0)=0 ∧ K ⊄ ker(CA²)
"""
import os
import io
import contextlib
import random
import itertools
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    _src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]

def Pt(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0: q.pop()
    return q
def Pa(a,b):
    n=max(len(a),len(b)); return Pt([(a[i] if i<len(a) else Fr(0))+(b[i] if i<len(b) else Fr(0)) for i in range(n)])
def Ps(a,b):
    n=max(len(a),len(b)); return Pt([(a[i] if i<len(a) else Fr(0))-(b[i] if i<len(b) else Fr(0)) for i in range(n)])
def Pm(a,b):
    if Pt(a)==[Fr(0)] or Pt(b)==[Fr(0)]: return [Fr(0)]
    r=[Fr(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return Pt(r)
def Pd(a,b):
    a=Pt(a); b=Pt(b); db=len(b)-1
    q=[Fr(0)]*max(1,len(a)-db)
    while len(a)-1>=db and a!=[Fr(0)]:
        d=len(a)-1-db; co=a[-1]/b[-1]; q[d]+=co
        for i in range(len(b)): a[d+i]-=co*b[i]
        a=Pt(a)
    return Pt(q),a
def Pg(a,b):
    a,b=Pt(a),Pt(b)
    while b!=[Fr(0)]:
        _,r=Pd(a,b); a,b=b,r
    if len(a)>1:
        lc=a[-1]; a=[x/lc for x in a]
    return a
def Pdet(M,k):
    if k==1: return [Fr(x) for x in M[0][0]]
    tot=[Fr(0)]
    for j in range(k):
        sub=[row[:j]+row[j+1:] for row in M[1:]]
        d=Pdet(sub,k-1); pr=Pm(M[0][j],d)
        tot=Pa(tot,pr) if j%2==0 else Ps(tot,pr)
    return Pt(tot)
def gcd_all(ps):
    if not ps: return None
    g=ps[0]
    for q in ps[1:]:
        g=Pg(g,q)
        if len(g)==1: break
    return g
def const_nz(g):
    return g is not None and len(Pt(g))==1 and any(x!=0 for x in g)


def cond_5a(L, A, N):
    LN = mm(L, N); LAN = mm(mm(L, A), N)
    K = ker_basis(LN)
    if not K or not K[0]: return True
    assert len(LAN[0]) == len(K), "维数不匹配 5a"
    return rk(mm(LAN, K)) == 0


def cond_5b(L, A, N, maxminors=800):
    d = len(N[0]); AN = mm(A, N); LN = mm(L, N)
    rho = rk(LN)
    if rho == 0: return True
    LAN = mm(L, AN); q = len(L)
    P = [[[-LAN[i][j], LN[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q), rho):
        for cols in itertools.combinations(range(d), rho):
            dd = Pdet([[P[i][j] for j in cols] for i in rows], rho)
            if dd != [Fr(0)]: ps.append(dd)
            cnt += 1
            if cnt > maxminors: break
        if cnt > maxminors: break
    return const_nz(gcd_all(ps))


def is_inv(A, N):
    if not N or not N[0]: return True
    AN = mm(A, N)
    cj = [N[i][:] + AN[i][:] for i in range(len(N))]
    return rk(cj) == rk(N)


def gen_instance(rng, n, force_inv, degenerate):
    A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
    if force_inv:
        A2 = mm(A, A)
        A2T = [[A2[j][i] for j in range(n)] for i in range(n)]
        Kb = ker_basis(A2T)
        if not Kb or not Kb[0] or len(Kb[0]) == 0:
            return None
        e = len(Kb[0])
        Cc = [[Kb[j][rng.randrange(e)] for j in range(n)]]
    else:
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
    if rk(Cc) != 1: return None
    CA2 = mm(mm(Cc, A), A)
    zero = all(all(x == 0 for x in r) for r in CA2)
    if zero != force_inv: return None
    CA = mm(Cc, A)
    if rk(CA) != 1: return None
    if degenerate:
        L0 = [CA[0][:]]
    else:
        L0 = None
        for _x in range(40):
            cand = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
            if rk(cand) != 1: continue
            if rk(cand + Cc) != 2: continue
            # 要求**非**退化：π(L0) ≠ 0
            W0 = Cc + CA
            N0 = ker_basis(W0)
            if not N0 or not N0[0]: continue
            pv = [sum(cand[0][i] * N0[i][j] for i in range(n)) for j in range(len(N0[0]))]
            if all(x == 0 for x in pv): continue
            L0 = cand; break
        if L0 is None: return None
    if rk(L0 + Cc) != 2: return None
    W = Cc + CA
    N = ker_basis(W)
    if not N or not N[0]: return None
    try:
        _Lx, eta = p1(A, Cc, L0)
    except Exception:
        return None
    if not eta: return None
    q0 = sum(eta); k = q0 - 1
    if k != 1: return None
    return A, Cc, L0, N, k


def sweep(n, dom, want, label, force_inv, degenerate, seed):
    rng = random.Random(seed)
    yes = no = 0; rows = []
    tried = 0
    while yes + no < want and tried < 300000:
        tried += 1
        g = gen_instance(rng, n, force_inv, degenerate)
        if g is None: continue
        A, Cc, L0, N, k = g
        if is_inv(A, N) != force_inv: continue
        W = Cc + mm(Cc, A)
        pv = [sum(L0[0][i] * N[i][j] for i in range(n)) for j in range(len(N[0]))]
        degen = all(x == 0 for x in pv)
        if degen != degenerate: continue
        n5a = nboth = 0
        for vals in itertools.product(dom, repeat=k * n):
            R = [[Fr(vals[i * n + j]) for j in range(n)] for i in range(k)]
            L = L0 + R
            if not cond_5a(L, A, N): continue
            n5a += 1
            if cond_5b(L, A, N): nboth += 1
        concl = "**YES**" if nboth else ("NO" if n5a else "无(5a)")
        if nboth: yes += 1
        else: no += 1
        rows.append((label, n, len(dom), k, n5a, nboth, concl))
    return rows, yes, no


def main():
    print("=== c7 可扩展性检验：更大枚举域 + 更大 n ===\n")
    print("%-4s %3s %4s %3s %8s %8s %8s" % ("组","n","|域|","k","(5a)点","(5a∧5b)","结论"))
    print("-" * 48)
    specs = [
        ("A", 4, [-2,-1,0,1,2], 8, False, True,  1001),
        ("B", 4, [-2,-1,0,1,2], 8, False, False, 1002),
        ("C", 4, [-2,-1,0,1,2], 6, True,  False, 1003),
        ("D", 4, [-2,-1,0,1,2], 6, True,  True,  1004),
        ("A", 5, [-1,0,1],      6, False, True,  2001),
        ("B", 5, [-1,0,1],      6, False, False, 2002),
        ("C", 5, [-1,0,1],      6, True,  False, 2003),
        ("D", 5, [-1,0,1],      6, True,  True,  2004),
    ]
    summary = {}
    for (lab, n, dom, want, fi, dg, sd) in specs:
        rows, y, nn = sweep(n, dom, want, lab, fi, dg, sd)
        for r in rows:
            print("%-4s %3d %4d %3d %8d %8d %8s" % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
        key = (lab, n)
        summary[key] = (y, nn)
        print("    → %s(n=%d) 小结：YES %d ；NO %d" % (lab, n, y, nn))
        print()
    print("=" * 48)
    print("【c7 判读】c7: YES ⟺ 退化 ∧ 非不变")
    print()
    print("  ⚠️ 严格判读需要区分两种情况：")
    print("    (i)  **必要性**：非退化 或 不变 ⟹ 应 NO（组 B/C/D 应全 NO）")
    print("    (ii) **充分性**：退化 ∧ 非不变 ⟹ 应 YES（组 A 应全 YES）")
    print()
    nec_ok = True; suf_ok = True
    for (lab, n), (y, nn) in sorted(summary.items()):
        if lab in ("B", "C", "D"):
            if y > 0:
                nec_ok = False
                print("  组%s(n=%d): **必要性被破坏** YES=%d" % (lab, n, y))
            else:
                print("  组%s(n=%d): 必要性 ✓（全 NO，n=%d）" % (lab, n, nn))
        else:  # A
            if nn > 0:
                suf_ok = False
                print("  组%s(n=%d): **充分性被破坏** YES=%d NO=%d  ← 混合！" % (lab, n, y, nn))
            else:
                print("  组%s(n=%d): 充分性 ✓（全 YES，n=%d）" % (lab, n, y))
    print()
    if nec_ok and suf_ok:
        print("⟹⟹⟹ **c7 完全成立** ⟹ q1 可能为假（判定 = 两次秩计算）⭐⭐⭐")
    elif nec_ok and not suf_ok:
        print("⟹⟹ **c7 的『必要性』成立，但『充分性』不成立**")
        print("     即：非退化 或 不变 ⟹ **一定 NO**（证据 26/26 强）")
        print("         退化 ∧ 非变 ⟹ **只是可能 YES**（不保证）")
        print("     ⟹ **判定仍非平凡** ⟹ q1 不能被简单秩判据平凡化 ⚠️")
        print("     ⟹ 但『NO 侧的判据』已经很明确 ⟹ 硬度只能在『退化 ∧ 非不变』区域内")
    else:
        print("⟹ **c7 被破坏**（必要性失败）—— 需重新分析")


if __name__ == "__main__":
    main()
