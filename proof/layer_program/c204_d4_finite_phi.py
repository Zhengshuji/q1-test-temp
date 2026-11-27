r"""$d=4$ 的**可行 $\varphi$ 只有有限个**：把 $(N)$ 化成"转移映射"的特征问题。

设 $\varphi\in B^{\perp}$（$\dim B=1$ ⟹ 这就是 $\mu\ge1$ 的轨迹）、$\mathcal U=\ker\varphi$。$(N)$ 等价于
$$\forall u\in\mathcal U:\ \varphi(\pi(uA))=0
\iff \psi:=\Phi(\varphi)\in\operatorname{span}\{\varphi\},\qquad \Phi(\varphi)(u):=\varphi(\pi(uA)).$$
$\Phi$ 在 $B^{\perp}$ 上良定义（$\varphi$ 杀掉 $B$）。写 $X^*=B^{\perp}\oplus\langle\theta\rangle$（$\theta(b)=1$）、
$\Phi(\varphi)=\Phi_1(\varphi)+c(\varphi)\theta$。则

$$\varphi\ \text{可行}\iff c(\varphi)=0\ \text{且}\ \Phi_1(\varphi)=\lambda\varphi\ (\exists\lambda).$$

$c$ 是**线性**泛函 ⟹ $\ker c\subseteq B^{\perp}$ 是 2 维（$\mathbb P^1$）；$\Phi_1|_{\ker c}$ 是 2 维映射
⟹ 特征方向**至多 2 个**（$\Phi_1|_{\ker c}=\lambda\mathrm{id}$ 时整条线，退化）。

$$\boxed{\ d=4,\ \dim B=1\ \Longrightarrow\ \text{可行 }\varphi\ \text{至多 2 个（退化时一条射影线）}\ }$$

用法：python proof/layer_program/c204_d4_finite_phi.py
"""
import math
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'proof', 'rho1_layer'))
sys.path.insert(0, _HERE)

import audit_independent as AI
import importlib.util as iu

spec = iu.spec_from_file_location('Q', os.path.join(_ROOT, 'proof', 'rho1_layer', 'quotient_selfcheck.py'))
Qm = iu.module_from_spec(spec)
spec.loader.exec_module(Qm)
spec2 = iu.spec_from_file_location('C202', os.path.join(_HERE, 'c202_d4_spectral_scan.py'))
C202 = iu.module_from_spec(spec2)
spec2.loader.exec_module(C202)

mm, rank, rb = Qm.mm, Qm.rank, Qm.rb

N = 7
A_MAT = [[0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 1]]
C_MAT = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]


def solve(M, rhs):
    R = AI.rref([list(M[i]) + [rhs[i]] for i in range(len(M))])[0]
    n = len(M[0])
    x = [Fr(0)] * n
    for row in R:
        piv = next((t for t in range(n) if row[t] != 0), None)
        if piv is None:
            if row[n] != 0:
                return None
            continue
        x[piv] = row[n] / row[piv]
    return x


