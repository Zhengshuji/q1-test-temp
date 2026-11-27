# 48 — ⭐ 证伪的**精确范围**：非退化平行 ⟹ $k=0$（定理）

> 承接 [history/47](47_c6p_refuted.md)。本文**精确界定** c6′ 证伪的影响范围。

---

## 0. 一句话

$$\boxed{\ \textbf{定理}：\text{非退化平行}\ \Longrightarrow\ (A)\ \text{对}\ L_0\ \text{成立}\ \Longrightarrow\ q_0=r,\ \mathbf{k=0}}$$
$$\boxed{\ \Longrightarrow\ \text{在}\ k\ge1\ \text{范围（硬度相关），平行}\ \Longrightarrow\ \text{必然}\ \textbf{退化}\ (\pi(L_0)=0)\ }$$

$$\Longrightarrow\ \textbf{history/47 的证伪}\ \textbf{只影响}\ k=0\ \text{；}\ c6'\ \text{在}\ k\ge1\ \text{范围仍}\ \textbf{开放}$$

---

## 1. ⭐ 定理与证明（**干净，无需不变性**）

### 1.1 陈述

$$\text{设}\ \operatorname{rank}[\pi(L_0);\pi(L_0A)]\le 1\ \text{且}\ \pi(L_0)\ne0\quad(\pi(x)=0\iff x\in\operatorname{row}[C;CA])$$
$$\text{则}\ L_0\ \text{本身满足}\ (A)：\exists\Lambda\in\mathbb R^{r\times r},\ G_0,G_1,\ \ L_0A=\Lambda L_0+G_0C+G_1CA$$

### 1.2 证明（三步）

$$\textbf{(i)}\ \text{约化}：\ (A)\ \text{对}\ L_0\iff\exists\Lambda,\ \pi(L_0A)=\Lambda\,\pi(L_0)$$
$$\text{（模}\ \operatorname{row}[C;CA]\ \text{约化；反之}\ \mu:=L_0A-\Lambda L_0\ \text{满足}\ \pi(\mu)=0，$$
$$\text{故}\ \mu=G_0C+G_1CA\ \text{—— 因}\ \operatorname{row}[C;CA]\ \text{恰由}\ C,CA\ \text{的行张成}\ ✓）$$

$$\textbf{(ii)}\ \text{平行结构}：\ \operatorname{rank}[\pi(L_0);\pi(L_0A)]\le1\ \Longrightarrow\ \pi(L_0)=c\,u^{\mathsf T},\ \ \pi(L_0A)=d\,u^{\mathsf T}$$
$$\text{（}c,d\in\mathbb R^r,\ u\in\mathbb R^d\ \text{列向量；非退化}\iff c\ne0,\ u\ne0\text{）}$$

$$\textbf{(iii)}\ \text{可解性}：\ \Lambda(cu^{\mathsf T})=du^{\mathsf T}\iff\Lambda c=d$$
$$\Longrightarrow\ \textbf{对任意}\ d\ \text{总是可解}\ (\text{未知}\ r^2\ \text{个、方程}\ r\ \text{个}) \checkmark$$

$$\Longrightarrow\ (A)\ \text{成立}\ \Longrightarrow\ q_0\le r\ \Longrightarrow\ q_0=r\ \Longrightarrow\ \boxed{k=0}\ \checkmark$$

### 1.3 ⚠️ 关键的**对照**（为什么 $r{=}2$ 不救场）

$$\text{我一度以为}：r\ge2\ \text{时} d\not\parallel c\ \text{可使 (A) 失败}$$
$$\textbf{错}\ ✗：\Lambda\ \text{是}\ r\times r\ (\text{不止标量})，\Lambda c=d\ \text{对任意}\ d\ \textbf{总可解}$$

$$\textbf{真正的分界是"退化"而非"}\ r\text{"}：$$
$$\pi(L_0)=0\ \text{且}\ \pi(L_0A)\ne0\ \Longrightarrow\ \Lambda\cdot0=0\ne d\ \Longrightarrow\ (A)\ \textbf{失败}\ \Longrightarrow\ k\ge1\ \checkmark$$

