# Gap 2：上界——lift 的显式构造与剩下的一个代数条件

> **本文档自足**，不需要读本项目其它文件。它是 [Gap 1 文档](T_Gap1_非饱和lift.md) 的姊妹篇：
> Gap 1 管**下界**（"非饱和的 lift 不存在"），Gap 2 管**上界**（"饱和的 $\mathcal A$ 确实能 lift"）。
>
> **与初稿的区别**：初稿说"构造失败"。那是我**脚本的 bug**（漏了 $kN=0$ 这条约束）。
> 修正后构造通过（12/12）。现在 Gap 2 的状态是：**构造已显式、数值全过，
> 但"它为什么总成立"仍缺证明**——剩下的是一条**循环向量**条件。
>
> 日期：2026-10-22

---

## 摘要

在最小增广行数问题里，把 $(5a)$ 化成"$F=\Lambda M$"之后，**唯一的实质条件是秩等式**

$$(b)\qquad \operatorname{rank}(\lambda M-F)=\operatorname{rank}M\qquad\forall\lambda\in\mathbb{C}.$$

本文档问的是**上界**：给定一个"合适"的子空间 $\mathcal A$（维数 $d+1-p$、与 $S$ 交成一维），
能否显式造出一个满足 $(a)\wedge(b)$ 的 lift。

**答案（构造部分）是肯定的**，构造在 §2 给出，是纯线性的（解两个线性方程组，不需要搜索）。
**剩下的问题**是一条代数条件（§4）：

$$\boxed{\ l\notin\operatorname{im}(\lambda_iI-\Lambda)\ \text{对}\ \Lambda\ \text{的每个特征值}\ \lambda_i\ }$$

等价说法：$l$ 是 $\Lambda^{\mathsf T}$ 的**循环向量**。数值上它在 4/4 实例、12/12 随机参数上成立，
但**没有证明**。

---

## 1. 记号

$A\in\mathbb{R}^{n\times n}$、$C\in\mathbb{R}^{p\times n}$、$L_0\in\mathbb{R}^{1\times n}$。

$$K=\ker[C;CA]\ (\dim d),\quad N\in\mathbb{R}^{n\times d}\ \text{基},\quad
A'=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN,$$
$$R_0=AN-NA'\ (n\times d),\qquad S=\operatorname{row}(R_0)\subseteq\mathbb{R}^d,\qquad p=\dim S .$$

$\alpha_0=L_0N$、$\beta_0=L_0AN$。候选解 $L\in\mathbb{R}^{q\times n}$（首行 $L_0$），

$$M=LN,\quad F=LAN,\quad \rho=\operatorname{rank}M,\quad \mathcal A=\operatorname{row}(M)\subseteq\mathbb{R}^d .$$

$$(a)\iff\exists\Lambda:\ F=\Lambda M;\qquad (b)\iff\operatorname{rank}(\lambda M-F)=\rho\ \ \forall\lambda\in\mathbb{C}.$$

**lift 的线性约束**：$\ell_iN\in\mathcal A$ 且 $\ell_iAN\in\mathcal A$。

---

## 2. 显式构造（已验证）

固定 $\mathcal A$ 满足

$$\dim\mathcal A=\rho=d+1-p,\qquad \mathcal A\supseteq\operatorname{span}\{\alpha_0,\beta_0\},\qquad \dim(\mathcal A\cap S)=1 .$$

（存在性：$\operatorname{span}\{\alpha_0,\beta_0\}+S$ 的维数 $\le p+2<d$，补几个一般方向即可。）

取 $\mathcal A$ 的基 $v_1=\alpha_0,v_2,\dots,v_\rho$，取 $0\ne l\in L:=\mathcal A\cap S$。

