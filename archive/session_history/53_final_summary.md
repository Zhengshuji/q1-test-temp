> # 🔴 **本文档已过时（2026-10-19）**
> $$\rho\ge\mathrm{obs}\ \textbf{已被反例推翻}\ \Longrightarrow\ |R|_{\min}=\mathrm{obs}+1-r\ \text{与}\ \textbf{"q1 为假"}\ \text{均已撤回}$$
> $$\textbf{仍然成立}：\text{判据（两侧）}、\text{可行性}\in\mathrm{P}、\text{A19}\ (\rho\le\mathrm{obs})$$
> 最新状态见 [`history/52`](52_session_conclusion.md) §7.101–7.104 与 [`OPEN_PROBLEM.md`](../OPEN_PROBLEM.md)。
# 53 — 本会话最终汇总（可导航版）

> 本文件是 [`history/52_session_conclusion.md`](52_session_conclusion.md)（1400+ 行）的**浓缩导航版**。
> 完整推导在 52；本文件只给结论 + 证据 + 状态。

---

## 一、问题与化简

**问题（q1）**：给定 LTI $(A,C,L_0)$ 与预算 $q$，是否存在 $|R|{=}q$ 使 (5a)∧(5b)？

**六步化简链**（每步都可一键复现）：

| 步 | 内容 | 验证 |
|---|---|---|
| 1 | $(A)\iff$ 分解 $\iff\ker\Theta\le\ker(\mathcal LA)$ | **Lean 45 定理** |
| 2 | $(5a)\iff\ker H\subseteq\ker F$（$H=\mathcal LN$, $F=\mathcal LAN$）| `verify_equivalences` E1 **400/400** |
| 3 | $(5b)\iff(S)$（$\operatorname{rank}(\lambda H-F)\equiv\operatorname{rank}H$）| E2 **400/400**（另有 5998/5998）|
| 4 | $(5b)\iff\operatorname{rank}(\mathcal LP_\lambda)\equiv\operatorname{rank}(\mathcal LN)$，$P_\lambda=\lambda N-AN$ | E3 **400/400** |
| 5 | $(5a)\iff$ 几何避让 $\mathcal M\cap(\{0\}\times\mathbb{R}^q)=0$ | E4 **400/400** |
| 6 | 一切只依赖 $(\mathcal LN,\ \mathcal LAN)$ | — |

$$\textbf{最终判定表述（无}\ \Lambda\textbf{）}：\text{找}\ \mathcal L\supseteq L_0\ \text{使}\ \ker(\mathcal LN)\subseteq\ker(\mathcal LAN)\ \wedge\ \operatorname{rank}(\mathcal LP_\lambda)\equiv\operatorname{rank}(\mathcal LN)$$

---

## 二、核心结果（按可靠性排序）

### A. 严格已证（Lean）

| 定理 | 内容 |
|---|---|
| `decomp_iff_rank` / `decomp_iff_ker` | $(A)\iff$ 分解 $\iff$ 核条件 |
| `c6'_of_K_le_ker_CA2` | $K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| `c6'_CA2_algclosed` | $CA^2{=}0$ 时 c6′（条件式）|
| `S_fails_of_comp_eq_zero` 等 | (S) 失败的组装 |
| **共 45 条**，`lake build` **18128 jobs，零 error** | |

### B. 严格已证（非 Lean）

| 结果 | 内容 |
|---|---|
| 引理 | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| 秩半连续性 | $(\text{5b})\Rightarrow\rho=\operatorname{rank}A_0$ |
| 充分性 | $\alpha_0\in V\Rightarrow$ **YES**（构造 $A_0{=}I$ + pole placement）|

### C. 严格枚举

| 实例 | 域 | 结果 |
|---|---|---|
| **c19**（$d{=}3$）| $\{-1,0,1\}^{12}$ = 531,441 | **无解** |
| t=7（$d{=}3$）| 同上 | **16,848 解，全 $\rho{=}2$** |
| 5 个定向构造（$d{=}2$）| 各 $\{-1,0,1\}^6$ = 729 | **全部无解** |
| n=4 t=0/5 等 | 各 729 | 456 / 80 解 |

### D. 定律与判据（实证）

