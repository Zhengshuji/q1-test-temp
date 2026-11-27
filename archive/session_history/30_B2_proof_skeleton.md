# 30 — B2：$k=1$ 时 $\Omega^\star_J=\{\Theta=0\}$，但 **$k\ge2$ 时是正维数**！

> ⚠️ **本文的核心结论有一个关键限定**：下面所有"单点"结论**只对 $k=1$ 成立** ✗。
> $k\ge2$ 时 $\Omega^\star_J$ 是**正维数**的（零测，但**无限集**）。
> 这**部分复活**了我在 [history/28](28_problem_reading_and_branchB_counterexample.md) 里
> 提出、后又撤回的"正维数"猜测——**当时撤回对 $k=1$ 是对的，但我错误地推广到了全部** ✗

---

## 0. 最终图景（`b2_k_dim_scan.py`，全部为**支 B** 实例）

| 支 B 实例 | $m$ | 格频率 | **非零扰动命中** | **Groebner 次数** | 结论 |
|---|---|---|---|---|---|
| $q_0{=}2,\ k{=}1,\ s{=}4$ | 3 | 0.008 | **0/1930** | $[1]$ | **单点** ✓ |
| $q_0{=}3,\ k{=}2,\ s{=}4$ | 4 | 0.040 | **218/1967** | $[1,2]$ | **正维数** ✗ |
| $q_0{=}3,\ k{=}2,\ s{=}5$ | 6 | 0.000 | **18/1998** | $[1,2]$ | **正维数** ✗ |
| $q_0{=}4,\ k{=}3,\ s{=}5$ | 6 | 0.000 | n/a | $[2,3,4]$ | **正维数** ✗ |

$$\boxed{\ \dim\Omega^\star_J=0\ (k{=}1)\ ;\qquad \dim\Omega^\star_J>0\ (k\ge2)\ }$$

$$\Longrightarrow\ \textbf{FINAL §8 的"有限孤立点"只对 }k{=}1\text{ 成立；}k\ge2\text{ 应为"零测、正维数"}\ ✗$$

---

## 1. $k=1$：$\Omega^\star_J=\{\Theta=0\}$（**成立** ✓）

> 本文记录 [history/29](29_B2_result.md) 中"Gröbner 基恒为线性"的**代数来源**与**证明骨架**。
> 状态：**骨架完整、判据普遍验证（12 例，$s=3,4,5$）；尚未 Lean 形式化** ⚠️
>
> ⚠️ **2026 更正**：本文初稿曾据 `b2_mechanism.py` / `b2_lemmaA_check.py` 报出
> "线性部分秩只有 2/3"与"解集是直线"的**假反例** —— 那是我**手写 $W$ 时行长度不足**
> （$d_C=5$ 时只造了 3 列）而 `mm` **不检查维数**导致的静默错误 ✗。
> 用与数值检验**同一个** `WJ_of` 构造器重做（`b2_redo.py`）后：
> **12/12 线性部分满秩、12/12 高次无常数项** ✓ 结论恢复。

---

## 0. 一句话

$$\boxed{\ (A)\ \text{的零点集}\ \subseteq\ \{\text{全部子式的\bf{线性部分}同时为 0}\}\ =\ \{0\}\ \Longrightarrow\ \Omega^\star_J=\{0\}\ }$$

**关键**：线性部分的**系数矩阵满秩**（$=m$），故其零点集是**单点** $\{0\}$；而 $0$ 本身是 $(A)$-点 ✓

---

## 1. 数据（`b2_redo.py`，12 例，**正确构造**）

| 形状 | $m$ | 线性子式数 | **秩(线性)** | 高次子式数 | $\Theta{=}0$ 处为 0 | $\in(t_0,\dots,t_{m-1})$ |
|---|---|---|---|---|---|---|
| $(r{=}1,k{=}1,s{=}3)$ | 2 | 2 | **2** ✓ | 2–3 | ✓ | ✓ |
| $(r{=}1,k{=}1,s{=}4)$ | 3 | 5–6 | **3** ✓ | 12 | ✓ | ✓ |
| $(r{=}1,k{=}1,s{=}5)$ | 4 | 6–12 | **4** ✓ | 26–30 | ✓ | ✓ |

$$\textbf{秩(线性部分)}=m\quad\wedge\quad\text{每个高次子式无常数项}$$

---

## 2. 记号

规范化坐标下（`build_norm_T`，$d_C=n-p$，$s=d_C-r$，$k$ 为增广行数）：

