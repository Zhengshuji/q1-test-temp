# Research direction: what to attack next, with proposals

This note replaces the earlier request for a paper plan. **We are not writing the paper now.** The objective is to
advance the project: to settle, or at least sharpen, the complexity question for $q_{\min}$. Everything below is
organised around that; writing can wait until there is a result worth writing.

Part I recalls the setting, Part II compresses the state (including what changed since the last note), and Part III
proposes five concrete lines of attack and asks for your assessment of them — in particular for the ones you would
drop, and for the one you would do first.

Verification levels: **L1** paper proof; **L2** exact arithmetic on instances; **L3** machine-checked (Lean).

---

# Part I. Setting

$A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L_0\in\mathbb C^{r\times n}$,
$\operatorname{rank}[C;L_0]=p+r$, $L_0$ observable, $(C,A)$ observable. A candidate $\mathcal L\in\mathbb C^{q\times n}$
has $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ and $\operatorname{rank}[C;\mathcal L]=p+q$ (hence
$\operatorname{rank}\mathcal L=q$). With $h=\operatorname{rank}[\mathcal L;CA;C]$:

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=h,\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=h\ \ \forall\lambda .$$

$R=\operatorname{row}\mathcal L$; $W=\operatorname{row}[C;CA]$, $\dim W=r_1$; $S=\operatorname{row}[C;L_0]+W$,
$\dim S=s_0$; $V=\ker[C;CA]$; $K=\ker[C;L_0]$; $\mathcal Z=\ker[C;\mathcal L]$; $d=n-p-q$; $\pi$ = quotient by $C$.
**Type I** $:=$ $h\ge q+r_1$; **Type III** $:=$ $h<q+r_1$ with a finite elementary divisor of positive degree.

---

# Part II. State, compressed

1. **Two mechanisms, not three.** The counting-deficiency case $k=q+r_1-h>\operatorname{rank}\mathcal L$ is empty
   (L1 + L3 + L2 93/93), so $(5b)$ fails for counting reasons or for spectral reasons, never both in a third way.

2. **Counting is arithmetic.** $h=s_0+q-\dim(R\cap S)$ (L1 + L2 35/35, 54/54), hence $h\le s_0+q-r$,
   $s_0\le r_1+r$, $\text{Type I}\iff R\cap W=0$, and
   $\text{Type I}\iff s_0=r_1+r$ **and** $R\cap S=\operatorname{row}L_0$ (L2 33/33). If $s_0<r_1+r$, no admissible
   order of that instance is Type I. Machine-checked geometric form: $h=q+r_1-\dim(\pi R\cap\pi W)$.

3. **The spectral condition for a fixed candidate is an observability test.** With
   $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ and $\ker E=\mathcal LV$:
   $(5b)\iff(E,\Lambda)$ observable $\iff\operatorname{rank}[E;E\Lambda;\dots;E\Lambda^{q-1}]=q$ (L1 + L2 44/44).
   The factorization is not canonical; the truth value does not depend on it.

4. **A fixed-candidate-free reformulation** (new, equivalent to the cited nullspace-pencil criterion):
   $$(5b)\ \text{fails at}\ \mathcal Z\iff\exists x\in V\setminus\mathcal Z,\ \lambda:\ (\lambda I-A)x\in\mathcal Z .$$
   L1 (three lines) + L2 (six explicit $(x,\lambda_0)$ certificates on the counterexample, with $\lambda_0$ irrational
   or complex). This version automatically carries the necessary condition $x\notin\mathcal Z$, which the earlier
   "bad-line" language omitted.

5. **Whole-family obstruction.** The proportionality locus $P=\{x\in V:\operatorname{rank}\Phi(x)\le1\}$ with
   $\Phi(x)=(L_0x;L_0Ax)$ is a linear section of a determinantal variety; with
   $\varepsilon=\dim V-\dim P$ one has $\dim S\le n-r_1-1-\varepsilon$ for the set $S$ of bad lines. The covering
   argument ("if $\dim S\ge q-r$ and $h=n$ then no augmentation works") is **conditional**: the image is only
   constructible, so projective dimension theory does not apply as stated; the boundary case is not repaired.

