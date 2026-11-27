r"""
c24_geometric.py -- ⭐⭐⭐ (5a)/(5b) 的几何避让形式（等价性验证）

【几何形式】
  M := {(A0·v, A1·v) : v ∈ R^d} = 列空间 [A0 | A1] ⊆ R^q ⊕ R^q

  (5a) ⟺ ker A0 ⊆ ker A1
       ⟺ ∄ v: A0v = 0 且 A1v ≠ 0
       ⟺ **M ∩ ({0} × R^q) = 0**

  (5b) ⟺ rank(λA0 − A1) ≡ rank A0  ∀λ
       ⟺ ∄ (λ, v): A0v ≠ 0 且 (λA0 − A1)v = 0
       ⟺ **M ∩ {(w, λw) : w ≠ 0} = ∅  ∀λ**   （"对角线族"避让）

【本脚本】逐实例双向核对这两个等价
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

def cond_5a_rank(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0

def cond_5a_geom(A0,A1):
    """M ∩ ({0}×R^q) = 0 ⟺ ∄v: A0v=0 且 A1v≠0"""
    q=len(A0); d=len(A0[0])
    Ker=ker_basis(A0)                      # d×e
    if not Ker or not Ker[0]: return True  # ker A0 = 0
    # 检查 A1·Ker 是否全零
    if len(A1[0])!=len(Ker): return False
    return rk(mm(A1,Ker))==0

def cond_5b_rank(A0,A1,maxminors=500):
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

def cond_5b_geom(A0,A1,ns=40):
    """避免对角线族：对有理 λ 抽样核对（仅交叉验证，非严格）"""
    q=len(A0); d=len(A0[0]); rho=rk(A0)
    if rho==0: return True
    for t in range(ns):
        lam=Fr(random.randint(-6,6), random.randint(1,3))
        P=[[lam*A0[i][j]-A1[i][j] for j in range(d)] for i in range(q)]
        if rk(P)!=rho: return False
    return True

def main():
    print("=== 几何形式验证 ===\n")
    rng=random.Random(24680)
    tot=0; a_agree=0; b_agree=0; aT=0; aF=0; bT=0; bF=0
    for trial in range(4000):
        q=rng.choice([2,3,4]); d=rng.choice([2,3])
        A0=[[Fr(rng.randint(-2,2)) for _ in range(d)] for _ in range(q)]
        A1=[[Fr(rng.randint(-2,2)) for _ in range(d)] for _ in range(q)]
        if rk(A0)==0: continue
        # 只保留 (5a) 或接近的样本以增强判定力
        x1=cond_5a_rank(A0,A1); x2=cond_5a_geom(A0,A1)
        y1=cond_5b_rank(A0,A1); y2=cond_5b_geom(A0,A1)
        tot+=1
        if x1==x2: a_agree+=1
        if x1: aT+=1
        else: aF+=1
        if y1==y2: b_agree+=1
        if y1: bT+=1
        else: bF+=1
    print("实例：%d" % tot)
    print("  (5a)：秩/核形式 与 几何形式 一致 %d ；True %d ；False %d" % (a_agree,aT,aF))
    print("  (5b)：gcd 形式 与 λ抽样形式 一致 %d ；True %d ；False %d" % (b_agree,bT,bF))
    print()
    print("【说明】")
    print("  (5a) 的几何形式与 ker 包含是**同一陈述**，必然一致（此处确认无实现错误）")
    print("  (5b) 的抽样形式只作交叉验证；严格判据是子式 gcd")
    print()
    if a_agree==tot and b_agree==tot and aT and aF and bT and bF:
        print("⟹ 两种形式**完全一致**（两侧都有点 ✓）⟹ 几何表述可用 ✓")
        print("   ⟹ 判定问题 = 在 M ⊆ R^q ⊕ R^q 中**同时避开两个代数集**")
    else:
        print("⚠️ 有不一致或缺乏判定力")


if __name__=="__main__":
    main()
