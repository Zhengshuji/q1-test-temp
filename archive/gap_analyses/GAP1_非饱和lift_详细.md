# Gap 1：非饱和的 lift 是否必能压到一行？
---

## 0. 一页摘要

**一句话**：我有一族线性系统参数，能证明"任何解的行空间 $\mathcal A$ 必须与某个固定子空间 $S$ 相交非空"；
**卡在**"$\mathcal A+S$ 是否必须是全空间"。后者等价于我已经拿到的下界的一半。

$$\boxed{\ \textbf{Gap 1}:\quad \mathcal A+S\ne\mathbb{R}^d\ \wedge\ \text{存在解}\ \Longrightarrow\ \exists\ \rho=1\ \text{的解（P7）}\ }$$

| 项 | 状态 |
|---|---|
| 数值证据 | 所有非饱和构型搜索 **0 命中**（~100 次，多族） |
| 证明 | ❌ 无 |
| 反例 | ❌ 无 |

**我要什么**：§9 给了四种可接受的回答形式（证明 / 反例 / 结构性归约 / 指出我的等价链有错）。

---

## 1. 背景与记号

给定 $A\in\mathbb{R}^{n\times n}$、$C\in\mathbb{R}^{p\times n}$、$L_0\in\mathbb{R}^{r\times n}$。要找
$R\in\mathbb{R}^{k\times n}$ 使 $L=\begin{bmatrix}L_0\\R\end{bmatrix}$（$q=r+k$ 行）满足

$$(\mathrm{5a})\quad\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(\mathrm{5b})\quad\operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \ \forall\lambda\in\mathbb{C}.$$

**约化**。令 $K=\ker[C;CA]$（$\dim d$），$N\in\mathbb{R}^{n\times d}$ 列满秩基，

$$A':=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN,\qquad R_0:=AN-NA',\qquad S:=\operatorname{row}(R_0)\subseteq\mathbb{R}^d,\qquad p:=\dim S .$$

记 $\alpha_0:=L_0N$、$\beta_0:=L_0AN$。对候选 $L$：

$$M:=LN,\quad F:=LAN,\quad \rho:=\operatorname{rank}M,\quad \mathcal A:=\operatorname{row}(M)\subseteq\mathbb{R}^d .$$

**两个等价**（初等）：

$$(\mathrm{5a})\iff\operatorname{row}(F)\subseteq\mathcal A\iff\exists\Lambda:\ F=\Lambda M ;\qquad
(\mathrm{5b})\iff\operatorname{rank}(\lambda M-F)=\rho\ \ \forall\lambda .$$

**lift 的线性约束**（反复用到）：

$$\ell_iN\in\mathcal A\quad\text{且}\quad\ell_iAN\in\mathcal A\qquad(i=1,\dots,q).$$

**P7 的定义（完整版，2026-10-22 修正）**：

$$\mathcal S:=\{\ell:\ \ell N\in\operatorname{span}\{\alpha_0\},\ \ell AN\in\operatorname{span}\{\alpha_0\}\}$$
$$\boxed{\ \mathrm{P7}:\quad L_0\in\mathcal S\ \ \wedge\ \ \dim\operatorname{im}\big(\mathcal S\to\mathbb{R}^2,\ \ell\mapsto(u,w)\big)=2\ }$$
$$\text{其中}\ \ell N=u\,\alpha_0,\ \ell AN=w\,\alpha_0 .$$

**注意 $L_0\in\mathcal S$ 这一半是不可省的**：它等价于

$$\alpha_0\in\operatorname{span}\{\alpha_0\}\ (\text{平凡})\quad\text{与}\quad\boxed{\beta_0\in\operatorname{span}\{\alpha_0\}}$$

（后者由 $(5a)$ 强制：单行解的 $\mathcal A=\operatorname{span}\{\alpha_0\}$ 必须容纳 $\beta_0=L_0AN$）。
所以"$\exists\ell:\ell N\parallel\alpha_0,\ \ell AN\parallel\alpha_0$"**只是 P7 的一半**；
若 $\beta_0\not\parallel\alpha_0$，P7 为**假**，无论这样的 $\ell$ 存在与否。

> ⚠️ **我此前的文档把 P7 简写成只有 $\ell$ 的那一半**，这是**错的**（2026-10-22 经外部评审指出后修正）。
> 正确的等价仍成立：**P7 $\iff$ 存在 $\rho=1$ 的解**（因为完整定义已包含 $L_0\in\mathcal S$）。

---

