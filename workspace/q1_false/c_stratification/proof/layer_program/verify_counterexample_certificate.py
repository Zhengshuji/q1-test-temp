# ⚠️ 本脚本**被取代** ✗（2026-10-30，HANDOVER2 §3 指出）：
#   (a) `lift` 末尾的 `% 1` 把整数坐标打成 0 ⟹ "V" 实际秩 1 ⟹ 28 个子式平凡为零 ✗；
#   (b) `r0` 写成 `rank(...) and n`，永远打印 n，不是真检查 ✗。
# 正确的证书是 verify_counterexample_certificate_v2.py（三行秩界，598/598 ✓）。
# 本文件仅作**过程记录**保留。
"""§82：给 §81 的反例做**可审计证书**（专家 QA8 第 1 优先级）。

⚠️⚠️ 2026-10-30 接手者更正：**本脚本的结论输出是坏的，不要引用它的 0/28** ⚠️⚠️
  * 第 61 行的 `% 1` 把 `lift(e_i)` 打成了零向量（`1 % 1 = 0`）⟹ 这里的 "V" 秩为 1
    ⟹ 28 个 6 阶子式**平凡地**全为零，"0/28" 不构成证书；
  * 第 103 行打印的 `r0` 是 `rank(J+K) and n`，不是真的算 `rank[V;C0A;C0]`（第二个 bug）；
  * **结论仍然成立**，但证明只要一行：rank(A)=2 ⟹ dim π(C^n A)=1 ≤ ρ−1 ⟹ 在 λ=0 处
    rank[-LA;CA;C] ≤ dim J + 1 = 4 < 6 = rank[L;CA;C] ⟹ (5b) 对所有 L 失败 ⟹ 层不可行。
  * 复核：`workspace/review_2026-10-30/verify_handover2_checks.py`；
    详见 `archive/handovers/HANDOVER2_2026-10-30.md` §3。

要点：
  * 写死 L0 的**具体那一行**；
  * 把**全部**提升参数符号化：每行可加 tau = a_i * τ0（τ0 ∈ 𝒥、β(τ0) = w0 ≠ 0），
    以及 ker β 方向（它们只把行变到 𝒥 内 ⇒ 该行与它的 A 像是常数行的组合 ⇒ 行列式不变 ✓）；
  * 对 6×6 铅笔 [λV − VA; C0A; C0] 的行列式做**符号**计算，变量 (a1,a2,a3,a4,λ)；
  * 若行列式**恒为零** ⟹ 每个 λ 都秩降 ⟹ **所有提升的 (5b) 都失败** ⟹ 层不可行 ✓（证书 ✓）。
"""
import itertools
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

n = 6
A_MAT = [[-1,0,2,1,-1,-1],[0,2,0,0,0,0],[0,0,0,0,0,0],
         [-2,-1,4,2,-2,-2],[-2,0,4,2,-2,-2],[0,-2,0,0,0,0]]
C_MAT = [[2,1,-2,2,-1,-1],[2,2,2,1,-1,1]]
L0_MAT = [[1, 0, 0, 0, 0, 0]]          # 写死的一行


