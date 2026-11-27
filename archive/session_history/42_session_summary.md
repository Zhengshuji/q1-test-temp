# 42 — 本轮总结（2025 续）：D4 完成 · D6 深挖 · 三处更正

> 本文是本轮（承接 [history/27](27_solver_bug_and_caseII_recheck.md) 之后）的**总索引**。

---

## 0. 一句话

$$\boxed{\ \textbf{净成果}：\textbf{D4 完成（Lean 0 error，并入主库）}\ ✓\ ;\quad \textbf{D6 深挖（模论形式找到，但对生成器平凡）}\ ⚠️\ }$$
$$\boxed{\ \textbf{净教训}：\text{我在本轮犯了}\ \textbf{2 处判据错误}（已更正）\ \text{—— 与项目历史上的教训同源}\ ⚠️}$$

---

## 1. ✅ 净成果一：**D4 完成**

### 1.1 定理（`MyProof/Theorems/D4.lean`，**0 error**）

$$T,S_1,S_2,S_3:P\to V,\quad \operatorname{range}T\subseteq\textstyle\sum\operatorname{range}S_i
\Longrightarrow\exists\Lambda,G_0,G_1:\ T=S_1\Lambda+S_2G_0+S_3G_1$$

$$\textbf{主库}\ \texttt{lake build}\ \to\ \textbf{Build completed successfully (18118 jobs)}\ ✓$$

**记录**：[history/37](37_D4_progress.md)

### 1.2 迭代统计（诚实）

| 项 | 数量 |
|---|---|
| Lean 编译迭代 | **22 轮** |
| 最耗时的坑 | **`LinearMap.comp` 的方向**（`g.comp f` 是 $g\circ f$）|

---

## 2. ⚠️ 净成果二：**D4 → c6′ 的类型障碍**（精确）

$$\textbf{D4 输出"同源系数"}\ (\Lambda,G_0,G_1:P\to P)\ ;\qquad
\textbf{(A) 需要"异源系数"}\ (\Lambda:W\to W,\ G_0:W\to G,\ G_1:W\to G)$$

$$\text{根源}：(A)\ \text{中}\ \mathcal L:W\to W\ \text{而}\ C,CA:W\to G\ \text{——}\textbf{陪域不同}\ ✗$$

**两条路**：
| 路 | 做法 | 评估 |
|---|---|---|
| **1** | 直和桥接（$\mathcal P=W\times(G\times G)$ + 分块）| 数学显然；Lean 工作量大 |
| **2** | 改 c6′ 表述为"对偶空间的分解" | 便宜；但需检查后续论证是否够用 |
| **3** ⭐ | 只取 $\Lambda$（**c6′ 的证明只用到 $\Lambda$**）| 见 §3 |

**记录**：[history/38](38_bridge_obstacle.md)、[39](39_route_C_insight.md)、[40](40_routeC_final.md)

---

## 3. ⚠️ 路 C 的探索与**我的 2 处错误**

### 3.1 路 C 的目标

$$\text{绕开桥接}：\text{只证}\ \exists\Lambda,\ F=\Lambda H\quad(H=LN,\ F=LAN)$$

### 3.2 🚨 错误 1：一个**假引理**

$$\text{我曾断言}：\operatorname{range}T\subseteq\operatorname{range}H\ \Longrightarrow\ \exists\Lambda,\ T=\Lambda\circ H$$
$$\textbf{反例}：H=\begin{pmatrix}1&0\\0&0\end{pmatrix},\ T=\begin{pmatrix}0&0\\0&1\end{pmatrix}$$
$$\text{根源}：\operatorname{range}\ \text{包含}\ \textbf{不蕴含}\ \ker H\subseteq\ker T$$

### 3.3 🚨 错误 2：一个**太弱的判据**（假阳性）

