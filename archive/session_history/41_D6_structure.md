# 41 — D6（$q_0$ 下界）的**结构性发现**

> 承接 [DIRECTIONS.md](docs/DIRECTIONS_2026-10-18.md) 的 D6。本文记录本轮对 $q_0$ 下界的结构分析。

---

## 0. 一句话

$$\boxed{\ \textbf{模论形式正确}：q_0=\min\{\dim\bar W:\bar W\ \bar A\text{-不变},\ \bar L_0\subseteq\bar W\}\ \text{（在商 }V/\mathcal C\text{ 中）}\ }$$
$$\textbf{但它只在}\ L_0\notin\mathcal C\ \text{时非平凡}；\ \text{而项目的生成器恰好取}\ L_0=CA^m\in\mathcal C\ ✗$$

---

## 1. ✅ 模论形式（已用手算例验证）

### 1.1 陈述

$$\mathcal C:=\operatorname{row}[C;CA;\dots;CA^{n-1}]\ (\textbf{完整可观测空间}，A\text{-不变}\ ✓)$$
$$(A)\iff \operatorname{row}(\mathcal L)+\mathcal C\ \text{是}\ A\text{-不变的}
\iff \bar{\mathcal L}:=\frac{\operatorname{row}\mathcal L+\mathcal C}{\mathcal C}\ \text{是}\ \bar A\text{-不变的}$$
$$\Longrightarrow\ \boxed{\ q_0=\min\{\dim\bar W:\ \bar W\ \bar A\text{-不变},\ \bar L_0\subseteq\bar W\}\ }$$

### 1.2 验证（手算小例 ✓）

$$A=\begin{bmatrix}0&1&0\\0&0&0\\0&0&2\end{bmatrix},\quad C=[1,0,0],\quad L_0=[0,0,1]$$
$$\mathcal C=\operatorname{row}[C;CA;CA^2]=\operatorname{span}\{e_1,e_2\},\quad \dim(V/\mathcal C)=1$$
$$\bar L_0=\bar e_3\ne0,\quad \bar A\bar e_3=2\bar e_3\ \Longrightarrow\ \text{最小不变子空间}=\operatorname{span}\{\bar e_3\},\ \dim=1$$
$$\text{而}\ p1\ \text{给出}\ \eta=[1],\ q_0=1\ \checkmark\ \textbf{一致}\ ✓$$

---

## 2. ⚠️ 关键限制：$L_0\in\mathcal C$ 时形式平凡

### 2.1 观察

$$\text{项目的生成器取}\ L_0=CA^m\ \Longrightarrow\ \mathbf{L_0\in\mathcal C}\ \Longrightarrow\ \bar L_0=0\ \Longrightarrow\ \min=0\ne q_0\ ✗$$

**数值证据**（`scripts/core/D6_verify3.py`，14 个随机实例）：
$$\text{全部给出}\ \min\text{InvDim}=0\ \text{（因}\ L_0=CA^m\in\mathcal C\text{）}\ ✗$$

$$\Longrightarrow\ \textbf{模论形式对生成器实例不适用}\ \text{（但对手算例适用 ✓）}$$

### 2.2 这意味着什么

$$\text{生成器实例的}\ L_0\ \textbf{本身就在可观测空间内}\ \Longrightarrow\ \text{"用}\ L_0\ \text{的信息"不足以决定}\ q_0$$
$$\text{真正的约束来自}\ L_0\ \text{的}\ \textbf{"功能性"}\ \text{：}\ L_0\ \text{虽在}\ \mathcal C\ \text{中，但}\ (A)\ \text{要求}\ L_0\ \text{的}\ A\text{-轨道被}\ \mathcal L\ \text{"承接"}$$
$$\Longrightarrow\ \text{需要}\ \textbf{更细的分解}\ \text{（如按}\ L_0A^k\ \text{的"阶"分层）}$$

---

## 3. 修正后的尝试（**全部失败**，见下表）

