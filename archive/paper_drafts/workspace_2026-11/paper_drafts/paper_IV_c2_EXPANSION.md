# Paper IV 扩版材料：(a) worked example 与 (b) 高度链的显式界

> 用途：交给论文侧并入 `paper/current/paper_IV_c2.tex`（预计 +2–3 页）。
> 两节都写成**可直接粘贴的 LaTeX**。数据全部由 `tools/verification/c412_worked_example.py` 精确算出。
> 放置建议：worked example 放 §VI 之后（新 §VII，原 §VII 顺延为 §VIII），
> 高度链替换现有 Appendix A。

---

## (a) 新 §VII：A worked example

```latex
\section{A worked example}\label{sec:example}

This section carries one instance through the whole procedure: the compressed data, the admissible
kernel direction, the image space, the pencil, and the gcd certificate. All entries are exact integers.
The point is to make the hypotheses of Theorem~\ref{thm:complexity} checkable on a concrete instance, and
to show that a certificate for the feasible case is four lines long.

\emph{The instance.} $n=8$, $p=2$, and
\begin{equation}\label{eq:exA}
A=\begin{pmatrix}
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0\\
1 & -2 & 1 & 0 & -1 & 1 & 1 & -1\\
-1 & 2 & 1 & 0 & 2 & -2 & -1 & 2\\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 2 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 3
\end{pmatrix},\qquad
C=\begin{pmatrix}
1&0&0&0&0&0&0&0\\ 0&1&0&0&0&0&0&0
\end{pmatrix}.
\end{equation}
Here $\rank[C;CA]=4$, so $k=4$, and
\[
K_0=\ker[C;CA]=\operatorname{span}\{e_5,e_6,e_7,e_8\},\qquad
N=\begin{pmatrix}0_{4\times4}\\ I_4\end{pmatrix}.
\]
The compression and the coupling are
\[
M=\pi_{K_0}A|_{K_0}=\operatorname{diag}(1,1,2,3),\qquad
A_{21}=\begin{pmatrix}
0&0&0&0\\ 0&0&0&0\\ -1&1&1&-1\\ 2&-2&-1&2\\ 0&0&0&0\\ 0&0&0&0\\ 0&0&0&0\\ 0&0&0&0
\end{pmatrix},
\]
the second matrix having rank one, with $A_{21}D\neq\{0\}$ for the direction used below.

\emph{The direction.} Take $D=\operatorname{span}\{e_1+e_2,\ e_3\}\le K_0$. Then
$M(e_1+e_2)=e_1+e_2$ and $Me_3=2e_3$, so $M(D)\subseteq D$ and $D\in\mathcal I_2(M)$ with
$\dim D=c=2$. Since $L_0=0$ the prescribed-row conditions read $P_{K_0}(V_0)=0$ and $W_0=0$, which hold
trivially, so $D\in\mathcal B_{\rm pres}$.

\emph{The fibre.} Here $A_{21}D=\operatorname{span}\{(1,-1,0,0,\dots)^{\mathsf T}\}$, so
\[
r(D)=1,\qquad \dim T_D=(n-k)-r(D)=4-1=3 .
\]
With $t=1$ (i.e.\ $q=\omega+t=2+1=3$) and $W=\operatorname{span}\{(0,0,1,1,0,0,0,0)^{\mathsf T}\}\subseteq T_D$
one computes
\[
\varphi_W=(1,-1,0,1)\in D^\circ,\qquad \Phi(W)=\operatorname{span}\{(1,-1,0,1)\},
\]
so $\dim\Phi(W)=1\le\min(t,\,2p)=2$: the image parameter is a line, as in
Definition~\ref{defn:charts}. The resulting design row space is
\[
V=D^{\perp_{K_0}}\oplus W
=\operatorname{span}\bigl\{(0,0,0,0,-1,1,0,0),\ (0,0,0,0,0,0,0,1),\ (0,0,1,1,0,0,0,0)\bigr\},
\]
of dimension $q=3$.

\emph{The pencil.} With this $V$,
\[
H=V^{\mathsf T}N=\begin{pmatrix}-1&1&0&0\\ 0&0&0&1\\ 0&0&0&0\end{pmatrix},\qquad
H_A=V^{\mathsf T}AN=\begin{pmatrix}-1&1&0&0\\ 0&0&0&3\\ 1&-1&0&1\end{pmatrix}.
\]
The invariants are $\omega=\rank H=2$, $\dim(K_0\cap V^\perp)=2=c$ (exact kernel), and
$\row H_A\subseteq\row H$, i.e.\ \eqref{eq:5a} holds. Of the nine $2\times2$ minors of
$\lambda H-H_A$ exactly six are nonzero:
\[
-(\lambda-3)(\lambda-1),\quad (\lambda-3)(\lambda-1),\quad \lambda-1,\quad 1-\lambda,\quad
\lambda-3,\quad 3-\lambda .
\]

\emph{The certificate.} The minors $\lambda-1$ and $\lambda-3$ are coprime, with Bézout identity
\[
\tfrac12\bigl((\lambda-1)-(\lambda-3)\bigr)=1 ,
\]
so the gcd of all maximal minors is $1$ and condition~\eqref{eq:5b} holds. By
Theorem~\ref{thm:correctness} the algorithm returns \emph{feasible}; and indeed a feasible design of order
$q=3$ with $c=2$ exists, whereas (Section~\ref{sec:layers:c}) no feasible design of order $3$ with $c=1$
does.

\emph{Reading the hypothesis of Theorem~\ref{thm:complexity}.} The spectrum of $M$ is $\{1,1,2,3\}$, so it
is \emph{not} simple: this instance lies outside the hypothesis of Theorem~\ref{thm:complexity} and
demonstrates the algorithm and the certificate format, not the polynomial bound. The distinction is worth
recording, because it shows that \emph{feasibility} is not confined to the simple-spectrum case --- only the
\emph{cost bound} is. For a simple-spectrum instance keep \eqref{eq:exA} and replace $M$ by
$\operatorname{diag}(1,2,3,4)$; the enumeration then has six admissible directions and the same certificate
format applies.
```

