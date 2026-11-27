# 10 — 三篇 PDF 的前提假设清单（命题 q 的真正基础）

> 你提示得对：**命题 q 是建立在论文的假设之上的**，而我在前面几轮的分析中长期漏掉了其中最重要的一条。
> 本文系统列出三篇 PDF 的**全部前提**，并指出哪些被我漏掉、漏掉后会造成什么后果。

---

## 1. P1（arXiv:2609.33615）的假设

出处：`p1.txt:95–107`（§II Preliminaries）

### (P1-a) $C$ 与 $L$ 满行秩

> "Without loss of generality, **$C$ and $L$ are assumed to have full row rank**: dependent measurements provide no additional information, while dependent prescribed functionals can be recovered from estimates of a maximal independent subset."（`p1.txt:95–98`）

$$\boxed{\mathrm{rank}(C)=p,\qquad \mathrm{rank}(L)=r}$$

### (P1-b) 联合满秩

> "We further assume
> $$\mathrm{rank}\begin{bmatrix}L\\C\end{bmatrix}=r+p,$$
> since any component of $L$ in $\mathrm{row}(C)$ is directly available from the measured output and requires no observer dynamics."（`p1.txt:98–106`）

$$\boxed{\mathrm{rank}\begin{bmatrix}L_0\\C\end{bmatrix}=r+p}$$

**含义**：$L_0$ 中已落在 $\mathrm{row}(C)$ 的成分被**排除**（它们不需观测器动力学）。
这是 P2 里说的"components of L already contained in row(C) are excluded"（`p2.txt:87–88`）。

### (P1-c) **功能可观性**（★ 我长期漏掉的那条）

> "**Throughout, the triple $(A,C,L)$ is assumed functional observable**, so that $z(t)=Lx(t)$ is reconstructible from the available input and output."（`p1.txt:107–109`）

P1 给出**两种等价定义**：

**定义 1（重构形式）**：存在有限 $T>0$，使 $z(0)=Lx(0)$ 可由 $y(t),u(t)$（$0\le t\le T$）唯一确定。

**定义 2（增广形式）**：
$$(\text{A})\qquad \mathrm{rank}\begin{bmatrix}LA\\L\\CA\\C\end{bmatrix}=\mathrm{rank}\begin{bmatrix}L\\CA\\C\end{bmatrix}
\quad\Longleftrightarrow\quad \mathrm{row}(LA)\subseteq\mathrm{row}(L,C,CA)$$
且**存在有限维增广** $R$ 使 $\mathcal L=[L;R]$ 满足 (A)。

> ⚠️ **关键澄清（我此前混淆的地方）**：
> P1 **用 (A) 来定义功能可观性**（Definition 2）。所以 (A) 与功能可观性在 P1 的框架下是**同一件事**，
> 而不是"(A) 是比功能可观性更强的东西"。
> 这与 P2 的秩形式 $\mathrm{rank}[O_C;O_L]=\mathrm{rank}(O_C)=n_0$（`p2.txt:96`）等价。

**推论**：功能可观性 **等价于** "存在某个增广使 (A) 成立"。于是命题 q（求最小增广）**天然在功能可观域内**——
若 (A) 对 $L=L_0$ 都不成立，那么**不存在**任何增广使其成立（因为 $L_0$ 的行必须保留），此时 $\nu_{\min}$ **无定义**。

### (P1-d) 最小阶问题的形式化（`p1.txt:187`）

$$\nu_{\min}:=\min_{\mathcal L}\ \mathrm{rank}\,\mathcal L\quad\text{s.t.}\quad \mathrm{row}(L)\subseteq\mathrm{row}(\mathcal L),\ (\text{A}),\ (\text{S})$$

**注意约束** $\mathrm{row}(L)\subseteq\mathrm{row}(\mathcal L)$：**$L_0$ 的每一行都必须保留**。这正是 P2 `p2.txt:107` 的 $\mathrm{row}(L)\subseteq\mathrm{row}\begin{bmatrix}C\\ \mathcal L\end{bmatrix}$。

---

## 2. P2（arXiv:2609.37992）的假设

出处：`p2.txt:81–108`

### (P2-a) 冗余行移除

> "Throughout, **redundant measured outputs and redundant functional rows are removed** so that
> $$\mathrm{rank}(C)=p,\qquad \mathrm{rank}\begin{bmatrix}C\\L\end{bmatrix}=p+r .$$"（`p2.txt:81–85`）

与 (P1-a)(P1-b) 一致。

> "Thus, **components of $L$ already contained in $\mathrm{row}(C)$ are excluded** from the functional estimation problem."（`p2.txt:87–88`）

### (P2-b) 保留原始 $n$ 维状态空间

