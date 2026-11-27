# Workstream B — final report (2 November 2026, night)

**Supersedes** `REPORT_2026-11-02_WORKSTREAM_B_FULL_EN.md` and `NOTE_2026-11-02_T4B_PROVED_EN.md`.
**Status:** the two conjectures of your revised target form T are now **theorems**. Three of our own
claims were found wrong along the way and are retracted with certificates (R18, R19, R20).

Everything is exact rational arithmetic; every claim below is marked **proof** / **verification** /
**Lean kernel**.

---

## 1. Executive summary

| item | status |
|---|---|
| right minimal indices of $Q_L$ | **Theorem B.6**: $(5a)\Rightarrow$ all zero (no $(5b)$ needed) — paper proof + Lean kernel + 150/150 |
| infinite elementary divisors of $Q_L$ | **Theorem B.7 (= T4-b)**: all of degree 1, $d_\infty=h-\operatorname{rank}L$ — paper proof + 151/151 |
| left minimal indices | count $=n-h$ for the right side, $q+2p-h$ for the left; **sum $=\operatorname{rank}L-d_{\rm fin}$** under $(5a)$, and $=\operatorname{rank}L$ when $(5b)$ also holds (**corrected**, see R21) |
| our own errors | **R18** (constant rank ⇏ zero right indices), **R19** ($\ker L=N$ wrong equivalence), **R20** ($d_\infty$ measured with degrees instead of $\mu$-adic valuations) |

Consequence: the Kronecker data of an observer pencil is **completely determined in aggregate** by
$(q,p,h,\operatorname{rank}L)$. The only remaining freedom is the *individual* left minimal indices
$\varepsilon_1\ge\cdots\ge\varepsilon_{q+2p-h}$ with $\sum_j\varepsilon_j=\operatorname{rank}L$.

---

## 2. Setting and notation

$A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L\in\mathbb C^{q\times n}$,
$$Q_L(\lambda)=\begin{bmatrix}\lambda L-LA\\ CA\\ C\end{bmatrix},\qquad
H=\begin{bmatrix}L\\CA\\C\end{bmatrix},\qquad h=\operatorname{rank}H .$$
$(5a)$: $\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]$, equivalently
$\operatorname{row}(LA)\subseteq\operatorname{row}(L;CA;C)$.
$(5b)$: $\operatorname{rank}Q_L(\lambda)=h$ for all $\lambda$.

---

## 3. Theorem B.6 — right minimal indices vanish

**Statement.** If $(5a)$ holds, every polynomial right null vector $v(\lambda)=\sum_{k\le d}\lambda^kv_k$
of $Q_L$ has all its coefficients in $N=\ker L\cap\ker LA\cap\ker C\cap\ker CA$. Hence the right null
module is $N\otimes\mathbb C[\lambda]$ and **all right minimal indices are $0$**.

**Proof.** Expand $Q_L(\lambda)v(\lambda)\equiv0$ in powers of $\lambda$: $LAv_0=0$;
$Lv_k=LAv_{k+1}$ ($0\le k<d$), so $Lv_d=0$; and $Cv_k=CAv_k=0$ for all $k$. Thus
$Lv_d=Cv_d=CAv_d=0$, and by $(5a)$ — written explicitly as $LA=XL+Y_1CA+Y_2C$ — we get $LAv_d=0$.
So $v_d\in N$; subtracting $\lambda^dv_d$ (also a null vector) and inducting on $d$ proves the claim. ∎

*(We thank you for suggesting the explicit factorization $LA=XL+Y_1CA+Y_2C$: it makes the key step a
one-liner, and we use it again in B.7.)*

**Lean kernel.** `proof/kron_null_module` is complemented by
`tools/lean/MyProof/KronCoeff.lean` — `RowContains`, `kron_coeff_chain_strong` (backward induction on the
coefficient equations), `kron_coeff_chain`, `kron_coeff_const`, `kron_coeff_mem_N`; `check_lean.sh` 51/51
OK, registered in `STATEMENT_MAP.md`. The paper part (polynomial ↔ coefficient translation, and
"constant basis ⇒ zero right indices") is **not** Lean-ified and is stated as the difference.

---

## 4. Theorem B.7 (= T4-b) — infinite elementary divisors have degree 1

**Statement.** If $(5a)$ holds, every infinite elementary divisor of $Q_L$ has degree $1$, and
$$d_\infty=h-\operatorname{rank}L .$$
**$(5b)$ is not used.**

**Proof (six steps).**

