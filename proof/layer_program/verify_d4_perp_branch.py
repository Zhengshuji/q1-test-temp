"""补 d=4 分类的 φ⊥B 分支（专家指出的覆盖缺口 ✗ -> ✓）。

构造法（不靠随机 ✗）：先取 b ∈ B 的一个具体向量，令 φ 在 B 上为零（φ⊥B ⟺ B ⊆ ker φ ✓），
再要求 φ(u0)=φ(u0A)=0。于是 φ 落在 B^⊥ ∩ {u0,u0A}^⊥ 里 —— 一般是非零空间 ✓。
对每个这样的 φ 验引理 2.1（μ = dim B）与引理 3.1（(N) ⟺ f(U) ⊆ U/B）。
"""
import itertools, random, sys
from fractions import Fraction as Fr
sys.path.insert(0,'tools/exact_linalg')
import audit_independent as AI
import importlib.util as iu
spec = iu.spec_from_file_location('Q','proof/rho1_layer/quotient_selfcheck.py')
Qm = iu.module_from_spec(spec); spec.loader.exec_module(Qm)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb

rng = random.Random(13579)
mu_ok = mu_tot = 0
N_ok = N_tot = 0
cases = 0
for trial in range(60):
    n = 6
    A = [[Fr(rng.randint(-2,2)) for _ in range(n)] for _ in range(n)]
    C = [[Fr(rng.randint(-2,2)) for _ in range(n)] for _ in range(1)]
    Q = Qm.Quotient(A, C)
    if Q.d != 4 or len(Q.B) < 1: continue
    d = Q.d; B = Q.B
    u0 = Q.pi(C[0]) if any(Q.pi(C[0])) else None
    u0A = Q.pi(mm([C[0]], A)[0])
    # 构造 φ：满足 φ|_B = 0 且 φ(u0) = φ(u0A) = 0
    cons = [list(b) for b in B]
    if u0 is not None and any(u0): cons.append(list(u0))
    if any(u0A): cons.append(list(u0A))
    ns = AI.nullspace(cons)
    if not ns: continue
    phi = None
    for coeffs in itertools.product([Fr(-1), Fr(0), Fr(1)], repeat=len(ns)):
        if not any(coeffs): continue
        cand = [sum(coeffs[i]*ns[i][k] for i in range(len(ns))) for k in range(d)]
        if any(cand):
            phi = cand; break
    if phi is None: continue
    U = rb(AI.nullspace([phi]))
    if len(U) != 3: continue
    cases += 1
    mu = len(B) + 3 - rank([r[:] for r in B] + [r[:] for r in U])
    mu_tot += 1
    if mu == len(B): mu_ok += 1
    fU = [Q.pi(mm([Q.lift(u)], A)[0]) for u in U]
    N_holds = all(rank([r[:] for r in U] + [r[:] for r in B] + [v]) ==
                  rank([r[:] for r in U] + [r[:] for r in B]) for v in fU)
    cond = all(rank([r[:] for r in U] + [v]) == len(U) for v in fU)
    N_tot += 1
    if N_holds == cond: N_ok += 1
print(f"φ⊥B 分支（构造法）：{cases} 个实例")
print(f"  引理 2.1（μ = dim B）：{mu_ok}/{mu_tot}")
print(f"  引理 3.1（(N) ⟺ f(U) ⊆ U/B）：{N_ok}/{N_tot}")
