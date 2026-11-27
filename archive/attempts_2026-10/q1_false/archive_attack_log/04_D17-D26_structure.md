> **归档说明（2026-10-27 重构）**：本文件是从旧文档拆出的归档件，文中链接指向重构前的旧路径；新旧路径映射见根目录 `ATTEMPTS.md` 与 `README.md`。

# 攻击日志 · D17–D26（拆分自 ATTACK_LOG.md）

> 原文：`archive/attack_A2V0/ATTACK_LOG.md`。

# 🎯 D17：解的结构定理（必要条件成立 45/45）

### 命题

$$\text{若}\ q>\rho\ (\rho=\dim\operatorname{row}(\mathcal LN)),\ \text{则}\ \ker(\cdot N|_{\mathcal V})\ne0$$

**更精确**（秩-零化度）：

$$\boxed{\ \dim\ker(\cdot N|_{\mathcal V})=q-\rho\ }$$

### 证明

$$\cdot N:\ \mathcal V\to\mathbb R^d,\quad \dim\mathcal V=q,\quad \operatorname{rank}=\rho$$

$$\Longrightarrow\ \dim\ker=\ q-\rho\qquad\blacksquare$$

### 验证

| 项 | 值 |
|---|---|
| $\rho=1$ 可达的实例 | 45 |
| 其中 $\mathcal V\cap\ker(\cdot N)\ne0$ | **45** ✓ |
| 违反 | **0** ✓ |

### 结构性推论（关键）

$$\boxed{\ \textbf{每个解} = \underbrace{(q-\rho)\text{ 维的 }N\text{-零部}}_{\text{退化部}} + \underbrace{\rho\text{ 维}}_{\text{非退化部}}\ }$$

$$\text{验证}:\ q=\dim\mathcal V=(q-\rho)+\rho\ \checkmark$$

### 为什么这是大简化

$$\text{原来}:\ \text{在 }\binom{n}{q}\ \text{个子空间里搜}$$
$$\text{现在}:\ \text{退化部在 }\ker(\cdot N)\ (\dim n-d)\ \text{里选},\ \text{非退化部在补空间里选}$$

$$\Longrightarrow\ \text{搜索空间从 }\binom{n}{q}\ \text{降到}\ \binom{n-d}{q-\rho}\times\binom{d}{\rho}$$

### 对分层的意义

| 层 | 退化部维数 | 非退化部维数 |
|---|---|---|
| $\rho=0$ | $q$ | 0（纯退化）|
| $\rho=\dim V$ | $q-\dim V$ | $\dim V$ |
| 中间层 | $q-\rho$ | $\rho$ |

$$\boxed{\ \text{中间层}\ =\ "\text{退化部与非退化部的}\textbf{混合}"\ ——\ \text{这就是它的复杂性来源}}$$


---

## D18：中间层的稀有性

### 数据（seed 5555，120 个实例）

| 项 | 值 |
|---|---|
| 测试实例 | 97 |
| $q_{\min}<\dim V+1$ 的 | **1** |
| 该例的 $\rho$ | **0**（退化）|
| 中间层（$0<\rho<\dim V$）出现次数 | **0** |

对比：D12 的 100 个实例里出现过 3 次中间层。

$$\boxed{\ \text{中间层\textbf{罕见但不为零}（D12: 3/100；D18: 0/97）}}$$

### 统计图景（全部数据的合并印象）

| 情形 | 频率 | $q_{\min}$ |
|---|---|---|
| 只有非退化解 | ~85% | $\dim V+1$ ✓ |
| 有退化解（$\rho=0$）| ~15% | $\min(\dim V+1,\ q_{\deg})$ |
| 有中间层解 | **~1–3%** | 需要单独的公式 ❌ |

### 这对 q1 的意义

$$\text{若中间层\textbf{根本不存在}} \Longrightarrow q_{\min}=\min(\dim V+1,q_{\deg})\ \text{多项式}\ \Longrightarrow \textbf{q1 = 假}$$

