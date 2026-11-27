r"""
c11_qstar_vs_d.py -- ⭐⭐⭐ 假设检验：q* = d_CA + 1 ？

【动机】
  c9_growth 观察到 q*−q0 ≈ n−3（线性增长）。但"n"未必是真正的参数！
  更可能的解释：**q* 与 d_CA 有关**（d_CA = n − rank[C;CA] 随 n 增长）

  检查已有数据：
    n=4: q0=2, q*=3, d_CA=2  ⟹ q* = d+1 ✓
    n=5: q0=2, q*=4, d_CA=3  ⟹ q* = d+1 ✓
  ⟹ **假设 H：q* = d_CA + 1（当 q0 ≤ d_CA 时）**

【本脚本】对每个实例：
   · 算 d_CA
   · 用"逐行加"搜索找 q*（到 d+2 为止）
   · 报告 (q0, d, q*) 三元组，检验 q* = d+1
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

def ok(L,A,N):
    return cond_5a(mm(L,N), mm(mm(L,A),N)) and cond_5b(mm(L,N), mm(mm(L,A),N))


def find_qstar(L0,A,N,n,dom,target_max,maxtime=40.0):
    """逐行加，返回 (q*, 说明)。target_max = 最多加到多少行"""
    t0=time.time()
    L=[r[:] for r in L0]
    if ok(L,A,N): return len(L), "直接"
    while len(L) < target_max:
        if time.time()-t0 > maxtime: return None, "超时"
        found=None; base=None
        for vals in itertools.product(dom, repeat=n):
            cand=[Fr(x) for x in vals]
            Ln=L+[cand]
            if ok(Ln,A,N): found=Ln; break
            if base is None and cond_5a(mm(Ln,N), mm(mm(Ln,A),N)): base=Ln
        if found is not None: return len(found), "找到"
        if base is None: return None, "无(5a)可加行"
        L=base
    return None, "达上限"


def main():
    print("=== 假设 H：q* = d_CA + 1 ===\n")
    dom=[-2,-1,0,1,2]
    print("%-3s %-6s %3s %3s %3s %6s %8s %8s %8s" %
          ("n","inst","q0","d","r","退化?","q*","d+1","H成立?"))
    print("-"*56)
    nq=0; nhit=0
    for n in [4,5,6]:
        rng=random.Random(31000+n)
        done=0; t_all=time.time()
        for trial in range(200000):
            if done>=3 or time.time()-t_all>260: break
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
            q0=sum(eta); r=1; k0=q0-r
            if k0<1: continue
            pv=[sum(L0[0][i]*N[i][j] for i in range(n)) for j in range(len(N[0]))]
            degen=all(x==0 for x in pv)
            qstar,why = find_qstar(L0,A,N,n,dom,target_max=d+2,maxtime=35.0)
            done+=1
            hit = (qstar is not None and qstar==d+1)
            if qstar is not None: nq+=1
            if hit: nhit+=1
            print("%-3d %-6d %3d %3d %3d %6s %8s %8d %8s" %
                  (n, trial, q0, d, r, "T" if degen else "F",
                   ("—" if qstar is None else str(qstar)), d+1,
                   ("✓" if hit else ("✗ "+why))))
        print()
    print("得到 q* 的实例：%d ；其中 q*=d+1 的：%d" % (nq,nhit))
    print()
    if nq>0 and nhit==nq:
        print("⟹⟹⟹ **假设 H 全部成立**：q* = d_CA + 1 ⟹")
        print("     最小增广行数 k* = q* − r = d_CA ⟹ **最小 |R| = d_CA** ⭐⭐⭐")
        print("     ⟹ 增长是因为 d_CA 随 n 增长 ⟹ 判定 = 算 d_CA（多项式）")
        print("     ⟹ **q1 可能为假**（但最小 |R| 确实随 n 增长）")
    elif nhit>0:
        print("⟹ 部分成立（%d/%d）—— 需更多数据" % (nhit,nq))
    else:
        print("⟹ 未验证")


if __name__ == "__main__":
    main()
