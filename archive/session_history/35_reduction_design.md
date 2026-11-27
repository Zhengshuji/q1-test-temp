# 35 — 归约设计：从 1-in-3-SAT 到 $\mathcal P$

> 承接 [history/34](34_P_final_form.md)。本文给出**归约的具体设计**与已完成的充分性验证。

---

## 0. 一句话

$$\boxed{\ \text{模板}\ (\bar A,\bar B)\mapsto(\text{二次形式})\ \textbf{满射}\ \Longrightarrow\ \text{可编码任意二次约束}\ \Longrightarrow\ \text{归约可行}\ ✓}$$

**目标**：从 **1-in-3-SAT**（NP-完全）归约到 $\mathcal P$：

$$\mathcal P:\quad \exists\,\Theta:\ (A)\wedge\operatorname{rank}\big(\mathcal L(\Theta)N_{CA}\big)<q_0\ ?$$

---

## 1. 为什么选 1-in-3-SAT（而不是 3-SAT）

$$\text{3-SAT 的子句}\ (x_1\vee x_2\vee x_3)\ \text{含"至少一个"}\ \Longrightarrow\ \textbf{不是} \text{单个多项式方程}\ ✗$$
$$(\text{例：若用多项式 }P=0\ \text{编码"至少一个真"，则 }P\ \text{必须是乘积型} \Longrightarrow\ \text{"全真"而非"至少一个"}\ ✗)$$

$$\text{1-in-3-SAT 的子句}\ = \{x_1+x_2+x_3=1\}\ \wedge\ \{x_ix_j=0\ \forall i<j\}\quad\textbf{全是二次}\ \checkmark$$

$$\text{而 1-in-3-SAT 是 NP-完全的（Schaefer）}\ \checkmark$$

---

## 2. 归约的两步

### 2.1 第 1 步（**已完成** ✓）：表达力

模板：$M_J(\Theta)$ 的 $(\rho{+}1)$ 阶子式，其中

$$M_J(\Theta)=\big[\bar W_J(\Theta);\ \bar B;\ \bar W_J(\Theta)\bar A\big],\qquad
\bar W_J(\Theta)=[I_r\ 0;\ 0\ I_k\ \Theta]$$

**数值验证**（`scripts/core/P_surjectivity.py`）：

| 形状 | $m=k(s{-}k)$ | $D=\frac{m(m+1)}{2}$ | 子式系数向量张成维数 | 满射 |
|---|---|---|---|---|
| $(r{=}1,k{=}2,s{=}4,d_C{=}5)$ | 4 | 10 | **10** | ✓ |
| $(r{=}1,k{=}2,s{=}3,d_C{=}4)$ | 2 | 3 | **3** | ✓ |

$$\Longrightarrow\ \text{变动}\ (\bar A,\bar B)\ \text{可张成全部二次形式}\ \checkmark$$

### 2.2 第 2 步（**待完成** ⚠️）：编码

需要：给定二次系统 $\{Q_j(\Theta)=0\}$，**构造**一个 $(\bar A,\bar B)$ 使其 $(A)$-子式**恰好**是某个包含 $Q_j$ 的理想。

**障碍（诚实标注）**：
$$\text{满射是关于}\ (\bar A,\bar B)\ \text{的（跨实例）}；\text{而一个实例的}\ (\bar A,\bar B)\ \textbf{固定}\ \checkmark$$
$$\Longrightarrow\ \text{需要解"逆问题"：}\text{给定 }Q_j\ \text{求}\ (\bar A,\bar B)\ \text{使子式} = Q_j$$
$$\text{由满射性，逆问题}\ \textbf{有解}；\text{但需}\textbf{显式构造}\ ✗$$

---

## 3. 归约的完整框架（设计）

$$\text{1-in-3-SAT 实例}\ \varphi\ \text{（变量 }x_1,\dots,x_N\text{，子句 }c_1,\dots,c_M\text{）}$$

| 步骤 | 内容 |
|---|---|
| ① | 为每个变量 $x_i$ 分配参数 $\Theta_i$；约束 $x_i^2=x_i$（二次 ✓）|
| ② | 为每个子句分配约束 $x_a+x_b+x_c=1$ 与 $x_ax_b=x_ax_c=x_bx_c=0$（二次 ✓）|
| ③ | 由 §2.1 的满射性，把上述全部二次约束**实现**为 $(A)$-子式（**待完成**）|
| ④ | 构造 $(\bar A,\bar B)$，并验证：$\varphi$ 可满足 $\iff$ $\mathcal P$ 为 YES |
| ⑤ | 附加退化条件（$\operatorname{rank}H<q_0$）使之等价于 $(A)\wedge(S)$ |

