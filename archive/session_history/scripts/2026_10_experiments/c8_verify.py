r"""
c8_verify.py -- ⭐⭐⭐ 检验猜想 c8：q* ≤ q0+1（扩大枚举域与 n）

【为什么这是本会话最关键的一步】
  c7_threshold.py 发现（n=4, 域 {−1,0,1}）：
     退化+非不变 : q* = q0        （6/6）
     非退化+非不变: q* = q0+1      （5/6）
  ⟹ 若 q* ≤ q0+1 恒成立 ⟹ 判定 = 常数次秩验证 ⟹ **多项式** ⟹ **q1 为假**

【本脚本】用更大枚举域（{−2..2}，625 个）与 n=5 检验
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

def cond_5a(L,A,N):
    LN=mm(L,N); LAN=mm(mm(L,A),N)
    K=ker_basis(LN)
    if not K or not K[0]: return True
    assert len(LAN[0])==len(K)
    return rk(mm(LAN,K))==0

def cond_5b(L,A,N,maxminors=600):
    d=len(N[0]); AN=mm(A,N); LN=mm(L,N); rho=rk(LN)
    if rho==0: return True
    LAN=mm(L,AN); q=len(L)
    P=[[[-LAN[i][j], LN[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
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

def try_k(L0,A,N,n,r,k,dom,cap):
    cnt=0
    for vals in itertools.product(dom, repeat=k*n):
        cnt+=1
        if cnt>cap: return None, cnt      # 截断
        R=[[Fr(vals[i*n+j]) for j in range(n)] for i in range(k)]
        L=L0+R
        if not cond_5a(L,A,N): continue
        if cond_5b(L,A,N): return True, cnt
    return False, cnt


def main():
    print("=== c8 检验：q* ≤ q0+1 ？（更大枚举域 + n=5）===\n")
    for n, dom, cap, want in [(4, [-2,-1,0,1,2], 7000, 10), (5, [-1,0,1], 7000, 8)]:
        print("--- n = %d, 枚举域 %s（|域|^k·n）---" % (n, dom))
        print("%-6s %3s %3s %6s %6s %6s %8s %8s" %
              ("inst","n","q0","退化?","K不变?","k0","q*","q*−q0"))
        rng = random.Random(7000 + n)
        done = 0; res = []
        for trial in range(400000):
            if done >= want: break
            A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
            Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(Cc)!=1: continue
            CA=mm(Cc,A)
            if rk(CA)!=1: continue
            W=Cc+CA
            N=ker_basis(W)
            if not N or not N[0]: continue
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
            if k0<1 or k0*n>8: continue
            inv=is_inv(A,N)
            pv=[sum(L0[0][i]*N[i][j] for i in range(n)) for j in range(len(N[0]))]
            degen=all(x==0 for x in pv)
            qstar=None; trunc=False
            for extra in range(3):
                k=k0+extra
                if k*n > 8: break
                ok,cnt = try_k(L0,A,N,n,r,k,dom,cap)
                if ok is None:
                    trunc=True; break
                if ok:
                    qstar=q0+extra; break
            done+=1
            qs = ("截断" if trunc else ("—" if qstar is None else str(qstar)))
            ds = ("?" if (trunc or qstar is None) else str(qstar-q0))
            print("%-6d %3d %3d %6s %6s %6d %8s %8s" %
                  (trial, n, q0, "T" if degen else "F", "T" if inv else "F", k0, qs, ds))
            res.append((degen, inv, qstar-q0 if qstar is not None else None, trunc))
        print()
        for lab, mask in [("退化+非不变", lambda d,i: d and not i),
                          ("非退化+非不变", lambda d,i: (not d) and (not i)),
                          ("退化+不变", lambda d,i: d and i),
                          ("非退化+不变", lambda d,i: (not d) and i)]:
            sel=[s for s in res if mask(s[0],s[1])]
            if not sel: continue
            found=[s[2] for s in sel if s[2] is not None]
            tr=sum(1 for s in sel if s[3])
            print("  %-14s: %d 个；找到 q* %d 个；q*−q0 = %s；截断 %d"
                  % (lab, len(sel), len(found), sorted(set(found)) if found else "—", tr))
        print()
    print("【判读】")
    print("  若所有 q*−q0 ≤ 1 ⟹ **c8 成立** ⟹ 判定多项式 ⟹ **q1 为假** ⭐⭐⭐")
    print("  若出现 q*−q0 ≥ 2 或大量'—' ⟹ c8 不成立，需要更细的分析")


if __name__ == "__main__":
    main()
