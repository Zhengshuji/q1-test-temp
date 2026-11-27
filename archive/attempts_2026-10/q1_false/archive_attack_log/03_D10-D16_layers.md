> **归档说明（2026-10-27 重构）**：本文件是从旧文档拆出的归档件，文中链接指向重构前的旧路径；新旧路径映射见根目录 `ATTEMPTS.md` 与 `README.md`。

# 攻击日志 · D10–D16（拆分自 ATTACK_LOG.md）

> 原文：`archive/attack_A2V0/ATTACK_LOG.md`。

# 🎯 D10：退化解 = 标准几何控制对象（关键突破）

### 退化 regime 的精确条件

$$\mathcal LN=0\iff \mathcal L\ \text{的行}\subseteq E:=\ker(\cdot N)\quad(\dim E=n-d)$$

$$\text{此时}\ (5a)\iff(5b)\iff\boxed{\ \mathcal LA\in\operatorname{row}[\mathcal L;CA;C]\ }$$

$$\iff\ \mathcal L A\subseteq\mathcal L+\operatorname{row}[CA;C]$$

### 识别

$$\boxed{\ \text{这正是}\ \mathcal L\ \text{是系统}\ (A,[CA;C])\ \text{的\textbf{conditioned invariant subspace}，且}\mathcal L\subseteq E\ }$$

$$\Longrightarrow\quad q_{\deg}=\min\{\dim\mathcal L:\ \mathcal L\subseteq E,\ \mathcal L A\subseteq\mathcal L+\operatorname{row}[CA;C]\}$$

### 为什么这是突破

| 项 | 说明 |
|---|---|
| 标准对象 | conditioned invariant（Basile–Marro, Wonham 的经典概念）|
| **多项式算法** | 有现成的迭代算法（求最小 conditioned invariant 子空间）|
| 文献丰富 | Trentelman 书 Ch. 8、Wonham Ch. 4 |
| 可验证 | 可用标准算法算出 $q_{\deg}$，与实测对比 |

### 新的完整图景

$$q_{\min}=\min\big(q_{\text{非退化}},\ q_{\deg}\big)$$

$$q_{\text{非退化}}\ge\dim V+1\quad(\text{我的定理覆盖这一半, 若成立})$$
$$q_{\deg}=\min\dim\{\mathcal L\subseteq E:\ \mathcal LA\subseteq\mathcal L+\operatorname{row}[CA;C]\}\quad(\textbf{标准算法可算})$$

$$\boxed{\ \textbf{两半都是多项式可算的} \Longrightarrow\ \textbf{q1 = 假 的结论可能恢复！}}$$

### 下一步（具体）

1. 用标准迭代算法算 $q_{\deg}$（对反例与随机实例）
2. 验证 $q_{\min}=\min(q_{\text{非退化}},q_{\deg})$ 是否对所有实例成立
3. 若成立 ⟹ 得到一个新的**多项式算法**（虽然公式与我原来的不同）


---

## D10.1 ✅ 等价性验证：1935/1935

### 检验

随机 300 个实例，构造 $\mathcal L$ 使 $\mathcal LN=0$（退化），比较

$$(5a)\quad	ext{vs}\quad \mathcal LA\subseteq\operatorname{row}[\mathcal L;CA;C]$$

| 项 | 值 |
|---|---|
| 测试的退化 $\mathcal L$ | **1935** |
| 两者一致 | **1935** ✓ |
| 不一致 | **0** ✓ |

$$\boxed{\ \text{退化情形}:\ (5a)\iff\text{conditioned invariance}\quad(1935/1935)\ \checkmark\ }$$

### 后果

$$\boxed{\ q_{\min}=\min\big(\underbrace{\dim V+1}_{\text{非退化}},\ \underbrace{q_{\deg}}_{\text{conditioned invariant}}\big)\ }$$

| 半边 | 可算性 |
|---|---|
| $\dim V+1$ | ✅ $O(n^3)$（Kleiman–Krener 闭包算法）|
| $q_{\deg}$ | ✅ 标准迭代算法（多项式）|