$$\text{我用}\ \operatorname{rk}[LN\mid LAN]=\operatorname{rk}[LN]\ (\textbf{列拼接})\ \text{作判据}$$
$$\textbf{那只是 range 包含}\ ✗\ ;\qquad
\text{可因子化需要}\ \textbf{行堆叠}\ \operatorname{rk}[LN;LAN]=\operatorname{rk}[LN]\ \checkmark$$

$$\Longrightarrow\ \text{我报的"12/12 ✓"、"14/14 ✓"是}\ \textbf{假阳性}\ ✗$$

### 3.4 路 C 的最终结论

| 检验 | 结果 |
|---|---|
| **ker 条件** $\ker(LN)\subseteq\ker(LAN)$（项目真实装置 + $(A)$）| **16/16** ✓ |
| 精确求解 $LAN=LN\cdot X$（$A$-不变）| **18/18 可解** ✓ |
| 非 $A$-不变（构造）| **有反例** ✗ |
| 我推导的"$A$-不变 $\Rightarrow$ ker 条件" | **不成立** ✗（$A$-不变不足）|

$$\Longrightarrow\ \textbf{ker 条件数值全成立，但}\ \textbf{机制未明}\ ⚠️$$

---

## 4. 🔴 净成果三：**D6（$q_0$ 下界）深挖**

### 4.1 ✅ 找到了模论形式（手算例验证 ✓）

$$\mathcal C:=\operatorname{row}[C;CA;\dots;CA^{n-1}]\quad(A\text{-不变}\ ✓)$$
$$(A)\iff\operatorname{row}(\mathcal L)+\mathcal C\ \text{是}\ A\text{-不变的}
\iff \frac{\operatorname{row}\mathcal L+\mathcal C}{\mathcal C}\ \text{是}\ \bar A\text{-不变的}$$
$$\Longrightarrow\ q_0=\min\{\dim\bar W:\ \bar W\ \bar A\text{-不变},\ \bar L_0\subseteq\bar W\}\quad(\text{在}\ V/\mathcal C\ \text{中})$$

**手算例验证**（`D6_hand.py` ✓）：
$$A=\operatorname{diag-block}(J_2(0),2),\ C=e_1^*,\ L_0=e_3^*\ \Longrightarrow\ q_0=1=\text{最小不变维数}\ ✓$$

### 4.2 🔴 但对**生成器实例**平凡（关键限制）

$$\text{项目的生成器取}\ L_0=CA^m\ \Longrightarrow\ \mathbf{L_0\in\mathcal C}\ \Longrightarrow\ \bar L_0=0\ \Longrightarrow\ \min=0\ (\text{或}\ n)\ne q_0\ ✗$$

**三个候选显式公式全部失败**：

| 候选 | 结果 |
|---|---|
| F1：$q_0=\dim(\mathcal C_{\rm full}+\operatorname{span}\{L_0A^k\})$ | **0/14** ✗ |
| F2：$q_0=\dim(\operatorname{row}[C;CA]+\operatorname{span}\{L_0A^k\})$ | **0/14** ✗ |
| F3：$q_0=\dim\operatorname{span}\{L_0A^k\}$ | **1/14** ✗ |

### 4.3 诚实评估

| 项 | 状态 |
|---|---|
| 模论形式（$L_0\notin\mathcal C$）| ✅ 手算例 ✓ |
| 生成器实例（$L_0\in\mathcal C$）| 🔴 平凡 ✗ |
| $q_0$ 下界的**普遍证明** | 🔴 **未完成** |
| P1 Theorem 2 的独立验证 | 🔴 **未完成** |

$$\textbf{结论}：\text{D6 比预想微妙} —— \text{生成器的}\ L_0\in\mathcal C\ \text{使"商空间/轨道"论证失效，}$$
$$\text{需要}\ \textbf{利用}\ L_0\ \text{与}\ \mathcal C\ \text{的相对位置}\ \text{（功能性指数}\ \eta\ \text{的真正含义）} ⚠️$$