1. By $(5a)$ there are constant $X\in\mathbb C^{q\times q}$, $Y_1,Y_2\in\mathbb C^{q\times p}$ with
   $LA=XL+Y_1CA+Y_2C$. Then
   $Q_L(\lambda)=P(\lambda)H$ with
   $P(\lambda)=\begin{bmatrix}\lambda I_q-X&-Y_1&-Y_2\\0&I_p&0\\0&0&I_p\end{bmatrix}$.
2. $P(\lambda)=U\operatorname{diag}(\lambda I_q-X,I_{2p})$ with $U$ constant invertible, so $Q_L$ is
   **strictly equivalent** to $M(\lambda)=\begin{bmatrix}(\lambda I_q-X)L\\CA\\C\end{bmatrix}$.
3. With $M=M_0+\lambda M_1$, the infinite divisors of $M$ are the elementary divisors at $\mu=0$ of
   $\widehat M(\mu)=M_1+\mu M_0=\begin{bmatrix}(I_q-\mu X)L\\ \mu CA\\ \mu C\end{bmatrix}$.
4. $\det(I_q-\mu X)|_{\mu=0}=1$, so $I_q-\mu X$ is a unit in $\mathbb C[\mu]_{(\mu)}$; multiplying by
   $\operatorname{diag}((I_q-\mu X)^{-1},I_p,I_p)$ gives the **locally equivalent** pencil
   $\widetilde M(\mu)=\begin{bmatrix}L\\ \mu CA\\ \mu C\end{bmatrix}$.
5. Determinantal divisors of $\widetilde M$: for $k\le r_1:=\operatorname{rank}L$ we get a nonzero
   constant (a minor with only $L$-rows); for $r_1<k\le h$ every nonzero minor uses $j\ge k-r_1$ rows of
   the $\mu$-blocks, and choosing $r_1$ independent $L$-rows plus $k-r_1$ rows of $[CA;C]$ (possible since
   $\operatorname{rank}[L;CA;C]=h\ge k$) attains equality, so $\Delta_k=c_k\mu^{k-r_1}$ with
   $c_k\ne0$; for $k>h$, $\Delta_k=0$.
6. Hence the invariant factors are $r_1$ units and $h-r_1$ copies of $\mu$: all infinite elementary
   divisors have degree $1$, and $d_\infty=h-\operatorname{rank}L$. ∎

**Corollary (corrected).** With $d_{\rm fin}$ the total degree of the finite elementary divisors, B.6 + B.7
and the global identity $\sum\eta+\sum\varepsilon+d_{\rm fin}+d_\infty=h$ give
$$\sum_j\varepsilon_j=\operatorname{rank}L-d_{\rm fin}\quad\text{under }(5a),\qquad
\sum_j\varepsilon_j=\operatorname{rank}L\quad\text{under }(5a)+(5b).$$
Consequences: $d_{\rm fin}\le\operatorname{rank}L$, and under $(5a)+(5b)$ the necessary bound
$\operatorname{rank}L\le q+2p-h$.

**Verification.** `proof/t4b_infinite_divisors/verify.py`: 151 pencils satisfying $(5a)$ for
$n=6,7,8,9,10$ — **43 of them fail $(5b)$** — all have $\mu$-valuation pattern $()$, $(1)$ or $(1,1)$,
and $d_\infty=h-\operatorname{rank}L$. Zero exceptions.

---

## 5. Our three retractions (all with certificates)

| id | what we said | why it is wrong | where |
|---|---|---|---|
| **R18** | constant rank $\Rightarrow$ right minimal indices $0$ | your counterexample $[\lambda\;\;1]$: rank $1$ everywhere, right index $1$ | `proof/refuted` |
| **R19** | $d_\infty=h-\operatorname{rank}L\iff\ker L=N$ | $\dim N=n-h$ and $N\subseteq\ker L$, so $\ker L=N\iff\operatorname{rank}L=h\iff d_\infty=0$ — only the special case; the correct statement is $d_\infty=\dim(\ker L/N)$ | `proof/refuted` |
| **R20** | $d_\infty$ = sum of the **degrees** of the reversed invariants | the infinite divisors are the elementary divisors at $\mu=0$, i.e. the **$\mu$-adic valuations**. Example: invariants $1,1,1,\tfrac14-\mu+\mu^2$ give $2$ by degrees but $0$ by valuation — the degree reading produced a spurious counterexample to T4-b | `proof/refuted` |

R20 also invalidates two numbers we quoted earlier ("103/103", "188/188"): those were computed with the
wrong measure. With the corrected measure the statement holds on 151/151 (including infeasible pencils)
and is now proved.

A fourth negative result, recorded but not a retraction: your literal **T4-b′**
($LAw\in\operatorname{im}L\Rightarrow LAw=0$) fails on 45 of 59 pencils, because for $L$ of full row rank
$\operatorname{im}L=\mathbb C^q$ and the condition is nearly vacuous; those chains live in the singular
part. The determinant-divisor argument replaces it.

