"""Subspace (quotient) reduction of DEC — exact verification.

Claim under test.  Let M = [N | A N] (n x 2k, N a basis of ker[C; CA]),
T = row M, W_0 = row(L_0 M), and for L = [L_0; R] put W = row(L M).  Then

  (i)   W_0 <= W <= T and dim(W/W_0) <= r  (always);
  (ii)  feasibility depends only on W: the conditions are
        pi_2(W) <= pi_1(W) and dim pi_lambda(W) = dim pi_1(W) for all lambda;
  (iii) a feasible W with omega = dim pi_1(W) > 0 satisfies
        omega + 1 <= dim W <= 2 omega;
  (iv)  round trip: from a feasible W one reconstructs free rows that are
        feasible at the same conditions;
  (v)   monotonicity: a feasible L stays feasible after appending zero rows.

Method: search random L for feasibility with the exact (5a)/(5b) test, then
check (i), (iii), (iv), (v) on the witnesses found.  Every printed conclusion is
backed by an exact test.  NOT a proof: finitely many instances, as the project
rules require.
"""

import random
from fractions import Fraction

import sympy as sp

import spectral_gcd as SG


def nullspace_basis(M):
    ns = M.nullspace()
    return sp.Matrix.hstack(*ns) if ns else sp.zeros(M.cols, 0)


def rowspace_basis(M):
    if M.rows == 0:
        return sp.zeros(0, M.cols)
    r = M.T.columnspace()
    return sp.Matrix.hstack(*r).T if r else sp.zeros(0, M.cols)


def preimage(M, w):
    try:
        sol, params = M.T.gauss_jordan_solve(w.T)
    except ValueError:
        return None
    if params:
        sol = sol.subs({p: 0 for p in params})
    u = sp.simplify(sol).T
    if sp.simplify(u * M - w) != sp.zeros(1, M.cols):
        return None
    return u


def feasible(A, C, L):
    CA = C * A
    top = sp.Matrix.vstack(L * A, L, CA, C)
    bot = sp.Matrix.vstack(L, CA, C)
    if top.rank() != bot.rank():
        return False, 'fails (5a)'
    def to_fr(X):
        return [[Fraction(int(sp.Rational(X[i, j]).p), int(sp.Rational(X[i, j]).q))
                 for j in range(X.cols)] for i in range(X.rows)]
    Lf, Af, Cf = to_fr(L), to_fr(A), to_fr(C)
    g, h, cnt = SG.spectral_gcd(Af, Cf, Lf)
    if SG.pdeg(g) != 0:
        return False, f'fails (5b): gcd degree {SG.pdeg(g)}'
    return True, 'ok'


def stats_line(tag, ok, msg, verbose):
    if verbose and not ok:
        print(f"    FAIL {tag}: {msg}")


def run_instance(A, C, L0, q, rng, tries=80, verbose=False):
    n = A.shape[0]
    r0 = L0.rows
    r = q - r0
    CA = C * A
    N = nullspace_basis(sp.Matrix.vstack(C, CA))
    k = N.cols
    M = sp.Matrix.hstack(N, A * N)
    T = rowspace_basis(M)
    d = T.rank()
    W0 = rowspace_basis(L0 * M)
    s = W0.rank()

    found = []
    for _ in range(tries):
        R = sp.Matrix([[rng.randint(-3, 3) for _ in range(n)] for _ in range(r)])
        L = sp.Matrix.vstack(L0, R)
        ok, why = feasible(A, C, L)
        if ok:
            found.append(L)
            break
    if not found:
        return {'feasible': 0, 'k': k, 'd': d, 's': s, 'fail': 0}

    L = found[0]
    fails = 0
    W = rowspace_basis(L * M)
    # (i) sandwich and dimension
    sandwich = (sp.Matrix.vstack(W0, W).rank() == W.rank()) and \
               (sp.Matrix.vstack(W, T).rank() == d)
    wn = sp.Matrix.vstack(W0, W).rank() - s
    stats_line('sandwich', sandwich, f'W0<=W<=T failed', verbose)
    stats_line('dim(W/W0)<=r', wn <= r, f'{wn} > {r}', verbose)
    fails += (not sandwich) + (wn > r)
    # (iii) structural bound
    omega = (L * N).rank()
    bound = (omega == 0) or (omega + 1 <= sp.Matrix.vstack(W0, W).rank() <= 2 * omega)
    stats_line('omega+1<=dimW<=2omega', bound,
               f'dimW={W.rank()}, omega={omega}', verbose)
    fails += (not bound)
    # (iv) round trip from W
    rows, cur = [], W0
    for i in range(W.rows):
        cand = sp.Matrix.vstack(cur, W.row(i))
        if cand.rank() > cur.rank():
            rows.append(W.row(i))
            cur = cand
    us = [preimage(M, w) for w in rows]
    rt_ok = all(u is not None for u in us)
    if rt_ok:
        R2 = sp.Matrix.vstack(*us) if us else sp.zeros(0, n)
        if R2.rows <= r:
            if R2.rows < r:
                R2 = sp.Matrix.vstack(R2, sp.zeros(r - R2.rows, n))
            ok2, why2 = feasible(A, C, sp.Matrix.vstack(L0, R2))
            stats_line('round-trip', ok2, why2, verbose)
            fails += (not ok2)
        else:
            rt_ok = False
    if not rt_ok:
        fails += 1
    # (v) monotonicity
    ok3, why3 = feasible(A, C, sp.Matrix.vstack(L, sp.zeros(1, n)))
    stats_line('monotone', ok3, why3, verbose)
    fails += (not ok3)
    return {'feasible': 1, 'k': k, 'd': d, 's': s, 'omega': omega,
            'dimW': sp.Matrix.vstack(W0, W).rank(), 'fail': fails}


def main():
    rng = random.Random(20261111)
    total = {'instances': 0, 'feasible': 0, 'fail': 0}
    for _ in range(12):
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
        q = rng.choice([min(n, r0 + 1), min(n, r0 + 2), min(n, r0 + 3)])
        res = run_instance(A, C, L0, q, rng, verbose=True)
        total['instances'] += 1
        total['feasible'] += res['feasible']
        total['fail'] += res['fail']
        tag = 'feasible' if res['feasible'] else 'no witness'
        line = f"  n={n} p={p} r0={r0} q={q}: k={res['k']} d={res['d']} s={res['s']} [{tag}]"
        if res['feasible']:
            line += f" omega={res['omega']} dimW={res['dimW']}"
        print(line)
    print(f"\ninstances={total['instances']} with-witness={total['feasible']} FAILURES={total['fail']}")


if __name__ == '__main__':
    main()
