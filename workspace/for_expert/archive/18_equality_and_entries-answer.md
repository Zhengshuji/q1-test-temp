# Referee report on `18_equality_and_entries.md`

## Overall assessment

This report makes a substantial advance. In particular, the equality case \\(h=q+r_1\\) can now be settled completely, and there is a short proof that is stronger and more transparent than the Kronecker-form route.

My main recommendation is to use the equality case to close the gap in B.11d immediately, rather than spend more time searching for a general formula for the total size of the infinite elementary divisors.

The key result is:

\\[ \boxed{ h=q+r_1,\quad q\ge1,\quad (5a) \quad\Longrightarrow\quad d\_{\rm fin}=q,\qquad d\_\infty=r_1. } \\]

In particular, (5b) necessarily fails at equality.

This is not just a numerical pattern or a consequence of an unproved Kronecker hypothesis. It follows directly from the special block structure of the observer pencil.

There is also an important refinement to B.8b: your new B.21 establishes that the observer pencil has only degree-zero right minimal indices, but it does not eliminate infinite elementary divisors. In fact, at equality, it forces a very specific infinite structure: exactly \\(r_1\\) elementary divisors at infinity, all of size one.

I will first prove the equality theorem, then answer Q1–Q5.

# Part I. The equality case is now settled

## 1. The key observation

Recall

\\[ H= \begin{bmatrix} \mathcal L\\\CA\\\C \end{bmatrix}, \qquad h=\operatorname{rank}H, \qquad r_1=\operatorname{rank} \begin{bmatrix} CA\\\C \end{bmatrix}. \\]

Choose a full-row-rank matrix \\(B\in\mathbb C^{r_1\times n}\\) whose row space is

\\[ \operatorname{row}B=\operatorname{row} \begin{bmatrix}CA\\\C\end{bmatrix}. \\]

Then replacing the possibly dependent lower block \\([CA;C]\\) by \\(B\\) does not change the rank of the stacked matrix. Define

\\[ H_0= \begin{bmatrix} \mathcal L\\\B \end{bmatrix}. \\]

We have

\\[ \operatorname{rank}H_0=h. \\]

Now assume the equality boundary:

\\[ \boxed{h=q+r_1.} \\]

Since \\(\mathcal L\\) has \\(q\\) independent rows and \\(B\\) has \\(r_1\\) independent rows, \\(H_0\\) is a square, invertible row matrix in the sense that it has \\(q+r_1\\) rows of full row rank.

Thus

\\[ H_0:\mathbb C^n\longrightarrow\mathbb C^{q+r_1} \\]

is surjective.

## 2. Use (5a) to factor \\(\mathcal LA\\) through \\(H_0\\)

Condition (5a) gives

\\[ \mathcal LA = \Lambda\mathcal L+G_0C+G_1CA. \\]

Since every row of \\(C\\) and \\(CA\\) belongs to \\(\operatorname{row}B\\), it follows that

\\[ \operatorname{row}(\mathcal LA) \subseteq \operatorname{row}H_0. \\]

Therefore there is a matrix

\\[ K\in\mathbb C^{q\times(q+r_1)} \\]

such that

\\[ \mathcal LA=KH_0. \\]

Partition \\(K\\) according to the two blocks of \\(H_0\\):

\\[ K=\begin{bmatrix}K_1&K_2\end{bmatrix}, \\]

where

\\[ K_1\in\mathbb C^{q\times q}, \qquad K_2\in\mathbb C^{q\times r_1}. \\]

Consequently,

\\[ \begin{aligned} \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\ B \end{bmatrix} &= \begin{bmatrix} \lambda\mathcal L-K_1\mathcal L-K_2B\\\ B \end{bmatrix}\\\\[1mm] &= \boxed{ \begin{bmatrix} \lambda I_q-K_1&-K_2\\\ 0&I\_{r_1} \end{bmatrix} \begin{bmatrix} \mathcal L\\\B \end{bmatrix}. } \end{aligned} \\]

