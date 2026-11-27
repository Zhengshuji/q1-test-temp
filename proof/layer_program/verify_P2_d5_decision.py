"""§66：$d=5$、$\\dim B=2$、$\\dim W_0=2$、$W_0\\cap B=0$ 时 P2 的**完整判定**。

关键：$\\mathcal U_L=\\operatorname{row}[W_0;\\,L(t)]$，其中 $L(t)=b_1+t\\,b_2$ 是 $B$ 上的直线。
  * $\\operatorname{rank}[W_0;L(t);B]=4$ 对**所有** $t$ 成立（$W_0\\cap B=0$、$L(t)\\subseteq B$）✓
  * $(N)$ ⟺ 对 $u\\in\\{w_1,w_2,L(t)\\}$：$f(u)\\in\\mathcal U_L+B$
         ⟺ 矩阵 $[W_0;\\,L(t);\\,B;\\,f(u)]$ 的全部 5 阶子式为零
  每个这样的子式都是 $t$ 的**一次**多项式 ✓（行对 $t$ 仿射 ✓）
  ⟹ "对所有 $u$ 同时为零" 是一个**线性**方程组（在 $t$ 上）✓
  ⟹ 解集是空/单点/全体 ⟹ **两次取值即可判定** ✓

本脚本在 §65 的实例上做这个判定。
"""
import itertools
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util as iu
spec = iu.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = iu.module_from_spec(spec)
spec.loader.exec_module(Qm)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb

n = 9

A_MAT = [[1,-1,-2,2,1,1,0,0,-1],[2,1,-2,1,-1,-1,2,1,-2],[-2,-1,2,-1,-1,0,-2,-1,-1],
         [2,-1,1,-2,0,0,-2,0,-1],[2,0,0,2,1,1,0,0,-1],[0,2,2,1,0,1,-2,1,0],
         [-1,2,-1,0,1,0,-2,-2,1],[1,1,1,-1,1,-1,-2,2,1],[1,2,1,-1,-1,0,-1,2,1]]
C_MAT = [[-2,0,-2,2,-1,-2,1,-2,-2],[2,1,2,2,-1,0,1,1,-1]]


def instance(seed=1):
    """n=9、p=2、j=4、d=5、dim B=2 的实例（§66 要求 J 非循环 ✓）。"""
    import random
    rng = random.Random(seed)
    A = [[Fr(x) for x in row] for row in A_MAT]
    C = [[Fr(x) for x in row] for row in C_MAT]
    for _ in range(200):
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
        Q = Qm.Quotient(A, C)
        if Q.d != 5 or len(Q.B) != 2:
            return None
        W0 = rb([Q.pi(r) for r in L0] + [Q.pi(mm([r], A)[0]) for r in L0])
        if len(W0) == 2 and rank([r[:] for r in W0] + [r[:] for r in Q.B]) == 4:
            return A, C, L0
    return None


def det_affine(M):
    """M 的行是 (const_vec, tcoef_vec)；返回 (const, tcoef) 的 1 次多项式，即行列式。
    只处理小矩阵（n<=5），用展开式，并把 t 当符号（双数 (c0,c1)）。"""
    k = len(M)
    # 以 (c0, c1) 双数运算
    def mul(x, y):
        return (x[0] * y[0], x[0] * y[1] + x[1] * y[0])

    def sub(x, y):
        return (x[0] - y[0], x[1] - y[1])

    def add(x, y):
        return (x[0] + y[0], x[1] + y[1])

    total = (Fr(0), Fr(0))
    for perm in itertools.permutations(range(k)):
        sign = 1
        p = list(perm)
        for i in range(k):
            for j in range(i + 1, k):
                if p[i] > p[j]:
                    sign = -sign
        term = (Fr(1), Fr(0))
        for i in range(k):
            term = mul(term, M[i][perm[i]])
        total = add(total, term) if sign > 0 else sub(total, term)
    return total


