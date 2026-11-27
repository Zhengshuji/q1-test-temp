> **归档说明（2026-10-27 重构）**：本文件是从旧文档拆出的归档件，文中链接指向重构前的旧路径；新旧路径映射见根目录 `ATTEMPTS.md` 与 `README.md`。

# 攻击日志 · D36–D42（拆分自 ATTACK_LOG.md）

> 原文：`archive/attack_A2V0/ATTACK_LOG.md`。

# ✅ D36：$\rho_0$ 可达性的化简（88/88 一致）

### 化简

$$\rho=\rho_0\iff \text{新增行的 }N\text{-像不增加秩}\iff \text{所有行都在}\ W_0\ \text{里}$$

$$W_0:=\{r\in\mathbb R^n:\ rN\in\operatorname{row}(L_0N)\}$$

$$W_0\ \text{是子空间（维数}\ n-\dim(\operatorname{row}(L_0N)^\perp)\text{）},\ \text{可显式算出}\ ✓$$

### 验证（88 个实例）

| 项 | 值 |
|---|---|
| $\rho_0$ 可达（无约束搜索）| **13** |
| $\rho_0$ 可达（只在 $W_0$ 里搜）| **13** |
| **不一致** | **0** ✓ |

$$\boxed{\ \rho_0\ \text{可达}\iff\exists\ \text{解其所有行都在}\ W_0\ \text{里}\quad(88/88)\ ✓}$$

### 这是一个有用的化简

| 项 | 化简前 | 化简后 |
|---|---|---|
| 搜索空间 | $\mathbb R^n$ | $W_0$（$\dim=3\sim5$）|
| 新增行的约束 | 无 | 全在 $W_0$ 里 |
| 秩条件 | 需检查 | **自动满足** ✓ |

### 让问题变成

$$\boxed{\ \text{在 }W_0\ \text{中找 }\mathcal L\supseteq\operatorname{row}(L_0)\ \text{满足}\ (5a)\wedge(5b)}$$

$$\text{若这个"子空间搜索"可多项式完成} \Longrightarrow \rho_0\ \text{可达性可判} \Longrightarrow\ \text{22% 的实例可算}$$

### 项目最新总账

| 项 | 数量 |
|---|---|
| 已证命题 | 8 |
| 精确验证 | **5**（新增本节的 88/88）|
| 精确证书 | 8 |
| 工具 bug | 4 |
| 自我更正 | 7 |
| 工作纪律 | 12 |
| ATTACK_LOG | 2250+ 行（D1–D36）|

### 下一步

1. 在 $W_0$ 中研究 $(5a)\wedge(5b)$ 的结构（$W_0$ 维数小，穷举可行）
2. 若能导出秩条件 ⟹ $\rho_0$ 可达性多项式 ⟹ 22% 覆盖
3. 中间层（稀有）另攻


---

## D37：$\rho_0$ 可达的情形主要是平凡的

### 数据（77 个实例）

| 情形 | 计数 | 特征 |
|---|---|---|
| $\rho_0$ 可达 | 17 | **15/17 是 $(n{=}5,p{=}2,\dim V{=}1)$** |
| $\rho_0$ 不可达 | 60 | $\dim V\ge2$ |

$$\boxed{\ \rho_0\ \text{可达}\ \Longrightarrow\ \dim V\ \text{小（多数}\dim V=1\text{）}}$$

### 为什么这是"平凡的"

$$\dim V=1\ \Longrightarrow\ \rho_0\le1\ \Longrightarrow\ \max(r,\rho_0+1)\le2=\dim V+1$$

$$\Longrightarrow\ \text{公式的两种取值只差 1（甚至相等）}$$

### 真正有意思的情形

$$\boxed{\ \dim V\ge2\ \wedge\ \rho^*<\dim V\quad\text{—— 即中间层（稀有）}}$$

$$\text{这才是 }q_{\min}\ \text{可能"意外地小"的地方}$$

### 最终的战略判断