### 3.1 一个技术要点

$\mathcal P$ 的结论部分含有"$\operatorname{rank}H<q_0$"（退化条件）。
在归约中，需把该条件与二次系统一起处理；**最简做法**：把退化条件也编成二次约束
（$H$ 的 $q_0$ 阶子式 $=0$ 是二次的 ✓）。

---

## 4. 归约的**三个可能失败点**（诚实标注，本轮新增第 3 点）

| # | 风险 | 说明 |
|---|---|---|
| **1** | **逆问题可能不易显式求解** | 满射性只保证"存在"，构造需要解非线性方程组 |
| **2** | **子式之间可能存在耦合** | 同一 $(\bar A,\bar B)$ 产生的子式**不独立**；若耦合太强，无法同时实现"我们需要的那组"约束 |
| **3** | 🔴 **$(A)$ 条件可能"空洞化"**（本轮新发现）| 见下 |

### 4.1 ⚠️ 风险 3 的细节（`scripts/core/P_inverse.py` 暴露）

把 $(\bar A,\bar B)$ 也符号化后，$[W;B]$ 中的 $\Theta$ 成了**符号** ⟹ 其**一般秩 $\rho$ 达到矩阵最大可能秩** ⟹ $(\rho{+}1)$ 阶子式为**空** ⟹ $(A)$ **空洞成立**：

$$\text{实例}\ (r{=}1,k{=}2,s{=}4,d_C{=}5):\ \rho=5\ (\text{最大})\ \Longrightarrow\ 0\ \text{个二次子式}\ ✗$$

$$\Longrightarrow\ \textbf{$(A)$ 的约束力来自}\ [W(\Theta);B]\ \text{的秩\textbf{随}\ \Theta\ \text{下降}}$$
$$\Longrightarrow\ (\bar A,\bar B)\ \text{必须取}\ \textbf{特殊值}\ \text{才能使条件非空}\ \text{—— 归约的构造必须精确落在这些值上}\ ⚠️$$

**这解释了此前所有数值实验的一致现象**：
$$\text{(A)}\ \textbf{几乎总成立}\（\text{泛点}\ \rho=\text{最大}\ \text{使条件空洞）}\ ;\qquad
\text{退化点}\ \textbf{稀有}\（\text{正是"秩降"发生的特殊轨迹}）$$

$$\textbf{风险 3 与 §4 风险 2 相关}：\text{"特殊值"集合本身可能就是}"NP-hard\ \text{判定}"\ \text{的所在}\ \checkmark$$

---

## 5. 反方向：多项式算法（若归约失败）

$$\mathcal P\ \text{的结构特殊}：\text{子式次数}\le2\ \text{且变量只在 } k\ \text{行}\ \Longrightarrow\ \text{可能有线性代数判据}$$

| $k$ | $\dim\Theta$ | 已知 |
|---|---|---|
| $k=1$ | $s-1$ | ✅ $\Omega^\star_J=\{0\}$（**单点**）⟹ 判定 $(S)$ 即可 ⟹ **多项式** ✓ |
| $k\ge2$ | $k(s-k)$ | ❌ 未定 |

$$\text{若能把 }k\ge2\ \text{归约到 }k=1\ \text{的情形（或证明退化簇的检测是线性的）}\ \Longrightarrow\ \mathcal P\in P\ \checkmark$$

---

## 6. 下一步（明确）

| 序 | 动作 | 产出 |
|---|---|---|
| **1** | **显式逆问题**：对 $(k{=}2,s{=}4)$ 单参数化，解出实现"给定二次形式"的 $(\bar A,\bar B)$ | 归约的构造基石 |
| **2** | **小实例验证**：取一个小 1-in-3-SAT（如 3 变量 2 子句），构造 $(\bar A,\bar B)$，**数值验证**可满足性等价 | 归约的正确性 |
| **3** | 若 1、2 成功 ⟹ 推广到一般 $N,M$ ⟹ **q1 是 NP-hard** ✓✓ | 项目目标 |
| **4** | 若失败 ⟹ 转向**多项式算法**（$k$ 的归纳）| 证伪方向 |

---

## 7. 本轮产出

| 文件 | 内容 |
|---|---|
| **本文** | 归约设计 + 充分性验证 + 风险标注 |
| `scripts/core/P_surjectivity.py` | ⭐ **满射性验证**（归约的关键前提）|
| `scripts/core/P_expressivity.py` | 单项式覆盖面分析（辅助）|
| [history/34_P_final_form.md](34_P_final_form.md) | $\mathcal P$ 的最终形式 |
| [history/33_mainline_unification.md](33_mainline_unification.md) | 支 B ≡ 情形 II |
