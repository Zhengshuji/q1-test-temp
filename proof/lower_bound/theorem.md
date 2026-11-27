# $q_{\min}$ 的下界：完整证明

> 对应 [docs/02](../../docs/02_theorems_proven.md) 的 A.1–A.3。本文是**展开版**（写论文可直接用）。

## 0. 记号

$A\in\mathbb C^{n\times n}$、$C\in\mathbb C^{p\times n}$、$L_0\in\mathbb C^{r\times n}$；$\mathcal L=\binom{L_0}{R}$ 行满秩，$q=\operatorname{rank}\mathcal L$。

$$\mathcal J=\operatorname{row}[C;CA],\quad j=\dim\mathcal J,\quad K=\ker[C;CA],\quad d=n-j,\quad \pi:\mathbb C^n\twoheadrightarrow\mathbb C^n/\mathcal J .$$

对解 $\mathcal L$ 记 $\mathcal V=\operatorname{row}\mathcal L$、$S=\operatorname{row}L_0$，

$$\rho=\dim\pi(\mathcal V),\qquad c=\dim(\mathcal V\cap\mathcal J),\qquad c_0=\dim(S\cap\mathcal J).$$

## 1. 两个条件的等价形式

**引理 1.1（$(5a)$ 的行空间形式）**
$$(5a)\iff \mathcal V A\subseteq\mathcal V+\mathcal J .$$

*证明*：$\operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C]$ 是说
$\operatorname{row}(\mathcal LA)+\operatorname{row}[\mathcal L;CA;C]=\operatorname{row}[\mathcal L;CA;C]$，
即 $\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}\mathcal L+\operatorname{row}[C;CA]=\mathcal V+\mathcal J$。$\square$

**引理 1.2（$(5b)$ 的商形式）**（= [docs/02](../../docs/02_theorems_proven.md) B.1）
$$(5b)\iff \operatorname{rank}\big(\lambda\,\pi(\mathcal L)-\pi(\mathcal LA)\big)=\rho\quad\forall\lambda\in\mathbb C .$$

*证明*：把 $[\lambda\mathcal L-\mathcal LA;CA;C]$ 对 $\mathcal J=\operatorname{row}[C;CA]$ 取商；左端的秩等于 $\operatorname{rank}(\lambda\pi(\mathcal L)-\pi(\mathcal LA))$，右端等于 $\dim\pi(\mathcal V)=\rho$。$\square$

## 2. 维数分解（A.1）

**命题 2.1** $q=\rho+c$。

*证明*：考虑正合列
$$0\to\mathcal V\cap\mathcal J\to\mathcal V\xrightarrow{\ \pi\ }\pi(\mathcal V)\to0 .$$
$\pi|_{\mathcal V}$ 的核是 $\mathcal V\cap\ker\pi=\mathcal V\cap\mathcal J$，像为 $\pi(\mathcal V)$，故 $\dim\mathcal V=\dim(\mathcal V\cap\mathcal J)+\dim\pi(\mathcal V)$，即 $q=c+\rho$。$\square$

## 3. $c\ge\max(c_0,1)$（A.2）

**命题 3.1** $c\ge c_0$。

*证明*：$S=\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L=\mathcal V$，故 $S\cap\mathcal J\subseteq\mathcal V\cap\mathcal J$。$\square$

**命题 3.2** $c\ge 1$。

*证明*：反设 $c=0$，即 $\mathcal V\cap\mathcal J=0$。

*第一步（压缩映射）*：由引理 1.1，$\mathcal V A\subseteq\mathcal V+\mathcal J$；又 $\mathcal V\cap\mathcal J=0$ 给出直和分解 $\mathcal V+\mathcal J=\mathcal V\oplus\mathcal J$。于是每个 $v\in\mathcal V$ 的 $Av$ 有唯一分解
$$Av=\varphi(v)+j_v,\qquad \varphi(v)\in\mathcal V,\ j_v\in\mathcal J,$$
且 $\varphi:\mathcal V\to\mathcal V$ 是**线性**映射（$A$ 线性 + 分解唯一）。

*第二步（特征向量）*：$\mathbb C$ 代数闭、$\dim\mathcal V=q\ge1$，故 $\varphi$ 有特征向量：$\exists\,0\ne v\in\mathcal V,\ \lambda\in\mathbb C$ 使 $\varphi(v)=\lambda v$。

*第三步（矛盾）*：由分解，$(\lambda I-A)v=\lambda v-Av=-j_v\in\mathcal J$，于是
$$\big(\lambda\pi(\mathcal L)-\pi(\mathcal LA)\big)\,\hat v=\pi\big((\lambda I-A)v\big)=0,$$
其中 $\hat v\ne0$ 是 $v$ 在 $\mathcal V\cong\mathbb C^{q}$ 中的坐标向量。故
$$\operatorname{rank}\big(\lambda\pi(\mathcal L)-\pi(\mathcal LA)\big)\le q-1<\rho,$$
最后一个不等号用 $c=0\Rightarrow\rho=q$（命题 2.1）。这与引理 1.2 矛盾。$\square$

> **注**：命题 3.2 是"$c\ge1$ 恒成立"的全部内容；它的意思是**任何解都必须与 $\mathcal J$ 有非平凡交**，这就是为什么 $\rho<q$ 恒成立（也解释了为什么 $q=\rho$ 不可能：见 `proof/refuted/` 里的 R1）。

## 4. 下界（A.3）

**定理 4.1** 对任何解，$q\ge r+\varepsilon$ 且 $q\ge\rho+\max(c_0,1)$，其中
$$\varepsilon=\begin{cases}0,&L_0\ \text{本身是解},\\ 1,&\text{否则}.\end{cases}$$
因此
$$q_{\min}\ \ge\ \max\big(r+\varepsilon,\ \rho_{ci}+\max(c_0,1)\big),\qquad \rho_{ci}=P(T,B,U_0)\ \text{（算术侧最小，[proof/p_is_polynomial/](../p_is_polynomial/README.md)）}.$$

*证明*：$q\ge r$ 因 $\mathcal L$ 包含 $L_0$ 的 $r$ 行；若 $L_0$ 不是解而 $q=r$ 则 $\mathcal L=L_0$ 是解，矛盾，故 $q\ge r+1$。
第二式由命题 2.1、3.1、3.2：$q=\rho+c\ge\rho+c_0$ 且 $c\ge1$。最后对 $\rho$ 取下确界（$= \rho_{ci}$）。$\square$

> **下界不紧**：见 [proof/refuted/](../refuted/README.md) R4（$n{=}4$ 实例：下界 $3$、真值 $4$）。
> 因此**不能**把定理 4.1 反过来当公式用——这正是四个闭式被推翻的原因。

## 5. 复核

| 项 | 脚本 | 结果 |
|---|---|---|
| A.1 / A.2 / A.3 | `python proof/lower_bound/verify.py` | 12 个随机可行解 + 7 个证书解，全部通过 |

复核只是**验证**（有限实例），不构成证明；证明在本文 §2–§4。
