# Research review: Class I \\((p=r=1)\\)

This is a productive report, and the quotient-pencil result is now in a good position to become a formal theorem. However, I found a significant issue in the proposed remaining lemma and, more importantly, in the dimension argument built around it.

The claim

\\[ \operatorname{im}\psi=\ker c \\]

is false in general. There is a very small counterexample satisfying all the hypotheses of Class I. In fact, that counterexample also shows that the conclusion \\(q\_{\min}=n-1\\) is not universally true.

This does not make the Class I programme unproductive. It changes what the next theorem should be: rather than proving the proposed lemma, I would characterize the image of \\(\psi\\), then characterize which admissible lines in \\(K\\) avoid it.

I will go through the four questions, starting with the counterexample.

## 1. Q1 — The remaining lemma is false

The claim is

\\[ \operatorname{im}\psi=\ker c, \qquad \psi(x,\lambda)=(\lambda I-A)x, \quad x\in V=\ker[c;cA]. \\]

You have already observed that

\\[ \operatorname{im}\psi\subseteq\ker c, \\]

because for \\(x\in V\\),

\\[ c(\lambda I-A)x=\lambda cx-cAx=0. \\]

The reverse inclusion, however, does not hold.

### 1.1 A counterexample in dimension three

Take

\\[ A= \begin{bmatrix} 0&1&0\\\ 0&0&1\\\ 1&0&0 \end{bmatrix}, \qquad c= \begin{bmatrix}1&0&0\end{bmatrix}, \qquad \ell= \begin{bmatrix}0&1&0\end{bmatrix}. \\]

All the hypotheses of Class I are satisfied.

First, \\((c,A)\\) is observable, since

\\[ \begin{bmatrix} c\\\cA\\\cA^2 \end{bmatrix} = \begin{bmatrix} 1&0&0\\\ 0&1&0\\\ 0&0&1 \end{bmatrix}. \\]

Similarly, \\((\ell,A)\\) is observable:

\\[ \begin{bmatrix} \ell\\\\\ell A\\\\\ell A^2 \end{bmatrix} = \begin{bmatrix} 0&1&0\\\ 0&0&1\\\ 1&0&0 \end{bmatrix}. \\]

Also, \\(\operatorname{rank}[c;\ell]=2\\).

Now calculate the relevant subspaces:

\\[ V=\ker[c;cA] =\operatorname{span}\\{e_3\\}, \\]

\\[ K=\ker[c;\ell] =\operatorname{span}\\{e_3\\}, \\]

and

\\[ \ker c=\operatorname{span}\\{e_2,e_3\\}. \\]

Since

\\[ Ae_3=e_2, \\]

we obtain

\\[ \psi(te_3,\lambda) =t(\lambda e_3-e_2). \\]

Consequently,

\\[ \boxed{ \operatorname{im}\psi = \\{0\\}\cup \\{ae_2+be_3:a\ne0\\}. } \\]

In particular,

\\[ e_3\notin\operatorname{im}\psi. \\]

But \\(e_3\in\ker c\\). Therefore

\\[ \boxed{\operatorname{im}\psi\ne\ker c.} \\]

This disproves the proposed lemma.

### 1.2 An even more important consequence: \\(q\_{\min}=n-1\\) is false in general

In this example, \\(n=3\\), so the proposed conclusion would be

\\[ q\_{\min}=2. \\]

But take

\\[ q=1,\qquad \mathcal L=\ell. \\]

Then

\\[ d=n-1-q=1, \\]

and

\\[ \mathcal Z=\ker[c;\ell] =\operatorname{span}\\{e_3\\} =V. \\]

Thus

\\[ S=V\cap\mathcal Z=V. \\]

By the quotient-pencil criterion,

\\[ (5b)\text{ holds} \\]

because \\(V/S=\\{0\\}\\): there are no nonzero quotient-domain vectors that can witness spectral failure.

Moreover,

\\[ \operatorname{rank}[\mathcal L;CA;C] = \operatorname{rank} \begin{bmatrix} e_2\\\e_2\\\e_1 \end{bmatrix} =2, \\]

