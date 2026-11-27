"""OPT and FIND under the subspace reduction — exact verification.

Claim.  Write M = [N | A N], T = row M, W_0 = row(L_0 M), and for a feasible
L = [L_0; R] let W = row(L M) and t = dim(W/W_0).  Then

  (A) t <= r, and the same W is realised by exactly t free rows;
  (B) hence DEC(q) at order q = r_0 + r implies DEC(r_0 + t): the witness can be
      compressed to the minimal order compatible with its own W;
  (C) q_min = r_0 + t_min, t_min = min{ dim(W/W_0) : W feasible },
      and t_min <= m = d - s <= 2k;
  (D) FIND: the compressed witness is an explicit rational R at order r_0 + t.

The script looks for feasible witnesses at several orders and compresses each to
its own t, verifying the compressed witness exactly.  The best (smallest) order
seen over all witnesses is an upper bound on q_min.

Exact arithmetic (5a)/(5b) test.  NOT a proof: finitely many instances.
"""

import random

import sympy as sp

import c320_subspace_reduction as S


def data(A, C, L0):
    CA = C * A
    N = S.nullspace_basis(sp.Matrix.vstack(C, CA))
    M = sp.Matrix.hstack(N, A * N) if N.cols else sp.zeros(A.rows, 0)
    T = S.rowspace_basis(M)
    W0 = S.rowspace_basis(L0 * M)
    return N, M, T, W0


def quotient_basis(W, W0):
    rows, cur = [], W0
    for i in range(W.rows):
        cand = sp.Matrix.vstack(cur, W.row(i))
        if cand.rank() > cur.rank():
            rows.append(W.row(i))
            cur = cand
    return rows


def compress(A, C, L0, L, M, W0, r):
    """Return (t, R_compressed) realising row(L M) with t free rows, or None."""
    W = S.rowspace_basis(L * M)
    rows = quotient_basis(W, W0)
    t = len(rows)
    if t > r:
        return None
    us = [S.preimage(M, w) for w in rows]
    if any(u is None for u in us):
        return None
    R = sp.Matrix.vstack(*us) if us else sp.zeros(0, A.cols)
    return t, R


def main():
    rng = random.Random(9091)
    best = {}
    rows = []
    for _ in range(14):
        n = rng.choice([5, 6, 7])
        p = rng.choice([1, 2])
        r0 = rng.choice([1, 2])
        A = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)])
        C = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)])
        if C.rank() < p:
            continue
        L0 = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(r0)])
        if L0.rank() < r0:
            continue
        N, M, T, W0 = data(A, C, L0)
        k, d, s = N.cols, T.rank(), W0.rank()
        m = d - s
        found = None
        for r in range(1, min(n - r0, 4) + 1):
            q = r0 + r
            for _ in range(60):
                R = sp.Matrix([[rng.randint(-3, 3) for _ in range(n)] for _ in range(r)])
                L = sp.Matrix.vstack(L0, R)
                ok, _why = S.feasible(A, C, L)
                if not ok:
                    continue
                res = compress(A, C, L0, L, M, W0, r)
                if res is None:
                    rows.append((n, p, r0, q, 'compress-failed'))
                    break
                t, Rc = res
                # verify the compressed witness at order r_0 + t
                Lc = sp.Matrix.vstack(L0, Rc) if t else L0
                ok2, why2 = S.feasible(A, C, Lc)
                rows.append((n, p, r0, q, t, ok2, why2))
                if ok2:
                    found = min(found or 10 ** 9, r0 + t)
                break
        if found is not None:
            best[(n, p, r0)] = (k, d, s, m, found)
    ok_count = sum(1 for row in rows if len(row) == 7 and row[5])
    bad = [row for row in rows if len(row) == 7 and not row[5]]
    print(f"witnesses examined: {sum(1 for r in rows if len(r) == 7)}; compressed and re-verified: {ok_count}; failures: {len(bad)}")
    for b in bad[:5]:
        print("  FAIL", b)
    print("instance -> (k, d, s, m, best order found)")
    for key in sorted(best):
        print(f"  n={key[0]} p={key[1]} r0={key[2]}: {best[key]}")
    print("\nnote: the reported order is an upper bound on q_min = r_0 + t_min, "
          "because it comes from an explicit witness.")


if __name__ == '__main__':
    main()
