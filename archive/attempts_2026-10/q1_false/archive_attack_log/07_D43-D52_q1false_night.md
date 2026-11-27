> **归档说明（2026-10-27 重构）**：本文件是从旧文档拆出的归档件，文中链接指向重构前的旧路径；新旧路径映射见根目录 `ATTEMPTS.md` 与 `README.md`。

# 攻击日志 · D43–D52（拆分自 ATTACK_LOG.md）

> 原文：`archive/attack_A2V0/ATTACK_LOG.md`。

# 🔬 D43：Q1-FALSE 夜班 —— $r\ge2$ 检验 + 压缩判据（2026-10-24 20:25）

> 方向：**Q1-FALSE**（证 q1 = 假）。详见 [`record/Q1FALSE_2026-10-24.md`](record/Q1FALSE_2026-10-24.md)。

### 结果 1：公式的 $r$ 分支首次被检验（20/20）

此前所有实例 $L_0$ 都只有 1 行，$q_{\min}=\max(r,\rho^*+1)$ 的 $r$ 分支从未测过。
给 `c166` 加 `--r`：

| 批次 | 可行 | 公式一致 | 紧性 |
|---|---|---|---|
| `--r 2`，seed 21 | 11 | **11/11** | **11/11** |
| `--r 2,3`，seed 22 | 9 | **9/9** | **9/9** |

$$\boxed{\ r\ge2\ \text{与公式一致（20/20），}r\ \text{分支无反例}\ }$$

### 结果 2：压缩的判据与一个反例

定义 $F=\operatorname{span}\{(\langle\mathcal V_i,y\rangle)_i:y\in K+AK\}\subseteq\mathcal V^*$。可证：

$$\boxed{\ K_0^\perp\not\subseteq F\ \Longrightarrow\ \exists\ \text{超平面}\ H\supseteq K_0\ \text{且}\ H\ \text{是解}\ }$$

（证明：$(5a)$ 由 $H+\mathcal W=\mathcal V$ 自动；$(5b)$ 的坏超平面集 $\subseteq P(F\cap K_0^\perp)$，
可容许超平面开稠。）

**但**在 `counterexample_refute_dimV1` 的 $q{=}3,\rho{=}1$ 解上：

$$\dim F=2,\ \dim K_0^\perp=2,\ F\cap K_0^\perp=K_0^\perp\ \Longrightarrow\ \text{条件不成立};$$

而该实例的 $q{=}2$ 解**不在这个 $\mathcal V$ 里**（$\rho$ 降到 0，解落在 $\mathcal J$ 内）。

$$\boxed{\ \text{"在给定解内下降"被否掉 ⟹ CP 必须写成全局形式：}\exists\ \text{解}\ \dim=\max(r,\rho+1)\ \text{即可，不必}\subseteq\mathcal V\ }$$

### 工具

- [`q1_false/tests/cp_check.py`](q1_false/tests/cp_check.py)：判定条件并显式构造 $H$
- [`q1_false/THE_LEMMA.md`](q1_false/THE_LEMMA.md) §4.3–4.4：判据、引理、反例、全局 CP

### 下一步

1. 造一个 $K_0^\perp\not\subseteq F$ 的非极小解，给引理找**数值正例**；
2. 弱化 CP：只证"存在更小的解"（任何 $\rho'\le\rho$），迭代后分析极限；
3. 单独攻 $r>\rho+1$ 分支（$q_{\min}=r\iff L_0$ 是解），可能比一般 CP 容易。


---

# 🎯 D44：引理 4.3 的正例 + 局部下降算法（只解顶层）（2026-10-24 20:50）

### 结果 1：引理 4.3 有正例（5/5）

构造非极小解：$w\in\mathcal J$，$Aw\in V_0+\mathcal J$，$w\perp A(Z)$（$Z=K\cap V_0^\perp$）。
这是 $w$ 的线性条件（解空间维 2），得到的 $V'=V_0+\langle w\rangle$ 仍是解。
再跑判据并显式构造 $H$：

