r"""
c7_threshold.py -- ⭐⭐⭐ 关键实验：**最小可行的 q**（增广行数）是多少？

【动机】
  穷举显示（history/52 §7.9）：
    · q = q0 时：非退化 ⟹ NO（26/26）；退化+非不变 ⟹ 有时 YES
  ⟹ 但**如果放开预算**（q = q0+1, q0+2 …），非退化实例能否变 YES？
  ⟹ 若能，则判定可能变成"YES ⟺ q ≥ 某阈值" —— 仍是**多项式**（q1 假！）
  ⟹ 若不能，则"非退化 ⟹ 恒 NO"是**无条件**的（q1 更接近真）

【做法】
  对每个实例，令 k = q − r 从 k0(=q0−r) 起递增：
     穷举 R ∈ {−1,0,1}^{k×n}，测 (5a)∧(5b)
     找到第一个可行的 q ⟹ 记最小可行 q*
  比较 q* 与 q0，以及 q* 与"退化/不变"的关系
"""
import os
import io
import contextlib
import random
import itertools
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
    LN=mm(L,N); LAN=mm(mm(L,A),N)
    K=ker_basis(LN)
    if not K or not K[0]: return True
    assert len(LAN[0])==len(K)
    return rk(mm(LAN,K))==0

def cond_5b(L, A, N, maxminors=600):
    d=len(N[0]); AN=mm(A,N); LN=mm(L,N); rho=rk(LN)
    if rho==0: return True
    LAN=mm(L,AN); q=len(L)
    P=[[[-LAN[i][j], LN[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q), rho):
        for cols in itertools.combinations(range(d), rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows], rho)
            if dd!=[Fr(0)]: ps.append(dd)
            cnt+=1
            if cnt>maxminors: break
        if cnt>maxminors: break
    return const_nz(gcd_all(ps))

def is_inv(A,N):
    if not N or not N[0]: return True
    AN=mm(A,N)
    cj=[N[i][:]+AN[i][:] for i in range(len(N))]
    return rk(cj)==rk(N)


def try_k(L0, A, N, n, r, k, dom, max_pairs=7000):
    """穷举 R ∈ dom^{k×n}；返回 (找到?, 枚举数, (5a)数)"""
    cnt=0; n5a=0
    for vals in itertools.product(dom, repeat=k*n):
        cnt+=1
        if cnt > max_pairs: break
        R=[[Fr(vals[i*n+j]) for j in range(n)] for i in range(k)]
        L=L0+R
        if not cond_5a(L,A,N): continue
        n5a+=1
        if cond_5b(L,A,N): return True, cnt, n5a
    return False, cnt, n5a


def main():
    print("=== 最小可行 q 的实验（q = q0, q0+1, q0+2）===\n")
    print("%-6s %3s %3s %6s %6s %6s %6s %8s" %
          ("inst","n","q0","退化?","K不变?","k=q0-r","q*","q*−q0"))
    print("-"*58)
    rng = random.Random(555111)
    n = 4
    dom = [-1,0,1]
    stats = []
    done = 0
    for trial in range(300000):
        if done >= 12: break
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA
        N=ker_basis(W)
        if not N or not N[0]: continue
        # L0：一半退化(CA) 一半 generic
        if trial % 2 == 0:
            L0=[CA[0][:]]
        else:
            L0=None
            for _x in range(40):
                cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
                if rk(cand)!=1: continue
                if rk(cand+Cc)!=2: continue
                pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(len(N[0]))]
                if all(x==0 for x in pv): continue
                L0=cand; break
            if L0 is None: continue
        if rk(L0+Cc)!=2: continue
        try:
            _Lx,eta=p1(A,Cc,L0)
        except Exception:
            continue
        if not eta: continue
        q0=sum(eta); r=1; k0=q0-r
        if k0 < 1 or k0 * n > 8:       # 限枚举规模（k0 ≤ 2, n=4）
            continue
        inv=is_inv(A,N)
        pv=[sum(L0[0][i]*N[i][j] for i in range(n)) for j in range(len(N[0]))]
        degen=all(x==0 for x in pv)
        qstar=None
        for extra in range(3):            # q = q0, q0+1, q0+2
            k=k0+extra
            if k*n > 8: break
            ok,cnt,n5a = try_k(L0,A,N,n,r,k,dom)
            if ok:
                qstar=q0+extra
                break
        done+=1
        qs = "—" if qstar is None else str(qstar)
        ds = ("—" if qstar is None else str(qstar-q0))
        print("%-6d %3d %3d %6s %6s %6d %6s %8s" %
              (trial, n, q0, "T" if degen else "F", "T" if inv else "F",
               k0, qs, ds))
        stats.append((degen, inv, qstar-q0 if qstar is not None else None))
    print()
    print("【统计】")
    for lab, mask in [("退化+非不变", lambda d,i: d and not i),
                      ("退化+不变",   lambda d,i: d and i),
                      ("非退化+非不变", lambda d,i: (not d) and (not i)),
                      ("非退化+不变",  lambda d,i: (not d) and i)]:
        sel=[s for s in stats if mask(s[0],s[1])]
        if not sel: continue
        found=[s[2] for s in sel if s[2] is not None]
        print("  %-14s: %d 个；找到 q* 的 %d 个；q*−q0 值 = %s"
              % (lab, len(sel), len(found), sorted(set(found)) if found else "—"))
    print()
    print("【判读】")
    print("  若非退化组在 q0+1 或 q0+2 找到 YES ⟹ 判定是『q ≥ 阈值』⟹ 可能多项式（q1 假）")
    print("  若非退化组在所有 q 都 NO ⟹『非退化 ⟹ 恒 NO』无条件成立（q1 更接近真）")


if __name__ == "__main__":
    main()
