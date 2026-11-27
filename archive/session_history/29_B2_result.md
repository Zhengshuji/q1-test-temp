# 29 — B2 的结果：支 B 的 (A)-解集是**单点/层**，且"解数"口径需澄清

> 本文是 [CLAUDE.md](../CLAUDE.md) 的溢出记录。结论以 [FINAL.md](../FINAL.md) 为准。
> 环境：`C:\ProgramData\anaconda3-updata\envs\python312_sim\python.exe`
> （Python 3.12.12 + sympy 1.13.1 + mpmath 1.3.0；**无需新建环境**）。

---

## 0. 一句话

> 用 sympy 的 Groebner 基算出：**支 B 上，每一层 $J$（$|J|=k$）对应的 (A)-解集
> $\Omega^\star_J$ 恒为**单点**（$k=1$，$s=3,4$，共 14 个实例，基**全为一次式**）。
> ⟹ 支 B 的 (A)-增广**总个数 = $\binom{s}{k}$**（多项式）。
> 同时发现：**项目的「解数」数的不是这个**（同实例项目报 2，我们只有 1 个 $\Theta$）。

---

## 1. ✅ B2 的结果

### 1.1 设定

$\Omega^\star_J:=\{\Theta\in\mathbb{Q}^{k(s-k)}: W_J(\Theta)\ \text{满足 (A)}\}$，其中 $J\subseteq\{1,\dots,s\}$，$|J|=k$。

**(A)**（规范化坐标下）$\iff \operatorname{rank}[W_J(\Theta);\,\bar B;\,W_J(\Theta)\bar A]=\operatorname{rank}[W_J(\Theta);\,\bar B]$。

### 1.2 方法（sympy）

把"秩降"写成**子式消失**：取 $\rho:=\operatorname{rk}[W;\bar B]$（一般值），
则 (A) $\iff$ 全部 $(\rho{+}1)$ 阶子式 $=0$。因 $W_J(\Theta)$ 对 $\Theta$ **仿射**，
这些子式是 $\Theta$ 的**多项式**。

**实测：这些多项式在 $\Theta$ 上的次数 ≤ 2**（$s=3,4,5$ 都是 $\{1,2\}$）——
与项目的铅笔形式（$f_1$ 一次、$f_2$ 二次）一致 ✓

于是可用 **Groebner 基**（lex）精确判定解集。

### 1.3 🔑 主要结果：Groebner 基**恒为一次式** ⟹ 解集是**单点**

| 形状 | 实例数 | 子式个数 | **Groebner 基** | 基全为一次式？ | 解数 |
|---|---|---|---|---|---|
| $(k{=}1,s{=}3)$ | 8 | 5 | $\{t_0,\,t_1\}$ | **是** | **1** |
| $(k{=}1,s{=}4)$ | 6 | 12–15 | $\{t_0,\,t_1,\,t_2\}$ | **是** | **1** |

**独立复核**（`b2_independent_check.py`）：

| 判据 | $(1,3)$ | $(1,4)$ |
|---|---|---|
| 整数格 $(\pm4)^m$ 上的 (A)-点数 | **1**（81 点中） | **1**（729 点中） |
| Groebner 基全为一次式 | ✓ | ✓ |
| 解 | $\Theta=0$ | $\Theta=0$ |