---

## 2. 数值确认

### 2.1 非退化平行 ⟹ $k=0$（6/6，本轮到 6 个后停止）

```
trial   n  r  q0  非退化  平行  (A)对L0   k
333     6  2   2    ✓     ✓      是      0
1919    6  2   2    ✓     ✓      是      0
1964    6  2   2    ✓     ✓      是      0
2329    6  2   2    ✓     ✓      是      0
7364    6  2   2    ✓     ✓      是      0
7461    6  2   2    ✓     ✓      是      0
```

$$\Longrightarrow\ \textbf{非退化平行且}\ k\ne0\ \text{的实例：0 个}\ ✓\ \text{（定理成立）}$$

### 2.2 与项目 14/14 证据的一致性

$$\text{项目所有"真平行"实例（}r{=}1\text{）}\textbf{全部退化}（16/16）\ \text{—— 与定理完全一致}\ ✓$$
$$\text{且它们的}\ k\ge1\ \text{（}q_0=2,3,4\text{）}\ \text{—— 正是"退化 + }k\ge1\text{"的情形}\ ✓$$
$$\Longrightarrow\ \textbf{项目 14/14 的证据}\ \textbf{不是空的}，\text{但只覆盖}\ \textbf{退化分支}\ ✓$$

---

## 3. ⭐ 精确的最终结论（c6′ 状态）

$$\boxed{
\begin{array}{ll}
\textbf{(1)} & \text{非退化平行}\ (k{=}0)\ \text{时：}\ \textbf{c6′ 假}\ \text{（history/47 的见证）}\ ✗\\[2pt]
\textbf{(2)} & k\ge1\ \text{时：平行}\Longrightarrow\pi(L_0)=0\ (\textbf{退化})\ \text{—— c6′ 只涉及退化分支}\\
\textbf{(3)} & \text{退化分支（}\pi(L_0)=0\text{）的 c6′：}\ \textbf{未证也未被证伪}\ \text{（开放）}\ ⚠️
\end{array}}$$

$$\Longrightarrow\ \text{"情形 II 恒 NO"}\ \textbf{作为一般陈述为假}\ (\text{因 (1)})\ ;$$
$$\text{但}\ \textbf{在}\ k\ge1\ \text{的硬度相关范围}\ \text{它}\ \textbf{仍未被推翻} ⚠️$$

---

## 4. 对项目的净影响

### 4.1 ⚠️ 必须修正的

| 原主张 | 修正 |
|---|---|
| "情形 II 恒 NO ⟹ 分支 A 无硬度" | 🔴 **作为一般陈述为假**（$k{=}0$ 反例）|
| "c6′ 是猜想，14/14 支持" | 🔴 **$k{=}0$ 时为假**；$k\ge1$ 时**仍开放** |

### 4.2 ✅ 仍然成立 / 变得更清楚的

| 项 | 状态 |
|---|---|
| **T12**（不平行 ⟹ NO）| ✅ 成立 |
| **$(A)\iff$分解$\iff$核条件** | ✅ Lean 已证 |
| **$CA^2{=}0$ 时 (S) 必失败** | ✅ Lean 已证（条件命题）|
| **非退化平行 ⟹ $k=0$** | ✅ **定理**（本轮）|
| **$k\ge1$ + 平行 ⟹ 退化** | ✅ 推论 |
| 项目的 14/14 实证 | ✅ **不空**，覆盖退化分支 |

### 4.3 🔴 新的开放问题（更精确！）

$$\textbf{在退化分支}\ (\pi(L_0)=0,\ k\ge1)：\text{情形 II 平行}\Longrightarrow\text{NO}\ \text{是否成立？}$$
$$\text{—— 这是}\ q_1\ \text{硬度的}\ \textbf{真正所在}\ ⚠️$$

$$\text{而}\ k=0\ \text{的情形：}\ \textbf{最小}\ |R|=0，\text{对 NP-hardness 无直接贡献}\ ✓$$

---

## 5. 教训

