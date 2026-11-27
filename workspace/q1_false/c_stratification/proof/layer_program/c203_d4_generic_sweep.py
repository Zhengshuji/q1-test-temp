r"""⚠️ 反面记录（2026-10-30）：**"$X/B$ 的不变子空间" ≠ "$B$-条件不变的 $\mathcal U$"** ✗

尝试（$d=4$、$\dim B=1$，见 [SPECTRAL_STEP_DESIGN.md](SPECTRAL_STEP_DESIGN.md) 观察 B）：
把"$\mu\ge1$ 且 $(N)$"的格子按 $f$ 在 $X/B$ 上的特征向量枚举：
$$\mathcal U=\ker\big(x\mapsto\psi(x\bmod B)\big),\qquad \psi M=\lambda\psi .$$

**障碍**：$f:X\to X/B$ **不下降到 $X/B$**，除非 $f(B)\subseteq B$。因此
$$\mathcal U\ \text{满足}\ (N)\iff \psi\ \text{是 }M\text{ 的特征向量}\ \textbf{并且}\ f(B)\subseteq B .$$
本脚本在小例上把这件事**算出来**：$f(B)\not\subseteq B$ 时，$\psi$ 的第二坐标 $\ne0$ 的候选**全部 $(N)$ 失败**。

**正确的对象**是"余维 1、含 $B$ 的条件不变子空间"（conditioned invariant）——即
[../layer_31_theorems/edci.md](../layer_31_theorems/edci.md) 与经典文献（Warren–Eckberg / Wonham）的对象。

用法：python proof/layer_program/c203_d4_generic_sweep.py
"""
import itertools
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
# J = <e1,e2,e3>（e1A=e3, e2A=0）；B = <e4>（e3A=e4）；
# f 在 X 上：e4↦e4+e6、e5↦e5、e6↦e6+e7、e7↦e7  ⟹ f(B) = e4+e6 ⊄ B
A_MAT = [[0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 1]]
C_MAT = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
L0_MAT = [[0, 0, 0, 0, 1, 0, 0]]


def main():
    A = [[Fr(x) for x in r] for r in A_MAT]
    C = [[Fr(x) for x in r] for r in C_MAT]
    Q = Qm.Quotient(A, C)
    print(f'n={N}、j={Q.j}、d={Q.d}、dim B={len(Q.B)}')
    b = Q.B[0]
    # f: X→X 的矩阵（行约定）
    F = [Q.pi(mm([Q.lift([Fr(1) if t == i else Fr(0) for t in range(Q.d)])], A)[0])
         for i in range(Q.d)]
    fB = Q.pi(mm([Q.lift(b)], A)[0])          # f(B 的生成元)
    print(f'f(B) = {[str(x) for x in fB]}；f(B) ⊆ B ? {rank([b, fB]) == rank([b])}')
    # 取 B 的补 K，做 f 的"下降"矩阵 M（只有在 f(B)⊆B 时才有意义）
    K = []
    for i in range(Q.d):
        e = [Fr(1) if t == i else Fr(0) for t in range(Q.d)]
        if rank(K + [b] + [e]) > len(K) + 1:
            K.append(e)
    basis_mat = K + [b]
    Binv = AI.inv([[basis_mat[i][k] for k in range(Q.d)] for i in range(Q.d)])

    def to_quotient(v):
        # v ∈ X；返回 (K 坐标, b 系数)
        sol = [sum(v[i] * Binv[k][i] for i in range(Q.d)) for k in range(Q.d)]
        return sol[:len(K)], sol[len(K)]

    M = []
    for col in K:
        M.append(to_quotient([sum(col[i] * F[i][k] for i in range(Q.d)) for k in range(Q.d)])[0])
    import sympy as sp
    Ms = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in M])
    lam = sp.symbols('lam')
    print(f'f 诱导的 M（在 X/B 的坐标里）= {Ms.tolist()}')
    print(f'char poly = {sp.factor(Ms.charpoly(lam).as_expr())}')
    ns = (Ms - sp.eye(len(K))).nullspace()
    print(f'λ=1 的特征向量：{len(ns)} 维')
    okN = badN = 0
    for vec in ns:
        psi = [Fr(int(v.p), int(v.q)) for v in vec]
        rhs = list(psi) + [Fr(0)]
        phi = [sum(rhs[i] * Binv[k][i] for i in range(Q.d)) for k in range(Q.d)]
        D = C202.cell_data(Q, A, phi)
        why = 'ok' if (D and D.get('reason') == 'ok') else (None if not D else D.get('reason'))
        print(f'  ψ={[str(x) for x in psi]} ⟹ 格子 {why}')
        if why == 'ok':
            okN += 1
        else:
            badN += 1
    print()
    print(f'结论：{okN} 个候选满足 (N)、{badN} 个失败。')
    print('     f(B) ⊄ B ⟹ M 不是 f 的"下降"，特征向量给的 U 一般不满足 (N) —— 这条路不成立 ✗')
    print('     正确对象：余维 1、含 B 的条件不变子空间（EDCI 的对象）✓')


if __name__ == '__main__':
    main()