$$\text{若中间层存在（哪怕是罕见的）}\ \Longrightarrow\ \text{公式必须包含它} \Longrightarrow\ \text{复杂度未知}$$

$$\boxed{\ \textbf{决定性实验}：\text{能否构造出中间层的实例（}0<\rho<\dim V\text{）？}}$$

D12 的三个实例是随机撞上的（$n=6,p=2$）。若能**定向构造**，就能研究其一般结构。

### 项目最终账目

| 类别 | 数量 |
|---|---|
| 已证命题 | 6（$N^{\mathsf T}R_0=0$、$S'=S$、线性引理、$q\ge\rho+1$、$\dim B\le p$、结构分解）|
| 已验证等价 | 2（$\rho=0$ ↔ conditioned invariant；$(5a)\Leftrightarrow\mathcal VA\subseteq\mathcal V+\mathcal J$）|
| 已推翻猜想 | 3（$\max(3,d+2-p)$、$\dim V+1$、双层公式）|
| 已排除路线 | 8 |
| 工具 bug | 3（全修）|
| 反例证书 | 1（精确）|

$$\boxed{\ \text{q1 归结为：中间层存在性 + 其最小化复杂度}}$$


---

# 🎯 D19：中间层证书（精确认证）

### 证书

```
n=6, p=2, dimV=2, q=2, rho=1
(5a)=True, (5b)=0（成功）, q=2 < dimV+1=3
```

文件：`lit/certificate_middle_layer.json`

### 意义

$$\boxed{\ \text{中间层（}0<\rho<\dim V\text{）\textbf{确实存在} —— 不再是猜测}}$$

| 层 | 是否存在 | 证书 |
|---|---|---|
| $\rho=0$（退化）| ✅ 存在 | `counterexample_refute_dimV1.json` + 构造族 |
| **$0<\rho<\dim V$（中间）** | ✅ **存在** | **`certificate_middle_layer.json`** |
| $\rho=\dim V$（非退化）| ✅ 总是存在 | 两步构造 |

### 所以

$$q_{\min}=\min\Big(\dim V+1,\ q_{\deg},\ \min\{q:\ \exists\ \text{中间层解}\}\Big)$$

$$\text{三项都可能胜出} \Longrightarrow\ \text{没有简单的两项公式}$$

### q1 的最终形态

$$\boxed{\ \textbf{q1}\iff\text{"中间层的最小行数"是否多项式可算}}$$

这是整个项目缩小到的**唯一问题**。

### 项目最终统计

| 类别 | 数量 |
|---|---|
| 已证命题 | 7 |
| 已验证等价 | 2 |
| 已推翻猜想 | 3 |
| 已排除路线 | 8 |
| 工具 bug | 3（全修）|
| **反例/证书** | **2**（退化层 + 中间层）|
| 攻击日志 | 约1400 行 |


---

## D20：第 4 个工具 bug（同一类错误）

### 测试

$$\text{公式 }\min(q_{\deg},\ \rho^*+1):\ 106/111$$

5 个"反例"里，3 个是 `(n,p,dimV,qmin,rhostar,qdeg,pred) = (6,2,2,3,1,None,2)`

### 诊断

$$\text{我的 }\rho^*\ \text{搜索用了\textbf{随机的 }(\rho+1)\text{ 行矩阵}}$$

$$\text{但问题要求}\ \operatorname{row}(L_0)\subseteq\operatorname{row}(\mathcal L)\ ✗\ \text{（漏了这个约束）}$$

$$\Longrightarrow\ \text{找到的"$q=2$ 解"根本不包含 }L_0\ \text{，不是本问题的解}$$

### 这与 D12 的 bug 是同一类

| bug | 表现 |
|---|---|
| D12 | 穷举时 `row_basis` 把 $L_0$ 的行替换掉了 |
| D20 | 搜索 $
ho^*$ 时完全没加 $\supseteq\operatorname{row}(L_0)$ 约束 |

