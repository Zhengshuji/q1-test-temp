# The middle layer of the compressed observer: criterion, chartwise decision, and what is still open

This report corrects and consolidates the layer analysis of the compressed observer. Several earlier
statements of ours were wrong and are listed as such. What survives is a criterion for a fixed row space, a
chartwise decision procedure suggested by the hyperplane-layer paper, and an honest list of what the three
papers (and this note) still leave open — chiefly the complexity of the decision problem itself.

---

## Part I. Setting

\(A\in\mathbb Q^{n\times n}\), \(C\in\mathbb Q^{p\times n}\), \(L_0\in\mathbb Q^{r_0\times n}\); witness
\(R\in\mathbb F^{m\times n}\), \(\mathcal L=[L_0;R]\), and
\[
K_0=\ker[C;CA],\quad k=\dim K_0,\quad N\text{ a basis},\quad H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H,
\]
\[
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda .
\]
The decision is \(\exists R\), decomposed over the layer number:
\(\text{decision}=\bigvee_{\omega=0}^{k}(\text{layer }\omega\text{ feasible})\).

Notation. \(\mathcal S=\operatorname{row}[N\ AN]\subseteq V\oplus V\) is the space of compressed pairs
\((rN,rAN)\); \(V=\mathbb F^{1\times k}\). For \(\omega\)-dimensional \(W\subseteq V\),
\[
\mathcal T_W=\mathcal S\cap(W\oplus W),\qquad
\pi_j:\mathcal T_W\to W\ \text{the two projections},\qquad
E_\lambda(x,y)=\lambda x-y .
\]
Fixed rows give \(h_i^0=(L_0)_iN\), \(g_i^0=(L_0)_iAN\), \(V_0=\operatorname{span}\{h_i^0\}\), and the compatible
loci are \(\{W:U\subseteq W\}\cong\operatorname{Gr}(\omega-d,k-d)\) with \(U=\operatorname{span}\{h_i^0,g_i^0\}\), \(d=\dim U\).

Three standing facts: the **kernel lemma** (\(\ker H=\ker H_A\)); **fibrewise rigidity** (the feasible set in a
fibre is Zariski open, so no polynomial condition can be imposed on the free rows beyond the fibre); and the
**structural bound of Paper I**, \(\omega+1\le\dim W\le 2\omega\), with \(\dim W\le2\ell\), \(\ell=\operatorname{rank}(AN)\).

---

## Part II. Results

### II.1 The spectral condition simplifies to one subspace equality

Since \(E_\lambda(\mathcal T_W)=\lambda\pi_1(\mathcal T_W)+\pi_2(\mathcal T_W)\), at \(\lambda=0\) one gets
\(E_0=-\pi_2\), and conversely \(\pi_2(\mathcal T_W)=W\) makes \(E_\lambda\supseteq W\) for every \(\lambda\). Hence
\[
\boxed{E_\lambda(\mathcal T_W)=W\ \ \forall\lambda\iff \pi_2(\mathcal T_W)=W.}
\]
No maximal-minor gcd is needed for this condition, and no homogenisation at \(\lambda=\infty\): a single
subspace equality suffices.

### II.2 Criterion for a fixed row space

> **Proposition.** Fix a compatible \(W\) and suppose \(m\ge\dim\mathcal T_W\). Then layer \(\omega\) is feasible on
> the fibre of \(W\) if and only if
> \[
> \textbf{(R)}\ \operatorname{span}\bigl(V_0\cup\pi_1(\mathcal T_W)\bigr)=W,
> \qquad \textbf{(E)}\ \pi_2(\mathcal T_W)=W .
> \]

Sketch. \((\Rightarrow)\) feasibility gives \(\operatorname{rank}H=\omega\), so the first components of the fixed
and free rows span \(W\), which is (R); the pencil rows are the evaluations of pairs in \(\mathcal T_W\), so rank
\(\omega\) forces (E). \((\Leftarrow)\) take a basis of \(\mathcal T_W\) as the free rows; (R) gives rank
\(H=\omega\), (E) gives rank \(\omega\) for the pencil at every \(\lambda\).

Note that (E) does **not** imply (R): \(\mathcal T_W=\{0\}\oplus W\) satisfies (E) while \(\pi_1=0\). This is the
correction of an earlier version of this report, which asserted the criterion with the spectral condition alone.

### II.3 The set of feasible row spaces, and a chartwise decision

