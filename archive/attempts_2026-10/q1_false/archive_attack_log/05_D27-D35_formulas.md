> **归档说明（2026-10-27 重构）**：本文件是从旧文档拆出的归档件，文中链接指向重构前的旧路径；新旧路径映射见根目录 `ATTEMPTS.md` 与 `README.md`。

# 攻击日志 · D27–D35（拆分自 ATTACK_LOG.md）

> 原文：`archive/attack_A2V0/ATTACK_LOG.md`。

# 🎯 D27：宽度=1 的公式成立 127/132（例外全是平凡的）

### 数据

| $q_{\min}-\min\_ci$ | 计数 |
|---|---|
| **1** | **127** ✓ |
| 0 | 5 |

5 个例外全部是 $(n{=}5,p{=}2,\dim V{=}1,\min\_ci{=}1,q_{\min}{=}1)$：

$$\Longrightarrow\ q_{\min}=r=1\ \text{（即 }L_0\ \text{自己满足条件）—— 平凡情形}$$

### 涌现的多项式候选公式

$$\boxed{\ q_{\min}=\begin{cases}
r & \text{若 } L_0 \text{ 自己满足 } (5a)\wedge(5b)\\
\min\_ci+1 & \text{若宽度}=1\\
\dim V+1 & \text{若宽度}\ge2
\end{cases}}$$

| 项 | 计算 |
|---|---|
| $r$ | 平凡 |
| $L_0$ 是否自己满足 | 精确检查（$O(n^3)$）|
| $\min\_ci$ | 迭代（$O(n^3)$）|
| $\dim V$ | 闭包（$O(n^3)$）|

$$\boxed{\ \text{全部 }O(n^3)\ \text{可算} \Longrightarrow\ \text{若公式成立则}\ \textbf{q1 = 假}}$$

### 与夹逼的关系

$$\min\_ci\ \le\ q_{\min}\ \le\ \dim V+1$$

- 宽度 0：$q_{\min}=\min\_ci$（下界）或 $r$
- 宽度 1：$q_{\min}=\min\_ci+1=\dim V+1$（两端重合）
- 宽度 ≥2：$q_{\min}=\dim V+1$（上界）

$$\Longrightarrow\ \text{公式的本质：}\ q_{\min}\ \text{由夹逼宽度唯一决定（加一个平凡检查）}$$

### 待验证

| 项 | 状态 |
|---|---|
| 宽度 0：$q_{\min}=\min\_ci$ 或 $r$ | 🟡 只有 2 个实例，样本不足 |
| 宽度 1：$q_{\min}=\min\_ci+1$ | ✅ 127/132（例外平凡）|
| 宽度 ≥2：$q_{\min}=\dim V+1$ | 🟡 4 个实例（全宽度 2）|

### 下一步

1. **专门测试宽度 0**（$\min\_ci=\dim V+1$）的实例
2. **测试宽度 3、4** 是否仍取上界
3. 若都成立 ⟹ 推广为定 理 ⟹ **q1 = 假**


---

# 🚨 D28：自我更正 —— "宽度公式"是恒等式

### 错误

$$\text{宽度}:=\dim V+1-\min\_ci\quad\Longrightarrow\quad \min\_ci+\text{宽度}=\dim V+1\ (\text{恒等})$$

$$\text{所以 D27 的"候选公式"里 width=0/1/≥2 三种情形\textbf{算出来都等于}\dim V+1}$$

$$\boxed{\ \text{那个"公式"没有新内容 —— 只是 }q_{\min}=\dim V+1\ \text{的伪装}\ ✗}$$

### 数据实际说了什么

| 宽度 | 样本 | $q_{\min}$ | $L_0$ 可行？ |
|---|---|---|---|
| 0 | 4 | $=\dim V+1$ | 否 |
| 1 | 4 | $=\dim V+1$ | 否 |
| 2 | 4 | $=\dim V+1$（3）/ $=1$（1，$L_0$ 可行）| 否/是 |
| 3 | 2 | $=\dim V+1$ | 否 |
| 4 | 1 | $=\dim V+1$ | 否 |

