"""验证 C.2 的**尖锐化**（RESTRICTED_COMPLETION_MODEL §34）—— 纯有理算术版。

对 mu=1、E 是 1 维的格子，T 为 3x3 格子数据。断言：

    好（不被覆盖，即 E^perp 里没有特征向量）
    <=>  T 恰好只有**一条**特征线，且该特征向量落在 E 里。

"恰好一条特征线" 的精确判定（只用有理算术 + 有理根定理）：
   - 特征多项式必须是 (x - t)^3，t 有理；
   - 且 rank(T - t I) = 2（核 1 维）。
若特征多项式有不可约的高次因子，则该因子给出 >= 2 条复特征线 => >= 2 条特征线 => 坏。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util
spec = importlib.util.spec_from_file_location('C', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CV)
V = CV.Qm.mm, CV.Qm.rank
mm, rank = CV.Qm.mm, CV.Qm.rank


def bad_by_definition(T, Erows):
    """E^perp 里有特征向量 <=> 铅笔 [lam I - T; E] 的 3x3 子式 gcd 非常量。"""
    rows = [[[-T[i][k], Fr(1) if i == k else Fr(0)] for k in range(3)] for i in range(3)]
    for e in Erows:
        rows.append([[e[k]] for k in range(3)])
    polys = []
    for rs in itertools.combinations(range(len(rows)), 3):
        for cs in itertools.combinations(range(3), 3):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = CV.V.det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return True
    g = polys[0]
    for q in polys[1:]:
        g = CV.V.pgcd(g, q)
    return not (len(g) == 1 and g[0] != 0)


def charpoly(T):
    """det(x I - T)，系数从低到高。"""
    M = [[([-T[i][j]] if i != j else [-T[i][i], Fr(1)]) for j in range(3)] for i in range(3)]
    return CV.V.det_poly(M)


def rational_roots_and_multiplicity(cp):
    """返回 (是否 = (x-t)^3 且 t 有理, t)。"""
    # (x - t)^3 = x^3 - 3t x^2 + 3t^2 x - t^3
    if len(cp) != 4:
        return (False, None)
    c3, c2, c1, c0 = cp[3], cp[2], cp[1], cp[0]
    if c3 == 0:
        return (False, None)
    t = -c2 / (3 * c3)
    if c1 != 3 * t * t * c3 or c0 != -t ** 3 * c3:
        return (False, None)
    return (True, t)


def main():
    rng = random.Random(424242)
    E = [[Fr(0), Fr(0), Fr(1)]]           # E = <e3>，1 维
    agree = tot = 0
    good_count = 0
    for _ in range(200):
        T = [[Fr(rng.randint(-2, 2)) for _ in range(3)] for _ in range(3)]
        bad = bad_by_definition(T, E)
        cp = charpoly(T)
        single, t = rational_roots_and_multiplicity(cp)
        if single:
            single = single and (rank([[T[i][j] - (t if i == j else Fr(0)) for j in range(3)]
                                       for i in range(3)]) == 2)
        vinE = False
        if single:
            ker = AI.nullspace([[T[i][j] - (t if i == j else Fr(0)) for j in range(3)]
                                for i in range(3)])
            if ker:
                v = ker[0]
                vinE = (v[0] == 0 and v[1] == 0)
        pred_good = single and vinE
        tot += 1
        if not bad:
            good_count += 1
        if (not bad) == pred_good:
            agree += 1
    print(f"C.2 尖锐化（好 <=> 单特征线且特征向量在 E 里）：一致 {agree}/{tot}")
    print(f"  随机样本里实际'好'的个数：{good_count}（预期很少 → 这个判据很严 ✓）")


if __name__ == '__main__':
    main()
