"""§52.22 的决定性计算：在 §52.7 的实例上，铅笔 [λV-VA;CA;C] 的 r0 阶子式**次数**。

若所有非零子式次数 >= 1，则 gcd 不可能是非零常量 => (5b) 必失败；
而 τ（给行加 β^{-1}(E) 的元素）只改系数、不改次数 => (5b) 对格子里**所有** τ 都失败
=> 该格子**被覆盖**。
"""
import itertools
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util as iu
spec = iu.spec_from_file_location('M', 'proof/rho1_layer/verify_mu1_instance_cell.py')
M = iu.module_from_spec(spec)
spec.loader.exec_module(M)
spec2 = iu.spec_from_file_location('C2', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = iu.module_from_spec(spec2)
spec2.loader.exec_module(CV)


def main():
    n = 6
    A, C, L0 = M.build(Fr(1), Fr(2))
    CA = M.mul(C, A)
    J = M.rb(C + CA)
    j = len(J)
    e = [[Fr(1) if t == i else Fr(0) for t in range(n)] for i in range(n)]
    V = M.rb([e[0], e[1], e[2], e[4]])
    VA = M.mul(V, A)
    r0 = M.rank(V + CA + C)
    print(f"j = {j}, dim V = {len(V)}, r0 = {r0}")
    rows = [(V[i], VA[i]) for i in range(len(V))]
    for r in CA:
        rows.append(([Fr(0)] * n, list(r)))
    for r in C:
        rows.append(([Fr(0)] * n, list(r)))
    degs = []
    for rs in itertools.combinations(range(len(rows)), r0):
        for cs in itertools.combinations(range(n), r0):
            Mx = [[[-rows[i][1][k], rows[i][0][k]] for k in cs] for i in rs]
            val = CV.V.det_poly(Mx)
            if not (len(val) == 1 and val[0] == 0):
                degs.append(len(val) - 1)
    print(f"非零子式的次数集合：{sorted(set(degs))}（共 {len(degs)} 个非零）")
    print("=> 若最小次数 >= 1，则 (5b) 对该格子**所有** τ 都失败 => 格子被覆盖 ✗")


if __name__ == '__main__':
    main()
