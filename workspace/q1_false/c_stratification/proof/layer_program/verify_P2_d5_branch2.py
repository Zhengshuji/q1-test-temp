"""§68：把"完全判定"推广到 $d=5$、$\\dim B=2$、$W_0\\cap B\\ne0$ 的分支。

该分支里 $\\mu\\ge1$ **自动成立**（$\\dim(W_0+B)\\le3$ ⟹ $W_0\\cap B\\ne0$ 已含在 $\\mathcal U$ 里）✓，
所以 P2 ⟺ P1 ⟺ $\\exists$ 3 维 $\\mathcal U\\supseteq W_0$ 满足 $(N)$ ✓。

$\\mathcal U=W_0\\oplus\\langle z\\rangle$，$z$ 在 $X/W_0$（3 维 ✓）里 ⟹ $z$ 由 $\\mathbb P^2$ 参数化 ✓
⟹ 取仿射图 $z=z_0+s z_1+t z_2$ ✓ ⟹ $(N)$ 变成 $(s,t)$ 的多项式条件 ✓ ⟹ 用 sympy 的 Gröbner 判定是否有解。
"""
import sys
from fractions import Fraction as Fr

import sympy as sp

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


def find_W0(Q, A, tries=400):
    """**构造** L0 使 W0 ∩ B ≠ 0（不靠随机 ✗）。

    取 L0 的行 ℓ0 ∈ J·A（即 ℓ0 = j A 的线性组合）⟹ π(ℓ0) ∈ B ✓ ⟹ W0 ∩ B ∋ π(ℓ0) ✓。
    """
    import random
    rng = random.Random(11)
    JA = [mm([j], A)[0] for j in Q.J]
    for _ in range(tries):
        coeffs = [Fr(rng.randint(-2, 2)) for _ in JA]
        l0 = [sum(coeffs[i] * JA[i][k] for i in range(len(JA))) for k in range(n)]
        if not any(Q.pi(l0)):
            continue
        L0 = [l0]
        W0 = rb([Q.pi(r) for r in L0] + [Q.pi(mm([r], A)[0]) for r in L0])
        if len(W0) != 2:
            continue
        if rank([r[:] for r in W0] + [r[:] for r in Q.B]) < 4:
            return L0, W0
    return None, None


