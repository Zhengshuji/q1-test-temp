r"""
c10_final_form.py -- ⭐⭐⭐ 化简链的终点：问题只依赖 (A0, A1) 的行空间

【最终形式】
  A0 := L·N      (q×d)
  A1 := L·A·N    (q×d)
  M  := [N, A·N] (n×2d)

  (5a) ⟺ ker A0 ⊆ ker A1
  (5b) ⟺ rank(λA0 − A1) = rank A0  ∀λ
       ⟺ **铅笔 λA0 − A1 无特征值**
         （rank 掉 ⟺ ∃v: A0v≠0 且 A1v = λA0v）

  L 的每一行 = v·M（v ∈ R^n）⟹ **问题只在 row(M) ⊆ R^{2d} 中**

【本脚本验证】
  1. cond_5a / cond_5b **只用 (A0,A1)**（不看 L 的其他信息）
  2. L 的行 ∈ row(M)（即 v↦v·M 的参数化）
  3. (5b) 的"无特征值"等价形式
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

def cond_5a(A0, A1):
    K = ker_basis(A0)
    if not K or not K[0]: return True
    assert len(A1[0]) == len(K)
    return rk(mm(A1, K)) == 0

def cond_5b(A0, A1, maxminors=600):
    q = len(A0); d = len(A0[0]); rho = rk(A0)
    if rho == 0: return True
    P = [[[-A1[i][j], A0[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q), rho):
        for cols in itertools.combinations(range(d), rho):
            dd = Pdet([[P[i][j] for j in cols] for i in rows], rho)
            if dd != [Fr(0)]: ps.append(dd)
            cnt += 1
            if cnt > maxminors: break
        if cnt > maxminors: break
    return const_nz(gcd_all(ps))


def no_eigenvalue(A0, A1, tests=8):
    """等价检验：不存在 (λ, v) 使 A0v ≠ 0 且 A1v = λA0v
       做法：枚举 λ（需真算特征值，这里用抽样 λ 试）——
       ⚠️ 抽样不严格，仅作交叉验证"""
    q=len(A0); d=len(A0[0]); rho=rk(A0)
    if rho==0: return True
    for t in range(tests):
        lam = Fr(random.randint(-3,3))
        M = [[lam*A0[i][j]-A1[i][j] for j in range(d)] for i in range(q)]
        if rk(M) != rho:
            return False
    return True


def main():
    print("=== 最终形式验证：问题只依赖 (A0, A1) ===\n")
    rng = random.Random(31415)
    n = 5
    tot = 0; same = 0; inrow = 0
    for trial in range(3000):
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        C=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(C)!=1: continue
        W=C+mm(C,A)
        N=ker_basis(W)
        if not N or not N[0]: continue
        d=len(N[0])
        AN=mm(A,N)
        Mm=[N[i][:]+AN[i][:] for i in range(n)]        # n×2d
        q=rng.choice([2,3])
        L=[[Fr(rng.randint(-2,2)) for _ in range(n)] for _ in range(q)]
        if rk(L)!=q: continue
        # (A0,A1) 从 L 算
        LN=mm(L,N); LAN=mm(mm(L,A),N)
        # 用 (A0,A1) 判定
        a=cond_5a(LN,LAN); b=cond_5b(LN,LAN)
        tot+=1
        # 检查 (A0,A1) 的两块拼起来 = L·M（应恒成立，因为 M = [N, AN]）
        LM = mm(L, Mm)
        blk0 = [[LM[i][j] for j in range(d)] for i in range(q)]
        blk1 = [[LM[i][d + j] for j in range(d)] for i in range(q)]
        assert len(LN[0]) == d and len(LAN[0]) == d, "维数不符"
        if blk0 == LN and blk1 == LAN:
            inrow += 1
        # (5b) 与"抽样无特征值"交叉（**注：抽样 λ 不可靠，仅作参考**）
        if b == no_eigenvalue(LN, LAN):
            same += 1
    print("随机 (L, A, C) 实例：%d" % tot)
    print("  (A0,A1) = L·M 的两块（参数化正确）：%d" % inrow)
    print("  (5b) 与『抽样无特征值』一致：%d" % same)
    print()
    print("【说明】")
    print("  · cond_5a / cond_5b 的实现**只接受 (A0,A1)** ⟹ 结构上已只依赖它们 ✓")
    print("  · L 的每行 = v·M  ⟹ 搜索空间 = row(M) ⊆ R^{2d} ✓")
    print("  · 因此：**问题的本质是『在 row(N, AN) ⊆ R^{2d} 中选 q 行』**")
    print()
    print("=" * 60)
    print("最终形式（本会话化简链的终点）")
    print("=" * 60)
    print("  给定  N (n×d),  A0₀ = L0·N (r×d),  A1₀ = L0·A·N (r×d)")
    print("  求    k 个向量 w_1..w_k ∈ row([N, AN]) ⊆ R^{2d}")
    print("  使    A0 = [A0₀; w_1的d列; …], A1 = [A1₀; w_1的后d列; …] 满足")
    print("        (5a) ker A0 ⊆ ker A1")
    print("        (5b) rank(λA0 − A1) ≡ rank A0  ∀λ   （铅笔无特征值）")


if __name__ == "__main__":
    main()
