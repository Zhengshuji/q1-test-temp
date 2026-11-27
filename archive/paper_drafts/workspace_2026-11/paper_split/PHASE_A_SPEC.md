# Phase A 修复规格（数学缺口 M2、M5、M6、M7、M8、M9、M10）

> 对象：`paper/current/paper_I_dec.tex`（只改这一个文件）。
> 原则：**不改结论**；只修"陈述与证明对不上"的地方。每条给出问题、目标文本、验收方式。

---

## M5（最重要）：`lem:rationalbasis` 里的 $D$ 与它的唯一用途不是同一个矩阵

**现状**（陈述）："a matrix $D$ with $\operatorname{row}D=\{x\in\mathbb{Q}^m:xM=0\}$"
—— 这是 $M$ 的**左**零空间，尺寸 $(m-r)\times m$，行向量在 $\mathbb{Q}^m$ 里。

**唯一用途**：$\Phi$ 的第 (iv) 项用 $D[(X_iB)^{\mathsf T};(G_iB)^{\mathsf T}]=0$，其中
"$D$ is a rational matrix with $\ker D=\mathcal T=\operatorname{row}[N\ AN]$"（§III 的定义），
即 $D$ 作用在 $\mathbb{Q}^{2k}$ 上、$\ker D$ 是 $\operatorname{row}M$，尺寸 $(2k-d_0)\times2k$。

**为什么冲突**：行 $D$ = 左零空间 $\{x:xM=0\}\subset\mathbb{Q}^n$ ⟺ 行 $D$ 张成 $\ker M$（把 $M$ 看作左乘映射）。
而 $\ker D=\operatorname{row}M$ 要求行 $D$ 张成 $(\operatorname{row}M)^\perp=\ker M$（作为 $M$ 的**右**零空间）——
两者张成的是**同一个子空间**，但一个是 $M$ 的右零空间在 $\mathbb{Q}^{2k}$ 内的基（转置形态），
另一个在 $\mathbb{Q}^n$ 内。对 $M=[N\ AN]$（$n\times2k$）而言前者是 $(2k-d_0)\times2k$、后者是 $(n-d_0)\times n$，
**不是同一个矩阵**。

**修法（已核对可行）**：把陈述里的第三个对象改成 (B.2) 真正要的那个，即
"a matrix $D\in\mathbb{Q}^{(n-r)\times n}$ with $\ker D=\operatorname{row}M$"，
并注明它与 $N$ 的关系：行 $D$ 是 $\ker M$ 的一组基（$N$ 的列也是），可由同一消元作用在 $M^{\mathsf T}$ 上得到。
$\operatorname{bits}D\le\tau_M$ 的结论与证明都不变（同一个消元、同样的子式估计）。
**收益**：`tab:bitlen` 里那行 "D with $\ker D=\operatorname{row}M$" 本来就写对了，改完引理后全篇一致；
`lem:coeff`(i) 里"applying the lemma again to $[N\ AN]$ … and hence the matrix $D$" 也随之正确。

---

## M2：`lem:zero` 的 (iii)⇒(iv) 有理性缺口

**现状**：由 $\sum_Ig_If_I=1$（`lem:bezout` 给的是**实**系数 $g_I$）构造 $S(\lambda)\in\mathbb{Q}[\lambda]^{\omega\times q}$。

**问题**：`lem:bezout` 的结论只保证 $g_I$ 实；而 (iv) 断言 $S$ 的系数在 $\mathbb{Q}$。

**修法**：在该步加一句（不要改 `lem:bezout`）：
> The coefficients of the $g_I$ solve a linear system with rational data, because the $f_I$ have rational
> coefficients; a rational linear system that is solvable over $\mathbb{R}$ is solvable over $\mathbb{Q}$,
> so the $g_I$ may be taken rational. The cofactors of $Q$ are rational polynomials as well, so the
> matrix $S$ assembled from them below has rational coefficients.

（或用一句更短的等价表述。）验收：`S(\lambda)\in\mathbb{Q}[\lambda]` 的出现处之前，$\mathbb{Q}$ 的来源已交代。

---

## M6：`lem:rationalbasis` 证明里的公分母句是错的

**现状**："the common denominator is a product of at most $r$ pivot minors, which adds only $O(r\log r)$ bits"。

**问题**：$r$ 个子式之积的位长是 $O(r^2(\tau+\log n))$，不是 $O(r\log r)$；照此推不出宣布的 $\tau_M$。

**修法**：换成 Bareiss（无分式消元）的正确机制：
> fraction-free elimination carries a single $r\times r$ minor as common denominator at every stage,
> so the entries of $N$, $R$ and $D$ are ratios of two $r\times r$ minors of $M$, of bit length at most
> $2r(\tau+\log r+1)$.

---

