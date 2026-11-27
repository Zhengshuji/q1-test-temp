r"""
c15_thin_or_empty.py -- ⭐⭐⭐⭐ "薄成功集" vs "空"：大规模搜索 + 测 q=d+2

【问题】
  c14 发现某些非不变实例在 q=d+1 处 160 次采样 0 命中。
  但 0/160 在 {-2..2}^{12} ≈ 2.4e8 中太弱 ⟹ 需大规模搜索区分"薄"与"空"。

【做法】
  1. 复现 c14 的实例（同种子），挑出 0% 那两个
  2. 在 q=d+1 处做 **20000 次** 随机采样（域 {-3..3} 与 {-1,0,1} 混合）
  3. 若仍 0 ⟹ 在 q=d+2 处搜索
"""
import os
import io
import contextlib
import random
import itertools
import time
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
    q=list(p)
    while len(q)>1 and q[-1]==0: q.pop()
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

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    assert len(A1[0])==len(K)
    return rk(mm(A1,K))==0

def cond_5b(A0,A1,maxminors=400):
    q=len(A0); d=len(A0[0]); rho=rk(A0)
    if rho==0: return True
    P=[[[-A1[i][j], A0[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
            if dd!=[Fr(0)]: ps.append(dd)
            cnt+=1
            if cnt>maxminors: break
        if cnt>maxminors: break
    return const_nz(gcd_all(ps))

def row_space_basis(M):
    m_rows=len(M); ncols=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(ncols):
        p=None
        for i in range(r,m_rows):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m_rows):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(ncols)]
        piv.append(r); r+=1
        if r==m_rows: break
    return [A[i][:] for i in piv]

def search(A0f, A1f, B, d, r, k, nsamp, rng, dom):
    m=len(B); ns=0; n5a=0; nboth=0; hit=None
    while ns < nsamp:
        ns+=1
        rows=[[Fr(rng.choice(dom)) for _ in range(m)] for _ in range(k)]
        A0=[A0f[i][:] for i in range(r)]; A1=[A1f[i][:] for i in range(r)]
        for rr in rows:
            w=[sum(rr[t]*B[t][j] for t in range(m)) for j in range(2*d)]
            A0.append(w[:d]); A1.append(w[d:])
        if not cond_5a(A0,A1): continue
        n5a+=1
        if cond_5b(A0,A1):
            nboth+=1
            if hit is None: hit=rows
            break
    return ns, n5a, nboth, hit


def main():
    n=5
    rng=random.Random(123450+n)
    targets={2,4}          # c14 中 0% / 0.6% 的两个
    found={}
    done=0; t_all=time.time()
    for trial in range(80000):
        if done>=6 or time.time()-t_all>200: break
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA
        N=ker_basis(W)
        if not N or not N[0]: continue
        d=len(N[0])
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
        q0=sum(eta)
        if trial in targets:
            found[trial]=(A,Cc,L0,N,d,q0)
        done+=1
    print("复现实例：%s" % sorted(found.keys()))
    print()
    for trial in sorted(found):
        A,Cc,L0,N,d,q0=found[trial]
        AN=mm(A,N)
        M=[N[i][:]+AN[i][:] for i in range(n)]
        B=row_space_basis(M); m=len(B)
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        print("=== trial %d: q0=%d, d=%d, m=%d ===" % (trial,q0,d,m))
        for q in [d+1, d+2]:
            k=q-1
            for dom,nsamp in [([-1,0,1],3000), ([-3,-2,-1,0,1,2,3],20000)]:
                t0=time.time()
                ns,n5a,nboth,hit = search(H0,F0,B,d,1,k,nsamp,
                                          random.Random(1000*trial+q+len(dom)),dom)
                print("   q=%d  k=%d  域大小=%d  采样=%-6d (5a)数=%-6d (5a∧5b)=%-4d  用时=%.1fs" %
                      (q,k,len(dom),ns,n5a,nboth,time.time()-t0))
                if hit is not None:
                    print("      ⟹ **找到** ✓")
                    break
        print()
    print("【判读】")
    print("  若 q=d+1 大规模仍 0 ⟹ 成功集**很可能是空**（而非薄）")
    print("  且 q=d+2 命中 ⟹ **该实例的 q* = d+2** ⟹ 阈值依实例而变 ⟹ 判定有内容 ⭐")


if __name__ == "__main__":
    main()