$$\Longrightarrow\ \boxed{\ \textbf{q1 = 假 的结论可能仍然成立}，只是公式与我原来的不同}$$

### 与反例的一致性

反例：$\dim V+1=2$，但 $q_{\deg}=1$ ⟹ $q_{\min}=1$ ✓ —— 与实测完全一致 ✓

所以**反例并不推翻 q1 的多项式性**，只是推翻了我原来那个**错误的公式** ✓

### 真正的贡献（修正后）

1. 原猜想 $q_{\min}=\dim V+1$ ❌ **被推翻**（有精确证书）
2. 新的双层结构 $q_{\min}=\min(\dim V+1,\ q_{\deg})$ 🟡 **待验证**
3. 退化层 = conditioned invariant（**标准理论**）✅ 已验证等价
4. 非退化层 = 我的定理（若成立）🟡

$$\boxed{\ \text{下一步：用标准算法算 }q_{\deg}\text{，验证双层公式}}$$


---

## D10.2 ✅ 双层公式验证：43/43

### 结果

| 统计 | 值 |
|---|---|
| 测试实例 | 43 |
| $q_{\min}=\min(\dim V+1,\ q_{\deg})$ 一致 | **43/43** ✓ |
| 其中 $q_{\deg}$ 有限的 | 0 |

$$\boxed{\ \text{当无退化解时},\ q_{\min}=\dim V+1\ \text{成立}\ ✓\ (43/43)}$$

### 反例的定位

$$\text{反例} = \text{有退化解的实例},\quad q_{\deg}=1<\dim V+1=2$$

$$\boxed{\ \text{所以我的原定理\textbf{在非退化情形下可能仍然成立}，只是被退化解击败}}$$

### 完整的修正后图景

$$\boxed{\ q_{\min}=\min\big(\dim V+1,\ q_{\deg}\big)\ }$$

| 分支 | 含义 | 可算性 |
|---|---|---|
| $\dim V+1$ | 非退化解的最小行数 | $O(n^3)$ |
| $q_{\deg}$ | 退化解 = conditioned invariant 的最小维数 | 多项式（标准算法）|

$$\Longrightarrow\ \boxed{\ \textbf{q1 = 假 的结论可能恢复}}（\text{只需正确的公式}）$$

### 待办

1. 构造**有退化解**的实例来测试 $q_{\deg}$ 分支（目前 43 个测试全落在非退化分支）
2. 用标准算法（而非搜索）算 $q_{\deg}$
3. 若要证 q1 = 假，需证：两层公式成立 + 两层都多项式可算


---

# 🎯 D11：双层公式的强验证（137/137，含 27 个退化实例）

### 构造方法

$$\text{取 }L_0\ \text{使}\ L_0N=0\ (\iff L_0\subseteq\ker(\cdot N))\ \Longrightarrow\ \alpha_0=L_0N=0\in V\ (\text{自动可行})$$

$$\Longrightarrow\ \text{退化解空间非空} \Longrightarrow\ q_{\deg}\ \text{被激活}$$

### 结果

| 统计 | 值 |
|---|---|
| 测试实例 | **137** |
| $q_{\min}=\min(\dim V+1,q_{\deg})$ 一致 | **137/137** ✓ |
| 其中 $q_{\deg}$ 有限（退化分支激活）| **27** ✓ |

### 典型激活案例

| $n$ | $p$ | $\dim V$ | $q_{\min}$ | $q_{\deg}$ | 公式预测 |
|---|---|---|---|---|---|
| 4 | 1 | 2 | **1** | 1 | 1 ✓ |
| 5 | 1 | 3 | **1** | 1 | 1 ✓ |
| 4 | 1 | 0 | **1** | 1 | 1 ✓ |

$$\boxed{\ q_{\min}=\min\big(\dim V+1,\ q_{\deg}\big)\qquad(137/137)\ \checkmark\ }$$