6. **Counterexample.** At $n=6$, $p=r=2$, $q_0=3$ every admissible augmentation fails, and $q_{\min}=4$ with the
   explicit witness recorded earlier ($h=6<q+r_1=8$, so the feasible point is not of counting type).

7. **Encodings.** Two polynomial-size $\exists\mathbb R$ encodings: a structured left inverse, and the observability
   form with the bilinear recurrence $E_{j+1}=E_j\Lambda$; the latter has, per rank branch, 200 variables and 208
   constraints at $n=8,p=r=2,q=4$ and about 570/515 at $n=12$, all of degree $\le2$, times $q+1$ branches for the
   rank stratum. Coefficient bit lengths are polynomial. This is an upper bound, not an algorithm.

8. **A conditional statement.** Under "counting-spectral separation" (every admissible non-Type-I augmentation is
   spectrally feasible), feasibility at order $q$ is equivalent to the existence of an admissible augmentation with
   $h<q+r_1$. If, in addition, that existence question is decidable in polynomial time on a given class — which is
   *not* automatic when $(5a)$ restricts the admissible row spaces — then $q_{\min}$ is polynomial-time computable
   on that class.

---

# Part III. Proposals and questions

We list five lines of attack in the order we would rank them, each with what it would settle and what it needs. We
would like to know which ones you consider promising, which are dead ends, and whether something obvious is missing.

## Proposal A. Make the canonical reformulation the object of study

The reformulation of II.4 says: order $q$ is feasible iff

$$\exists\,\mathcal Z\in\mathrm{Gr}(d,K)\ \ \forall x\in V\setminus\mathcal Z,\ \forall\lambda:\
(\lambda I-A)x\notin\mathcal Z ,$$

subject to $(5a)$ (which is automatic when $h=n$). This is a $\exists\forall$ condition over a Grassmannian with an
algebraic inner condition, and it no longer mentions pencils, indices, or $\lambda$-quantification over a matrix.

