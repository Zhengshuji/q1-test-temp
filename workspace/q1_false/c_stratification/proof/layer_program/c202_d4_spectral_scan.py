r"""d=4 的**谱步**：在射影子空间 $\Phi\subseteq\mathbb P^3$ 上逐点判"格子是否被覆盖"。

背景（proof/layer_31_theorems/d4_classification.md §5）：$d=4$ 时 $\mathcal U=\ker\varphi$（$\varphi\in\mathbb P^3$），
$\dim\Phi\le1$ 时可判，$\dim\Phi\ge2$ 时原文写"需要 incidence/消元"。本脚本做两件事：

  1. **逐点精确判定**：给一个有理点 $\varphi$，算 U、$\mu$、$T$、$w$，用
     $\left[\lambda I-T;\,w\right]$ 的最大子式 $\gcd$ 判"被覆盖"（全有理算术）；
  2. **在 $\Phi$ 上扫描**：$\varphi(s,t)=\varphi_0+s\varphi_1+t\varphi_2$，报出被覆盖/不被覆盖的分布；
     一旦找到**不被覆盖**的点，就构造 $\mathcal L$ 并**直接**验 $(5a)\wedge(5b)$（这给出**可证**的层可行）。

**这个脚本能证明什么、不能证明什么**（见同目录 `SPECTRAL_STEP_DESIGN.md`）：
  * 找到不被覆盖的点 ⟹ 层可行 ✓（严格，附见证）；
  * 全部扫描点都被覆盖 ⟹ 只是**证据**，不是证明（"被覆盖"集是闭集，"不被覆盖"是开集；
    要证全被覆盖，需要消元/整化）。

用法：python proof/layer_program/c202_d4_spectral_scan.py [--seed 3] [--n 25]
"""
import itertools
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'proof', 'rho1_layer'))

import audit_independent as AI
import importlib.util as iu
import verify_mu1_w_ne_0_instance as LIB          # minors_gcd_degree（插值 + Euclid）

spec = iu.spec_from_file_location('Q', os.path.join(_ROOT, 'proof', 'rho1_layer', 'quotient_selfcheck.py'))
Qm = iu.module_from_spec(spec)
spec.loader.exec_module(Qm)

mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def cell_data(Q, A, phi):
    """给定 φ（X 的坐标），返回格子数据 (U, mu, T, w, E, h)；不可用返回 None。"""
    d = Q.d
    ns = AI.nullspace([phi])
    U = rb(ns)
    if len(U) != 3:
        return None
    mu = len(Q.B) + 3 - rank([r[:] for r in Q.B] + [r[:] for r in U])
    if mu == 0:
        return dict(U=U, mu=0)   # C.4：恒被覆盖（与 T,w 无关）
    # E = B∩U
    rows = [[Q.B[i][k] for i in range(len(Q.B))] + [-U[j][k] for j in range(3)]
            for k in range(d)]
    E = []
    for sol in AI.nullspace(rows):
        v = [sum(sol[i] * Q.B[i][k] for i in range(len(Q.B))) for k in range(d)]
        if any(v):
            E.append(v)
    E = rb(E)
    if not E:
        return dict(U=U, mu=mu, reason='E=0')
    # h：J 中元素，β(h)=w ∈ E 且 w ≠ 0
    h = None
    w = None
    for er in E:
        # 解 β(h) = er：h = Σ c_i J_i，π(hA) = er
        Jpi = [Q.pi(mm([Ji], A)[0]) for Ji in Q.J]     # β(J_i) 在 X 里的坐标
        eqs = [[Jpi[i][k] for i in range(len(Q.J))] + [er[k]] for k in range(d)]
        try:
            sol = AI.rref(eqs)
        except Exception:
            continue
        # 取一个解
        nv = len(Q.J)
        cand = [Fr(0)] * nv
        ok = True
        for row in sol[0]:
            piv = next((t for t in range(nv) if row[t] != 0), None)
            if piv is None:
                if row[nv] != 0:
                    ok = False
                continue
            cand[piv] = row[nv] / row[piv]
        if not ok:
            continue
        hh = [sum(cand[i] * Q.J[i][k] for i in range(nv)) for k in range(len(A))]
        ww = Q.pi(mm([hh], A)[0])
        if any(ww):
            h, w = hh, ww
            break
    if h is None:
        return dict(U=U, mu=mu, reason='no h')
    # T：f(u_i) = Σ_j T_ij u_j + Σ_k c_ik B_k
    fU = [Q.pi(mm([Q.lift(u)], A)[0]) for u in U]
    nunk = 9 + 3 * len(Q.B)
    eqs = []
    for i in range(3):
        for k in range(d):
            row = [Fr(0)] * nunk + [fU[i][k]]
            for j in range(3):
                row[j * 3 + i] = U[j][k]
            for t in range(len(Q.B)):
                row[9 + i * len(Q.B) + t] = Q.B[t][k]
            eqs.append(row)
    sol = [Fr(0)] * nunk
    for row in AI.rref(eqs)[0]:
        piv = next((t for t in range(nunk) if row[t] != 0), None)
        if piv is None:
            continue
        sol[piv] = row[nunk] / row[piv]
    T = [[sol[j * 3 + i] for j in range(3)] for i in range(3)]
    # 残差检查（纪律：先打印/断言约束）
    for i in range(3):
        res = [fU[i][k] - sum(T[i][j] * U[j][k] for j in range(3)) for k in range(d)]
        if rank(Q.B + [res]) != len(Q.B):
            return dict(U=U, mu=mu, reason='(N) fails')
    return dict(U=U, mu=mu, T=T, w=w, E=E, h=h, reason='ok')


