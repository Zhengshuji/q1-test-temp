# **Review of&#x20;**`98_multiplication_gate_anatomy.md`

The report contains a useful structural diagnosis, and several of its central observations are genuinely strong. In particular, **the maximality lemma (Lemma 3) is the most important result in the note**: it gives a direct algebraic obstruction to increasing the compressed output rank while preserving feasibility. The pinning argument also looks sound, subject to making the parameter space and the fixed-row contribution precise.

However, I would not yet accept the report's strongest formulation of Theorem 2 or the escape taxonomy without qualifications. There are two issues to resolve:

1. Theorem 2's density conclusion is correct under a natural interpretation of the feasible set, but its proof needs to distinguish the complex algebraic feasible locus from its real rational points.
2. Lemma 3 rules out *rank-increasing extensions of a feasible witness*. It does not, by itself, prove that every attempted multiplication gadget can be escaped only by shrinking, nor that no multiplication gadget exists in the unpinned region.

My overall assessment: **the report establishes a meaningful obstruction theory, but not yet a general no-go theorem.** The best next step is to formalize the obstruction as a theorem about pinned instances and maximal feasible row spaces, then investigate what additional hypotheses would be needed to extend it to non-pinned instances.

## **1. Detailed correctness audit**

### **1.1 The&#x20;**\\(\lambda=0\\)**&#x20;bound — correct**

The argument is immediate but important. From (5b), setting \\(\lambda=0\\) gives

\\[ \operatorname{rank}(-H_A)=\omega. \\]

Therefore

\\[ \operatorname{rank}H_A=\operatorname{rank}H=\omega. \\]

Since \\(H_A=LAN\\), its rank cannot exceed the rank of \\(AN\\):

\\[ \boxed{\omega\leq \operatorname{rank}(AN)=\dim(AK_0).} \\]

This is a necessary condition for feasibility. The report correctly emphasizes that it is an *upper bound* on the possible rank stratum, not a spectral argument.

One small improvement: explicitly state that \\(\operatorname{rank}(AN)=\dim(AK_0)\\), since \\(N\\) is a basis matrix for \\(K_0\\). This makes the last equality transparent.

### **1.2 Lemma 1 (pinning) — correct**

The fixed rows give

\\[ W_0:=\operatorname{row}H_0 \subseteq W:=\operatorname{row}H, \qquad \dim W_0=\omega_0. \\]

Feasibility and the \\(\lambda=0\\) bound give

\\[ \omega_0\leq\dim W =\operatorname{rank}H \leq\dim(AK_0). \\]

If \\(\dim(AK_0)=\omega_0\\), all inequalities are equalities. Consequently,

\\[ \boxed{W=W_0,\qquad \omega=\omega_0.} \\]

There is no hidden spectral assumption here. This is a clean rank sandwich.

I would retain this lemma almost unchanged.

### **1.3 Theorem 2 (pinned instances have linear expressive power) — correct after a necessary qualification**

The underlying idea is sound, but the equality

\\[ \mathcal F=\mathcal L\cap\mathcal O \\]

needs one additional hypothesis or one adjustment to the definition of \\(\mathcal L\\).

The report defines \\(\mathcal L\\) by requiring each *free* row pair to lie in

\\[ \mathcal T\cap(W_0\times W_0). \\]

This guarantees that the free rows' contributions to both \\(H\\) and \\(H_A\\) lie in \\(W_0\\). It does **not**, by itself, guarantee that the fixed contribution \\(H\_{A,0}=L_0AN\\) lies in \\(W_0\\).

For a feasible solution, (5a) certainly forces

\\[ \operatorname{row}H\_{A,0}\subseteq W_0. \\]

But if the fixed rows violate this condition, there are no feasible solutions, while \\(\mathcal L\cap\mathcal O\\) could still be nonempty if \\(\mathcal O\\) tests only (5b).

There are two clean repairs:

- **Repair A:** State Theorem 2 under the additional hypothesis\
  \\[\
  \operatorname{row}H\_{A,0}\subseteq W_0.\
  \\]
- **Repair B:** Include this fixed-row condition in the definition of the linear feasible ambient space, and define \\(\mathcal O\\) as the open spectral-feasibility subset of that space.

I prefer Repair A because it makes the logical structure easier to read: first check the fixed rows satisfy (5a), then characterize the free rows.

Under that qualification, the argument is:

1. Pinning forces \\(W=W_0\\).
2. The first condition (5a) is then exactly the requirement that every free \\(g_i\\) lie in \\(W_0\\), together with the fixed-row compatibility condition.
3. The free \\(h_i\\) must also lie in \\(W_0\\), since they are rows of \\(H\\).
4. Thus (5a) cuts out the linear space \\(\mathcal L\\).
5. Within \\(\mathcal L\\), (5b) is the complement of the bad spectral locus, hence a Zariski-open condition.

So the corrected statement is

\\[ \boxed{\mathcal F=\mathcal L\cap\mathcal O} \\]

provided the fixed rows already satisfy the row-space inclusion.

### **1.4 The Zariski-density step — sound, with the field made explicit**

Suppose \\(\mathcal L\\) is a complex linear subspace and \\(\mathcal O\subseteq\mathcal L\\) is a nonempty Zariski-open subset. Then

\\[ \overline{\mathcal O}^{\\,\mathrm{Zar}}=\mathcal L. \\]

This is simply the irreducibility of a linear space (an affine space after choosing coordinates).

It does not matter that \\(\mathcal O\\) is a *proper* Zariski-open subset. A nonempty Zariski-open subset of an irreducible variety is dense.

The real/rational-point concern should be handled separately:

- If \\(\mathcal F\\) means the **complex** feasible locus, the density conclusion follows immediately.
- If \\(\mathcal F\\) means the **real** feasible locus and it is nonempty, then \\(\mathcal O(\mathbb R)\\) contains a nonempty Euclidean-open subset of \\(\mathcal L(\mathbb R)\\). A polynomial vanishing on that subset vanishes identically on \\(\mathcal L\\).
- If \\(\mathcal F\\) means the **rational** feasible locus, and \\(\mathcal L\\) and \\(\mathcal O\\) are defined over \\(\mathbb Q\\), then a nonempty rational Zariski-open subset of a \\(\mathbb Q\\)-linear space has Zariski-dense rational points. In particular, nonempty rational feasibility suffices.

The last point is worth stating carefully: a nonempty complex open set need not contain a rational point. The report avoids that error by conditioning on \\(\mathcal F\ne\varnothing\\), but it should say which field defines \\(\mathcal F\\).

**Conclusion for Theorem 2:** its density argument is sound once the fixed-row compatibility is included and the field of points is specified.

## **2. Lemma 3: the maximality lemma**

Correct as stated

This is the strongest part of the report.

Let the original feasible compressed row space be

\\[ W=\operatorname{row}H,\qquad \dim W=\omega. \\]

Add a row pair \\((h,g)\in\mathcal T\\) with \\(h\notin W\\). Then

\\[ \operatorname{row}H'=W+\langle h\rangle, \qquad \operatorname{rank}H'=\omega+1. \\]

Assume, for contradiction, that the enlarged system remains feasible. Its first condition implies

\\[ g\in\operatorname{row}H_A' \subseteq\operatorname{row}H' =W+\langle h\rangle. \\]

Thus there are \\(\alpha\in\mathbb C\\) and \\(w\in W\\) such that

\\[ g=\alpha h+w. \\]

At \\(\lambda=\alpha\\), the new pencil row is

\\[ \alpha h-g=-w\in W. \\]

Every old pencil row also belongs to \\(W\\), because the old witness was feasible and its pencil has rank \\(\omega\\). Hence

