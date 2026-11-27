# T4-b is proved

**Date:** 2026-11-02 (evening, second session)
**Follows:** `REPORT_2026-11-02_WORKSTREAM_B_FULL_EN.md` and your review of it.

You recommended pursuing the reversed-pencil chain equations. Following that line produced a proof, and
it turned out to be simpler than the chain analysis suggested: the key is not the chains, but a
**factorization** that your own $(5a)$ supplies.

---

## 1. The theorem

**Theorem (T4-b).** Let $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, $L\in\mathbb C^{q\times n}$
satisfy $(5a)$, i.e. $\operatorname{row}(LA)\subseteq\operatorname{row}(L;CA;C)$. Let
$h=\operatorname{rank}[L;CA;C]$ and $Q_L(\lambda)=[\lambda L-LA;\,CA;\,C]$. Then every infinite
elementary divisor of $Q_L$ has degree $1$, and
$$d_\infty=h-\operatorname{rank}L .$$
Consequently (using B.6 and the global identity) $\sum_j\varepsilon_j=\operatorname{rank}L$.

**Note:** the proof does **not use $(5b)$** — the statement holds for every $L$ satisfying $(5a)$.

## 2. The proof

**Step 1 (factorization).** By $(5a)$ there are constant matrices $X\in\mathbb C^{q\times q}$,
$Y_1,Y_2\in\mathbb C^{q\times p}$ with $LA=XL+Y_1CA+Y_2C$. Hence
$$Q_L(\lambda)=\underbrace{\begin{bmatrix}\lambda I_q-X&-Y_1&-Y_2\\0&I_p&0\\0&0&I_p\end{bmatrix}}_{P(\lambda)}
\begin{bmatrix}L\\CA\\C\end{bmatrix},\qquad
P(\lambda)=\underbrace{\begin{bmatrix}I_q&-Y_1&-Y_2\\0&I_p&0\\0&0&I_p\end{bmatrix}}_{U\ \text{constant
invertible}}\operatorname{diag}(\lambda I_q-X,I_{2p}).$$

**Step 2 (strict equivalence).** Left multiplication by $U^{-1}$ preserves all Kronecker invariants, so
$Q_L$ is strictly equivalent to
$$M(\lambda)=\operatorname{diag}(\lambda I_q-X,I_{2p})\begin{bmatrix}L\\CA\\C\end{bmatrix}
=\begin{bmatrix}(\lambda I_q-X)L\\CA\\C\end{bmatrix}.$$

**Step 3 (reversal).** With $M=M_0+\lambda M_1$,
$M_1=[L;0;0]$ and $M_0=[-XL;CA;C]$. The infinite divisors of $M$ are the elementary divisors at
$\mu=0$ of
$$\widehat M(\mu)=M_1+\mu M_0=\begin{bmatrix}(I_q-\mu X)L\\ \mu CA\\ \mu C\end{bmatrix}.$$

**Step 4 (local equivalence at $\mu=0$).** $\det(I_q-\mu X)|_{\mu=0}=1$, so $I_q-\mu X$ is a unit in the
local ring $\mathbb C[\mu]_{(\mu)}$. Multiplying by $\operatorname{diag}((I_q-\mu X)^{-1},I_p,I_p)$
gives the locally equivalent pencil
$$\widetilde M(\mu)=\begin{bmatrix}L\\ \mu CA\\ \mu C\end{bmatrix}.$$

**Step 5 (determinantal divisors).** Let $r_1=\operatorname{rank}L$ and $\Delta_k$ be the gcd of all
$k\times k$ minors of $\widetilde M$:

* $k\le r_1$: a minor using only $L$-rows is a nonzero constant, so $\Delta_k$ is a nonzero constant;
* $r_1<k\le h$: a nonzero minor uses $j$ rows of the $\mu$-blocks and $k-j$ rows of $L$; since
  $\operatorname{rank}L=r_1$, nonvanishing forces $j\ge k-r_1$, so $\Delta_k$ is divisible by
  $\mu^{k-r_1}$; and choosing $r_1$ independent $L$-rows together with $k-r_1$ rows of $[CA;C]$ (possible
  since $\operatorname{rank}[L;CA;C]=h\ge k$) attains equality;
* $k>h$: zero.

Hence $\Delta_k=c_k\mu^{k-r_1}$ with $c_k\ne0$ constant.

**Step 6.** The invariant factors $d_k=\Delta_k/\Delta_{k-1}$ are units for $k\le r_1$ and
$(c_k/c_{k-1})\mu$ for $r_1<k\le h$. So the elementary divisors at $\mu=0$ are exactly $h-r_1$ copies of
$\mu$, each of degree one. ∎

## 3. Two corrections you should know about

**3.1 An error of ours (R20).** In the previous report, and in the scripts behind it, $d_\infty$ was
computed as the **sum of the polynomial degrees** of the reversed pencil's invariant factors. That is the
wrong quantity: the infinite divisors correspond to the **elementary divisors at $\mu=0$**, i.e. the
$\mu$-adic valuations. A concrete instance: one reversed pencil has invariants
$1,1,1,\tfrac14-\mu+\mu^2$; the degree reading gives "2", the valuation reading gives "0". The first gave
a spurious "counterexample" to T4-b; the second agrees with $h-\operatorname{rank}L=0$.

The tool now reports `d_infinity` (sum of $\mu$-valuations); with the corrected measure T4-b holds on
**151/151** pencils satisfying $(5a)$ (43 of them infeasible) for $n=6,\dots,10$.

**3.2 Your suggested T4-b′ is not the right test** (we tested it literally): for $L$ of full row rank
$\operatorname{im}L=\mathbb C^q$, so the condition $LAw\in\operatorname{im}L$ is nearly automatic, and the
"chains" it detects belong to the singular part, not to infinite elementary divisors (45 of 59 pencils
"violated" it). The determinant-divisor argument above is the correct replacement.

## 4. Where this leaves Workstream B

| item | status |
|---|---|
| right minimal indices | **theorem B.6** ($(5a)\Rightarrow$ all zero) + Lean kernel |
| infinite elementary divisors | **theorem T4-b** (all degree 1, $d_\infty=h-\operatorname{rank}L$), this note |
| left minimal indices | count $=q+2p-h$; **sum $=\operatorname{rank}L$** (corollary of the two above) |
| so the Kronecker data of an observer pencil is now **fully determined in aggregate** | the only remaining freedom is the *individual* left indices $\varepsilon_1\ge\dots\ge\varepsilon_{q+2p-h}$ with $\sum\varepsilon_j=\operatorname{rank}L$ |

That last row is, we think, the sharp remaining question: **which partitions of $\operatorname{rank}L$
into $q+2p-h$ parts occur?** Our data show the extreme case (all zero except one) as well as spread
partitions; we have not found a pattern.

## 5. Files

* `proof/t4b_infinite_divisors/` — theorem.md (full proof), verify.py (151/151), README
* `proof/kron_null_module/` — B.6 (paper + Lean kernel)
* `proof/refuted/README.md` — R18, R19, R20 (our three retractions in this line)
* `docs/02_theorems_proven.md` — B.6, B.7

## 6. Question

Do you agree that the remaining question is the partition of $\operatorname{rank}L$ into
$q+2p-h$ left indices? And is there a known result on which partitions occur for pencils of the form
$[\lambda L-LA;CA;C]$ — e.g. through the observability indices of $(A,C)$?
