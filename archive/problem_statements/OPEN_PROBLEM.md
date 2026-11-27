# 一个最小维数问题：almost controlled invariant 子空间 + 铅笔正则性

**主题**：求最小的 $q$（行数）使条件 $(a)\wedge(b)$ 可满足 —— **多项式还是 NP-hard？**

**背景**：这是原文命题 q1 的真伪。「是否存在解」已证是多项式的（P1），故硬度（若存在）只能来自**最小化**。

> **状态**：已证 P1–P10；已排除 **13 条路线**（§7）；当前卡点见 §6。
> **74 处自我更正**已记录（其中 7 处是"已写进文档的结论"被自己推翻）。
> 严格区分「已证」/「已验证（数值）」/「已撤回」。

---

## §0 一句话

$$\text{给定}\ (A,C)\ \text{与固定首行}\ L_0，\text{求最小}\ q\ \text{与}\ \mathcal L\in\mathbb{R}^{q\times n}\ (\text{首行}=L_0)\ \text{使}\ (a)\wedge(b)。\quad\textbf{复杂度？}$$

---

## §1 记号

$A\in\mathbb{R}^{n\times n}$，$C\in\mathbb{R}^{p\times n}$，$d:=\dim\ker[C;CA]\ge1$。

$$K:=\ker\begin{pmatrix}C\\CA\end{pmatrix};\quad N\in\mathbb{R}^{n\times d}\ (\text{列基});\quad A':=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN;\quad R_0:=AN-NA'$$

**一行可验**：$N^{\mathsf T}R_0=0$（$NA'$ 是 $AN$ 在 $K$ 上的正交投影）。

$$S:=\operatorname{rowspace}(R_0)\subseteq\mathbb{R}^d;\qquad V:=\sum_{t\ge0}(A'^{\mathsf T})^t\operatorname{im}R_0^{\mathsf T};\qquad \mathrm{obs}:=\dim V$$

**三条关键恒等式**（反复使用）：
$$R_0=P_{K^\perp}(AN);\qquad \{\ell R_0:\ \ell\perp K\}=S\ \textbf{（满射）};\qquad \ell AN=(\ell N)A'+\ell R_0$$

**未知量**：$\mathcal L\in\mathbb{R}^{q\times n}$，首行固定为 $L_0$（$L_0N\ne0$）。

$$M:=\mathcal LN,\quad F:=\mathcal LAN,\quad \rho:=\operatorname{rank}M$$
$$(a)\ F=\Lambda M\ \text{对某}\ \Lambda;\qquad (b)\ \operatorname{rank}(\lambda M-F)=\rho\ \ \forall\lambda\in\mathbb{C}$$

$$\alpha_0:=L_0N,\qquad \beta_0:=L_0AN$$

---

## §2 已严格证明（每条附验证要点）

### P1 可行性判据（**两侧都已证**）—— 主结果
$$\boxed{\ \exists\mathcal L\ \text{满足}\ (a)\wedge(b)\iff\alpha_0\in V\ }$$
*必要性*：$(b)\iff\operatorname{im}M\cap\ker(\lambda I_q-\Lambda)=0\ \forall\lambda$（因 $\lambda M-F=(\lambda I_q-\Lambda)M$）；PBH 给 $(\Lambda^{\mathsf T},\ker M^{\mathsf T})$ 可控；用 $F^{\mathsf T}=A'^{\mathsf T}M^{\mathsf T}+R_0^{\mathsf T}\mathcal L^{\mathsf T}$ 归纳得 $\operatorname{im}M^{\mathsf T}\subseteq V$。
*充分性*：取 $A_0=I$、$A_1=A'+B$（$B$ 的行 $=\ell_iR_0$），用 $(A'^{\mathsf T},R_0^{\mathsf T})$ 的可控性配置 $\mathrm{charpoly}(A_1)$ 无实根。
$$\Longrightarrow\ \textbf{可行性判定}\in\mathrm{P}\ (O(n^3))$$

