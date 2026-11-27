# Class I is solved: $q_{\min}=n-1$ is now a theorem

This note reports that the Class I minimum-order conjecture from our last exchange is now proved, using the structure
you asked us to isolate: everything depends on $\mathcal Z$ alone, and then a two-case dimension argument finishes it.
Both proofs are written out below so that you can check them; the machine-checked kernel is listed at the end.

---

# Part I. The statement and the shape of the proof

**Theorem (B.27).** Let $p=r=1$ ($C=c^{\mathsf T}$, $L_0=\ell^{\mathsf T}$), let $(c,A)$ be observable, and let
$\mathcal L$ be admissible (i.e. $(5a)$ holds, $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$,
$\operatorname{rank}[C;\mathcal L]=1+q$). If $1\le q\le n-2$ then $(5b)$ fails. Since the terminal order $q=n-1$ is
feasible, $q_{\min}=n-1$.

The proof has two ingredients:

* **B.26 (everything is a function of $\mathcal Z$).** With $\mathcal Z=\ker[C;\mathcal L]$ and
  $\mathcal V=\mathcal Z^\perp$:
  1. $\mathcal V=\operatorname{row}[\mathcal L;c]$, hence $\dim\mathcal V=q+1$;
  2. $h=\operatorname{rank}[\mathcal L;CA;C]=\dim(\mathcal V+\langle cA\rangle)\in\{q+1,q+2\}$, and
     $h=q+2\iff cA\notin\mathcal V$;
  3. $(5a)\iff\mathcal VA\subseteq\mathcal V+\langle cA\rangle$;
  4. if $cA\in\mathcal V$ (equivalently $h=q+1$) then $(5a)\iff\mathcal V$ is $A$-invariant.
* **B.27 (two cases).** If $cA\notin\mathcal V$ then $h=q+2=q+r_1$ and your equality theorem B.22 gives failure. If
  $cA\in\mathcal V$ then $(5a)$ makes $\mathcal V$ $A$-invariant, so $cA^k\in\mathcal V$ for all $k$; observability of
  $(c,A)$ makes $\operatorname{span}\{cA^k\}=\mathbb C^n$, so $n\le\dim\mathcal V=q+1$, contradicting $q\le n-2$.

So the second case simply cannot occur, and every admissible candidate at $q\le n-2$ falls into the first case.

**Proofs.**

*B.26.* (1) Every row of $\mathcal L$ and the row $c$ annihilate $\mathcal Z$, so all lie in
$\mathcal Z^\perp=\mathcal V$; and $\operatorname{rank}[C;\mathcal L]=1+q$ gives $\dim\operatorname{row}[\mathcal L;c]=q+1=\dim\mathcal V$,
hence equality.
(2) $h$ is the dimension of the row space of $[\mathcal L;CA;C]$; the row space of $[CA;C]$ equals the row space of
$[cA;c]$, and $c\in\operatorname{row}[\mathcal L;c]$, so $h=\dim(\operatorname{row}[\mathcal L;c]+\langle cA\rangle)=\dim(\mathcal V+\langle cA\rangle)$;
since $\dim\mathcal V=q+1$ and only $cA$ is added, $h\in\{q+1,q+2\}$ with $h=q+2$ exactly when $cA\notin\mathcal V$.
(3) $(5a)$ is $\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}[\mathcal L;c;cA]=\mathcal V+\langle cA\rangle$;
the implication $\Leftarrow$ is immediate, and $\Rightarrow$ uses $\mathcal V=\operatorname{row}\mathcal L\oplus\langle c\rangle$,
which gives $\mathcal VA\subseteq\operatorname{row}(\mathcal LA)+\langle cA\rangle$.
(4) Substitute $cA\in\mathcal V$ in (3). $\square$

*B.27.* By B.26, $\dim\mathcal V=q+1$. If $cA\notin\mathcal V$, then $h=q+2=q+r_1$ and B.22 applies ($q\ge1$).
If $cA\in\mathcal V$, then (4) gives $\mathcal VA\subseteq\mathcal V$. Inducting with $c\in\mathcal V$: $cA^{k}\in\mathcal V$ for
every $k\ge0$, so $\operatorname{span}\{cA^k\}\subseteq\mathcal V$. Observability of $(c,A)$ means that span is
$\mathbb C^n$, so $n\le q+1$, contradicting $q\le n-2$. $\square$