> "The original $n$-dimensional state-space representation is **retained throughout**; no separate $n_0$-dimensional state realization is introduced."（`p2.txt:99–101`）

### (P2-c) 可重构性约束

> "The prescribed functional $Lx(t)$ is required to be **recoverable** from $Lx(t)$ and the measured output $Cx(t)$. Equivalently,
> $$\mathrm{row}(L)\subseteq\mathrm{row}\begin{bmatrix}C\\ \mathcal L\end{bmatrix},$$
> In rank form: $\mathrm{rank}\begin{bmatrix}C\\ \mathcal L\end{bmatrix}=\mathrm{rank}\begin{bmatrix}C\\L\end{bmatrix}$."（`p2.txt:103–114`）

### (P2-d) 功能可观性（秩形式）

> "Functional observability is characterized by [26]
> $$\mathrm{rank}\begin{bmatrix}O_C\\O_L\end{bmatrix}=\mathrm{rank}(O_C)=n_0 .$$"（`p2.txt:93–97`）

$$\boxed{\mathrm{row}(O_L)\subseteq\mathrm{row}(O_C)\iff Z\subseteq\mathrm{row}(O_C),\quad Z:=\mathrm{row}(O_{L_0})+\mathrm{row}(O_C)}$$

---

## 3. P3（IEEE TAC 2010）的假设

出处：`p3.txt:96–110`（§III Problem Statement）

### (P3-a) 全行秩与联合满秩

> "Without loss of generality, it is assumed that
> $$\mathrm{rank}(C)=p,\quad \mathrm{rank}(L_0)=r,\quad \mathrm{rank}\begin{bmatrix}C\\L_0\end{bmatrix}=(p+r).$$"

与 (P1-a)(P1-b)(P2-a) 完全一致。

### (P3-b) 无稳定不可控状态

> "It is assumed without loss of generality that **there are no stable uncontrollable states** in the system because the asymptotic value of uncontrollable but stable states are zero, those states play no part in an asymptotic estimation of $z_0(t)$, and if present, those states can be removed from the system and the function $z_0(t)$."（`p3.txt:96–104`）

### (P3-c) $s$ 的取值范围（(5b) 的量词）

> "In [16], Condition 2 considers $s\in\mathbb C,\ \Re(s)\ge0$; however if we consider $s\in\mathbb C$ instead of $s\in\mathbb C,\Re(s)\ge0$ in Condition 2, then the observer can have **arbitrary stable poles** as opposed to just stable poles."（`p3.txt:127–133`）

(5b) 取 s ∈ C (任意极点配置)  或   Re(s) ≥ 0 (仅渐近收敛)

---

## 4. 假设汇总表

| 编号 | 假设 | 出处 | 我此前是否漏掉 |
|---|---|---|---|
| H1 | $\mathrm{rank}(C)=p$（$C$ 满行秩） | P1:95, P2:81, P3:96 | ❌ 未漏 |
| H2 | $\mathrm{rank}(L_0)=r$（$L_0$ 满行秩） | P1:95, P2:82, P3:96 | ❌ 未漏 |
| H3 | $\mathrm{rank}[L_0;C]=r+p$（联合满秩） | P1:98, P2:85, P3:96 | ⚠️ 曾漏（后来补上） |
| **H4** | **功能可观性** $\mathrm{row}(O_{L_0})\subseteq\mathrm{row}(O_C)$，即 $Z\subseteq\mathrm{row}(O_C)$ | **P1:107, P2:93** | **❌❌ 长期漏掉** |
| H5 | $\mathrm{row}(L_0)\subseteq\mathrm{row}(\mathcal L)$（$L_0$ 行必须保留） | P1:187, P2:107 | ❌ 未漏 |
| H6 | 无稳定不可控状态 | P3:96 | 未用 |
| H7 | $s\in\mathbb C$ 或 $\Re(s)\ge0$ | P3:127 | ❌ 未漏 |

---

## 5. 漏掉 H4 造成的后果（关键）

### 5.1 我此前构造的"反例"其实无效

例：$A=\mathrm{diag}(1,2)$，$C=[1,0]$，$L_0=[e_1]$。

| 检查 | 结果 |
|---|---|
| $\mathrm{row}(O_C)=\mathrm{row}([1,0;1,0])$ | $\mathrm{span}(e_1)$ |
| $O_{L_0}=[e_1;e_1]$ | $\mathrm{span}(e_1)$ |
| $Z=\mathrm{row}(O_{L_0})+\mathrm{row}(O_C)$ | $\mathrm{span}(e_1)$ |
| $Z\subseteq\mathrm{row}(O_C)$？ | **✓ 成立** |
| (A) 对 $L=L_0$ 成立？ | $LA=e_1,\ \mathrm{row}(L_0,C,CA)=\mathrm{span}(e_1)$，**✓ 成立** |
| 但 (5b) 呢？ | 在 $s=2$ 处失败（$P(2)=[1,0]\ne0$） |

