"""c190_invariant_family.py -- the row(L0)=J family: q_min = n  (exact, proved)

WHAT
----
For instances with  row(L0) = J  (equivalently r = c0 = j) we prove

    q_min = min{ dim V : V is A-invariant, V >= J, (5b) }            (*)

Reason: V >= row(L0) = J gives  dim(V n J) = j  and  V + J = V, hence

    (5a)  <=>  V A <= V + J = V  <=>  V is A-invariant.

Consequence.  If  <J>_A = C^n  and  C^n satisfies (5b), then (*) forces V = C^n,
so  q_min = n  -- the maximum possible value.  In that case the only feasible V
is C^n, so  rho* = d, and

    max(r + eps, rho* + 1) = max(j+1, d+1) < n = q_min      (when j >= 2)

Hence  q_min = max(r+eps, rho*+1)  and  q_min = dim V + 1  are BOTH refuted
rigorously -- no sampling, no field caveat.  The surviving closed form

    q_min = max(r + eps, rho* + max(c0,1))

is met exactly (rho* = d, c0 = j, eps = 1, so the right side is j + d = n).

WHY THIS FAMILY WAS MISSED
--------------------------
It needs  row(L0) = J  (a codimension condition).  Random sampling hits it with
probability zero; the census in Q1_FOR_EXPERT_9 (n in {4,5}) never saw it.

USAGE
-----
    python tools/certificates/c190_invariant_family.py
    python tools/certificates/c190_invariant_family.py --n 6 --k 5

Everything is exact over Q (scripts/core/audit_independent.py).
"""
import sys, os, json, math, random

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))          # .../q1_true/scripts -> ...
sys.path.insert(0, os.path.join(_ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import audit_independent as AI

mul, rank, inv = AI.mul, AI.rank, AI.inv


# ------------------------------------------------------------------ helpers

def to_F(rows):
    return [[Fr(x) for x in r] for r in rows]


def is_int(x):
    return isinstance(x, Fr) and x.denominator == 1


def intify(rows):
    """Fraction rows -> int rows (entries must be integral)."""
    return [[int(x) for x in r] for r in rows]


def integer_version(rows):
    """Clear denominators of a rational row list, keeping the row space."""
    den = 1
    for r in rows:
        for x in r:
            den = den * x.denominator // math.gcd(den, x.denominator)
    return [[Fr(int(x * den)) for x in r] for r in rows]


def basic(A, C):
    n = len(A)
    CA = mul(C, A)
    M = AI.vstack([C, CA])
    j = rank(M)
    J = AI.row_basis(M)
    Nv = AI.nullspace(M)
    N = [[Nv[k][i] for k in range(len(Nv))] for i in range(n)]
    return dict(n=n, CA=CA, J=J, j=j, d=n - j, N=N)


def complement(J, n, d):
    """A basis of a complement of J, built greedily from the standard basis."""
    W = []
    for i in range(n):
        v = [Fr(0)] * n
        v[i] = Fr(1)
        if rank(AI.vstack([J, W + [v]])) == len(J) + len(W) + 1:
            W.append(v)
        if len(W) == d:
            break
    return W


def cond(A, C, L):
    return AI.cond_5a_orig(A, C, L) and AI.cond_5b_orig(A, C, L)


# ------------------------------------------------------------------ analysis

def analyse(A, C, L0):
    """Full diagnostics for one instance.  hypothesis = (row(L0) == J)."""
    D = basic(A, C)
    n, j, d, J, N = D["n"], D["j"], D["d"], D["J"], D["N"]
    S = AI.row_basis(L0)
    c0 = len(S) + j - rank(AI.vstack([S, J]))
    hyp = (len(S) == j == len(L0)) and all(AI.in_span(r, J) for r in L0)

    W = complement(J, n, d)
    B = [list(r) for r in J] + [list(w) for w in W]
    Binv = inv(B)

    def proj(x):
        """coordinates on W, i.e. the projection along J"""
        return mul([x], Binv)[0][j:]

    def T(x):
        """the compressed operator  x |-> proj( x A )  on W (row action)"""
        v = [sum(x[k] * W[k][t] for k in range(d)) for t in range(n)]
        return proj(mul([v], A)[0])

    E = AI.row_basis([proj(mul([r], A)[0]) for r in J]) if J else []

    # T-closure of E: the smallest T-invariant subspace containing E
    clo = [list(r) for r in E]
    while True:
        nxt = AI.row_basis(clo + [T(x) for x in clo])
        if len(nxt) == len(clo):
            break
        clo = nxt

    # ambient A-closure of J:  <J>_A = J + JA + JA^2 + ...
    clo_amb = [list(r) for r in J]
    while True:
        nxt = AI.row_basis(clo_amb + [mul([r], A)[0] for r in clo_amb])
        if len(nxt) == len(clo_amb):
            break
        clo_amb = nxt

    Cn = [[Fr(1) if i == k else Fr(0) for k in range(n)] for i in range(n)]
    cn_ok = cond(A, C, Cn)
    L0_ok = cond(A, C, L0)
    JA = AI.row_basis([mul([r], A)[0] for r in J])
    J_inv = rank(AI.vstack([J, JA])) == j if J else True
    rho_cn = rank(mul(Cn, N))

    # the old reduced quantity "dim V" (<= S >_{A'} in K-coordinates), for reference
    old_dimV = None
    if d > 0:
        # A' = (N^T N)^{-1} N^T A N ;  R0 = A N - N A' ;  V = closure of row(R0) under A'
        NtN = mul(AI.tr(N), N)
        Ap = mul(inv(NtN), mul(AI.tr(N), mul(A, N)))
        R0 = [[mul(A, N)[i][k] - mul(N, Ap)[i][k] for k in range(d)] for i in range(n)]
        Vr = AI.row_basis(R0)
        while Vr:
            V2 = AI.row_basis(Vr + mul(Vr, Ap))
            if len(V2) == len(Vr):
                break
            Vr = V2
        old_dimV = len(Vr)

    q_min = n if (hyp and not J_inv and len(clo_amb) == n and cn_ok) else None
    return dict(n=n, j=j, d=d, c0=c0, hyp=hyp, J=J, W=W, proj=proj, T=T, E=E,
                closure=len(clo), closure_ambient=len(clo_amb),
                Cn=Cn, cn_feasible=cn_ok, L0_feasible=L0_ok, old_dimV=old_dimV,
                J_A_invariant=J_inv, rho_cn=rho_cn, q_min=q_min,
                rho_star=(rho_cn if q_min is not None else None))


def probe_no_smaller(A, C, L0, trials=120, rng=None):
    """Machine check of the closure step: for every dim q < n, (5a) must fail.

    (By the theorem this is forced: (5a) => V invariant >= <J>_A = C^n.)
    Returns the list of q for which a (5a)-satisfying V was found (should be empty).
    """
    rng = rng or random.Random(0)
    n = len(A)
    bad = []
    for q in range(len(L0), n):
        for _ in range(trials):
            V = [list(r) for r in L0] + [[Fr(rng.randint(-2, 2)) for _ in range(n)]
                                         for _ in range(q - len(L0))]
            if rank(V) != q:
                continue
            if AI.cond_5a_orig(A, C, V):
                bad.append(q)
                break
    return bad


# ------------------------------------------------------------------ generator

def generate(seed=4242, k=8, n=5, max_tries=40000):
    """Instances with row(L0) = J, J not A-invariant, <J>_A = C^n."""
    rng = random.Random(seed)
    out = []
    tries = 0
    while len(out) < k and tries < max_tries:
        tries += 1
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
        if rank(C) != 1:
            continue
        D = basic(A, C)
        if D["j"] != 2 or D["d"] < 2:
            continue
        J = D["J"]
        JA = AI.row_basis([mul([r], A)[0] for r in J])
        if rank(AI.vstack([J, JA])) == D["j"]:
            continue                                   # want J NOT A-invariant
        L0 = integer_version(J)                        # row(L0) == J exactly
        info = analyse(A, C, L0)
        if info["q_min"] is None:
            continue
        out.append((A, C, L0, info))
    return out


# ------------------------------------------------------------------ report

def main():
    n = 5
    k = 8
    if "--n" in sys.argv:
        n = int(sys.argv[sys.argv.index("--n") + 1])
    if "--k" in sys.argv:
        k = int(sys.argv[sys.argv.index("--k") + 1])

    print("=" * 96)
    print("c190 -- family  row(L0) = J  =>  every feasible V is A-invariant and contains J")
    print("=" * 96)
    print(f"  n={n}  p=1  r=j=2  ;  exact over Q")
    print()

    insts = generate(seed=4242, k=k, n=n)
    if not insts:
        print("  no instance found -- increase the search budget")
        return

    hdr = ("  #   j  d  c0 eps  dim<J>_A  C^n?  L0?  JA<=J?  T-clo  q_min   "
           "max(r+eps,rho*+1)   d+c0   unified")
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))

    proof_rows = []
    for t, (A, C, L0, info) in enumerate(insts, 1):
        n_ = info["n"]; j = info["j"]; d = info["d"]; c0 = info["c0"]
        eps = 0 if info["L0_feasible"] else 1
        q = info["q_min"]; rs = info["rho_star"]
        f2 = max(2 + eps, rs + 1)
        f3 = max(2 + eps, rs + max(c0, 1))
        print(f"  {t:2d}  {j:2d} {d:2d}  {c0:2d}  {eps:2d}   {info['closure_ambient']:5d}   "
              f"{str(info['cn_feasible']):5s} {str(info['L0_feasible']):5s} "
              f"{str(info['J_A_invariant']):6s}   {info['closure']:2d}     {q:2d}      "
              f"{f2:2d}                  {d + max(c0,1):2d}    {f3:2d}")
        if info["q_min"] is not None:
            proof_rows.append((t, A, C, L0, info))

    q0 = proof_rows[0]
    _, A, C, L0, info = q0
    eps = 0 if info["L0_feasible"] else 1
    print()
    print("  every instance above has  q_min = n  (proved); the d+1 layer is EMPTY.")
    print(f"  check on instance 1:  old reduced dim V = {info['old_dimV']} "
          f"(so dim V+1 = {None if info['old_dimV'] is None else info['old_dimV'] + 1}),  "
          f"max(r+eps, rho*+1) = {max(2 + eps, info['rho_star'] + 1)},  "
          f"q_min = {info['q_min']}")

    # ---- machine check of the closure step on instance 1
    bad = probe_no_smaller(A, C, L0, trials=80, rng=random.Random(7))
    print(f"  probe: any (5a)-satisfying V of dim < n ?  {'YES ' + str(bad) if bad else 'no (as proved)'}")

    # ---- export a certificate
    out = dict(
        name="counterexample_max_r_eps_rho_star_plus1",
        date="2026-10-26",
        problem="MIN-ROWS (q1)",
        n=info["n"], p=1, r=len(L0),
        A=intify(A), C=intify(C), L0=intify(L0),
        computed=dict(j=info["j"], d=info["d"], c0=info["c0"],
                      eps=eps, rho_star=info["rho_star"], q_min=info["q_min"],
                      dim_closure_J_under_A=info["closure_ambient"],
                      old_reduced_dimV=info["old_dimV"],
                      J_A_invariant=info["J_A_invariant"],
                      C_whole_space_feasible=info["cn_feasible"],
                      L0_feasible=info["L0_feasible"]),
        refutes=[
            "q_min = max(r + eps, rho* + 1)",
            "q_min = dim V + 1",
        ],
        supports=True,
        proof=("row(L0) = J and J is not A-invariant, so (5a) makes V A-invariant; "
               "V >= J forces dim(V n J) = j = 2 and V >= <J>_A = C^n, hence V = C^n; "
               "C^n satisfies (5a)(5b) exactly, so q_min = n. "
               "rho* = d because C^n is the only feasible V."),
        verifier="tools/certificates/c190_invariant_family.py (Q exact), c189_ledger.py",
        field_convention="L rational (all searches in this project are rational)",
    )
    path = os.path.join(_ROOT, "proof", "refuted", "certificates",
                        f"counterexample_max_r_eps_rho_star_plus1_n{info['n']}_2026-10-26.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\n  certificate written: {os.path.relpath(path, _ROOT)}")
    print()
    print("  NOTE: q_min = n is the maximum possible value, yet this family is")
    print("  polynomially decidable (compute <J>_A).  So it kills the closed forms")
    print("  without providing hardness: q1 stays open.")


if __name__ == "__main__":
    main()