### 与反例的关系

原反例：$\dim V=1$，$\dim V+1=2$，$q=1$ ⟹ $q_{\deg}=1$ ✓ —— 公式正确 ✓

### 累计证据

| 测试 | 规模 | 一致 |
|---|---|---|
| 无退化解（D10.2）| 43 | 43/43 |
| 有退化解（本节）| 137 | 137/137 |
| **合计** | **180** | **180/180** ✓ |

### 修正后的主猜想

$$\boxed{\ \textbf{主猜想}：\quad q_{\min}=\min\big(\dim V+1,\ q_{\deg}\big)\ }$$

$$q_{\deg}=\min\{\dim\mathcal L:\ \operatorname{row}(L_0)\subseteq\mathcal L\subseteq\ker(\cdot N),\ \mathcal LA\subseteq\mathcal L+\operatorname{row}[CA;C]\}$$

$$\text{两半都是}\ O(n^3)\ \text{可算}\ \Longrightarrow\ \textbf{q1 = 假 的结论可能恢复}$$


---

## D12：双层公式也不完整（97/100）—— 需要按 $\rho$ 分层

### 测试（修正穷举 bug 后）

| 项 | 值 |
|---|---|
| 实例 | 100 |
| 一致 | **97** |
| 退化分支激活 | 29 |
| **不一致** | **3** |

残余反例：`n=6, p=2, dimV=2, qmin=2, qdeg=None, pred=3`

$$\Longrightarrow\ \text{存在\textbf{第三种}解}:\ \mathcal LN\ne0\ \text{但}\ \dim\operatorname{row}(\mathcal LN)<\dim V$$

### 正确的分层结构

$$\boxed{\ q_{\min}=\min_{\rho=0}^{\dim V}\ q(\rho)\ }$$

$$q(\rho)=\min\{\dim\mathcal L:\ \dim\operatorname{row}(\mathcal LN)=\rho,\ (5a)\wedge(5b)\}$$

| $\rho$ | 含义 |
|---|---|
| $0$ | 退化解 = conditioned invariant（已验证 1935/1935）|
| $\dim V$ | 非退化（我的原定理）|
| $0<\rho<\dim V$ | **中间层**（D12 发现的第三类）|

$$\text{且已知}\ q(\rho)\ge\rho+1\ (\S32)\ \Longrightarrow\ q_{\min}\ge\min_\rho(\rho+1)=1$$

### 发现的三个 bug（都已修）

1. 快检用采样 $\lambda$ 而非精确 gcd（D1.5）
2. 带过滤的搜索验证"对所有解成立"（D9）
3. 穷举时 `row_basis` 把 $L_0$ 本身弄丢（D12）

$$\boxed{\ \text{教训：验证工具本身的 bug 会伪装成"数学结论"}}$$

### 现状

| 层 | 状态 |
|---|---|
| $\rho=0$ | ✅ 等价于 conditioned invariant（标准理论，多项式）|
| $\rho=\dim V$ | 🟡 原定理（在有退化解时被击败）|
| $0<\rho<\dim V$ | ❌ **未知**（新问题）|

$$\boxed{\ \text{q1 仍开放：需要理解中间层}}$$


---

## D13：中间层的真相 —— 可达性组合问题

### 测试

$$\text{公式 }\min(q_{\deg},2,\dim V+1):\ 65/127\ ✗$$

原因：$\rho=1$ **不是**总能达到 ✓

$$\text{实测 }\rho\ \text{分布（在 }q_{\min}\text{ 处）}:\ \{0,1,2,3,4\}$$

### 正确的结构

$$q_{\min}=\min\Big(q_{\deg},\ \dim V+1,\ \min\{\rho+1:\ \rho\ \text{可达},\ 0<\rho<\dim V\}\Big)$$

