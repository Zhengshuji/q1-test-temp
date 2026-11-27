"""M2：一参数族上的覆盖检验（RESTRICTED_COMPLETION_MODEL §32）。

X = Q^5, B = <e5>; f 在 <e1,e2,e3> 上恒等、f(e4)=f(e5)=0。
族：U_t = <e5> + <e1, t e2 + e3>（3 维、含 B、mu=1）。
由 f 在 <e1,e2,e3> 上恒等 => (N) 对所有 t 成立。

对每个 t 算格子 T_t 与 C.2 的判据（T_t 是否有落在 E^perp 里的特征向量）。
结论（§32）：13/13 全部被覆盖；机制是 f 在 <e1,e2,e3> 上恒等 => lambda=1、e1 是特征向量且 e1 ⟂ e5。
"""
import itertools
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util
spec = importlib.util.spec_from_file_location('C', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CV)
mm, rank, rb = CV.Qm.mm, CV.Qm.rank, CV.Qm.rb


def main():
    F = [[Fr(0)] * 5 for _ in range(5)]
    for i in range(3):
        F[i][i] = Fr(1)
    B = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1)]]
    results = []
    for k in range(-6, 7):
        t = Fr(k)
        E2 = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)], [Fr(0), t, Fr(1), Fr(0), Fr(0)]]
        U = rb([r[:] for r in B] + E2)
        if len(U) != 3:
            continue
        fU = [mm([u], F)[0] for u in U]
        condN = all(rank(U + B + [v]) == rank(U + B) for v in fU)
        W = []
        span = [r[:] for r in U]
        for i in range(5):
            e = [Fr(1) if j == i else Fr(0) for j in range(5)]
            if rank(span + [e]) > len(span):
                W.append(e)
                span = rb(span + [e])
            if len(span) == 5:
                break
        Linv = AI.inv(U + W)
        Trows = []
        for u in U:
            c = mm([mm([u], F)[0]], Linv)[0]
            Trows.append(c[:3])
        Erow = [Fr(0), Fr(0), Fr(1)]
        rows = [[[-Trows[i][kk], Fr(1) if i == kk else Fr(0)] for kk in range(3)] for i in range(3)]
        rows.append([[Erow[kk]] for kk in range(3)])
        polys = []
        for rs in itertools.combinations(range(4), 3):
            for cs in itertools.combinations(range(3), 3):
                M = [[rows[i][kk] for kk in cs] for i in rs]
                v = CV.V.det_poly(M)
                if not (len(v) == 1 and v[0] == 0):
                    polys.append(v)
        if not polys:
            good = False
        else:
            g = polys[0]
            for q in polys[1:]:
                g = CV.V.pgcd(g, q)
            good = (len(g) == 1 and g[0] != 0)
        results.append((str(t), condN, good))
    print(f"t 取 {len(results)} 个值；全部 (N) 成立？{all(r[1] for r in results)}")
    print("  好格子（不被覆盖）的 t：", [r[0] for r in results if r[2]])
    print("  被覆盖的 t 数：", sum(1 for r in results if not r[2]))


if __name__ == '__main__':
    main()