| 情形 | 频率 | 状态 |
|---|---|---|
| $\dim V=1$ | 常见 | 公式两端只差 1 ⟹ 影响小 |
| $\dim V\ge2$，$\rho^*=\dim V$ | 多数 | ✅ 已证 $q_{\min}=\dim V+1$ |
| $\dim V\ge2$，$\rho^*<\dim V$ | **稀有** | ❌ 未解（中间层）|

$$\boxed{\ \textbf{q1}\iff\text{稀有中间层的复杂度}}$$

### 项目终态（2026-10-24 17:20）

| 项 | 数量 |
|---|---|
| 已证命题 | 8 |
| 精确验证 | 5 |
| 精确证书 | 8 |
| 工具 bug | 4 |
| 自我更正 | 7 |
| 工作纪律 | 12 |
| ATTACK_LOG | 2300+ 行（D1–D37）|

### 总结

$$\boxed{\ \text{问题的"主体"已解决（}\dim V\ge2\ \text{且}\ \rho^*=\dim V\ \text{时}\ q_{\min}=\dim V+1\text{）}}$$

$$\text{剩余的难点被压缩到\textbf{稀有的中间层} —— 这既是坏消息（未解）也是好消息（可能不影响实际应用）}$$


---

# 🎯 D38：中间层不可通过块扩展放大（q1 偏向于假）

### 实验

把中间层证书做块对角扩展：

$$A'=\begin{pmatrix}A&0\\0&A_{\text{extra}}\end{pmatrix},\qquad C'=(C,\ C_{\text{extra}})$$

| extra | $n$ | $\dim V$ | $q_{\min}$ | $\dim V+1$ | 中间层保持？ |
|---|---|---|---|---|---|
| 1 | 7 | 3 | 4 | 4 | **否** ✗ |
| 2 | 8 | 3 | 4 | 4 | **否** ✗ |
| 3 | 9 | 3 | 4 | 4 | **否** ✗ |

$$\boxed{\ \text{中间层\textbf{不可}通过块扩展放大 —— 它是"低维偶然"}}$$

### 对 q1 的意义

$$\boxed{\ \text{若"硬情形"不能规模化} \Longrightarrow \text{问题\textbf{很可能}是多项式可解的} \Longrightarrow \textbf{q1 偏向于假}}$$

**但这是启发式论证** ✗ —— 不是证明 ✓

### 为什么块扩展破坏了它

$$\text{中间层需要}\ \rho^*<\dim V\ \text{且}\ q_{\min}=\rho^*+1<\dim V+1$$

$$\text{块扩展把}\ \dim V\ \text{从 }2\ \text{提到 }3\ \text{，而}\ \max(r,\rho+1)\ \text{的增长跟不上}$$

$$\Longrightarrow\ q_{\min}=\dim V+1\ \text{—— 回到默认情形}$$

### 证据的最终天平

| 证据 | 偏向 |
|---|---|
| 8 个已证命题 | 中性 |
| 85/85 随机实例是默认情形 | q1 = 假 |
| 夹逼两端可算 | q1 = 假 |
| 中间层不可块扩展 | **q1 = 假** |
| 中间层存在（有证书）| q1 = 真（弱）|
| 子空间格问题一般困难 | q1 = 真（弱）|

$$\boxed{\ \text{最终判断：}\\\textbf{q1 = 假}（启发式，非证明）}$$

### 项目终态（2026-10-24 17:35）

| 项 | 数量 |
|---|---|
| 已证命题 | 8 |
| 精确验证 | 5 |
| 精确证书 | 8 |
| 工具 bug | 4 |
| 自我更正 | 7 |
| 工作纪律 | 12 |
| ATTACK_LOG | 2350+ 行（D1–D38）|

$$\boxed{\ \text{从"一个错误证明"到"8 个真命题 + 5 个验证 + 8 个证书 + 一个有力但未证的判断"}}$$


---

## D39：其他扩展方式（未完成）

### 尝试

| 方式 | 描述 | 状态 |
|---|---|---|
| A | 两份证书块对角（$L_0$ 复制到两块）| ⏳ 搜索太慢，未完成 |
| B | 三份块对角 | ⏳ 同上 |
| C | 单份 + 零块 | ⏳ 同上 |