> **(S1)** 分解：对每个 $i$，把 $v_iA'\in\mathbb{R}^d$ 写成
> $$v_iA'=a_i+s_i,\qquad a_i\in\mathcal A,\ s_i\in S .$$
> （存在，因为 $\mathcal A+S=\mathbb{R}^d$；不唯一，差一个 $L$。）
>
> **(S2)** 取 $\Lambda v_i:=a_i$（即把 $L$-自由度全部取 $0$；下文说明这个取法够用）。
>
> **(S3)** 解 $k_i\in\mathbb{R}^n$：
> $$k_iN=0\qquad\text{且}\qquad k_iR_0=\Lambda v_i+c_i\,l-v_iA'-v_iN^{+}R_0,$$
> 其中 $c\in\mathbb{R}^\rho$ 任意（如 $c=(1,1,0,\dots)$），$N^{+}=(N^{\mathsf T}N)^{-1}N^{\mathsf T}$。
>
> **(S4)** 令 $\ell_i:=v_iN^{+}+k_i$，$L^{*}:=\begin{bmatrix}L_0\\ \ell_1\\ \vdots\\ \ell_\rho\end{bmatrix}$（$q=\rho+1$ 行）。

**为什么 (S3) 可解**：右边逐项属于 $S$（$\Lambda v_i-v_iA'=-s_i\in S$、$c_il\in L\subseteq S$、$v_iN^{+}R_0\in S$）；
而 $\{k:kN=0\}\to S,\ k\mapsto kR_0$ 是**满射**（这是已证的一条引理）。所以 $k_i$ 总能解出。

**为什么 $(a)$ 自动成立**：$\ell_iN=v_iN^{+}N+k_iN=v_i$，故

$$f_i=\ell_iAN=(\ell_iN)A'+\ell_iR_0=v_iA'+v_iN^{+}R_0+k_iR_0=\Lambda v_i+c_i\,l\in\mathcal A .$$

于是 $F=M\Lambda+l\,c^{\mathsf T}$，且 $f_i\in\operatorname{row}(M)=\mathcal A$ ⟹ $(a)$ ✓。

**验证**（精确有理数，$(p,d,n)=(2,4,8)$）：

| 检验 | 规模 | 结果 |
|---|---|---|
| 随机 $(\eta,c)$ | 12 | **12/12** $(a)\wedge(b)$ ✓ |
| 固定 $(\eta,c)\in\{0,1\}^3\times\{0,1\}^3$ | 25 | **25/25** ✓ |
| 固定 $\eta=(1,1,0),c=(1,1,0)$，**跨实例** | 6 个实例 | **6/6** ✓ |
| $\eta=0$、$c=(1,1,0)$（最简形式）| 8 个实例 | **8/8** ✓ |

$$\Longrightarrow\ \textbf{上界的 lift 有显式构造};\quad (a)\wedge(b)\ \text{在全部 51 个测试点上成立}$$

---

## 3. $(b)$ 化简成一条特征值条件

因为 $F=M\Lambda+l\,c^{\mathsf T}$，

$$\lambda M-F=M(\lambda I-\Lambda)-l\,c^{\mathsf T}\ \xrightarrow{\ \text{在特征值}\ \lambda_i\ }\ \text{row space}=\underbrace{(\lambda_iI-\Lambda)(\mathcal A)}_{=:H_i,\ \dim=\rho-1}+\langle l\rangle$$

$$\boxed{\ (b)\iff l\notin H_i=(\lambda_iI-\Lambda)(\mathcal A)\quad\text{对每个特征值}\ \lambda_i\ }$$

**与 $c$ 无关**（只要 $c\ne0$）：$c$ 只决定"能否取到 $l$"，不决定秩。

---

## 4. 🎯 剩下的问题

> **要证**：对上面构造的 $\Lambda$（$\Lambda v_i=$ $v_iA'$ 的 $\mathcal A$-分量）与 $l$，
> $$l\notin\operatorname{im}(\lambda_iI-\Lambda)\qquad\text{对}\ \Lambda\ \text{的每个特征值}\ \lambda_i .$$
>
> 等价地：$l$ 是 $\Lambda^{\mathsf T}$ 的**循环向量**（每个左特征向量 $\phi_i$ 满足 $\phi_i\cdot l\ne0$）。

**已知的数值证据**：

| 检验 | 规模 | 结果 |
|---|---|---|
| Krylov 矩阵 $[l_c;\ l_c\Lambda;\ l_c\Lambda^2]$ 的秩 | 4 个实例 | **3/3/3/3**（满秩）✓ |
| $l\notin H_i$（间接：$(b)$ 成立）| 51 个点 | 全部 ✓ |

