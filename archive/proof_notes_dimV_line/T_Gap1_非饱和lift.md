# Gap 1：非饱和的 lift 是否必可压到一行？

> **这份文档是自足的**——不需要读本项目其它文件。目的是把一个问题准确地描述出来，
> 便于请教。文中每个定义都给出，每条"已知"都标注是**证明**还是**数值验证**。
>
> 日期：2026-10-22 ｜ 相关文件：[proof/S](S_维数下界定理_2026-10-21.md)

---

## 0. 一句话版

$$\textbf{问题}:\quad \text{若线性系统 }(5a)\wedge(5b)\text{ 有一个解、且它的"行空间"}\ \mathcal A\ \text{与某个固定子空间}\ S\ \text{之和不是全空间，}\ $$
$$\text{那么是否一定存在一个}\ \textbf{行数更少}（\text{秩}=1）\ \text{的解？}$$

---

## 1. 背景：问题的来源（3 分钟）

给定 $A\in\mathbb{R}^{n\times n}$、$C\in\mathbb{R}^{p\times n}$、$L_0\in\mathbb{R}^{r\times n}$。要找
$R\in\mathbb{R}^{k\times n}$ 使 $L:=\begin{bmatrix}L_0\\R\end{bmatrix}$ 满足

$$(\mathrm{5a})\quad \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],$$
$$(\mathrm{5b})\quad \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\qquad\forall\lambda\in\mathbb{C}.$$

**问**：最小的 $k$ 是多少？它是不是多项式时间可算？

**约化**（把所有东西搬到 $d$ 维空间）：令 $K=\ker[C;CA]$（维数 $d$），取基 $N\in\mathbb{R}^{n\times d}$，令

$$A':=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN\in\mathbb{R}^{d\times d},\qquad
R_0:=AN-NA'\in\mathbb{R}^{n\times d},$$
$$S:=\operatorname{row}(R_0)\subseteq\mathbb{R}^d,\qquad p:=\operatorname{rank}(R_0)=\dim S .$$

记 $\alpha_0:=L_0N\in\mathbb{R}^d$、$\beta_0:=L_0AN=\alpha_0A'+L_0R_0$。对候选的 $L$（$q$ 行）令

$$M:=LN\in\mathbb{R}^{q\times d},\qquad F:=LAN\in\mathbb{R}^{q\times d},\qquad
\rho:=\operatorname{rank}M,\qquad \mathcal A:=\operatorname{row}(M)\subseteq\mathbb{R}^d .$$

则（项目已证）

$$(\mathrm{5a})\iff \exists\,\Lambda\in\mathbb{R}^{q\times q}:\ F=\Lambda M,$$
$$(\mathrm{5b})\iff \operatorname{rank}(\lambda M-F)=\rho\quad\forall\lambda\in\mathbb{C}.$$

