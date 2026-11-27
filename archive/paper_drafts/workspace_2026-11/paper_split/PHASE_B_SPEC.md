# Phase B 规格：编辑级手术（Paper I）

> 对象：`paper/current/paper_I_dec.tex`。**不改数学结论**，只删重复/重推、降级编号、补策略句。
> 每条给出**搜索锚点**（原文片段），行号会因前面的删除而漂移，所以一律按锚点定位。

---

## B1. `lem:compression` 的证明（目标 65 → 约 40 行）

1. 删重复陈述：锚点 `Set $P_0=\begin{bmatrix}C\\CA\end{bmatrix}$. Since $K_0=\ker P_0$, the matrix $N$ is a basis matrix for $\ker P_0$.`
   → 改为 `Set $P_0=[C;CA]$.`（$N$ 是 $K_0$ 的基矩阵已在 §III-A 说过）
2. 删第二处的同一句：锚点 `Since $N$ is a basis matrix for $K_0$, $M(\lambda)N=[P(\lambda);0;0]$ and $JN=[H;0;0]$.`
   → 改为 `With $N$ as above, $M(\lambda)N=[P(\lambda);0;0]$ and $JN=[H;0;0]$.`
3. 明确代换：锚点 `Since the row space of $P_0$ is a subspace of the row spaces of both $M(\lambda)$ and $J$, Lemma~\ref{lem:rankid} with $P=P_0$ yields`
   → 改为 `Lemma~\ref{lem:rankid} with $P=P_0$, $M=\lambda L-LA$ and $M=L$ gives`（并删去那句关于行空间包含的多余前提）
4. `eq:5a-1`、`eq:5a-2`、`eq:5b-2` 三处 `\begin{equation}\label{...}` → `\begin{equation*}`，**删掉对应 `\label`**，并把正文里对它们的 `\eqref` 换成等价的文字引用（例如"the row inclusion just displayed"）。
5. 证明开头加一句策略句（放在 `\begin{proof}` 之后第一段）：
   > Each part is one rank computation on the stacked matrices of \eqref{eq:5a} and \eqref{eq:5b}: with $P=P_0$ and $N$ a basis of $\ker P_0$, Lemma~\ref{lem:rankid} replaces every stacked rank by $\operatorname{rank}P_0$ plus the rank of a compressed block, and what remains is to read off the resulting row inclusion and to propagate it to $\lambda H-H_A$.
6. **保留**项 (iv)（$\operatorname{rank}H_A=\operatorname{rank}H$）：它已被后面"The projection lies in $S$"那段引用。

---

## B2. `lem:attainable` 的证明（11 → 约 5 行）

锚点：证明开头 `The identity $(H_i,(H_A)_i)=r_i[N\ AN]$ places every free row pair in $\mathcal T$` 到 `$d_0\le rd_0$`（即 `\eqref{eq:kappa}` 相关几句）。
→ 删掉这些复述（它们就是正文 l.391–398 与记号表里的话），只保留：
> Since $N$ has full column rank, $k=\operatorname{rank}N\le\operatorname{rank}[N\ AN]=d_0$, and
> $d_0\le rd_0$ for $r\ge1$; the count $\kappa_{\rm obs}=rd_0$ is a coordinate count, not the dimension
> of an image, since many $R$ give the same row pairs. The case $r=0$ is excluded here and handled in
> Section~\ref{sec:zero}.
（若原证明里的 $k\le d_0$ 推导已在上句覆盖，删其余部分。）

---

## B3. `lem:zero` 的证明前 8 行

锚点：`\emph{(i)$\Leftrightarrow$(ii).} Since $Q(\lambda)$ is $q\times\omega$, its rank drops below $\omega$` 到 `\emph{(ii)$\Leftrightarrow$(iii).} …` 那两句结论。
→ 用一句引用替代：
> The three equivalent forms in (i)--(iii) are those of Lemma~\ref{lem:compression}(iii) with $(H,H_A)$
> replaced by $(X,G)$ and $k$ by $\omega$, together with the passage from $\mathbb{C}[\lambda]$ to
> $\mathbb{Q}[\lambda]$: a nonconstant gcd over $\mathbb{Q}[\lambda]$ still has a complex root, so the
> rational gcd is a constant exactly when there is no common complex root.