## M7：$\tau_M$ 用 $O(\cdot)$ 定义却在结论里当常数用

**现状**：陈述里 "put $\tau_M=O(r(\tau+\log n))$. Then … have bit length at most $\tau_M$"。

**问题**：含隐藏常数，句子不是良构的断言。

**修法**：把 $\tau_M$ 定义成显式表达式，使证明里给出的界**严格小于**它：
> put $\tau_M=2r(\tau+\log r+1)$。

（Hadamard：$r\times r$ 子式的位长 $\le r(\tau+\tfrac12\log r)+1$；Cramer 给之比值的界 $\le2r(\tau+\log r+1)$。）
并相应把证明里的估计写成 $\le\tau_M$。若消元给出的界是 $O(r(\tau+\log n))$ 的另一个常数，
取足够大的显式常数即可（例如 $4r(\tau+\log n+2)$），但**必须显式**。

---

## M8：`lem:coeff`(i) 把未知的自由行当成输入

**现状**："Each entry of $H=LN$ is a sum of $n$ products of an input entry with an entry of $N$"。

**问题**：$r\ge1$ 时 $L$ 的下 $r$ 行是**未知量**（自由行），$\operatorname{bits}(H)$ 对任意可行 $L$ 没有输入级上界。
算法里真正的变量是枢轴块 $X$ 与 $G$。

**修法**：把 (i) 的对象限定为**算法实际使用的代表**：
> the pivot block $X$, the block $G$ and the prescribed products $h^0=L_0N$, $g^0=L_0AN$ produced by the
> elimination of Section~\ref{sec:pivot} have entries of bit length $\operatorname{poly}(n,\mathcal L)$,

并说明理由（它们是输入矩阵的子式之比）。不要再对"任意可行 $L$ 的 $H$"断言位长。

---

## M9：`lem:coeff`(ii) 引用了不存在的"系数矩阵"

**现状**："Hadamard applied to its coefficient matrix bounds each of its $\omega+1$ coefficients"。

**问题**：$\det(\lambda H_I-H_{A,I})$ 没有 $\omega\times\omega$ 的系数矩阵；系数是 $\lambda$ 的多项式系数。

**修法**：改为 Laplace 展开 + 两次 Hadamard：
> By Laplace expansion the coefficient of $\lambda^a$ is a signed sum over $\binom{\omega}{a}$ index sets of
> $\det H_{I,S}\det H_{A,I,S^{c}}$, and Hadamard's inequality bounds each product by
> $O\bigl(\omega(\operatorname{bits}H+\log\omega)\bigr)$ bits.

（结论 $\operatorname{bits}c_{i,a}=\operatorname{poly}(n,\mathcal L)$ 不变。）

---

## M10：`lem:coeff`(iii) 的项数与 `tab:bitlen` 矛盾

**现状 (a)**："$Z^{\mathsf T}Z$ is a sum of at most $\binom{\ell}{\omega}\le2^{\ell}$ terms"——把 Cauchy–Binet 的**列集个数**当成了 $Z^{\mathsf T}Z$ 的项数。
**现状 (b)**：(iii) 的结论给 $f(\ell)\operatorname{poly}(\mathcal L)$，而 `tab:bitlen` 说 $\beta=\operatorname{poly}(\mathcal L)$。

**修法**：
1. 项数按 §IV 的 `item:coef` 写法：$(Z^{\mathsf T}Z)_{t,t'}=\sum_{j}S_{t-j,t'-j}$，项数 $\le\omega\cdot\#\{I\}$，其中 $\#\{I\}=\binom{q}{\omega}\binom{k}{\omega}$；对数因子 $\le\omega+2\omega\log n=O(n)$ 位。
2. 结论统一为 $\operatorname{poly}(n,\mathcal L)$（与 `tab:bitlen` 一致），并删去 $f(\ell)$ 因子；若某处引用了 (iii) 的 $f(\ell)$ 形式，一并改成 $\operatorname{poly}$。

---

## 验收

```
cd workspace\_scratch\cur1
remove p.aux; copy paper\current\paper_I_dec.tex p.tex
pdflatex -interaction=nonstopmode p.tex   (twice)
```
必须：`Output written` 存在、`!` 行数 0、`Reference ... undefined` 0、`Citation ... undefined` 0、`Overfull` 0。

另需自查：
- `grep -n "row D=\|rowD=" ` 应无残留的左零空间表述；
- `grep -n "D=O(r\|O(r\\log r)"` 应无残留；
- `grep -n "binom{\\\\ell}{\\\\omega}"` 在 (iii) 处应已改为正确的项数；
- `grep -n "f(\\\\ell)\\\\operatorname{poly}(\\\\mathcal L)"` 在 (iii) 的结论处应已改为 $\operatorname{poly}(n,\mathcal L)$。