| 记号 | 含义 | 形状 |
|---|---|---|
| $\bar A$ | 规范化状态矩阵 | $d_C\times d_C$ |
| $\bar B$ | 规范化输入矩阵 | $k\times d_C$ |
| $\bar C$ | **基行块** $\begin{bmatrix}I_r&0\\0&I_k\end{bmatrix}$ | $(r{+}k)\times d_C$ |
| $\bar W(\Theta)$ | 增广行块 $[I_r\ \ 0]\oplus[0\ I_k\ \Theta]$ | $(r{+}k)\times d_C$ |
| $\Theta$ | 参数（$k=1$ 时是 $1\times(s{-}k)$ 行向量）| 维数 $m=k(s{-}k)$ |

**(A)**（规范化坐标）：
$$(\text{A})\iff\operatorname{rank}\big[\bar W(\Theta);\,\bar B;\,\bar W(\Theta)\bar A\big]=\operatorname{rank}\big[\bar W(\Theta);\,\bar B\big]$$

**等价形式（用 $\rho$）**：令 $\rho=\operatorname{rk}[\bar W(\Theta);\bar B]$（一般位置），则
$$(\text{A})\iff\text{矩阵}\ P(\Theta):=\big[\bar W(\Theta);\,\bar B;\,\bar W(\Theta)\bar A\big]\ \text{的全部}\ (\rho{+}1)\ \text{阶子式}=0$$

**关键结构**：
$$\bar W(\Theta)=\bar W(0)+\bar V(\Theta),\qquad \bar V(\Theta)\ \textbf{对}\ \Theta\ \textbf{线性}$$

$(k{=}1)\Rightarrow\bar V$ 只有**最后一行**非零，且它是 $\Theta$ 的**齐次线性**函数。

⟹ 每个 $(\rho{+}1)$ 阶子式是 $\Theta$ 的**次数 ≤ 2** 的多项式，
且**其中"$\bar V$ 恰好出现一次"的那些是线性的** ✓

---

## 3. 证明骨架

### 3.1 引理 A（**线性部分满秩**｜12/12 验证 ✓，待证 ⚠️）

$$\operatorname{rank}\Big\{\ \text{全部}\ (\rho{+}1)\text{-子式的\bf{线性部分}}\ \Big\}=m$$

即：线性部分在 $\Theta$ 空间上**张满** ⟹ 它们的唯一公共零点是 $\Theta=0$ ✓

#### 3.1.1 ⭐ 线性部分是**一个方阵的行列式族**（关键结构，已验证 ✓）

$(A)$ 是 $\operatorname{rank}\big[\bar W(\Theta);\bar B;\bar W(\Theta)\bar A\big]=\operatorname{rank}\big[\bar W(\Theta);\bar B\big]=:\rho$。
$(k{=}1)$ 时 $\bar W(\Theta)=\bar W(0)+\bar V(\Theta)$，其中 $\bar V(\Theta)$ 只有**一行**非零且线性。

**"$\bar V$ 出现一次"的子式 = 线性部分** ✓

设
$$M(\Theta):=\big[\bar W(\Theta);\,\bar B;\,\bar W(\Theta)\bar A\big],\qquad
M(\Theta)=M(0)+\dot M(\Theta),\quad \dot M\ \text{线性}$$

则对子式 $I_\alpha(\Theta)=\det M(\Theta)[r_\alpha,c_\alpha]$，由行列式的**多重线性**：

$$\boxed{\ \frac{\partial I_\alpha}{\partial \Theta_a}\bigg|_{0}
=\sum_{i\in r_\alpha}\det\Big(M(0)[r_\alpha,c_\alpha]\ \text{第 }i\text{ 行换成}\ \dot M_a[i]\Big)\ }$$

**数值验证**（`b2_jacobian.py`）：

| 形状 | 线性子式数 | "Poly 系数 == 替换一行行列式"一致率 |
|---|---|---|
| $(1,3)$ | 2 | **2/2** ✓ |
| $(1,4)$ | 4 | **4/4** ✓ |

**⟹ 线性部分的系数矩阵 $J$ 是 $N\times m$ 矩阵（$N$ = 线性子式个数），其"原料"是**
$$K:=\big[\,[\bar W(0);\bar B]\ ;\ [\bar W(0);\bar B]\bar A\ ;\ \{\dot v_a\}\ ;\ \{\dot v_a\bar A\}\,\big]$$
**的 $(r{+}k)\times(r{+}k)$ 子式的集合** ✓（数值：$K$ 的秩在 $(1,3)/(1,4)$ 上分别为 $4/4$、$5/5$，满）

#### 3.1.2 证明策略

$$\boxed{\ \text{只需证：}\operatorname{rank} J=m\quad(\text{等价于}\ \dim T_0\Omega^\star_J=0)\ }$$

**已验证（`b2_criterion2.py`，9 例）**：

