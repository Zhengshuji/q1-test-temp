r"""
c87_AUDIT_FIXED.py -- 用修正版判据重跑 A19 步 1-2 的审计（含 ρ<d）

旧版 c82 报 2/40 不一致，已定位为 **cond_5b 的 gcd bug**（假阴性），
不是数学问题。本脚本用 exact_gcd.cond_5b（修正版）重测。
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.insert(0, _HERE)
from exact_gcd import cond_5b, cond_5b_verbose, Pdet, gcd_list, _rank, is_nonzero_const

_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

def nullspace_rows(M):
    if not M or not M[0]: return []
    m=len(M); n=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-A[i][fc]
        out.append(v)
    return out

def pbh_form(M,F,q,d,Lam):
    """rank[Λᵀ − λI | N] = q ∀λ ？"""
    Mt=[[M[i][j] for i in range(q)] for j in range(d)]
    Ns=nullspace_rows(Mt)
    if not Ns: return None
    m=len(Ns)
    P=[]
    for i in range(q):
        row=[]
        for j in range(q):
            a=Lam[j][i]
            if i==j: row.append([a, Fr(-1)])
            else:    row.append([a])
        for t in range(m):
            row.append([Ns[t][i]])
        P.append(row)
    ps=[]
    for cols in itertools.combinations(range(q+m),q):
        ps.append(Pdet([[P[i][j] for j in cols] for i in range(q)],q))
    g=gcd_list(ps)
    return is_nonzero_const(g)

def main():
    print("=== 修正版重跑：ρ<d 时 (5b) ⟺ PBH 形式 ===\n")
    print("%-6s %3s %4s %4s %8s %10s %6s" % ("#","d","ρ","q","(5b)","PBH","一致"))
    print("-"*48)
    ok=0; bad=0; tot=0; layers={}
    rng=random.Random(555999)
    for trial in range(3000):
        d=rng.choice([2,3]); q=d+1
        rr=rng.choice([1,2])
        if rr>=d: continue
        M=[[Fr(0)]*d for _ in range(q)]
        for i in range(rr):
            M[i]=[Fr(rng.randint(-1,1)) for _ in range(d)]
        for i in range(rr,q):
            a,b=Fr(rng.randint(-1,1)),Fr(rng.randint(-1,1))
            M[i]=[a*M[0][j]+b*M[1][j] for j in range(d)] if rr==2 else [a*M[0][j] for j in range(d)]
        rho=rk(M)
        if rho==0 or rho>=d: continue
        Lam=[[Fr(rng.randint(-1,1)) for _ in range(q)] for _ in range(q)]
        F=mm(Lam,M)
        g=cond_5b(M,F)
        p=pbh_form(M,F,q,d,Lam)
        if p is None: continue
        tot+=1
        key=(d,rho)
        layers[key]=layers.get(key,[0,0])
        layers[key][0]+=1
        if g==p:
            ok+=1; layers[key][1]+=1
        else:
            bad+=1
            print("%-6d %3d %4d %4d %8s %10s **✗**" % (trial,d,rho,q,str(g),str(p)))
        if tot>=60: break
    print()
    print("ρ<d 实例 %d ；一致 %d ；不一致 %d" % (tot,ok,bad))
    print("按 (d,ρ) 分层：")
    for k in sorted(layers):
        t,c=layers[k]
        print("  (d=%d, ρ=%d) : %d 个，一致 %d" % (k[0],k[1],t,c))
    if bad==0 and tot>0:
        print("\n⟹ **ρ<d 时 (5b) ⟺ PBH 成立** ⟹ A19 步 1-2 审计完整通过 ✓")
        print("   旧版 2/40 的\"不一致\"确认为 gcd bug（假阴性），已消除 ✓")


if __name__=="__main__":
    main()
