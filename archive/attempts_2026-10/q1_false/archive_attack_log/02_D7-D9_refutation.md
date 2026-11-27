> **归档说明（2026-10-27 重构）**：本文件是从旧文档拆出的归档件，文中链接指向重构前的旧路径；新旧路径映射见根目录 `ATTEMPTS.md` 与 `README.md`。

# 攻击日志 · D7–D9（拆分自 ATTACK_LOG.md）

> 原文：`archive/attack_A2V0/ATTACK_LOG.md`。

## D7：$(5a)$ 与 $(5b)$ 是否等价？—— **不等价**（已否决）

### 我的猜测（错）

$$L\in R\ \text{且}\ \lambda L-LA\in R\ (\lambda\ne0)\ \Longrightarrow\ LA\in R\ \Longrightarrow\ (5a)$$
$$\Longrightarrow\ \text{猜想}\ (5b)\Rightarrow(5a)\ \text{甚至}\ (5a)\iff(5b)$$

### 测试结果（4777 个组合）

| 情形 | 个数 |
|---|---|
| 两者都成立 | 1708 |
| **只 $(5a)$** | **1097** |
| **只 $(5b)$** | **1970** |
| **不一致** | **3067** ✗ |

$$\boxed{\ \text{两者\textbf{不等价}，且互不包含}}$$

### 我错在哪

$$(5b)\ \text{是\textbf{秩}等式}:\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]$$
$$\text{秩相等只给"同维数"，\textbf{不给}同行空间}\ ✗$$

$$\text{只有在已有 }(5a)\ (\text{保证 }\ker M\subseteq\ker(\lambda M-F))\ \text{时，才推出核相等}\ ✓$$

$$\text{而那时得到的信息与 }(5a)\ \text{单独给的\textbf{相同}} —— \text{仍是\textbf{一阶}}$$

### 结论（关键）

$$\boxed{\ (5a)\wedge(5b)\ \text{合起来也不给 }LA^2\ \text{的任何信息}}$$

$$\Longrightarrow\ LA^2\in\operatorname{row}[L;CA;C]\ \text{不能从 }(5a)\wedge(5b)\ \text{纯代数地推出（就我所知）}$$

$$\text{虽然它\textbf{数值上成立}（14/14）—— 说明背后有未发现的结构，或它不是代数推论而是"最小值解"的性质}$$


---

# 🚨🚨 D8：定理被推翻（2026-10-24 02:20）

### 反例（完整证书）

$$n=5,\ p=2,\ q=1,\ d=1,\ \dim V=1,\ p=\dim S=1$$

$$A=\begin{pmatrix}0&0&1&-2&-1\\1&-2&2&0&2\\1&1&-2&0&0\\-2&2&0&-1&0\\-1&-1&2&-1&0\end{pmatrix},\quad
C=\begin{pmatrix}-1&1&1&0&-1\\1&-1&-2&-1&-1\end{pmatrix},\quad
L=\begin{pmatrix}2&-2&-1&1&1\end{pmatrix}$$

### 精确验证

```
(5a) = True                 （精确秩判定）
(5b) = True                 （20 个非零 ρ 阶子式，gcd = 1，次数 0）
dim V = 1,  q = 1,  α₀ ∈ V = True
```

$$\boxed{\ q_{\min}\le 1\ <\ 2=\dim V+1\quad\Longrightarrow\quad \textbf{定理 }q_{\min}=\dim V+1\ \textbf{被推翻}\ }$$

### 崩在哪

| 量 | 值 |
|---|---|
| $\mathcal LN$ | **0**（$\dim\mathcal A=0$）|
| $S\subseteq\mathcal A$ | **False** ✗ |
| $\rho=\dim\mathcal A$ | 0 |
| $\dim V$ | 1 |
| $q$ vs $\rho+1$ | $1=1$ ✓ |