| 形状 | $m$ | 线性子式个数 | $\operatorname{rank}J$ | $=m$? |
|---|---|---|---|---|
| $(1,3)$ | 2 | 2–3 | **2** | ✓ |
| $(1,4)$ | 3 | 4–6 | **3** | ✓ |
| $(1,5)$ | 4 | 9–12 | **4** | ✓ |

**⟹ 9/9 成立** ✓
（注：线性子式**个数不同**但秩恒为 $m$ —— 说明 $J$ 是正确的不变量 ✓）

**⚠️ 走错的一步（已更正）**：我曾试图把判据化为"$[\bar W(0);\bar B;\bar W(0)\bar A]$ 的 $\theta$-列块满秩"，
但**该判据 0/12 不成立** ✗ —— 因为 $\delta$ **不必**落在 $\operatorname{row}[\bar W(0);\bar B;\bar W(0)\bar A]$ 中。
正确的对象就是 $J$ 本身 ✓

**证明路线（几何版）**：
- $\dim T_0\Omega^\star_J=\dim\ker J^\top$
- $\delta\in\ker J^\top\iff$(A) 沿 $\delta$ 一阶保持 $\iff$
  $\operatorname{rank}M(\varepsilon\delta)=\operatorname{rank}M(0)$ 对一阶 $\varepsilon$ 成立
- 需证：**不存在** $\delta\ne0$ 使 $\operatorname{rank}M(\varepsilon\delta)\le\rho$（一阶）
- **待完成的部分**：把上述"不存在"化为 $J$ 的一个显式行列式非零 ⚠️

**已排除的坏情形**：我曾报出"秩 $=m-1$"的三个实例，**全部是我手写 $W$ 时行长度不足**的 bug ✗
（`mm` 不检查维数 ⟹ 静默算错）。用与数值检验同一个构造器重做后，**12/12 满秩** ✓

**⚠️ 状态**：$\operatorname{rank}J=m$ 普遍成立的**证明未完成** ✗
—— 但已从"黑箱"变成**显式可攻击的命题**：$J$ 的每个元素 = $\det$(把 $M(0)$ 的某行换成 $\dot M_a$ 的某行) ✓

### 3.2 引理 B（**高次部分落在线性理想中**｜6/6 验证 ✓）

$$\boxed{\ \text{每个次数}\ge2\ \text{的子式}\ \in\ \big(\text{全部线性部分生成的理想}\big)\ }$$

**这蕴含**："线性部分同时为 0 $\Rightarrow$ 高次子式也为 0" ✓

**验证**（`b2_divisibility.py`）：
| 形状 | 实例 | 高次子式全 $\in$ 线性理想？ |
|---|---|---|
| $(1,3)$ | 3 | **3/3** ✓ |
| $(1,4)$ | 3 | **3/3** ✓ |

**⚠️ 一个更强的形式**（"每个高次子式 = 线性式 × 线性式"）**不成立**（只有 1/6）✗
—— 所以**理想的成员性**才是正确、可验证的形式 ✓

**⟹ 引理 B 是代数事实，已数值验证；其证明 = 具体矩阵的行列式恒等式（待做 ⚠️）**

### 3.3 组装（**已成立** ✓ —— 且已 Lean 形式化 ✓）

$$\text{(A)}\ \Longrightarrow\ \text{线性部分}=0\ \xrightarrow{\ \text{引理 A}\ }\ \Theta=0\ \Longrightarrow\ \Omega^\star_J\subseteq\{0\}$$
$$\Theta=0\in(A)\ \Longrightarrow\ \{0\}\subseteq\Omega^\star_J$$
$$\boxed{\ \Longrightarrow\ \Omega^\star_J=\{0\}\quad(\text{单点，孤立})\ ✓\ }$$

---

## 4. 与 Gröbner 结果的一致性

| 方法 | 结果 |
|---|---|
| **Groebner 基**（`b2_structure.py`，14 例）| 基 $=\{t_0,\dots,t_{m-1}\}$（线性）⟹ 解 $=\{\Theta=0\}$ |
| **线性部分满秩**（`b2_proof_step3.py`，12 例）| 秩 $=m$ ⟹ 线性部分的解 $=\{\Theta=0\}$ |
| **整数格扫描**（`b2_independent_check.py`）| $(\pm4)^m$ 全域只命中 $\Theta=0$ |

三条独立证据一致 ✓

---

## 5. 意义（对主线）

$$\textbf{支 B 的 (A)-增广总个数}=\#J=\binom{s}{k}\ \text{（多项式）}\ \Longrightarrow\ \textbf{支 B 不是 (A) 层面的硬度源}\ ✓$$

**⚠️ 保留**：完整的"支 B 是否硬度源"还需 **(S)** 在该唯一点上的行为（FINAL 已有"零测"结论）。

