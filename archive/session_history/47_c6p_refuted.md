# 47 — 🎉🎉🎉 **c6 / c6′ 被显式见证证伪**（本轮最重要的发现）

> 承接 [history/46](46_weakest_condition.md)。

---

## 0. 结论（一句话）

$$\boxed{\ \textbf{c6 / c6′（情形 II 平行 ⟹ NO）为假}\ ✗\qquad
\textbf{存在}\ \textbf{情形 II + 非退化平行}\ \textbf{的 YES 实例}\ ⭐⭐⭐}$$

$$\Longrightarrow\ \textbf{情形 II 不能恒 NO}\ \Longrightarrow\ \textbf{分支 A 未被排除为硬度所在}\ \checkmark$$

---

## 1. ⭐⭐ 显式见证（已用**两个独立判据**验证）

### 1.1 数据

$$n=6,\quad p=1,\quad r=2,\quad q_0=2,\quad d_{CA}=4\ (\textbf{情形 II}：4\ge 2)\ ✓$$

$$A=\begin{pmatrix}
1&-1&1&1&0&0\\
0&1&1&1&1&0\\
1&1&1&1&1&0\\
0&-1&1&0&0&0\\
0&-1&0&-1&-1&1\\
0&1&0&0&0&-1
\end{pmatrix},\quad
C=\begin{pmatrix}1&-1&1&1&0&0\end{pmatrix}$$

$$L_0=\begin{pmatrix}2&-2&2&1&0&0\\ -2&0&0&-2&0&0\end{pmatrix}\qquad(\mathcal L=L_0,\ \textbf{不需增广}：k=0)$$

（存于 `scripts/core/witness_caseII_parallel_YES.json`）

### 1.2 验证清单（**全部 ✓**）

| 项 | 内容 | 结果 |
|---|---|---|
| **H1** | $\operatorname{rank}C=p=1$ | ✅ |
| **H2** | $\operatorname{rank}L_0=r=2$ | ✅ |
| **H3** | $\operatorname{rank}[L_0;C]=3$ | ✅ |
| **H4** | $\operatorname{row}(O_{L_0})\subseteq\operatorname{row}(O_C)$ | ✅ |
| **(5a)** | $\operatorname{rank}[L_0A;L_0;CA;C]=\operatorname{rank}[L_0;CA;C]=3$ | ✅ |
| **(5b)** | $\operatorname{rank}[\lambda L_0-L_0A;CA;C]=3\ \ \forall\lambda$ | ✅ **12 个具体 $\lambda$ 逐一验证**（$\lambda=0,\pm1,\pm2,3,\pm\tfrac12,5,7,11,\tfrac13$）|
| **情形 II** | $d_{CA}=4\ge q_0=2$ | ✅ |
| **非退化平行** | $\operatorname{rank}[\pi(L_0);\pi(L_0A)]=1$ **且** $\pi(L_0)\ne0$ | ✅ |
| **T5a** | $\operatorname{rank}H=1<q_0=2$ | ✅ |

$$\Longrightarrow\ \textbf{该实例的判定问题答案（预算 }|R|=0\textbf{）为 YES}\ ✓$$

### 1.3 两个**独立**判据一致

| 判据 | 结果 |
|---|---|
| **多项式 gcd**（全部 $r_0$ 阶子式的 gcd 为常数）| ✅ (5b) 成立 |
| **逐 λ 直接算秩**（12 个有理 $\lambda$）| ✅ 全部 $=3=r_0$ |

### 1.4 ⭐⭐⭐ 完全独立实现的复核（**决定性**）

`scripts/core/verify_witness_independent.py`：
- **不 import 项目的任何库**（不用 `exact_count_thm7` / `linalg_exact`）
- 自带 Fraction Gauss 消元求秩、自带矩阵乘法、自带多项式算术、自带零空间基

