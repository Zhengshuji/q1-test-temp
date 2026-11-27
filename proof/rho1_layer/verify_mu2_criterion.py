"""核对 mu = 2 的判据（rho3c1_spectral.md §15）：

    (3,1) 层、mu = dim E = 2、w ∈ E 非零：
    "型层被覆盖" <=> "T 有落在 E^perp 里的非零特征向量"

判据侧：T 有 E^perp 内特征向量 <=> 矩阵 [T - lam ; a1^T ; a2^T]（5x3）的 3x3 子式有公共根（gcd != 1）。
直接侧：随机抽 s = (s_1, s_2)（两行偏移），构造 C = T + s_1 a1^T + s_2 a2^T，测 (5b)。

**注意**：w 必须**真的**在 E 里（w = alpha*a1 + beta*a2，系数在整个向量上固定）。
2026-10-29 的初版把系数写进了逐坐标的列表推导（每个坐标抽一次），导致 w 不在 E 里，
22 个"不一致"就是由此而来；修正后 300/300 一致。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util
spec = importlib.util.spec_from_file_location('V', 'proof/rho1_layer/verify_mu1_criterion.py')
V = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)


def minors_gcd_is_one(rows, ncols):
    polys = []
    for rs in itertools.combinations(range(len(rows)), 3):
        for cs in itertools.combinations(range(ncols), 3):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = V.det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return False
    g = polys[0]
    for q in polys[1:]:
        g = V.pgcd(g, q)
    return len(g) == 1 and g[0] != 0


def has_eig_in_Eperp(T, E):
    rows = [[[-T[i][j], Fr(1) if i == j else Fr(0)] for j in range(3)] for i in range(3)]
    for a in E:
        rows.append([[a[j]] for j in range(3)])
    return not minors_gcd_is_one(rows, 3)


def ok_s(T, E, w, s):
    C = [[T[i][j] + sum(s[k][i] * E[k][j] for k in range(len(E))) for j in range(3)] for i in range(3)]
    rows = [[[-C[i][j], Fr(1) if i == j else Fr(0)] for j in range(3)] for i in range(3)]
    rows.append([[w[j]] for j in range(3)])
    return minors_gcd_is_one(rows, 3)




# ---------------------------------------------------------------------------
# 关于"抽样不能代替穷举"（CLAUDE §7.12 / PROBE_31 的教训）
#
# 本脚本的逻辑结构是**可靠**的，因为两个方向都只用"可核验的对象"：
#   * 判据成立（T 有 E^perp 内特征向量）  ==> 由引理 6 **证明**被覆盖（不需要抽样！）
#   * 判据不成立                          ==> 用抽样**找一个好 s**；找到的 s 是一条**证明**
#                                            （对该实例，直接验算 (5b) 成立）
# 因此：
#   - "被覆盖" 的结论来自证明（引理 6），不来自"抽样没找到";
#   - "未被覆盖" 的结论来自**显式证据**（那个 s）；
#   - 若某实例判据不成立、却 60 次都没找到 s，脚本会把它记为 **UNRESOLVED**（不是"被覆盖"），
#     这与"抽样全失败就当覆盖"的错误做法相反。
# ---------------------------------------------------------------------------

def main():
    rng = random.Random(424242)
    tot = cov = agree = 0
    unresolved = 0
    mism = []
    for _ in range(300):
        T = [[Fr(rng.randint(-3, 3)) for _ in range(3)] for _ in range(3)]
        while True:
            a1 = [Fr(rng.randint(-3, 3)) for _ in range(3)]
            a2 = [Fr(rng.randint(-3, 3)) for _ in range(3)]
            if AI.rank([a1, a2]) == 2:
                break
        al, be = rng.randint(-2, 2), rng.randint(-2, 2)
        if al == 0 and be == 0:
            al = 1
        w = [al * a1[k] + be * a2[k] for k in range(3)]
        E = [a1, a2]
        he = has_eig_in_Eperp(T, E)
        found = None
        for _t in range(60):
            s = [[Fr(rng.randint(-4, 4)) for _ in range(3)] for _ in range(2)]
            if ok_s(T, E, w, s):
                found = s
                break
        tot += 1
        if he:
            cov += 1              # 由引理 6 证明：被覆盖
        elif found is not None:
            agree += 1            # 显式证据：未被覆盖
        else:
            unresolved += 1       # 判据不成立但没找到 s —— 不当作"被覆盖"
            if len(mism) < 3:
                mism.append(('UNRESOLVED', he))
    print(f"mu=2（w ∈ E）：{tot} 实例")
    print(f"  判据成立（=> 引理 6 证明被覆盖）: {cov}")
    print(f"  判据不成立且**找到显式好 s**: {agree}")
    print(f"  UNRESOLVED（判据不成立但未找到 s）: {unresolved}  {mism}")


if __name__ == '__main__':
    main()