## 2. Gap 1 的精确陈述

> **Gap 1**。设 $(L,\Lambda)$ 是解，$\rho=\operatorname{rank}M\ge2$。则
> $$\mathcal A+S=\mathbb{R}^d .$$

**等价形式**（以下四条互相等价，前两条我已证，后两条是重述）：

1. 任何 $\rho\ge2$ 的解满足 $\mathcal A+S=\mathbb{R}^d$；
2. 若 $\mathcal A+S\ne\mathbb{R}^d$ 且有解，则存在 $\rho=1$ 的解（P7）；
3. P7 假 $\Longrightarrow$ 每个"可 lift 的"$\mathcal A$ 都满足 $\mathcal A+S=\mathbb{R}^d$；
4. 非饱和（$\mathcal A+S\ne\mathbb{R}^d$）的 $\mathcal A$ 一律不可 lift。

**为什么它不平凡**：它**不是**说"$\mathcal A+S=\mathbb{R}^d$ 自动成立"——那是**假**的。
$\rho=1$ 的解取 $\mathcal A=\operatorname{span}\{\alpha_0\}$，此时 $\dim(\mathcal A+S)\le1+p$，**可以严格小于 $d$**。
所以 Gap 1 的真实内容是：

$$\textbf{"非饱和的 lift 必可压到一行"}$$

**它为什么重要**：它等价于下界 $\rho\ge d-p+1$（见 §3.3），
与上界（已构造，见姊妹文档）合起来给出 $q_{\min}=\max(3,d+2-p)$，从而原问题（NP-hard？）的答案为**假**。

---

## 3. 已经证明的（可当工具用）

### 3.1 定理 T2：任何解都有 $\mathcal A\cap S\ne\{0\}$

*证明*：设 $\mathcal A\cap S=0$。定义 $\Lambda_{\mathcal A}(\ell N):=\ell AN$（$\ell\in V_{\mathcal A}:=\{\ell:\ell N,\ell AN\in\mathcal A\}$）。
**良定义**：若 $\ell_1N=\ell_2N$，则 $(\ell_1-\ell_2)AN=(\ell_1-\ell_2)R_0\in S$，又在 $\mathcal A$ 里，故 $=0$ ✓。
于是 $\Lambda_{\mathcal A}:\mathcal A\to\mathcal A$ 线性，且 $F=M\Lambda_{\mathcal A}$。
它在 $\mathbb{C}$ 上有特征对 $(\lambda_0,v)$，$v\in\mathcal A=\operatorname{im}M$，故
$\operatorname{rank}(\lambda_0M-F)\le\rho-1<\rho$，$(b)$ 败。$\blacksquare$

> 这条已用 **Lean 4** 形式化（`WellDefined`、`EigenRankDrop`、`RankDrop`、`RowFamily` 四个模块，`lake build` 零错误）。

### 3.2 维数恒等式（在 (L-1) 下）

令 $V_{\mathcal A}=\{\ell:\ell N\in\mathcal A,\ \ell AN\in\mathcal A\}$，条件

$$(\mathrm{L\text{-}1}):\quad \dim V_{\mathcal A}=n-2(d-\rho) .$$

则

$$\dim\{\ell N:\ell\in V_{\mathcal A}\}=2\rho-d+p-|\mathcal A\cap S| .$$

**推论**（在 (L-1) 下）：$\rho\ge d-p+|\mathcal A\cap S|\ge d-p+1$。

### 3.3 ⚠️ 关键等价：(L-1) $\iff$ 饱和

对 **admissible** 的 $\mathcal A$（即 $\mathcal A A'\subseteq\mathcal A+S$，这是 lift 的必要条件）：

$$(\mathrm{L\text{-}1})\iff\mathcal A+S=\mathbb{R}^d .$$

*（"$\Leftarrow$"已证；"$\Rightarrow$"即 Gap 1。）* 数值：53 个 admissible 组，0 违反。

$$\Longrightarrow\ \textbf{所以不能走"先证 (L-1)、再得下界"的路——那是循环的}$$

(L-1)、下界、饱和，**三者是同一件事**。

### 3.4 其它工具

- $S':=\{kR_0:\ kN=0\}=S$（构造：$\ell:=x-xN(N^{\mathsf T}N)^{-1}N^{\mathsf T}$ 给出 $\ell N=0,\ \ell AN=xR_0$）；
- admissible 在 $\dim\mathcal A=d+1-p,\ |\mathcal A\cap S|=1$ 时**自动**（因 $\dim(\mathcal A+S)=d$）；
- 若 $w\perp\mathcal A+S$，则自动有 $w\perp\mathcal A$、$w\perp S$、$w\perp\mathcal A\mathcal A'$、$Mw=0$、$M(A'w)=0$。