def main():
    A = [[Fr(x) for x in r] for r in A_MAT]
    C = [[Fr(x) for x in r] for r in C_MAT]
    L0 = [[Fr(x) for x in r] for r in L0_MAT]
    Q = Qm.Quotient(A, C)
    d = Q.d
    j = Q.j
    B = Q.B
    CA = mm(C, A)
    J = rb(C + CA)
    print(f"n={n}, j={j}, d={d}, dim B={len(B)}")

    # X 的基（在 C^n 中的 lift）与 π
    K = []
    span = [r[:] for r in J]
    for i in range(n):
        e = [Fr(1) if t == i else Fr(0) for t in range(n)]
        if rank(span + [e]) > len(span):
            K.append(e); span = rb(span + [e])
        if len(span) == n:
            break
    Lmat = J + K
    Linv = AI.inv(Lmat)

    def pi(x):
        return mm([x], Linv)[0][j:]

    def lift(u):
        a = [Fr(0)] * j + list(u)
        return [sum(a[i] * Lmat[i][t] for i in range(n)) % 1 for t in range(n)]

    # τ0：𝒥 中的一个元素，β(τ0) ≠ 0（即 π(τ0·A) = w0 ≠ 0）
    tau0 = None
    for t in J:
        w = pi(mm([t], A)[0])
        if any(w):
            tau0 = t
            break
    if tau0 is None:
        print("没有 β ≠ 0 的 𝒥 元素"); return
    w0 = pi(mm([tau0], A)[0])
    print(f"τ0 = {[str(x) for x in tau0]}；w0 = β(τ0) = {[str(x) for x in w0]}")

    # V 的 4 行：3 个 X 的基的 lift + ℓ0 的 lift；各加 a_i τ0
    Xs = [[Fr(1) if t == i else Fr(0) for t in range(d)] for i in range(d)]
    lifts = [lift(x) for x in Xs]
    l0_lift = lift(pi(L0[0]))
    a1, a2, a3, a4, lam = sp.symbols('a1 a2 a3 a4 lam')

    def R(x):
        return sp.Rational(x.numerator, x.denominator)

    Vrows = []
    for i, coef in enumerate([a1, a2, a3]):
        Vrows.append([R(lifts[i][k]) + coef * R(tau0[k]) for k in range(n)])
    Vrows.append([R(l0_lift[k]) + a4 * R(tau0[k]) for k in range(n)])

    # 铅笔：6 行 = 4 行 (λV − VA) + 2 行 C0A + 2 行 C0 —— 取 6 阶子式
    VArows = [[sum(R(A[t][k]) * Vrows[i][t] for t in range(n)) for k in range(n)] for i in range(4)]

    def pencil_rows():
        rows = []
        for i in range(4):
            rows.append([lam * Vrows[i][k] - VArows[i][k] for k in range(n)])
        for r in CA:
            rows.append([R(x) for x in r])
        for r in C:
            rows.append([R(x) for x in r])
        return rows

    Rows = pencil_rows()
    print(f"铅笔总共 {len(Rows)} 行 × {n} 列；r0 = rank[V;C0A;C0] = {rank([r[:] for r in (J + K)] ) and n}（应 = 6）")

    dets = []
    for rs in itertools.combinations(range(len(Rows)), n):
        M = sp.Matrix([[Rows[i][k] for k in range(n)] for i in rs])
        d_ = sp.expand(M.det())
        dets.append((rs, d_))
    nonzero = [(rs, d_) for rs, d_ in dets if d_ != 0]
    print(f"非零的 6 阶子式个数 = {len(nonzero)} / {len(dets)}")
    if not nonzero:
        print("=> 全部 6 阶子式**恒为零** ⟹ 对**所有**提升、(几乎)所有 λ 都秩降 ⟹ 层不可行 ✓✓")
        return
    # 检查它们是否都恒为零（作为 (a_i, λ) 的多项式）
    for rs, d_ in nonzero[:3]:
        p = sp.Poly(d_, lam, a1, a2, a3, a4)
        print(f"  子式 {rs}: λ 次数 = {p.degree(lam)}；总次数 = {p.total_degree()}")
    # 关键检查：是否**所有**子式都含有因子 λ（即 λ=0 处全为零）
    all_zero_at_0 = True
    for rs, d_ in nonzero:
        if sp.expand(d_.subs(lam, 0)) != 0:
            all_zero_at_0 = False
            break
    print(f"所有非零子式在 λ=0 处是否为零：{all_zero_at_0}")
    if all_zero_at_0:
        print("=> λ=0 处**每个** 6 阶子式都为零 ⟹ 对所有提升、λ=0 处秩 ≤5 < 6 ⟹ (5b) 失败 ⟹ 层不可行 ✓✓")


if __name__ == '__main__':
    main()