**给论文侧的注**：上面最后一段是**有意留下的诚实说明**——这个 worked example 的 $M$ 有重根（$\mu=1$ 重数 2），
所以它落在 Theorem 14 的假设（单谱）**之外**，只演示算法与证书格式，不演示复杂度界。
如果审稿人不喜欢这种"示例不在假设内"的安排，两个选项：
(i) 保留它但标题改为"an example outside the simple-spectrum hypothesis"（我推荐，诚实且有教学价值）；
(ii) 换成 $\operatorname{diag}(1,2,3,4)$ 的实例（我需要重算一次证书，约 10 分钟）。

---

## (b) 替换现有 Appendix A：高度传播的显式界

```latex
\appendices
\section{Height propagation with explicit bounds}\label{app:height}

This appendix records the chain used in Claim~\ref{clm:arithmetic} with the standard bounds made
explicit. Throughout, $h(\cdot)$ is the maximum bit length of the entries (for a matrix) or of the
coefficients (for a polynomial), and $B$ denotes a running bound on $h$.

\emph{Step 0 (input).} $h(A),h(C)\le\tau$.

\emph{Step 1 ($CA$ and $[C;CA]$).} Entrywise, $(CA)_{ij}$ is a sum of $p$ products, so
$h(CA)\le 2\tau+\lceil\log_2 p\rceil$. Hadamard's bound gives, for every square submatrix $S$ of
$[C;CA]$ of order $d$, $|\det S|\le(\sqrt{n}\,2^{2\tau+\log p})^{d}$, i.e.\
$h(\det S)\le d\,(2\tau+\log p+\tfrac12\log n)$.

\emph{Step 2 (kernel basis $N$).} A basis of $\ker[C;CA]$ can be chosen so that each entry is a cofactor
of $[C;CA]$, hence of order $2p$; by Step 1,
\[
h(N)\le 2p\,(2\tau+\log p+\tfrac12\log n).
\]

\emph{Step 3 (Gram matrix and its inverse).} $G=N^{\mathsf T}N$ has entries that are sums of $k$ products,
so $h(G)\le 2h(N)+\log k$. Since $G$ is a positive definite integer matrix, $\det G\ge1$, and the entries
of $G^{-1}$ are cofactors over $\det G$, so
\[
h(G^{-1})\le k\,(2h(N)+\log k+\tfrac12\log k).
\]

\emph{Step 4 (compression and coupling).} $M=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$ and
$A_{21}=P_{K_0^\perp}AN$ are obtained from $G^{-1}$, $N$ and $A$ by $O(k^2)$ ring operations, so
\[
h(M),\,h(A_{21})\le 4h(N)+2h(G^{-1})+\tau+O(\log k),
\]
which is $\poly(n,\tau)$.

\emph{Step 5 (characteristic and minimal polynomial).} The coefficient of $t^{\,k-i}$ in $\chi_M$ is a sum
of $k\times k$ minors of order $i$, hence at most $\binom{k}{i}(\sqrt{k}\,2^{h(M)})^{i}$ in absolute
value; so $h(\chi_M)\le k\,h(M)+O(k\log k)$. The minimal polynomial divides $\chi_M$.

\emph{Step 6 (irreducible factors).} By Mignotte's bound, a divisor $f$ of a degree-$k$ integer polynomial
$g$ satisfies $\|f\|_\infty\le\binom{k}{\lfloor k/2\rfloor}\|g\|_\infty$, so
\[
h(f)\le h(\chi_M)+k .
\]

\emph{Step 7 (roots).} Represent a root $\alpha$ of $f$ by the class of $t$ in $\mathbb Q[t]/(f)$; its
height is $h(f)$. Cauchy's bound gives $|\alpha|\le2\|f\|_\infty^{1/\deg f}$, and the logarithmic height
satisfies $h(\alpha)\le h(f)+\log\deg f$.

\emph{Step 8 (eigenvectors).} Solving $(M-\alpha I)v=0$ over $L=\mathbb Q(\alpha)$ by Cramer expresses each
coordinate of $v$ as a quotient of two minors of order $k-1$ of $M-\alpha I$. Those minors are polynomials
in $\alpha$ of degree at most $k-1$ whose coefficients involve $k!$ products of entries of $M$; hence
\[
h(v)\le (k-1)\bigl(h(M)+h(\alpha)\bigr)+O(k\log k).
\]
The denominators are nonzero by simplicity of the spectrum.

\emph{Step 9 (subspaces and the image map).} The bases of $D$, $D^{\perp_{K_0}}$ and $T_D$ are kernels and
orthogonal complements of matrices with entries of the heights above, so they inherit an $O(k)$ factor.
The functionals $\varphi$, the prescribed image $\Phi_0$ and the entries of the cleared pencil are obtained
from these by $O(k^2)$ field operations, so their heights are again $\poly(n,\tau)$.

\emph{Step 10 (gcd).} The maximal minors have $\lambda$-degree at most $\omega\le k$ and heights
$\poly(n,\tau)$; the subresultant chain and hence the gcd have coefficients bounded by
$2^{O(k\log k)}\cdot\poly(n,\tau)$ (see \cite{vzgg13}), which is $\poly(n,\tau)$ for fixed $p$.

Combining Steps 0--10 yields Claim~\ref{clm:arithmetic}. The constants above are not optimized: each step
multiplies the height by a factor polynomial in $k$ and in the degree of the field, and the field degree is
at most $k^2$; no attempt has been made to minimize the exponents.
```

**给论文侧的注**：

1. 这节现在的语气是"标准界 + 不优化常数"，这是**诚实**的写法；不要把它改成"显式常数已算出"。
2. Step 2 的 $2p\,(2\tau+\cdots)$ 是 Hadamard 的直接结果；若审稿人要求更紧的界，可换成 Bareiss
   分式自由消元的界（同一量级，常数更小）。
3. Step 10 引用的 `vzgg13` 已在现有参考文献里（von zur Gathen–Gerhard）。

---

## 与草稿其它部分的一致性检查（我已核）

| 项 | 状态 |
|---|---|
| worked example 的 $\omega=2$、$\dim D^\circ=\omega=2$ | 与 416 的更正一致（本例 $k=2c$，故 $\omega=c$，是巧合） |
| 六个非零子式 | 与 §VIII 的不单调例子**同一组**（因为同一个 $A$），所以两处可以互引 |
| 论文的 $R_\lambda$、$P_D$ | worked example 里不必出现（只用到最大子式） |
| 高度链的符号 $h(\cdot)$ | 与论文正文一致（正文若未定义，请在此附录开头定义一次） |
