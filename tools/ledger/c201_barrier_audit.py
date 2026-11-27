"""c201_barrier_audit.py -- 用"秩屏障"（proof/rank_barrier/）给账本里的每个实例算
一个**可证**的结论：有的实例**根本无解**。

为什么能无解
------------
秩屏障（docs/02 §F.1）：任何可行层满足 ρ ≤ r(λ0) = dim π(C^n(λ0 I − A))，对**每个** λ0。
而 ρ_ci = P(T,B,U_0) 是 ρ 的下界（E.1）。于是

    ρ_ci > r(λ0) 对某个 λ0  ⟹  没有任何解（q_min 不存在，不只是"找不到"）

本脚本对每个实例：
  1. 在 X = C^n/𝒥 的坐标里造出 T、B、U0（与 proof/p_is_polynomial/reduction.md 一致），
     把 T 提升成端同态 φ（φ = T mod B），用 c195 的 P_alg 算 ρ_ci；
  2. 算 r(λ) 于一组具体的 λ（0, ±1, ±2, 1/2, 3），取最小；
  3. 若 ρ_ci > min r ⟹ 判定 **NO SOLUTION**（可证）；
  4. 对有见证的实例，断言 ρ_wit ≤ min r（屏障的一致性检查）。

全部有理算术。用法：
    python tools/ledger/c201_barrier_audit.py
    python tools/ledger/c201_barrier_audit.py --random 8 --seed 5
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'p_algorithm'))
sys.path.insert(0, _HERE)

import audit_independent as AI
import c195_P_q as PA
import c189_ledger as LED

mul, rank, vstack, nullspace, row_basis = AI.mul, AI.rank, AI.vstack, AI.nullspace, AI.row_basis


def barrier_data(A, C, L0):
    """返回 (j, d, N, J, Brows, U0rows) —— 全部在 X 的坐标里。"""
    n = len(A)
    M = vstack([C, mul(C, A)])
    j = rank(M)
    J = row_basis(M)
    d = n - j
    Nv = nullspace(M)                      # K = ker[C;CA] 的基，n×d
    N = [[Nv[k][i] for k in range(len(Nv))] for i in range(n)]
    JA = [mul([r], A)[0] for r in J] if J else []
    Brows = [mul([ja], N)[0] for ja in JA]
    U0rows = [mul([l], N)[0] for l in L0]
    return j, d, N, J, Brows, U0rows


def lift_to_endomorphism(A, N):
    """φ: Q^d -> Q^d，满足 φ(u) ≡ T(u) mod B。行约定。"""
    n = len(N)
    d = len(N[0])
    # G = N^T N，x_i = e_i G^{-1} N^T 满足 x_i N = e_i
    G = [[sum(N[a][i] * N[a][k] for a in range(n)) for k in range(d)] for i in range(d)]
    Ginv = AI.inv(G)
    xs = []
    for i in range(d):
        eG = [Ginv[i][k] for k in range(d)]                    # e_i G^{-1}（行）
        xs.append([sum(eG[k] * N[a][k] for k in range(d)) for a in range(n)])
    phi = []
    for xi in xs:
        xA = mul([xi], A)[0]
        phi.append(mul([xA], N)[0])
    return phi                              # d×d，u ↦ u·φ


def r_of(A, C, lam):
    """r(λ) = dim π(C^n(λI−A)) = rank[λI−A; C; CA] − j"""
    n = len(A)
    M = vstack([C, mul(C, A)])
    j = rank(M)
    L = [[(lam if a == b else 0) - A[a][b] for b in range(n)] for a in range(n)]
    return rank(L + C + mul(C, A)) - j


LAMS = [Fr(0), Fr(1), Fr(-1), Fr(2), Fr(-2), Fr(1, 2), Fr(3)]


def audit(A, C, L0, W=None):
    j, d, N, J, Brows, U0rows = barrier_data(A, C, L0)
    phi = lift_to_endomorphism(A, N)
    rho_ci = PA.P_alg(phi, Brows, U0rows)
    rmin = min(r_of(A, C, lam) for lam in LAMS)
    rmin_lam = min(LAMS, key=lambda lam: r_of(A, C, lam))
    out = dict(j=j, d=d, rho_ci=rho_ci, rmin=rmin, rmin_lam=rmin_lam,
               no_solution=rho_ci > rmin, rho_wit=None)
    if W:
        out['rho_wit'] = rank(mul(W, N))
        assert out['rho_wit'] <= out['rmin'], '见证违反秩屏障（不该发生）'
        assert rho_ci <= out['rho_wit'], 'ρ_ci 不是见证 ρ 的下界（P 的实现有问题）'
    return out


def main():
    rows = LED.certificates() + LED.directed() + LED.family(k=3)
    nrand = 0
    seed = 5
    if '--random' in sys.argv:
        nrand = int(sys.argv[sys.argv.index('--random') + 1])
    if '--seed' in sys.argv:
        seed = int(sys.argv[sys.argv.index('--seed') + 1])
    if nrand:
        import random
        rng = random.Random(seed)
        for t in range(nrand):
            n = rng.choice([4, 5])
            p = rng.choice([1, 2])
            r = rng.choice([1, 2])
            A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
            C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
            L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(r)]
            if rank(C) != p or rank(L0) != r:
                continue
            rows.append(dict(name=f'rand_s{seed}_{t}', src='census', A=A, C=C, L0=L0,
                             W=None))

    hdr = f"{'instance':33s} {'j d':5s} {'rho_ci':>7s} {'min r':>6s} {'lam*':>5s} {'rho_wit':>7s}  verdict"
    print('=' * len(hdr))
    print('c201 -- 秩屏障审计：rho_ci > min r  ⟹  可证无解')
    print('=' * len(hdr))
    print(hdr)
    print('-' * len(hdr))
    bad = 0
    for row in rows:
        try:
            out = audit(row['A'], row['C'], row['L0'], row.get('W'))
        except Exception as e:                      # 不让单个坏实例毁掉整张表
            print(f"{row['name'][:33]:33s}  ERROR: {e}")
            continue
        verdict = 'NO SOLUTION（屏障）' if out['no_solution'] else ''
        if out['no_solution']:
            bad += 1
        rw = '' if out['rho_wit'] is None else str(out['rho_wit'])
        print(f"{row['name'][:33]:33s} {out['j']} {out['d']} "
              f"{out['rho_ci']:>7d} {out['rmin']:>6d} {str(out['rmin_lam']):>5s} "
              f"{rw:>7s}  {verdict}")
    print('-' * len(hdr))
    print(f'可证无解的实例：{bad} / {len(rows)}')


if __name__ == '__main__':
    main()