| 候选公式 | 结果 |
|---|---|
| F1：$q_0=\dim(\mathcal C_{\rm full}+\operatorname{span}\{L_0A^k\})$ | **0/14** ✗ |
| F2：$q_0=\dim(\operatorname{row}[C;CA]+\operatorname{span}\{L_0A^k\})$ | **0/14** ✗ |
| F3：$q_0=\dim\operatorname{span}\{L_0A^k\}$ | **1/14** ✗ |

（$\mathcal C_{\rm full}=\operatorname{row}[C;CA;\dots;CA^{n-1}]$）

$$\textbf{全部失败的原因}：\text{生成器实例的}\ L_0=CA^{mp}\in\mathcal C\ \text{（甚至}\ L_0\in\operatorname{row}[C;CA]\text{）}$$
$$\Longrightarrow\ \operatorname{span}\{L_0A^k\}\subseteq\mathcal C\ \Longrightarrow\ \text{F1 给出}\ \dim\mathcal C=n\ne q_0\ ✗$$

### 3.1 为什么"商空间"论证在此失效

$$\text{模论形式的前提是}\ \bar L_0\ne0\ \text{（即}\ L_0\notin\mathcal C\text{）}$$
$$\text{而生成器恰好取}\ L_0\in\mathcal C\ \text{——这是}\ \textbf{功能性}\ \text{情形（}L_0\ \text{的信息已在输出中）}$$
$$\text{此时}\ q_0\ \text{反映的不是"}\ L_0\ \text{在商中的像"，而是}\ \textbf{"}\ L_0\ \text{的}\ A\text{-轨道被承接所需的最小行数"}$$

$$\Longrightarrow\ \text{需要}\ \textbf{按}\ A\text{-轨道分阶}\ \text{的更细结构} ⚠️\ \text{（尚未找到正确形式）}$$

---

## 4. 诚实评估

| 项 | 状态 |
|---|---|
| 模论形式（$\mathcal C$ 完整版）| ✅ 手算例（$L_0\notin\mathcal C$）验证 ✓ |
| 生成器实例（$L_0\in\mathcal C$）| 🔴 **模论形式给出平凡答案**（$=n$ 或 0）✗ |
| 三个候选显式公式 | 🔴 **全部失败**（F1/F2: 0/14；F3: 1/14）✗ |
| $q_0$ 下界的**普遍证明** | 🔴 **未完成** |
| P1 Theorem 2 的独立验证 | 🔴 **未完成** |

$$\textbf{结论}：\text{D6 比预想的更微妙}。\text{生成器实例的}\ L_0\in\mathcal C\ \text{使纯"商空间/轨道"论证失效；}$$
$$\text{需要}\ \textbf{利用}\ L_0\ \text{与}\ \mathcal C\ \text{的相对位置}\ \text{（功能性指数}\ \eta\ \text{的真正含义）} ⚠️$$

**已有的严格结果**（项目，[FINAL §6.1](../FINAL.md)）：
$$\text{对生成器实例，}\textbf{严格确认}\ \text{不存在 2 行 (A)-增广} \Longrightarrow \text{最小行数}=3=\eta_1\ ✓$$
$$\text{（用子式插值，无缺口）——}\text{但只覆盖特定形状}$$

---

## 5. 下一步（明确）

| 序 | 动作 | 说明 |
|---|---|---|
| **1** ⭐ | **验证分层猜测**（§3）：在生成器实例上算 $\sum_k$ 的新维数 | 若成立 ⟹ 得到 $q_0$ 的**显式公式**（独立于 P1）|
| **2** | 若成立，**证明**它 | 纯线性代数（按轨道分层）|
| **3** | 与项目已有的"子式插值"严格结论合并 | 巩固 $q_0$ |

---

## 6. 本轮产出

| 文件 | 内容 |
|---|---|
| **本文** | D6 的模论形式 + **关键限制**（$L_0\in\mathcal C$）+ 分层猜测 |
| `scripts/core/D6_hand.py` | 手算例验证 ✓ |
| `scripts/core/D6_verify3.py` | 生成器实例的检验（暴露限制）|
| `scripts/core/D6_verify.py`、`D6_verify2.py`、`D6_debug.py`、`D6_eta.py` | 迭代过程 |