$$\boxed{\ \Omega^\star_J\ \text{是\textbf{单点}}\ \Longrightarrow\ \text{支 B 的 (A)-增广总个数}=\#J=\binom{s}{k}\ \text{（多项式 ✓）}\ }$$

### 1.4 这直接回答了什么

$$\textbf{支 B 的 (A)-解集规模} = \binom{s}{k}\ \le\ 2^{s}\ \text{（多项式，且与实例无关）}$$

⟹ **支 B 不是硬度的候选来源**（至少对于 (A) 层面）✓

**⚠️ 但注意**：完整的"支 B 是否硬度源"还要看 **(S)**（谱条件）在该唯一点上是否成立——
本项目已有结论：支 B 的解集**零测**，且 $(1,3)=2$、$(1,4)=2\text{–}3$（见 §2 的口径问题）。

---

## 2. ⚠️ 重要发现：项目的「解数」**数的不是 (A)-解集**

### 2.1 同实例对照（`b2_compare.py`）

| 对象 | 结果 |
|---|---|
| 项目 `exact_count_14_elim.exact_count` | **2**（gcd 次数 6）|
| 我的 Groebner（(A)-系统的 $\Theta$-解数）| **1**（基 $=\{t_0,t_1\}$，解 $=\{\Theta=0\}$）|

**同一组 $(A,C,L)$ 实例**上，两个数字**不同**。

### 2.2 为什么不同：数的对象不同

| | 数的是什么 | 依据 |
|---|---|---|
| **本项目 B2** | 使 **(A)** 成立的 $\Theta$ 个数 | (A) 的子式系统的 Groebner 基 |
| **`exact_count_14_elim.py`** | **消元后一元多项式 $g(s)$ 的根数**（$s$ = 谱变量 $\lambda$）| 脚本第 3、14 行注释与实现（Cramer + 一元多项式 gcd）|

$$\Longrightarrow\ \text{项目的"解数"}\neq\#\Omega^\star\ \Longrightarrow\ \textbf{FINAL/c4 的表述需要澄清口径}\ \text{（与 [history/28](28_problem_reading_and_branchB_counterexample.md) §2 同一问题）}$$

### 2.3 建议的措辞（供采纳）

$$\text{FINAL c4}:\quad \#\Omega^\star\ \text{有多项式上界}\ \longrightarrow\
\textbf{每层}\ J\ \text{的}\ \Omega^\star_J\ \text{是单点}\ \Longrightarrow\ \text{总个数}=\tbinom{s}{k}$$

**理由**：这个陈述
- **可良定义**（数是有限的）；
- **更强**（单点，不是"上界"）；
- **与实例无关**（$=\binom{s}{k}$，只依赖 $s,k$）；
- 有 14 个实例的机器验证 + 两重独立判据（Groebner 基的线性性、整数格扫描）。

---

## 3. ⏸ 仍需做的

| # | 事项 | 说明 |
|---|---|---|
| **1** | 把 $k=1$ 的"基恒线性"从**观测**升级为**证明** | 现在只有 14 个实例；需要说明为何 (A) 的二次子式被线性组合消掉 |
| **2** | 扩到 $k\ge2$ | $\Theta$ 是 $k\times(s-k)$ 矩阵，子式次数仍 $\le2$？基仍线性？ |
| **3** | 与 **(S)** 合起来 | (A)-解唯一，但该点处 (S) 是否成立？若恒不成立 ⟹ 支 B 无解（与"零测"一致）|
| **4** | 与项目"解数 2"**彻底对齐** | 需要项目脚本的作者确认它数的是 $s$ 的根还是 $\Theta$ 的点 |

---

## 4. 本轮交付的脚本（均用 `python312_sim` 运行）

| 脚本 | 用途 |
|---|---|
| `scripts/core/b2_elim.py` | 符号化 (A)-系统，报告子式个数与次数 |
| `scripts/core/b2_bound.py` | Bézout 界 $2^{m}$ vs 商环维数 |
| `scripts/core/b2_verify.py` | 打印 Groebner 基与解 |
| **`scripts/core/b2_structure.py`** | ⭐ 14 个实例的基线性性检验（**主结果**）|
| **`scripts/core/b2_independent_check.py`** | ⭐ 独立复核（整数格扫描 + Groebner）|
| `scripts/core/b2_compare.py` | 项目解数 vs $\Theta$-解数 的对照 |
| `scripts/core/b2_shapes.py` | 矩阵形状核对 |

**运行方式**：
```powershell
& "C:\ProgramData\anaconda3-updata\envs\python312_sim\python.exe" scripts\core\b2_structure.py
```

---

## 5. 教训 / 备注

| # | 备注 |
|---|---|
| 1 | **sympy 环境不必新建** —— `python312_sim` 已有 1.13.1 + mpmath ✓（`python312` 反而缺 mpmath）|
| 2 | **行堆叠不能逐元素相加** —— $\bar B$ 是 $k\times d_C$、$W$ 是 $(r{+}k)\times d_C$，我第一次写成 `W[i] + BAT[i]` 就 IndexError ✗ |
| 3 | **"解数"必须先问数的对象** —— 本轮再次证实（同一实例两个数字：2 vs 1）|
| 4 | **Groebner 基的"线性性"是个强信号** —— 它把"有限解"加强为"唯一解"，且给出显式解 |
