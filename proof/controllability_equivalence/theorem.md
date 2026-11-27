# Q5：$(5b)\iff(S_\tau,\beta|_{\mathcal H})$ 可控 —— 证明进展与精确缺口

> 这是主线的瓶颈（[docs/05](../../docs/05_open_questions.md) Q5）。
> **本文的结果**：在 $B\subseteq\mathcal U$ 的情形**证明了**该等价；一般情形下找到一个明确的障碍项，
> 并把它写成一个可检验的附加条件。所以 Q5 从"未证"变成"**一条已证 + 一个精确缺口**"。

## 1. 设定

$X=\mathbb C^n/\mathcal J$、$B=\pi(\mathcal J A)\subseteq X$、$T:X\to X/B$、$U=\pi(\mathcal V)$、$H=\mathcal V\cap\mathcal J$。
取截面 $s:U\to\mathbb C^n$（$\pi\circ s=\mathrm{id}$）、$\tau:U\to\mathcal J$，则
$$\mathcal V=(s+\tau)(U)\oplus H .$$
记 $\beta:=\pi\circ(A|_{\mathcal J}):\mathcal J\to X$（即 $\beta(j)=\pi(jA)$），$S_\tau:=(T+\beta\tau)|_U:U\to (U+B)/B$（由 $(5a)$ 保证落入 $(U+B)/B$）。

取 $U$ 的基 $u_1,\dots,u_\rho$、$H$ 的基 $h_1,\dots,h_c$，则 $\mathcal V$ 的基为
$$\ell_i=s(u_i)+\tau(u_i)\ (i\le\rho),\qquad h_k\ (k\le c).$$
于是
$$\pi(\ell_i)=u_i,\quad \pi(\ell_iA)=\widetilde T(u_i)+\beta(\tau(u_i)),\quad \pi(h_kA)=\beta(h_k),$$
其中 $\widetilde T(u):=\pi(s(u)A)$（模 $B$ 与 $s$ 的选取无关）。

## 2. 铅笔的行

**引理 2.1** $Q_{\mathcal V}(\lambda)=\lambda\pi(\mathcal L)-\pi(\mathcal LA)$ 的行是
$$\underbrace{(\lambda I-S_\tau)u_i\ (i\le\rho)}_{\in\ \mathcal U+B},\qquad \underbrace{-\beta(h_k)\ (k\le c)}_{\in\ \mathcal U\ (\text{由 }(5a))}.$$

*证明*：代入 §1 的 $\pi(\ell_i)$、$\pi(\ell_iA)$。$\square$

记 $R_\lambda\subseteq\mathcal U+B$ 为这些行张成的子空间。

**推论 2.2** $(5b)\iff\dim R_\lambda=\rho\ \ \forall\lambda$。

*证明*：$(5b)$ 就是 $\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho$（[docs/02](../../docs/02_theorems_proven.md) B.1），而秩 $=$ 行空间的维数。$\square$

## 3. 一个方向（不需要额外假设）

**命题 3.1** 若存在 $\lambda$ 使 $(S_\tau,\beta|_{\mathcal H})$ 在 $(\mathcal U+B)/B$ 上**不可控**，则 $\dim R_\lambda<\rho$，即 $(5b)$ 失败。

*证明*：不可控 $\iff$（PBH，在 $(\mathcal U+B)/B$ 中）存在 $\lambda$ 与 $0\ne\varphi\in\big((\mathcal U+B)/B\big)^*$ 使
$$\varphi\circ S_\tau=\lambda\varphi,\qquad \varphi\circ\beta|_{\mathcal H}=0 .$$
把 $\varphi$ 沿 $B$ 零延拓成 $\tilde\varphi\in(\mathcal U+B)^*$（即 $\tilde\varphi|_B=0$）。则由引理 2.1 的每一项：
$$\tilde\varphi\big((\lambda I-S_\tau)u_i\big)=\lambda\tilde\varphi(u_i)-\varphi(S_\tau u_i)=0,\qquad \tilde\varphi(\beta(h_k))=0 .$$
故 $R_\lambda\subseteq\ker\tilde\varphi$，而 $\ker\tilde\varphi\subsetneq\mathcal U+B$ 是真子空间。又 $R_\lambda\subseteq\mathcal U+B$ 且
$$\dim R_\lambda\le\dim(\mathcal U+B)-1 .$$
当 $\dim(\mathcal U+B)=\rho$（即 $B\subseteq\mathcal U$）时立即得 $\dim R_\lambda\le\rho-1<\rho$ ✓。$\square$

**推论 3.2（$B\subseteq\mathcal U$ 情形）** 若 $B\subseteq\mathcal U$，则
$$(5b)\iff(S_\tau,\beta|_{\mathcal H})\ \text{可控}.$$

*证明*：命题 3.1 给 $(5b)\Rightarrow$ 可控。反向：若不可控则 $(5b)$ 失败（命题 3.1），故可控 $\Rightarrow(5b)$。$\square$

（反方向也可直接写：设 $(5b)$ 失败，取 $0\ne\tilde\varphi$ 灭掉 $R_\lambda$；则由 $R_\lambda$ 含 $(\lambda I-S_\tau)u_i$ 与 $\beta(h_k)$ 得 $\tilde\varphi\circ S_\tau=\lambda\tilde\varphi$、$\tilde\varphi\circ\beta|_{\mathcal H}=0$，即不可控。）

## 4. 一般情形的精确缺口

若 $B\not\subseteq\mathcal U$，命题 3.1 只能给出 $\dim R_\lambda\le\dim(\mathcal U+B)-1$，**不足以**推出 $\dim R_\lambda<\rho$。此时的真实条件是

