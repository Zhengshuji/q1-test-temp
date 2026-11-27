"""重跑 end-to-end（§49）：修法 s(u0)=ℓ0，并用 10 项检查器逐条核验。

每条成功实例都满足：
  dim U = 3；W0 ⊆ U；w ≠ 0；(N)；mu ≥ 1；row(L0) ⊆ V；dim V = 4；类型 (3,1)；(5a)；(5b)。
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import importlib.util as iu
sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

spec = iu.spec_from_file_location('CHK', 'proof/rho1_layer/verify_cell_all_conditions.py')
CHK = iu.module_from_spec(spec)
spec.loader.exec_module(CHK)
spec2 = iu.spec_from_file_location('E', 'proof/rho1_layer/verify_end2end_genuine.py')
E2E = iu.module_from_spec(spec2)
spec2.loader.exec_module(E2E)
Qm = CHK.Qm
mm, rank, rb = CHK.mm, CHK.rank, CHK.rb


def main():
    rng = random.Random(443322)
    succ = tried = 0
    from collections import Counter
    MUS = Counter()
    for trial in range(40):
        n = rng.choice([6, 7])
        p = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
        Q = Qm.Quotient(A, C)
        if Q.d < 3 or Q.m < 1:
            continue
        u0 = Q.pi(L0[0])
        if not any(u0):
            continue
        for _k in range(8):
            U = rb([u0] + [[Fr(rng.randint(-2, 2)) for _ in range(Q.d)] for _ in range(3)])
            if len(U) != 3:
                continue
            U = rb([u0] + [r for r in U if rank([u0] + [r]) == 2][:2])
            if len(U) != 3 or rank([u0] + U) != 3:
                continue
            W0 = rb([u0] + [Q.pi(mm([r], A)[0]) for r in L0])
            if not all(rank(U + [x]) == 3 for x in W0):
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
            if not E:
                continue
            w = next((e for e in E if any(e)), None)
            if w is None:
                continue
            rowsV = [list(L0[0])]
            taus = [[Fr(0)] * n]
            ok = True
            for i in range(1, 3):
                s = Q.lift(U[i])
                img = Q.pi(mm([s], A)[0])
                if rank(U + [img]) == 3:
                    taus.append([Fr(0)] * n)
                else:
                    found = None
                    for k in range(len(E)):
                        for cc in (Fr(1), Fr(-1)):
                            img2 = [img[j] + cc * E[k][j] for j in range(Q.d)]
                            if rank(U + [img2]) == 3:
                                found = E2E.solve_tau(Q, [cc * x for x in E[k]])
                                break
                        if found is not None:
                            break
                    if found is None:
                        ok = False
                        break
                    taus.append(found)
                rowsV.append([s[k] + taus[-1][k] for k in range(n)])
            if not ok:
                continue
            h = E2E.solve_tau(Q, w)
            rowsV.append(list(h))
            V = rb(rowsV)
            CA = mm(C, A)
            J = rb(C + CA)
            j = len(J)
            rho = rank(V + CA + C) - j
            cc_ = len(V) + j - rank(V + J)
            conds = {
                'dimU=3': len(U) == 3,
                'W0⊆U': all(rank(U + [x]) == 3 for x in W0),
                'w≠0': any(w),
                'N': all(rank(U + Q.B + [mm([Q.lift(u)], A)[0]]) == rank(U + Q.B) for u in U),
                'mu≥1': len(E) >= 1,
                'row(L0)⊆V': all(rank(V + [list(r)]) == len(V) for r in L0),
                'dimV=4': len(V) == 4,
                'type(3,1)': (rho, cc_) == (3, 1),
                '5a': E2E.cond5a(V, A, C),
                '5b': E2E.cond5b(V, A, C),
            }
            tried += 1
            if all(conds.values()):
                succ += 1
                from collections import Counter
                MUS[len(E)] += 1
                break
    print(f"尝试构造 {tried} 次；**全部 10 条都通过**的：{succ}")
    print(f"  这些成功实例的 mu 分布：{dict(MUS)}")
    print("（dim V=4、类型 (3,1)、row(L0) ⊆ V、(5a)(5b) 都成立 => 真正的 (3,1) 见证）")


if __name__ == '__main__':
    main()
