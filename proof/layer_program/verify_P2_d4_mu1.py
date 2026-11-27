"""§63 的落地：$d=4$、$\\dim B=1$ 时 P2 的判定（有限维特征向量问题）。

$d=4$ 时 $\\mathcal U=\\phi^{\\perp}$（$\\phi\\in X^*$，$\\phi\\ne0$）。
$\\dim B=1$ 时要 $\\mu=1$ 必须 $B\\subseteq\\mathcal U$，即 $\\phi\\perp B$。
此时 $(N)\\iff\\phi\\circ f\\parallel\\phi$（$\\phi$ 已下降到 $X/B$，故 $\\phi\\circ f$ 良定义）。

本脚本：
  1. 造一个 $d=4$、$\\dim B=1$ 的实例；
  2. 在 $\\{\\phi:\\ \\phi|_B=0,\\ \\phi(u_0)=\\phi(u_0A)=0\\}$ 里解广义特征问题 $\\phi f=\\lambda\\phi$；
  3. 若找到，构造 $\\mathcal U=\\phi^\\perp$ 并**逐项**核验 A1–A3、A6、$\\mu=1$ —— 即 P2 = YES。
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

n = 6


def build():
    """§55 的"好"实例（d=4, dim B=1）。"""
    A = [[Fr(0)] * n for _ in range(n)]
    A[0][1] = Fr(1); A[1][2] = Fr(1); A[2][0] = Fr(3); A[2][1] = Fr(2); A[2][2] = Fr(1)
    A[3][3] = Fr(1)
    A[4][5] = Fr(1)
    A[5][0] = Fr(1); A[5][4] = Fr(1)
    C = [[Fr(-1), Fr(-2), Fr(0), Fr(0), Fr(0), Fr(-1)]]
    L0 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1), Fr(0)]]
    return A, C, L0


def main():
    A, C, L0 = build()
    Q = Qm.Quotient(A, C)
    d = Q.d
    muB = len(Q.B)
    print(f"n={n}, j={Q.j}, d={d}, dim B={muB}")
    if d != 4 or muB != 1:
        print("（这个实例不是 d=4、dim B=1，换个实例再试）")
        return

    # X 的坐标 -> C^n 的 lift、pi 都是 Q 提供的
    # 构造 "φ ↦ φ∘f" 的矩阵：以 X^* 的标准基 e_i^* 为基
    # φ = (φ_0..φ_{d-1})，作用在 X 坐标上
    # (φ∘f)(x) = φ( f(x) )，其中 f(x) = π(lift(x) A) ∈ X
    dX = d
    # e_i^*∘f 的坐标：对每个 j，取值 = e_i^*( f(e_j) )
    Fcols = []           # Fcols[j] = f(e_j) 在 X 里的坐标
    for j in range(dX):
        ej = [Fr(1) if t == j else Fr(0) for t in range(dX)]
        Fcols.append(Q.pi(mm([Q.lift(ej)], A)[0]))
    # (φ∘f) = φ^T · M，其中 M[i][j] = f(e_j)[i]  =>  M 是 d×d
    M = [[Fcols[j][i] for j in range(dX)] for i in range(dX)]

    def phi_of(coeffs):
        """把 φ 的坐标向量当行向量，返回 φ^T M（= φ∘f 的坐标）"""
        return [sum(coeffs[i] * M[i][j] for i in range(dX)) for j in range(dX)]

    # 约束：φ ⊥ B，φ(u0)=0，φ(u0A)=0
    u0 = Q.pi(L0[0])
    u0A = Q.pi(mm([L0[0]], A)[0])
    cons = [list(b) for b in Q.B]
    if any(u0):
        cons.append(list(u0))
    if any(u0A):
        cons.append(list(u0A))
    # 解 cons · φ = 0 的空间
    ns = AI.nullspace(cons)
    phi_space = rb(ns) if ns else []
    print(f"可行的 φ 空间维数 = {len(phi_space)}")
    if not phi_space:
        print("=> 没有满足 A2/A3 且 φ⊥B 的 φ ⟹ 该通道 P2 = NO")
        return

    # 在 phi_space 上找 φ 使 φ∘f = λφ（广义特征问题）
    # 取 ϕ = Σ c_k phi_space[k]，要求 φ f ∥ φ
    # 等价：rank[φ ; φ f] = 1
    found = None
    # 先试：φ f 属于 span(φ)  <=>  对每个基向量，φ f 与 φ 成比例
    # 用小范围有理数搜索系数 c
    rng_range = [Fr(k) for k in range(-3, 4)]
    for coeffs in itertools.product(rng_range, repeat=len(phi_space)):
        if not any(coeffs):
            continue
        phi = [sum(coeffs[k] * phi_space[k][i] for k in range(len(phi_space))) for i in range(dX)]
        phif = phi_of(phi)
        if rank([phi, phif]) <= 1:
            found = (coeffs, phi)
            break
    if found is None:
        print("=> 在小范围系数里没找到特征向量（可能解在更大的系数上，或 P2 = NO）")
        return

    coeffs, phi = found
    print(f"找到 φ（系数 {[str(c) for c in coeffs]}）: {[str(x) for x in phi]}")
    U = rb(AI.nullspace([phi]))
    print(f"U = ker φ，dim = {len(U)}")
    # 逐项核验
    mu = len(Q.B) + len(U) - rank([r[:] for r in Q.B] + [r[:] for r in U])
    fU = [Q.pi(mm([Q.lift(u)], A)[0]) for u in U]
    N_ok = all(rank([r[:] for r in U] + [r[:] for r in Q.B] + [v]) == rank([r[:] for r in U] + [r[:] for r in Q.B]) for v in fU)
    A2 = (not any(u0)) or rank(U + [u0]) == len(U)
    A3 = (not any(u0A)) or rank(U + [u0A]) == len(U)
    print(f"  A2 (u0 ∈ U) = {A2};  A3 (u0A ∈ U) = {A3};  (N) = {N_ok};  mu = {mu}")
    print("=> P2 =", "YES ✓" if (A2 and A3 and N_ok and mu >= 1) else "NO（有条件不满足）")


if __name__ == '__main__':
    main()