**已有的严格结果**（项目）：对生成器实例**严格确认**不存在 2 行 (A)-增广 ⟹ 最小行数 $=3=\eta_1$ ✓（子式插值，无缺口 ✓）—— 但只覆盖特定形状。

**记录**：[history/41](41_D6_structure.md)

---

## 5. 🎯 本轮最重要的教训

$$\boxed{\ \textbf{判据的"方向"必须与所需结论严格对应}\ }$$

| 判据 | 蕴含 |
|---|---|
| $\operatorname{rk}[\text{**列拼接**}]\ \text{相等}$ | range 包含 |
| $\operatorname{rk}[\text{**行堆叠**}]\ \text{相等}$ | $\ker$ 条件 |
| $\dim(\text{span}+\text{span})$ 相等 | 子空间相等 |

$$\text{我混淆了前两者} \Longrightarrow \textbf{假阳性}\ ✗$$
$$\text{这与项目历史上的第 13 处（\texttt{mm} 维数错配）、第 20 处（"只用第一行"）}\ \textbf{同源}\ ⚠️$$

---

## 6. 累计资产

### 6.1 Lean（**25 条定理，主库 18118 jobs，零 error** ✓）

| 模块 | 定理 |
|---|---|
| `Foundations/Basic.lean` | F1 / F3 / F4 / F4' / finrank_top_eq / F5 / T5a_core / **T5a** |
| `Theorems/Pencil.lean` | T5' / T2 |
| `Theorems/CaseII.lean` | T6 |
| `Theorems/Spectral.lean` | rank_comp_eq_iff / **T5** |
| `Theorems/Decomp.lean` | `F_eq_Lam_comp_H` |
| `Theorems/C6.lean` | `c6'_CA2_zero` / **`c6'_conditional`** / `c6'_final`（**条件式**）|
| `Theorems/B2.lean` | B2 |
| `Theorems/D4.lean` 🆕 | `pi1/2/3` / `Omega` / `Omega_range` / **`decomp_of_range_le`** |

### 6.2 未完成的（诚实）

| 项 | 状态 |
|---|---|
| c6′ 的**无条件**化（桥接）| 🔴 类型障碍 |
| 路 C 的 ker 条件机制 | ⚠️ 数值 16/16，机制未明 |
| D6 $q_0$ 下界的普遍证明 | 🔴 未完成 |
| D1/D2（归约 / 多项式算法）| 🔴 平台期 |
| D7（图卡限定）| ⚠️ 未解决 |

---

## 7. 下一步（按优先级，明确）

| 序 | 方向 | 动作 | 预期 |
|---|---|---|---|
| **1** ⭐ | **D6** | 从 $\eta$ 的**真正定义**出发，找 $q_0$ 的显式公式（我已试 3 个，皆败——需换角度）| 或有突破 |
| **2** | **D3** | 走 §2 的**路 1（直和桥接）**——数学显然，Lean 工作量大 | 确定但耗时 |
| **3** | **D3** | 或**精确化路 C 的 ker 条件机制** | 中间难度 |
| **4** | **D6** | 退一步：**形式化已有的子式插值结果**（严格但只覆盖特定形状）| 巩固已知 |
| **5** | **D7** | 图卡限定的界定 | 明确结论范围 |

### 7.1 我的判断

$$\text{D6 的困难在于：}\text{生成器实例的}\ L_0\in\mathcal C\ \text{使几何直观失效}$$
$$\text{需要}\ \textbf{纯代数地}\ \text{刻画}\ q_0\ \text{——}\text{这可能需要新的洞察（不便宜）} ⚠️$$

$$\text{而}\ \textbf{D3 的路 1（直和桥接）}\ \text{虽然繁琐，但}\ \textbf{路径明确} ✓$$
$$\text{若目标是"消除 c6′ 的条件假设"，路 1 比 D6 更可靠} ✓$$