so this rank is not \\(n\\), but (5a) still holds: \\(e_2A=e_3\\), and \\(e_3\\) lies in the row space of \\([c;CA;\mathcal L]\\) only if we interpret the rows correctly. Here \\(CA=cA=e_2\\), so the row space is \\(\operatorname{span}\\{e_1,e_2\\}\\), which does not contain \\(e_3\\).

Thus this particular choice \\(\mathcal L=\ell\\) does not satisfy (5a).

This is an important distinction: the quotient-pencil criterion establishes (5b), but it does not replace the algebraic condition (5a). We must not conclude feasibility from the quotient-pencil test alone.

I therefore need to correct the conclusion above: this example disproves the proposed lemma, but it does not by itself disprove \\(q\_{\min}=n-1\\). The \\(q=1\\) candidate fails the algebraic condition (5a).

This is exactly why the two conditions must remain separate throughout the Class I analysis.

### 1.3 What the counterexample tells us about the image

The image is not merely a proper subset of \\(\ker c\\). It is a constructible set with a particularly simple description in this example:

\\[ \operatorname{im}\psi = \ker c\setminus\operatorname{span}\\{e_3\\} \ \cup\ \\{0\\}. \\]

Its Zariski closure is all of \\(\ker c\\), even though it does not equal \\(\ker c\\).

This distinction is central:

\\[ \boxed{ \overline{\operatorname{im}\psi}=\ker c \quad\not\Rightarrow\quad \operatorname{im}\psi=\ker c. } \\]

It also exposes a problem in the report's dimension argument.

### 1.4 The claimed dimension bound needs correction

The report states

\\[ \dim\operatorname{im}\psi\le n-2. \\]

That does not follow from the dimensions of the individual subspaces \\((\lambda I-A)V\\). The map

\\[ \psi:V\times\mathbb C\to\ker c \\]

has a domain of dimension

\\[ \dim V+1=(n-2)+1=n-1. \\]

Its image can therefore have dimension \\(n-1\\), and in the counterexample above it does:

\\[ \dim\operatorname{im}\psi=2=n-1. \\]

The correct general bound from the parameter count is

\\[ \boxed{\dim\operatorname{im}\psi\le n-1.} \\]

This is the same as the dimension of \\(\ker c\\), so it does not give the dimension obstruction you wanted.

There is a further geometric point: \\(\operatorname{im}\psi\\) is the image of a polynomial map, hence constructible, but it need not be closed. Calling \\(K\\) an irreducible component of \\(\operatorname{im}\psi\\) is therefore not justified without first taking the Zariski closure and proving the relevant component statement.

Conclusion for Q1: abandon the equality \\(\operatorname{im}\psi=\ker c\\) as a general lemma. The right problem is to characterize \\(\operatorname{im}\psi\\) more precisely, particularly its intersection with the admissible directions in \\(K\\).

## 2. A more useful formulation of the \\(d=1\\) problem

I think the \\(d=1\\) analysis remains very promising, but it needs a small correction.

Let

\\[ \mathcal Z=\langle z\rangle,\qquad z\in K\setminus\\{0\\}. \\]

For the case \\(S=V\cap\mathcal Z=0\\), the quotient-pencil failure criterion gives

\\[ (5b)\text{ fails} \iff \exists x\in V,\ \lambda: x\notin\mathcal Z,\quad (\lambda I-A)x\in\langle z\rangle. \\]

Because \\((c,A)\\) is observable, there is no nonzero eigenvector of \\(A\\) in \\(\ker c\\). Thus, for nonzero \\(x\in V\\), the vector \\((\lambda I-A)x\\) cannot be zero. Hence the condition is equivalent to

\\[ \boxed{ (5b)\text{ fails} \iff z\in\operatorname{im}\psi, \qquad \mathcal Z\cap V=0. } \\]

This is a good and useful equivalence.

However, the set of admissible lines is not necessarily all of \\(\mathbb P(K)\\). The lines satisfying \\(S=0\\) are precisely

\\[ \mathbb P(K)\setminus\mathbb P(K\cap V). \\]

Thus the correct whole-family statement for this stratum is

\\[ \boxed{ \text{Every admissible }S=0\text{ line fails} \iff \mathbb P(K)\setminus\mathbb P(K\cap V) \subseteq\mathbb P(\operatorname{im}\psi). } \\]