---

## 6. What is now determined, and what is not

For an observer pencil $Q_L$ with $(5a)$:

| Kronecker datum | value | source |
|---|---|---|
| right minimal indices | all $0$ | B.6 |
| infinite elementary divisors | all of degree 1, $d_\infty=h-\operatorname{rank}L$ | B.7 |
| number of left minimal indices | $q+2p-h$ | dimensions |
| sum of left minimal indices | $\operatorname{rank}L$ | corollary |
| finite elementary divisors | free (bounded: $d_{\rm fin}\le\operatorname{rank}L$) | corollary |
| **the individual left indices** | **open** | — |

The aggregate data depend on $(n,q,p,h,\operatorname{rank}L)$: there are $n-h$ right and $q+2p-h$ left minimal indices.

So the entire remaining content is: **which partitions of $\operatorname{rank}L$ into $q+2p-h$ parts are
realizable?** Our samples show both extremes (one large index and the rest zero; and spread partitions),
but we have no pattern and no theorem.

---

## 7. Questions

**Q1.** Is the partition question the right final target? Equivalently: can one characterize the possible
left minimal index sequences of $[\lambda L-LA;CA;C]$ in terms of the pair $(A,C)$ — e.g. via the
observability indices of $(A,C)$ and the position of $L$?

**Q2.** Do you see a route to the partition question using the factorization $Q_L=P(\lambda)H$?
We can now compute with $P$ (a linearization of $X$ with two identity blocks) and the constant $H$;
a natural guess is that the left indices are determined by the "observability indices" of the pair
$(X, \text{something})$ plus $\operatorname{rank}L$, but we have not formulated it.

**Q3.** B.6 is Lean-verified at the kernel level; B.7 relies on Smith forms over $\mathbb C[\mu]$ and
determinantal divisors. Is a Lean formalization of B.7 worth it in your view, or is
"[proved on paper] + [exact verification 151/151]" the right permanent status?

---

## 8. Files

| path | content |
|---|---|
| `proof/kron_null_module/` | B.6: theorem.md, verify.py, README |
| `proof/t4b_infinite_divisors/` | B.7: theorem.md (full six-step proof), verify.py (151/151), README |
| `tools/lean/MyProof/KronCoeff.lean` | Lean kernel of B.6 (5 declarations) |
| `proof/refuted/README.md` | R18, R19, R20 with certificates |
| `tools/verification/kronecker_pencil.py` | Kronecker data; `d_infinity` = sum of $\mu$-adic valuations |
| `tools/verification/observer_pencils.py` | builds the actual observer pencil from an instance |
| `docs/02_theorems_proven.md` | B.6, B.7 registered with grades |
| `workspace/kronecker/` | direction index, target form T, running log, raw data |

Reproduce:

```bash
python proof/kron_null_module/verify.py        # B.6: 150/150
python proof/t4b_infinite_divisors/verify.py   # B.7: 151/151
wsl -e bash tools/lean/check_lean.sh           # 51/51 OK
```

---

## 9. Addendum (after your review of this report)

**Your correction is accepted and implemented (R21).** The left-index sum is
$$\sum_j\varepsilon_j=\operatorname{rank}L-d_{\rm fin}\ \text{under }(5a),\qquad
\sum_j\varepsilon_j=\operatorname{rank}L\ \text{under }(5a)+(5b),$$
registered as R21 in `proof/refuted/`, and `proof/t4b_infinite_divisors/verify.py` now asserts the four
identities (including the finite/infinite split) on all 151 pencils. Consequences added: $d_{\rm fin}\le
\operatorname{rank}L$, and the necessary feasibility bound $\operatorname{rank}L\le q+2p-h$.

**Your descriptor reduction is now a lemma (proved + verified).**
`proof/descriptor_reduction/`: with $J$ a basis of the row space of $H^{\mathsf T}$ (i.e. $h$ independent
*columns* of $H$ — taking rows of $H$ instead breaks $\operatorname{rank}E=\operatorname{rank}L$, which we
found numerically), $R(\lambda)=J D(\lambda)^{\mathsf T}=[\lambda E-EX^{\mathsf T}\ B]$ satisfies
$$\{\text{right minimal indices of }R\}=\{\text{left minimal indices of }Q_L\},\qquad
\operatorname{rank}E=\operatorname{rank}L .$$
Proof: $R(\lambda)y=0\iff JD^{\mathsf T}y=0\iff D^{\mathsf T}y\in\ker J=\ker H^{\mathsf T}\iff
Q'(\lambda)^{\mathsf T}y=0$. Verified on 66 pencils ($n=6,7,8$), no exceptions.
