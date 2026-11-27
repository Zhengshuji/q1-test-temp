# 组合形式与复杂度问题

> 目标：把最小行数问题写成纯组合形式，明确它是否是（或像）一个已知的 NP-hard 问题。
> 前置：[ATTACK_LOG](ATTACK_LOG.md) §D8–D14，[STATUS](STATUS.md)。

---

## 一、问题的干净形式

### 1.1 从原始数据到三个对象

给定 $(A, C, L_0)$（$A\in\mathbb R^{n\times n}$，$C\in\mathbb R^{p\times n}$，$L_0\in\mathbb R^{r\times n}$），定义

$$\mathcal J:=\operatorname{row}\begin{pmatrix}CA\\C\end{pmatrix}\subseteq\mathbb R^n\qquad(\dim\mathcal J\le 2p)$$

$$\mathcal K:=\operatorname{row}(L_0)\subseteq\mathbb R^n$$

### 1.2 核心观察

$$\text{条件 }(5a)\iff\operatorname{row}[\mathcal LA;\mathcal L;CA;C]=\operatorname{row}[\mathcal L;CA;C]\iff\boxed{\ \mathcal VA\subseteq\mathcal V+\mathcal J\ }$$

其中 $\mathcal V:=\operatorname{row}(\mathcal L)$。

**所以 $(5a)$ 只依赖 $\mathcal V$，不依赖 $\mathcal L$ 的具体选取。**

### 1.3 问题

$$\boxed{\ \textbf{MIN-ROWS}:\quad \min\dim\mathcal V\quad\text{s.t.}\quad \mathcal K\subseteq\mathcal V,\ \ \mathcal VA\subseteq\mathcal V+\mathcal J,\ \ \text{且铅笔无零点}\ }$$

其中"铅笔无零点"指

$$\operatorname{rank}\begin{pmatrix}\lambda L-LA\\CA\\C\end{pmatrix}=\operatorname{rank}\begin{pmatrix}L\\CA\\C\end{pmatrix}\qquad\forall\lambda\in\mathbb C$$

---

## 二、三个已定位的边界

| 对象 | 定义 | 性质 |
|---|---|---|
| $\mathcal V_{\min}^{\mathrm{ci}}$ | 最小 conditioned invariant 子空间 $\supseteq\mathcal K$ | 可多项式算出；**但不满足"无零点"** ✗ |
| $\mathcal V^{A}$ | 最小 $A$-不变子空间 $\supseteq\mathcal K$（$A$-不变包）| 可多项式算出；**总满足"无零点"** ✓，但太大 |
| $\mathcal V^\star$ | 所求（最小且无零点）| 在两者之间 |

$$\mathcal V_{\min}^{\mathrm{ci}}\ \subseteq\ \mathcal V^\star\ \subseteq\ \mathcal V^{A}$$

**数值**：$\mathcal V_{\min}^{\mathrm{ci}}$ 与 $q_{\min}$ 一致仅 5/52；$\mathcal V^A$ 仅 6/59。

---

## 三、复杂度问题

### 3.1 上界（容易）

$$\textbf{MIN-ROWS}\in\mathrm{NP}:\quad\text{给定}\ \mathcal V\ \text{的基，验证三条件都是多项式时间}$$

（$(5a)$ 是秩比较；"无零点"用子式 gcd。）

### 3.2 下界（未知）

$$\boxed{\ \text{不知道 MIN-ROWS 是多项式可解还是 NP-hard}}$$

### 3.3 归约目标（三个候选）

| 候选问题 | 为何相关 |
|---|---|
| **最小 conditioned invariant 子空间** | 是本问题的"松弛"（去掉"无零点"）；已知多项式可解 |
| **子空间格最小化**（选最小子空间满足线性约束）| 一般形式常 NP-hard |
| **最小 $A$-不变子空间**含给定子空间 | 多项式可解（$A$-不变包）|

$$\text{本问题}\ =\ \text{"conditioned invariant"}+\text{"无零点"}$$
$$\text{两个约束都多项式可判，但它们的}\textbf{交集最小化}\ \text{未知}$$

---

## 四、为什么"无零点"难处理

### 4.1 它不是一个格条件

$$\mathcal V\ \text{conditioned invariant}\ \Longrightarrow\ \mathcal V+\mathcal W\ \text{也是}$$

$$\text{但"无零点"对}\ \mathcal V+\mathcal W\ \text{不一定继承（数值上 }A\text{-不变包满足，但这只是上界）}$$

### 4.2 它是"开条件"的另一种形式

$$\text{无零点}\iff\gcd\{\rho\text{ 阶子式}(\lambda L-LA;CA;C)\}=1$$

$$\text{这对}\ \mathcal V\ \text{的基选择是"开"的（genericity），不是闭的 ✗}$$

**这与本项目的旧教训一致**："开集 ≠ 稠密"，薄实例的解集是薄集。

---

## 五、一个可能的具体归约

### 5.1 想法：从"最小 $A$-不变子空间含给定子空间"的变体归约

标准的 $A$-不变包是多项式可算的；但若把 $A$ 换成"一个子空间族"，问题变成

$$\min\dim\mathcal V\ \text{s.t.}\ \mathcal VA_i\subseteq\mathcal V+\mathcal J_i\quad(i=1,\ldots,m)$$

$$\text{这是}\ \textbf{多个 conditioned invariant 约束的交} —— \text{已知这类问题常 NP-hard}$$

### 5.2 本问题是否含这种形式？

$$\text{本问题的"A"只有一个，"J"也只有一个 ✗}$$

$$\Longrightarrow\quad \text{没有直接的多约束结构，归约需要别的技巧 ⚠️}$$

**可能的技巧**：用 $A$ 的块结构模拟多个 $A_i$（把 $n$ 扩大 $m$ 倍）。

$$\text{若可行}\ \Longrightarrow\ \textbf{NP-hard}$$

### 5.3 状态

$$\boxed{\ \text{归约尚未完成；这是下一步的核心任务}}$$

---

## 六、诚实总结

| 结论 | 状态 |
|---|---|
| $\textbf{MIN-ROWS}\in\mathrm{NP}$ | ✅ 显然 |
| $\textbf{MIN-ROWS}$ 的多项式算法 | ❌ 无（三层公式都失败）|
| $\textbf{MIN-ROWS}$ 的 NP-hard 证明 | ❌ 无（归约未完成）|
| 三个边界对象的可算性 | ✅ 都有多项式算法 |
| $\rho=0$ 层 = conditioned invariant | ✅ 已验证 1935/1935 |

$$\boxed{\ \text{q1 处于"上界简单、下界未知"的典型状态}}$$

$$\text{这与许多经典的子空间选择问题相同 —— 它们在很长时间里也是这样}$$
