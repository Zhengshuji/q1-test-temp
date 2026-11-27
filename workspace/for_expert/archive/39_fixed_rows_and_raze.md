# Two items for verification: the fixed-row image, and the equivalence of the decision problem with the rank-stratified target

This report submits the last two items of the verification list for review, and asks one question about the
remaining item.

---

# Part I. Setting

Let $K=\ker[C;CA]$, $k=\dim K$, $N_K\in\mathbb C^{n\times k}$ with columns a basis of $K$ (so $N_K$ has full
column rank), $A$ fixed, and for $R\in\mathbb C^{(q-r)\times n}$
$$\mathcal L(R)=\begin{bmatrix}L_0\\R\end{bmatrix},\qquad H(R)=\mathcal L(R)N_K,\qquad H_A(R)=\mathcal LA(R)N_K .$$
Both are $q\times k$. Put $\omega=\operatorname{rank}H(R)$, $D=K\cap\ker\mathcal L$, $d=\dim D$, and let
$(5a)$, $(5b)$ be as usual, with the identity
$$(5a)\iff\ker H\subseteq\ker H_A$$
(machine-checked in the form $K\cap\ker L\le\ker T\iff\ker(L|_K)\le\ker(T|_K)$).

---

# Part II. Item 4: the image with fixed rows

**Lemma 1.** Let $M=\begin{bmatrix}L_0\\R\end{bmatrix}$ with $L_0$ fixed and $R$ free, and let
$$\Psi_{L_0}(R)=\bigl(MN_K,\ MAN_K\bigr).$$
Then
$$\operatorname{im}\Psi_{L_0}
=\Bigl\{(H,H_A)\in(\mathbb C^{q\times k})^2:\ H_{1:r,:}=L_0N_K,\ \ (H_A)_{1:r,:}=L_0AN_K\Bigr\}$$
**if and only if** $K\cap AK=0$.

*Proof.* Split both equations by row blocks. $MN_K=H$ is equivalent to the pair
$$L_0N_K=H_{1:r,:},\qquad RN_K=H_{r+1:q,:}=:B_1,$$
and $MAN_K=H_A$ to
$$L_0AN_K=(H_A)_{1:r,:},\qquad RAN_K=(H_A)_{r+1:q,:}=:B_2 .$$
The first members of each pair involve only the fixed data, so the question reduces to: for which $(B_1,B_2)$
does $RN_K=B_1$, $RAN_K=B_2$ have a solution?

$(\Leftarrow)$ If $K\cap AK=0$, then $N_K$ and $AN_K$ both have full column rank and their images meet only in
$0$; hence $R$ can be prescribed independently on $K$ and on $AK$, and extended arbitrarily to a complement. This
gives a solution for every $(B_1,B_2)$. (The dimension count is $(q-r)n\ge2(q-r)k$, i.e. $n\ge2k$, consistent
with $K\cap AK=0$.)

$(\Rightarrow)$ If $K\cap AK\ne0$, choose $0\ne v\in K\cap AK$ and write $v=Aw$ with $w\in K$. For every $R$,
$$Rv=R(Aw)=(RA)w,$$
so the information of $B_1$ on $v$ and of $B_2$ on $w$ is tied by one linear relation; hence not every pair
$(B_1,B_2)$ is attainable, and the image is a proper subset of the displayed set. $\square$

**Consequence for sampling.** Randomly draw $B_1,B_2$, solve $RN_K=B_1$, $RAN_K=B_2$, form
$(H,H_A)=(MN_K,MAN_K)$. When $K\cap AK=0$ this produces points of the chart uniformly over the target space, and
the fixed rows cost nothing beyond requiring the top blocks to match.

---

# Part III. Item 5: the decision problem equals the rank-stratified target

**Definition (rank-stratified affine zero exclusion, RAZE).** An instance is the observer data together with the
two top blocks $H^{(0)}=L_0N_K$, $H_A^{(0)}=L_0AN_K$. The answer is YES if there exist $R$ and
$\omega\in\{0,1,\dots,k\}$ such that