$$\boxed{\ (5b)\iff\underbrace{(S_\tau,\beta|_{\mathcal H})\ \text{在}\ (\mathcal U+B)/B\ \text{上可控}}_{(\mathrm{i})}\ \wedge\ \underbrace{\dim R_\lambda=\rho\ \forall\lambda}_{(\mathrm{ii})}}$$

而 $(\mathrm{ii})$ 与 $(\mathrm{i})$ 的差别**正是** $R_\lambda$ 落在 $B$ 里的那部分：
$$\dim R_\lambda=\dim\overline{R_\lambda}+\dim\big(R_\lambda\cap B\big),\qquad \overline{R_\lambda}\subseteq(\mathcal U+B)/B .$$
$(\mathrm{i})$ 只控制 $\overline{R_\lambda}$（要求其维数 $=\dim(\mathcal U+B)/B$），$(\mathrm{ii})$ 额外要求 $R_\lambda\cap B$ 的维数取到 $(\mathcal U+B)/B$ 之外应有的值。

**所以 Q5 的精确形式是**：

$$\text{Q5}\iff\Big[\,B\subseteq\mathcal U\ \text{（此时（ii）自动）}\ \Big]\ \text{或}\ \Big[\text{附加条件（ii）由 }(5a)\text{ 自动成立}\Big].$$

## 5. 为什么数值上 16276/16276 全对

若那些 ci 子空间都满足 $B\subseteq\mathcal U$（$B$ 很小、$\rho$ 相对大时自动成立），则由推论 3.2 该等价成立——这解释了为什么穷举从未发现反例。

**可检验的预测**：只要构造出 $B\not\subseteq\mathcal U$ 的实例，且 $(\mathrm{ii})$ 不自动成立，就应有"可控但 $(5b)$ 失败"的反例。**这是下一步该做的实验**（见 §6）。

## 6. 下一步（两条，都可做）

1. **构造 $B\not\subseteq\mathcal U$ 的反例**：取 $\mathcal J$ 非 $A$-不变（$B\ne0$）、$\rho$ 很小（$\rho<\dim B$），检查 $(\mathrm{ii})$ 是否失效；
2. **直接证 $(\mathrm{ii})$ 自动成立**：即由 $(5a)$ 与可控性推出 $R_\lambda\cap B$ 的维数是对的——若成立，Q5 无条件成立，$(k,1)$ 全线打通。

## 7. 与主线的关系

- 推论 3.2 已经把 Q5 在 $B\subseteq\mathcal U$ 的情形**变成了定理**；
- 一般情形只剩 §4 的 (ii)；
- [proof/rho1_layer/theorem.md](../rho1_layer/theorem.md) 的定理 4.1 因此可以改写为"$B\subseteq\mathcal U$ 时无条件成立"。

---

## 8. ⚠️ 2026-10-27 实验后的更正：按字面表述，Q5 **本身有缺陷**

用 [tools/layer_search/c200_q5_probe.py](../../tools/layer_search/c200_q5_probe.py) 探测后发现一个**表述层面的问题**：

**观察**：$B=\pi(\mathcal J A)$ 的定义就是 $\operatorname{span}\{\beta(J_k)\}_{k}$（因为 $\beta(j)=\pi(jA)$、$J_1..J_j$ 是 $\mathcal J$ 的基）。于是对任何 $h\in\mathcal H\subseteq\mathcal J$，
$$\beta(h)\in B\quad	ext{恒成立}.$$
把 $(\mathcal S_	au,\beta|_{\mathcal H})$ 放到商空间 $(\mathcal U+B)/B$ 上看时，**输入矩阵恒为零**，于是"可控"退化成
$$(\mathcal S_	au,\beta|_{\mathcal H})\ 	ext{可控}\iff(\mathcal U+B)/B=0\iff\mathcal U\subseteq B,$$
而后者显然不是 $(5b)$。**所以"$(5b)\iff$ 可控"按字面（$B=\pi(\mathcal J A)$、输入 $=\beta|_{\mathcal H}$）不可能是正确的陈述。**

**这解释了 c191 的异常**：在顶层实例上，"铅笔 65/65、可观测 65/65、可控 63/65"——可控正是那个不对的。

**结论**：

1. **删掉"可控"这条提法**（含旧交接文档的 Theorem 9 与 c192 的注释）。可用的层判据是**铅笔形式**：
   $(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=
ho\ \forall\lambda$（[docs/02](../../docs/02_theorems_proven.md) B.1），
   顶层再加 PBH 可观测性（B.2）、$c_0=1$ 时退化为循环向量（B.5）。
2. §2–§4 的推导（$R_\lambda$、$B\subseteq\mathcal U$ 时的等价）在**代数上是对的**，但它刻画的是 $R_\lambda$ 的**模 $B$ 部分**，而 §8 说明这部分在 $\beta|_{\mathcal H}$ 作输入时是退化的。因此 §4 的"缺口 (ii)"不是"待证"，而是**这个提法本身缺一个正确的输入算子**。
3. 若将来要用可控性语言，必须换一个**非零的输入算子**（例如把 $\mathcal H$ 在 $\mathcal V$ 里的作用直接写成 $Q_{\mathcal V}$ 的某几行，而不是 $\beta|_{\mathcal H}$）。

**教训**（已并入 [CLAUDE.md](../../CLAUDE.md) §10.1）：**一个"等价"在数值上 16276/16276 成立，也可能只是因为在采样到的情形里某一项恒为零。**
遇到"某结构定理只在一个方向上被验证"，先检查其中一个对象是否**退化成零**。