**可行性**（$\exists R$）已完全解决：$\alpha_0\in V$，其中 $V:=\langle\operatorname{row}R_0\rangle_{A'}$
是 $\operatorname{row}(R_0)$ 在 $A'$ 下的闭包。所以下面只关心**最小化**。

---

## 2. 已知的两条定理（这两条我已有证明）

**定理 A（维数恒等式）**。设 $\mathcal A=\operatorname{row}(M)$ 是一个**解**的行空间，令

$$V_{\mathcal A}:=\{\ell\in\mathbb{R}^n:\ \ell N\in\mathcal A,\ \ell AN\in\mathcal A\}\quad(\text{一个线性子空间}).$$

若 $\dim V_{\mathcal A}=n-2(d-\rho)$（记为条件 **(L-1)**），则

$$\dim\{\ell N:\ \ell\in V_{\mathcal A}\}=2\rho-d+p-|\mathcal A\cap S| .$$

（理由是：$\ell\mapsto\ell N$ 在 $V_{\mathcal A}$ 上的核等于
$\{k\in\operatorname{row}[C;CA]:kR_0\in\mathcal A\}$，其维数为 $(n-d-p)+|\mathcal A\cap S|$，
用到 $S'=\{kR_0:kN=0\}=S$，这一步我证了。）

**推论**：（在 (L-1) 下）任何解满足

$$\rho\ \ge\ d-p+|\mathcal A\cap S|\ \ge\ d-p+1 .$$

**定理 B（交非空）**。任何解都有 $\mathcal A\cap S\ne0$。

*证明提要*：若 $\mathcal A\cap S=0$，则 $\ell N\mapsto\ell AN$ 在 $\mathcal A$ 上**单值**
（核方向 $(\ell_1-\ell_2)$ 满足 $(\ell_1-\ell_2)AN=(\ell_1-\ell_2)R_0\in S$，又在 $\mathcal A$ 里 ⟹ $=0$）。
于是得到一个线性映射 $\Lambda_{\mathcal A}:\mathcal A\to\mathcal A$，且 $F=M\Lambda_{\mathcal A}$。
它在 $\mathbb{C}$ 上有特征对 $(\lambda_0,v)$，$v\in\mathcal A=\operatorname{im}M$，
故 $\operatorname{rank}(\lambda_0M-F)\le\rho-1<\rho$，$(b)$ 败。

---

## 3. Gap 1 的精确陈述

**(L-1) 与我要的界是等价的**。具体地：

$$\dim(\mathcal A+S)=\rho+p-|\mathcal A\cap S|\ \Longrightarrow\ \Big[\ (L\text{-}1)\iff \mathcal A+S=\mathbb{R}^d\ \Big]\qquad(\text{对 admissible 的 }\mathcal A)$$

其中 **admissible** 指 $\mathcal A A'\subseteq\mathcal A+S$（这是 lift 的必要条件：
$(a)$ 给出 $f_i=m_iA'+\ell_iR_0\in\mathcal A$）。"$\mathcal A+S=\mathbb{R}^d\Rightarrow(L\text{-}1)$"
这一向她已证；反向（即下面这条）是 Gap。

> ### 🎯 **Gap 1（要证或推翻的命题）**
>
> 设存在解 $(L,\Lambda)$，其行空间 $\mathcal A=\operatorname{row}(M)$，$\rho=\operatorname{rank}M\ge2$。
> 则
> $$\mathcal A+S=\mathbb{R}^d .$$
>
> 等价地：**若 $\mathcal A+S\ne\mathbb{R}^d$ 且存在解，则存在一个 $\rho=1$ 的解**
> （即 $\exists\ell$ 使 $\ell N\parallel\alpha_0$ 且 $\ell AN\parallel\alpha_0$——项目里叫 "P7"）。

**为什么它不平凡**：它**不是**说"$\mathcal A+S=\mathbb{R}^d$ 自动成立"——那是假的。
$\rho=1$ 的解（若存在）取 $\mathcal A=\operatorname{span}\{\alpha_0\}$，此时
$\dim(\mathcal A+S)\le 1+p\le d$，**可以严格小于 $d$**。所以命题的实际内容是：

$$\textbf{"非饱和的 lift 必可压到一行"}$$

---

## 4. 我知道的证据（数值，不是证明）

| 检验 | 规模 | 结果 |
|---|---|---|
| $\mathcal A\supseteq S$ 的平面（$|\mathcal A\cap S|=p$）| 25 个 $\mathcal A$ × 3 个 $q$ | 全部**不可行** |
| $\mathcal A=S$（构造 $\alpha_0,\beta_0\in S$）| 2 个实例 | 全部**不可行** |
| P7 假实例上的系统扫描（$\mathcal A=S$、$S+e$、$\operatorname{span}\{\alpha_0,\beta_0\}$）| 12 次 | 全部**不可行** |
| $\mathcal A\cap S=0$、$\rho=d-p$（此时 $\mathcal A+S=\mathbb{R}^d$，属饱和情形）| 800 次 | 全部不可行（且**本就不该**可行，见定理 B）|

$$\textbf{从未见过一个}\ \mathcal A+S\ne\mathbb{R}^d\ \text{的 lift（除 }\rho=1\text{ 的 P7 分支外）}$$

---

## 5. 我试过、但失败的路线

| 路线 | 为什么失败 |
|---|---|
| 在 $\lambda=c$（$c$ 由 $\beta_0=c\alpha_0$ 定义）处降秩 | 只在 $\beta_0\parallel\alpha_0$ 时有 $c$；且我一度把 $\lambda=c$ 的行写成 $f_i$ 而非 $\ell_i(AN-cN)$，错了两次 |
| 预设 $\Lambda_{\mathcal A}$ 是幂零的 | 实测真实解里 $\Lambda_{\mathcal A}$ **满秩**（3/3）|
| 猜 $\Lambda_{\mathcal A}$ 的特征多项式有固定形状 | 10 个 lift 的特征多项式**互不相同**（它不是不变量）|
| 用 $w\perp\mathcal A+S$ 做"投影压缩" | 没能把 $(\mathcal L,\Lambda,w)$ 变成一行的 lift；已知 $w\perp\mathcal A$、$w\perp S$、$w\perp\mathcal A\mathcal A'$、$Mw=0$、$M(A'w)=0$ |

**我认为的困难**：定理 B 的证明用到了"$\Lambda_{\mathcal A}$ 在 $\mathcal A$ 上单值"（因为 $\mathcal A\cap S=0$）。
而 $\mathcal A\cap S\ne0$ 时 $\Lambda_{\mathcal A}$ 只是**多值**（歧义落在 $\mathcal A\cap S$ 里），
多值性恰好是允许 $(b)$ 成立的原因。所以 Gap 1 相当于说：

