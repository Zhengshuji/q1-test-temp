r"""
c9_growth.py -- ⭐⭐⭐ 测 q*−q0 的增长速率（"加一行"增量搜索）

【关键优化】
  (5a) ⟺ ker(L·N) ⊆ ker(L·A·N)。**加一行**使 ker(L·N) 变小 ⟹ (5a) **更易**满足。
  ⟹ 从已知满足 (5a) 的 L 出发，只搜索**新加的一行**（n 个参数）
  ⟹ 复杂度从 |域|^{k·n} 降到 |域|^n

【做法】
  1. 找 L 满足 (5a)（k = k0 行）
  2. 若 (5b) 也满足 ⟹ q* = q0
  3. 否则：枚举新加一行 ∈ {−2..2}^n，检查 (5a)∧(5b)
  4. 再不行：再加一行
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

def cond_5a(L,A,N):
    LN=mm(L,N); LAN=mm(mm(L,A),N)
    K=ker_basis(LN)
    if not K or not K[0]: return True
    assert len(LAN[0])==len(K)
    return rk(mm(LAN,K))==0

def cond_5b(L,A,N,maxminors=400):
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


def find_qstar(L0, A, N, n, dom, max_extra=3, maxtime=60.0):
    """从 L0 出发，逐行增加，找最小可行 q"""
    t0 = time.time()
    L = [r[:] for r in L0]
    cur_k = 0
    while True:
        if cond_5a(L, A, N) and cond_5b(L, A, N):
            return len(L), 0
        if cur_k >= max_extra or time.time() - t0 > maxtime:
            return None, cur_k
        cur_k += 1
        found = None
        for vals in itertools.product(dom, repeat=n):
            if time.time() - t0 > maxtime:
                break
            cand = [Fr(x) for x in vals]
            Ln = L + [cand]
            if cond_5a(Ln, A, N) and cond_5b(Ln, A, N):
                found = Ln; break
        if found is None:
            # 找不到可行行 ⟹ 随便加一行（保持 (5a) 若可能）继续
            base = None
            for vals in itertools.product(dom, repeat=n):
                cand = [Fr(x) for x in vals]
                Ln = L + [cand]
                if cond_5a(Ln, A, N):
                    base = Ln; break
            if base is None:
                return None, cur_k
            L = base
        else:
            return len(found), cur_k
    return None, cur_k


def main():
    print("=== q*−q0 的增长速率 ===\n")
    dom = [-2,-1,0,1,2]
    for n in [4, 5, 6]:
        print("--- n = %d（域 %s）---" % (n, dom))
        print("%-6s %3s %3s %6s %6s %8s %8s" %
              ("inst","q0","k0","退化?","q*","q*−q0","用时s"))
        print("-"*48)
        rng = random.Random(9000 + n)
        done = 0
        results = []
        t_all = time.time()
        for trial in range(200000):
            if done >= 4 or time.time() - t_all > 300:
                break
            A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
            Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(Cc)!=1: continue
            CA=mm(Cc,A)
            if rk(CA)!=1: continue
            W=Cc+CA
            N=ker_basis(W)
            if not N or not N[0]: continue
            # **非退化** L0（这是最关心的组）
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
            t0=time.time()
            qs, extra = find_qstar(L0,A,N,n,dom,max_extra=3,maxtime=60.0)
            dt=time.time()-t0
            done+=1
            qstr = "—" if qs is None else str(qs)
            dstr = "?" if qs is None else str(qs-q0)
            print("%-6d %3d %3d %6s %8s %8s %8.1f" %
                  (trial,q0,k0,"F",qstr,dstr,dt))
            results.append(qs-q0 if qs is not None else None)
        print("  小结：q*−q0 取值 = %s" % (sorted(set(r for r in results if r is not None)) or "—"))
        print()
    print("【判读】")
    print("  若 q*−q0 随 n 单调增长 ⟹ 阈值增长 ⟹ 支持 NP-hardness 方向")
    print("  若 q*−q0 保持常数 ⟹ q1 可能平凡")


if __name__ == "__main__":
    main()