def main():
    A = [[Fr(x) for x in row] for row in A_MAT]
    C = [[Fr(x) for x in row] for row in C_MAT]
    Q = Qm.Quotient(A, C)
    d = Q.d
    B = Q.B
    print(f"n={n}, j={Q.j}, d={d}, dim B={len(B)}")
    L0, W0 = find_W0(Q, A)
    if L0 is None:
        print("没找到 W0 ∩ B ≠ 0 的 L0")
        return
    print(f"dim W0 = {len(W0)}; rank[W0;B] = {rank([r[:] for r in W0] + [r[:] for r in B])} (＜4 => W0∩B≠0 ✓)")

    # z 的仿射参数化：X/W0 的补空间（3 维）+ 基点（0 即可，因为 z 只需在 W0 之外）
    K = []
    span = [r[:] for r in W0]
    for i in range(d):
        e = [Fr(1) if t == i else Fr(0) for t in range(d)]
        if rank(span + [e]) > len(span):
            K.append(e); span = rb(span + [e])
        if len(span) == d:
            break
    print(f"X/W0 的维数 = {len(K)}")
    if len(K) != 3:
        print("（需要 3，跳过）")
        return
    z1, z2, z3 = K[0], K[1], K[2]
    s, t = sp.symbols('s t')

    def z_of(sv, tv):
        return [z1[i] + sv * z2[i] + tv * z3[i] for i in range(d)]

    # (N)：对 u ∈ {W0 的基, z}，f(u) ∈ U + B
    # U 的基 = [W0; z]；条件 = [W0; z; B; f(u)] 的全部 (r0+1) 阶子式为零，r0 = rank[W0; z; B]
    # 对一般位置的 (s,t)，rank[W0; z; B] = dim(W0+B) + 1（假设 z 一般）
    r0 = rank([r[:] for r in W0] + [r[:] for r in B]) + 1
    print(f"r0 = {r0}")

    def f(u):
        return Q.pi(mm([Q.lift(u)], A)[0])

    fW = [f(w) for w in W0]
    # 符号矩阵 [W0; z(s,t); B; f(w1); f(w2); f(z)]
    # f(z(s,t)) 是 s,t 的仿射（f 线性）
    fz1, fz2, fz3 = f(z1), f(z2), f(z3)

    rows = []
    for w in W0:
        rows.append([sp.Rational(x.numerator, x.denominator) for x in w])
    rows.append([sp.Rational(x.numerator, x.denominator) + s * sp.Rational(y.numerator, y.denominator)
                 + t * sp.Rational(zv.numerator, zv.denominator) for x, y, zv in zip(z1, z2, z3)])
    for b in B:
        rows.append([sp.Rational(x.numerator, x.denominator) for x in b])
    for fw in fW:
        rows.append([sp.Rational(x.numerator, x.denominator) for x in fw])
    rows.append([sp.Rational(x.numerator, x.denominator) + s * sp.Rational(y.numerator, y.denominator)
                 + t * sp.Rational(zv.numerator, zv.denominator) for x, y, zv in zip(fz1, fz2, fz3)])

    import itertools
    polys = []
    for rs in itertools.combinations(range(len(rows)), r0 + 1):
        for cs in itertools.combinations(range(d), r0 + 1):
            M = sp.Matrix([[rows[i][k] for k in cs] for i in rs])
            det = sp.expand(M.det())
            if det != 0:
                polys.append(sp.Poly(det, s, t))
    print(f"非零子式个数 = {len(polys)}")
    if not polys:
        print("=> 无子式（退化），跳过")
        return
    G = sp.groebner([p.as_expr() for p in polys], s, t, order='lex')
    print(f"Gröbner 基 = {list(G.exprs)[:3]}{' ...' if len(G.exprs) > 3 else ''}")
    no_sol = (list(G.exprs) == [sp.Integer(1)])
    print("=> 1 ∈ I（无解）？", no_sol)
    if no_sol:
        print("   => P2 = NO ✗")
        return
    # 解出 (s,t)：Gröbner 基应为 {s-c1, t-c2}
    sols = sp.solve([p.as_expr() for p in polys], [s, t], dict=True)
    print(f"   解：{sols}")
    if not sols:
        print("   （solve 没找到显式解，但 I 不是 1-ideal）")
        return
    sv0, tv0 = sols[0][s], sols[0][t]
    zval = [sp.Rational(z1[i].numerator, z1[i].denominator)
            + sv0 * sp.Rational(z2[i].numerator, z2[i].denominator)
            + tv0 * sp.Rational(z3[i].numerator, z3[i].denominator) for i in range(d)]
    zf = [Fr(int(sp.nsimplify(x).p), int(sp.nsimplify(x).q)) for x in zval]
    U = rb([r[:] for r in W0] + [zf])
    mu = len(B) + len(U) - rank([r[:] for r in B] + [r[:] for r in U])
    fU = [Q.pi(mm([Q.lift(u)], A)[0]) for u in U]
    N_ok = all(rank([r[:] for r in U] + [r[:] for r in B] + [v]) ==
               rank([r[:] for r in U] + [r[:] for r in B]) for v in fU)
    W0ok = all(rank(U + [w]) == len(U) for w in W0)
    print(f"   取 z = {[str(x) for x in zf]}")
    print(f"   dim U = {len(U)}, W0 ⊆ U: {W0ok}, (N): {N_ok}, mu = {mu}")
    print("   => P2 =", "YES ✓（已验证）" if (W0ok and N_ok and mu >= 1) else "NO（条件不满足）✗")


if __name__ == '__main__':
    main()