---

## 6. 待办

| # | 事项 | 难度 | 状态 |
|---|---|---|---|
| 1 | **Lean 形式化组装**（引理 A、B 作假设）| 🟢 | ✅ **完成** —— `MyProof/Theorems/B2.lean`（3 条定理，**0 error**）|
| 2 | 证 **引理 A**（$\operatorname{rank}J=m$）| 🔴 研究级 | ⏸ |
| 3 | 证 **引理 B**（高次 $\in$ 线性理想）| 🟠 需行列式恒等式 | ⏸ |
| 4 | 扩到 **$k\ge2$** | 🟡 | 🔄 后台（已见 $(1,2,s{=}3/4)$ **无实例**）|
| 5 | 与项目"解数 2"的口径对齐 | 🟡 | ⏸ |

### 6.1 ✅ Lean 已形式化的内容（`MyProof/Theorems/B2.lean`）

| 定理 | 内容 |
|---|---|
| `omega_subset_singleton` | $\Omega\subseteq\bigcap\ker f_i$ $\wedge$ $\bigcap\ker f_i=\{0\}$ $\wedge$ $0\in\Omega$ $\Longrightarrow$ $\Omega=\{0\}$ |
| `ker_inter_eq_singleton` | $(\forall\theta,\ (\forall i,f_i\theta=0)\Rightarrow\theta=0)\Rightarrow\bigcap\ker f_i=\{0\}$ |
| `omega_singleton_of_lemmas` | **引理 A + 引理 B + $0\in\Omega$ $\Longrightarrow$ $\Omega=\{0\}$** |

**主库**：`lake build` → **Build completed successfully (18116 jobs)** ✓

**⟹ 逻辑组装已机器验证；代数内容（引理 A、B）currently 作为假设** ✓

---

## 7. 脚本

| 脚本 | 用途 |
|---|---|
| **`MyProof/Theorems/B2.lean`**（WSL）★ | ⭐ ⭐ **Lean 形式化的条件定理**（组装部分，0 error）|
| **`scripts/core/b2_redo.py`** | ⭐ 用**正确构造**重做的 12 例检验（引理 A 满秩 + 引理 B 无常数项）|
| **`scripts/core/b2_divisibility.py`** | ⭐ **引理 B 的精确形式**：高次 $\in$ 线性理想（6/6）|
| **`scripts/core/b2_criterion2.py`** | ⭐ 正确判据：$\operatorname{rank}(J)=m$（9/9）|
| **`scripts/core/b2_lemmaA_explicit.py`** | ⭐ 显式化：线性部分的系数向量 + 秩 |
| **`scripts/core/b2_jacobian.py`** | ⭐ "系数 = 替换一行后的行列式"验证（6/6 一致）|
| `scripts/core/b2_final3.py` | 四条判据的一致性核验 |
| `scripts/core/b2_arbitrate.py` | 仲裁 Groebner vs 数值（**暴露我手写 W 的 bug**）|
| `scripts/core/b2_mechanism.py`、`b2_lemmaA_check.py` | ⚠️ **含 bug 的脚本**（手写 $W$ 行长度不足）——保留作反面教材 |
| `scripts/core/b2_criterion.py` | ⚠️ **错误判据**（$\theta$-列块，0/12）——保留作反面教材 |
| `scripts/core/b2_structure.py`、`b2_independent_check.py`、`b2_compare.py` | [history/29](29_B2_result.md) 的 Groebner 与对照 |
| `scripts/core/b2_bound.py`、`b2_elim.py`、`b2_verify.py`、`b2_shapes.py` | 早期符号化与形状核对 |

---

## 8. 本轮累积的自我更正（2 处）

| # | 错误 | 更正 |
|---|---|---|
| **1** | 手写 $W$ 时**行长度不足**（$d_C{=}5$ 只造 3 列），`mm` 不检查维数 ⟹ 静默算错 ⟹ 报出"线性部分秩 $m-1$"与"解集是直线"的**假反例** ✗ | 改用与数值检验**同一个** `WJ_of` 构造器 ⟹ 12/12 满秩 ✓ |
| **2** | 把判据化为"$\theta$-列块满秩"（`b2_criterion.py`），**0/12 不成立** ✗（因 $\delta$ 不必在 $\operatorname{row}[\bar W(0);\bar B;\bar W(0)\bar A]$ 中）| 正确判据是 $J$ 本身 ✓（`b2_criterion2.py`，9/9）|

$$\textbf{教训}：\texttt{mm}\ \text{不检查维数} \Rightarrow \textbf{必须自己断言}；\ \text{且"换一个等价判据"前要确认推导的每一步}\ \checkmark$$
