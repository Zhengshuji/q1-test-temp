# The free-witness obstruction: why the single-gate programme has not forced an arithmetic relation

This note states the obstruction that has emerged from the attempts to build the one-gate gadget, and asks whether it is a theorem.

## Part I. What the programme needs

A reduction must produce, for each source instance, a fixed observer instance \((A,C,L_0,q)\) such that

\[
\text{source feasible}\iff \exists L\ \text{satisfying }(5a)(5b).
\]

The arithmetic variables of the source are to be recovered from \(L\); the rank conditions must force them to satisfy the source equations.

## Part II. What the attempts show

1. **The uniform spectral condition is solved** by a filtration with a unit minor: if \(H_A(X)=D(X)H(X)\), \(\operatorname{im}H=W\) fixed, and \(D(X)\) preserves a shift filtration, then \(\operatorname{rank}P_X(\lambda)=\omega\) for all \(X,\lambda\).

2. **A fixed first row \(L_0\) forbids the naive graph chart** \(H=[I\ -X]\); the correct normal form is \(H=C_0[h_0;g(X)]\).

3. **For \(\omega=2,q=3\), a variable kernel is impossible**: \(h_{A,0}\) is forced into \(\operatorname{span}\{h_0,g(X)\}\), whose intersection over varying \(g\) is \(\operatorname{span}\{h_0\}\), so \(h_{A,0}=\lambda_0h_0\) and \(P(\lambda_0)\) drops rank.

4. **Shift \(A\) and \(A(W)\subseteq S\) fail** by a zero-column/eigenvalue dilemma: if \(h_A(v)\) lies in a fixed subspace, the variable coordinate is a zero column of \(D\) (drop at \(\lambda=0\)); if it contains \(v\), it is an eigenvector (drop at its eigenvalue). A two-step variable chain is needed, suggesting \(\omega\ge4\).

5. **The lift channel works but cannot force equations**: on the \(\dim W_L=3\) instance, \(L_3(s)=s e_2+e_3+e_6\) gives a family feasible for every \(s\ne0\), with fixed kernel and varying \(H_A\). Feasibility is the open condition \(s\ne0\), so \(s\) absorbs any value; it cannot be forced to equal \(xy\).

6. **The good kernel appears isolated**: an exact search over \(18\) of the \(124\) planes of \(\operatorname{Gr}(2,3)\) (all row combinations with coefficients in \(\{-1,0,1\}\)) finds exactly one good plane, \(V_{45}=\operatorname{span}\{e_4,e_5\}\). The good locus is not open.

## Part III. The obstruction

The observer conditions are rank equalities. Their solution set is constructible: a finite union of locally closed sets. Two behaviours are possible for a parameter:

- if feasibility is **open** in the parameter, the parameter is free and absorbs arbitrary values (as in II.5);
- if feasibility is a **proper closed condition**, the parameter is constrained by a polynomial equation, but then the observer can usually choose the other free parameters to satisfy it.

What the programme needs is a parameter that is **determined by the input and appears in a rank equality whose zero set is exactly the arithmetic relation**, with no free parameter able to absorb it. None of the architectures above produces such a parameter: the fixed first row removes the natural graph parameter; the remaining parameters are either free (lift) or isolated (kernel).

**Question.** Is there a general theorem to the effect that, for fixed \((A,C,L_0)\), the set of feasible \(L\) projects to a constructible subset of the graph parameters whose fibres are either open or finite — and that this cannot encode an arbitrary polynomial equation such as \(z=xy\)? If so, the single-gate route is impossible, and hardness must come from a different mechanism (e.g. varying the input rather than the witness, or a genuinely different target problem).

If the answer is negative, a concrete construction of a parameter that is both input-determined and constrained by a rank equality would be the key missing gadget.

## Part IV. Status

- The uniform spectral lemma is proved (unit minor).
- The single-gate realization has resisted all attempted architectures; the evidence points to a structural obstruction.
- We ask for adjudication: is the free-witness obstruction a theorem, or is there a construction we have missed?
