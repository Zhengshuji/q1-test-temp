r"""
c16_criterion.py -- ⭐⭐⭐⭐ 候选判据：Type I ⟸ 存在"实"广义特征值

【推导】
  ρ=1 的充分构造：所有行取同一个 (a, sa) ∈ W = {(vN, vAN)}
  ⟹ 只需 ∃ v: v·(AN − sN) = 0 且 vN ≠ 0  （**关于 (v,s) 的双线性系统**）

  等价说法：s 是 "N 与 AN 的广义特征值"，且对应右向量不被 N 杀死。

【不变 K 的情形】
  AN = N·A'  ⟹  v(AN − sN) = (vN)(A' − sI)
  ⟹ vN ≠ 0 且 (vN)(A'−sI) = 0 ⟹ s 是 A' 的**实**特征值
  ⟹ 若 A' 只有复特征值（如旋转）⟹ **无解** ⟹ Type II！

【本脚本】
  对每个实例，数一下"实广义特征值"存在与否，并与 c14/c15 的类型对照。
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


def rank_rat(M):
    """有理数矩阵的秩（Fraction）"""
    return rk(M)


def char_poly_rat(M):
    """M 为 n×n 有理矩阵；返回特征多项式系数（低次在前），用 Faddeev–LeVerrier"""
    n = len(M)
    I = [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    # Faddeev–LeVerrier: p(λ) = λ^n + c1 λ^{n-1} + ... + cn
    Mk = [[Fr(0)] * n for _ in range(n)]
    cs = []
    Acur = [row[:] for row in I]
    for k in range(1, n + 1):
        Mk = mm(M, Acur) if k > 1 else mm(M, I)
        c = -sum(Mk[i][i] for i in range(n)) / k
        cs.append(c)
        # Acur = Mk + c*I
        Acur = [[Mk[i][j] + (c if i == j else Fr(0)) for j in range(n)] for i in range(n)]
    # p(λ) = λ^n + cs[0] λ^{n-1} + ... + cs[n-1]
    coef = [cs[-1]] + list(reversed(cs[:-1])) + [Fr(1)]
    while len(coef) > 1 and coef[-1] == 0:
        coef.pop()
    return coef


def has_real_root(coef):
    """有理系数多项式是否有**实**根 —— 用 Sturm 序列（严格判定）"""
    p = [c for c in coef]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    if len(p) <= 1:
        return True
    def norm(q):
        q = [c for c in q]
        while len(q) > 1 and q[-1] == 0:
            q.pop()
        if q[-1] != 0:
            lc = q[-1]
            q = [c / lc for c in q]
        return q
    def divmod_poly(a, b):
        a = [c for c in a]; b = norm([c for c in b])
        db = len(b) - 1
        q = [Fr(0)] * max(1, len(a) - db)
        while len(a) - 1 >= db and any(x != 0 for x in a):
            d = len(a) - 1 - db
            co = a[-1] / b[-1]
            q[d] += co
            for i in range(len(b)):
                a[d + i] -= co * b[i]
            while len(a) > 1 and a[-1] == 0:
                a.pop()
        return q, a
    def deriv(q):
        return [Fr(i) * q[i] for i in range(1, len(q))] or [Fr(0)]
    seq = [norm(p), norm(deriv(p))]
    while len(seq[-1]) > 1 or (len(seq[-1]) == 1 and seq[-1][0] != 0):
        _, r = divmod_poly(seq[-2], seq[-1])
        r = norm([-c for c in r])
        if len(r) == 1 and r[0] == 0:
            break
        seq.append(r)
        if len(seq) > 60:
            break
    # 变号数：x = -inf 与 x = +inf
    def signs_at(seq, at_inf):
        vals = []
        for q in seq:
            d = len(q) - 1
            lc = q[-1]
            if at_inf > 0:
                vals.append(lc)
            else:
                vals.append(lc if d % 2 == 0 else -lc)
        return vals
    def count_sign_changes(vals):
        c = 0
        prev = None
        for v in vals:
            if v == 0:
                continue
            s = 1 if v > 0 else -1
            if prev is not None and s != prev:
                c += 1
            prev = s
        return c
    Vp = count_sign_changes(signs_at(seq, +1))
    Vm = count_sign_changes(signs_at(seq, -1))
    return (Vm - Vp) > 0


def main():
    print("=== 候选判据：A' 是否有实特征值（不变情形）===\n")
    print("%-3s %-5s %3s %3s %3s %6s %10s %8s" %
          ("n","inst","q0","d","m","退化","K不变","A'实谱?")
    );
    print("-"*52)
    n=5
    rng=random.Random(123450+n)
    done=0
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
        M=[N[i][:]+AN[i][:] for i in range(n)]
        # m = rank M
        m=rk(M)
        inv = (m==d)
        pv=[sum(L0[0][i]*N[i][j] for i in range(n)) for j in range(d)]
        degen=all(x==0 for x in pv)
        real_spec="—"
        if inv:
            # A' = N^{-1} A N 的正方形表示（用最小二乘解 N X = AN）
            # 解 N X = AN（d×d）
            X=None
            # 用伪逆：X = (N^T N)^{-1} N^T AN
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]     # d×n
            NtN=mm(Nt,N)                                            # d×d
            try:
                invNtN=[[Fr(0)]]*0
                # 简单求逆
                d2=len(NtN)
                M2=[row[:]+[Fr(1) if i==j else Fr(0) for j in range(d2)] for i,row in enumerate(NtN)]
                for c in range(d2):
                    p=None
                    for i in range(c,d2):
                        if M2[i][c]!=0: p=i; break
                    if p is None: raise ValueError
                    M2[c],M2[p]=M2[p],M2[c]
                    pv2=M2[c][c]; M2[c]=[x/pv2 for x in M2[c]]
                    for i in range(d2):
                        if i!=c and M2[i][c]!=0:
                            f=M2[i][c]
                            M2[i]=[M2[i][j]-f*M2[c][j] for j in range(2*d2)]
                invNtN=[row[d2:] for row in M2]
                X=mm(mm(invNtN,Nt),AN)
                coef=char_poly_rat(X)
                real_spec = "**有**" if has_real_root(coef) else "**无**"
            except Exception:
                real_spec="?"
        done+=1
        print("%-3d %-5d %3d %3d %3d %6s %10s %8s" %
              (n,trial,q0,d,m,"T" if degen else "F","T" if inv else "F",real_spec))
    print()
    print("【判读】")
    print("  c14/c15 的数据（q=d+1 处成功率）：")
    print("    inst 0: 95.0% ; inst 1: 97.5% ; inst 2: 0%(实为采样运气) ;")
    print("    inst 3: 0% (K 不变!) ; inst 4: 0.6% (Type II) ; inst 5: 97.5%")
    print("  ⟹ 若 'K 不变 ⟹ A' 无实谱' 吻合 inst 3，则判据方向正确")
    print("  ⟹ 但 inst 0/1/2/4/5 都是**非不变**，本判据不适用 —— 需要非不变版本的判据")


if __name__ == "__main__":
    main()