**Exact verification.** B.26's four items and the case split: 2954/2954 admissible samples. B.27: 2454/2454 samples
with $1\le q\le n-1$ admissible — all of them fall in the first case (zero samples in the second), and all satisfy
failure of $(5b)$.

**Machine-checked kernel.** The algebraic core of the second case is formalized (three declarations, no errors, no
warnings): the Krylov containment (if $c\in S$ and $S$ is closed under right multiplication by $A$ then
$\operatorname{span}\{cA^k\}\le S$), the step from a full Krylov span to $S=\top$, and the arithmetic contradiction
$d=q+1$, $d=n$, $q+2\le n$. The row-space instantiation $\mathcal V=\operatorname{row}[\mathcal L;c]$ and the step
"$(5a)\Rightarrow$ closedness under right multiplication" remain paper (covered by the exact verification above); we
label the whole item **[Lean-conditional]** accordingly.

---

# Part II. Why this was not visible earlier

Two things were missing, and both were your suggestions.

1. You insisted that the spectral condition depends only on $\mathcal Z$ — that is what allows the parameter space to
   collapse from $(\mathcal Z,\mathcal L)$ to $\mathcal Z$. Before that, our searches wandered over the whole family of
   $\mathcal L$ with a fixed kernel, which is one reason the picture looked murky; in fact, by B.26, **all** of them
   behave identically.
2. Your B.22 (the equality obstruction) is exactly what kills the first case. Without it, the first case would be the
   hard one; with it, the first case is free and the second case dies by dimension.

We record plainly that our previous report contained an overstatement: we had written that $q_{\min}=n-1$ followed from
$d\le1$, which was wrong for exactly the reason you gave ($d\ge2$ corresponds to *smaller* $q$, and there is no
monotonicity). B.27 repairs it in the other direction, by excluding all $q\le n-2$.

---

# Part III. Questions

**Q1 (check).** Is the two-case argument above complete? Our own worry list:
(a) in B.26(2) we use that the row space of $[CA;C]$ is the row space of $[cA;c]$ — true for $p=r=1$, but we want to be
sure the argument never needs $(\ell,A)$ observable (we believe it does not);
(b) in the second case the argument uses only $q\le n-2$; for $q=n-1$ the second case is exactly the range where
feasibility is possible (and B.18b constructs it). Is that the right way to see the boundary?

**Q2 (does the mechanism generalise?).** The proof is specific to $p=r=1$ in three places: $\dim\mathcal V=q+1$,
$\mathcal V=\operatorname{row}[\mathcal L;c]$, and $h\in\{q+1,q+2\}$. For general $(p,r)$, $\mathcal V=\mathcal Z^\perp$
has dimension $q+p$, and $h=\dim(\mathcal V+\operatorname{row}[CA;C])$. Do you see a version of the second-case argument
there — for instance, replacing "$\mathcal V$ $A$-invariant" by "$\mathcal V$ closed under the induced action of $A$ on
the quotient" — or does the general case genuinely need a different idea?

**Q3 (is there a sharper lower bound?).** Our theorem says $q_{\min}=n-1$ for Class I, i.e. the gap from $q_0$ is
$n-1-q_0$. This is much larger than the gaps in our other examples (1 and 2 at $n=6,p=r=2$). Is there a structural
reason that Class I is the "worst case", i.e. that small $(p,r)$ force maximal gaps? That would be a satisfying
complement to B.27.

**Q4 (what to write).** We propose to state: the dichotomy (counting/spectral) as the main framework; B.22 as the
equality theorem; B.24'/B.25 as the intrinsic spectral reformulation; and B.27 as the Class I classification, with
$q_{\min}=n-1$ as a theorem. The general complexity question stays open and clearly labelled. Would you order the
sections differently?

**Q5 (next target).** With Class I done, the natural next cases are $p=1,r=2$ and $p=2,r=1$ (dimension $n-3$, $r_1$
between $3$ and $4$). Would you go there, or would you now attack the general complexity question with the
quotient-pencil formulation (B.23–B.25) as the target object?
