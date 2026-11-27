# 32 — 主线重大进展：**支 B 上 $(A)\wedge(S)$ 可为 YES**（附独立核验）

> 承接 [history/31](31_back_to_mainline.md)。本文给出**可复现的见证**，
> 推翻"支 B 恒空"的假设，**重新确立支 B 为硬度候选**。

---

## 0. 一句话

$$\boxed{\ \textbf{支 B}\ (2p+q_0<n)\ \textbf{上}\ (A)\wedge(S)\ \textbf{可为 YES}\ \Longrightarrow\ \nu_{\min}=q_0\ \Longrightarrow\ \text{支 B 是硬度候选}\ }$$

---

## 1. 见证（`scripts/core/mainline_witness2.py`，已存 `witness_branchB.json`）

$$n=6,\ p=1,\ r=1,\ q_0=3,\ k=2,\qquad 2p+q_0=5<6\ \checkmark\ \text{（支 B）}$$

$$A=\begin{bmatrix}1&0&1&0&1&0\\0&0&-1&-1&-1&0\\-1&1&0&1&1&-1\\0&-1&0&0&-1&-1\\1&1&1&-1&0&0\\1&-1&-1&-1&0&1\end{bmatrix},\quad
C=\begin{bmatrix}0&-1&0&0&-1&1\end{bmatrix},\quad
L_0=\begin{bmatrix}0&-2&-1&1&1&1\end{bmatrix}$$

$$\mathcal L=\begin{bmatrix}L_0\\R\end{bmatrix}=\begin{bmatrix}0&-2&-1&1&1&1\\-2&-3&-5&-2&-6&0\\5&3&8&0&5&0\end{bmatrix}\qquad(k=2\ \text{行增广})$$

### 1.1 独立核验（四条判据，全部 ✓）

| 判据 | 结果 |
|---|---|
| 支 B：$2p+q_0=5<n=6$ | ✓ |
| $(A)$（**4 块**秩条件 $\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]$）| **True** |
| $(A)$ 的分解：$\Lambda H=F$（$H=\mathcal L N_{CA}$，$F=\mathcal L A N_{CA}$）| **True** |
| $(S)$（$\rho$ 阶子式 gcd 判据）| **True** |

$$H=\begin{bmatrix}0&0&0&0\\-2&-7&-18&2\\5&8&26&-5\end{bmatrix},\quad \operatorname{rank}H=\rho=2,\quad
\Lambda=\begin{bmatrix}1&1&1\\2&-1&-1\\-2&-1&0\end{bmatrix}$$

$$\Longrightarrow\ \nu_{\min}\le 3=q_0\ \text{且}\ q_0\ \text{是下界}\ \Longrightarrow\ \boxed{\nu_{\min}=q_0}\ ✓$$

---

## 2. ⚠️ 我上一轮的"0 成立"是**错的**（第 3 处 B2 相关更正）

`scripts/core/mainline_B2.py` 报"（A）-点 464 ；(S) 成立 0"，
`mainline_claim.py` 的某些行也报 "(S) 0"。**原因**：

$$\text{那两个循环里}\ \texttt{max\_l}\ \text{耗尽后}，\textbf{只测了每个形状的第一个实例}\ ✗$$

而"第一个实例"恰好是 $(A)\wedge(S)$ 空的。**换了实例就有见证**。

$$\textbf{教训（与前一课同源）}：\text{"某实例上未找到"}\ \ne\ \text{"不存在"}；\ \textbf{必须报出样本量}\ \checkmark$$

---

## 3. 这对主线意味着什么（重新评估）

### 3.1 支 B 的地位（**从"已排除"回到"候选"**）

| | 旧认识（[FINAL §8](../FINAL.md)）| 本轮更正 |
|---|---|---|
| 支 B 解集 | "有限孤立点" | $k=1$：单点；$k\ge2$：**正维数零测集** |
| "解数不随规模增长" | ⟹ 非硬度源 | ⚠️ **口径未定**（数的是什么？）|
| $(A)\wedge(S)$ 是否可空 | —— | ✅ **可非空（有见证）** |
| **支 B 是否硬度候选** | ❌（据上）| ⚠️ **是**（重新开放）|

### 3.2 问题回到最本质的形式

$$\textbf{支 B 的判定问题}:\quad \exists\,\Theta\in\mathbb{R}^{k(s-k)}:\ (A)\wedge(S)\ \text{在}\ W_J(\Theta)\ \text{处成立}\ ?$$

$$\text{这是}\ \textbf{实代数存在性问题（ETR 型）}：\text{约束是}\ (\rho{+}1)\ \text{阶子式}=0\ (\text{次数}\le2)\ +\ (S)\ \text{条件}$$

$$\text{变量数}\ m=k(s-k)\ \text{多项式于}\ n$$

### 3.3 两个方向的判据（明确）

| 要证 | 需要 |
|---|---|
| **q1 是 NP-hard** | 把某个 NP-hard 问题**归约**到"$\exists\Theta$" —— 支 B 或情形 II |
| **q1 不是 NP-hard** | 给出多项式算法（或证明结构足够特殊）|

---

## 4. 下一步（优先序）

| 序 | 动作 | 为什么 |
|---|---|---|
| **1** | **把上述见证做成可复现的独立脚本**（不依赖随机搜索）| 供他人核验 ✓ **已做**（`witness_branchB.json`）|
| **2** | **量化**：支 B 上"$(A)\wedge(S)$ 非空"的实例**频率**（大样本）| 判断是"罕见"还是"常见" |
| **3** | **找模式**：见证的 $\mathcal L$ 有何结构？（如 $\Lambda$ 的特征值、$H$ 的像）| 可能揭示构造法 |
| **4** | **若频率高且有结构** ⟹ 尝试**归约**（编码 SAT / 子集选择）| 证 NP-hard |
| **5** | **若频率低且无结构** ⟹ 支 B 可能只是"罕见可满足"⟹ 复杂度仍开放 | 继续观察 |

---

## 5. 诚实评估

$$\text{本轮把主线的状态从"支 B 已排除、只剩情形 II"改回"支 B 与情形 II \textbf{都是候选}"}\ ⚠️$$

**但**：找到**一个**见证 $\ne$ 支 B 难。它只说明：
- 支 B 的判定**不是平凡的"恒 NO"** ✓
- 存在"YES"实例 ⟹ 若判定是多项式的，也要能处理这些 ✓

$$\Longrightarrow\ \textbf{支 B 的复杂度真正回到\textbf{未知}}\ \text{——但这次有正确的依据}\ ✓$$

---

## 6. 本轮新增脚本

| 脚本 | 用途 |
|---|---|
| **`scripts/core/mainline_witness2.py`** | ⭐ **找到并核验支 B 的 (A)∧(S) 见证**（可复现）|
| `scripts/core/witness_branchB.json` | 见证的完整数据（A, C, L0, L, Λ, H）|
| `scripts/core/mainline_S_sanity.py` | $(S)$ 检验器的健全性检查（3 个人工例 ✓）|
| `scripts/core/mainline_B2.py`、`mainline_claim.py` | ⚠️ **含"样本量不足"缺陷**（`max_l` 耗尽）——保留作反面教材 |
| `scripts/core/mainline_verify_witness.py`、`mainline_witness_pin.py` | 复现失败的中间尝试 |
