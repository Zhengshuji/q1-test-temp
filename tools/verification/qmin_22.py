"""qmin_22.py —— $(p,r)=(2,2)$：$q_{\\min}$ 与 $q_0$ 的关系（按 $\\delta$ 分层）"""
import os, sys, itertools, random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))
import linalg_q as LQ
import z_generator as ZG
import qmin_scan_pr as QR
import c208_q0_lower_bound as Q0
import decide_symbolic as DS
import observability_test as OT

F = Fraction

def main():
    rng = random.Random(20261123)
    st = Counter()
    for trial in range(600):
        n = rng.choice([6, 7])
        p = r = 2
        A = [[F(rng.randrange(-2,3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2,3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2,3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r: continue
        if LQ.rank([list(x) for x in C] + L0) != p + r: continue
        O = QR.observability_matrix(A, C); n0 = LQ.rank(O)
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n: continue
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]): continue
        k = len(K[0]); q0 = Q0.eta_and_q0(A, C, L0)[0]
        qmin = None
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d <= 0 or d > k: continue
            found = False
            for rows in itertools.combinations(range(k), d):
                for b in (0,1):
                    Z = DS.Z_from_theta(A, C, L0, q, rows, [F(b)]*(d*(k-d)))
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d: continue
                    try: L = ZG.L_from_Z(A, C, L0, Z, q)
                    except AssertionError: continue
                    if L is None or not LQ.condA(A, C, L): continue
                    ok, _ = OT.observability_ok(A, C, L)
                    if ok:
                        found = True; break
                if found: break
            if found:
                qmin = q; break
        st['实例'] += 1
        if qmin is None:
            st['未找到可行'] += 1
        else:
            st[f' qmin-q0 = {qmin - q0}'] += 1
            st[f' qmin = n-1' if qmin == n-1 else f' qmin < n-1'] += 1
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')

if __name__ == '__main__':
    main()