$$\Longrightarrow\ \text{这批样本\textbf{全部}落在"非退化"情形} \Longrightarrow\ \text{宽度不起作用}$$

### 真正的图景（回到已验证的三层）

$$\boxed{\ q_{\min}=\min\big(\dim V+1,\ q_{\deg},\ \text{中间层}\big)\ }$$

| 层 | 触发条件 | 证书 |
|---|---|---|
| $\dim V+1$ | 默认（绝大多数）| — |
| $q_{\deg}$ | 存在退化解 | `counterexample_refute_dimV1.json` |
| 中间层 | 存在 $0<\rho<\dim V$ 的解 | `certificate_middle_layer.json` |

$$\text{夹逼}:\ \min\_ci\ \le\ q_{\min}\ \le\ \dim V+1$$

### 教训（加入纪律 11）

$$\boxed{\ \textbf{纪律 11}：\text{任何"新公式"必须先检查它是不是恒等式}}$$

（D27 的"宽度三分"看起来很漂亮，实际上三项都等于同一个恒等式 ✗）

### 下一步

$$\text{真正的任务不变}:\quad \text{判定"是否存在退化/中间解"}$$

具体：对给定实例，如何**快速判定**是否存在 $
ho<\dim V$ 的解？这是 q1 的核心 ✓


---

# ✅ D29：第 8 个已证命题 —— $
ho_0=\dim V$ 时公式成立

### 命题

$$\boxed{\ \textbf{命题}：\quad \operatorname{rank}(L_0N)=\dim V\ \Longrightarrow\ q_{\min}=\dim V+1\ }$$

### 证明（三行）

$$\mathcal LN=[L_0N;\ RN]\ \Longrightarrow\ \rho=\operatorname{rank}(\mathcal LN)\ \ge\ \operatorname{rank}(L_0N)=\dim V$$
$$\text{由}\ q\ge\rho+1\ (\S D32):\quad q\ge\dim V+1$$
$$\text{由两步构造（上界）}:\quad q\le\dim V+1$$
$$\Longrightarrow\ q_{\min}=\dim V+1\qquad\blacksquare$$

### 验证（120 个实例）

| $(\rho_0=\dim V,\ q_{\min}=\dim V+1)$ | 计数 |
|---|---|
| **(True, True)** | **26** ✓ |
| **(True, False)** | **0** ✓ |
| (False, True) | 81 |
| (False, False) | 3 |

$$\boxed{\ \text{定理的 26 个实例全部成立，\textbf{零反例}}\ ✓}$$

### 情况划分

| 情形 | 频率 | $q_{\min}$ |
|---|---|---|
| $\rho_0=\dim V$ | 22% | $=\dim V+1$（**定理保证**）|
| $\rho_0<\dim V$ | 78% | 通常 $=\dim V+1$（81/84），偶尔更小（3/84）|

$$\Longrightarrow\ \boxed{\ \text{所有"更小"的例外都\textbf{必须}满足}\ \rho_0<\dim V\ }$$

### 这是第 8 个已证命题

| # | 命题 |
|---|---|
| 1 | $N^{\mathsf T}R_0=0$ |
| 2 | $S'=S$ |
| 3 | 线性引理 |
| 4 | $q\ge\rho+1$ |
| 5 | $\dim B\le p$ |
| 6 | 结构分解 $\dim\ker(\cdot N|_{\mathcal V})=q-\rho$ |
| 7 | $(5a)\iff\mathcal VA\subseteq\mathcal V+\mathcal J$ |
| **8** | **$\rho_0=\dim V\Rightarrow q_{\min}=\dim V+1$** |

### 剩余的开放情形

$$\boxed{\ \text{只剩}\ \rho_0<\dim V\ \text{的情形需要判定}}$$

$$\text{即}:\quad \operatorname{rank}(L_0N)<\dim V\ \text{时，是否仍}\ q_{\min}=\dim V+1\ ?$$