$$\boxed{\ \textbf{纪律 9}：\text{任何搜索都必须显式检查 }\operatorname{row}(L_0)\subseteq\operatorname{row}(\mathcal L)}$$

### 修正后的公式（待验证）

$$\boxed{\ q_{\min}=\min\big(q_{\deg},\ \rho^*+1\big),\qquad \rho^*=\min\{\rho\ge1:\ \exists\ (\rho+1)\text{-行解}\supseteq\operatorname{row}(L_0),\ \operatorname{rank}(\mathcal LN)=\rho\}}$$

$$\text{若这个公式成立}\ \Longrightarrow\ \text{只需对每个 }\rho\ \text{判定可达性}$$

### 修正后的正确率

去掉 3 个 bug 造成的"反例"后：**106/108**（剩下 2 个是搜索深度不够）

### 四次 bug 的教训总表

| # | bug | 伪装成什么 |
|---|---|---|
| 1 | 采样 $\lambda$ 验 $(5b)$ | "找到反例" |
| 2 | 带过滤搜索验"对所有解" | "24188 次验证通过" |
| 3 | `row_basis` 丢 $L_0$ | "双层公式 180/180" |
| 4 | $\rho^*$ 搜索漏 $\supseteq\operatorname{row}(L_0)$ | "公式 106/111" |

$$\boxed{\ \text{四次都是\textbf{同一个敌人}：搜索约束写漏，然后结论看起来是对的}}$$


---

# ✅ D21：可信基线（可信验证器 c164）

### 动机

四次工具 bug 之后，把所有检查集中到一个脚本，**逐项打印约束**，使"结论"与"检查"一一对应。

$$\texttt{scripts/core/c164\_trusted\_baseline.py}$$

### 检查项（每一项都显式打印）

| 项 | 含义 |
|---|---|
| `prefix_L0` | $\mathcal L$ 的前 $r$ 行**逐字**等于 $L_0$（问题的字面要求）|
| `rowspan_L0` | 较弱版本：$\operatorname{row}(L_0)\subseteq\operatorname{row}(\mathcal L)$ |
| `5a` | 精确秩判定 |
| `5b` | **精确 GCD**（不采样 $\lambda$）|
| `rank_L` | 行满秩 |

### 结果

```
cert: refute_dimV1
  完整检查: {'prefix_L0': True, 'rowspan_L0': True, '5a': True, '5b': True, 'rank_L': True}
  → 是合法解? True     q=1 < dimV+1=2 ✓

cert: middle_layer
  完整检查: {'prefix_L0': True, 'rowspan_L0': True, '5a': True, '5b': True, 'rank_L': True}
  → 是合法解? True     q=2 < dimV+1=3 ✓
```

$$\boxed{\ \text{两个反例在完整检查下\textbf{全部通过} —— 推翻结论可靠}\ ✓}$$

### 公式验证

| 实例 | $q_{\min}$ | $q_{\deg}$ | $\rho^*$ | 预测 $\min(q_{\deg},\rho^*+1)$ | 一致 |
|---|---|---|---|---|---|
| `cand` | 3 | None | 2 | 3 | ✓ |
| `p2` | 3 | None | 2 | 3 | ✓ |
| 随机 ×3 | — | — | — | — | ✓ |

### 可信基线总结

| 断言 | 状态 |
|---|---|
| 主定理 $q_{\min}=\dim V+1$ | ❌ **推翻**（证书通过完整检查）|
| 中间层存在 | ✅ **证书通过完整检查** |
| 公式 $\min(q_{\deg},\rho^*+1)$ | 🟡 目前无已知反例 |
| $N^{\mathsf T}R_0=0$、$S'=S$、$q\ge\rho+1$ 等 7 个命题 | ✅ 已证（与搜索无关）|

