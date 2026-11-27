"""在真实实例上验证 mu=2（定理 11）与 mu=3（定理 2）的格子判据 —— 需要**定向构造** U，
因为随机取 U 几乎总能得到 mu=1（见 verify_cell_criteria_genuine.py 的限制）。

构造：先取 E ⊆ B（dim = mu），再补 (3-mu) 个不在 B 里的向量，并要求 U0 ⊆ U。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI
import importlib.util

spec = importlib.util.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Qm)
spec2 = importlib.util.spec_from_file_location('C', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(CV)

mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def build_U(Q, U0, mu, rng):
    """构造 3 维 U ⊆ X，使 dim(B ∩ U) = mu，且 U0 ⊆ U。"""
    if len(Q.B) < mu:
        return None
    # 取 E ⊆ B 的 mu 维子空间
    perm = list(range(len(Q.B)))
    rng.shuffle(perm)
    E = rb([Q.B[i] for i in perm[:mu]])
    if len(E) != mu:
        return None
    # 补到 3 维：加随机向量，保持 B∩U 的维数不变（即新向量不在 B 里）
    U = [r[:] for r in E]
    tries = 0
    while len(U) < 3 and tries < 200:
        tries += 1
        z = [Fr(rng.randint(-3, 3)) for _ in range(Q.d)]
        cand = rb(U + [z])
        if len(cand) != len(U) + 1:
            continue
        # 检查 B ∩ span(cand) 仍是 mu 维
        Bcap = [b for b in Q.B if rank(cand + [b]) == len(cand)]
        if len(Bcap) != mu:
            continue
        U = cand
    if len(U) != 3:
        return None
    # 要求 U0 ⊆ U
    if any(rank(U + [u0]) > 3 for u0 in U0):
        return None
    return U


def _no_common_root(T, Erows):
    """[lam I - T ; E 的行] 的全部 3x3 子式的 gcd 是否为非零常数（True = 无公共根）。"""
    rows = [[[-T[i][j], Fr(1) if i == j else Fr(0)] for j in range(3)] for i in range(3)]
    for e in Erows:
        rows.append([[e[j]] for j in range(3)])
    polys = []
    for rs in itertools.combinations(range(len(rows)), 3):
        for cs in itertools.combinations(range(3), 3):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = CV.V.det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return False
    g = polys[0]
    for q in polys[1:]:
        g = CV.V.pgcd(g, q)
    return len(g) == 1 and g[0] != 0


def main():
    rng = random.Random(31415)
    stats = {}
    for target_mu in (2, 3):
        agree = tot = 0
        bad = []
        for trial in range(300):
            n = rng.choice([6, 7, 8])
            p = rng.choice([2, 3])
            A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
            C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
            L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
            Q = Qm.Quotient(A, C)
            if Q.d < 3 or Q.m < target_mu:
                continue
            U0 = rb([Q.pi(r) for r in L0])
            if len(U0) > 3:
                continue
            U = build_U(Q, U0, target_mu, rng)
            if U is None:
                continue
            # μ = dim(B ∩ U)：维数公式（§61：不能数"B 的基向量里有多少个落在 U 里" ✗）
            mu = len(Q.B) + len(U) - rank(Q.B + U)
            E = []
            if mu > 0:
                _rows = [[Q.B[i][k] for i in range(len(Q.B))] + [-U[j][k] for j in range(len(U))] for k in range(Q.d)]
                for _sol in AI.nullspace(_rows):
                    _v = [sum(_sol[i] * Q.B[i][k] for i in range(len(Q.B))) for k in range(Q.d)]
                    if any(_v):
                        E.append(_v)
                E = rb(E)
            if len(E) != target_mu:
                continue
            w = E[0]
            if not any(w):
                continue
            try:
                h = CV.solve_for_h(Q, w)
            except Exception:
                continue
            W = Qm.complement(U, Q.d)
            Linv = AI.inv(U + W)
            def decompose(x):
                c = mm([x], Linv)[0]
                return c[:3], c[3:]
            # w 在 U 基下的坐标（第 4 行必须用这个，不是 X 坐标！）
            wc = decompose(w)[0]
            Trows = []
            for u in U:
                ubar = Q.Tbar(u)
                rep = [sum(ubar[k] * Q.Bcomp[k][j] for k in range(len(ubar))) for j in range(Q.d)]
                upart, _ = decompose(rep)
                Trows.append(upart)
            # E 的基在 U 坐标下的表示
            Ec = [decompose(e)[0] for e in E]
            crit = not _no_common_root(Trows, Ec)   # crit=True <=> 存在 E^perp 内特征向量
            found = False
            for _t in range(40):
                cs = [[Fr(rng.randint(-2, 2)) for _ in E] for _ in range(3)]
                prow = []
                for i in range(3):
                    e = [sum(cs[i][k] * E[k][j] for k in range(len(E))) for j in range(3)]
                    ei = [Fr(1) if i == j else Fr(0) for j in range(3)]
                    prow.append((ei, [Trows[i][j] + e[j] for j in range(3)]))
                prow.append(([Fr(0)] * 3, list(wc)))
                if CV.pencil_minors_gcd_one(prow, 3, 3):
                    found = True
                    break
            cov = not found
            tot += 1
            if crit == cov:
                agree += 1
            elif len(bad) < 3:
                bad.append((crit, cov))
        stats[target_mu] = (agree, tot, bad)
        print(f"mu={target_mu}：判据与直接测量一致 {agree}/{tot}；不一致样本 {bad}")


if __name__ == '__main__':
    main()