---

## 4. 为什么它难（三个结构性障碍）

### 4.1 多值性：$\Lambda_{\mathcal A}$ 只在 $\mathcal A\cap S=0$ 时单值

T2 的证明**完全依赖** $\mathcal A\cap S=0$ 带来的单值性。当 $\mathcal A\cap S\ne0$ 时，
$\ell N\mapsto\ell AN$ 的多值歧义恰好落在 $L:=\mathcal A\cap S$ 里——**这个多值性正是 $(b)$ 能成立的原因**。

$$\Longrightarrow\ \text{Gap 1 相当于说}:\quad \textbf{"多值性只要不是 1 维（$\rho=1$）或 0 维，就救不活 }(b)\text{"}$$

而"1 维多值性"正是 P7 的情形。**这个二分法目前没有证明。**

### 4.2 不能用 (L-1) 绕道

由 §3.3，(L-1) 与饱和等价。所以任何"先建立 (L-1) 再推下界"的策略都是循环。

### 4.3 极值性不唯一

"最小 admissible 子空间"不唯一：$\mathcal A_t=\operatorname{span}\{\alpha_0,\beta_0\}+L(t)$，$t\in\mathbb{P}^{p-1}$，
**整族都可 lift**（75/75 验证）。所以"取最小的那个"这种论证没有目标。

### 4.4 维数计数不够

$$\dim(\mathcal A+S)=\rho+p-|\mathcal A\cap S| .$$

T2 只给 $|\mathcal A\cap S|\ge1$，于是 $\dim(\mathcal A+S)\ge\rho+p-|\mathcal A\cap S|$——**与 $d$ 无必然关系**。
要 $\dim=d$ 需要 $|\mathcal A\cap S|=\rho+p-d$，即 $|\mathcal A\cap S|$ **恰好取到下界**——这是一个等式条件，不是不等式。

---

### 4.5 Gap 1 的**作用范围**（不是所有 $\rho$ 都可能有非饱和解）

由 $\dim(\mathcal A+S)=\rho+p-|\mathcal A\cap S|$ 与 T2（$|\mathcal A\cap S|\ge1$）：

$$\mathcal A+S\ne\mathbb{R}^d\ \Longrightarrow\ \rho+p-1<d\ \Longrightarrow\ \boxed{\ 2\le\rho\le d-p\ }$$

$$\textbf{所以 Gap 1 的实质内容是：}\quad \text{不存在}\ 2\le\rho\le d-p\ \text{的 lift}$$

**这解释了 $\rho=d+1-p$ 为什么是"自然"的**：它是 $\rho\le d-p$ 之外的第一个值。
若 Gap 1 成立，$\rho\ge d-p+1$ 就直接得到，不需要任何 (L-1)。

**特例 $d=p+2$**：唯一可能的非饱和 $\rho$ 是 $\rho=2$，此时 $\mathcal A$ 必为 2 维且 $|\mathcal A\cap S|=1$（故 $\dim(\mathcal A+S)=3<d$）。
数值检验（6 个 $\beta_0\not\parallel\alpha_0$ 实例）：
- $\mathcal A=\operatorname{span}\{\alpha_0,\beta_0\}$ 时 $|\mathcal A\cap S|=0$ ⟹ 违反 T2 ⟹ **必然不可 lift** ✓（$q{=}3,4$ 均不可）
- 这**不是**有效的反例搜索，因为该 $\mathcal A$ 已违反 T2

$$\Longrightarrow\ \textbf{有效的攻击面}：\ \mathcal A\ \text{取}\ 2\ \text{维、含}\ \alpha_0,\beta_0\text{、且与}\ S\ \text{交成 1 维}$$
### 4.6 ⭐ $p=1$ 时 Gap 1 归结为一个**可检验条件**（2026-10-22）

**适用范围**：$p=1$ **且 $d=3$**（即 $d=p+2$；此时 $\rho\le d-p=2$，所以 $\rho=2$ 是唯一的非饱和候选）。
（$d\ge4$ 时 $\rho=3$ 等也可能非饱和，族更大，另行处理。）