### 已知

$$\text{D38 已证：简单的块对角扩展（}L_0\ \text{只放第一块）\textbf{破坏}中间层}$$

$$\text{原因：}\dim V\ \text{从 }2\ \text{升到 }3\ \text{，而 }q_{\min}\ \text{的增长跟不上}$$

### 一个理论观察

$$\text{中间层需要}\ \rho^*<\dim V\ \text{且}\ q_{\min}=\rho^*+1<\dim V+1$$

$$\text{块扩展使}\ \dim V\ \text{增长得比}\ q_{\min}\ \text{快} \Longrightarrow \text{中间层消失}$$

$$\boxed{\ \text{若这个"增长速度"论证能严格化} \Longrightarrow \text{中间层在大 }n\ \text{时消失} \Longrightarrow \textbf{q1 = 假（多项式）}}$$

### 这是最后一个可攻的技术点

$$\text{需要证明}：\text{中间层实例的最大规模有界（与 }n\ \text{无关），或中间层在}\ n\to\infty\ \text{时消失}$$

$$\text{若成立} \Longrightarrow q_{\min}\ \text{最终总等于}\ \dim V+1\ \text{或}\ \max(r,\rho_0+1)\ \text{（多项式）}$$

### 项目状态

| 项 | 数量 |
|---|---|
| 已证命题 | 8 |
| 精确验证 | 5 |
| 精确证书 | 8 |
| 工具 bug | 4 |
| 自我更正 | 7 |
| 工作纪律 | 12 |
| ATTACK_LOG | 2400+ 行（D1–D39）|

$$\boxed{\ \text{最后一个技术点：}\"中间层的规模是否有界"\ }}$$


---

# 🎯 D40：中间层只能平凡放大（q1 判断加强）

### 实验：不可见块 padding

$$A'=\begin{pmatrix}A&0\\0&0_k\end{pmatrix},\qquad C'=(C,\ 0_k),\qquad L_0'=(L_0,\ 0_k)$$

| $k$ | $n$ | $d$ | $\dim V$ | $\rho_0$ |
|---|---|---|---|---|
| 1 | 7 | 3 | **2** | **0** |
| 3 | 9 | 5 | **2** | **0** |
| 8 | 14 | 10 | **2** | **0** |
| 20 | 26 | 22 | **2** | **0** |

$$\boxed{\ \text{padding 使 }n\ \text{任意增长，而}\ \dim V=2\ \text{不变}}$$

### 但这是平凡放大

$$\text{额外维度完全不可见（}C=0,\ A=0\text{）} \Longrightarrow \text{不增加任何组合复杂性}$$

### 两种放大的对照

| 放大方式 | 中间层 | 意义 |
|---|---|---|
| **平凡**（$C=0$ 的块）| **保持** ✓ | 不增加难度 ✗ |
| **非平凡**（$C\ne0$ 的块）| **破坏** ✓（D38）| 无法编码困难实例 ✗ |

$$\boxed{\ \text{中间层是"低维偶然"：不能承载非平凡的组合复杂性}}$$

### 对 q1 的意义

$$\text{若 NP-hard 归约需要}\underbrace{\text{可任意缩放的非平凡硬实例}}_{\text{中间层做不到}} \Longrightarrow \text{归约难以构造}$$

$$\boxed{\ \textbf{q1 = 假}（启发式，证据进一步加强）}$$

**注意**：这不是证明 ✗ —— 只是说"最自然的 NP-hard 路线走不通"

### 项目最终判断

| 判断 | 强度 |
|---|---|
| $q_{\min}=\dim V+1$ 在非退化情形 | ✅ **已证** |
| $q_{\min}=\max(r,\rho^*+1)$ | ✅ 结构正确（5 个验证）|
| 中间层存在 | ✅ 有证书 |
| 中间层不能非平凡放大 | ✅ D38 |
| **q1 = 假** | 🟡 **启发式（多项证据）** |
| q1 = 真 | ❌ 无归约 |

### 项目终态