### P2 秩上界
$$(a)\wedge(b)\Longrightarrow\rho\le\mathrm{obs}$$

### P3 $\rho=0$
$$\rho=0\ \text{可行}\iff L_0N=0\ \wedge\ L_0AN=0$$

### P4 / P4b
$$q=1\wedge(a)\wedge(b)\Longrightarrow M=0\quad(\text{故}\ q_{\min}\ge2)$$
$$\boxed{\ (a)\wedge(b)\Longrightarrow\rho\le q-1\qquad(M\ \textbf{永不\textbf{满射}})}$$
*证明*：若 $\rho=q$，$M$ 满射；取 $\Lambda$ 的特征向量 $v\ne0$，$Mx=v$，则 $(\lambda_0M-F)x=0$ 而 $Mx\ne0$，(b) 败。□

### P5 $\Phi$-等价（**两侧已证**，验证 118/118）
$$\Phi(\mathcal A):=\{\ell N:\ \ell N\in\mathcal A,\ \ell AN\in\mathcal A\}\ \subseteq\ \mathcal A\quad(\textbf{收缩})$$
$$\boxed{\ \Phi(\mathcal A)=\mathcal A\iff\mathcal A A'\subseteq\mathcal A+S\ }$$
$$\text{（即：}\ \mathcal A\ \text{是}\ (A'^{\mathsf T},S^{\mathsf T})\text{-不变子空间，Wonham 意义）}$$
**任何解**的 $\mathcal A:=\operatorname{row}M$ 都满足它。

### P6 / P6b 两条必要条件

> 🔴 **2026-10-20 更正（第 75 处）：P6b 是<u>假</u>的。**
> 存在 $n{=}5,p{=}1,r{=}1$、$q{=}3$、$\rho{=}2$ 的实例，满足 H1–H3、$\mathcal A\mathcal A'\subseteq\mathcal A$、**(5a) 与 (5b) 都成立**。
> 见证与三套独立复核：`scripts/core/c140_p6b_counterexample.py`、[`proof/I_P6b_反例_2026-10-20.md`](proof/I_P6b_反例_2026-10-20.md)。
> **证明的错误**："取 lift $=0$" **不是一个可选的选择**——首行被 $L_0$ 钉死，$L_0R_0$ 一般 $\ne0$。
> 该论证只说明了"把 lift 取成 $0$ 的那**一个**解"会失败，不能推出所有解都失败。
> **后果**：§5 的条件 4（$\mathcal AA'\not\subseteq\mathcal A$）**不是必要条件**；§7 路线 5 与"极端 1"的解释失去依据。

$$\boxed{\ \mathcal N_{\mathcal A}:=\{\ell:\ell N=0,\ \ell AN\in\mathcal A\}=0\ \Longrightarrow\ (b)\ \text{必败}\ }$$
$$\text{"等价"形式：}\ \mathcal A\cap S=\{0\}\ \Longrightarrow\ (b)\ \text{必败}\quad(\text{⚠️ 见下注})$$
$$\boxed{\ \mathcal A A'\subseteq\mathcal A\ \Longrightarrow\ (b)\ \text{必败}\quad\text{❌ 已被反例推翻}\ }$$
*证明*：前者 $\Lambda_{\mathcal A}$ 单值（ℂ 上必有特征值）；后者（**已失效**）原说"取 lift $=0$，$A'|_{\mathcal A}$ 必有特征值"。

> ⚠️ **第二个小缺口**：$\mathcal N_{\mathcal A}=0$ 与 $\mathcal A\cap S=0$ 的"等价"只在
> $\ell\mapsto(\ell N,\ell R_0)$ **单射**时成立（一般 $n$ 与 $2d$ 无固定大小关系），
> 故"$\mathcal A\cap S=0\Rightarrow(b)$ 必败"的这条推理链也**不是**无条件的。

### P7 $\rho\le1$ 的完整多项式判据（验证 148/148 与 185/185）
$$\mathcal S:=\{\ell:\ \ell N\in\operatorname{span}\{\alpha_0\},\ \ell AN\in\operatorname{span}\{\alpha_0\}\}$$
$$\rho\le1\ \text{可达}\iff L_0\in\mathcal S\ \wedge\ \dim\operatorname{im}\big(\mathcal S\to\mathbb{R}^2,\ell\mapsto(u,w)\big)=2$$

### P8 固定 $q$ 的决策 $\in\exists\mathbb{R}$
$$(b)\iff\operatorname{rank}\big[H\ \ \Lambda^{\mathsf T}H\ \ \cdots\ \ (\Lambda^{\mathsf T})^{q-1}H\big]=q,\quad M^{\mathsf T}H=0,\ \operatorname{rank}H=q-\rho$$
（或用 Bézout：$(b)\iff\gcd_{\mathbb{C}[\lambda]}\{D_I\}=1$，$D_I$ 为 $\rho\times\rho$ 子式。）
$$\Longrightarrow\ D_k:=\{q\le k\ \text{可行}\}\in\exists\mathbb{R}\qquad(\mathrm{NP}\subseteq\exists\mathbb{R}\subseteq\mathrm{PSPACE})$$

### P9 固定首行给出的额外必要条件（外部指出，验证 320/320）
$$(a)\wedge(b)\Longrightarrow\operatorname{row}F=\operatorname{row}M\ \Longrightarrow\ \boxed{\ \beta_0:=L_0AN\in\mathcal A\ }$$
*理由*：$F=\Lambda M\Rightarrow\operatorname{row}F\subseteq\operatorname{row}M$；$(b)$ 在 $\lambda=0$ 给 $\operatorname{rank}F=\rho$，故相等。□
$$\text{它比 P5 强}：\ \beta_0=\alpha_0A'+L_0R_0\ \text{固定了}\ L_0R_0\ \text{这个具体的}\ s_0\in S$$

### P10 正确的 $(b)$ 失败条件
$$\boxed{\ (b)\ \text{失败}\iff\exists\lambda_0:\ \dim\ker\big((\lambda_0M-F)^{\mathsf T}\big)\ \ge\ q-\rho+1\ }$$
$$\text{（只要求一个左零向量是不够的 —— }\rho<q\ \text{时二者不同）}$$

---

## §3 一个反例（说明**没有** $\mathrm{obs}$ 的简单闭式）

$$n{=}7,\ p{=}2,\ d{=}3$$
$$A=\begin{pmatrix}0&1&0&0&0&0&0\\0&0&1&0&0&0&0\\0&0&0&0&0&0&0\\1&0&0&0&0&0&0\\0&1&0&0&0&0&0\\0&0&0&1&0&0&0\\0&0&0&0&1&0&0\end{pmatrix},\quad
C=\begin{pmatrix}0&0&0&0&0&1&0\\0&0&0&0&0&0&1\end{pmatrix}$$
$$L_0=(1,0,0,0,-1,0,0),\qquad
\mathcal L=\begin{pmatrix}1&0&0&0&-1&0&0\\0&0&0&1&0&0&0\end{pmatrix}$$
$$M=\begin{pmatrix}1&0&0\\0&0&0\end{pmatrix},\quad F=\begin{pmatrix}0&0&0\\1&0&0\end{pmatrix},\quad\rho=1$$
$$(a)\ \Lambda=\begin{pmatrix}0&0\\1&0\end{pmatrix};\quad (b)\ \operatorname{rank}(\lambda M-F)=1\ \forall\lambda\ \checkmark\qquad\textbf{但}\ \mathrm{obs}=3$$
$$\Longrightarrow\ \rho<\mathrm{obs}\ \text{可发生}\ \Longrightarrow\ \textbf{无}\ q_{\min}=\mathrm{obs}+1-r\ \text{型闭式}$$

---

## §4 我要问的

$$\boxed{\ \textbf{问题}：\ q_{\min}\ \text{的计算是多项式可算，还是 NP-hard？}\ }$$

**已知**：$\rho\le1$ 时多项式可判（P7）；$\rho\le q-1$（P4b）；$q_{\min}\le\mathrm{obs}+1$（P1 的构造）。

---

## §5 问题的精确重述（**最可攻的形式**）

$$\boxed{\ \rho_{\min}=\min\{\dim\mathcal A:\ \alpha_0\in\mathcal A,\ \beta_0\in\mathcal A,\ \mathcal AA'\subseteq\mathcal A+S,\ \mathcal A\cap S\ne0,\ \mathcal AA'\not\subseteq\mathcal A,\ (b)\text{-liftable}\}\ }$$

**条件表**：

| # | 条件 | 性质 | 状态 |
|---|---|---|---|
| 1 | $\alpha_0\in\mathcal A$ | 线性 | ✓ |
| 1b | $\beta_0\in\mathcal A$ | 线性（**P9**）| ✓ |
| 2 | $\mathcal AA'\subseteq\mathcal A+S$ | 双线性（子簇）| ✓ |
| 3 | $\mathcal A\cap S\ne0$ | 秩不等式 | ✓ |
| 4 | $\mathcal AA'\not\subseteq\mathcal A$ | 秩不等式 | ✓ |
| **5** | **$(b)$-liftable** | **黑箱** | **✗** |

**已化简 1**（lift 的自由部分 $\sigma'$ 可消去）：$\sigma'$ 的可行集是**仿射子空间** $\Sigma$；$(b)$ 是 **Zariski-开**条件（$\gcd\{D_I\}=1$）⟹ 「某 $\sigma'$ 满足」$\iff$「generic $\sigma'$ 满足」⟹ **对固定 $\mathcal A$ 只需一次 $\gcd$ 检查（poly）**。

**已化简 2**（商空间分解）：
$$\dim\mathcal A=\dim\overline{\mathcal A}+\dim(\mathcal A\cap S)\quad(\overline{\mathcal A}\subseteq\mathbb{R}^d/S)\qquad\Longrightarrow\ \rho\ge1+\dim\overline{\mathcal A}$$

$$\Longrightarrow\ \textbf{搜索变量只剩}\ \mathcal A\in\mathrm{Gr}(\rho,d)\qquad(\text{Grassmann})$$

---

## §6 我确切卡在哪一步

### 6.1 卡点（一句话）

$$\text{给定满足条件 1–4 的}\ \mathcal A，\text{是否存在 lift 使}\ (b)\ \text{成立？}\qquad\textbf{没有}\ \mathcal A\ \text{的有限秩刻画}$$

### 6.2 为什么难（三条已经量化的障碍）

**(i) 格论路线不存在**（我自己测出，$d{=}4$，3726 对样本）：
$$\{\mathcal A:\ \mathcal AA'\subseteq\mathcal A+S\}\ \textbf{不对交封闭}\qquad(\mathbf{1873/3726=50.3\%}\ \text{反例})$$
显式反例：
$$U=\begin{pmatrix}1&0&0&0\\0&1&0&1\\0&0&1&0\end{pmatrix},\ V=\begin{pmatrix}0&1&0&0\\0&0&1&-1\end{pmatrix}\ \text{均 admissible};\qquad U\cap V=(0,1,-1,1)\ \textbf{不 admissible}$$
$$\Longrightarrow\ \text{infimum（格论最小元）}\textbf{未必存在}\ \Longrightarrow\ \text{无"最小元"算法可用}$$

**(ii) 两个自然极端都失败**：

| 极端 | 结果 |
|---|---|
| 最小 admissible（$A'$-闭包）| 是 $A'$-不变的 ⟹ **P6b ⟹ (b) 必败**（数值 $0/77$）|
| 最小 admissible $+\langle s\rangle$（$s\in S$）| **不 admissible**（$0/86$）|

**(iii) 已排除 13 条路线**（§7）。

---

## §7 已试过并失败的路线（**13 条，请勿重复**）

| # | 路线 | 失败方式 |
|---|---|---|
| 1 | $\Phi$-闭包迭代 $\bigcup\Phi^i$ | $\Phi$ 是**收缩**的 ⟹ 迭代恒等于 $\operatorname{span}\{\alpha_0\}$ ⟹ 平凡 |
| 2 | 并集 $\Phi^\infty(\operatorname{span}\{\alpha_0\}+\operatorname{row}R_0)$ | $0/75$；$\Lambda$ 变单值 ⟹ (b) 必败 |
| 3 | 典原子空间（$\operatorname{row}R_0$、$W$、$W\cap\operatorname{row}R_0$）| 维数不够；$\rho\ge2$ 必败 |
| 4 | Segre 形式 $\mathbb{P}(\Lambda_{\mathcal A})\cap\Sigma=\emptyset$ | 混同**关系**与**映射** |
| 5 | $A'$-循环子空间 | $0/77$；$A'$-不变 ⟹ **P6b** |
| 6 | **单向量扩张 $\mathcal A_*+\langle s\rangle$** | $0/86$；**不 admissible** |
| 7 | 穷尽 $\beta\in\mathbb{P}^1$ | $0/38$；但有限采样**不能证明** |
| 8 | 单调性（"(b) 在大 $\mathcal A$ 上更难"）| **与 P1 逻辑冲突** |
| 9 | 各种闭式（$\rho=d$、$\rho=\mathrm{obs}$、$c\le1$、$q=\mathrm{obs}+1-r$）| 全部有反例 |
| 10 | Willems 最小 kernel representation | $\mathcal L$ **左乘**、$R$ **右乘**，方向相反 |
| 11 | Conte–Perdon "small $(A,B)$-invariant submodule" | 他们的 "smallest" 是**格论最小元**，不是最小维数 |
| 12 | **格论（infimum）路线** | 族**不对交封闭**（50% 反例）⟹ infimum 未必存在 |
| 13 | "存在左特征方向"作为 (b) 的刻画 | 只给**必要条件**（$\rho<q$ 时不等价）|

---

## §8 文献（查过 / 读过 / 读不到）

| 文献 | 内容 | 与我的关系 |
|---|---|---|
| **Trentelman–Stoortvogel–Hautus**, *Control Theory for Linear Systems*, Ch. 5–8 | 受控不变 / conditioned invariant；$\mathcal V^*,\mathcal S^*$ | 我的条件 = $(A'^{\mathsf T},S^{\mathsf T})$-不变性 |
| **Wonham**, *Linear Multivariable Control* | 不变子空间格 | 对**和**封闭（sup 存在），**不对交封闭** |
| **Willems**, *Almost invariant subspaces: An approach to high gain feedback design — Part I: Almost controlled invariant subspaces*, IEEE TAC AC-26 (1981) | $\mathcal VA\subseteq\mathcal V+\operatorname{im}B$ 的完整理论 | ⭐ **我的条件就是 almost controlled invariant** |
| **Willems**, *Part II: Almost conditionally invariant subspaces*, IEEE TAC AC-27 (1982) | 对偶概念 | conditioned 型有 infimum（我这型没有）|
| **Malabre**, *Almost invariant subspaces, transmission and infinite zeros: a lattice interpretation* | 这些子空间的**格结构** | 我需要的"最小元"不在其中 |
| **Conte–Perdon**, *Small (A,B)-invariant subspaces in DDP* | "特定格中最小 $(A,B)$-不变子模"，存在性由温和假设保证；**递归几何程序** | 不同问题（格论最小元 vs 最小维数）|
| **Jaffe–Karcanias**, *Int. J. Control* 33 (1981) 51–93 | restriction pencil | 只处理 $\mathcal L=\mathrm{id}$ |
| **Berger–Trunk–Winkler**, LAA 488 (2016) | 线性关系与 Kronecker 形 | 对应 P6 的机理 |
| **Schaefer–Cardinal–Miltzow**, arXiv:2407.18006 | $\exists\mathbb{R}$ 综述 | P8 的复杂度上界 |
| 核范数松弛方向（Recht–Fazel–Parrilo 等）| min-rank 一般 NP-hard | 我的约束**不是**线性约束，不能直接归约 |

**获取情况**：IEEE / ScienceDirect / zbMATH / Semantic Scholar 全部付费或被墙 ✗；仅取得书目信息。

---

## §9 数值验证（规模 + 结果，**不是证明**）

| 检验 | 规模 | 结果 |
|---|---|---|
| P5 等价 | 118 | 118/118 ✓ |
| P7 的 $\rho\le1$ 判据 | 148 + 185 | 全通过 ✓ |
| P4b 的 $q\ge\rho+1$ | 5 | 5/5 ✓ |
| P9 的 $\operatorname{row}F=\operatorname{row}M$ | 320 | 320/320 ✓ |
| 交封闭性 | 3726 对 | **1873 反例** ⟹ 不封闭 |
| $A'$-循环构造 | 77 | 0 成功（P6b 解释）|
| 单向量扩张 | 86 | 0 成功（不 admissible）|
| 并集构造 | 75 | 0 成功（P6 解释）|
| 穷尽 $\beta\in\mathbb{P}^1$ | 38 | 0 救回（采样不足，不能证明）|

### 9.1 🆕 2026-10-20 一轮的独立验证（详见 [`proof/`](proof/)）

| 检验 | 规模 | 结果 | 文档 |
|---|---|---|---|
| P1 必要性 / A19 / P4b（**原始 4 块与原始铅笔**上判，独立实现）| 618 个真实解 | **0 违规** | [G](proof/G_独立复核_2026-10-20.md) |
| P1 在 $\mathrm{obs}=1$ 上与穷举对比 | 14 实例 | **14/14**（2 True + 12 False）| 同上 |
| $\rho_{\min}$ 公式（$\min_r\dim\Phi^\infty(\mathrm{span}\{\alpha_0,r\})$）| $d=2,3,4$ 共 103 例 | **0 反例**；含 $\rho=1$ 与 $\rho=2$ 两侧 | [P](proof/P_rho_min公式重验_2026-10-20.md) |
| $\operatorname{rank}(R_0)=\min(p,d)$ | 6 组 × 120 例 | 未见反例（**未证**）| [L](proof/L_小q族_2026-10-20.md) §8 |
| 分层：$q_{\min}=2$（P7）/ $3$（≈6%）/ $4=\mathrm{obs}+1$（326/326）| $n{=}5,p{=}1$ | 见文档 | [O](proof/O_qmin分层_2026-10-20.md) |

### 9.2 🔴 P6b 被反例推翻（2026-10-20，见 P6 的更正块）

$$n{=}5,\ p{=}1,\ q{=}3,\ d{=}3,\ \rho{=}2:\quad H1\text{–}H3\ \checkmark,\ \mathcal AA'\subseteq\mathcal A\ \checkmark,\ (5a)\ \checkmark,\ (5b)\ \checkmark$$

$$\Longrightarrow\ \text{条件 4（}\mathcal AA'\not\subseteq\mathcal A\text{）}\textbf{不是必要条件}\ ;\quad \text{§7 路线 5 的解释失效}$$


---

## §10 我最想要的（按优先级）

1. **$q_{\min}$ 是多项式还是 NP-hard**。
2. 若多项式：**关键引理** —— 大概是"条件 5 等价于某个**有限秩条件**"（在 $\mathcal A$ 上，或在 $(\mathcal A,\mathcal A',S,\alpha_0,\beta_0)$ 上）。
3. 若 NP-hard：**归约**。注意约束：$N^{\mathsf T}R_0=0$、$\operatorname{row}R_0\subseteq\operatorname{row}N$、$S$ 的满射性 —— 不能把 $A',R_0$ 当作独立任意矩阵。
4. **辅助问题**：almost controlled invariant 子空间族中，"含给定子空间的**最小维数**元素"是否有已知结果？（**不是**格论最小元 —— 那个不存在。）

---

## §11 附：原问题（q1）

$$\textbf{q1}：\text{"找到行数最小的}\ R\ \text{使}\ [L_0;R]\ \text{满足}\ (5a)\wedge(5b)\ \text{是 NP-hard"}$$
$$\text{原始假设 H1–H4（我证明了 H4 未被使用）};\qquad (5a),(5b)\ \text{即本文档的}\ (a),(b)$$
$$\text{若}\ q_{\min}\in\mathrm{P}\Longrightarrow\textbf{q1 为假};\qquad \text{若}\ q_{\min}\ \text{NP-hard}\Longrightarrow\textbf{q1 为真}$$

---

---

## §12 当前状态（2026-10-22）

### 12.0 🔴🔴🔴 **2026-10-22：闭式被一个验证过的反例推翻**

$$\boxed{\ \textbf{反例（精确验证）}:\quad (p,d)=(1,3)\ \text{的实例，}q_{\min}=3\ne4=\max(3,d+2-p)\ }$$

- 证书：[`COUNTEREXAMPLE_2026-10-22.md`](COUNTEREXAMPLE_2026-10-22.md)、[`lit/counterexample_candidate.json`](lit/counterexample_candidate.json)；
- 该实例还有一个 **$\rho=2$ 的非饱和 lift**（$\dim(\mathcal A+S)=2<d=3$）⟹
  **Gap 1 的两种表述都被推翻** ⟹ $\rho\ge d-p+1$ **假**；
- 该实例是 $c142$ 型（$\beta_0\parallel\alpha_0$），落在薄集上：此前的 8 个数据点都在一般位置。

$$\Longrightarrow\ \textbf{§12.1 的闭式}\ \textbf{不是定理，且在某些实例上为假};\ \text{§12.3 的两个 Gap 也随之作废（被反例取代）}$$

### 12.1 目标：一个闭式（🔴 见 §12.0：已被反例推翻）

$$\boxed{\ q_{\min}=\begin{cases}2 & \text{P7 成立（项目已证的多项式判据）}\\[2pt] \max\big(3,\ d+2-p\big) & \text{否则}\end{cases} }$$

$$\textbf{若成立}\ \Longrightarrow\ q_{\min}\in\mathrm{P}\ \Longrightarrow\ \textbf{原命题 q1（NP-hard）为假}$$

该闭式有 **8 个 $(p,d)$ 组合**的**精确**验证（$(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,3),(3,4)$），
**下界已证**，**上界有显式构造**；剩下的是两个技术缺口（§12.3）。

### 12.2 它从哪来

$$\text{可行性已完全解决（P1）};\quad \text{最小化}=\underbrace{\text{下界}}_{\rho\ge d+1-p}+\underbrace{\text{上界}}_{\exists\ \text{lift 且}\ \rho=d+1-p}$$

其中 $\rho=\operatorname{rank}(LN)$，$p=\dim S$，$d=\dim\ker[C;CA]$（记号见 §1）。

### 12.3 两个缺口（**都可独立提问**）

| 缺口 | 命题 | 状态 | 自足文档 |
|---|---|---|---|
| **Gap 1**（下界）| $\mathcal A+S\ne\mathbb{R}^d$ 且存在 lift $\Longrightarrow$ 存在 $\rho=1$ 的 lift（即 P7）| ❌ 未证；所有非饱和构型搜索 **0 命中** | [proof/T](proof/T_Gap1_非饱和lift.md) |
| **Gap 2**（上界）| 构造出的 $l$ 是 $\Lambda^{\mathsf T}$ 的**循环向量**（与分解无关，U §4.2a；等价于 almost-invariant 闭包满，U §4.4）| 🟡 构造已显式、**51+ 测试点全过**；循环性未证 | [proof/U](proof/U_Gap2_上界存在性.md) |

$$\textbf{Gap 1}\ \text{与下界等价（不是"先证 (L-1)"的循环）};\qquad
\textbf{Gap 2}\ \text{等价于"}\ l\ \text{是}\ \Lambda^{\mathsf T}\ \text{的循环向量"$$

两份文档都是**自足**的（不依赖本文件其余部分），可直接转发给专家。
🆕 **对外提问请用**：[问题陈述_最小增广行数_2026-10-22.md](问题陈述_最小增广行数_2026-10-22.md)（把两者合并、并写明"要什么形式的回答"）。

**已收到的两份外部反馈**（2026-10-22）：
- feedback 1：Gap 2 的 PBH 框架（与我独立推导一致）；Gap 1 仍 open；
- feedback 2：**状态反馈不变性** ⟹ 循环性与分解无关（已采纳，U §4.2a）；并确认 **Gap 1 是 open**；
  其建议的"最小自界 + 伴随形"路线经检验**不适用**（该算法给出全空间，U §4.3）。

### 12.4 已确立的结果（按可信度）

| 级别 | 内容 | 文档 / 验证 |
|---|---|---|
| **已证** | 可行性判据 $\alpha_0\in V\iff\exists R$（两侧）| §2 P1；`audit_independent`（618 解 0 违规）|
| **已证** | $\rho\le\mathrm{obs}$；$\rho\ge1$；$d=2$ 时 $\rho_{\min}\in\{1,2\}$ | §2 P2/P4b；[proof/Q](proof/Q_d2_定理_2026-10-20.md) |
| **已证** | $\rho\le1$ 的多项式判据（P7）| §2 P7（148+185 验证）|
| **已证** | 维数恒等式 $\dim\{\ell N:\ell\in V_{\mathcal A}\}=2\rho-d+p-\|\mathcal A\cap S\|$ | [proof/S](proof/S_维数下界定理_2026-10-21.md) §2 |
| **已证** | 任何解都有 $\|\mathcal A\cap S\|\ge1$（$\Rightarrow\rho\ge d-p+1$）| S §5.1d |
| **已证** | $S'=S$（即 $\operatorname{row}[C;CA]\to S$ 满射）| S §1.2 |
| **已证（条件性）** | 跳层定理：$p=1$、$\beta_0\parallel\alpha_0$ 时 $q_{\min}\in\{2,\mathrm{obs}+1\}$ | [proof/R](proof/R_跳层定理_2026-10-20.md) |
| **反驳** | **P6b 是假的**（显式反例，三套实现复核）| [proof/I](proof/I_P6b_反例_2026-10-20.md) |
| **数值（未证）** | 闭式本身：8 个 $(p,d)$ 组合 | S §7.9 |
| **形式化** | T2 的 (i)(iii)(iv)、行族形式、§1.5 的代数核心 | `scripts/lean/*.lean`（5 个模块 build 通过）|

### 12.5 复现（全部精确有理数）

```bash
python scripts/core/c158_lower_bound_audit.py           # 恒等式 42/42、(L-1) 42/42、(L-2) 18/18
python scripts/core/c159_admissibility_equivalence.py   # (L-1) ⟺ 饱和：53 组 0 违反
python scripts/core/c160_gap2_construction.py           # Gap 2 的构造：(a)∧(b) 12/12
python scripts/core/audit_independent.py                # P1/P2/P4b 独立复核（618 解）
```

**两条硬规矩**（各用一次事故换来）：
1. $(b)$ 只能用 **$\rho$ 阶子式的 gcd** 判定——随机 $\lambda$ 采样会给出**假阳性**；
2. 构造 lift 的线性系统必须**同时**解 $\ell N\in\mathcal A$ 与 $\ell AN\in\mathcal A$——漏一条会让整个代数关系崩掉。

### 12.6 过程记录

会话日志（方向、任务清单、禁区、总账）已移到 [`history/SESSION_LOG_2026-10-21.md`](history/SESSION_LOG_2026-10-21.md)。
**结论以本文件与 `proof/` 为准。**