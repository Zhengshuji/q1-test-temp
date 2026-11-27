"""检查 §7 的 7 个"判据 B 不一致"案例：是真的没有好 s，还是抽样没找到？

做法：复现同样的随机序列（seed 31415），挑出判据 B 说"应存在好 s"但 60 次抽样没找到的实例，
然后对它们做 **穷尽网格搜索** s ∈ {-3,...,3}^3（343 个点），看是否真的存在好 s。
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
spec2 = importlib.util.spec_from_file_location('C', 'proof/rho1_layer/verify_mu1_compression.py')
C = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(C)


def good_s_exists_exact(T, a, w, bound=3):
    """在 s ∈ {-bound..bound}^3 上穷尽搜。返回 (found, s)。"""
    rng = None
    for sx in range(-bound, bound + 1):
        for sy in range(-bound, bound + 1):
            for sz in range(-bound, bound + 1):
                s = [Fr(sx), Fr(sy), Fr(sz)]
                Cmat = [[T[i][j] + a[j] * s[i] for j in range(3)] for i in range(3)]
                rows = [([Fr(1) if i == j else Fr(0) for j in range(3)], [Cmat[i][j] for j in range(3)])
                        for i in range(3)]
                rows.append(([Fr(0)] * 3, list(w)))
                polys = []
                for rs in itertools.combinations(range(4), 3):
                    for cs in itertools.combinations(range(3), 3):
                        M = [[[-rows[i_][1][j], rows[i_][0][j]] for j in cs] for i_ in rs]
                        v = V.det_poly(M)
                        if not (len(v) == 1 and v[0] == 0):
                            polys.append(v)
                if V.gcd_is_one(polys):
                    return True, s
    return False, None


def main():
    rng = random.Random(31415)
    bad_cases = []
    for _ in range(200):
        T = [[Fr(rng.randint(-3, 3)) for _ in range(3)] for _ in range(3)]
        a = [Fr(rng.randint(-3, 3)) for _ in range(3)]
        if not any(a):
            continue
        beta = Fr(rng.randint(-2, 2) or 1)
        w = [beta * a[k] for k in range(3)]
        scalar = C.is_scalar_compression(T, a)
        if scalar is None:
            continue
        d = V.direct(T, a, w, 60, rng)
        if (not scalar) and (not d):
            bad_cases.append((T, a, w))
    print(f"复现出 {len(bad_cases)} 个不一致案例")
    for idx, (T, a, w) in enumerate(bad_cases[:7]):
        found, s = good_s_exists_exact(T, a, w, bound=3)
        print(f"  案例 {idx}: T={[[str(x) for x in r] for r in T]} a={[str(x) for x in a]}")
        print(f"         穷尽 s∈[-3,3]^3 找到好 s？{found}" + (f"  s={[str(x) for x in s]}" if found else ""))


if __name__ == '__main__':
    main()
