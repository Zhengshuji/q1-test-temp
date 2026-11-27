r"""
c17_final_criterion.py -- ⭐⭐⭐⭐ 判据的最终形式与验证

【判据（来自 §7.17 的 ρ=1 构造）】
  需要 (a,0) ∈ W ⟺ ∃v: vN ≠ 0 且 vAN = 0
  ⟺ ker(·AN) ⊄ ker(·N)
  ⟺ **row(N) ⊄ row(AN)**
  ⟺ rank[N; AN] > rank(AN)        （行堆叠！）

【注意】这与 m = rank[N | AN]（**列**拼接，测不变性）不同！
  · m − d = 0 ⟺ K 不变 ⟺ row(AN) ⊆ row(N) 的**对偶**版
  · 本判据是 row(N) ⊆ row(AN) 的方向 —— **相反**！

【验证】与 c14/c15 的 Type I/II 标签对照
"""
import os
import io
import contextlib
import random
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


def main():
    print("=== 判据验证：row(N) ⊄ row(AN) ⟺ Type I ？ ===\n")
    print("%-3s %-5s %3s %3s %3s %5s %8s %8s %8s %8s %8s" %
          ("n","inst","q0","d","m","退化","r(AN)","r[N;AN]","列判据","行判据","实测类型"))
    print("-"*82)
    n=5
    rng=random.Random(123450+n)
    labels={0:"I (95%)",1:"I (97.5%)",2:"I (第1样本)",3:"II (0%,不变)",4:"II (0.6%)",5:"I (97.5%)"}
    done=0
    agree_col=0; agree_row=0; tot=0
    for trial in range(80000):
        if done>=6: break
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
        AN=mm(A,N)
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]          # n×2d（列拼接用）
        m=rk(Mcol)                                          # = rank[N | AN]
        Mrow=[r[:] for r in N]+[r[:] for r in AN]           # 2d×n（行堆叠用）
        rAN=rk(AN)
        rRow=rk(Mrow)                                       # = rank[N; AN]
        pv=[sum(L0[0][i]*N[i][j] for i in range(n)) for j in range(d)]
        degen=all(x==0 for x in pv)
        # 判据
        col_crit = (m-d>0)             # K 非不变（列拼接）
        row_crit = (rRow>rAN)          # row(N) ⊄ row(AN)
        lab=labels.get(trial,"?")
        is_I = lab.startswith("I")
        done+=1; tot+=1
        if col_crit==is_I: agree_col+=1
        if row_crit==is_I: agree_row+=1
        print("%-3d %-5d %3d %3d %3d %5s %8d %8d %8s %8s %8s" %
              (n,trial,q0,d,m,"T" if degen else "F",rAN,rRow,
               "T" if col_crit else "F","T" if row_crit else "F",lab))
    print()
    print("与实测类型一致：列判据 %d/%d ；**行判据 %d/%d**" % (agree_col,tot,agree_row,tot))
    print()
    if agree_row==tot:
        print("⟹⟹⟹ **行判据完全吻合！**")
        print("     **Type I ⟺ row(N) ⊄ row(AN) ⟺ rank[N;AN] > rank(AN)** ⭐⭐⭐⭐")
        print("     ⟹ 这是**纯秩条件** ⟹ 多项式可判 ⟹ **q1 为假**")
    elif agree_row>agree_col:
        print("⟹ 行判据更好（%d vs %d）但未完全吻合" % (agree_row,agree_col))
    else:
        print("⟹ 判据不符")


if __name__ == "__main__":
    main()