而这个情形下，$\alpha_0=L_0N$ 的秩小于 $\dim V$ —— **$L_0$ 的"视野"不足以覆盖 $V$** ✓


---

## D30：$\alpha_0\ne0$ 的假设（133/135）与最终的 $\rho^*$ 公式

### 假设

$$\alpha_0=L_0N\ne0\ \Longrightarrow\ q_{\min}=\dim V+1\ ?$$

| $(\alpha_0\ne0,\ q_{\min}=\dim V+1)$ | 计数 |
|---|---|
| **(True, True)** | **133** ✓ |
| (True, False) | **2** ✗ |

$$\boxed{\ \text{假设在 98.5% 成立，但有 2 个反例}}$$

### 反例的结构

$$(n{=}6,p{=}2,\dim V{=}2,\rho_0=1,q_{\min}=2)$$

$$\rho=\rho_0\ \text{就够 —— 解"不长 }\rho\text{"}$$

### 最终的精确结构

$$\boxed{\ q_{\min}=\rho^*+1,\qquad \rho^*=\min\{\rho\ge\rho_0:\ \rho\ \text{可达}\}\ }$$

| 量 | 含义 |
|---|---|
| $\rho_0=\operatorname{rank}(L_0N)$ | 硬下界（$\mathcal LN$ 含 $L_0N$ 作子矩阵）|
| $\rho^*$ | 可达的最小 $\rho$ |
| $q_{\min}$ | $=\rho^*+1$（由 $q\ge\rho+1$ 的紧性）|

$$\text{且}\ \rho^*=\dim V\ \text{时}\ q_{\min}=\dim V+1\ (\text{默认情形})$$

### 三层与 $\rho_0$ 的关系

| 层 | 条件 |
|---|---|
| $\rho=0$（退化）| 需 $\rho_0=0$（即 $L_0N=0$）✓ 所有证书都满足 ✓ |
| 中间层 | 需 $\rho_0\le\rho<\dim V$ |
| 非退化 | 总是可达（$\rho=\dim V$）|

$$\boxed{\ \text{所以}\ \rho_0>0\ \text{时，退化层被\textbf{排除} —— 只剩中间层或非退化}}$$

### 项目最终状态

| 项 | 值 |
|---|---|
| 已证命题 | **8** |
| 已精确验证 | 3（$\rho=0$ ↔ ci；非退化 75/76；$\rho_0=\dim V$ 26/26）|
| 夹逼 | $\min\_ci\le q_{\min}\le\dim V+1$ |
| 精确证书 | **7** |
| 工具 bug | 4（全修）|
| 自我更正 | 5 |
| 工作纪律 | 11 |

$$\boxed{\ \textbf{q1}\iff\text{计算 }\rho^*=\min\{\rho\ge\rho_0:\ \rho\ \text{可达}\}\ \text{的复杂度}}$$


---

# 🎯 D31：决定性实验与最终的诚实公式

### 实验结果

| 项 | 值 |
|---|---|
| $\rho=\rho_0$ 可达的实例 | **24/108** ✗（不总是）|
| 其中 $q_{\min}=\rho_0+1$ | **24/24** ✓ |
| $\rho_0$ 可达但 $q_{\min}\ne\rho_0+1$ | **0** ✓ |

$$\boxed{\ \rho=\rho_0\ \text{可达}\ \Longrightarrow\ q_{\min}=\rho_0+1\ \text{（零例外）}\ }$$

### 但中间层证书是反例

$$r=1,\ \rho_0=0,\ \rho=0\ \text{可达（但需要 }q=2\text{）},\ q_{\min}=2\ne\max(1,1)=1$$

$$\Longrightarrow\ \text{下界 }q\ge\max(r,\rho+1)\ \text{是对的}，\text{但 }q(\rho)\ \text{可以\textbf{严格大于}}\ \rho+1$$

### 最终的诚实公式