**为什么这不是平凡的**：$\Lambda$ 是**由 $(A',\mathcal A)$ 决定**的，不是可以随便选的；
"$l$ 恰好是循环向量"是关于 $(A,C,L_0)$ 的一条代数条件，我只有数值证据。

**反例可能存在于哪里**：若 $\Lambda$ 有两个不同的左特征向量 $\phi_1,\phi_2$ 都垂直于 $l$（即 $l$ 落在它们的张成里），
则 $l\in H_1\cap H_2$，$(b)$ 在两个特征值处同时失败。这在 $l$ 与 $\mathcal A$ 的"位置"特殊时可能发生。

---

## 4.1 ✅ **已证**：$0$ 必是 $\Lambda$ 的特征值

**命题**。上面构造的 $\Lambda:\mathcal A\to\mathcal A$ **总是奇异**的。

*证明*。$\Lambda=(I-\sigma)\circ(\cdot A')|_{\mathcal A}$，其中 $\sigma:\mathbb{R}^d\to S$ 是沿 $\mathcal A$ 的投影
（$\ker(I-\sigma)=S$）。故

$$\Lambda v=0\iff vA'\in S .$$

考虑 $\Psi:\mathcal A\to\mathbb{R}^d/S,\ v\mapsto[vA']$。则

$$\dim\ker\Psi\ \ge\ \dim\mathcal A-\dim(\mathbb{R}^d/S)\ =\ (d+1-p)-(d-p)\ =\ 1 .$$

$$\Longrightarrow\ \exists\,0\ne v\in\mathcal A:\ vA'\in S\ \Longrightarrow\ \Lambda v=0\ \Longrightarrow\ \det\Lambda=0\qquad\blacksquare$$

**数值确认**：10 个实例，$\operatorname{charpoly}(\Lambda)$ 的常数项**全为 $0$**（10/10）。

$$\boxed{\ 0\in\operatorname{spec}\Lambda\ \textbf{必然（对}\ \eta=0\ \textbf{的构造）};\quad \text{所以}\ \lambda=0\ \text{是必查的特征值} }$$

> ⚠️ **限定（2026-10-22 修订）**：上面的证明针对 $\eta=0$ 的构造（$\Lambda v=$ $vA'$ 的 $\mathcal A$-分量）。
> 在**其他分解** $\Lambda\mapsto\Lambda+\eta\otimes l$ 下，$\Lambda$ 可能**可逆**，$0$ 不再是特征值——
> 精确检验：$\eta=0$ 时 $\operatorname{charpoly}$ 常数项 $=0$；$\eta\in\{(1,0,0),(1,1,0),(0,1,1)\}$ 时分别为
> $93751/8300,\ -99377/8300,\ -884843/116200\ne0$。
> 所以"$0\in\operatorname{spec}\Lambda$"是**构造特定**的事实，不是不变量；不变量是**循环性**（见 §4.2a）。

**推论**：$(b)$ 要求

$$l\notin H_0=\Lambda(\mathcal A),\qquad H_0\ \text{是}\ \mathcal A\ \text{的超平面}\ (\dim=d-p=\rho-1)$$

这是 (b) 的**一个确定的、可检验的条件**（不再是"对所有特征值"这种模糊要求）。
## 4.2a ✅ **状态反馈不变性（采纳评审意见，2026-10-22）**

分解冗余 $\Lambda\mapsto\Lambda+\eta\otimes l$、$c\mapsto c-\eta$ 在转置侧就是

$$B:=\Lambda^{\mathsf T}\ \longmapsto\ B+b\,\eta^{\mathsf T},\qquad b:=l^{\mathsf T}\qquad(\textbf{rank-one state feedback})$$

而**状态反馈不改变可控子空间**，故

$$\operatorname{span}\{b,Bb,\dots\}=\operatorname{span}\{b,B_{\rm new}b,\dots\}$$
$$\boxed{\ l\ \text{对}\ \Lambda^{\mathsf T}\ \text{循环}\iff l\ \text{对}\ (\Lambda+\eta\otimes l)^{\mathsf T}\ \text{循环（对一切}\ \eta\text{）}\ }$$

**精确检验**（$\eta\in\{(0,0,0),(1,0,0),(1,1,0),(0,1,1)\}$）：Krylov 秩**全为 3/3** ✓

$$\Longrightarrow\ \textbf{循环性是不变量}\ \checkmark;\quad \text{而"}\ 0\in\operatorname{spec}\Lambda\ \text{"不是（§4.1 的限定）}$$

**这条引理解决了我此前的担心**（"判据依赖分解"）：真正依赖分解的是 "$l\notin\operatorname{im}\Lambda$"（$\lambda=0$ 处的写法），
而**不变量是循环性**。所以 Gap 2 的正确陈述就是"$l$ 循环"。

## 4.2 ⚠️ 一个必须小心的**分解冗余**（$\lambda=0$ 条件的精确化）

$(\Lambda,c)$ 不唯一：把 $\Lambda$ 换成 $\Lambda+\eta\otimes l$（即 $\Lambda v_i\mapsto\Lambda v_i+\eta_i l$）、
同时把 $c$ 换成 $c-\eta$，$F=M\Lambda+l\,c^{\mathsf T}$ **不变**。故 $(b)$ 是**内蕴**的，
但"$l\notin\operatorname{im}\Lambda$"这种写法**依赖分解**。

**$\lambda=0$ 处的内蕴条件**是（因为 $\lambda M-F\big|_{\lambda=0}=-F$）：

$$(b)\ \text{在}\ \lambda=0\ \text{处}\iff\operatorname{rank}F=\rho .$$

而 $F=M\Lambda+l\,c^{\mathsf T}$ 的行空间 $=\operatorname{im}\Lambda+\langle l\rangle$，故（取任一 $c\ne0$ 的分解）

$$(b)\big|_{\lambda=0}\iff l\notin\operatorname{im}\Lambda .$$

**关键结构**（用 $\Psi:\mathcal A\to\mathbb{R}^d/S,\ v\mapsto[vA']$）：

$$v\in\ker\Psi\ (vA'\in S)\ \Longrightarrow\ \Lambda v\in\mathcal A\cap S=L .$$

$$\Longrightarrow\ l\in\operatorname{im}\Lambda\iff l\in\Lambda(\ker\Psi)\iff \Lambda|_{\ker\Psi}\ne0\quad(\text{因}\ \dim L=1)$$

$$\boxed{\ (b)\big|_{\lambda=0}\iff\Lambda\ \text{在}\ \ker\Psi\ \text{上为零（对所选分解）} }$$

**数值事实**：$\eta\in\{(0,0,0),(1,0,0),(1,1,0)\}$ 三种分解下，Krylov 秩与 $(a)\wedge(b)$ **同时成立（9/9）**。

$$\Longrightarrow\ \text{这个分解依赖\textbf{没有}造成矛盾；但判据的\textbf{内蕴形式}仍需写出}$$
## 4.3 ❌ 对"最小自界子空间 + 伴随矩阵"路线的检验（2026-10-22）

回复建议：取 **最小自界（self-bounded）子空间** $\mathcal V_{\min}$（算法
$\mathcal Z_{k+1}=\mathcal Z_k+(A'\mathcal Z_k\cap(S+\mathcal Z_k))$，$\mathcal Z_0=\operatorname{span}\{\alpha_0,\beta_0\}$），
并断言此时 $\Lambda$ 呈 **Frobenius 伴随形**、$l$ 是首个基向量，从而 Krylov 平凡满秩。

**我实现了该算法并精确检验**（$(p,d)=(2,4)$，5 个实例）：

| 实例 | $\dim\mathcal Z_\infty$ | $\|\mathcal Z_\infty\cap S\|$ | $\dim(\mathcal Z_\infty+S)$ | admissible |
|---|---|---|---|---|
| seed 0–4 | **4**（$=d$，全空间）| **2** | 4 | True |

**结论**：

$$\boxed{\ \mathcal Z_\infty=\mathbb{R}^d\ \ (\dim=d=4),\quad \text{而我们需要的是}\ \dim=d+1-p=3,\ |\mathcal A\cap S|=1\ }$$

$$\Longrightarrow\ \textbf{该算法给出的是"最小 }A'\text{-不变闭包"，不是我们要的 admissible 子空间}$$

**为什么不一样**（结构性）：
- 我们要的 $\mathcal A$ 由两条条件**唯一确定维数**：$|\mathcal A\cap S|=1$ 与 $\mathcal A+S=\mathbb{R}^d$ ⟹ $\dim=d+1-p$；
- 而"自界/最小元"是**按包含**的格论极小，与"按维数固定"是**两件事**；
- 实测下格论极小元 = 全空间（因为从 $\{\alpha_0,\beta_0\}$ 出发的最小 $A'$-不变闭包已经把 $S$ 整个吸进来）。

$$\Longrightarrow\ \textbf{"伴随形 ⟹ 循环性"这条路线对本题}\ \textbf{不适用}$$

**仍然成立的**（回复中有价值的部分）：
- $\lambda=0$ 处的 PBH 形式与我的超平面条件**一致** ✓；
- 明确承认 **Gap 1 是 OPEN** ✓（与我对 Willems 1981 / Karcanias–Vafiadis 1993 的查证一致）；
- 接受了我指出的两处逻辑问题（$L_0$ 的 genericity、"测度为零⟹成立"）✓
## 4.4 Gap 2 的"几乎不变性"表述（与 cover 问题同一语言）

由 §4.2a（循环性是不变量），可以**任选分解**。循环子空间

$$\mathcal K:=\operatorname{span}\{l,\ \Lambda^{\mathsf T}l,\ (\Lambda^{\mathsf T})^2l,\dots\}\subseteq\mathcal A$$

正是**最小的**满足

$$l\in\mathcal K,\qquad \Lambda^{\mathsf T}\mathcal K\subseteq\mathcal K+\langle l\rangle$$

的子空间（标准事实：Krylov 子空间 = 最小的"模 $\langle l\rangle$ 不变"子空间）。于是

$$\boxed{\ (b)\iff\mathcal K=\mathcal A\iff\text{迭代}\ \mathcal K_{i+1}=\mathcal K_i+\Lambda^{\mathsf T}\mathcal K_i\ (\mathcal K_0=\langle l\rangle)\ \text{爬满}\ \mathcal A\ }$$

**这个表述把 Gap 2 变成了 cover 问题的语言**："$\langle l\rangle$ 在 $\Lambda^{\mathsf T}$ 下的 almost-invariant 闭包是否等于 $\mathcal A$"——
与 §4.3 引用的 Karcanias–Vafiadis 框架同类。

**精确检验**（4 个实例，$\eta=0$）：

| 实例 | $\dim\mathcal K_0,\mathcal K_1,\mathcal K_2,\mathcal K_3$ | 结论 |
|---|---|---|
| seed 0–3 | $1,\ 2,\ 3,\ 3$ | 两步入满秩 ⟹ 循环 ✓ |

$$\textbf{所以数值上迭代} \textbf{两步就到顶};\quad \text{但"为什么不会卡住"仍无证明}$$

**卡住意味着什么**：存在 $\mathcal K\subsetneq\mathcal A$ 使 $\Lambda^{\mathsf T}\mathcal K\subseteq\mathcal K+\langle l\rangle$——
即 $\mathcal A/\mathcal K$ 上有诱导映射且 $l$ 在其核里。**这正是要排除的。**
## 5. 我要的答案形式

1. **一个证明**：说明对上述 $\Lambda$，$l$ 总是循环向量（或给出使它成立的条件）；
2. **一个反例**：某个 $(A,C,L_0)$ 与满足三条的 $\mathcal A$，使 $l\in H_i$ 对某个特征值成立（于是 $(b)$ 在该处失败）；
3. 或者指出这条条件**等价于**某个已知概念（例如 PBH 型的可控性/可观测性条件），我可以去查文献。

**验证成本**：给一个 $n\le8$、$d\le5$ 的数值例子，我有精确有理数脚本，一秒判定。

---

## 6. 这件事的意义

$$\text{Gap 2 证成}\ +\ \text{Gap 1 证成}\ \Longrightarrow\ q_{\min}=\max(3,\ d+2-p)\ \Longrightarrow\ q_{\min}\in\mathrm{P}\ \Longrightarrow\ \textbf{原命题（NP-hard）为假}$$

单独看，Gap 2 就是"**这个显式构造是否总给出合法 lift**"——一个关于循环向量的具体问题。

---

## 7. 复现

```bash
python scripts/core/c160_gap2_construction.py   # 构造 + 检验（(a)∧(b) 12/12）
```

**注意**：本构造的脚本里必须同时解 $kN=0$ 与 $kR_0=\cdots$——
只解后者会让 $\ell_iN\ne v_i$，整个代数关系崩掉（我第一版就是这样错的，得到 0/12）。