**结论**：此例**满足 H4**，但仍**不存在**满足 (A)∧(S) 的增广 —— 即 $\nu_{\min}$ **无定义**！

> **这是比"漏掉假设"更严重的发现**：即使 `q.txt` 在此基础上加上 H4，$\nu_{\min}$ **仍然可能不存在**。
> 换言之，**q.txt 的命题本身可能是一个空命题**（对某些系统，最小行数 $R$ 根本不存在）。

### 5.2 那 P1/P2 的 $\nu_{\min}\le n_0-p$ 是怎么回事？

P2 `p2.txt:102` 说："The resulting theory characterizes the functional-observer order spectrum **between $q_0$ and $n_0-p$**"，
且 `p2.txt:51` 给出 $r\le q_0\le\nu_{\min}\le n_0-p$。

这说明 P2 断言 $\nu_{\min}\le n_0-p$ **总有解**（在 H1–H4 下）。但我的例子满足 H1–H4 却似乎无解——
**矛盾**。可能的原因：

1. 我的例子**违反了某条我尚未识别的假设**（例如 (P3-b) 无稳定不可控状态，或 $A$ 与 $C$ 的某种关系）；
2. 或 $\nu_{\min}$ 的定义中 $\mathcal L$ **不必包含 $L_0$ 的行**，而是形如 P2 的 $\mathrm{row}(L)\subseteq\mathrm{row}[C;\mathcal L]$（更宽松）；
3. 或我对 (5b) 的检验出现了错误（尽管用精确有理算术复核过）。

> ⚠️ **这一矛盾尚未解决**，是当前最需要澄清的问题。若原因 3，则我前面所有"证伪"推理都需重审；
> 若原因 1，则**还有一条我没找到的假设**。

---

## 6. 对命题 q 的重新定位

基于以上，`q.txt` 的命题应当被**重新表述**为：

> **命题 q（修正后的完整表述）.**
> 给定功能可观的系统 $(A,C,L_0)$，满足 H1–H3（可能还需 H6 等），
> 求最小的 $k$，使存在 $R\in\mathbb R^{k\times n}$ 且 $L=[L_0;R]$（或更宽松地 $\mathrm{row}(L_0)\subseteq\mathrm{row}(L)$）
> 同时满足 (A) 与 (S)。**问：这个计算问题是否 NP-hard？**

**当前状态**：

| 结论 | 依据 |
|---|---|
| (A) 是子空间包含条件，只依赖 $\mathrm{row}(L)$ | ✅ 引理 1 |
| (5b) 只依赖 $\mathrm{row}(L)$ | ✅ 引理 2 |
| (S) 的核形式 $P(s)=(sI-T_\mathcal{R})H$，$\mathrm{im}(H)\cong\mathcal{R}/(\mathcal{R}\cap\mathrm{row}(C))$ | ✅ 引理 3/4 |
| (S) 是 Zariski 开条件 | ✅ |
| **H4 功能可观性是必需前提** | ✅ 本轮确认 |
| **$\nu_{\min}$ 的存在性** | ❌ **我的例子与之矛盾，未解决** |
| **$\Sigma_d$ 非空性判定** | ❌ 未证 |
| 去随机化 | ❌ 未做 |

---

## 7. 下一步（按优先级）

1. **解决 §5.2 的矛盾**（最高优先）：
   - 用 P1/P2 的**算例**（P1 `p1.txt:1224` 给的 $8\times8$ 例子，$(\eta_1,\eta_2)=(3,1)$）
     逐条核对我对 (5b) 的实现；
   - 检查是否还有**未识别的假设**（尤其 (P3-b) 无稳定不可控状态的作用）。
2. 若矛盾解决且 $\nu_{\min}$ 确有定义，则继续判定 $\Sigma_d$ 的非空性与复杂度。
3. 若矛盾指向"$\nu_{\min}$ 可能不存在"，则命题 q 需**加上存在性假设**才成立，
   或者在"存在"的那些系统上讨论复杂度。

---

## 8. 参考文献

1. T. Fernando. arXiv:2609.33615 —— §II 假设（H1–H5）
2. T. Fernando. arXiv:2609.37992 —— §II 假设（H1–H4、可重构性）
3. T. L. Fernando, H. M. Trinh, L. Jennings. IEEE TAC **55**(5):1268–1273, 2010 —— §III 假设（H1–H3、H6、H7）