| 检验 | 结果 |
|---|---|
| H1 / H2 / H3 / H4 | ✅ / ✅ / ✅ / ✅ |
| (5a) | ✅ $r_0=3=\operatorname{rank}[\mathcal LA;\mathcal L;CA;C]$ |
| **(5b) 全部 8 个 3 阶子式的 gcd** | ✅ $=\mathbf{4}$（**非零常数**，次数 0）|
| (5b) 30 个随机有理 $\lambda$ | ✅ 全部 $=r_0=3$ |
| 情形 II（$d_{CA}=4\ge q_0=2$）| ✅ |
| T5a（$\operatorname{rank}H=1<2$）| ✅ |
| 平行（$\operatorname{rank}[\pi(L_0);\pi(L_0A)]\le1$）| ✅ |
| **非退化**（$\pi(L_0)\ne0$）| ✅ |

$$\boxed{\ \textbf{13/13 全部通过}\ \Longrightarrow\ \textbf{c6 / c6′ 正式撤回（第 25 处更正）}\ }$$

---

## 2. ⚠️ 这推翻了什么 / 没推翻什么

### 2.1 ❌ 被推翻

$$\textbf{c6}：\text{情形 II 平行}\Longrightarrow\text{NO}\quad ✗$$
$$\textbf{c6}'：\text{情形 II 平行}\wedge(A)\wedge\text{T5a}\Longrightarrow(S)\ \text{失败}\quad ✗$$
$$\Longrightarrow\ \textbf{"情形 II 恒 NO"}\quad ✗$$
$$\Longrightarrow\ \textbf{"分支 A 无硬度"}\quad ✗\ \text{（分支 A 未被排除！）}$$

$$\text{项目此前 14/14 的实证}\ \textbf{全部落在退化分支}（\pi(L_0)=0）\ \text{或不变 }A\ \text{族}⚠️$$

### 2.2 ✅ 未被推翻（仍然成立）

| 项 | 状态 |
|---|---|
| **T12**（情形 II **不平行** ⟹ NO）| ✅ 仍成立 |
| **D4**（range 包含 ⟹ 分解）| ✅ Lean 已证 |
| **$(A)\iff$ 分解 $\iff$ 核条件** | ✅ Lean 已证（10 定理）|
| **c6′ 的条件式定理**（7 种形式）| ✅ **作为条件命题仍然为真**（假设可满足时不矛盾；但**假设不再覆盖全部情形**）|
| **$CA^2=0$ 时 (S) 必失败** | ✅ Lean 已证 |

$$\text{（我的 Lean 定理都是}\ \textbf{条件命题}，见证不违反它们的假设 ⟹ 无矛盾 ✓）$$

### 2.3 ⚠️ 但**没有**建立 NP-hardness

$$\text{该见证的}\ |R|=0\ \text{（不需增广）}\ \Longrightarrow\ \textbf{最小行数}=0，\text{问题"容易"}$$
$$\text{NP-hardness 需要"最小}\ |R|\ \text{很大且难判定"的实例族}\ ⚠️$$

