"""在 F_3 上**完全枚举**候选实例 (3,1) 层的全部合法 V，并按"子式次数分层"给出每个分层的覆盖情况。

复用 enum_31_finitefield.py 的有限域算术（P=3）。

对每个合法 V：
  * polys = 全部 3x3 子式（F_3[lam]）；
  * dstar = max deg；N = len(polys)；
  * gcd 判据：(5b) <=> gcd 是非零常数；
  * Bezout 判据：D = 2*dstar*(N-1)，M_D 满射 <=> (5b)；
  * pattern = 排序后的次数元组。
输出：
  - 每个 pattern 下的 V 数与其中 (5b) 成立的个数（=> 该分层是否被完全覆盖）；
  - gcd 判据与 Bezout 判据是否一致。
"""
import importlib.util
import itertools
import json
import sys

spec = importlib.util.spec_from_file_location('E', 'proof/rho1_layer/enum_31_finitefield.py')
E = importlib.util.module_from_spec(spec)
spec.loader.exec_module(E)

P = E.P


def minors_fp(rows, rho, d):
    """rows[i] = (vec, vecA)；返回全部 rho x rho 子式的多项式（F_p[lam]，系数升序）。"""
    out = []
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(d), rho):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            val = E.det_poly(M)
            if not (len(val) == 1 and val[0] % P == 0):
                out.append(val)
    return out


def bezout_rank_full(polys, dstar, D):
    rows = dstar + D + 1
    cols = len(polys) * (D + 1)
    M = [[0] * cols for _ in range(rows)]
    col = 0
    for p in polys:
        for sh in range(D + 1):
            for k, c in enumerate(p):
                if sh + k < rows:
                    M[sh + k][col] = c % P
            col += 1
    return E.rank(M), rows


def main():
    d0 = json.load(open('proof/rho1_layer/candidate_c31_counterexample.json', encoding='utf-8'))[0]
    A = [[int(x) for x in r] for r in d0['A']]
    C = [[int(x) for x in r] for r in d0['C']]
    L0 = [[int(x) for x in r] for r in d0['L0']]
    n = len(A)
    CA = E.mm(C, A)
    J = E.row_basis(E.vstack(C, CA))
    j = len(J)
    rho, c = 3, 1

    strata = {}
    agree = 0
    total = 0
    for pivots in itertools.combinations(range(n), 4):
        free = [cc for cc in range(n) if cc not in pivots]
        for vals in itertools.product(range(P), repeat=4 * len(free)):
            M = [[0] * n for _ in range(4)]
            for i, pc in enumerate(pivots):
                M[i][pc] = 1
            idx = 0
            for i in range(4):
                for fc in free:
                    M[i][fc] = vals[idx]
                    idx += 1
            L = E.row_basis(M)
            if len(L) != 4:
                continue
            if not all(E.in_span(L, r) for r in L0):
                continue
            if E.rank(E.vstack(L, CA, C)) - j != rho:
                continue
            if len(L) + j - E.rank(E.vstack(L, J)) != c:
                continue
            if not E.cond_5a(L, A, C):
                continue
            # 铅笔必须是 [lam*L - L*A ; CA ; C]：L 的行是 lam 一次的，CA/C 的行是常数
            rows = [(L[i], E.mm([L[i]], A)[0]) for i in range(4)]
            for r in CA:
                rows.append(([0] * n, [x % P for x in r]))
            for r in C:
                rows.append(([0] * n, [x % P for x in r]))
            polys = minors_fp(rows, rho, n)
            if not polys:
                strata.setdefault(('EMPTY',), [0, 0])
                strata[('EMPTY',)][0] += 1
                continue
            g = polys[0]
            for q in polys[1:]:
                g = E.pgcd(g, q)
            b5 = (len(g) == 1 and g[0] % P != 0)
            dstar = max(len(p) - 1 for p in polys)
            N = len(polys)
            D = 2 * dstar * (N - 1)
            rk, rows_ = bezout_rank_full(polys, dstar, D)
            bz = (rk == rows_)
            if bz == b5:
                agree += 1
            total += 1
            pat = tuple(sorted(len(p) - 1 for p in polys))
            st = strata.setdefault(pat, [0, 0])
            st[0] += 1
            if b5:
                st[1] += 1

    print(f"F_{P}: 合法 V 共 {total} 个")
    print(f"gcd 判据与 Bezout 判据一致: {agree}/{total}")
    print("按次数分层（pattern: [V 数, 其中 (5b) 成立数]）:")
    for k in sorted(strata):
        a, b = strata[k]
        flag = "  <== 该分层被完全覆盖" if b == 0 else ""
        print(f"   {k}: [{a}, {b}]{flag}")


if __name__ == '__main__':
    main()
