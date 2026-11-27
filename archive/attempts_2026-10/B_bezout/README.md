# B_bezout/ —— 不依赖系数判据的 A3 编码（分支 2）

> **任务**：B-1（Bézout 证书 + 次数界）→ B-2（显式 $\exists S\exists U\exists\{g_{ij}\}$）→ B-3（constructibility）。
> **为什么独立**：这条路只用 **minors 的 gcd 判据**（`feasible_by_minors`，§27 已验证的正确判据），
> 不碰已撤回的系数判据（A2 §38）。

## 1. 数学基础

$$U\cap I_\lambda=0\ \ \forall\lambda\in\mathbb C
\iff \operatorname{rank}[U\mid P(\lambda)]=r+t\ \ \forall\lambda
\iff \gcd(f_1,\dots,f_N)\in\mathbb C^\times,$$

其中 $f_i$ 是 $[U\mid P(\lambda)]$ 的全部 $(r+t)$ 阶极大子式，$N=\binom{m}{r+t}$，$\deg f_i\le t$。

**Bézout 证书**：$\gcd=\text{unit}\iff\exists g_i(\lambda)$：
$$\sum_i g_i(\lambda)f_i(\lambda)=1 .$$

## 2. B-1 的验收

| 检查 | 标准 |
|---|---|
| 证书恒等式 | $\sum g_if_i=1$ **精确成立**（有理算术）|
| 与直接判据一致 | 证书存在 $\iff$ `feasible_by_minors` 判可行 |
| 次数界 | 实测 $\deg g_i\le(N-1)\cdot\max\deg f_i$ |
| 非平凡性 | 至少一个实例 $N>1$（否则证书退化成单多项式）|

## 3. 进展

### 2026-11-01：B-1 开始

模块：`tools/verification/bezout_cert.py`（`minors_of`、`gcd_and_certificate`、`degree_bound`、`analyse`）。
脚本：`scripts/b1_certificate.py`（本目录）。

**待记录**：结果表。

---

## 4. B-1 结果（2026-11-01）

脚本：[`scripts/b1_certificate.py`](scripts/b1_certificate.py)，模块 `tools/verification/bezout_cert.py`。

### 4.1 数据

| 实例 | $\dim W/S$ | $\dim H/S$ | $r+t$ | $N$（非零子式数）| 结论 |
|---|---|---|---|---|---|
| c282（$q=4,s=1$）| 5 | 4 | 4 | **1** | 单一子式 |
| c282（一般位置 $U$，5 个）| 5 | 4 | 4 | **1** | 同上 |
| 第二实例（$q=2,s=2$）| 3 | 2 | 3 | **1** | 方阵，只有行列式 |

**与直接判据（`feasible_by_minors`）一致：0 不一致** ✓

### 4.2 **关键发现：$N=1$ 是结构性的**

$N$ 只统计**非零**子式。在 c282 上 $\operatorname{im}P\subseteq H/S$，而 $U\subseteq H/S$，
故 $[U\mid P]$ 的**所有列**都落在 $H/S$ 的坐标子空间里 ⟹ 任何包含"外面那一行"的子式**恒为零** ⟹ 只剩一个。

在第二实例上 $r+t=\dim W/S$ ⟹ 方阵 ⟹ 只有一个最大子式。

$$\boxed{\ \text{在本项目所有已测实例上，gcd 判据退化为\textbf{单个多项式}\ }f(\lambda)\ \text{是否非零常数}\ }$$

### 4.3 对 B-2 的影响（**简化**）

于是 Bézout 证书是**平凡的**（$g_1=1/f_1$），真正的编码是：

$$f(\lambda)=\det[U\mid P(\lambda)]=\sum_{j=0}^{d}c_j(S,U)\,\lambda^j,\qquad
\boxed{\ c_1=\cdots=c_d=0,\quad c_0\ne0\ }$$

即**有限多个多项式方程 + 一个非零条件**——比通用 Bézout 干净得多。