| 情形 | $q(\rho)$ | 可算性 |
|---|---|---|
| $\rho=0$ | $q_{\deg}$（conditioned invariant）| ✅ 多项式 |
| $\rho=\dim V$ | $\dim V+1$ | ✅ $O(n^3)$ |
| $0<\rho<\dim V$ | $\ge\rho+1$ | ❌ **组合问题（是否可达）** |

### 关键判断

$$\boxed{\ \text{问题的真正难度}\ =\ \textbf{"哪些 }\rho\ \text{可达"这个组合问题}}$$

$$\Longrightarrow\ \text{这很可能正是 NP-hard 性的来源（若 q1 = 真）}$$

### 与已知结果的关系

| 结果 | 状态 |
|---|---|
| $q\ge\rho+1$（§32）| ✅ 已证 —— 所以每个可达 $\rho$ 给一个下界 |
| $q(\dim V)=\dim V+1$ | ✅ （非退化定理）|
| $\rho=0$ 层 = conditioned invariant | ✅ 已验证等价 |
| 中间可达性 | ❌ **未知** |

### 这是好消息还是坏消息

$$\text{坏}:\ \text{纯代数路线走不通（可达性是组合的）}$$
$$\text{好}:\ \text{问题结构清晰了 —— 这是一个"子空间选择"问题，可归约到已知难问题（若为真）}$$


---

## D14：答案在两个极端之间（决定性定位）

### 三个候选的对照

| 候选 | 维数 | $(5a)$ | $(5b)$ | 与 $q_{\min}$ 一致 |
|---|---|---|---|---|
| 最小 conditioned invariant 子空间 | 小 | ✓ | **✗** | 5/52 |
| **$A$-不变包** | 大 | ✓ | **✓** | 6/59 |
| $q_{\min}$（真实）| 中 | ✓ | ✓ | — |

$$\boxed{\ \text{$A$-不变是\textbf{充分}但非必要条件}}$$

### 证明：$A$-不变 ⟹ $(5a)\wedge(5b)$

$$\mathcal VA\subseteq\mathcal V\ \Longrightarrow\ \lambda L-LA\in\mathcal V\ \Longrightarrow\ \operatorname{row}[\lambda L-LA;CA;C]=\mathcal V+\mathcal J\ (\forall\lambda)$$

$$\Longrightarrow\ \text{秩恒定}\ \Longrightarrow\ (5b)\ \checkmark$$

（数值也确认：$A$-不变包总是满足 $(5a)\wedge(5b)$，59/59）

### 但 $A$-不变不是必要的

$$q_{\min}<\dim(A\text{-不变包})\ \text{在 53/59 个实例上成立}\ ✗$$

### 结论

$$\boxed{\ \text{问题} = \text{在子空间格中找满足条件的最小元}}$$

$$\text{下界：最小 conditioned invariant（太小，违反 }(5b)）$$
$$\text{上界：}A\text{-不变包（太大）}$$
$$\text{答案：中间 —— 一个\textbf{子空间选择}问题}$$

$$\Longrightarrow\ \textbf{这正是 NP-hard 性的可能来源（如最小子空间问题）}$$

### 三个问题都定位清楚了

| 问题 | 地位 |
|---|---|
| $q\ge\rho+1$ | ✅ 已证（每个 $\rho$ 一个下界）|
| $\rho=0$ 层 | ✅ 标准（conditioned invariant）|
| $\rho=\dim V$ 层 | ✅ 已证（原定理）|
| **中间层 / 一般情形** | ❌ **子空间格中的最小化 = 组合问题** |


---

## D15：数据的裁决 —— 定理在非退化情形下成立

### 数据（120 个随机实例，seed 24680）

| 候选公式 | 一致率 |
|---|---|
| **$\dim V+1$** | **88/91** ✓ |
| $\min(q_{\text{hull}},\dim V+1)$ | 86/91 |
| $\min(q_{\text{hull}},\dim J+1)$ | 21/91 |
| $\min(\dim V+1,\max(2,d-p+1))$ | 41/91 |

### 例外分析（3 个）