$$\boxed{\ \textbf{线性代数层的"自由度计数"要先做}\ ——\ \text{我误以为}\ r{=}2\ \text{时}\ \Lambda\ \text{是标量}\ ✗}$$
$$\Lambda\ \text{是}\ r\times r，\Lambda c=d\ \text{有}\ r^2-1\ \text{个自由参数}\ \Longrightarrow\ \textbf{总可解}$$
$$\text{这正是项目历来的教训类型（"判据/对象的阶数要数清"）} ⚠️$$

---

## 6. 本轮产出

| 文件 | 内容 |
|---|---|
| **本文** | 证伪的**精确范围** + 定理"非退化平行 ⟹ $k=0$" |
| `scripts/core/c6_theorem_k0.py` | 定理的数值验证（6/6）|
| `scripts/core/c6_k_ge1b.py` | "非退化平行 + $k\ge1$"的构造尝试（发现不可能 ⟹ 符合定理）|
| `scripts/core/verify_witness_independent.py` | 见证的独立复核（13/13，见 [47](47_c6p_refuted.md)）|
| `scripts/core/witness_caseII_parallel_YES.json` | 见证 |
| `scripts/core/c6_degenerate_5b.py` | 退化分支（非不变 $A$）的 (5b) 测试 |

---

## 7. 退化分支（$\pi(L_0)=0$，$k\ge1$）的测试结果

### 7.1 ⭐ 一个重要的**判据澄清**

$$\text{项目的 14/14 证据用的是 }(S)\ ;\quad (5b)\Rightarrow(S)\ \Longrightarrow\ \neg(S)\Rightarrow\neg(5b)\ ✓$$
$$\Longrightarrow\ \textbf{项目 14/14 的证据对 (5b) 是有效的}\ \checkmark\ \text{（不空）}$$

$$\text{（我此前担心"只测 (S) 不算"—— 但只在}\ \textbf{反方向}\ \text{不成立：}(S)\ \not\Rightarrow\ (5b)）$$

### 7.2 退化 + **非不变** $A$ 的测试（`c6_degenerate_5b.py`）

| 项 | 结果 |
|---|---|
| 实例数 | **12**（$n{=}6,p{=}1$，$\pi(L_0){=}0$，**非** $A$-不变，情形 II）|
| $L_0$ 本身的 (5a) | 全部**失败**（符合 $k\ge1$）|
| $L_0$ 本身的 (5b) | 全部 ✓（退化时铅笔部分自动常秩）|
| **找到** $R$（120 次随机）使 (5a)∧(5b) | **0** |

### 7.3 ⚠️ 诚实标注：**这个测试不是决定性的**

$$\text{随机搜索}\ R\ \text{是}\ \textbf{弱方法}\ ——\ (A)\ \text{的可行集是}\ \textbf{代数集（零测）} ⚠️$$
$$\text{项目自己的禁区："用随机方向验证}\ \Longrightarrow\ \text{采样必错过"}$$

$$\Longrightarrow\ \textbf{结论}：\text{退化分支的 c6′}\ \textbf{既未证、也未找到反例}\ —— \textbf{仍开放}$$

$$\text{严格路线（未做）}：\text{套用}\ \texttt{attack\_chart\_rigorous.py}\ \text{的}\ \textbf{子式插值}，$$
$$\text{证明"不存在}\ q_0\ \text{行的 (A)∧(5b) 增广"}$$

---

## 8. 本轮结束时的**精确状态**

| 分支 | c6′ 状态 | 依据 |
|---|---|---|
| **非退化平行**（$\pi(L_0)\ne0$）| 🔴 **假** | 见证（13/13 独立复核）；且此时 $k{=}0$ |
| **退化**（$\pi(L_0)=0$）+ 不变 $A$ | ⚠️ **14/14 支持**（未证）| 项目已有证据（对 (5b) 有效）|
| **退化** + 非不变 $A$ | ⚠️ **12/12 未找到反例**（弱证据）| 本轮（随机搜索，不决定性）|

$$\textbf{当前唯一的开放问题}：\text{退化分支}（\pi(L_0)=0,\ k\ge1）\ \text{的 c6′}$$
$$\text{—— 这是}\ q_1\ \text{硬度的}\ \textbf{真正所在}\ ⚠️$$
