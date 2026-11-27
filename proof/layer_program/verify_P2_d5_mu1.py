"""§65：$d=5$、$\\dim B=2$、$\\dim W_0=2$ 且 $W_0\\cap B=0$ 时，P2 的判定化归为**一参数**问题。

关键观察：
  $\\mu\\ge1\\iff\\mathcal U\\cap B\\ne0\\iff\\exists$ 直线 $L\\subseteq B$ 使 $L\\subseteq\\mathcal U$ ✓。
  若 $\\dim W_0=2$ 且 $W_0\\cap B=0$ ✓，则对**每条** $L\\in\\mathbb P(B)\\cong\\mathbb P^1$：
     $\\mathcal U_L:=W_0+L$ 是 3 维 ✓ 且 $W_0\\subseteq\\mathcal U_L$ ✓、$\\mu=1$ ✓。
  ⟹ P2 ⟺ ∃$[L]\\in\\mathbb P^1$ 使 $\\mathcal U_L$ 满足 $(N)$ ✓
     —— 一个**单变量**条件（$L$ 由 $t\\in\\mathbb P^1$ 参数化）✓ ⟹ 可由有限检验 + 结式判定 ✓。

本脚本：在具体实例上枚举 $t\\in\\mathbb P^1$（有限个有理点 + 无穷远点），逐点验 $(N)$，
报告是否存在满足的点（若存在 ⟹ P2 = YES ✓）。
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


def make_instance(seed=0):
    """显式构造 d=5、dim B=2 的实例（不再拒绝采样）。

    n=7；C = e7；A: e7->e6, e6->e5, e5->e1，其余 0。
      J = <e7, e6>（因为 e7 A = e6）=> d = 7 - 2 = 5 ✓
      J A = <e6 A, e7 A> = <e5, e6> => B = pi(J A) 2 维 ✓
    L0 随机（一般位置）=> W0 = <pi(l0), pi(l0 A)> 一般 2 维 ✓
    """
    import random
    rng = random.Random(seed)
    n = 7
    A = [[Fr(0)] * n for _ in range(n)]
    A[6][5] = Fr(1)      # e7 -> e6
    A[5][4] = Fr(1)      # e6 -> e5
    A[4][0] = Fr(1)      # e5 -> e1
    C = [[Fr(1) if t == 6 else Fr(0) for t in range(n)]]     # C = e7
    L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
    Q = Qm.Quotient(A, C)
    if Q.d != 5 or len(Q.B) != 2:
        return None
    W0 = rb([Q.pi(r) for r in L0] + [Q.pi(mm([r], A)[0]) for r in L0])
    if len(W0) != 2 or rank([r[:] for r in W0] + [r[:] for r in Q.B]) != 4:
        return None
    return A, C, W0, Q


def main():
    found = None
    for seed in range(40):
        out = make_instance(seed)
        if out is None:
            continue
        A, C, W0, Q = out
        d = Q.d
        B = Q.B
        # 把 B 参数化：L_t = <b1 + t b2>（t ∈ Q），再加无穷远 L_inf = <b2>
        b1, b2 = B[0], B[1]
        trials = []
        for k in range(-6, 7):
            t = Fr(k)
            L = [b1[i] + t * b2[i] for i in range(d)]
            trials.append((f"t={t}", L))
        trials.append(("t=∞", list(b2)))
        hits = []
        for name, L in trials:
            U = rb([r[:] for r in W0] + [L])
            if len(U) != 3:
                continue
            # (N)
            fU = [Q.pi(mm([Q.lift(u)], A)[0]) for u in U]
            N_ok = all(rank([r[:] for r in U] + [r[:] for r in B] + [v]) ==
                       rank([r[:] for r in U] + [r[:] for r in B]) for v in fU)
            mu = len(B) + len(U) - rank([r[:] for r in B] + [r[:] for r in U])
            if N_ok and mu >= 1:
                hits.append((name, mu))
        if hits:
            found = (seed, hits[:3])
            print(f"seed={seed}: d=5, dim B=2, dim W0=2, W0∩B=0 ✓")
            print(f"  存在满足 (N) 且 μ≥1 的 U_L：{hits[:3]}")
            print("  => P2 = YES ✓")
            break
    if found is None:
        print("在 40 个实例 × 13 个 L 里没找到满足 (N) 且 μ≥1 的 U_L ⟹ 本轮未确认 P2")


if __name__ == '__main__':
    main()