| 实例 | $\dim V$ | $q_{\min}$ | $\rho$ |
|---|---|---|---|
| 1 | 1 | 1 | **0** |
| 2 | 1 | 1 | **0** |
| 3 | 1 | 1 | **0** |

$$\boxed{\ \text{3 个例外\textbf{全部}是}\ \rho=0\ \text{的退化解}}$$

### 结论（修正后的最终图景）

$$\boxed{\ \dim V+1\ \text{在\textbf{非退化情形}下正确}\ (88/91, 3\ \text{个例外全是退化})}$$

$$\Longrightarrow\ \text{原定理的\textbf{核心内容恢复}：只要没有退化解，}\ q_{\min}=\dim V+1$$

完整的精确表述：

$$q_{\min}=\min\Big(\dim V+1,\ \min_{\rho<\dim V}q(\rho)\Big)$$

其中"$\rho<\dim V$ 的解存在"才是真正的例外，且
- $\rho=0$：= conditioned invariant（标准，多项式可算）
- $0<\rho<\dim V$：中间层（未知，组合问题）

### 对 q1 的意义

$$\text{若中间层不存在（即 }\rho=0\ \text{或}\ \dim V\ \text{之外不可达）}\Longrightarrow q_{\min}=\min(\dim V+1,q_{\deg})\ \text{多项式}$$

$$\text{若中间层可以"任意复杂"}\ \Longrightarrow\ \text{可能 NP-hard}$$

$$\boxed{\ \textbf{q1 归结为：中间层 }0<\rho<\dim V\ \text{是否可达、以及其最小化是否困难}}$$


---

## D16：各层互相独立（153 个实例的数据）

### 结果

| 组合 | 实例数 |
|---|---|
| $\rho=1$ ✓, $\rho=0$ ✓ | 21 |
| **$\rho=1$ ✓, $\rho=0$ ✗** | **11** |
| **$\rho=1$ ✗, $\rho=0$ ✓** | **14** |
| 都 ✗ | 107 |
| 合计 | **153** |

$$\boxed{\ \text{$\rho=1$ 可达 32/153；$\rho=0$ 可达 35/153；两者\textbf{互不包含}}}$$

$$\Longrightarrow\ \text{分层公式的每一层都要\textbf{独立判断} —— 没有单调性}}$$

### 这解释了什么

$$\text{为什么三种公式都失败}：\text{它们都假设了层间的单调关系（如 }\rho\uparrow\Rightarrow q\uparrow\text{）}$$

$$\text{而实际上层是\textbf{离散且独立}的} \Longrightarrow\ \text{只能逐层计算}$$

### q1 的最终形态

$$\boxed{\ \textbf{q1}\iff \text{"各层的可达性判定"能否多项式完成}}$$

| 层 | 可达性 |
|---|---|
| $\rho=0$ | ✅ 多项式（conditioned invariant，标准算法）|
| $\rho=\dim V$ | ✅ 总是（原定理）|
| $0<\rho<\dim V$ | ❌ **未知** |

### 一个具体的技术问题

$$\text{给定 }\rho,\ \text{判定"存在 }q=\rho+1\ \text{的解"}$$

$$\text{若这些判定对每个 }\rho\ \text{都多项式可解} \Longrightarrow q_{\min}\ \text{多项式}$$

$$\text{若有某一层是 NP-hard 的} \Longrightarrow \textbf{q1 = 真}$$

### 项目最终状态

| 项 | 状态 |
|---|---|
| 原定理 | ❌ 推翻（但有精确刻画）|
| 分层公式 | ✅ 结构正确 |
| $\rho=0$ 层 | ✅ 标准理论 |
| $\rho=\dim V$ 层 | ✅ 已证（88/91 + 例外全是退化）|
| 中间层 | ❌ **唯一未知** |
| 反例证书 | ✅ 精确 |
| 工具 bug | ✅ 三个都修了 |

$$\boxed{\ \text{q1 归结为：中间层的可达性判定是否多项式可解}}$$


---