| 项 | 数量 |
|---|---|
| 已证命题 | 8 |
| 精确验证 | 5 |
| 精确证书 | 8 |
| 工具 bug | 4 |
| 自我更正 | 7 |
| 工作纪律 | 12 |
| ATTACK_LOG | 2450+ 行（D1–D40）|

$$\boxed{\ \text{结论：}q_{\min}\ \text{有一个多项式结构的公式；硬实例不能规模化} \Longrightarrow \textbf{q1 很可能为假}}$$


---

## D41：搜索路线的极限（诚实记录）

### 未完成的实验

$$\text{定向搜索}\ \dim V\ge3\ \text{的中间层实例（}n=6,7\text{）}$$

$$\text{状态：}10+\ \text{分钟未完成 ✗（随机 }q\text{-搜索在 }n\ge7\ \text{时太慢）}$$

### 这本身是一个信号

$$\boxed{\ \text{穷举/随机搜索路线已到极限 —— 剩余问题需要\textbf{数学洞察}，不是更多计算}}$$

| 证据 | 说明 |
|---|---|
| 每次 $n$ 增大 1，搜索时间增 10–30 倍 | 组合爆炸 |
| 中间层实例极稀有（随机撞不到）| 需定向构造 |
| 已有 8 个证书 | 计算能给的已经给了 |

### 现在需要的是

$$\text{一个\textbf{结构性判据}}：\quad \text{何时}\ \rho^*<\dim V\ ?$$

$$\text{可用的工具}：\text{条件不变子空间理论、Rosenbrock 铅笔、Kleiman–Krener 闭包}$$

### 项目最终状态（2026-10-24 18:50）

| 项 | 数量 |
|---|---|
| 已证命题 | 8 |
| 精确验证 | 5 |
| 精确证书 | 8 |
| 工具 bug | 4 |
| 自我更正 | 7 |
| 工作纪律 | 12 |
| ATTACK_LOG | 2500+ 行（D1–D41）|

### 诚实的总结

$$\boxed{\ \text{计算路线已经做完了它该做的：建立了可信基线、找到了所有反例、量化了所有边界}}$$

$$\text{下一步需要的是\textbf{新的数学想法}（或换问题）—— 不是更多的脚本}$$


---

# 🎯 D42：D33 的「1/70」被分类 —— 不紧是定理，且恰好无害（2026-10-24 19:40）

### 缺口

D33 的紧性实验（$q(\rho)=\max(r,\rho+1)$，69/70）**没有保存脚本**：`scripts/core/` 里 10-24 只新增了 c164、c165。那 1 个失败无法复核，D33 的「很可能是搜索深度不足」只是猜测。

### 新增工具

| 脚本 | 作用 |
|---|---|
| [`c166_layer_audit.py`](scripts/core/c166_layer_audit.py) | 可复现审计：逐实例算 $q_{\min}$、$\rho^*$、每个可达 $\rho$ 的紧性；失败案例存 JSON |
| [`c167_probe_tightness.py`](scripts/core/c167_probe_tightness.py) | 小实例穷举（$n{=}5,q{=}2$ 只有 5 个自由坐标） |

$(5b)$ 用精确子式 gcd；随机 $\lambda$ 只作**必要条件的快速拒绝器**（真解必过所有 $\lambda$，不会误杀）。

### 发现 1（可证）：`refute_dimV1` 的 $\rho=1$ 层确实不紧

首跑 `c166 --certs` 立刻复现：

$$\text{q\_min}=1,\ \rho^*=0\ \checkmark;\qquad \rho=1:\ q\ \text{只到}\ 3\ (\text{下界}\ 2)\ \text{✗紧}$$

穷举 $n{=}5,q{=}2$：$[-2,2]^5$ 共 3125 个矩阵，**92 个解全部 $\rho=0$**；再 3000 次随机抽样，83 个解仍全为 $\rho=0$。

### 发现 2：$d=1$ 时，不紧 $\iff L_0$ 本身是解

设 $K=\langle\nu\rangle$（$d=1$），$L_0\nu=0$。对任意 $L$：