$$\Longrightarrow\ \text{正确的表述}：\textbf{情形 II 的硬度问题重新开放}（\text{不再被 c6′ 排除）$$

---

## 3. ⭐ 由此得到的**结构性新认识**

### 3.1 非退化平行 ⟹ $k=0$（数值 3/3 + 理论）

$$\text{若}\ \pi(L_0)\ne0\ \text{且}\ \mathrm{rank}[\pi(L_0);\pi(L_0A)]\le1，\text{则（}r{=}2\text{ 时）}L_0\ \text{本身已满足 (A)}$$
$$\Longrightarrow k=0\ \text{（L0 不需增广）}\ \checkmark$$

**数值**（`c6_degenerate2.py`）：3 个非退化平行实例**全部** $k=0$ ✓
**理论**（$r=1$）：$\pi(L_0A)=c\pi(L_0)\Rightarrow L_0A-cL_0\in\operatorname{row}[C;CA]\Rightarrow L_0$ 满足 (A)

### 3.2 退化分支（$\pi(L_0)=0$）才是项目 14/14 的实际范围

$$\text{项目所有"真平行"实例（}$r{=}1$\text{）}\textbf{全部退化}：\pi(L_0)=0\ \text{—— 16/16 数值确认}✓$$
$$\text{此时"平行"判据被脚本}\ \textbf{强制设为真}\ \text{（}\texttt{pL0\_zero}\ \text{分支）}⚠️$$

$$\Longrightarrow\ \text{c6′ 的 14/14 实证}\ \textbf{只覆盖"}\pi(L_0)=0\text{"或"}$A$-不变"}\ \text{—— 不是真正的平行} ⚠️$$

---

## 4. ⭐⭐ 让我修正的方向（对主线的影响）

$$\text{原结论链}：\underbrace{\text{T12}}_{\text{不平行}\Rightarrow\text{NO}}\ +\ \underbrace{\text{c6}'}_{\text{平行}\Rightarrow\text{NO}}\ \Longrightarrow\ \text{情形 II 恒 NO}\ \Longrightarrow\ \text{分支 A 无硬度}$$
$$\text{现在}：\textbf{c6′ 假}\ \Longrightarrow\ \textbf{链条断裂}\ \Longrightarrow\ \textbf{情形 II（分支 A）重新成为硬度的候选} ⭐$$

$$\text{而}\ q_1\ \text{本身的答案仍然未定}\ ⚠️$$

---

## 5. 本轮的另一项实质成果（Lean，仍然有效）

### 5.1 c6′ 的最弱条件

$$A\text{-不变}\iff K\subseteq\ker(CA^2)\quad(K=\ker C\sqcap\ker(CA))$$
$$A(K)\subseteq\ker C\ \textbf{自动}\ ✓\ ;\quad\textbf{新定理}\ \texttt{c6'\_of\_K\_le\_ker\_CA2}\ ✓$$

### 5.2 累计资产（**45 条定理**）

$$\texttt{lake build}\ \to\ \textbf{Build completed successfully (18128 jobs)}\ ✓\ \text{零 error}$$

---

## 6. 教训（必须记录）

$$\boxed{\ \textbf{1. 判据"方向"（行/列）}\ \text{—— 本轮第 3 次踩坑}\ ⚠️}$$
$$\boxed{\ \textbf{2. "平行"判据必须}\textbf{排除退化}\ (\pi(L_0)=0)\ \text{—— 否则}\ 14/14\ \text{实证是空的}\ ⚠️⚠️}$$
$$\boxed{\ \textbf{3. (S) 只是 (5b) 的必要条件 —— 必须直接测 (5b)}\ ⚠️⚠️⚠️}$$
$$\boxed{\ \textbf{4. 问题的 (5b) 量词是}\ \lambda\in\mathbb C\ \text{—— }\textbf{代数闭域}}\ \text{（我此前猜对 ✓）}$$

$$\text{第 3 条最危险：我差点因 (S) 成立就宣布"发现 YES"}$$
$$\text{—— 但 (S) 只蕴含 (5b) 在 }H\text{ 上的约化，必须直接验证 (5b) 才可靠 ✓}$$

---

## 7. 下一步

| 序 | 动作 | 说明 |
|---|---|---|
| **1** ⭐ | **形式化该见证**（Lean 或可计算的验证脚本 + 独立复核）| 若成立 ⟹ c6′ 正式撤回 |
| **2** ⭐⭐ | 更新 **FINAL.md** 的 c6′ 条目（从"猜想"改为"**已被证伪**"）| 必须做 |
| **3** | 重新评估 **分支 A 的硬度候选**（这是主线的核心问题）| |
| **4** | 查清"非退化平行 ⟹ $k=0$"是否是**定理**（对 $r\ge2$ 也成立？）| |

---

## 8. 本轮产出

| 文件 | 内容 |
|---|---|
| **`scripts/core/witness_caseII_parallel_YES.json`** ★⭐⭐ | **显式见证** |
| **`scripts/core/c6_witness.py`** ★⭐ | 见证提取 + 独立验证 |
| `scripts/core/c6_5b.py` | 直接检验 (5a)∧(5b) |
| `scripts/core/c6_degenerate.py`、`c6_degenerate2.py` | 退化性 + $k=0$ 的确认 |
| `scripts/core/c6_CRUX.py` | (S) 检验（后证明不足）|
| `scripts/core/c6_general_A.py` | 一般 $A$ 的构造尝试 |
| `MyProof/Theorems/C6Mech.lean` | c6′ 最弱条件（Lean，仍有效）|