**结构**：$p=1$ 时 $S=\operatorname{span}\{r\}$ 是一维，且 $S\subseteq\mathcal A$（因 $|\mathcal A\cap S|=1$）。
于是 "含 $\alpha_0,\beta_0$、$\dim=2$、$|\mathcal A\cap S|=1$" 的 $\mathcal A$ **唯一**：

$$\boxed{\ \mathcal A=\operatorname{span}\{\alpha_0,\ r\}\ }$$

（$\beta_0\parallel\alpha_0$ 时已含 $\beta_0$ ✓；若 $\beta_0\not\parallel\alpha_0$ 则需 $\dim=3$，故 $p=1,d=3$ 的非饱和情形只有这一个候选。）

**admissibility（lift 的必要条件）化简为一个条件**：$\mathcal A A'\subseteq\mathcal A+S=\mathcal A$，即 $\mathcal A$ 是 $A'$-不变子空间。逐项：

$$\alpha_0A'=c\alpha_0-L_0R_0\in\operatorname{span}\{\alpha_0\}\subseteq\mathcal A\quad(\text{恒真，因}\ L_0R_0\in S\subseteq\mathcal A)$$
$$\boxed{\ rA'\in\operatorname{span}\{\alpha_0,\,r\}\ }$$

**结论**：

$$\text{若}\ rA'\notin\operatorname{span}\{\alpha_0,r\}\ \Longrightarrow\ \mathcal A\ \text{不 admissible}\ \Longrightarrow\ \textbf{不存在任何 lift（}\rho=2\text{）}$$

**这是无搜索的证明**（只用一个必要条件），不是数值证据。

**数值**（$p{=}1$、$c142$ 构造的 10 个 $\beta_0\parallel\alpha_0$ 实例）：

| 检验 | 结果 |
|---|---|
| $rA'\in\operatorname{span}\{\alpha_0,r\}$ | **0/10**（全部否）|
| 该 $\mathcal A$ 可 lift（$q{=}3,4$，搜索）| **0/8** |

$$\Longrightarrow\ \textbf{这 10 个实例的 Gap 1 由 admissibility 直接成立（不需要 (b) 的任何分析）}$$

**剩下要研究的是一族薄集**：

$$\mathcal R:=\{(A,C,L_0):\ rA'\in\operatorname{span}\{\alpha_0,r\}\}\qquad(\text{余维 }1\ \text{的条件})$$

在这族里 admissibility **不**排除候选，必须用 $(b)$。**这是 $p=1,d=3$ 时 Gap 1 的精确剩余。**

**$\mathcal R$ 是薄的**：等价地，$r$ 在 $A'$ 下的 **Krylov 维数 $=2$**（而不是 $3$）。
数值诊断（$c142$ 的 8 个实例）：Krylov 维数序列全为 $1,2,3,3,\dots$ ⟹ **Krylov 维数 $=3$** ⟹ **全都不在 $\mathcal R$ 里** ✓

$$\Longrightarrow\ \text{随机的 }(A,C)\ \text{几乎总给 Krylov 维数 }d\implies \text{admissibility 障碍总成立}$$

**要测 $\mathcal R$ 必须专门构造**（让 $r$ 的 Krylov 维数恰为 2），而这需要控制 $r=\operatorname{row}(AN-NA')$ 的生成元——
目前没有现成的构造法。**这是下一步的明确任务。**

---

### 4.7 一般 $p,d$：障碍是 **admissibility**，不是 $(b)$

$p=1,d=3$ 的机制（§4.6）抽象出来是：

$$\text{非饱和的}\ \mathcal A\ \text{要 admissible}\iff\mathcal A A'\subseteq\mathcal A+S$$

而**非饱和**时 $\mathcal A+S\subsetneq\mathbb{R}^d$ 是**真子空间**，所以 admissibility 是一条**实质约束**（不像饱和时自动成立）。

**一般情形的候选**：$\mathcal A\supseteq\operatorname{span}\{\alpha_0,\beta_0\}$、$|\mathcal A\cap S|=t\ge1$、$\rho=\dim\mathcal A$。admissibility 逐项是

$$\alpha_0A'\in\mathcal A+S\ (\textbf{恒真，因}\ \beta_0=\alpha_0A'+L_0R_0\parallel\alpha_0)$$
$$\beta_0A'\in\mathcal A+S\ ?\qquad S A'\subseteq\mathcal A+S\ ?$$

**关键观察**：$SA'\subseteq\mathcal A+S$ 是**最难**的那条（$\mathcal A$ 只含 $S$ 的 $t$ 维部分，而 $SA'$ 有 $p$ 维）。
$p=1,d=3$ 时它退化成"$rA'\in\operatorname{span}\{\alpha_0,r\}$"，数值上 **10/10 失败** ✓。

$$\boxed{\ \textbf{猜想（Gap 1 的"不变性版"）}:\quad \mathcal A\ \text{admissible}\ \wedge\ \mathcal A\cap S\ne0\ \Longrightarrow\ \dim(\mathcal A+S)=d\ }$$

$$\text{等价}:\quad \rho+p-t\ge d\iff\rho\ge d-p+t\quad(t=|\mathcal A\cap S|)$$

**这个形式的优点**：它**完全不提 $(b)$**——若成立，Gap 1 就是纯几何的（几乎不变子空间的维数下界），
不需要任何谱分析、也不需要 (L-1)。**这正是 Karcanias–Vafiadis 那套工具的适用形式。**

**难点**：$SA'\subseteq\mathcal A+S$ 要求 $\mathcal A$ 含 $S$ 在 $A'$ 下的"足够多"像，而 $\mathcal A$ 只含 $S$ 的 $t$ 维。
$t=1$ 时 $\mathcal A$ 几乎不含 $S$ 的方向——这是 $p=1$ 时障碍强的直观原因。
一般 $p$ 时 $t$ 可以大（最多 $p$），需要 $t$ 与 $p$ 的权衡。

**已知**：$t=p$（即 $S\subseteq\mathcal A$）时 $\mathcal A+S=\mathcal A$，admissibility 退化为 $A'$-不变性；此时若要非饱和，需要 $\mathcal A$ 是**真**的 $A'$-不变子空间且含 $S$ —— 而 $A'$ 在 $S$ 上一般不可对角化/不保持 $S$，所以仍难。

#### ⚠️ 这个猜想**不是**显然成立的（2026-10-22 尝试证明时发现）

- **若 $A'=0$**（即 $N^{\mathsf T}AN=0$），则 $\mathcal A A'=0\subseteq\mathcal A+S$ 对**任何** $\mathcal A$ 成立 ⟹ admissibility **自动** ⟹ 猜想会假；
- **$p=0$**（$S=0$）时猜想也假——但那时 **T2 直接排除任何 lift**（$\mathcal A\cap S=0$），所以该情形是**空的**；
- 所以猜想**只对 $p\ge1$ 且 $A'\ne0$ 有意义**；而"$A'=0$ 且 $p\ge1$"（需要 $AN\ne0$ 但 $N^{\mathsf T}AN=0$，同时 $K=\ker[C;CA]$）我**没有构造出来**。

**数值支持**（$p{=}2,d{=}4$）：构造 $\mathcal A=\operatorname{span}\{l,u\}$（$l\subseteq S$、$u$ 随机）共 **499** 个候选，**admissible 的 0 个** ✓

$$\Longrightarrow\ \text{正确表述应为}:\quad \text{admissible}\ \wedge\ \textbf{liftable}\ \wedge\ \mathcal A\cap S\ne0\ \Longrightarrow\ \text{饱和}$$

即 **admissibility 单独不够，必须与 liftability 联手**；$A'=0$ 时前一半退化，剩下的全压在 $(b)$ 上。
这是 §4.1（多值性）之外的**第二个障碍**。

### 4.8 多值映射的**商形式**（T2 的自然延伸，2026-10-22）

T2 的证明依赖"$\mathcal A\cap S=0$ ⟹ 单值"。多值时：若 $\ell_1N=\ell_2N$（$\ell_i\in V_{\mathcal A}$），则

$$(\ell_1-\ell_2)AN=(\ell_1-\ell_2)R_0\in S\ \ \text{且}\ \ \in\mathcal A\ \Longrightarrow\ (\ell_1-\ell_2)AN\in\mathcal A\cap S=L$$

**所以多值映射 $\Lambda_{\mathcal A}:\mathcal A\rightsquigarrow\mathcal A$ 的歧义落在 $L$ 里，从而**

$$\boxed{\ \bar\Lambda:=\pi\circ\Lambda:\ \mathcal A/L\to\mathcal A/L\quad(\pi:\mathcal A\to\mathcal A/L)\ \textbf{是良定义的线性映射}\ }$$

（$\dim(\mathcal A/L)=\rho-t$，$t=|\mathcal A\cap S|$。）

#### 由此得到的 $(b)$ 的**等价刻画**

因为 $F=M\Lambda+l\,c^{\mathsf T}$，

$$\operatorname{row}(\lambda M-F)=(\lambda I-\Lambda)(\mathcal A)+\langle l\rangle,\qquad \dim(\lambda I-\Lambda)(\mathcal A)=\rho-\dim\ker(\lambda I-\Lambda)$$

$$\Longrightarrow\ (b)\iff\boxed{\ \Lambda\ \text{的所有特征值都\textbf{单}（重数 1）},\ \text{且}\ l\notin(\lambda_iI-\Lambda)(\mathcal A)\ \text{对每个}\ \lambda_i\ }$$

**理由**：若某特征值重数 $\ge2$，则 $\dim(\lambda I-\Lambda)(\mathcal A)\le\rho-2$，加一个 $\langle l\rangle$ 也到不了 $\rho$ ✗。

#### 商算子的作用

$$\ker(\lambda I-\bar\Lambda)=\{m\in\mathcal A:\ (\lambda I-\Lambda)m\in L\}\ \supseteq\ \ker(\lambda I-\Lambda)$$

$$\textbf{若}\ \lambda\ \text{是}\ \bar\Lambda\ \text{的特征值}\ \Longrightarrow\ (\lambda I-\Lambda)(\mathcal A)+L\ne\mathcal A\ \Longrightarrow\ (\lambda I-\Lambda)(\mathcal A)\ne\mathcal A\ \Longrightarrow\ \lambda\ \text{也是}\ \Lambda\ \text{的特征值}$$

**所以 $\bar\Lambda$ 的谱 $\subseteq\Lambda$ 的谱**，且由 $(b)$ 两者都**单** ✓（数值：$\operatorname{charpoly}(\bar\Lambda)$ 是 2 次，常数项 $\ne0$，见三个实例）。

$$\Longrightarrow\ \textbf{商形式没有给出矛盾};\ \text{它只是把}\ (b)\ \text{重述成"谱单 + }l\ \text{避超平面"}$$

**这就是 T2 延伸的极限**：T2 用"单值"造出一个算子再取特征值；
多值时算子只存在于商上，而商上的谱**不提供新的约束**（$\lambda$ 仍可以是 $\Lambda$ 的单特征值）。
## 5. 试过的思路（含失败原因）

| # | 想法 | 为什么看似可行 | 失败在哪 |
|---|---|---|---|
| 1 | 在 $\lambda=c$ 处降秩（$c$ 由 $\beta_0=c\alpha_0$ 定义）| 那时第一行贡献 $0$，秩掉 1 | 只在 $\beta_0\parallel\alpha_0$ 时存在这样的 $c$；一般不存在。且我一度把该行的值写错，浪费一轮 |
| 2 | 预设 $\Lambda_{\mathcal A}$ 幂零 | 幂零 ⟹ 特征值全 0 ⟹ 在 $\lambda=0$ 处降秩 | 实测真实解的 $\Lambda_{\mathcal A}$ **满秩**（3/3）|
| 3 | 假设 $\Lambda_{\mathcal A}$ 的特征多项式有固定形状 | 若固定，可算 | 10 个 lift 的特征多项式**互不相同**；它不是不变量 |
| 4 | 用 $w\perp\mathcal A+S$ 做"投影压缩" | 有现成的降维工具（Willems 的 almost invariance 约化）| 只能推出 $w\perp\mathcal A$、$w\perp S$、$Mw=0$ 等**若干正交关系**，无法构造出单行的 $\ell$ |
| 5 | 取"最小 admissible 的 $\mathcal A$" | 极值性可能强制结构 | $\mathcal A$ **不唯一**（§4.3），没有目标 |
| 6 | 用"自界（self-bounded）+ Frobenius 伴随形" | 伴随形 ⟹ 循环性平凡 | 实测该算法（$\mathcal Z_{k+1}=\mathcal Z_k+(A'\mathcal Z_k\cap(S+\mathcal Z_k))$）给出 **$\dim\mathcal Z_\infty=d$（全空间）**，不是我们要的 $\dim=d+1-p$ |
| 7 | 纯维数计数 | 便宜 | §4.4：得到的是不等式，不是等式 |

**共同点**：所有失败都因为**缺少一个把 $(L,\Lambda)$ 与 $w$ 变成单行 $\ell$ 的构造**。

---

### 5.1 ⚠️ 枚举时必须先检查的**两条必要条件**（我自己踩过两次）

在枚举/构造候选 $\mathcal A$ 时，以下两条**必须先查**，否则"不可 lift"是平凡的、不构成证据：

$$\textbf{(N1)}\quad \operatorname{span}\{\alpha_0,\beta_0\}\subseteq\mathcal A\qquad(\text{否则第一行的 } (a)\ \text{就失败})$$
$$\textbf{(N2)}\quad \mathcal A\cap S\ne\{0\}\qquad(\text{T2：否则必败})$$

**我犯过的两次错**：
1. 取 $\mathcal A=\operatorname{span}\{\alpha_0,\beta_0\}$（$\beta_0\not\parallel\alpha_0$，$d=p+2$）——它满足 (N1) 但**违反 (N2)** ⟹ "不可 lift"是 T2 的推论，**不是** Gap 1 的证据；
2. 取 $\mathcal A=\operatorname{span}\{\alpha_0,L\}$（$L\subseteq S$）而不检查 $\beta_0\in\mathcal A$——**违反 (N1)** ⟹ 同样平凡。

$$\Longrightarrow\ \text{有效的 }\rho=2\ \text{非饱和候选，只有在}\ \beta_0\parallel\alpha_0\ \text{时才存在（此时}\ \mathcal A=\operatorname{span}\{\alpha_0,L\}\ \text{自动含}\ \beta_0\text{）}$$

**而这类实例需要专门构造**（随机的 $A,C$ 几乎总给 $\beta_0\not\parallel\alpha_0$）。
## 6. 数值证据（精确有理数，无浮点）

| 搜索族 | 规模 | 结果 |
|---|---|---|
| $\mathcal A\supseteq S$ 的平面（$|\mathcal A\cap S|=p$）| 25 个 $\mathcal A$ × 3 个 $q$ | 全部**不可行** |
| $\mathcal A=S$（构造 $\alpha_0,\beta_0\in S$ 的实例）| 2 个实例 | 全部**不可行** |
| P7 假实例上的系统扫描（$\mathcal A=S$、$S+e$、$\operatorname{span}\{\alpha_0,\beta_0\}$）| 12 次 | 全部**不可行** |
| $\mathcal A\cap S=0$、$\rho=d-p$（**注意**：此构型其实饱和，见 §3.3）| 800 次 | 全部不可行（**本就不该**可行，见 T2）|

$$\textbf{从未见过一个}\ \mathcal A+S\ne\mathbb{R}^d\ \text{的 lift（除}\ \rho=1\ \text{的 P7 分支外）}$$

**这类证据的价值与局限**：它排除了"容易找到的反例"，但**不能**证明不存在——
而且按 §4.3 的经验，非饱和构型可能是**余维很高的薄集**，采样本来就会错过。

---

## 7. 文献状态

| 文献 | 与本题的关系 |
|---|---|
| **Willems (1981)**, *Almost invariant subspaces*, IEEE TAC 26(1) 235–252 | almost invariance 的经典来源；**最小维数未解决** |
| **Karcanias & Vafiadis (1993)**, *On the cover problems of geometric theory*, Kybernetika 29(6) 547–562 | 我们的问题正是其 **partial + almost cover** 问题；原文明确把"最小维数解"列为 open："of particular interest are the problems of determining the **minimal dimension** subspace solutions" |
| **Basile & Marro (1992)** | self-bounded 理论给的是**按包含**的格论极小元，与本题**按维数**极小时不同（§5 第 6 行的实测也印证）|
| Fernando–Trinh–Jennings (2010), IEEE TAC | **最小阶功能观测器的设计**（存在性 + 构造），**不是复杂度**；不能直接当作本问题的解 |

$$\boxed{\ \text{我没有找到任何能核实地对应 Gap 1 的定理}\ }$$

---

## 8. 瓶颈的确切位置

要证 Gap 1，需要下面**三者之一**：

**(a) 一个构造**：给定解 $(L,\Lambda)$ 与 $0\ne w\perp\mathcal A+S$，造出 $\ell$ 使
$$\ell N\parallel\alpha_0,\qquad \ell AN\parallel\alpha_0 .$$

> ⚠️ **注意这只在 $\beta_0\parallel\alpha_0$ 时有意义**：因为 $\rho=1$ 的解需要 $L_0\in\mathcal S$（见 §1 的 P7 定义）。
> 若 $\beta_0\not\parallel\alpha_0$，P7 为假，Gap 1 的结论就变成"**该实例根本没有非饱和的 lift**"——
> 这也是一种（更强的）需要证明的形态。
已知 $w$ 满足：$w\perp\mathcal A$、$w\perp S$、$w\perp\mathcal A\mathcal A'$、$Lw=0$、$M(A'w)=0$。
**问题**：这些正交关系不足以确定 $\ell$；缺的是"从 $w$ 到 $\ell$ 的映射"。

**(b) 一个反例**：某个 $(A,C,L_0)$ 与解 $(L,\Lambda)$，满足 $(5a)\wedge(5b)$、$\rho\ge2$、$\mathcal A+S\ne\mathbb{R}^d$。

**(c) 一个结构性理由**：例如"Gap 1 $\iff$ 某个已知的公开问题 X"——那样论文可以引用 X 的状态。

---

## 9. ⭐ 我要什么形式的回答

### 形式 ①：一个证明（最有价值）

请给出**关键一步**，并标明哪些是标准事实（引理名/出处）、哪些是新论证。特别想知道：

- 如果用 $w$（$w\perp\mathcal A+S$），**怎么用**？
- 如果用商空间 $\mathcal A/L$（$L=\mathcal A\cap S$），**诱导映射是什么**、为什么它迫使 $\rho=1$？
- 如果用多值性，**多值歧义的维数与 $\rho$ 的关系**是什么？

### 形式 ②：一个反例（同样有价值）

给整数矩阵即可，规模 $n\le10$、$p\le3$、$d\le5$：

```
A (n×n 整数), C (p×n 整数), L0 (r×n 整数), 以及一个解 L (q×n)
```

**我一秒判定** $(5a)\wedge(5b)$、$\rho$、$\dim(\mathcal A+S)$（精确有理数，无浮点）。
反例的判据：$(5a)\wedge(5b)$ 成立、$\rho\ge2$、$\dim(\mathcal A+S)<d$。

### 形式 ③：一个归约

指出 Gap 1 **等价于**某个我有机会查到的公开问题（给出名字/出处）。
即使它仍是 open，这个归约也能让论文写出"本问题等价于 X，而 X 自 19XX 年起 open"。

### 形式 ④：指出我的等价链有错

如果你认为 §3.3 的等价（(L-1) $\iff$ 饱和）或 §3.1 的 T2 有错，请直接指出——
**那样整个路线的形态会改变**，这同样是有价值的回答。

### 不要给的

- "直觉上高度成立"、"generic 情形下测度为零"——这两类回答我收到过，**不能推进**。
  理由：$L_0$ 是**输入**（不能靠它的 genericity）；"坏集测度为零"预设了它不等于全集，而那正是要证的。

---

## 10. 我能提供的验证

| 量 | 能否精确判定 |
|---|---|
| $(5a)$、$(5b)$（**原矩阵形式**，不经过约化）| ✅ 精确有理数 |
| $\rho=\operatorname{rank}(LN)$、$\dim(\mathcal A+S)$、$|\mathcal A\cap S|$ | ✅ |
| 维数恒等式、$S'=S$、admissibility | ✅ |
| 任何你提出的候选判据 / 构造 | ✅ 可当场核对 |

**所以：任何可检验的陈述（定义、定理、条件、反例）我都能立刻核对并回报结果。**

---

## 11. 速查表

| 符号 | 含义 |
|---|---|
| $d$ | $\dim\ker[C;CA]$ |
| $p$ | $\operatorname{rank}(R_0)=\dim S$ |
| $A'$ | $A$ 在 $K=\ker[C;CA]$ 上的诱导映射 |
| $S$ | $\operatorname{row}(R_0)$（"扰动"子空间）|
| $\alpha_0,\beta_0$ | $L_0N,\ L_0AN$ |
| $\rho,\mathcal A$ | $\operatorname{rank}(LN),\ \operatorname{row}(LN)$ |
| admissible | $\mathcal A A'\subseteq\mathcal A+S$（lift 的必要条件）|
| (L-1) | $\dim V_{\mathcal A}=n-2(d-\rho)$ |
| P7 | $L_0\in\mathcal S$（即 $\beta_0\parallel\alpha_0$）**且** $\dim\operatorname{im}(\mathcal S\to\mathbb{R}^2)=2$；$\iff\exists\,\rho=1$ 的解 |

| 待证 | 一句话 |
|---|---|
| **Gap 1** | 非饱和 lift ⟹ 可压到一行（P7）|
| 等价说法 | P7 假 ⟹ 所有 liftable 的 $\mathcal A$ 都饱和 |
| 若成立 | 配合上界 ⟹ $q_{\min}=\max(3,d+2-p)$ ⟹ q1 为假 |