This is the decisive factorization.

The pencil on the left has the same rank as the original \\(Q\_{\mathcal L}(\lambda)\\), because \\(B\\) and \\([CA;C]\\) have the same row space.

The matrix \\(H_0\\) has full row rank. Hence multiplication by \\(H_0\\) does not change the row rank of the square factor. We obtain

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda) = \operatorname{rank} \begin{bmatrix} \lambda I_q-K_1&-K_2\\\ 0&I\_{r_1} \end{bmatrix}. \\]

But

\\[ \det \begin{bmatrix} \lambda I_q-K_1&-K_2\\\ 0&I\_{r_1} \end{bmatrix} = \det(\lambda I_q-K_1). \\]

The latter is a monic polynomial of degree \\(q\\).

Since \\(q\ge1\\), it has a root \\(\lambda_0\in\mathbb C\\). At that root,

\\[ \operatorname{rank}(\lambda_0I_q-K_1)\<q, \\]

and therefore

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda_0)\<q+r_1=h. \\]

Thus:

New theorem — equality boundary resolved

Theorem B.22 (Equality obstruction).

Suppose \\(\mathcal L\\) satisfies (5a), \\(\operatorname{rank}\mathcal L=q\ge1\\), and

\\[ h=\operatorname{rank} \begin{bmatrix} \mathcal L\\\CA\\\C \end{bmatrix} =q+r_1, \qquad r_1=\operatorname{rank} \begin{bmatrix}CA\\\C\end{bmatrix}. \\]

Then there exists a finite \\(\lambda_0\in\mathbb C\\) such that

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda_0)\<h. \\]

Consequently, (5b) fails.

This proof is independent of B.21 and does not require the Kronecker canonical form.

It also does not require observability of \\((C,A)\\) or \\((L_0,A)\\). It uses only the row-space representation in (5a), the equality of dimensions, and \\(q\ge1\\).

That is a useful strengthening.

## 3. The exact infinite and finite divisor degrees

The same factorization gives more than just failure.

The reduced square pencil is

\\[ P(\lambda)= \begin{bmatrix} \lambda I_q-K_1&-K_2\\\ 0&I\_{r_1} \end{bmatrix}. \\]

By a constant invertible row operation, we can eliminate \\(-K_2\\):

\\[ \begin{bmatrix} I_q&K_2\\\0&I\_{r_1} \end{bmatrix} P(\lambda) = \begin{bmatrix} \lambda I_q-K_1&0\\\ 0&I\_{r_1} \end{bmatrix}. \\]

Thus the pencil is strictly equivalent to

\\[ \operatorname{diag}(\lambda I_q-K_1,I\_{r_1}). \\]

The first block is a regular \\(q\times q\\) pencil with monic determinant of degree \\(q\\). The second block consists of \\(r_1\\) constant unit invariant factors.

Therefore

\\[ \boxed{d\_{\rm fin}=q,\qquad d\_\infty=r_1.} \\]

The \\(r_1\\) infinite elementary divisors are all of size one.

This is the strongest useful conclusion from the equality analysis.

# Part II. Answers to Q1–Q5

## Q1. Can \\(d\_\infty\\) be computed from \\(\operatorname{rank}A_0,\operatorname{rank}A_1,h\\)?

There are two different questions here:

1. Is there a general formula for the total size \\(d\_\infty\\) from these ranks?
2. Is there a useful formula for the observer pencil?

The answers are different.

### 1. General pencils: the ranks do not determine the total size

For a general pencil

\\[ P(\lambda)=A_0+\lambda A_1 \\]

of normal rank \\(h\\), the total size of the infinite elementary divisors is not determined by

\\[ \operatorname{rank}A_0,\quad \operatorname{rank}A_1,\quad h. \\]

Here is an explicit pair of regular \\(3\times3\\) examples.

Example 1.

\\[ P_1(\lambda)= \begin{bmatrix} 1&0&0\\\ \lambda&1&0\\\ 0&0&\lambda \end{bmatrix}. \\]

