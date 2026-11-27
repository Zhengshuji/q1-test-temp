r"""c292：(2,6) 铅笔的结构化搜索——能否找到 span < dim L 的退化铅笔？

随机铅笔已由 `c290`（D=2, m=6）证明非退化（span=13）。这里试**结构化**的铅笔：
- 共享 2 维核；
- 两个都是 rank 2；
- 一个是 rank 2、一个 rank 4；
- 同余。

用法：python proof/layer_program/c292_struct_pencils_n6.py
"""
import os, random, sys
from fractions import Fraction as Fr
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
import audit_independent as AI

def pairs(m): return [(i,j) for i in range(m) for j in range(i+1,m)]

def skew_from(vec, m):
    F=[[Fr(0)]*m for _ in range(m)]
    for (i,j),x in zip(pairs(m), vec):
        F[i][j]=x; F[j][i]=-x
    return F

def wedge(a,b,m):
    return [[a[i]*b[j]-a[j]*b[i] for j in range(m)] for i in range(m)]

def span_of_X(forms, m, rng, nsamp=300):
    pts=[]
    P=pairs(m)
    for _ in range(nsamp):
        u=[Fr(rng.randint(-3,3)) for _ in range(m)]
        if all(x==0 for x in u): continue
        eqs=[[sum(F[i][j]*u[j] for j in range(m)) for i in range(m)] for F in forms]
        for base in AI.nullspace(eqs):
            v=list(base)
            if all(x==0 for x in v): continue
            p=[u[i]*v[j]-u[j]*v[i] for (i,j) in P]
            if all(x==0 for x in p): continue
            for F in forms:
                a=[F[i][j] for (i,j) in P]
                assert sum(a[k]*p[k] for k in range(len(p)))==0
            pts.append(p)
    return pts

def main():
    m=6; P=pairs(m); rng=random.Random(20261031)
    print("(2,6) 结构化铅笔：span 是否 = dim L = 13？（维数 15，dim A=2）\n")
    print(f"{'类型':<26}{'rank(w0)':<10}{'rank(w1)':<10}{'点数':<7}{'span':<7}结论")
    cases=[]
    # 共享 2 维核 {e0,e1}
    for _ in range(2):
        F0=skew_from([Fr(rng.randint(-2,2)) for _ in range(15)],m)
        F1=skew_from([Fr(rng.randint(-2,2)) for _ in range(15)],m)
        for j in range(m):
            for i2 in (0,1):
                F0[i2][j]=Fr(0); F0[j][i2]=Fr(0)
                F1[i2][j]=Fr(0); F1[j][i2]=Fr(0)
        cases.append(("共享 2 维核",F0,F1))
    # 两个 rank 2
    for _ in range(2):
        a=[Fr(rng.randint(-2,2)) for _ in range(m)]; b=[Fr(rng.randint(-2,2)) for _ in range(m)]
        c=[Fr(rng.randint(-2,2)) for _ in range(m)]; d=[Fr(rng.randint(-2,2)) for _ in range(m)]
        cases.append(("两个 rank 2",wedge(a,b,m),wedge(c,d,m)))
    # rank 2 + rank 4
    for _ in range(2):
        a=[Fr(rng.randint(-2,2)) for _ in range(m)]; b=[Fr(rng.randint(-2,2)) for _ in range(m)]
        F1=skew_from([Fr(rng.randint(-2,2)) for _ in range(15)],m)
        cases.append(("rank2 + rank4",wedge(a,b,m),F1))
    for name,F0,F1 in cases:
        pts=span_of_X([F0,F1],m,rng)
        rk=AI.rank(pts) if pts else 0
        verdict=("**证书：span=L** ✓" if rk>=13 else f"下界 {rk} < 13（退化或采样不足）")
        print(f"{name:<26}{AI.rank([r[:] for r in F0]):<10}{AI.rank([r[:] for r in F1]):<10}{len(pts):<7}{rk:<7}{verdict}")
    print("\n结论：若全部达到 13，则 (2,6) 的 D=2 铅笔在所有已测结构下都非退化。")

if __name__=='__main__':
    main()