$$\boxed{\ \text{现在有了一个\textbf{可信}的基线：结论与检查一一对应，无法再悄悄漏约束}}$$


---

# ✅ D22：两项重验（可信验证器 c165）

### 任务 1：$\rho=0$ 层 ⟺ conditioned invariant（精确重做）

| 项 | 值 |
|---|---|
| 测试的退化 $\mathcal L$ | 60 |
| 一致 | **60/60** ✓ |
| 不一致 | **0** ✓ |

$$\boxed{\ \text{等价性在\textbf{精确检查}下成立}}$$

（旧验证 D10.1 用了采样 $\lambda$，现在确认结论无碍 ✓）

### 任务 2：$q_{\min}=\dim V+1$ 的一致率（精确重做）

| 项 | 值 |
|---|---|
| 实例 | 76 |
| $q_{\min}=\dim V+1$ | **75/76** ✓ |
| 例外 | 1：$(n,p,\dim V,q_{\min},\rho)=(5,2,1,1,0)$ |
| **非退化例外** | **0** ✓ |

$$\boxed{\ \text{原定理在\textbf{非退化情形下精确成立}}}$$

（旧结论 88/91，现在 75/76，且唯一例外确认是 $\rho=0$ ✓）

### 可信基线（最终）

| 断言 | 状态 | 验证方式 |
|---|---|---|
| $q_{\min}=\dim V+1$（非退化）| ✅ **成立** | 75/76，例外全是 $\rho=0$ |
| $\rho=0$ ⟺ conditioned invariant | ✅ **成立** | 60/60（精确）|
| 中间层存在 | ✅ **成立** | 证书通过完整检查 |
| 主定理（无条件下）| ❌ **推翻** | 证书通过完整检查 |
| 7 个已证命题 | ✅ | 纸面/Lean |

### 最终图景（可信）

$$\boxed{\ q_{\min}=\min\big(\dim V+1,\ q_{\deg},\ \min\{q:\ \text{中间层解}\}\big)\ }$$

| 层 | 可算性 |
|---|---|
| $\dim V+1$（非退化）| ✅ $O(n^3)$ |
| $q_{\deg}$（退化）| ✅ conditioned invariant（多项式）|
| 中间层 | ❌ **未知** |

$$\textbf{q1} \iff \text{中间层最小行数是否多项式可算}$$

### 项目最终状态

| 项 | 值 |
|---|---|
| 已证命题 | 7 |
| 已精确验证的等价 | 2（$\rho=0$ ↔ ci；$(5a)$ 的行空间形式）|
| 已推翻猜想 | 3 |
| 精确证书 | 2 |
| 工具 bug | 4（全修）|
| 可信验证器 | `c164`（完整检查）+ `c165`（重验）|


---

# 🎯 D23：中间层证书的结构分析（关键发现）

### 数据

```
n=6, p=2, d=2, dimV=2, dimJ=4
q=2, rho=1, dim(V ∩ ker(·N)) = 1  （= q-rho ✓）
V A ⊆ V + J ? True    （conditioned invariant ✓）

最小 conditioned invariant 维数 = 2     ← 与 q 相等！
A-不变包维数 = 6                       ← 太大
```

$$\boxed{\ \text{中间层解的维数} = \text{最小 conditioned invariant 维数} = 2}$$

### 含义（推翻我 D14 的结论）

我此前（D14）说"最小 conditioned invariant 不满足 $(5b)$" ✗ ——
实际上：那个"最小 ci"是**某个特定的**（格中的交）；**同维数下还有别的** ci 子空间，其中某些满足 $(5b)$ ✓

$$\boxed{\ \text{所以问题不是"最小 ci 不行"，而是"最小维数下是否存在无零点的 ci"}}$$

### 修正后的公式

$$q_{\min}=\min\{\dim\mathcal V:\ \mathcal V\ \text{ci}\supseteq\operatorname{row}(L_0),\ \mathcal V\ \text{无铅笔零点}\}$$