$$\boxed{\ \textbf{定律}：\operatorname{rank}(\text{解})=\text{obs}=\dim\big\langle\operatorname{row}R\big\rangle_{A'}\qquad(4/4\ \text{完全枚举})\ }$$

$$\boxed{\ \textbf{判据}：\textbf{YES at}\ q{=}d_{CA}{+}1\iff\alpha_0=L_0N\in V=\big\langle\operatorname{row}R\big\rangle_{A'}\ }$$

$$A'=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN,\qquad R=AN-NA'$$

---

## 三、判据的两侧状态

| 侧 | 状态 | 依据 |
|---|---|---|
| **充分**（$\alpha_0\in V\Rightarrow$YES）| ✅ **已证** | 归约到 $V$（obs$'{=}d'$）+ $A_0{=}I$ 构造 + pole placement |
| **必要**（$\alpha_0\notin V\Rightarrow$NO）| ✅ 机制找到；⚠️ 证明依赖定律 | 7 实例（6 穷尽）全 NO；障碍在 **(5a)** |

**必要性机制**（3/3 分层验证）：

$$\text{解必须}\ \rho=\text{obs}\ \Longrightarrow\ \operatorname{rank}A_0=\text{obs}$$
$$(\text{5a})\Rightarrow A_1=\Lambda A_0\Rightarrow\gamma_0\in\operatorname{row}(A_0)=U$$
$$\gamma_0=\alpha_0A'+\beta_0,\ \beta_0\in\operatorname{row}R\subseteq V\ ;\ \alpha_0\notin V$$
$$\Longrightarrow\ \bar\gamma_0=\bar\alpha_0\bar A'\ne0\ \text{而}\ \dim U=\dim V\ \text{容纳不下}\ \Longrightarrow\ \textbf{无解}$$

**关键诊断数据**：

| 实例 | $\operatorname{rank}(A_0)=$obs | $\operatorname{rank}(A_0)>$obs |
|---|---|---|
| trial 0/1/7 | **过 (5a) 0%** | 过 (5a) **100%**（但 (5b) 全败）|

---

## 四、已证伪的清单（**15 个判据**）

$$\text{不变性、}m{-}d\text{、}\mathrm{rank}(AN){<}d\text{、}\rho_0\text{、row 包含、铅笔特征值、}$$
$$A'\ \text{有理谱、}A'\ \text{实谱、obs 充要性、obs 强形式、加行单调、H2（基行平行）、}$$
$$\text{合成判据、obs}{<}d{\Rightarrow}\text{NO、必要性机制（商的谱）}$$

另有：**c6/c6′ 被证伪**（可手算的无穷族，$n\ge4$）；"情形 II 恒 NO"、"判定平凡"均被证伪。

---

## 五、两个待证点（唯一剩余）

| # | 待证 | 现状 |
|---|---|---|
| **1** | **定律** $\operatorname{rank}(\text{解})=\text{obs}$ | 4/4 完全枚举支持 |
| **2** | **必要性**（$\alpha_0\notin V\Rightarrow$NO）| 机制已找到，证明依赖定律 |

$$\Longrightarrow\ \textbf{若两点严格化}\ \Longrightarrow\ \textbf{判定多项式}\ \Longrightarrow\ \textbf{q1 为假（NP-hardness 不成立）}$$

---

## 六、一键复现

```
python scripts/core/verify_all.py            # A/B/C 全过
python scripts/core/verify_equivalences.py   # E1–E4 各 400/400
```

关键脚本（按主题）：

| 主题 | 脚本 |
|---|---|
| 等价关系 | `verify_equivalences.py`、`c6_ker_criterion.py`、`c6_S_iff_5b.py`、`c6_lambda_free.py`、`c10_final_form.py` |
| 见证 / 无穷族 | `verify_witness_independent.py`、`verify_witness2_independent.py`、`verify_family.py` |
| 判据搜索 | `c13`–`c23`（8 个被否）|
| **定律 / 判据** | `c25`、`c26`、`c27`、`c31`、`c36`、`c37`、`c39`、`c42`、`c43`、`c44` |
| 枚举 | `c19_typeII_exhaustive.py`、`c28_thin_instance.py`、`c35_n5t7_enumerate.py` |
| 反驳 | `c40_quotient_spec.py`（必要性机制）|

---

## 七、本会话的 29 处更正（**必须与结论一并引用**）

$$\textbf{19 处是猜想/判据/表述被自己的数据推翻}\ ;\qquad \textbf{0 处是 Lean 级已证结论被推翻}\ \checkmark$$

**最重要的四处**：

| # | 内容 |
|---|---|
| 25 | 必要性机制"商的谱"被反驳（c19 与 t=1 的 $\bar A'$ 都无有理特征值）|
| 26 | **"23/23" 是误导的** —— obs$=d$ 的实例只测充分性；真正测必要性的原仅 2 个 |
| 27 | 定向构造使必要性证据从 2 个增至 7 个（6 穷尽）|
| **29** | **"(5b) 的新等价形式" $\forall y:\ y^{\mathsf T}A_1\not\parallel y^{\mathsf T}A_0$ 是错的** |

**第 29 处的教训**：$\dim\ker((\lambda A_0-A_1)^{\mathsf T})=q-\rho>0$ 对 generic λ **总成立** ⟹
"$\exists y$" 是**平凡条件**；(5b) 失败需要**左零空间维数上跳**（多个独立 $y$）✓

---

## 八、结论一句话

$$\boxed{\
\begin{array}{l}
\textbf{q1 仍未定。}\\
\text{会话把判定问题化简到}\ 2d\ \text{维，证明了充分性（构造 + pole placement），}\\
\text{找到了必要性机制（障碍在 (5a)），把必要条件精确到}\ \alpha_0\in\langle\operatorname{row}R\rangle_{A'}，\\
\text{并用 6 个穷尽枚举 + 45 条 Lean 定理作了交叉验证。}\\
\textbf{剩两个待证点}：定律 \operatorname{rank}(\text{解})=\text{obs}，与必要性的严格证明。
\end{array}}$$