另外删掉循环指针：锚点 `This is the adjugate/B\'ezout construction of Appendix~\ref{app:encoding}`（构造就在本证明里，附录反而说"不在此重复"）。

---

## B4. `prop:zero` 的证明

1. 删结尾复述：锚点 `Step 1 is \eqref{eq:5a}, and step 2 is the exact $\omega=0$ reading of the same identity. The zero-free-row decision is therefore the conjunction of one constant-rank test and one pencil test` 那一段 → 只保留一句操作性的：`If \eqref{eq:5a} fails the spectral question is not asked.`
2. 删与 `rem:witness` 重复的句子：锚点 `the test returns the coefficients $S_0,\dots,S_{2\omega-2}$ explicitly` → 删（`rem:witness` 已说）。
3. 秩转移改为引用：锚点 `Since $B$ is of full row rank,` 那个 display 与前后句 → 改为
   `since $B$ is of full row rank, $\operatorname{rank}P(\lambda)=\operatorname{rank}((\lambda X-G)B)=\operatorname{rank}(\lambda X-G)$ as in Section~\ref{sec:pivot}`（保留一句，不重写推导）。
4. 给 (5b)→铅笔 那步补引用：锚点 `\eqref{eq:5b} is $\operatorname{rank}(\lambda H-H_A)=\omega$ for all $\lambda$` → 末尾加 `(Lemma~\ref{lem:compression}(iii))`。

---

## B5. `cor:time` 的证明

锚点：那句 `The two bounds available are those of Sections~\ref{sec:fixedq} and~\ref{sec:fpt},` 及其后的两行 `aligned` display。
→ 整个 display 删除，改为一句：`By \eqref{eq:fpt-l} and the bound of Theorem~\ref{thm:fixedq}, and since both algorithms decide the same language, the smaller bound applies.`

---

## B6. 策略句（两处）

1. `thm:fixedq` 的证明开头（`\emph{(i) Equivalence.}` 之前）加：
   > It suffices to show that $\Phi_{\omega,J}$ is satisfiable exactly when a feasible $L$ exists, and then to substitute the sizes of $\Phi$ into \eqref{eq:rengar} chart by chart.
2. `thm:fpt` 的证明开头（`\emph{(i)}` 之前）加：
   > It suffices to parameterize every feasible $W$ by the chart coordinates of $W/W_0\subseteq\mathcal V/W_0$ and to express the two conditions on that chart by a formula whose size is governed by $\ell$.

---

## B7. `lem:coeff`：删 17 行前奏与重复 display

1. **删前奏**：从 `Let $m=n^2+pn+r_0n$ be the number of rational input entries.` 到第一次出现 `\emph{(i)}` 之前的所有内容（含那个 `aligned` display 里的 `m\le3n^2=O(n^2),\qquad \beta_0=2^{O(m\mathcal L)}` 行）。
   → 换成一句：
   > Each object below is a ratio of minors of the integer input, or a short sum of products of two such
   > minors, so the Hadamard estimate of Lemma~\ref{lem:rationalbasis} bounds its entries.
   **删除前务必确认**：$m$ 与 $\beta_0$ 在 (i)–(iii) 的其余部分不再出现；若出现，保留其定义但删掉重复的第二遍。
2. 删与相邻句子重复的 display 行：锚点 `\operatorname{bits}H_{ij}\le\mathcal L+\operatorname{poly}(n,\mathcal L)+O(\log n)`（若它只是复述紧邻的那句话）。
3. **保留** fixer-a 刚做的 M8/M9/M10 内容（(i) 的对象改为 $X,G,h^0,g^0$ 等；(ii) Laplace + Hadamard；(iii) 项数与 $\operatorname{poly}(n,\mathcal L)$）。不要回退这些。

---

## 验收

同 Phase A：两遍编译，`!`=0、`Reference ... undefined`=0、`Citation ... undefined`=0、`Overfull`=0。
另外：
- `grep -c "eq:5a-1\|eq:5a-2\|eq:5b-2"` 应为 0；
- `grep -c "Appendix~\\\\ref{app:encoding}"` 在 `lem:zero` 证明内应为 0；
- 页数应 **不增加**（目标 15 → 14）。