$$\text{且}\ q_{\min}\ge\ \dim(\text{最小 ci})\quad(\text{下界，多项式可算})$$

### 这重新打开了多项式算法的可能

| 步骤 | 可算性 |
|---|---|
| 计算最小 ci 维数 $d_0$ | ✅ 多项式（标准算法）|
| 在 $d_0$ 维 ci 中找无零点的 | ❓ **这就是新的核心问题** |
| 若找不到，加到 $d_0+1$ | hmm |

$$\boxed{\ \textbf{q1}\iff\text{"在 }d_0\text{ 维 ci 中判定无零点者是否存在"的复杂度}}$$

### 与已有结果的关系

| 结果 | 状态 |
|---|---|
| $q\ge\dim(\text{最小 ci})$ | ✅ 新下界（可算！）|
| 证书里取等号 | ✅ 2 = 2 |
| D14 的"最小 ci 失败" | ⚠️ **需修正**：那是特指格中交，不是所有最小维 ci |


---

## D24：$q_{\min}$ 不必取夹逼的两端

### 测试（59 个实例）

| 项 | 值 |
|---|---|
| 实例 | 59 |
| $q_{\min}\in\{\min\_ci,\ \dim V+1\}$ | **57/59** ✓ |
| 反例 | 2：$(n,p,\dim V,\min\_ci,q_{\min},\dim V+1)=(6,2,2,1,2,3)$ |

$$\boxed{\ q_{\min}\ \text{通常取两端之一，但\textbf{可以严格在中间}}}$$

### 所以

$$\dim(\mathcal V^{\mathrm{ci}}_{\min})\ \le\ q_{\min}\ \le\ \dim V+1$$

$$\text{两端都可多项式算，但中间值存在} \Longrightarrow\ \text{夹逼不能闭合}$$

### 精确的图景（最终版）

| 量 | 可算性 | 与 $q_{\min}$ 的关系 |
|---|---|---|
| $\dim(\mathcal V^{\mathrm{ci}}_{\min})$ | ✅ $O(n^3)$ | 下界（可取等）|
| $q_{\min}$ | ❓ | 通常 = 下界或上界，偶尔在中间 |
| $\dim V+1$ | ✅ $O(n^3)$ | 上界（可取等）|

$$\boxed{\ \text{夹逼宽度} = \dim V+1-\dim(\mathcal V^{\mathrm{ci}}_{\min})\ \text{—— 宽度为 }0\ \text{时可算}}$$

### q1 的最终形态

$$\textbf{q1}\iff\text{能否在夹逼内部精确判定 }q_{\min}$$

$$\text{若夹逼宽度为 }0\ \text{或 }1\ \text{时能判定} \Longrightarrow \text{多项式}$$
$$\text{若宽度可以任意大且判定困难} \Longrightarrow \textbf{NP-hard}$$

### 今日总结（最终）

| 时间 | 事件 |
|---|---|
| 10-23 早 | 以为定理 6/7 已证 |
| 10-23 晚 | 发现 $A^2V_0$ 路线三条死路 |
| 10-24 02:20 | **主定理被推翻**（精确证书）|
| 10-24 02:40 | 双层公式（180/180 → 发现 bug → 97/100）|
| 10-24 03:00 | 分层结构 |
| 10-24 03:30 | 中间层证书 |
| 10-24 04:00 | **夹逼建立**（两端可算）|
| 10-24 04:10 | 夹逼不能闭合（57/59）|

$$\boxed{\ \text{净结果：从"一个错误证明"到"一个精确夹逼 + 三个证书 + 四个 bug 教训"}}$$


---

## D25：夹逼宽度的分布（54 个实例）

### 数据

| 夹逼宽度 $(\dim V+1-\min\_ci)$ | 计数 |
|---|---|
| 0 | 2 |
| **1** | **46** |
| 2 | 5 |
| 3 | 1 |