Writing \(W=\ker q^{\mathsf T}\) and \((x,y)=B\theta\) with \(B\) a basis matrix of \(\mathcal S\), the admissible
pairs are the solutions of \(M(q)\theta=0\) with
\[
M(q)=\begin{pmatrix}q^{\mathsf T}&0\\0&q^{\mathsf T}\end{pmatrix}B .
\]
Both conditions are "some minor is non-zero" within a stratum where \(\operatorname{rank}M(q)\) is constant; hence
the feasible set is **constructible** (a finite union of locally closed pieces), not in general open or closed.

Consequently a *single generic* test is not a decision procedure. Testing a generic point of the whole space
returned "infeasible" in every case of a small experiment, while exhaustive enumeration over a grid found feasible
points — the feasible points lay in coordinate charts that the generic point does not represent. The correct
device is the one used in the hyperplane-layer paper: on a chart of the parameter space, coprimality over the
function field implies feasibility at **every** point of the chart (a Bézout identity with polynomial
coefficients specialises everywhere). Both of our conditions are of "some minor is non-zero" type, so the same
argument applies, and one computation per chart decides the chart.

Experimentally, replacing exhaustive enumeration by **one generic point per chart** (three charts for
\(\operatorname{Gr}(2,3)\)) reproduced the enumeration's answer in \(4/4\) instances, including one feasible one.

### II.4 Other layers

* \(\omega=0\): feasible iff \(L_0[N\ AN]=0\) (take \(R=0\)).
* \(\omega=k\): rank completion is possible iff \(m\ge k-\operatorname{rank}(L_0N)\); a necessary condition is
  \(\operatorname{rank}((\lambda I-A)N)=k\) for all \(\lambda\). Sufficiency of the latter was verified on rational
  instances but is **not proved**.

### II.5 Corrections of earlier statements

1. "Every middle layer is infeasible" — false; rational feasible examples exist.
2. "The middle-layer criterion is \(\mathcal T_W=W\oplus W\), i.e. \(\dim=2\omega\)" — false; a subspace of
   dimension \(2\omega-1\) can satisfy the spectral condition (take \(\mathcal T=\ker(\alpha+\beta)\) with
   \(\alpha\notin\operatorname{span}\beta\)).
3. "The conditions are open, so a generic point decides" — false; the feasible set is constructible.
4. "A single generic point fails, so the spectral condition is not sufficient" — the diagnosis was wrong; the
   failure came from testing the wrong chart.
5. "The middle-layer conditions are closed (a fixed-point set)" — also wrong; the right description is
   constructible, decided chartwise.

---

## Part III. Questions

**Q1.** Does the "one computation per chart" lemma hold for arbitrary layer numbers \(\omega\), or is its proof
specific to the hyperplane layer \(\omega=k-1\)? In our setting the chart lives in
\(\operatorname{Gr}(\omega-d,k-d)\) and the conditions are "some minor non-zero", but we have not verified that
the proof of the lemma does not use \(\omega=k-1\).

**Q2.** With the criterion of II.2 and the chartwise decision of II.3, is the middle layer decidable in time
polynomial in the input length for fixed \(\ell\)? The chart count and the cost of one chart's computation both
grow with \(\ell\); is the resulting bound comparable to the \(\exp(O(\ell^{2}\log(\ell+2)))\) of the decision
problem in the companion paper, or better?

**Q3.** The review of the companion papers recommends embedding an \(\exists\mathbb R\)-hard problem into the two
coupled rank conditions. Which target is best matched by (R) and (E)? Candidates we see are 0–1 linear
feasibility and subspace problems with prescribed intersection dimensions. Is one of them known to be
\(\exists\mathbb R\)-hard in exactly this form?

**Q4.** Is there a structural reason why the decision should be in P — for instance, that the two conditions are
projections of one subspace and the \(\ell\)-parameterisation bounds the search — or is there a known hardness for
"\(\exists W\) with prescribed projection ranks", which would transfer here?

**Q5.** Which single statement would you regard as decisive for the complexity of the decision problem: a
polynomial algorithm for II.3 including the repeated-spectrum case, or a reduction? And in the second case,
which of the two conditions is the natural place to put the gadget — (R) (a span condition) or (E) (a projection
equality)?

### Reliability

| item | label |
|---|---|
| kernel lemma, fibrewise rigidity, compatibility loci | proved |
| structural bound \(\omega+1\le\dim W\le2\omega\), \(\dim W\le2\ell\) | proved (companion paper) |
| (E) \(\iff\pi_2(\mathcal T_W)=W\) | proved |
| criterion of II.2 | proved |
| feasible set is constructible | proved |
| chartwise ("one computation per chart") | transplanted from the hyperplane paper; verified experimentally 4/4 |
| \(\omega=0\) and rank-completion threshold | proved |
| top-layer spectral sufficiency | verified only |
| complexity of the decision problem | **open** |