$$\textbf{"多值性只要不是 1 维或 0 维，就不足以救活 (b)"}$$

而"1 维多值性"正是 $\rho=1$（P7）的情形。

---

## 6. 我要的答案形式

下面任一即可：

1. **一个证明**：从 $(\mathcal L,\Lambda)$ 与 $0\ne w\perp\mathcal A+S$ 出发，构造一个 $\rho=1$ 的解；
2. **一个反例**：显式的 $(A,C,L_0)$ 与一个解，其 $\mathcal A+S\ne\mathbb{R}^d$ 且 $\rho\ge2$；
3. 或者告诉我这个问题**已知**等价于某个标准问题（例如某个几乎不变子空间/几何控制里的最小维数问题），
   我再去查文献。

**最小的验证方式**：给一个 $n\le8$、$d\le5$ 的具体数值例子即可——我有精确有理数的检验脚本，
一秒钟就能判定 $(5a)\wedge(5b)$。

---

## 7. 与标准理论的联系

- $\mathcal A A'\subseteq\mathcal A+S$ 就是 **almost $A'$-invariance**（Willems 的 almost controlled
  invariant subspace，只是把 $\operatorname{im}B$ 换成了 $S$）；
- $p=\operatorname{rank}(R_0)$ 是"输出注入"的秩；
- 我要的东西是：**在"含 $\alpha_0,\beta_0$ 的 admissible 子空间"里，最小维数元素的维数**，
  并且它必须"$(b)$-liftable"。
- 我得到的最小维数是 $\max(2,\ d+1-p)$（8 个 $(p,d)$ 组合精确验证），
  而 Gap 1 就是它的**下界**那一半。

$$\text{如果 Gap 1 成立}\ \Longrightarrow\ q_{\min}=\max(3,\ d+2-p)\ \Longrightarrow\ q_{\min}\in\mathrm{P}\ \Longrightarrow\ \text{原命题（NP-hard）为假}$$

---

## 8. 复现

```bash
python scripts/core/c158_lower_bound_audit.py      # 定理 A（在 (L-1) 下）42/42
python scripts/core/c159_admissibility_equivalence.py  # (L-1) ⟺ 饱和，53 组 0 违反
```

两者都用**精确有理数**（不用浮点）。

---

## 9. 🆕 文献查证（2026-10-22）

**Karcanias & Vafiadis, _On the cover problems of geometric theory_, Kybernetika 29 (1993) 547–562**
（[dml.cz](https://dml.cz/handle/10338.dmlcz/125037)，全文已存 `lit/Karcanias_Vafiadis_1993_cover.pdf` 与 `.txt`）

他们的**标准 cover problem**：

$$\text{给定}\ J\subseteq W,\ \text{求所有}\ (A,B)\text{-不变子空间}\ V\ \text{使}\ J\subseteq V\subseteq W .$$

**我们的问题正是它的"partial + almost"版本**：

$$\underbrace{J=\operatorname{span}\{\alpha_0,\beta_0\}}_{\text{要覆盖}},\qquad
\underbrace{(A,B)\ \text{换成}\ (A',S)}_{\text{almost }A'\text{-invariant：}\mathcal A A'\subseteq\mathcal A+S},\qquad W=\mathbb{R}^d .$$

**他们的贡献与局限**：

| 他们做了 | 他们**没做** |
|---|---|
| 用**矩阵铅笔**（restricted pencil $sNV-NAV$）刻画 $(A,B)$-不变性 | **没有**给出"最小维数 cover"的公式 |
| 把 cover 问题化成 Kronecker 结构分配（KSAP） | 没有讨论最小解的**唯一性/lattice 结构**（全文 `lattice/unique/supremum` 各 0 次）|
| 给出 left regular / regular 情形的**参数化** | 他们的参数化是"解族"，不是"最小元" |

文中原话（引言后）：

> "of particular interest are the problems of determining the **minimal dimension** subspace solutions, when such solution exist."

$$\Longrightarrow\ \textbf{最小维数 cover 在他们那里也是\textbf{公开问题}}$$

**其它可查的**：
- Willems, *Almost invariant subspaces*（IEEE TAC 1981）——almost invariance 的经典来源；
- Jaffe & Karcanias（Int. J. Control 1981）——almost $(A,B)$-invariant 的矩阵铅笔刻画，但只处理 $\mathcal L=\mathrm{id}$（见项目 `pdf/reference/`）。

$$\boxed{\ \text{结论：Gap 1 落在一个\textbf{被承认但未解决}的问题类里；文献没现成答案}}$$