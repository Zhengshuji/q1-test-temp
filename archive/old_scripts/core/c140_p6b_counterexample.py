r"""
c140_p6b_counterexample.py -- P6b 的反例（可复核）

P6b（`OPEN_PROBLEM.md` P6b / `RESULTS.md` §2.8）断言：
    $$\mathcal A\mathcal A'\subseteq\mathcal A\ \Longrightarrow\ (b)\ \text{必败}$$
其中 $\mathcal A=\operatorname{row}(\mathcal L N)$，$A'=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$。

本文件给出一个**反例**（$n=5,\ p=1,\ r=1,\ q=3,\ \rho=2$）：
    H1–H3 ✓、$\mathcal A\mathcal A'\subseteq\mathcal A$ ✓、(5a) ✓、(5b) ✓。

判据一律用**原始**形式（不经过 $(A)$/$(S)$ 归约）：
    (5a)  rank[LA; L; CA; C] == rank[L; CA; C]
    (5b)  [λL-LA; CA; C] 的所有 r0 阶子式的 gcd 为**非零常数**（r0 = rank[L;CA;C]）

实现：sympy（与项目库、与 audit_independent.py 都无关 —— 第三套实现）。
跑法：python scripts/core/c140_p6b_counterexample.py
"""
import itertools
import sympy as sp

# ---------------- 见证（固定数据，来自 c139 的 seed 18） ----------------
A = sp.Matrix([[-1, -1, 1, 0, 0],
               [-1, -1, 0, 1, 0],
               [-1, 0, 0, 0, 0],
               [-1, 0, 1, -1, 0],
               [1, 1, -1, -1, -1]])
C = sp.Matrix([[-1, -1, 1, 0, 1]])
L0 = sp.Matrix([[1, -1, 1, 0, -1]])
L = sp.Matrix([[1, -1, 1, 0, -1],
               [1, -1, 2, -2, 0],
               [-1, -2, 1, 1, 1]])


def main():
    lam = sp.symbols("l")
    CA = C * A
    LA = L * A

    print("=" * 72)
    print("0. 假设 H1–H3")
    print(f"   rank C = {C.rank()} (H1, p=1)   rank L0 = {L0.rank()} (H2, r=1)"
          f"   rank[L0;C] = {sp.Matrix.vstack(L0, C).rank()} (H3)")

    base = sp.Matrix.vstack(L, CA, C)
    r0 = base.rank()
    print(f"   r0 = rank[L;CA;C] = {r0}")

    print("=" * 72)
    print("1. (5a)： rank[LA;L;CA;C] == rank[L;CA;C]")
    lhs = sp.Matrix.vstack(LA, L, CA, C).rank()
    print(f"   {lhs} == {r0}  ->  {lhs == r0}")

    print("=" * 72)
    print("2. (5b)： 所有 r0 阶子式的 gcd 为非零常数")
    P = sp.Matrix.vstack(lam * L - LA, CA, C)
    minors = []
    for rs in itertools.combinations(range(P.rows), r0):
        for cs in itertools.combinations(range(P.cols), r0):
            m = sp.expand(P.extract(rs, cs).det())
            if m != 0:
                minors.append(m)
    g = sp.gcd_list(minors)
    print(f"   非零 r0 阶子式 {len(minors)} 个；gcd = {sp.factor(g)}"
          f"  -> 常数: {bool(g.is_number and g != 0)}")

    print("=" * 72)
    print("3. 归约量： N, A', R0, M, F, rho")
    N = sp.Matrix.hstack(*sp.Matrix.vstack(C, CA).nullspace())
    Ap = (N.T * N).inv() * N.T * A * N
    R0 = A * N - N * Ap
    M = L * N
    F = L * A * N
    al, be = L0 * N, L0 * A * N
    print(f"   d = {N.cols},  rho = rank M = {M.rank()}")
    print(f"   alpha0 = {list(al)},  beta0 = {list(be)}")
    print(f"   A = row[alpha0;beta0], dim = {sp.Matrix.vstack(al, be).rank()}")

    print("=" * 72)
    print("4. P6b 的前提： A A' ⊆ A ?")
    BasisA = sp.Matrix.vstack(al, be)
    aug = sp.Matrix.vstack(BasisA, al * Ap, be * Ap)
    print(f"   dim(A + A A') = {aug.rank()}  (等于 dim A = {BasisA.rank()} 即 A A' ⊆ A)")

    print("=" * 72)
    print("5. 结论")
    ok = (lhs == r0) and bool(g.is_number and g != 0) and (aug.rank() == BasisA.rank())
    print(f"   (5a) ✓, (5b) ✓, A A' ⊆ A ✓  ==>  P6b 不成立：{ok}")
    print("   （P6b 的证明只说明『取 lift=0』那一个选择必败；")
    print("     但 lift 并不是自由的：首行被 L0 钉死，L0R0 ≠ 0。）")


if __name__ == "__main__":
    main()
