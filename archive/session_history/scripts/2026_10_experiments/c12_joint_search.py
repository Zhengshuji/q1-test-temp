r"""
c12_joint_search.py -- ⭐⭐⭐ n=6 的**联合搜索**（不做逐行贪心）

【关键更正】
  §7.11 我说"加行使 (5a) 更易" —— **错**！新行引入 w1 约束，ker A0 缩小后可能不再被 A1 杀死。
  ⟹ 必须**一次选够 k 行**。

【参数化（最终形式）】
  M = [N, AN]  (n×2d)；row(M) 的一组基 b_1..b_m（每个在 R^{2d}）
  新行的候选 = 任意 w ∈ row(M)，拆成 (w 的前 d 个分量, 后 d 个) 作为 A0/A1 的新行
  ⟹ 参数 = k·m 个系数

【做法】随机搜索 k·m 个系数（在 {−2..2} 内的整数），检验 (5a)∧(5b)
   —— 因为 row(M) 上的解集不是薄集（已有大量 (5a) 点），随机搜索是合理的
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

def cond_5b(A0,A1,maxminors=300):
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

def row_basis(M):
    """row(M) 的一组基（每个是长为 cols 的向量）"""
    Mt=[[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]   # 转置
    Kb=ker_basis(Mt)          # 零空间：cols×e
    if not Kb or not Kb[0]: return []
    return [[Kb[j][i] for j in range(len(Kb[0]))] for i in range(len(Kb[0]))] and None


def row_space_basis(M):
    """返回 row(M) 的一组基（列表，每个长度为 len(M[0])）"""
    m_rows = len(M); ncols = len(M[0])
    # 取 M 的行，做行化简取主元行
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


def main():
    print("=== n=6 联合搜索：检验 q* = d+1 ===\n")
    n=6
    rng=random.Random(777001)
    done=0
    print("%-6s %3s %3s %4s %6s %8s %10s %8s %8s" %
          ("inst","q0","d","m","试q","采样数","(5a)数","(5a∧5b)","结论"))
    print("-"*62)
    t_all=time.time()
    for trial in range(100000):
        if done>=3 or time.time()-t_all>750: break
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA
        N=ker_basis(W)
        if not N or not N[0]: continue
        d=len(N[0])
        # 非退化 L0
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
        q0=sum(eta); r=1
        AN=mm(A,N)
        M=[N[i][:]+AN[i][:] for i in range(n)]
        B=row_space_basis(M)
        m=len(B)
        qtest=d+1                 # 检验 q = d+1
        k=qtest-r
        if k<1 or k*m>14:         # 限参数规模
            continue
        done+=1
        # A0/A1 的固定部分
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        nsamp=0; n5a=0; hit=0
        tt=time.time()
        while nsamp < 8000 and time.time()-tt < 200:
            nsamp+=1
            rows=[[Fr(rng.randint(-2,2)) for _ in range(m)] for _ in range(k)]
            A0=[H0[i][:] for i in range(r)]
            A1=[F0[i][:] for i in range(r)]
            for rr in rows:
                w=[sum(rr[t]*B[t][j] for t in range(m)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if not cond_5a(A0,A1): continue
            n5a+=1
            if cond_5b(A0,A1):
                hit+=1; break
        print("%-6d %3d %3d %4d %6d %8d %10d %8d %8s" %
              (trial,q0,d,m,qtest,nsamp,n5a,hit,"**YES ✓**" if hit else "NO"))
    print()
    print("【判读】")
    print("  若 q=d+1 全部 YES ⟹ **H 成立**（q*=d+1）⟹ 最小 |R| = d+1−r ⟹ 多项式 ⟹ q1 假")
    print("  若全部 NO ⟹ H 破产（可能 q* 更大）")


if __name__ == "__main__":
    main()