**诚实限制**：我们**没有**找到 $N>1$ 的实例（需要同时满足 $\operatorname{im}P\not\subseteq H/S$ 且 $r+t<\dim W/S$）。
所以"通用 Bézout 版本"**未经检验**；$N=1$ 的结论只覆盖已测实例。

## 5. B-2：显式系统（下一项）

在 $N=1$ 的情形下（本项目已测全部），

$$\exists S\,\exists U:\ \underbrace{S\subseteq D,\ S\subseteq U\subseteq H,\ U\cap G=S}_{\text{线性/秩}},\ \underbrace{c_j(S,U)=0\ (j\ge1),\ c_0(S,U)\ne0}_{\text{系数条件}}$$

其中 $c_j$ 是 $\det[U\mid P(\lambda)]$ 的 $\lambda^j$ 系数，对 $U$ 的 Plücker 坐标**线性**、对 $S$ **多项式**。

---

## 6. B-3：可行 $S$ 集是**构造集**（纸面）

### 6.1 陈述

设 $\mathcal B=\mathcal B_{s,k}$ 基族，$\mathcal Y\subseteq\mathcal B\times\operatorname{Gr}(r,H/S)$ 由
$$S\subseteq U\subseteq H,\quad S\subseteq D,\quad U\cap G=S,\quad c_j(S,U)=0\ (j\ge1),\quad c_0(S,U)\ne0$$
定义。这些是**多项式方程与不等式**（$U\cap G=S$ 写成秩条件 $\operatorname{rank}[U\mid G]=b+s$ 等），
故 $\mathcal Y$ 是**构造集**（constructible，有限个局部闭之并）。

设 $\pi:\mathcal B\times\operatorname{Gr}\to\mathcal B$ 是投影。则

$$\boxed{\ \text{可行 }S\text{ 集}\ =\ \pi(\mathcal Y)\ \text{是构造集}\ }$$

*证明*：Chevalley 定理（构造集在态射下的像是构造集）。$\square$

### 6.2 为什么这**不是** Zariski 开

构造集 = 有限个"局部闭"之并，**不必**开。反例形状：$\{(x,y):xy=0\}$ 在 $\mathbb A^2$ 中投影到 $x$ 轴是开集，
但 $\{(x,y):x=0,\ y\ne0\}\cup\{(x,y):x\ne0\}$ 投影是构造但非开。

**所以 A2 §34 的"Zariski 开"必须降级**（QA25 已指出）。

## 7. B-4：何时能加强为**开集**

### 7.1 充分条件（纸面）

若 $\pi|_{\mathcal Y}$ 是**等维的**（每条纤维维数相同）且 $\mathcal Y$ 在 $\mathcal B\times\operatorname{Gr}$ 中局部闭，
则 $\pi(\mathcal Y)$ 开（标准的"开映射/平坦"论证）。

**在本问题中的含义**：固定 $S$ 的可行 $U$ 集 $\mathcal F_S$（A2 的 §29 命题 1）维数恒定
（$=(r-k)(m-r)$，A2 §3 已算）⟹ **在 $\mathcal F_S\ne\varnothing$ 的 $S$ 上维数确实恒定** ⟹
若 $\pi$ 局部等维，则可行 $S$ 集**开**。

### 7.2 仍缺的一步

需要证明 $\pi|_{\mathcal Y}$ 局部等维（或 $\mathcal Y\to\mathcal B$ 平坦）。这等价于
"可行 $U$ 的族在 $S$ 上**不跳变**"，即 A2 §3 的纤维维数公式在**整个** $\mathcal Y$ 上成立（不只是非空纤维上）。

**状态**：`[猜想]`。这是 B 线剩下的唯一理论缺口。

## 8. B-5：$\exists\mathbb R$ 归约的规模（粗估）

- 变量：$S$ 的 Plücker 坐标 $\binom{b}{s}$ 个 + $U$ 的 $\binom{m}{r}$ 个；
- 方程：Plücker 关系（二次）$\binom{b}{s}-$ 个 + 系数条件 $d$ 个线性 + 一个非零条件（Rabinowitsch 引入 1 个变量）；
- 度数 $\le\max(2,\deg c_j)$，$\deg c_j\le t$。