Its coefficient matrices satisfy

\\[ \operatorname{rank}A_0=2,\qquad \operatorname{rank}A_1=2,\qquad h=3. \\]

Moreover,

\\[ \det P_1(\lambda)=\lambda, \\]

so

\\[ d\_\infty=3-\deg\det P_1=2. \\]

Example 2.

\\[ P_2(\lambda)= \begin{bmatrix} 1&0&0\\\ 0&\lambda&0\\\ 0&0&1+\lambda \end{bmatrix}. \\]

Again,

\\[ \operatorname{rank}A_0=2,\qquad \operatorname{rank}A_1=2,\qquad h=3. \\]

But now

\\[ \det P_2(\lambda)=\lambda(1+\lambda), \\]

so

\\[ d\_\infty=3-\deg\det P_2=1. \\]

Thus the same three rank values can correspond to different total infinite degrees.

### 2. There is nevertheless a useful general formula

Although the total size is not determined, the number of infinite elementary divisors is determined by the leading coefficient rank.

Let \\(\nu\_\infty\\) denote the number of infinite elementary divisors, counted as blocks rather than by their sizes.

Then the Kronecker block decomposition gives

\\[ \boxed{ \nu\_\infty=h-\operatorname{rank}A_1. } \\]

To see why, consider the contributions of the Kronecker blocks to the rank of the leading coefficient:

- A left or right singular block of minimal index \\(\epsilon\\) contributes \\(\epsilon\\) to the normal rank and \\(\epsilon\\) to the leading coefficient rank.
- A finite regular block of size \\(k\\) contributes \\(k\\) to both.
- An infinite elementary divisor of size \\(k\\) has leading coefficient a nilpotent Jordan block of rank \\(k-1\\), so it contributes one less to the leading coefficient rank than to the normal rank.

Summing over all blocks gives

\\[ h-\operatorname{rank}A_1=\nu\_\infty. \\]

Similarly, reversing the pencil shows that

\\[ h-\operatorname{rank}A_0 \\]

counts the finite elementary divisors at \\(\lambda=0\\), counted by blocks.

These two rank differences count particular types of elementary-divisor blocks, not their total degrees.

### 3. Application to the observer pencil

For the observer pencil,

\\[ A_1= \begin{bmatrix} \mathcal L\\\0\\\0 \end{bmatrix}, \\]

so

\\[ \operatorname{rank}A_1=q. \\]

At equality,

\\[ h=q+r_1. \\]

Therefore

\\[ \nu\_\infty=h-\operatorname{rank}A_1=r_1. \\]

This tells us that there are exactly \\(r_1\\) infinite elementary divisors.

But it does not, by itself, tell us their total size.

The direct factorization in Part I supplies the missing information and proves that their total size is also \\(r_1\\). Hence every one of those infinite elementary divisors has size one.

My recommendation: retain the general formula

\\[ \nu\_\infty=h-\operatorname{rank}A_1 \\]

as a useful Kronecker bookkeeping lemma, but do not try to derive \\(d\_\infty\\) from coefficient ranks alone. For the observer pencil, use the special factorization instead.

## Q2. Should the equality case be proved directly or absorbed into the dichotomy?

It is now proved directly, and I recommend absorbing it into the dichotomy.

Let

\\[ m=q+r_1. \\]

Since \\(Q\_{\mathcal L}(\lambda)\\) has \\(m\\) rows,

\\[ h>m \\]

is impossible under (5b), because

\\[ \operatorname{rank}Q\_{\mathcal L}(\lambda)\le m\<h. \\]

At equality \\(h=m\\), Theorem B.22 proves that (5b) fails.

Thus we have the stronger statement

\\[ \boxed{ h\ge q+r_1 \quad\Longrightarrow\quad \text{(5b) fails}, } \\]

where the two cases are justified separately:

- \\(h>q+r_1\\): row-count obstruction;
- \\(h=q+r_1\\): equality obstruction.

Consequently, the original CSS reduction can be stated cleanly.