| 实例 | $V'$ ($q,\rho$) | $\dim F$ | $\dim K_0^\perp$ | 交 | $H$ 解？ |
|---|---|---|---|---|---|
| refute | 2,0 | 0 | 1 | 0 | ✅ |
| middle | 3,1 | 2 | 2 | 0 | ✅ |
| rhostar | 3,1 | 2 | 2 | 0 | ✅ |
| candidate | 4,2 | 3 | 3 | 2 | ✅ |
| d4 | 4,2 | 3 | 3 | 2 | ✅ |

**推论检验**（极小解必须 $K_0^\perp\subseteq F$）：5/5 成立 —— 与引理自洽。

### 结果 2：下降算法保持 $\rho$，因此只解出**起始层**

每步取超平面 $H$ 且 $H+\mathcal W=\mathcal V\Rightarrow\pi(H)=\pi(\mathcal V)$：

$$\boxed{\ \rho\ \text{在下降中不变}\ \Longrightarrow\ \text{只得到}\ q(\rho_{\rm start})\ }$$

| 实例 | 初始 $(q,\rho)$ | 下降后 | $q(\rho_{\rm start})$ | $\rho^*$ | 命中 |
|---|---|---|---|---|---|
| refute | 2, **0** | **1** | 1 | 0 | ✅ |
| candidate | 3, 2 | 3 | 3 | 2 | ✅ |
| d4 | 3, 2 | 3 | 3 | 2 | ✅ |
| middle_layer | 3, **2** | 3 | 3 | **1** | ❌ |
| rhostar | 3, **2** | 3 | 3 | **1** | ❌ |

$$\boxed{\ \text{下降命中}\ q_{\min}\iff\rho_{\rm start}=\rho^*\ }$$

refute 成功是因为初始解恰在 $\rho=0$ 层，**不是**因为 $q_{\min}=\dim V+1$（那里 $1\ne2$）。

### 结论：项目被压成一个动作

$$\boxed{\ \text{如何把}\ \rho\ \text{降 1（保持是解）？}\ }$$

障碍：$\mathcal V'$ 需要 $\bar{\mathcal V}$ 的 $A$-不变子空间，实数域上不一定存在
—— 这解释了中间层为何稀有，也说明"降 $\rho$"可能根本不可行（若可证，则下降算法即多项式算法）。

### 新工具

- [`q1_false/tests/lemma43_positive.py`](q1_false/tests/lemma43_positive.py)：构造正例 + 推论检验
- [`q1_false/tests/descent_algorithm.py`](q1_false/tests/descent_algorithm.py)：局部下降
- [`q1_false/THE_LEMMA.md`](q1_false/THE_LEMMA.md) §4.5：算法、$\rho$ 不变性、实验


---

# 🔍 D45：中间层证书拆解 —— 两个解互不包含（2026-10-24 21:10）

> Q1-FALSE 方向。脚本 [`q1_false/tests/rank_drop_analysis.py`](q1_false/tests/rank_drop_analysis.py)。

### 结构对比（`certificate_middle_layer.json`，$n{=}6$）

| | $V_2$（证书） | $V_3$（顶层解） |
|---|---|---|
| $\dim$ | 2 | 3 |
| $\rho$ | 1 | 2 |
| $\dim(V\cap\mathcal J)$ | 1 | 1 |
| $K_0^\perp\subseteq F$（层内极小判据）| ✅ | ✅ |

$$\dim(V_2+V_3)=4,\qquad \dim(V_2\cap V_3)=1,\qquad V_2\not\subseteq V_3,\quad V_3\not\subseteq V_2 .$$

### 三条推论

$$\boxed{\ \text{“降}\rho\text{”不是子空间操作 —— 必须另起一个与}\ V_3\ \text{横截的解}\ }$$

$$\boxed{\ K_0^\perp\subseteq F\ \text{只判“层内极小”，不判全局 —— 两个解都满足它}\ }$$

$$\boxed{\ \text{下降 + 局部判据不可能单独解决 q1，需独立的“构造}\ \rho-1\ \text{层解”方法}\ }$$

### 方向判断

- 局部（层内）问题：**已解决**（引理 4.3 + 下降）；
- 全局问题：**只剩“跨层”**，而跨层不是子空间关系 ⟹ 必须用构造（不是搜索/下降）。