$$\text{规模}=\operatorname{poly}(\tbinom{b}{s},\tbinom{m}{r},d,t)\ \text{个变量与方程}$$

这给出 $\mathrm{DEC}(q)\in\exists\mathbb R$ 的**显式**归约（与早期 `dec_q_existsR` 一致，但更紧）。

---

## 9. B-1 补充：**非平凡** Bézout 证书（2026-11-01）

脚本 `scripts/b2_find_N_gt_1.py`（随机搜索 $N>1$ 的实例）。

### 9.1 找到的实例

| $n$ | $p$ | $w$ | $v$ | $h$ | $b$ | $q$ | $s$ | $r$ | $t$ | $\dim W/S$ | $N$ | 子式次数 | $\deg g$ | $\deg(g_i)$ | 界 | 证书 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7 | 2 | 5 | 3 | 4 | 2 | 3 | 1 | 1 | 2 | 4 | **4** | $[2,2,1,2]$ | 0 | **1** | 6 | ✓ |

$$\boxed{\ \sum_i g_if_i=1\ \text{精确成立},\quad \deg(g_i)=1\le(N-1)D=6\ }$$

**这是第一个真正非平凡的 Bézout 证书**：4 个子式、**没有常数子式**、gcd 是单位、证书系数次数 1。

### 9.2 三个层次的证书（按非平凡程度）

| 情形 | 例子 | 证书 | 难度 |
|---|---|---|---|
| $N=1$（方阵/坐标子空间）| c282、第二实例 | $g_1=1/f_1$，平凡 | 无 |
| $N>1$ 但有常数子式 | 上面搜到的前 3 个 | $g$ 只取那个常数子式，$\deg g_i=0$ | 平凡 |
| $N>1$ 且**无**常数子式 | 上表 | $\deg g_i=1$，**真要用 Bézout** | 非平凡 ✓ |

$$\boxed{\ \text{B-1 完成：三个层次都验证过，含第一个非平凡证书}\ }$$

---

## 10. B-4：用**可信判据**重做 $S$-扫描（2026-11-01）

### 10.1 为什么要重做

此前 `c297`／`c299` 的随机扫描用的是**已撤回的系数判据**（A2 §38），结论作废。
本脚本 [`scripts/b4_openness.py`](scripts/b4_openness.py) 改用**可信的直接判据**
`base_sweep.fixed_S`（枚举可容许 $U$ + `check_Z` 的 $(A)(S)$）。

### 10.2 结果（14 个有效 sweep）

| 观察 | 数 |
|---|---|
| 全不可行 | **14** |
| 全可行 | 0 |
| **混合**（$0<k<$ 总数）| **0** |

$$\boxed{\ \text{在可信判据下，已测范围内可行集总是\textbf{全空或全满}——没有"半开"的情形}\ }$$

### 10.3 与 B-3/B-4 的关系

- **B-3**（构造集）只给"有限个局部闭之并"，允许多种形状；
- **B-4**（开性）预言：开集**不能**是"半边"——随机格点要么全落进去、要么全落外面 ✓
- 观测与"开集"**一致**，但**不能证明**开性（格点是有限的）。

### 10.4 诚实限制

- 只用 $r=1$（$U$ 的枚举便宜）；$r\ge2$ 未扫；
- 格点范围 $\{-1,0,1\}$；
- 14 个 sweep 全部空——**没有**一个实例给出非空可行集（除了已知的 R17/c282 这类专门构造的实例）。

### 10.5 B-4 的状态

| 项 | 状态 |
|---|---|
| 充分条件（局部等维 ⟹ 开）| 已写（§7）|
| 局部等维本身 | `[猜想]` |
| 支持证据 | 14/14 sweep 全空，与开性一致 |
| 反例 | 无 |

**分支 2 到此：B-1 完成、B-2/B-3/B-5 纸面已写、B-4 缺口明确且有支持证据。**