def main():
    out = instance()
    if out is None:
        print('没有找到合适的 L0')
        return
    A, C, L0 = out
    Q = Qm.Quotient(A, C)
    d = Q.d
    B = Q.B
    print(f"n={n}, j={Q.j}, d={d}, dim B={len(B)}")
    W0 = rb([Q.pi(r) for r in L0] + [Q.pi(mm([r], A)[0]) for r in L0])
    print(f"dim W0 = {len(W0)}; rank[W0;B] = {rank([r[:] for r in W0] + [r[:] for r in B])}")
    if d != 5 or len(B) != 2 or len(W0) != 2:
        print("（实例不符合 d=5、dim B=2、dim W0=2）")
        return
    if rank([r[:] for r in W0] + [r[:] for r in B]) != 4:
        print("（W0 ∩ B ≠ 0，走另一分支）")
        return

    b1, b2 = B[0], B[1]
    w1, w2 = W0[0], W0[1]
    # f(u) = pi(lift(u) A)，对 u = b1, b2, w1, w2
    def f(u):
        return Q.pi(mm([Q.lift(u)], A)[0])

    fb1, fb2, fw1, fw2 = f(b1), f(b2), f(w1), f(w2)

    # 需要零的所有 5x5 子式：矩阵行 = [w1, w2, L(t), B..., f(u)]
    # L(t) = b1 + t b2；f(L(t)) = fb1 + t fb2
    def rows_for(u, fu):
        if u is None:      # u = L(t)
            rows = []
            rows.append([(w1[i], Fr(0)) for i in range(d)])
            rows.append([(w2[i], Fr(0)) for i in range(d)])
            rows.append([(b1[i], b2[i]) for i in range(d)])
            for b in B:
                rows.append([(b[i], Fr(0)) for i in range(d)])
            rows.append([(fu[0][i], fu[1][i]) for i in range(d)])
            return rows
        else:
            rows = []
            rows.append([(w1[i], Fr(0)) for i in range(d)])
            rows.append([(w2[i], Fr(0)) for i in range(d)])
            rows.append([(b1[i], b2[i]) for i in range(d)])
            for b in B:
                rows.append([(b[i], Fr(0)) for i in range(d)])
            rows.append([(fu[i], Fr(0)) for i in range(d)])
            return rows

    # 对每个 u（3 个：w1, w2, L(t)），把全部 5x5 子式 = 一次多项式；收集所有系数
    polys = []
    for u, fu in [(w1, fw1), (w2, fw2), (None, (fb1, fb2))]:
        R = rows_for(u, fu)
        for rs in itertools.combinations(range(len(R)), d):
            for cs in itertools.combinations(range(d), d):
                M = [[R[i][k] for k in cs] for i in rs]
                if len(M) != len(M[0]):
                    continue
                c0, c1 = det_affine(M)
                if c0 != 0 or c1 != 0:
                    polys.append((c0, c1))
    print(f"非零子式个数 = {len(polys)}（每个是 c0 + c1·t）")

    # 求公共解：c0 + c1 t = 0 对所有子式
    cons = [p for p in polys]
    # 先看 t=0 与 t=1 是否同时为零
    zero_at_0 = all(c0 == 0 for c0, c1 in cons)
    zero_at_1 = all(c0 + c1 == 0 for c0, c1 in cons)
    if zero_at_0 and zero_at_1:
        print("=> 所有子式在 t=0 与 t=1 都为零 ⟹ 线性 ⟹ 对所有 t 为零 ⟹ (N) 对所有 L 成立")
        print("   => P2 = YES ✓（任取一条线）")
        return
    # 否则找唯一候选 t
    cand = None
    for c0, c1 in cons:
        if c1 != 0:
            t = -c0 / c1
            if cand is None:
                cand = t
            elif cand != t:
                print("=> 两个子式给出不同的 t ⟹ 无公共解 ⟹ P2 = NO ✗")
                return
    if cand is None:
        print("=> 有子式恒不为零 ⟹ P2 = NO ✗")
        return
    ok = all(c0 + c1 * cand == 0 for c0, c1 in cons)
    print(f"=> 唯一候选 t = {cand}；代入全部子式：{'全为零 ✓' if ok else '不全为零 ✗'}")
    print("   => P2 =", "YES ✓" if ok else "NO ✗")


if __name__ == '__main__':
    main()