This is weaker than the proposed condition

\\[ K\setminus\\{0\\}\subseteq\operatorname{im}\psi. \\]

The distinction matters because

\\[ \dim(V\cap K)\ge n-3. \\]

For \\(n\ge4\\), this intersection is necessarily nontrivial. Its lines are not part of the \\(S=0\\) stratum.

There is also an important second stratum: if \\(\mathcal Z\subseteq V\\), then \\(S=\mathcal Z\\), and (5b) is automatic. Such a line must still be checked against (5a).

### 2.1 What to compute instead

I recommend replacing the proposed lemma with a theorem about the projective bad-direction set

\\[ \mathcal D= \mathbb P(\operatorname{im}\psi) \cap\mathbb P(K). \\]

The key question is whether

\\[ \mathbb P(K)\setminus\mathbb P(K\cap V) \subseteq\mathcal D. \\]

This directly answers the spectral part of the \\(d=1\\) problem.

But for the original augmentation problem, you must additionally impose (5a). I would therefore define

\\[ \mathscr A_1 = \\{\mathcal Z\in\operatorname{Gr}(1,K): \mathcal Z\text{ satisfies (5a)}\\} \\]

and ask whether

\\[ \mathscr A_1 \subseteq\mathscr B_1, \\]

where \\(\mathscr B_1\\) is the spectral bad locus.

That is the exact whole-family question. It avoids confusing a spectral obstruction with full infeasibility.

## 3. Q2 — Is Class I worth completing?

Yes, but I would change the goal.

I would not aim immediately for a complete classification of all orders. I would first aim for a complete classification of the \\(d=1\\) case, including both (5a) and (5b).

The reason is that this case has a particularly simple geometry:

\\[ \operatorname{Gr}(1,K)=\mathbb P(K). \\]

The unknown is a projective point, and the spectral failure condition is membership in the image of a polynomial map.

### 3.1 Suggested sequence

Step 1. Characterize the \\(d=1\\) candidates satisfying (5a).

This is essential. The image \\(\operatorname{im}\psi\\) only captures spectral failure. It says nothing by itself about algebraic admissibility.

Step 2. Characterize the \\(d=1\\) spectral bad locus.

Use

\\[ \mathcal D=\mathbb P(\operatorname{im}\psi)\cap\mathbb P(K) \\]

and account separately for the \\(S=0\\) and \\(S=1\\) strata.

Step 3. Combine the two descriptions.

Determine whether

\\[ \mathscr A_1\setminus\mathscr B_1 \\]

is empty, and if not, characterize its elements.

Step 4. Only then investigate \\(d\ge2\\).

For \\(d\ge2\\), the natural object is no longer a bad image of individual vectors, but a Grassmannian incidence variety. A candidate \\(\mathcal Z\\) fails if it contains at least one vector of the form \\((\lambda I-A)x\\), with the necessary condition \\(x\notin\mathcal Z\\). This is a subspace-containment problem.

The \\(d=1\\) classification may reveal a pattern that generalizes to higher-dimensional \\(\mathcal Z\\).

### 3.2 A useful special-case direction

The companion-form case is worth investigating, but I would not begin by assuming that the answer is always \\(q\_{\min}=n-1\\).

For a single-output observable pair, one can choose a cyclic basis in which

\\[ c=e_1^{\mathsf T}, \qquad cA=e_2^{\mathsf T}, \\]

and \\(A\\) has companion-like form. Then

\\[ V=\operatorname{span}\\{e_3,\ldots,e_n\\}. \\]

This makes \\(\psi\\) explicit. In particular, the first two coordinates of \\(Ax\\) and the polynomial coefficients of \\(A\\) can be used to characterize which vectors in \\(\ker c\\) are in \\(\operatorname{im}\psi\\).

I would first derive an exact formula for \\(\operatorname{im}\psi\\) in this canonical setting. That may lead to a clean theorem for \\(p=r=1\\).

My recommendation: complete \\(d=1\\) first, but do not promise a full all-orders classification yet. A rigorous theorem for \\(d=1\\), combined with the terminal-order theorem, would already be a meaningful result.

## 4. Q3 — Polynomial algorithm or hardness reduction?

I would pursue the algorithmic and geometric directions before committing to a hardness reduction.