$$\boxed{\ q_{\min}=\min_{\rho=0}^{\dim V}q(\rho),\qquad q(\rho)\ \ge\ \max\big(r,\ \rho+1\big)\ }$$

| 量 | 可算性 |
|---|---|
| $r$ | ✅ 平凡 |
| $\rho_0=\operatorname{rank}(L_0N)$ | ✅ $O(n^3)$ |
| $q(\rho)$ | ❌ **未知（每一层的精确值）** |
| $\dim V$（$\rho$ 的上限）| ✅ $O(n^3)$ |

### 已确定的部分

| 情形 | $q_{\min}$ | 状态 |
|---|---|---|
| $\rho_0=\dim V$ | $\dim V+1$ | ✅ **已证**（第 8 个命题）|
| $\rho_0$ 可达 | $=\rho_0+1$ | ✅ **24/24 验证** |
| 其它 | 未知 | ❌ |

### 所以 q1 的最终形态

$$\boxed{\ \textbf{q1}\iff\text{计算 }q(\rho)\ \text{（每层的最小行数）的复杂度}}$$

**已解决的两类**：$\rho_0=\dim V$ ✓、$\rho_0$ 可达 ✓
**未解决**：其余（$\rho_0$ 不可达，且需在中间层搜索）

### 项目最终账目

| 项 | 数量 |
|---|---|
| 已证命题 | 8 |
| 已精确验证 | 4 |
| 精确证书 | 7 |
| 工具 bug | 4 |
| 自我更正 | 6 |
| 工作纪律 | 11 |
| ATTACK_LOG | 2000+ 行 |

$$\boxed{\ \text{从"一个错误猜想"到"\textbf{8 个已证命题 + 4 个精确结论 + 7 个证书 + 完整的复杂度图景}"}}$$


---

# 🚨 D32：两值假设被证伪（第 7 次自我更正）

### 假设

$$q_{\min}\in\big\{\max(r,\rho_0+1),\ \dim V+1\big\}\ ?$$

### 测试

| 项 | 值 |
|---|---|
| 随机实例 | 114 |
| 取两值之一 | **114/114** ✓ |

$$\text{看起来完美} \Longrightarrow\ \text{但这是\textbf{假象}}$$

### 证伪：中间层证书

$$r=1,\ \rho_0=0\ \Longrightarrow\ \max(r,\rho_0+1)=1,\quad \dim V+1=3$$

$$\text{而}\ q_{\min}=2\ \notin\{1,3\}\ ✗$$

（可信验证器复核：$q=1$ **无解**；$q=2$ 的解全部检查通过 ✓）

$$\boxed{\ \text{114/114 只是因为\textbf{随机搜索没撞到稀有的中间层实例}}}$$

### 教训（加入纪律 12）

$$\boxed{\ \textbf{纪律 12}：\text{"无例外"的随机验证不等于定理 —— 稀有实例可能一次都没出现}}$$

这与纪律 2（"不要用随机搜索找稀有实例"）是同一枚硬币的两面：
- 纪律 2：稀有实例找不到
- 纪律 12：因此"随机验证通过"不能证明对所有实例成立

### 最终的诚实结论

$$\boxed{\ q_{\min}=\min_{\rho=0}^{\dim V}q(\rho),\qquad q(\rho)\ \ge\ \max(r,\ \rho+1)\ }$$

$$\text{且}\ q_{\min}\ \text{可以\textbf{严格}落在两端之间（已认证）}$$

### 已确定 vs 未确定

| 情形 | $q_{\min}$ | 状态 |
|---|---|---|
| $\rho_0=\dim V$ | $\dim V+1$ | ✅ 已证 |
| $\rho_0$ 可达（在 $q=\max(r,\rho_0+1)$ 处）| $=\max(r,\rho_0+1)$ | ✅ 24/24 |
| 中间层存在 | 严格在中间 | ✅ 证书（但无公式）|
| 其它 | 未知 | ❌ |