### Recommended revised B.11d

Let CSS mean that, for every admissible order \\(q\\), every augmentation satisfying (5a) with

\\[ h\<q+r_1 \\]

also satisfies (5b).

Then

\\[ \boxed{ \exists\mathcal L:\ (5a)\wedge(5b) \iff \exists\mathcal L:\ (5a)\wedge h\<q+r_1. } \\]

Proof.

- If (5a) and (5b) hold, then \\(h\<q+r_1\\), by the row-count obstruction and Theorem B.22.
- Conversely, if (5a) holds and \\(h\<q+r_1\\), CSS gives (5b).

This is now a complete proof, assuming the CSS hypothesis itself.

The equality case should no longer be listed as open.

## Q3. Does B.21 prove the missing hypotheses in B.8b?

It proves one of them, but the other should not be pursued in its original form.

### 1. The right polynomial nullspace result is correct

The claim

\\[ \ker\_{\mathbb C[\lambda]}Q\_{\mathcal L}(\lambda)=S[\lambda] \\]

is correct under (5a).

Here is a slightly more formal version.

Let

\\[ x(\lambda)=\sum\_{j=0}^d x_j\lambda^j \\]

satisfy

\\[ Q\_{\mathcal L}(\lambda)x(\lambda)=0. \\]

The lower blocks give

\\[ Cx(\lambda)=0,\qquad CAx(\lambda)=0. \\]

Since these are polynomial identities, every coefficient \\(x_j\\) lies in

\\[ V=\ker C\cap\ker CA. \\]

For \\(x(\lambda)\in V[\lambda]\\), (5a) gives

\\[ \lambda\mathcal Lx(\lambda)-\mathcal LAx(\lambda) = (\lambda I-\Lambda)\mathcal Lx(\lambda). \\]

Therefore

\\[ (\lambda I-\Lambda)\mathcal Lx(\lambda)=0. \\]

The matrix \\(\lambda I-\Lambda\\) is invertible over the rational function field \\(\mathbb C(\lambda)\\). Hence

\\[ \mathcal Lx(\lambda)=0. \\]

It follows that every coefficient belongs to

\\[ S=V\cap\ker\mathcal L=V\cap\mathcal Z. \\]

Conversely, if all coefficients belong to \\(S\\), then the lower blocks vanish and, because (5a) implies

\\[ A(S)\subseteq\mathcal Z, \\]

the upper block vanishes too.

Thus

\\[ \boxed{ \ker\_{\mathbb C[\lambda]}Q\_{\mathcal L}(\lambda)=S[\lambda]. } \\]

This is a clean theorem and should be retained.

### 2. Consequence for right minimal indices

The dimension of the polynomial right nullspace over \\(\mathbb C(\lambda)\\) is

\\[ \dim S=s. \\]

A constant basis of \\(S\\) is a polynomial basis with all degrees zero. Therefore there are exactly \\(s\\) right minimal indices, and all are zero.

Since

\\[ s=\dim S=n-h, \\]

we get