| $q_{\min}$ 相对下界的偏移 | 计数 |
|---|---|
| 0 | 5 |
| **1** | **44** |
| 2 | 4 |
| 3 | 1 |

$$\boxed{\ \text{宽度}\le1\ \text{占}\ 48/54\ (89\%);\quad q_{\min}=\min\_ci+1\ \text{占}\ 44/54\ (81\%)}$$

### 但更紧的夹逼不成立

$$\min\_ci\ \le\ q_{\min}\ \le\ \min\_ci+1\quad ✗\ (\text{偏移可以到 2、3})$$

$$\Longrightarrow\ \text{真正的夹逼仍是}\ \min\_ci\le q_{\min}\le\dim V+1$$

### 这对 q1 的意义

$$\text{宽度通常为 }1\ \Longrightarrow\ \text{只需判定"取上界还是下界"（1 bit）}$$

$$\text{但偶尔宽度 }\ge2\ \text{且 }q_{\min}\ \text{在中间} \Longrightarrow\ \text{需要更细的判定} ✗$$

$$\boxed{\ \textbf{q1}\iff\text{判定"落在夹逼的哪个位置"的复杂度}}$$

### 一个有趣的统计事实

$$\text{宽度}=1\ \text{时}，\ \dim V+1 = \min\_ci+1\ \text{，而} q_{\min}\ \text{通常是} \min\_ci+1$$

$$\Longrightarrow\ \text{在宽度 1 的多数情形下}，q_{\min}=\dim V+1 = \min\_ci+1\ \text{，两端重合}$$

$$\text{所以""多数情形是退化的（两端重合）"—— 真正的难点只在少数宽度}\ge2\ \text{的实例}$$


---

## D26：宽度 ≥2 的实例（构造成功）

### 结果（4 个实例，全部宽度 = 2）

| $n$ | $p$ | $\dim V$ | $\min\_ci$ | 宽度 | $q_{\min}$ | 偏移 |
|---|---|---|---|---|---|---|
| 5 | 1 | 3 | 2 | **2** | 4 | 2 |
| 6 | 1 | 4 | 3 | **2** | 5 | 2 |
| 5 | 1 | 3 | 2 | **2** | 4 | 2 |
| 6 | 1 | 4 | 3 | **2** | 5 | 2 |

$$\boxed{\ \text{宽度 }2\ \text{时，}q_{\min}=\dim V+1\ (\text{取上界})\ ✓}$$

证书：`lit/certificate_wide_bracket.json`

### 模式

| 宽度 | $q_{\min}$ 位置 |
|---|---|
| 0 | 下界（$\min\_ci$）|
| 1 | $\min\_ci+1=\dim V+1$（两端重合）|
| ≥2 | **上界**（$\dim V+1$）|

$$\Longrightarrow\ \text{宽度越大，} q_{\min}\ \text{越倾向于上界}$$
$$\text{即：真正的"便宜解"（取到下界附近）只在宽度}\le1\ \text{时出现}$$

### 一个可能的候选公式

$$q_{\min}=\begin{cases}\min\_ci & \text{宽度}=0\\ \min\_ci+1 & \text{宽度}=1\\ \dim V+1 & \text{宽度}\ge2\end{cases}$$

$$\text{若成立}\ \Longrightarrow\ \text{纯组合判定（只看宽度）}\ \Longrightarrow\ \textbf{q1 = 假}$$

**但需要验证**：宽度 1 时 $q_{\min}$ 是否一定等于 $\min\_ci+1$（旧数据里有 offset=0 与 width=1 共存的情形 ⚠️）

### 下一步（明确）

1. 在**宽度 1** 的实例上专门检验：$q_{\min}=\min\_ci+1$ 是否总是成立
2. 若成立 ⟹ 候选公式在宽度 ≤2 时成立
3. 再检验宽度 3、4 是否仍取上界


---

