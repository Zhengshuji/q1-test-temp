"""620：秩层判定器（符号版）——对给定 H(R), HA(R) 枚举 ω，
打印每层的：(ω+1) 阶子式（必须恒为零）、ω 阶子式的 gcd（须为常数）。"""
import itertools
import sympy as sp


def stratum_report(H, HA, name):
    lam = sp.symbols('lam')
    q, k = H.shape
    P = lam * H - HA
    print(f'=== {name}: q={q}, k={k}, rank H (generic) = {H.rank()} ===')
    for om in range(0, min(q, k) + 1):
        higher = []
        if om + 1 <= min(q, k):
            for idx in itertools.combinations(range(q), om + 1):
                for cidx in itertools.combinations(range(k), om + 1):
                    higher.append(sp.expand(P.extract(idx, cidx).det()))
        lower = []
        if om >= 1:
            for idx in itertools.combinations(range(q), om):
                for cidx in itertools.combinations(range(k), om):
                    lower.append(sp.expand(P.extract(idx, cidx).det()))
        lower = [m for m in lower if sp.expand(m) != 0]
        g = sp.factor(sp.gcd_list(lower)) if lower else sp.Integer(0)
        print(f'-- omega={om}: #higher={len(higher)}, #lower={len(lower)}, gcd={g}')


if __name__ == '__main__':
    lam = sp.symbols('lam')
    r1, r2, z = sp.symbols('r1 r2 z')

    # 598: 右铅笔乘积门
    H = sp.Matrix([[r1, z, 0], [1, r2, 0], [0, 0, 0]])
    Z = sp.diag(0, 1, 0)
    stratum_report(H, H * Z, '598')

    # 613: 不可约 Z'（循环）乘积门
    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    H = sp.Matrix([[r1, z, 0], [1, r2, 0], [0, 0, 1]])
    stratum_report(H, H * C, '613')