\\[ \boxed{ \\#\\{\text{right minimal indices}\\}=n-h, \qquad \eta_j=0\text{ for every }j. } \\]

This is stronger than merely saying that there are no positive-degree right minimal indices.

I would correct the wording in B.8b accordingly. It is not accurate to say that the observer pencil has “no right minimal indices” in general. It has \\(n-h\\) right minimal indices, all of degree zero.

### 3. The infinite elementary divisors are not absent

The second proposed hypothesis in B.8b is not true in general.

Indeed, at equality, we have just proved

\\[ d\_\infty=r_1. \\]

For \\(r_1>0\\), there are nontrivial infinite elementary divisors.

So the original observer-specific identity

\\[ h=\sum_i\varepsilon_i+d\_{\rm fin} \\]

cannot be justified by claiming that the infinite elementary divisors vanish.

The correct identity is

\\[ \boxed{ h=\sum_i\varepsilon_i+d\_{\rm fin}+d\_\infty, } \\]

because all right minimal indices have degree zero.

This identity is valid for the observer pencil under (5a), with the usual Kronecker conventions.

At equality, the left minimal-index count is zero because the pencil has \\(q+r_1=h\\) rows. Thus

\\[ h=d\_{\rm fin}+d\_\infty. \\]

The direct factorization refines this to

\\[ d\_{\rm fin}=q,\qquad d\_\infty=r_1. \\]

Conclusion: B.21 resolves the right-index issue, but it does not eliminate infinite divisors. Instead, it tells you exactly how to write the correct observer-specific Kronecker identity.

## Q4. Should Lean use arbitrary index types or explicit propositions?

I strongly recommend explicit propositions in the mathematical problem domain.

The current approach—quantifying over an arbitrary index type and assuming the substantive content—is logically legitimate, but it makes the Lean artifact less informative.

For example, a theorem of the form

\\[ (\forall i,\ P(i))\to(\forall i,\ Q(i)) \\]

may verify an abstract logical pattern without making clear which mathematical facts about the observer problem are being assumed.

A better structure is to define the relevant predicates explicitly.

For instance, introduce:

- `AdmissibleAugmentation A C L0 q L`
- `Satisfies5a A C L`
- `Satisfies5b A C L`
- `StackRank A C L`
- `CSS A C L0`

Then state a theorem schematically as:

```
theorem b11d_css
    (h_css : CSS A C L0)
    (h_feasible : ∃ q L,
      AdmissibleAugmentation A C L0 q L ∧
      Satisfies5a A C L ∧
      StackRank A C L < q + r1) :
    ∃ q L,
      AdmissibleAugmentation A C L0 q L ∧
      Satisfies5a A C L ∧
      Satisfies5b A C L := by
  ...
```

The precise definitions can be adapted to the existing development, but the principle is important:

the hypotheses should be named mathematical propositions, not anonymous logical placeholders.

This has several advantages:

1. The assumptions can be inspected independently.
2. The theorem statement corresponds directly to the paper.
3. Later, a proof of CSS can replace the hypothesis without changing the conclusion.
4. The dependency graph becomes more transparent.
5. A reviewer can distinguish a mathematical assumption from a purely formal artifact.

I would keep the `[Lean-conditional]` label for such results.

For the new equality theorem, I would aim for a fully `[Lean-verified]` declaration once the row-space factorization has been formalized. It should be considerably easier than formalizing the full Kronecker canonical form.

## Q5. What should be done next?

My recommendation is a combination of (i) and (ii), in that order, followed by a write-up.

First: close the equality boundary

Mathematically solved

Incorporate Theorem B.22 into the paper, revise B.11d, and formalize the block factorization in Lean. This should be a short, self-contained task.

Second: investigate Class I for \\(d\ge2\\)

Main research problem

The \\(d=1\\) obstruction is now established. The remaining intermediate orders are the natural next mathematical target.

Third: consolidate the paper layer

After the equality theorem is incorporated, write the current results as a coherent theorem sequence, with the remaining Kronecker and Class I questions clearly identified as open.

I would not stop structural work now. The equality theorem is relatively inexpensive to finish, while the \\(d\ge2\\) problem is where the next substantial mathematical advance is likely to come from.

# Part III. Two additional deductions

There are two consequences of the new results that I think are worth making explicit in your next report.

## 1. A direct proof of B.19 from B.21

Your B.19 proof uses the Type I criterion. There is a shorter route.

Recall

\\[ S=V\cap\mathcal Z,\qquad s=\dim S. \\]

B.21 gives

\\[ s=n-h. \\]

If

\\[ V\subseteq\mathcal Z, \\]

then

\\[ S=V. \\]

Since

\\[ \dim V=n-r_1, \\]

we obtain

\\[ n-h=n-r_1. \\]

Therefore

\\[ \boxed{h=r_1\<q+r_1} \\]

for \\(q\ge1\\).

This proves B.19 directly.

It also makes the geometry particularly clear:

- \\(V\subseteq\mathcal Z\\) means the quotient domain \\(V/S\\) is zero;
- this automatic spectral feasibility occurs strictly below the equality boundary;
- equality cannot be explained by the permanent-kernel/vacuity mechanism.

I would replace the existing B.19 proof with this shorter dimension argument.

## 2. A particularly useful structural interpretation of equality

At equality,

\\[ h=q+r_1, \\]

the map

\\[ H_0= \begin{bmatrix}\mathcal L\\\B\end{bmatrix} \\]

identifies the effective state quotient with

\\[ \mathbb C^q\oplus\mathbb C^{r_1}. \\]

In these coordinates, the observer pencil is

\\[ \begin{bmatrix} \lambda I_q-K_1&-K_2\\\ 0&I\_{r_1} \end{bmatrix}. \\]

The lower \\(r_1\\) coordinates are algebraically static: they contribute identity blocks and no finite spectral zeros.

All finite spectral behavior is concentrated in the \\(q\times q\\) matrix

\\[ \lambda I_q-K_1. \\]

This gives a useful interpretation:

> At the equality boundary, the pencil necessarily retains a \\(q\\)-dimensional finite spectral component. The \\(r_1\\) remaining dimensions appear as infinite elementary divisors of size one.

That is why equality must fail (5b): the finite characteristic polynomial cannot be a nonzero constant when \\(q\ge1\\).

This structural interpretation may be useful in the introduction or discussion section of the eventual paper.

# Part IV. Revised theorem inventory

I recommend the following updates.

| Item    | Revised status                                                                                                          |
| ------- | ----------------------------------------------------------------------------------------------------------------------- |
| B.8a    | Correct: retain Smith criterion                                                                                         |
| B.8b    | Replace with \\(h=\sum_i\varepsilon_i+d\_{\rm fin}+d\_\infty\\) under (5a)                                              |
| B.9     | Retain after clarifying that the number of left minimal indices is \\(q+r_1-h\\)                                        |
| B.9b    | Correct                                                                                                                 |
| B.10    | Retain with corrected B.8 bookkeeping                                                                                   |
| B.11c   | Retain, subject to the earlier definitions                                                                              |
| B.11d   | Now complete under CSS, using Theorem B.22                                                                              |
| B.19    | Correct; simplify proof using \\(s=n-h\\)                                                                               |
| B.20    | State explicitly whether “constant right nullspace” means the common pointwise kernel or the polynomial right nullspace |
| B.21    | Correct and important; retain                                                                                           |
| B.22    | Add: equality obstruction and exact \\(d\_{\rm fin},d\_\infty\\)                                                        |
| B.12    | Correct                                                                                                                 |
| B.13c–e | Retain                                                                                                                  |
| B.13f   | Retain corrected formulation                                                                                            |
| B.14    | Retain                                                                                                                  |
| B.18b–e | Retain with the qualifications already introduced                                                                       |

One additional point: B.21's proof of the polynomial right nullspace should be marked as relying on (5a), because the implication

\\[ A(S)\subseteq\mathcal Z \\]

is essential for the converse direction.

# Final verdict

This is a strong update. The equality boundary is no longer an open problem.

The most important new result is:

\\[ \boxed{ \begin{gathered} h=q+r_1,\quad q\ge1,\quad (5a)\\\ \Longrightarrow\quad \operatorname{rank}Q\_{\mathcal L}(\lambda_0)\<h \text{ for some }\lambda_0\in\mathbb C,\\\ d\_{\rm fin}=q,\qquad d\_\infty=r_1. \end{gathered} } \\]

It closes the equality gap in the CSS reduction and provides a much sharper understanding of the infinite structure of the observer pencil.

I would now make this theorem the next formal and paper-level milestone, then turn the main research effort to Class I with \\(d\ge2\\). The remaining Kronecker work should be organized around the corrected identity and the fact that the right minimal indices are all zero—not around trying to prove that infinite elementary divisors disappear, which is generally false.&#x20;

18_equality_and_entries.md