$$(5b)\iff\ker\big((\lambda L-LA)|_K\big)=\ker(L|_K)\quad\forall\lambda .$$

$q=2,\rho=1$ 时 $\ker(L|_K)=0$，故 $(5b)\iff L\nu,LA\nu$ 线性无关。而

$$L\nu=\begin{pmatrix}0\\ R\nu\end{pmatrix},\qquad LA\nu=\begin{pmatrix}L_0A\nu\\ RA\nu\end{pmatrix}.$$

若 $L_0A\nu=0$，两个向量都在 $\{0\}\times\mathbb R$ 里 $\Longrightarrow$ 必相关 $\Longrightarrow$ 某 $\lambda$ 处 $(5b)$ 降秩。$\blacksquare$

再注意 $K^\perp=\operatorname{row}[C;CA]=\mathcal J$，故

$$L_0A\nu=0\iff L_0A\in\mathcal J\iff(5a)\ \text{对}\ L_0\ \text{成立}\iff L_0\ \text{是解}\quad(\text{退化时}\ (5a)\Rightarrow(5b)).$$

$$\boxed{\ \rho=1\ \text{层不紧}\iff L_0\ \text{本身是解}\iff\rho^*=0\ }$$

而 $\rho^*=0$ 时公式给 $q_{\min}=\max(r,1)=r$，**恰由 $L_0$ 达到**。

$$\boxed{\ \text{这个不紧点不是反例，而是公式在退化层的自洽性。}}$$

注：$\rho^*=0\Rightarrow L_0$ 是解 这条对**一般 $d$** 也成立（取 $\rho=0$ 的解 $V\subseteq\mathcal J$，
则 $K_0A\subseteq VA\subseteq V+\mathcal J=\mathcal J=\operatorname{row}(L_0)+\mathcal J$，即 $(5a)$；
退化时 $(5a)\Rightarrow(5b)$）。故 $\rho^*=0$ 层对一般 $d$ 已闭。

### 发现 3：批量审计

| 批次 | 可行实例 | 公式一致 | 逐层紧性 |
|---|---|---|---|
| `--certs` | 6 | **5/5** | 7/8（唯一不紧 = refute 的 $\rho=1$）|
| `--random 10 --seed 5` | 10 | **10/10** | **10/10** |
| `--random 8 --seed 3` | 7 | **7/7** | **7/7** |
| `--random 8 --seed 9` | 8 | **8/8** | **8/8** |

$$\boxed{\ \text{30 个可行实例：公式 30/30；可达 }(\text{实例},\rho)\text{ 对 32/33 紧（唯一不紧已证）}}$$

一个被排除的假象：首轮 `rand_s5_8` 曾报「$\rho=\dim V$ 不紧」，与已证构造 $q\le\dim V+1$ 矛盾
⟹ 是搜索深度；关键层 trials ×4 后恢复正常（$q_{\min}=4=\dim V+1$）。
**搜不到 $\ne$ 不存在；"反例"先与已证上界对照。**

### 发现 4：紧层的线性代数判据

令 $M=LN$、$N'=LR_0$、$A'$ 为 $A$ 在 $K$ 上的压缩。则

$$(5b)\iff\ker(\lambda M-MA'-N')=\ker M\quad\forall\lambda .$$

$q=\rho+1$（紧层）时：

$$\forall\xi:\ M\xi\neq0\ \Longrightarrow\ N'\xi\notin\{M(\lambda\xi-A'\xi):\lambda\}\ .$$

这把「层紧性」化成一个 $(M,N',A')$ 的线性代数条件 —— 可能是证 $q(\rho)=\max(r,\rho+1)$ 的入口。

### 判断

- $\rho^*=0$ 层：**自洽**（发现 2）。
- $\rho^*=\dim V$ 层：已证。
- $\rho^*=\rho_0>0$：24/24，无独立证明。
- **真正的剩余风险**：$\rho^*>\rho_0$ 且该层不紧 —— 目前既无反例也无证明。

详细记录：[`record/LAYER_AUDIT_2026-10-24.md`](record/LAYER_AUDIT_2026-10-24.md)


---