Your observation that infeasibility may be “thin” is interesting, but the current evidence does not establish that the bad locus is thin in a mathematically uniform sense. The counterexample above illustrates why: the image can be dense in \\(\ker c\\) while missing a projective direction.

There are three different possibilities:

1. the bad locus is a proper closed subset;
2. the bad locus is dense constructible but not all of the parameter space;
3. the bad locus is the whole admissible family.

These cases can have very different algorithmic implications.

### 4.1 The most promising algorithmic question

For fixed \\(p=r=1\\), can one characterize the image of

\\[ \psi:V\times\mathbb C\to\ker c \\]

using polynomial equations and nonvanishing conditions that can be computed efficiently?

If yes, then the \\(d=1\\) problem may reduce to testing whether an admissible projective set intersects a constructible set.

That would be a concrete algorithmic theorem, rather than a general claim about constrained deflation.

### 4.2 When to return to hardness

Once the small case is understood, the general problem can be attacked through a Grassmannian selection problem. I would look for reductions from:

- prescribed-subspace containment problems;
- matrix-pencil completion problems;
- algebraic subspace-selection problems.

But any reduction must encode both the admissibility constraints and the spectral condition. A reduction that only creates a rank condition is insufficient.

I would not yet choose hardness as the exclusive direction. The special-case geometry is too promising to abandon.

## 5. Q4 — Where should the permanent-kernel proposition go?

I recommend the following order in the paper:

1. Structural setup and rank notation.
2. Dimension obstruction.
3. General quotient-pencil failure criterion.
4. Permanent-kernel proposition.
5. Stratification by \\(s\\).
6. Class I specialization.
7. The \\(d=1\\) image characterization.

The dimension obstruction should appear first because it is a cheap necessary test that can rule out candidates before spectral analysis.

The permanent-kernel proposition should immediately follow the general failure criterion, because it explains why the quotient pencil is needed and why the ordinary full-column-rank test is invalid on middle strata.

I would state it as:

Proposition (Permanent kernel). For every admissible \\(\mathcal Z\\) satisfying (5a),

\\[ V\cap\mathcal Z \subseteq \ker N\_{\mathcal Z}(\lambda) \qquad\forall\lambda\in\mathbb C. \\]

Furthermore,

\\[ (5b)\iff \ker N\_{\mathcal Z}(\lambda)=V\cap\mathcal Z \qquad\forall\lambda\in\mathbb C. \\]

This is concise, general, and independent of the Class I specialization.

## 6. What I would ask the research team to do next

Immediate correction

Recheck the \\(d=1\\) derivation

- Remove the claim \\(\dim\operatorname{im}\psi\le n-2\\).
- Replace \\(K\setminus\\{0\\}\\) by the appropriate admissible directions.
- Keep (5a) separate from the spectral membership test.
- Treat the image as constructible, not automatically closed.

Next theorem

Characterize \\(\operatorname{im}\psi\\) in canonical coordinates

Start with a single-output observable companion-form pair. Derive a necessary-and-sufficient condition for a vector \\(w\in\ker c\\) to have a representation

\\[ w=(\lambda I-A)x,\qquad x\in V. \\]

After that

Classify feasible \\(d=1\\) augmentations

Intersect the spectral good locus with the candidates satisfying (5a). Determine whether this intersection is empty and under which additional hypotheses.

## 7. Final verdict

The quotient-pencil formulation is now a strong and useful foundation. The terminal-order theorem is also a clean result.

The proposed remaining lemma, however, is false. The counterexample above shows that even under observability of both \\((c,A)\\) and \\((\ell,A)\\),

\\[ \operatorname{im}\psi \\]

can be a dense proper constructible subset of \\(\ker c\\).

The main correction is therefore:

\\[ \boxed{ \text{Do not try to prove }\operatorname{im}\psi=\ker c. \text{ Characterize }\operatorname{im}\psi\cap K \text{ instead.} } \\]

That is the exact geometric object relevant to the \\(d=1\\) spectral problem. Then intersect it with the algebraically admissible candidates from (5a).

I would continue Class I, but with this revised target. The next meaningful milestone is a necessary-and-sufficient \\(d=1\\) classification, not a proof of the false equality.