$$\boxed{\ \text{崩溃点：}S\subseteq\mathcal A\ (\text{Gap A})\ \text{为假}\Longrightarrow\rho<\dim V\Longrightarrow q_{\min}\le\rho+1<\dim V+1}$$

### 为什么之前的搜索没发现

- §34（24188 个解）与 §42 的搜索都用了 $\alpha_0\in V$ 与 $q\ge r$ 的过滤
- 本例是**退化边界**：$\mathcal LN\equiv0$（$L$ 的行全在 $\ker(\cdot N)$ 里）
- 之前的 "18/18、24188/24188 满足 $S\subseteq\mathcal A$" **全部是错的结论** ✗

### 后果

| 项 | 之前 | 现在 |
|---|---|---|
| 定理 $q_{\min}=\dim V+1$ | 6/7 已证 | ❌ **假** |
| 下界 $q\ge\dim V+1$ | 已证 | ❌ **假** |
| Gap A（$S\subseteq\mathcal A$）| 24188/24188 验证 | ❌ **假**（本节反例）|
| $q\ge\rho+1$（§32）| 已证 | ✅ **仍成立**（本例 $1=1$）|
| $\dim B\le p$（§29）| 已证 | ✅ 仍成立（独立结论）|
| $N^{\mathsf T}R_0=0$、$S'=S$ | 已证 | ✅ 仍成立（纯代数恒等式）|

### 正确的下界是什么

$$\text{已知}:\quad q\ge\rho+1\quad(\rho=\dim\operatorname{row}(\mathcal LN))$$

$$\text{但}\ \rho\ \text{依赖 }\mathcal L\ \text{本身 —— 这不是一个"可算的下界" ✗}$$

$$\boxed{\ \text{所以下界问题重新开放：}q_{\min}\ \text{的正确下界未知}}$$

### 教训（加入纪律）

$$\boxed{\ \textbf{不要用带过滤的随机搜索验证"对所有解成立"的断言} —— \text{过滤本身就是断言的一部分}}$$


---

## D9：反例的结构 —— 两个 regime

### 反例的退化结构

```
L·N = 0          ← L 的所有行都在 ker(·N) 里
dim ker(·N) = 4  （n=5, d=1）
L ∈ ker(·N)      ✓
```

$$\boxed{\ \text{反例属于"\textbf{退化}"情形：}\mathcal LN=0}$$

### 两个 regime

| regime | 定义 | 下界 |
|---|---|---|
| **非退化** | $\operatorname{row}(\mathcal LN)=V$ | $q\ge\dim V+1$（我的定理覆盖这一半）|
| **退化** | $\operatorname{row}(\mathcal LN)\subsetneq V$（极端：$=0$）| $q$ 可以很小 |

$$\boxed{\ q_{\min}=\min\big(q_{\text{非退化}},\ q_{\text{退化}}\big)}$$

### 新猜想

$$q_{\min}=\min\big(\dim V+1,\ q_{\deg}\big)$$

其中 $q_{\deg}$ 是**退化解**（$\mathcal LN=0$）的最小行数。

- 反例：$q_{\deg}=1$，$\dim V+1=2$ ⟹ $q_{\min}=1$ ✓（与实测一致）
- 若对所有实例 $q_{\deg}\ge\dim V+1$，则原定理仍成立

### 退化解的结构问题

$$\mathcal LN=0\iff \mathcal L\ \text{的行} \in\ker(\cdot N)$$

$\ker(\cdot N)$ 的维数是 $n-d$（本例 4）。问：在这个子空间里，
满足 $(5a)\wedge(5b)$ 的最小行数是多少？

$$\boxed{\ \text{这是新的、独立的组合问题} —— \text{可能正是 q1 的难点所在}}$$

### 教训（第 8 条纪律）

$$\boxed{\ \textbf{不要用带过滤的随机搜索验证"对所有解成立"的断言}}$$

（我搜 $S\subseteq\mathcal A$ 时用了 $\alpha_0\in V$ 与 $q\ge r$ 的过滤，过滤本身隐含了结论 ✗）


---