\\[ \operatorname{rank}(\alpha H'-H_A')\leq\omega <\omega+1=\operatorname{rank}H', \\]

contradicting (5b).

Therefore

\\[ \boxed{\text{A feasible witness cannot be extended by a row whose }h \text{-component is independent of }W.} \\]

I would keep the proof. It is short, self-contained, and does not need an external reference.

### **Is it a known result?**

I would not present it as a standard named theorem without finding a precise reference. It is a direct consequence of the particular pair of conditions (5a) and (5b), and the proof is short enough that citing it as an independently proved lemma is preferable.

A useful way to describe its mechanism is:

> The row-space inclusion condition forces the new \\(g\\)-component to be expressible using the enlarged \\(h\\)-row space. That expression determines a spectral parameter at which the new pencil row becomes dependent on the old row space.

This is more precise than saying merely that the pencil “punishes extra rows.”

## **3. The escape taxonomy — the report currently overstates it**

The report says that the only escape is shrinking, and that enlargement of \\(\operatorname{row}H\\) is impossible. This is correct for a *specific kind of extension*, but not yet for arbitrary pairs of feasible witnesses.

Lemma 3 proves:

\\[ \boxed{ R\text{ feasible},\quad R'\text{ obtained by retaining all rows of }R \text{ and adding }(h,g),\ h\notin W \ \Longrightarrow\ R'\text{ infeasible}. } \\]

It does **not** prove that there cannot be two feasible witnesses \\(R_1,R_2\\) with

\\[ \dim W_2>\dim W_1 \\]

when the rows of \\(R_1\\) are not a subset of the rows of \\(R_2\\).

That distinction matters. A larger feasible witness might use a different collection of rows, rather than extending a smaller feasible witness. Lemma 3 does not compare such witnesses.

There is a second issue with the table's final row. From

\\[ W_0\subseteq W,\qquad \dim W=\dim W_0 \\]

one gets \\(W=W_0\\). But if the feasible rank is strictly larger than \\(\omega_0\\), two feasible spaces of the same dimension can both contain \\(W_0\\) and still be different.

Thus the corrected taxonomy is:

| Potential escape                                               | What is actually established                                                            |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Add a row with \\(h\notin W\\) while retaining the old witness | Impossible by Lemma 3                                                                   |
| Add a row with \\(h\in W\\)                                    | Does not increase \\(\operatorname{rank}H\\); feasibility still needs checking          |
| Move to a different feasible witness with a larger row space   | Not ruled out by Lemma 3                                                                |
| Shrink to a lower rank stratum                                 | Possible unless excluded by the fixed-row lower bound                                   |
| Change the row space at the same rank                          | Impossible in the pinned case; possible in general when the rank exceeds \\(\omega_0\\) |

The last two rows are important for the next stage of the project. The report's diagnosis of the \\(R=0\\) failure is convincing for the example described: the fixed rows allow a lower-rank witness than the intended one. But it should not be elevated to a universal classification of all escapes until the non-extension cases are addressed.

**Suggested replacement wording:**

> Lemma 3 rules out monotone rank-increasing extensions of a feasible witness. In a pinned instance, the fixed rows already determine the entire compressed row space, so no row-space movement is possible. Outside the pinned regime, shrinking remains a demonstrated escape mechanism, but the present lemmas do not establish that it is the only one.

That is both accurate and still a strong structural conclusion.

## **4. Q3: where can a multiplication gate live?**

The report's proposed region,

> not pinned, with the row space maximal,

is a sensible place to focus, but “maximal” needs a definition.

There are at least three different notions:

1. **Extension-maximal:** no feasible witness obtained by adding a row to the current witness can have larger rank.
2. **Rank-maximal:** no feasible witness for the same instance has larger \\(\operatorname{rank}H\\).
3. **Inclusion-maximal among feasible row spaces:** there is no strictly larger feasible row space containing the current one.

Lemma 3 establishes the first and, in the extension sense, the third. It does not establish the second.

For gadget design, the second notion is often the one that matters: an unintended witness might be a completely different solution with a larger rank. I recommend using “extension-maximal” for Lemma 3 and reserving “maximum feasible rank” for the global property.

### **What is known from the present report?**

There is a useful dichotomy.

**Pinned regime.** The compressed row space is fixed, and the feasible set is a nonempty Zariski-open subset of a linear space. Therefore the feasible set cannot impose a genuinely nonlinear polynomial equation on its free-row parameters.

**Unpinned regime.** The rank of \\(H\\) can vary between the fixed-row lower bound and the \\(\dim(AK_0)\\) upper bound. Different rank strata can occur, and the feasible set is a union of pieces with potentially different row spaces. The current arguments do not show that this union is linear or dense in a single linear space.

That second regime is where a multiplication construction might conceivably hide. But the report has not yet shown that it can.

A useful next question is whether the *maximal-rank feasible stratum* is itself an open subset of a linear parameter space, or whether the row-space condition creates genuinely nonlinear geometry there. If it is always linear-open, that would give a much broader no-go theorem. If not, the failure of linearity identifies exactly where to search for a gate.

## **5. Q4: should the project aim for a no-go theorem?**

Yes—but I would aim for a **tiered no-go theorem**, not the strongest universal statement immediately.

The universal claim in the report is:

> In this architecture (row-wise common \\(\mathcal T\\), the two rank conditions), no gadget can express multiplication.

That is much stronger than what has been proved. The architecture permits different fixed-row data, different \\(A,C\\), and different ways of encoding the variables. A universal impossibility result must specify what counts as a gadget and what counts as expressing multiplication.

For example, does a gadget express \\(z=xy\\) if:

- every feasible witness gives \\(z=xy\\), with \\(x,y,z\\) linear functions of the free-row parameters?
- every feasible witness gives \\(z=xy\\), where \\(x,y,z\\) are polynomial functions of the parameters?
- the projection of the feasible set onto three designated coordinates is exactly the multiplication graph?
- the projection merely contains a subset of that graph?

These are inequivalent requirements. I recommend fixing the first or third definition before attempting a no-go theorem.

### **A first no-go theorem that is already within reach**

The following is a precise and useful theorem.

**Pinned-instance no-go theorem.** Suppose:

1. the instance is pinned, i.e.\
   \\[\
   \dim(AK_0)=\operatorname{rank}H_0;\
   \\]
2. the fixed rows satisfy the compatibility condition\
   \\[\
   \operatorname{row}H\_{A,0}\subseteq\operatorname{row}H_0;\
   \\]
3. the feasible set is nonempty;
4. the encoded variables \\(x,y,z\\) are affine-linear functions of the free-row parameters.

Then if

\\[ z-xy=0 \\]

holds for every feasible witness, it must hold identically on the entire linear parameter space \\(\mathcal L\\).

**Proof.** By the corrected Theorem 2, the feasible set is Zariski dense in \\(\mathcal L\\). The polynomial

\\[ f=z-xy \\]

vanishes on the feasible set. Its zero locus is Zariski closed, so it contains the Zariski closure of the feasible set, namely all of \\(\mathcal L\\). Hence \\(f\\) vanishes identically on \\(\mathcal L\\). \\(\square\\)

This is a real no-go result: a pinned instance cannot use the spectral condition to enforce a new, nontrivial multiplication identity. Any such identity must already be a consequence of the linear parameterization.

One subtlety: if the intended encoding uses *homogeneous linear* rather than affine-linear coordinate functions, the theorem still applies, but it is even more restrictive. If it uses rational functions or nonlinear decoding, the theorem does not directly apply; those cases need separate treatment.

### **A stronger target**

The next worthwhile target is:

> On every irreducible component of every feasible rank stratum, the feasible points are either empty or Zariski dense in a linear subspace determined by the fixed data.

If true, it would extend the pinned no-go argument to a substantial part of the unpinned regime. But I do not see a proof from the current lemmas alone. In particular, the rank-\\(\omega\\) condition on \\(H\\) is locally closed, and the requirement that the row space vary with the free parameters can introduce nonlinear incidence geometry.

I would not state this stronger target as a conjecture without first testing it on small symbolic examples.

## **6. Q5: the affine-rank-minimisation obstruction**

### **6.1 The bound&#x20;**\\(d_0\leq n-p\\)**&#x20;— correct**

Since

\\[ K_0=\ker\begin{bmatrix}C\\\CA\end{bmatrix}, \\]

we have

\\[ CN=0,\qquad CAN=0. \\]

Consequently,

\\[ C[N\ AN]=0. \\]

Every column of \\([N\ AN]\\) belongs to \\(\ker C\\), whose dimension is \\(n-p\\). Therefore

\\[ \boxed{d_0=\operatorname{rank}[N\ AN]\leq n-p.} \\]

The implication for row-wise encoding is also correct, provided the claim is understood as an encoding of an *arbitrary* \\(n\\)-dimensional row.

Indeed, the map

\\[ \psi:\mathbb Q^{1\times n}\longrightarrow\mathbb Q^{1\times 2k}, \qquad r\longmapsto(rN,rAN) \\]

has image dimension \\(d_0\\). Its kernel therefore has dimension at least \\(p\\). Thus it cannot faithfully preserve arbitrary \\(n\\)-dimensional row data.

However, this is not yet a general impossibility theorem for reductions from affine rank minimisation. A reduction might encode only a restricted row space, or encode variables through a different representation. The correct conclusion is:

> The direct row-wise encoding \\(r\mapsto(rN,rAN)\\) cannot faithfully represent arbitrary \\(n\\)-dimensional carrier rows when \\(p\geq1\\).

That is a genuine obstruction to the most straightforward translation, not to every possible translation.

### **6.2 The claim about affine control needs clarification**

There is a point I would revise in the report. It says that pinning is an excellent device for imposing affine constraints. But the displayed definition

\\[ \mathcal L: \qquad (h_i,g_i)\in\mathcal T\cap(W_0\times W_0) \\]

imposes a **linear** constraint on each free row pair.

It does not, by itself, impose an arbitrary affine constraint such as

\\[ x_1+x_2=1. \\]

The fixed rows can provide fixed reference data, and a suitable choice of coordinates might allow some affine-looking conditions to be represented relative to those references. But that needs an explicit construction. It does not follow from Theorem 2 as currently stated.

I would replace the report's sentence with:

> Pinning provides a mechanism for imposing fixed linear restrictions on every free row pair. Whether these restrictions, together with fixed-row data and an appropriate encoding, can simulate arbitrary affine constraints requires a separate construction.

This distinction is particularly important if the intended hardness reduction starts from affine rank minimisation, where the translation needs to preserve nonhomogeneous affine constraints.

## **7. What I would change in the report**

The report is already well organized. I would make the following targeted changes rather than restructure it.

| Location | Current issue                                                                    | Recommended revision                                                                           |
| -------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| II.1     | Rank bound is correct but the last equality is implicit                          | State \\(\operatorname{rank}(AN)=\dim(AK_0)\\) explicitly                                      |
| II.3     | Equality \\(\mathcal F=\mathcal L\cap\mathcal O\\) omits fixed-row compatibility | Assume \\(\operatorname{row}H\_{A,0}\subseteq W_0\\), or include it in the ambient constraints |
| II.3     | Density discussion does not specify the field                                    | Distinguish complex, real, and rational feasible points                                        |
| II.3     | “Only relations” could be interpreted too broadly                                | Specify that the relations are polynomial identities in the chosen free-row coordinates        |
| II.4     | “Maximal” is potentially ambiguous                                               | Call it extension-maximality                                                                   |
| II.5     | The taxonomy overstates what Lemma 3 proves                                      | Distinguish extensions from unrelated feasible witnesses                                       |
| II.6     | “Affine control” is not established by the displayed linear space                | Say linear restrictions unless an affine encoding is supplied                                  |
| Part III | The universal no-go question is broad                                            | First state a pinned-instance no-go theorem                                                    |

The report's reliability table should also be adjusted. I would use:

| Item                                                         | Assessment                                                           |
| ------------------------------------------------------------ | -------------------------------------------------------------------- |
| \\(\lambda=0\\) bound                                        | Proved                                                               |
| Lemma 1 (pinning)                                            | Proved                                                               |
| Theorem 2 (pinned \\(\Rightarrow\\) linear expressive power) | Proved after fixed-row compatibility and field clarification         |
| Lemma 3 (extension-maximality)                               | Proved                                                               |
| Escape taxonomy                                              | Partially proved; current wording is too strong                      |
| \\(d_0\leq n-p\\)                                            | Proved                                                               |
| General affine-rank-minimisation obstruction                 | Direct row-wise encoding ruled out; general reductions not ruled out |
| Universal no-multiplication theorem                          | Open                                                                 |

## **8. Recommended research direction**

I would not abandon multiplication-gate construction entirely. But I would change the order of attack.

**Stage 1 — establish the pinned no-go theorem**

Within reach

Formalize the corrected Theorem 2 and its polynomial-identity consequence. This gives a rigorous negative result for a clearly defined class of gadgets.

**Stage 2 — understand non-pinned rank strata**

Main open problem

For each possible rank \\(\omega\\), study

\\[ \mathcal F\_\omega = \\{R:\operatorname{rank}H=\omega,\ (5a),(5b)\\}. \\]

Determine whether its irreducible components have a linear-open structure, or whether genuinely nonlinear geometry can occur.

**Stage 3 — characterize global rank maximality**

Not yet established

Determine whether a feasible witness of maximum possible rank can be characterized by its row space alone, and whether all maximum-rank witnesses are related by transformations that preserve the encoded variables.

**Stage 4 — revisit multiplication**

Only after Stages 1–3 should you decide whether to seek a construction or prove a broader no-go theorem. The key question is whether the non-pinned feasible locus can impose a nonlinear polynomial relation on the encoded coordinates.

### **A particularly useful next lemma to investigate**

Try to prove or disprove the following statement:

**Candidate linearity principle.** Fix the instance \\((A,C,L_0)\\) and a rank value \\(\omega\\). On every irreducible component of the rank-\\(\omega\\) feasible locus, the feasible set is either empty or Zariski dense in a linear subspace of the free-row parameter space.

If this holds, then the pinned argument is not an isolated phenomenon. It could imply that no rank stratum can enforce a genuinely new multiplication identity under affine-linear decoding.

If it fails, the counterexample would be equally valuable: it would identify the geometric mechanism through which multiplication might be encoded.

I would test this principle first in small dimensions, with exact rational arithmetic and symbolic elimination, rather than immediately attempt a universal proof. In particular, distinguish a nonlinear *rank stratum* from a nonlinear *feasible locus*: determinantal rank constraints are algebraic, but their intersection with the pencil-feasibility open condition may have a much simpler structure.

## **9. Final verdict**

The report has identified a real structural phenomenon:

- The \\(\lambda=0\\) condition bounds the compressed rank from above.
- Fixed rows bound it from below.
- When those bounds coincide, the compressed row space is pinned.
- In that pinned regime, spectral feasibility is an open condition inside a linear parameter space.
- A feasible witness cannot be extended by a new row that increases the compressed rank.

These are meaningful results, not merely computational observations.

The main correction is that **extension-maximality is not global maximality**, and the current escape taxonomy should not claim more than Lemma 3 establishes. Likewise, the pinned theorem needs the fixed-row compatibility condition made explicit.

My recommendation is to make this report the foundation of a short structural paper or a rigorous section of the larger complexity paper. The pinned no-go theorem is already a defensible result. The unpinned regime is the real remaining mathematical problem, and the candidate linearity principle is a good next target.

98_multiplication_gate_anatomy.md