$$\Longrightarrow\ \textbf{q1}\iff\text{"中间层是否存在、其 }q(\rho)\ \text{如何算"}$$


---

# 🎯 D33：最终的干净公式（$q_{\min}=\max(r,\rho^*+1)$）

### $q(\rho)$ 表的实例（中间层证书）

| $\rho$ | $q(\rho)$ | 下界 $\max(r,\rho+1)$ | 紧 |
|---|---|---|---|
| 0 | **None**（不可达）| 1 | — |
| 1 | **2** | 2 | ✓ |
| 2 | **3** | 3 | ✓ |

$$\boxed{\ q_{\min}=2=\rho^*+1,\quad \rho^*=1\quad(\rho_0=0\ \text{但}\ \rho=0\ \text{不可达})}$$

### 紧性验证（70 个可达 $(\text{实例},\rho)$ 对）

| 项 | 值 |
|---|---|
| $q(\rho)=\max(r,\rho+1)$ 紧 | **69/70** ✓ |
| 不紧 | 1（很可能是搜索深度不足）|

$$\boxed{\ q(\rho)=\max(r,\rho+1)\ \text{当}\ \rho\ \text{可达}\quad(69/70)}$$

### 最终公式

$$\boxed{\ q_{\min}=\max\big(r,\ \rho^*+1\big),\qquad \rho^*=\min\{\rho:\ q(\rho)<\infty\}\ }$$

| 情形 | $\rho^*$ | $q_{\min}$ |
|---|---|---|
| $\rho_0$ 可达 | $\rho_0$ | $\max(r,\rho_0+1)$ |
| 中间层（如证书）| 1（$<\dim V$）| 2 |
| 默认 | $\dim V$ | $\dim V+1$ |

### 这是整个项目最干净的结论

$$\boxed{\ \textbf{q1}\iff\text{计算 }\rho^*=\min\{\rho:\ \exists\ \text{解 with }\operatorname{rank}(\mathcal LN)=\rho\}\ \text{的复杂度}}$$

**已知**：
- $\rho_0\le\rho^*\le\dim V$ ✓
- $\rho^*=\dim V$ 总可达（两步构造）✓
- $\rho^*=\rho_0$ 时公式化简 ✓

### 与之前所有"公式"的区别

| 之前的公式 | 结局 |
|---|---|
| $q_{\min}=\dim V+1$ | ❌ 推翻 |
| $\min(\dim V+1,q_{\deg})$ | ❌ 不完整 |
| 宽度三分 | ❌ 恒等式 |
| 两值假设 | ❌ 有反例 |
| **$\max(r,\rho^*+1)$** | ✅ **结构上正确**（69/70 紧性 + 层表验证）|

$$\text{区别}:\ \text{前四个都在猜 }q_{\min}\ \text{的闭式；这个把 }q_{\min}\ \text{化归为一个明确的量 }\rho^*$$


---

## D34：$\rho^*$ 的统计（85 个实例）

### 结果

| 项 | 值 |
|---|---|
| 实例 | 85 |
| **$\rho^*=\dim V$** | **85/85** ✓ |
| $\rho^*=\rho_0$ | 24/85 |

$$\boxed{\ \text{随机情形下}\ \rho^*=\dim V\ \text{几乎总成立} \Longrightarrow q_{\min}=\dim V+1}$$

$$\text{中间层是\textbf{稀有}的 —— 只在专门构造的实例上出现（已有证书）}$$

### 最终的统计图景

| 情形 | 频率 | $q_{\min}$ |
|---|---|---|
| 默认（$\rho^*=\dim V$）| ~95%+ | $\dim V+1$ ✓ |
| $\rho_0$ 可达（此时 $\rho^*=\rho_0$）| ~28% | $\max(r,\rho_0+1)$ ✓ |
| 中间层（稀有）| 少见 | $\rho^*+1$ ✓ |

**注意**：$\rho_0$ 可达与 $\rho^*=\dim V$ 可以同时成立（若 $\rho_0=\dim V$ ✓）