def covered(T, w):
    def rows(lam):
        R = [[(lam if i == k else Fr(0)) - T[i][k] for k in range(3)] for i in range(3)]
        R.append([Fr(x) for x in w])
        return R
    return LIB.minors_gcd_degree(rows, 4, 3) > 0


def witness_ok(Q, A, L0, D):
    """在格子里找一个 L=[L0;R]（row L = V）使 (5a)∧(5b) 成立；成功返回 L。"""
    U, h = D['U'], D['h']
    n = len(A)
    # V = <lift(U)> ⊕ <h>
    V = rb([Q.lift(u) for u in U] + [h])
    if len(V) != 4:
        return None
    if not AI.in_span(L0[0], V):
        return None
    e = [[Fr(1) if t == i else Fr(0) for t in range(n)] for i in range(n)]
    # 用 L0 作第一行，其余三行在 V 的补里取（这里用 V 的基做行变换凑出含 L0 的基）
    basis = [list(L0[0])]
    for v in V:
        if rank(basis + [v]) > len(basis):
            basis.append(v)
        if len(basis) == 4:
            break
    if len(basis) != 4:
        return None
    return basis


def main():
    seed = 3
    ngrid = 25
    if '--seed' in sys.argv:
        seed = int(sys.argv[sys.argv.index('--seed') + 1])
    if '--n' in sys.argv:
        ngrid = int(sys.argv[sys.argv.index('--n') + 1])
    rng = random.Random(seed)
    n = 7
    for trial in range(400):
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        # 强制 j=3（d=4）：行 1 = e3、行 2 = 0，C = [e1;e2] ⟹ J = <e1,e2,e3>
        A[0] = [Fr(0)] * n; A[0][2] = Fr(1)
        A[1] = [Fr(0)] * n
        C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)],
             [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
        Q = Qm.Quotient(A, C)
        if Q.d != 4:
            continue
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
        # 只用 μ≥1 的 φ：μ = dim(B∩kerφ) ≥ 1 ⟺ φ ∈ B^⊥；dim B=1 时这是 P^2（正是要判的情形）
        if len(Q.B) != 1:
            continue
        b = Q.B[0]
        nsp = AI.nullspace([b])            # 4×3：B^⊥ 的三维坐标空间
        if len(nsp) != 3:
            continue
        phi0 = [Fr(x) for x in nsp[0]]
        phi1 = [Fr(x) for x in nsp[1]]
        phi2 = [Fr(x) for x in nsp[2]]
        print(f'实例：n={n}、j={Q.j}、d={Q.d}、dim B={len(Q.B)}；Φ = <φ0,φ1,φ2>（P^2）')
        print(f'  φ0={[str(x) for x in phi0]}  φ1={[str(x) for x in phi1]}  φ2={[str(x) for x in phi2]}')
        grid = [Fr(k) for k in range(-ngrid // 2 + 1, ngrid // 2 + 1)]
        cov = nocov = bad = 0
        reasons = {}
        found = None
        for s in grid:
            for t in grid:
                phi = [phi0[i] + s * phi1[i] + t * phi2[i] for i in range(4)]
                if not any(phi):
                    continue
                D = cell_data(Q, A, phi)
                if D is None:
                    bad += 1
                    continue
                if D['mu'] == 0:
                    cov += 1
                    continue
                if D.get('reason') != 'ok':
                    reasons[D['reason']] = reasons.get(D['reason'], 0) + 1
                    continue
                if covered(D['T'], D['w']):
                    cov += 1
                else:
                    nocov += 1
                    if found is None:
                        found = (s, t, phi, D)
        print(f'  扫描 {len(grid) ** 2} 点：被覆盖 {cov}、不被覆盖 {nocov}、其它 {reasons}、None {bad}')
        if found:
            s, t, phi, D = found
            print(f'  → 找到不被覆盖的点 (s,t)=({s},{t})、μ={D["mu"]}：层可行 ✓（下面直接验）')
            L = witness_ok(Q, A, L0, D)
            if L is None:
                print('    但没构造出 L（需要 W0⊆U）；记为"未完成" ✗')
            else:
                CA = mm(C, A)
                r0 = rank(L + CA + C)
                ok5a = rank(mul(L, A) + L + CA + C) == r0
                # (5b)：λ 扫描（有限）
                ok5b = all(rank([[lam * L[i][k] - mm(L, A)[i][k] for k in range(n)]
                                 for i in range(4)] + CA + C) == r0
                           for lam in [Fr(0), Fr(1), Fr(-1), Fr(2)])
                print(f'    L 的秩={rank(L)}、r0={r0}、(5a)={ok5a}、(5b)[λ=−1,0,1,2]={ok5b}')
        return
    print('400 个随机 trial 里没有 d=4 的实例')


if __name__ == '__main__':
    main()