### 下一步

1. 从 $V_2$ 的形态反推构造：$q{=}2,\rho{=}1$ 时 $M$（$2\times d$）的核是 $d-1$ 维，
   铅笔条件退化成对单个 $\xi$ 的条件 —— 可能在 $\rho=1$ 层可以**完全刻画**并可构造。
2. 若 $\rho=1$ 层可构造，再看 $\rho=k$ 的归纳。这是目前最具体的入口。


---

# 📐 D46：$\rho=1$ 层的完全刻画（2026-10-24 21:40）

> Q1-FALSE 方向。脚本 [`q1_false/tests/rho1_characterization.py`](q1_false/tests/rho1_characterization.py)。

### 定理

设 $q=2$、$\operatorname{rank}(LN)=1$，$M=LN=uv^{\mathsf T}$（$u\in\mathbb R^2$，$v\in\mathbb R^d$ 非零）。则

$$\boxed{\ (5b)\iff\exists\,y\in\mathbb R^2\setminus\operatorname{span}\{u\}:\quad
LN=uv^{\mathsf T},\quad LR_0=-u\,(A'^{\mathsf T}v)^{\mathsf T}+y\,v^{\mathsf T}\ }$$

证明：$\ker M=v^\perp$；写 $N'\xi=a(\xi)u+b(\xi)z$（$z\not\parallel u$）。
$v^\perp$ 上要求 $a=-w^{\mathsf T}$（$w=A'^{\mathsf T}v$）；$v^\perp$ 外要求 $b\ne0$，即 $b=c\,v^{\mathsf T}$。
合并得 $y=cu+cz\notin\operatorname{span}u$。$\blacksquare$

### 验证

| 实例 | $M=uv^{\mathsf T}$ | C1: $b\propto v$ | C2: 行 $\propto v$ |
|---|---|---|---|
| `middle_layer`（$v=(1,-2)$）| ✅ | ✅ $c=-1/3$ | ✅ |
| `rhostar`（$v=(0,1)$）| ✅ | ✅ | ✅ |

### 意义

固定 $(u,v)$ 后方程对 $L$ **线性**，$y$ 只受开条件约束。于是

$$\rho=1\ \text{层存在}\iff\exists(u,v)\in P^1\times P^{d-1}:\ \text{线性方程组有解且}\ y\notin\operatorname{span}u .$$

参数空间只有 $d$ 维（$d=2$ 时二维），这是把它压成多项式算法的具体入口。


---

# ⚙️ D47：$\rho=1$ 判定器 —— 多项式、可构造、优于搜索（2026-10-24 22:10）

> Q1-FALSE 方向。脚本 [`q1_false/tests/rho1_solver.py`](q1_false/tests/rho1_solver.py)、
> 对拍 [`compare_rho1.py`](q1_false/tests/compare_rho1.py)。

### 参数塌缩：$v$ 由 $L_0$ 直接给出

$$L_0N=u_1v^{\mathsf T}\Longrightarrow
\begin{cases}\alpha_0\neq0:& v\propto\alpha_0,\ u_1=1;\\ \alpha_0=0:& u=(0,1),\ v\propto L_0R_0\ (L_0R_0=0\Rightarrow\text{无解}).\end{cases}$$

剩下对 $(\ell,t,y_2)$ **线性**，加开条件 $y\notin\operatorname{span}u$。不需要搜索 $(u,v)$。

### 验证

| 验证 | 结果 |
|---|---|
| 5 个证书 | middle/rhostar **构造成功**；refute/candidate/d4 无解 —— 与已知真值全部一致 |
| 定向实例（$\rho_0{=}0$，13 个）| 5 次构造，**全部经 c164 可信基线复核通过**；其中 **3 个是随机搜索漏掉的** |
| 普通随机实例 5 个 | 5/5 一致 |

$$\boxed{\ \text{判定器 \textbf{sound}：True 必有构造解且经精确复核；False 依赖 §4.7 定理 + }(5a)\text{ 抽样}\ }$$

### 结构进展

| 层 | 判定 | 复杂度 |
|---|---|---|
| $\rho^*=0$ | $L_0$ 是解 | 多项式 |
| $\rho^*=1$ | 本判定器 | 多项式 |
| $\rho^*=\dim V$ | 构造 | 多项式 |
| $2\le\rho<\dim V$ | ❌ | — |

$$\boxed{\ \text{q1 的可判定性问题，现在只剩中间层 }2\le\rho<\dim V\ }$$

### 下一步

把 §4.7 的模板推广到 $\rho=k$：$M=LN$ 是 $q\times d$ 的秩 $k$ 矩阵，
$M=UV^{\mathsf T}$（$U\in\mathbb R^{q\times k}$，$V\in\mathbb R^{d\times k}$）；
铅笔条件给出 $N'=-U(A'^{\mathsf T}V)^{\mathsf T}+Y V^{\mathsf T}$ 形式的方程，
$Y\in\mathbb R^{q\times k}$ 且某个开条件。$k=1$ 的全部论证应该能逐字推广。


---

# 🧮 D48：一般 $\rho=k$ 的铅笔化简 —— 以及为什么 $k=1$ 特殊（2026-10-24 22:40）

> Q1-FALSE。脚本 [`q1_false/tests/rho_k_structure.py`](q1_false/tests/rho_k_structure.py)。

### 定理（一般 $k$）

对任意解 $L$，令 $M=LN=UV^{\mathsf T}$（$U$ 为 $q\times k$、$V$ 为 $d\times k$，均满列秩），$W=A'^{\mathsf T}V$。则

$$LR_0=-UW^{\mathsf T}+YV^{\mathsf T}\quad(Y\ \text{唯一}),\qquad
\lambda M-MA'-N'=(\lambda U-Y)V^{\mathsf T},$$

$$\boxed{\ (5b)\iff\operatorname{rank}(\lambda U-Y)=k\ \ \forall\lambda\ }$$

即 $k$ 列铅笔**无实广义特征值**。

### 验证

| 实例 | $q$ | $k$ | $d$ | 结构式 | 铅笔满秩 |
|---|---|---|---|---|---|
| `candidate` | 3 | 2 | 3 | ✅ | ✅ |
| `d4` | 3 | 2 | 4 | ✅ | ✅ |
| `middle_layer` | 2 | 1 | 2 | ✅ | ✅ |
| `rhostar` | 2 | 1 | 2 | ✅ | ✅ |

### 为什么 $k=1$ 能解、$k\ge2$ 不能照搬

$$\boxed{\ k=1:\ y\notin\operatorname{span}\{u\}\ \text{是线性条件};\qquad k\ge2:\ \text{是真正的谱条件}\ }$$

一维时"线 $\lambda u$ 不经过 $y$"就是一个不等式；$k\ge2$ 时"铅笔 $\lambda U-Y$ 不满秩"
是一族（实）广义特征值 —— 不再是线性的。

### 意义

$$\text{问题从 }n\text{ 维原数据}\ \longrightarrow\ k\text{ 列铅笔}\qquad(k\le\dim V\le d\ll n)$$

这是真正的降维，但 $k\ge2$ 的存在性仍需在 $(U,V,Y)$ 上处理。

### 下一步

1. 对 $k=2$ 试：用 $L_0$ 的数据把 $V$ 的一部分定下来（$k=1$ 时 $v\propto\alpha_0$ 或 $L_0R_0$），
   看剩多少自由度。
2. 若 $(U,V)$ 能被 $L_0$ 定死，则 $Y$ 的方程仍线性，条件变成"线性族的解里有几个点满足谱条件"——
   这是可判定的（判别式/结式）。


---

# 🧱 D49：$k=2$ 的 $V$ 不被线性结构钉住（负结果）（2026-10-24 23:10）

> Q1-FALSE。脚本 [`q1_false/tests/k2_V_scan.py`](q1_false/tests/k2_V_scan.py)。

### 实验

`candidate`（$n{=}5,d{=}3,k{=}2$，$\alpha_0=(1,1,0)$），参数化

$$V(t)=\operatorname{span}\{\alpha_0,\ \beta(t)\},\qquad t\in\{-2,-1,0,1,2,\pm\tfrac12\}.$$

对每个 $t$，解 $(L,U,Y)$ 的线性系统（$LN=UV^{\mathsf T}$，$LR_0=-UW^{\mathsf T}+YV^{\mathsf T}$）：

$$\boxed{\ \text{全部 }7\ \text{个 }t\ \text{都可解}\ }$$

### 结论（负）

$$\boxed{\ k=1\ \text{的"由 }L_0\text{ 定死 }v\text{"不推广；}k=2\text{ 的 }V\text{ 有连续族，线性结构不区分}\ }$$

所以 $k\ge2$ 的判定**必须**引入 $(5a)$（或另一个判别式），不能靠线性塌缩。
这与 D45 的"两个解互不包含"一致：**跨层的自由度本质上不是线性的**。

### 对 Q1-FALSE 路线的影响

- $k=1$ 的多项式判定器（D47）是**真的特殊**，不是模板；
- $k\ge2$ 要么找到新的非线性判别式（如 $(5a)$ 的秩条件的代数化），要么这条路走不通；
- 若 $k\ge2$ 不可判，则"$q_{\min}$ 多项式可算"只能覆盖 $\rho^*\in\{0,1,\dim V\}$ 的实例。

### 今天 Q1-FALSE 的总账

| 条目 | 结果 |
|---|---|
| D42 | $\rho^*=0$ 已证；30/30 |
| D43 | $r\ge2$ 20/20；引理 4.3 + "内部下降"反例 |
| D44 | 引理 4.3 正例 5/5；下降算法（保持 $\rho$）|
| D45 | 中间层两解互不包含 |
| D46 | $\rho=1$ 刻画 |
| D47 | $\rho=1$ 多项式判定器（sound，优于搜索）|
| D48 | 一般 $k$ 铅笔化简 $n\to k$ |
| D49 | $k=2$ 的 $V$ 不被钉住（负）|

$$\boxed{\ \text{多项式可判定层：}\rho^*\in\{0,1,\dim V\};\qquad 2\le\rho<\dim V\ \text{仍开放}\ }$$


---

# 🎁 D50：$(5a)$ 是自动的（重要简化）（2026-10-24 23:40）

> Q1-FALSE。脚本 [`q1_false/tests/k2_V_scan.py`](q1_false/tests/k2_V_scan.py)。

### 定理

若 $LN=UV^{\mathsf T}$、$LR_0=-UW^{\mathsf T}+YV^{\mathsf T}$（$U$ 列满秩，$W=A'^{\mathsf T}V$），则 $(5a)$ **自动成立**。

*证明*：$(5a)\iff\ker L\cap K\subseteq\ker(LA)$。取 $x=N\xi\in\ker L\cap K$：$UV^{\mathsf T}\xi=0\Rightarrow V^{\mathsf T}\xi=0$，于是

$$LAx=(LN)A'\xi+(LR_0)\xi=UW^{\mathsf T}\xi-UW^{\mathsf T}\xi+YV^{\mathsf T}\xi=0.\ \blacksquare$$

### 实验（`candidate`，$d{=}3$）

| $t$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $\pm\frac12$ |
|---|---|---|---|---|---|---|
| $(5a)$ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| $(5b)$ gcd | 2 | 2 | **0** | 2 | 2 | 2 |

$$\boxed{\ \text{结构方程的解全部自动满足 }(5a);\ \text{钉住 }V\ \text{的是\textbf{谱条件}}\ }$$

### 修正

D49 的措辞要更正：不是"$(5a)$ 才是关键约束"，而是 **$(5a)$ 免费，谱条件才是**。

### 现在 $k\ge2$ 的精确形式

$$\exists\,V:\quad \text{线性系统（结构方程）有解，且解空间含一个"铅笔 }\lambda U-Y\text{ 无实特征值"的点}.$$

$$\boxed{\ \text{问题彻底变成：线性系统的解空间}\ \cap\ \{\text{谱条件}\}\ \neq\ \emptyset\ ?\ }$$

这正是代数几何可以处理的形式（判别式/结式），比原来的"子空间最优化"干净得多。


---

# 🎯 D51：谱条件只依赖 $V$ —— 全好／全坏二分（2026-10-24 24:00）

> Q1-FALSE。脚本 [`q1_false/tests/k2_V_scan.py`](q1_false/tests/k2_V_scan.py)。

### 实验（`candidate`，$d{=}3$，每个 $t$ 采样 ~57 个满秩点）

| $t$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $\pm\tfrac12$ |
|---|---|---|---|---|---|---|
| 满足 $(5b)$ 的样本 | 0/57 | 0/57 | **57/59** | 0/57 | 0/57 | 0/57 |

$$\boxed{\ \text{每个 }V\ \text{的解空间是\textbf{全好}或\textbf{全坏} —— 谱条件只依赖 }V\ }$$

这与"坏集是闭的、解空间是不可约仿射空间"一致：要么整体落在坏集里，要么通有满足。

### 推论

$$\boxed{\ \exists V:\ \text{解空间}\cap\{\text{谱条件}\}\ne\emptyset\iff\exists V:\ \text{解空间\textbf{通有}满足}\ }$$

于是 $k=2$（$d=3$）的判定变成：**好 $V$ 的集合是否非空**，而 $V$ 只有一维参数 —— 这是
"构造性集合是否非空"的标准问题，可以用结式/判别式精确判定。

### 对算法的意义

- 实验里好 $V$ 是**孤立点**（$t{=}0$），坏集是余维 1；
- 若这个模式普遍，那么 $k=2$ 的判定 = 求一个关于 $t$ 的多项式的实根并检查 —— **多项式时间**（对固定 $d$）。

### 当前 $k\ge2$ 的完整形式

$$\exists\,V\in\mathrm{Gr}(k,d):\quad \Phi(V):=\gcd\{2\times2\ \text{子式}(\lambda U-Y)\}=1,$$

其中 $(U,Y)$ 由线性系统给出（且与解空间中的点无关，见上）。这是纯代数条件。


---

# 🤝 D52：与 Q1-TRUE 的 Z-FORM 对账 —— 发现 (8c) 缺项（2026-10-24 24:20）

> 读了 [`Q1_TRUE_HANDOFF.md`](Q1_TRUE_HANDOFF.md)，做交叉验证。回执：[`Q1_FALSE_TO_Q1_TRUE.md`](Q1_FALSE_TO_Q1_TRUE.md)。

### 发现：(8c) 原式在一个实例上假失败

`counterexample_d4`（$q{=}3$，$\dim Z{=}2$，$\dim(Z\cap K){=}2$）：

| $\lambda$ | $0,1,-1,2,-3$ | $\mathbf{5}$ | $\mathbf{3}$ |
|---|---|---|---|
| $\dim((\lambda I-A)K\cap Z)$ | 2 | **1** | **1** |
| $\dim\ker((\lambda I-A)\vert_K)$ | 0 | **1** | **1** |

该解是合法的（c164 精确验证过 $(5b)$），所以原式有误。修正：

$$\boxed{\ \dim((\lambda I-A)K\cap Z)=\dim(K\cap Z)-\dim\ker\big((\lambda I-A)|_K\big)\ }$$

修正后 4 个证书全部通过。

### 对应关系

$$Z=\ker[C;L],\quad \dim Z=n-p-q,\quad \boxed{\ \dim(Z\cap K)=d-\rho\ }$$

（4 个证书验证）⟹ 两边的"中间层"是同一个：

$$0<\dim(Z\cap K)<\dim Z\iff 0<\rho<d\ \text{且}\ \rho<\dim V .$$

### 结构不对称点

| | V-形式 | Z-形式 |
|---|---|---|
| 半不变性 | $(5a)$ **自动**（D50）| $A(Z\cap K)\subseteq Z$ **不自动** |
| 谱条件 | 铅笔 $\lambda U-Y$ | $(\lambda I-A)K$ 与 $Z$ 的交维数 |

这解释了两边"缺口"为何不同：Q1-TRUE 的缺口 A（$L_{\max}$）对应 V-形式的自动项，
而 Q1-FALSE 的缺口（谱条件）在两边都存在 —— **它是真正的硬核**。

### 结论

$$\boxed{\ \text{两个方向收敛到同一个问题：中间层（}0<\rho<\dim V\text{）的谱条件}\ }$$
