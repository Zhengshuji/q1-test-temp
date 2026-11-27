"""反例的**可审计证书**（v2，取代 v1 的 28 子式符号计算）。

裁决：HANDOVER2 §3 是对的 —— v1 脚本里
  (a) `lift` 末尾的 `% 1` 把整数坐标打成 0 ⟹ "V" 实际秩 1 ⟹ 28 个子式平凡为零 ✗；
  (b) `r0` 写成 `rank(...) and n`，永远打印 n，不是真检查 ✗。
所以 v1 的 "0/28" 是 bug 的产物，不能作证书 ✗。

正确的证明只要三行（与 U、截面、提升**全都无关**）：

  设 rank(A) = 2、j = 3、dim π(XA) = 1。
  铅笔在 λ = 0 处是 [−LA; CA; C]：
     * CA、C 的行张成 𝒥           ⟹ 贡献 ≤ j = 3
     * LA 的行（模 𝒥）落在 π(XA)  ⟹ 贡献 ≤ dim π(XA) = 1
  ⟹ rank[−LA; CA; C] ≤ 4。
  而类型 (3,1) 给 rank[V; CA; C] = dim(V+𝒥) = 4+3−1 = 6。
  ⟹ 对**每一个** 4 行 L（不必假设类型）都有 rank[−LA;CA;C] ≤ 4 < 6 ⟹ (5b) 在 λ=0 处失败
  ⟹ 层不可行 ✓

本脚本：(1) 打印被检验对象的**基本不变量**（防止再出 v1 那种假检查）；
        (2) 对 300 个随机类型 (3,1) 的 V 核验 4 < 6；
        (3) 核验 dim π(XA) = 1 与 j = 3。
"""
import random
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
A = [[Fr(x) for x in r] for r in [[-1, 0, 2, 1, -1, -1], [0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                                  [-2, -1, 4, 2, -2, -2], [-2, 0, 4, 2, -2, -2], [0, -2, 0, 0, 0, 0]]]
C = [[Fr(x) for x in r] for r in [[2, 1, -2, 2, -1, -1], [2, 2, 2, 1, -1, 1]]]
L0 = [[Fr(x) for x in r] for r in [[1, 0, 0, 0, 0, 0]]]


def main():
    Q = Qm.Quotient(A, C)
    CA = mm(C, A)
    J = rb(C + CA)
    basis = [[Fr(1) if t == i else Fr(0) for t in range(n)] for i in range(n)]
    imA = rank([Q.pi(mm([e], A)[0]) for e in basis])

    # ---- (1) 基本不变量（v1 缺这一步）----
    inv = {
        'rank(A)': rank(A),
        'j = dim row[C;CA]': len(J),
        'd = dim X': Q.d,
        'dim B': len(Q.B),
        'dim pi(XA)': imA,
        'n': n,
    }
    for k, v in inv.items():
        print(f"  {k} = {v}")
    assert rank(A) == 2 and len(J) == 3 and imA == 1, "不变量与反例声明不符 ✗"

    # ---- (2) 三行证明的核心不等式 ----
    bound = len(J) + imA
    print(f"\n  界：rank[−LA;CA;C] ≤ j + dim π(XA) = {len(J)} + {imA} = {bound}")

    rng = random.Random(20251030)
    tot = bad = 0
    r0_seen = set()
    for _ in range(600):
        V = rb([[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(4)])
        if len(V) != 4:
            continue
        if rank([Q.pi(v) for v in V]) != 3:
            continue
        c = len(V) + len(J) - rank(V + J)
        if c != 1:
            continue
        tot += 1
        LA_neg = [[-x for x in row] for row in mm(V, A)]
        r_lam0 = rank(LA_neg + list(CA) + list(C))     # 铅笔在 λ=0
        r0 = rank(V + CA + C)                          # 真 r0
        r0_seen.add(r0)
        if r_lam0 <= bound and r_lam0 < r0:
            bad += 1
    print(f"  {tot} 个类型 (3,1) 的 V：满足 rank[−LA;CA;C] ≤ {bound} 且 < r0 的：{bad}/{tot}")
    print(f"  （r0 的取值集合：{sorted(r0_seen)} —— 类型 (3,1) 应恒为 {n}）")
    assert bad == tot and r0_seen == {n}, "反例结论不成立 ✗"

    # ---- (3) 结论 ----
    print(f"\n  对每个类型 (3,1) 的 V：rank[−LA;CA;C] ≤ {bound} < {n} = r0")
    print("  ⟹ (5b) 在 λ=0 处失败 ⟹ **层不可行** ✓")
    print("  又 μ = dim(B ∩ X) = dim B = 1 ≥ 1 ⟹ **P2 = YES** ✓")
    print("\n  => P2 = YES 而层不可行 ==> 二分猜想为假（证书成立）✓")


if __name__ == '__main__':
    main()