*What it would settle:* whether $q1$ is an instance of a recognisable problem class. If this object has a name or a
known complexity in the algebraic-geometry or real-algebraic literature, we would know immediately whether to look
for an algorithm or for hardness.
*What it needs:* a literature search phrased in this shape ("does a subspace of dimension $d$ avoid an algebraic
family", "$\exists\forall$ over Grassmannians"), and a comparison with $\exists\mathbb R$-complete problems of the
same quantifier shape.

**Question A.** Do you recognise this shape? Is there a known hard problem of the form "there exists a $d$-subspace
avoiding a family of subspaces" that we should compare with?

## Proposal B. Decide whether the counterexample is isolated or the tip of a family

Whole-family spectral infeasibility is currently known in exactly one instance. The necessary condition of II.5
($q-r+\varepsilon\le n-r_1-1$, with $\varepsilon$ the codimension of the proportionality locus, hence $0$ whenever
the proportionality quadrics vanish identically on $V$) predicts where to look: $h=n$, $\varepsilon=0$, and the
dimension count tight.

*What it would settle:* whether a hardness reduction has room. If whole-family infeasibility occurs on a large
family, a reduction can aim at that family; if it is isolated, hardness would have to come from the *existence*
question, not from an infeasibility pattern.
*What it needs:* a targeted search over structured data (e.g. $A$ with repeated eigenvalues or Jordan blocks,
$r_1=p+r$, proportionality vanishing identically) rather than random sampling — the feasible sets are thin, and we
have already been burned by sampling.

**Question B.** Would you expect whole-family spectral infeasibility to be a codimension-one phenomenon in the space
of instances, or an isolated accident? Is there a structural reason why proportionality should vanish identically
(we have seen it only in the $6,2,2$ instance and in $r=1$ cases where it is vacuous)?

## Proposal C. Repair the covering criterion, or replace it by an upper-semicontinuity argument

Two routes to a non-conditional whole-family theorem:

* **(C1) close the image properly.** The image of the graph closure under the projection is a closed subvariety, so
  the closure $\overline S$ is legitimate; what is missing is an argument that a $\mathbb P^{d-1}$ meeting
  $\overline S$ only in $\overline S\setminus S$ still contains a genuine drop. One natural attempt: use upper
  semicontinuity of the rank of the pencil along the degeneration, i.e. show the drop at the boundary point persists.
* **(C2) forget dimension counting.** Use the closedness of the failure locus on each stratum (we have that:
  the failure set is closed on $\{h=h_0,\ \operatorname{rank}[V|Z]=\rho\}$) and prove whole-family failure by
  showing the failure locus *equals* the stratum, e.g. by exhibiting for each $\mathcal Z$ an explicit $x$ via a
  constructive formula. This replaces a global geometric argument by a per-$\mathcal Z$ construction, which is
  closer to what the explicit certificates of II.4 already do.

**Question C.** Which route would you take? Is there a standard device (e.g. a degeneration to the boundary of the
Grassmannian, or a semicontinuity lemma for determinantal rank) that formally bridges the gap we are missing?

## Proposal D. Try to embed a known hard problem through the observability interface

The conditions are bilinear and the spectral condition is an observability test on a $q$-dimensional pair $(E,\Lambda)$
where $\Lambda$ is itself determined by $\mathcal L$ through $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$. Two candidate
sources, in increasing order of structure:

* **D1.** A bounded quadratic feasibility instance, encoded with the multiplication gates realised by the bilinear
  constraints $E_{j+1}=E_j\Lambda$ and $M=\mathcal LV_0=AB$. The known difficulty is not embedding a gate but
  preventing unintended solutions; a first experiment would be to see whether the observer constraints *force* the
  rank and observability conditions in a way that cannot be satisfied by spurious solutions.
* **D2.** Static output feedback / eigenvalue assignment, known to be hard in the structured setting. Our problem
  also chooses the rows of an observer and imposes a spectral condition, so there may be a direct embedding:
  use the free rows of $\mathcal L$ to carry the feedback matrix, and the requirement that the spectrum of
  $\Lambda$ avoid the finite-eigenvalue obstruction to encode the spectral constraint.

**Question D.** Is D2 worth attempting before D1? Our concern with D1 is that our variables are heavily constrained
by $(5a)$ and by the rank conditions, which may leave too little freedom to encode arbitrary multiplications.

## Proposal E. Prove a positive result: an unconditional polynomial class

The cheapest rigorous deliverable on the positive side. Under "counting-spectral separation", feasibility reduces to
the existence of an admissible augmentation with $h<q+r_1$; and when $(5a)$ is automatic ($h=n$), that existence
question reduces to a rank comparison between the spaces $S$, $L_0$ and $C$. The missing piece is a decidable
sufficient condition for "no Type III on the admissible locus".

**Question E.** Do you see such a sufficient condition? For instance, could one prove that Type III forces
$\varepsilon=0$ and the dimension count to be tight (the two hypotheses under which our only example lives), which
would give an unconditional polynomial class consisting of all instances where those fail?

## Two smaller questions

**Question F (invariant $\varepsilon$).** You suggested computing $\varepsilon$ from the determinantal ideal. Is
there any chance that $\varepsilon=0$ has a matrix-theoretic characterisation (e.g. that the two maps $L_0|_V$ and
$L_0A|_V$ are related by a scalar on a dense set, which would mean $U_1=\lambda U_0$ modulo a degenerate part)?

**Question G (what to drop).** We have limited time and a large toolbox. If you had to delete three of the following
directions, which would they be: the incidence/covering line; the hardness line; the search for more counterexamples;
the polynomial-class line; the encoding refinements?

We would follow your ranking. The only thing we ask is that the answer be about research direction rather than about
presentation, since the paper is deferred.