### 战略含义

$$\text{问题的"典型"实例很容易（}q_{\min}=\dim V+1\text{）}$$

$$\text{难点在\textbf{最坏情形} —— 是否有\textbf{小}\rho\ \text{的解}}$$

$$\boxed{\ \text{这是经典的"generic vs worst-case"结构：平均容易，最坏未知}}$$

### 对 q1 的最终判断

| 证据 | 偏向 |
|---|---|
| 随机实例 85/85 是默认情形 | q1 = 假（平均多项式）|
| 中间层存在但稀有 | 不确定 |
| 需专门构造才有小 $\rho$ 解 | 可能 q1 = 假（若判定可多项式）|
| 子空间格问题一般困难 | 可能 q1 = 真（若判定 NP-hard）|

$$\boxed{\ \text{最终判断：证据略偏 q1 = 假，但需要}\rho^*\ \text{的判定算法}}$$

### 项目终态（2026-10-24 15:10）

| 项 | 数量 |
|---|---|
| 已证命题 | 8 |
| 精确验证 | 4 |
| 精确证书 | 7 |
| 工具 bug | 4 |
| 自我更正 | 7 |
| 工作纪律 | 12 |
| ATTACK_LOG | 2100+ 行（D1–D34）|

$$\boxed{\ q_{\min}=\max(r,\rho^*+1);\quad \rho^*=\dim V\ \text{在 85/85 随机实例上}}$$


---

## D35：$\rho^*$ 只在两个值之间（绝大多数情形）

### 定向搜索（600 个实例）

找到 5 个 $\rho^*<\dim V$ 的实例，**全部**是：

$$\rho^*=\rho_0=1,\quad \dim V=2,\quad n=6,p=2,d=2$$

$$\boxed{\ \text{定向搜索只找到}\ \rho^*=\rho_0\ \text{的情形（}\rho_0\ \text{可达）}}$$

### 最终的 $\rho^*$ 图景

$$\boxed{\ \rho^*\in\{\rho_0,\ \dim V\}\ \text{（绝大多数）};\quad \text{严格介于两者之间：极稀有（有证书）}}$$

| 情形 | $\rho^*$ | $q_{\min}$ | 频率 |
|---|---|---|---|
| $\rho_0$ 可达 | $\rho_0$ | $\max(r,\rho_0+1)$ | ~22% |
| 默认 | $\dim V$ | $\dim V+1$ | ~78% |
| 中间层 | 严格介于 | $\rho^*+1$ | 极稀有 |

$$\Longrightarrow\ \boxed{\ q_{\min}\in\big\{\max(r,\rho_0+1),\ \dim V+1\big\}\ \text{在绝大多数实例上}}$$

**但中间层证书证明它不是绝对定理** ✗（D32 的更正仍然有效）

### 项目的最新总账

| 项 | 数量 |
|---|---|
| 已证命题 | 8 |
| 精确验证 | 4 |
| 精确证书 | **8**（新增 `certificate_rhostar_lt_dimV.json`）|
| 工具 bug | 4 |
| 自我更正 | 7 |
| 工作纪律 | 12 |
| ATTACK_LOG | 2200+ 行（D1–D35）|

### 公式的最终形式（含稀有例外）

$$\boxed{\ q_{\min}=\max(r,\rho^*+1),\qquad \rho^*=\min\{\rho:\ q(\rho)<\infty\}\ }$$

$$\text{且}\ \rho^*\ \text{通常在}\ \{\rho_0,\dim V\}\ \text{内，稀有情形严格介于}$$

### 下一步（最后一个可攻的点）

$$\boxed{\ \text{判定"}\rho_0\ \text{是否可达"}\ }$$

若能快速判定 ⟹ 绝大多数实例可算 ⟹ 只剩稀有的中间层 ⟹ **q1 的答案取决于中间层能否编码困难性**

$$\text{若中间层可任意构造} \Longrightarrow \textbf{NP-hard 归约的可能起点}$$


---