1. $\operatorname{rank}H(R)=\omega$;
2. $\ker H(R)\subseteq\ker H_A(R)$;
3. with a column set $S\subseteq\{1,\dots,k\}$, $|S|=\omega$, such that $H_{[:,S]}$ has full column rank, and
   with $U=H_{[:,S]}$, $G=H_{A,[:,S]}$, the $\omega\times\omega$ minors of $\lambda U-G$ have gcd a nonzero
   constant. For $\omega=0$ condition 3 is vacuous and holds automatically.

**Theorem 2.** $\mathrm{DEC}(q)=\mathrm{YES}\iff\mathrm{RAZE}=\mathrm{YES}$.

*Proof.* $(\Rightarrow)$ Take $R$ satisfying $(5a)$ and $(5b)$ and put $\omega=\operatorname{rank}H(R)$.
Condition 1 holds by definition. Condition 2 is the identity above applied to $(5a)$. For condition 3: if
$\omega=0$ it is vacuous; if $\omega>0$, the reduced criterion (verified earlier) gives
$(5b)\iff\gcd\{\omega\text{-minors of }\lambda H-H_A\}\in\mathbb C^\times$, and the fixed-column construction
gives $P_{[:,S]}=\lambda U-G$ together with $\operatorname{rank}(\lambda H-H_A)=\operatorname{rank}(\lambda U-G)$
for every $\lambda$, since the coordinate factor has full row rank. Hence the gcd condition holds for the reduced
pencil.

$(\Leftarrow)$ Take $(R,\omega)$ satisfying 1–3. Condition 2 with the identity gives $(5a)$. For $(5b)$: by the
kernel identity
$$\dim\ker Q_{\mathcal L}(\lambda)=\dim D+\dim\ker P_K(\lambda),$$
$(5b)$ holds iff $\ker P_K(\lambda)$ has constant dimension, i.e. iff the induced map on $W_K$ has no invariant
line. Condition 3 says precisely that the reduced pencil has no finite rank drop, i.e.
$\operatorname{rank}(\lambda U-G)=\omega$ for all $\lambda$; by the rank equality this gives no rank drop for
the full pencil, which is the no-invariant-line condition, hence $(5b)$. For $\omega=0$: $H=0$ forces $H_A=0$ by
condition 2, and the zero-rank branch of the reduced criterion gives $(5b)$ automatically. $\square$

**Dependencies and their status.**

| Component | Status |
|---|---|
| $(5a)\iff\ker H\subseteq\ker H_A$ | machine-checked |
| $\dim\ker Q_{\mathcal L}=\dim D+\dim\ker P_K$ | set-level identity machine-checked; the additive $d$ is rank–nullity on $v\mapsto Lv$ |
| reduced criterion, including $\omega=0$ | verified |
| $P_{[:,S]}=\lambda U-G$ and the rank equality | verified |

---

# Part IV. Questions

**Question 1.** Is Lemma 1 correct, in particular the converse direction? We argue that $K\cap AK\ne0$ forces one
linear relation between $B_1$ and $B_2$. We would like to know whether the relation is exactly "one per nonzero
element of $K\cap AK$", and whether the image is then described by those relations alone (i.e. cut out by linear
conditions), since that description would be needed for a sampler in the case $K\cap AK\ne0$.

**Question 2.** Is Theorem 2 correct as an equivalence, and is the $(\Leftarrow)$ direction's use of the kernel
identity legitimate at $\omega=0$? Our concern is that at $\omega=0$ the reduced pencil is empty and the gcd
statement is vacuous, so the equivalence must rest on the zero-rank branch of the reduced criterion alone.

**Question 3.** For the remaining item of the list — the per-layer complexity claims — what is the minimum
defensible statement? We can show that on the $\omega=0$ stratum the feasible set is a single point and
membership is decidable by inspection, and that on the $\omega=1$ stratum the bad condition is a system of
quadratic equations whose vanishing on the stratum can be tested by linear algebra. We are inclined to state only
these two and to say nothing about $\omega\ge2$. Is that the right level of caution, or is the $\omega=1$
statement itself in need of an input-encoding qualification before it can be called polynomial-time?
