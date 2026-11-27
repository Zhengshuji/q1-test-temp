# ⚠️ 本脚本里的"⟂"判据**不是不变量** ✗（§77–§79）—— 它的筛选/判断用坐标点积，
# 而正确的不变形式是**秩/包含**条件：w ∈ (λI−T)(U)（见 RESTRICTED_COMPLETION_MODEL §80）。
# 本脚本仅作为**过程记录**保留；正确的反例脚本是 verify_counterexample_final.py（§81）。
"""§74 / 优先项 (1)：造一个 **正维** 的 μ≥1 族，并检查"是否所有格子都被覆盖"。

取 ($d$, $\\dim B$) = (5, 3)：由 §60 的引理 $\\dim B\\ge d-2=3$ ⟹ **每个** 3 维 $\\mathcal U$ 都 $\\mu\\ge1$ ✓
⟹ 只要 $\\dim W_0=2$，$\\mathcal U=W_0\\oplus\\langle z\\rangle$（$z\\in\\mathbb P^2$）就是**2 维族** ✓。

对族里每个 $z$：算 $E$、$T$（解线性方程组），判"是否被覆盖"（C.2/C.3 的 gcd 判据）✓。
若某个开集上都不被覆盖 ⟹ 二分猜想 (b) 分支成立（无压力）✓；
若**全部**被覆盖 ⟹ **候选反例** ✗（再上符号验证）。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util as iu
spec = iu.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = iu.module_from_spec(spec)
spec.loader.exec_module(Qm)
spec2 = iu.spec_from_file_location('C2', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = iu.module_from_spec(spec2)
spec2.loader.exec_module(CV)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def cell_covered(Q, A, U):
    """返回 (covered?, mu)。covered = 不存在使 (5b) 成立的 tau。"""
    d = Q.d
    B = Q.B
    mu = len(B) + len(U) - rank([r[:] for r in B] + [r[:] for r in U])
    if mu == 0:
        return True, 0
    # E = B ∩ U
    _rows = [[B[i][k] for i in range(len(B))] + [-U[j][k] for j in range(len(U))] for k in range(d)]
    E = []
    for sol in AI.nullspace(_rows):
        v = [sum(sol[i] * B[i][k] for i in range(len(B))) for k in range(d)]
        if any(v):
            E.append(v)
    E = rb(E)
    rho = len(U)
    fU = [Q.pi(mm([Q.lift(u)], A)[0]) for u in U]
    nunk = rho * rho + rho * len(B)
    eqs = []
    for i in range(rho):
        for k in range(d):
            row = [Fr(0)] * nunk + [fU[i][k]]
            for j in range(rho):
                row[j * rho + i] = U[j][k]
            for t in range(len(B)):
                row[rho * rho + i * len(B) + t] = B[t][k]
            eqs.append(row)
    R = AI.rref(eqs)[0]
    s_ = [Fr(0)] * nunk
    for row in R:
        piv = next((j for j in range(nunk) if row[j] != 0), None)
        if piv is None:
            continue
        s_[piv] = row[nunk] / row[piv]
    T = [[s_[j * rho + i] for j in range(rho)] for i in range(rho)]
    Erows = []
    for er in E:
        ER = AI.rref([[U[j][k] for j in range(rho)] + [er[k]] for k in range(d)])[0]
        a = [Fr(0)] * rho
        for row in ER:
            piv = next((j for j in range(rho) if row[j] != 0), None)
            if piv is None:
                continue
            a[piv] = row[rho] / row[piv]
        Erows.append(a)
    rows = [[[-T[i][k], Fr(1) if i == k else Fr(0)] for k in range(rho)] for i in range(rho)]
    for er in Erows:
        rows.append([[er[k]] for k in range(rho)])
    polys = []
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(rho), rho):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = CV.V.det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return True, mu
    g = polys[0]
    for q in polys[1:]:
        g = CV.V.pgcd(g, q)
    good = (len(g) == 1 and g[0] != 0)
    return (not good), mu


def find_instance(rng, n=11, p=3):
    """d=5 且 dim B >= 3 的实例。

    注意（新引理）：dim B <= p（C 的行数）—— 因为 J = row[C;CA]，J·A 模 J 只由 {c_i A^2} 张成。
    所以要 dim B >= 3 必须 p >= 3。
    """
    from collections import Counter
    seen = Counter()
    for _ in range(300):
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        CA = mm(C, A); J = rb(C + CA)
        Q = Qm.Quotient(A, C)
        seen[(len(J), Q.d, len(Q.B))] += 1
        if Q.d == 5 and len(Q.B) >= 3:
            print(f"  找到：j={len(J)}, d={Q.d}, dim B={len(Q.B)}")
            return A, C, Q
    print(f"  统计（j, d, dimB）：{dict(list(seen.items())[:8])}")
    return None


def main():
    rng = random.Random(31415)
    got = find_instance(rng)
    if got is None:
        print("没找到 d=5、dim B=3 的实例")
        return
    A, C, Q = got
    d = Q.d
    B = Q.B
    print(f"n=11, j={Q.j}, d={d}, dim B={len(B)} ⟹ 由引理 60.1（dim B >= d-2），所有 3 维 U 都 mu>=1 ✓")
    # W0：随机 L0，使 dim W0 = 2
    W0 = None
    for _ in range(200):
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(11)]]
        W0c = rb([Q.pi(L0[0])] + [Q.pi(mm([L0[0]], A)[0])])
        if len(W0c) == 2:
            W0 = W0c
            break
    if W0 is None:
        print("没找到 dim W0=2")
        return
    # z ∈ X/W0 的补空间（P^2）
    K = []
    span = [r[:] for r in W0]
    for i in range(d):
        e = [Fr(1) if t == i else Fr(0) for t in range(d)]
        if rank(span + [e]) > len(span):
            K.append(e); span = rb(span + [e])
        if len(span) == d:
            break
    print(f"X/W0 维数 = {len(K)}（z ∈ P^{len(K)-1}）")
    stats = {'covered': 0, 'good': 0, 'degenerate': 0}
    mus = set()
    for _ in range(40):
        coeffs = [Fr(rng.randint(-2, 2)) for _ in K]
        if not any(coeffs):
            continue
        z = [sum(coeffs[i] * K[i][k] for i in range(len(K))) for k in range(d)]
        U = rb([r[:] for r in W0] + [z])
        if len(U) != 3:
            stats['degenerate'] += 1
            continue
        cov, mu = cell_covered(Q, A, U)
        mus.add(mu)
        stats['covered' if cov else 'good'] += 1
    print(f"族里 40 个随机 z：{stats}；μ 取值 {sorted(mus)}")
    if stats['good'] > 0:
        print("=> 族里**存在好格子** ⟹ 二分猜想 (b) 分支成立 ✓（此实例无压力）")
    elif stats['covered'] > 0:
        print("=> 随机点**全部**被覆盖 ⟹ **候选反例** ✗ —— 需要符号验证（incidence 投影）")
    else:
        print("=> 全部退化（z 落进 W0）")


if __name__ == '__main__':
    main()