def main():
    A = [[Fr(x) for x in r] for r in A_MAT]
    C = [[Fr(x) for x in r] for r in C_MAT]
    Q = Qm.Quotient(A, C)
    d = Q.d
    print(f'n={N}、j={Q.j}、d={d}、dim B={len(Q.B)}')
    if d != 4 or len(Q.B) != 1:
        print('本脚本只处理 d=4、dim B=1'); return
    b = Q.B[0]
    e = [[Fr(1) if t == i else Fr(0) for t in range(d)] for i in range(d)]
    fv = [Q.pi(mm([Q.lift(ei)], A)[0]) for ei in e]        # f(e_i)
    Bperp = rb(AI.nullspace([b]))                          # {φ : φ·b = 0}
    print(f'B^⊥ 的基：{[[str(x) for x in r] for r in Bperp]}')
    if len(Bperp) != 3:
        print('B^⊥ 维数 != 3'); return
    Phi = [[sum(Bperp[j][i] * fv[k][i] for i in range(d)) for k in range(d)] for j in range(3)]
    fb = Q.pi(mm([Q.lift(b)], A)[0])
    c = [sum(Bperp[j][i] * fb[i] for i in range(d)) for j in range(3)]
    print(f'c（θ 分量）= {[str(x) for x in c]}')
    # ker c ⊆ B^⊥
    xs = AI.nullspace([c]) if any(c) else e[:2]
    Kc = [[sum(x[j] * Bperp[j][k] for j in range(3)) for k in range(d)] for x in xs]
    print(f'ker c 的基（{len(Kc)} 个）')
    if len(Kc) != 2:
        print('ker c 不是 2 维（退化情形，整条线）'); return
    # θ：任一 b_k ≠ 0 的单位泛函
    theta = None
    for i in range(d):
        if b[i] != 0:
            theta = [Fr(0)] * d
            theta[i] = Fr(1) / b[i]
            break
    # Φ_1 在 B^⊥ 基下的 3×3 矩阵：Φ(Bperp_j) - c_j θ = Σ_i A3[i][j] Bperp_i
    A3 = [[None] * 3 for _ in range(3)]
    for j in range(3):
        psi = [Phi[j][k] - c[j] * theta[k] for k in range(d)]
        y = solve([[Bperp[i][k] for i in range(3)] for k in range(d)], psi)
        if y is None:
            print('Φ_1 不在 B^⊥ 里（不该发生）'); return
        for i in range(3):
            A3[i][j] = y[i]
    print(f'Φ_1 在 B^⊥ 基下：{[[str(x) for x in r] for r in A3]}')
    # ker c 在 B^⊥ 坐标里的基（x ∈ Q^3：c·x = 0）
    xs = AI.nullspace([c]) if any(c) else AI.nullspace([[Fr(0)] * 3])
    xs = rb(xs)
    print(f'ker c（B^⊥ 坐标）：{[[str(x) for x in r] for r in xs]}')
    if len(xs) != 2:
        print('ker c 不是 2 维：退化（整条线）'); return
    import sympy as sp
    a_, b_ = sp.symbols('a b')
    # x = a*xs[0] + b*xs[1]
    xv = [sp.Rational(xs[0][k].numerator, xs[0][k].denominator) * a_ +
          sp.Rational(xs[1][k].numerator, xs[1][k].denominator) * b_ for k in range(3)]
    M3 = sp.Matrix([[sp.Rational(A3[i][j].numerator, A3[i][j].denominator) for j in range(3)] for i in range(3)])
    # Φ_1(φ) 的坐标 = M3 * x（列约定：第 j 列 = Φ(Bperp_j) 的坐标）
    yv = [sum(M3[i, j] * xv[j] for j in range(3)) for i in range(3)]
    quads = []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        quads.append(sp.expand(yv[i] * xv[j] - yv[j] * xv[i]))
    print(f'二次型：[{[str(q) for q in quads]}]')
    g = sp.Poly(quads[0], a_, b_)
    for q in quads[1:]:
        g = sp.gcd(g, sp.Poly(q, a_, b_))
    print(f'gcd（作为二元齐次多项式）= {g.as_expr()}')
    sols = sp.solve([sp.Eq(q, 0) for q in quads], [a_, b_], dict=True)
    print(f'解（a,b）：{sols}')
    cands = []
    for sd in sols:
        av = sp.simplify(sd.get(a_, a_)); bv = sp.simplify(sd.get(b_, b_))
        # 解是一个方向：把自由的那个参数归一化为 1
        if av.free_symbols and not bv.free_symbols and bv == 0:
            av = sp.Integer(1)
        elif bv.free_symbols and not av.free_symbols and av == 0:
            bv = sp.Integer(1)
        if av.free_symbols or bv.free_symbols:
            continue
        x = [sum(sp.Rational(av) * sp.Rational(xs[0][k].numerator, xs[0][k].denominator) +
                 sp.Rational(bv) * sp.Rational(xs[1][k].numerator, xs[1][k].denominator)
                 for _ in [0]) for k in range(3)]
        # φ = Σ x_j Bperp_j
        phi = [Fr(0)] * d
        for k in range(d):
            phi[k] = sum(Fr(int(sp.nsimplify(x[j]).p), int(sp.nsimplify(x[j]).q)) * Bperp[j][k] for j in range(3))
        cands.append((av, bv, phi))
    print(f'候选：{len(cands)} 个')
    for av, bv, phi in cands:
        if not any(phi):
            continue
        D = C202.cell_data(Q, A, phi)
        why = 'ok' if (D and D.get('reason') == 'ok') else (None if not D else D.get('reason'))
        extra = f'、covered={C202.covered(D["T"], D["w"])}' if why == 'ok' else ''
        print(f'  (a,b)=({av},{bv})、φ={[str(x) for x in phi]} ⟹ {why}{extra}')
    print('\n结论：可行 φ 由"ker c 上的二次型组"决定（P^1 上有限个解，或在退化时整条线）⟹ 谱步是有限计算 ✓')


if __name__ == '__main__':
    main()

