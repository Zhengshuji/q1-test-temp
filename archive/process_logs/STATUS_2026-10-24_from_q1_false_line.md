# Q1-FALSE 状态（2026-10-24 收盘）

> 方向：证明 q1 = 假（$q_{\min}$ 多项式可算）。本文是**唯一的状态入口**；
> 过程日志见 [ATTACK_LOG](../ATTACK_LOG.md) D42–D52，细节见 [THE_LEMMA](THE_LEMMA.md)。

---

## 0. 一句话

$$\boxed{\ \text{层公式已推翻（2026-10-25）；修正形式 } q_{\min}=\max(r+\delta,\ \rho^*+1)\ \text{与全部 66 个实例一致}\ }$$

---

## 1. 化归链

$$q_{\min}=\min_{\rho}q(\rho),\qquad q(\rho)=\min\{\dim\mathcal V:\operatorname{rank}(\mathcal V N)=\rho,\ (5a)\wedge(5b)\}$$

$$\text{原经验公式（}\textbf{已推翻}\text{）：}\ q_{\min}=\max(r,\ \rho^*+1),\qquad \rho^*=\min\{\rho:q(\rho)<\infty\}$$

**反例**（`lit/counterexample_refute_layer_formula_2026-10-25.json`，独立复核）：

$$n{=}5,\ p{=}2,\ r{=}2,\ d{=}1,\ \dim V{=}1,\ \rho_0{=}0;\quad
q_{\min}=3>\max(r,\rho^*+1)=\max(2,2)=2 .$$

机制：$q=r$ 时 $\mathcal V$ 只能是 $\operatorname{row}(L_0)$，故 $L_0$ 必须是解；这里 $(5a)$ 对 $L_0$ 失败。

**修正形式**（下界已证，等号是猜想）：

$$\boxed{\ q_{\min}=\max\big(r+\delta,\ \rho^*+1\big)},\qquad
\delta=\begin{cases}0,& L_0\ \text{本身是解}\\1,& L_0\ \text{不是解}\end{cases}$$

- 下界：$q\ge r+\delta$（$L_0$ 不是解时 $q=r$ 会迫使 $L_0$ 是解，矛盾）与 $q\ge\rho+1$；
- 与全部 $66$ 个已核实例一致（65 个审计实例 + 上述反例）；
- 原公式只在 $r\le\rho^*$（或 $L_0$ 是解）时与修正版一致；反例恰在 $r>\rho^*$ 的边界上。

$$\boxed{\ \text{推论：Q1′（最小层紧）为\textbf{假} —— 反例中 } q(\rho^*)=3\ne\max(r,\rho^*+1)=2\ }$$

### 1.1 "两个机制取大"的检验（$r>\rho^*$ 区域，299 实例）

在反例所在区域（$d{=}1$、$L_0\subseteq\mathcal J$ 故 $\rho_0{=}0$、$L_0$ 不是解、$r\in\{2,3\}$）随机造实例：

| $r$ | 找到 $q{=}r+1$ 解 | 精确？ |
|---|---|---|
| 2 | 165 | ✅（下界 $r+1$ 由 $L_0$ 不是解给出）|
| 3 | 134 | ✅ |

$$\boxed{\ \text{299/299：}q_{\min}=r+1=\max(r+\delta,\ \rho^*+1)\ \text{（因为 }\rho^*\le1<r\text{）}\ }$$

即该区域里"行数机制"（$r+\delta$）完全压过"秩机制"（$\rho^*+1$），且**可达性与下界都闭合**。

所以"两个机制取大"的图像在 $r>\rho^*$ 一侧被 299 个实例支持；
风险只剩 $r\le\rho^*$ 一侧——那里需要中间层紧性（Q1′ 已被推翻，但已知的中间层只有 $\rho^*{=}1$ 且都紧）。

### 1.2 $r{=}1$ 通道的排查（唯一还能推翻修正公式的通道）

用 D47 判定器（$q{=}2$ 精确）联合 $q{=}3,\rho{=}1$ 的精确/搜索判定，扫 394 个 $L_0$ 不是解的实例：

| 项 | 数量 |
|---|---|
| $q{=}2$ 精确不可行 | 306 |
| 其中 $q{=}3,\rho{=}1$ 被搜索找到 | **0** |

精确化尝试（[`tests/exact_r1_q3.py`](tests/exact_r1_q3.py)）：只查铅笔子式是否恒零时，118 个里有 60 个"可达"；
但构造时发现

$$\boxed{\ \operatorname{rank}(L)=3\ \text{的点全部满足}\ y\parallel u\（\text{谱条件失败}）\ }$$

即**秩条件与谱条件在同一仿射族里互斥**（$\operatorname{rank}(L)$ 最大确实到 3，但那时铅笔必坏）。

$$\boxed{\ \text{所以 }r{=}1\ \text{的非紧最小层没有找到；修正公式存活}\ }$$

（教训：精确判定必须同时含 $\operatorname{rank}(L)=q$ 与 $\operatorname{rank}(U)=k$，只查铅笔子式会误报。）

---

## 2. 已证/已验证的定理

| # | 命题 | 强度 | 位置 |
|---|---|---|---|
| A | $\rho^*=0\iff L_0$ 本身是解 $\Rightarrow q_{\min}=r$ | **已证** | THE_LEMMA §3.1 |
| B | $\rho^*=\dim V\Rightarrow q(\rho^*)=\dim V+1$ | **已证**（§21 构造）| §3.2 |
| C | 引理 4.3：$K_0^\perp\not\subseteq F\Rightarrow$ 存在解超平面 | 已推导 + 正例 5/5 | §4.3 |
| D | 下降算法保持 $\rho$，给出 $q(\rho_{\rm start})$ | 已验证 | §4.5 |
| E | $\rho=1$（$q{=}2$）的**完全刻画** | **已证** | §4.7 |
| F | $\rho=1$ 判定器：多项式、sound、优于搜索 | 已验证 | §4.8 |
| G | 一般 $k$：$(5b)\iff\operatorname{rank}(\lambda U-Y)=k\ \forall\lambda$ | **已证** | §4.9 |
| H | $(5a)$ 由结构方程**自动**成立 | **已证** | §4.11 |
| I | Z-形式对应：$\dim(Z\cap K)=d-\rho$；(8c) 需核项修正 | 已验证 | §4.12 |
| J | $k{=}1$ 时 $\Sigma$ 由 $L_0$ 唯一确定（$\alpha_0\ne0\Rightarrow v\propto\alpha_0$；否则 $v\propto L_0R_0$，为零则无解）| **已证** | §4.14 |
| K | 行 1 约束：$\beta=L_0R_0+A'^{\mathsf T}\alpha_0\in\Sigma$（一般 $k$）；$k{=}2$ 且 $\beta\not\propto\alpha_0$ 时 $\Sigma$ 唯一 | **已证** | §4.15 |

### 2.1 证明复核（2026-10-24 晚）

逐条重推后：

| 命题 | 复核结果 |
|---|---|
| A（$\rho^*{=}0$）、E（$\rho{=}1$ 刻画）、G（铅笔化简）、H（$(5a)$ 自动）、I（Z-对应）| ✅ 推导无误 |
| **C（引理 4.3）** | ⚠️ **缺前提**：可容许超平面可能为空（$\mathcal W\subseteq K_0$ 时）。已加条件 $\mathcal W\not\subseteq K_0$ |

实测：`middle_layer`、`refute` 的 $\mathcal W\subseteq K_0$ 成立（它们都是紧层，不需要压缩，所以没被触发）。
下降算法在 $\mathcal W\subseteq K_0$ 时**不能压缩**，但输出仍经检查（安全、不完备）。

**已加固**：

1. 引理 4.3 的陈述加了条件 $\mathcal W\not\subseteq K_0$（THE_LEMMA §4.3）；
2. `descent_algorithm.py` 加了显式防护：压缩前先算 $\mathcal W=\mathcal V\cap\mathcal J$，
   若 $\mathcal W\subseteq K_0$ 则记录 `NO_ADMISSIBLE` 并停止（不再构造注定失败的 $H$）；
3. 5 个证书回归通过（refute 仍 $2\to1$，其余停在紧层）。

> 注：$\mathcal W\subseteq K_0$ 且 $q>\max(r,\rho+1)$ 的组合在现有数据里一次都没出现
> （所有 $\mathcal W\subseteq K_0$ 的解都是紧层）。所以这个缺口在实践中未被触发，但它是真的。

### 2.2 spec_cut 的量化尝试（2026-10-24 深夜）

"去掉谱条件后的最大 $\dim Z$"至少是 $\dim E-\dim(E\cap K)$（取 $Z\cap K=0$，此时半不变性空真）。
实测这个自由上界：

| 实例 | $\dim E$ | $\dim(E\cap K)$ | 自由上界 | 真实 $d_{\max}$ |
|---|---|---|---|---|
| `refute` | 2 | 1 | 1 | 2 |
| `middle` | 3 | 2 | 1 | 2 |
| `candidate` | 3 | 2 | 1 | 1 |
| `d4` | 4 | 3 | 1 | 2 |

$$\boxed{\ \text{自由上界只有 }1\ \text{——}Z\cap K=0\ \text{不是有意义的区域}\ }$$

所以真正的 $Z$ 必须与 $K$ 相交（与 §4.13 的"实谱强迫 $Z\cap K\ne0$"一致）。
`candidate` 的 $d_{\max}=1$ 且 $Z\subseteq K$，退化成"$A$ 在 $E\cap K$ 里的特征向量"——多项式。

---

## 3. 可判定的层

$$\begin{array}{c|c|c}
\text{层} & \text{判定方法} & \text{复杂度}\\ \hline
\rho^*=0 & L_0\ \text{是否解} & O(n^3)\\
\rho^*=1 & \text{线性方程组（D47）} & \text{多项式}\\
\rho^*=\dim V & \text{构造（\$21）} & O(n^3)\\
2\le\rho<\dim V & \text{谱条件} & \textbf{开放}
\end{array}$$

### 3.1 证书实例的**精确** $q(\rho)$ 表

（"精确"= 上界由显式解给出、下界由 $q\ge\max(r,\rho+1)$ 或专门论证给出，两边相等。）

| 实例 | $d$ | $\dim V$ | $\rho_0$ | $q(0)$ | $q(1)$ | $q(2)$ | $q_{\min}$ |
|---|---|---|---|---|---|---|---|
| A（refute）| 1 | 1 | 0 | **1** | **3** | — | **1** |
| B（middle）| 2 | 2 | 0 | $\infty$ | **2** | **3** | **2** |
| rhostar | 2 | 2 | 1 | $\infty$ | **2** | **3** | **2** |
| C（candidate）| 3 | 2 | 1 | $\infty$ | $\ge3$ | **3** | **3** |
| d4 | 4 | 2 | 1 | $\infty$ | $\ge3$ | **3** | **3** |

依据：

- $q(0)$：$\rho_0>0$ 时 $\infty$（$\operatorname{rank}(LN)\ge\rho_0$）；$\rho_0=0$ 时由 §2.2(A)，
  $L_0$ 是解 $\Rightarrow q(0)=1$，否则 $\infty$。
- $q(\dim V)$：$q\le\dim V+1$（构造），$q\ge\dim V+1$（$q\ge\rho+1$，且本列 $\rho=\dim V$）$\Rightarrow$ 相等。
- $q(1)$：$q=2$ 的情形由 D47 判定器精确判定（A 为无解，B/rhostar 有解）；
  A 的 $q(1)=3$ 由"$q=2$ 不可能"证明给出（$\nu$ 的一维论证）。
- C/d4 的 $q(1)$ 只确定了 $\ge3$（$q=2$ 无解）；$q\ge3$ 的值未定，但**不影响 $q_{\min}$**
  （因为 $q(2)=3$ 已给出 $q_{\min}\le3$，而 $q_{\min}\ge3$ 由 $q=2$ 无解 + $\rho_0=1$ 给出）。

$$\boxed{\ \text{五个证书实例的 }q_{\min}\ \text{全部是精确值，不是搜索上界}\ }$$

---

## 4. 唯一未解决的问题

$$\exists\,V\in\mathrm{Gr}(k,d):\quad \text{线性系统}\ (LN=UV^{\mathsf T},\ LR_0=-UW^{\mathsf T}+YV^{\mathsf T})\ \text{有解，}$$
$$\text{且解空间含一个使铅笔}\ \lambda U-Y\ \text{无实特征值的点}.$$

**已知的结构**（全部验证过）：

- 对固定 $V$，解空间"全好或全坏"（`candidate`：57/59 vs 0/57）；
- $k{=}2$、$d{=}3$ 时，好 $V$ **唯一**：16 个候选方向里只有 $V_{\rm cert}=\operatorname{span}\{e_1,e_2\}$ 通过；
- $k{=}2$ 时铅笔的子式 gcd 通有为 1（无特征值），所以谱条件本身不稀少，稀少的是"好 $V$"。

> ⚠️ **重要保留**：`candidate`/`d4` 的 $\rho^*=\dim V=2$，所以它们的 $k{=}2$ 解是**顶层解**，
> 由 §21 构造已保证存在、且 V 本质唯一。**真正的中间层 $k{=}2$（$2\le\rho^*<\dim V$）一个实例都还没有**
> —— 现有全部 $k\ge2$ 实验都是在顶层做的，不能当作中间层的证据。

---

## 5. 与 Q1-TRUE 的关系

两个方向在**同一个硬核**上汇合：

$$0<\dim(Z\cap K)<\dim Z\iff 2\le\rho<\dim V\iff \text{中间层}.$$

| | V-形式（本文）| Z-形式（Q1-TRUE）|
|---|---|---|
| 半不变性 | $(5a)$ **自动** | $A(Z\cap K)\subseteq Z$ 不自动 |
| 谱条件 | 铅笔 $\lambda U-Y$ | $(\lambda I-A)K$ 与 $Z$ 的交维数（需核项）|
| 目标 | 最小化 $\dim V$ | 最大化 $\dim Z$ |

---

## 6. 文件地图

| 内容 | 位置 |
|---|---|
| 紧性引理全文 | [THE_LEMMA.md](THE_LEMMA.md) |
| $\rho=1$ 判定器 | [tests/rho1_solver.py](tests/rho1_solver.py) |
| 引理 4.3 验证 | [tests/cp_check.py](tests/cp_check.py)、[tests/lemma43_positive.py](tests/lemma43_positive.py) |
| 下降算法 | [tests/descent_algorithm.py](tests/descent_algorithm.py) |
| $k$ 铅笔 / $V$ 扫描 | [tests/rho_k_structure.py](tests/rho_k_structure.py)、[tests/k2_V_scan.py](tests/k2_V_scan.py) |
| Z-形式对账 | [tests/zform_check.py](tests/zform_check.py)、[Q1_FALSE_TO_Q1_TRUE](../Q1_FALSE_TO_Q1_TRUE.md) |
| 审计数据 | `record/layer_audit_*.json`、[record/Q1FALSE_2026-10-24.md](../record/Q1FALSE_2026-10-24.md) |

---

## 7. 下一步（按优先级）

### 7.-1 专家反馈（2026-10-24 深夜）

外部反馈确认：

1. **Q3 已解决**：谱条件 $\iff$ 全部 $k\times k$ 子式的最大公因式为 $1$（即本项目的 `cond5b`）。
   并且 $q=k$ 时 $\det(\lambda U-Y)$ 必有 $k$ 个根，独立验证了 $q\ge\rho+1$。
2. **Q1′ 的陈述要改**：统一形式是 $q(\rho^*)=\max(r,\rho^*+1)$；只在 $r\le\rho^*+1$ 时才化为 $\rho^*+1$。已修正。
3. **好的 $\Sigma$ 集合是构造集**（不是必然开/闭）；实例 C 的"单点"只是有限采样，不能当定理。
4. **符号消元的正确做法**：参数化 $X=X_0(t)+T(t)s$，对 $s$ 做消元/子结式，不能随便固定 $s$。
5. **压缩引理的两个障碍**：$\mathcal W\not\subseteq K_0$ 可能失效；以及需说明压缩保持 $\rho$（后者已补：$H+\mathcal W=\mathcal V$ 给出秩不变）。
6. **Q4 的实例级做法**：参数化所有含 $K_0$ 的低维子空间，逐个精确判定。

### 7.0 实例 A 的 Q4 精确检验（本轮）

取实例 A 的 $q{=}3,\rho{=}1$ 解 $\mathcal V$（$\dim\mathcal W{=}2$，$\mathcal W\not\subseteq K_0$，所以失效原因是另一条：
$K_0^\perp\subseteq F$）。参数化 $\mathcal V$ 内所有含 $L_0$ 的 2 维子空间（$168$ 个 $(a{:}b)$ 点）：

$$\boxed{\ \text{没有任何 2 维解}\ }$$

精确原因：2 维解必须 $\subseteq\mathcal J$（$\rho{=}0$），需 $w\in\mathcal W$ 且 $wA\in\mathcal J$；
实测 $w\mapsto wA\nu$ 在 $\mathcal W$ 上的核恰为 $\operatorname{span}\{L_0\}$ —— 只有 $L_0$ 自己，故无 2 维解。

$$\Longrightarrow\quad \mathcal V\ \text{里只有}\ \dim 1\ \text{的解（即 }L_0\text{）和 }\dim 3\ \text{的解，}\textbf{跳过}\ \dim 2.$$

这印证了专家的判断："超平面压缩失效 $\ne$ 不存在其他压缩"——这里压缩是 $3\to1$ 的直接跳跃。

### 7.0b 结构性障碍：块对角造不出紧的中间层

若 $(A,C,L_0)$ 分解成两个块（$A=\operatorname{diag}$，$C=(C_1\ C_2)$，$L_0=(L_{0,1}\ L_{0,2})$），
且 $L$ 的行也按块分开，则

$$q=q_1+q_2,\qquad \rho=\rho_1+\rho_2,\qquad q_i\ge\rho_i+1\ (\rho_i>0) .$$

$$\Longrightarrow\quad q\ \ge\ \rho+\#\{\text{用到的块}\}\ >\ \rho+1\ \ \text{（两块都非退化时）}.$$

$$\boxed{\ \text{所以块对角扩展\textbf{永远}给不出 }q=\rho+1\ \text{的中间层}\ }$$

（D38 的实验——中间层被块扩展破坏——现在有了维数计数的理由。）

### 7.0c $k{=}2$ 层的**精确**判定（专家四步法的实现）

对非退化实例（$\beta\not\propto\alpha_0$），$\Sigma$ 唯一（§4.15）。于是可精确判定：
把自由参数当符号 $s$，算铅笔子式的 $\gcd_{\mathbb Q(s)[\lambda]}$。

- $\gcd=1$：一般 $s$ 无公共根 $\Rightarrow$ 层可达；
- $\gcd$ 非平凡且**系数与 $s$ 无关**：所有 $s$ 都有公共根 $\Rightarrow$ 层**不可达（证明）**。

在实例 C 上校验（[`tests/exact_sigma.py`](tests/exact_sigma.py)）：

| $\Sigma$ | $\gcd$ | 结论 |
|---|---|---|
| $t{=}0$（经验好）| $1$ | 可达 ✓ |
| $t{=}1$（经验坏）| $(\lambda-3)(\lambda-1)$ | 不可达 ✓ |

在 6 个随机非退化实例上（[`tests/exact_k2_layer.py`](tests/exact_k2_layer.py)，$\dim V{=}3,\rho_0{=}1$）：

$$\gcd=\frac{11\lambda^2+6\lambda-28}{11},\ \frac{24\lambda^2-38\lambda-53}{24},\ \lambda^2+3\lambda+5,\ \lambda^2-8\lambda-8,\ \lambda^2+2,\ \lambda^2-\lambda-4 .$$

$$\boxed{\ \text{6/6 的 }\gcd\ \text{系数与 }s\ \text{无关}\ \Longrightarrow\ \text{这 6 个实例的 }\rho{=}2\ \text{层\textbf{证明为空}}\ }$$

这把之前的"随机搜索没找到"升级成了"精确不可达"。并且 $\gcd$ 不含 $s$ 这一现象，正是
"全好/全坏"在非退化情形下的**证明**（不再只是抽样观察）。

### 7.1 定向搜索的现状
| 尝试 | 规模 | 命中 |
|---|---|---|
| 随机 $n{=}7,p{=}2,d{=}3$ | 8 实例 | 0 |
| `middle_layer` 耦合扩展（$x,y\in\{0,1\}$，$a\in\{-1,0,1\}$，$c\in\{0,1\}^2$）| 48 候选（多数 $\dim V{=}3$）| **0** |

$$\boxed{\ \text{中间层 }k{=}2\ \text{比 }k{=}1\ \text{难造得多}\ }$$

原因可以定性：$k{=}1$ 的条件是**线性**的（$y\notin\operatorname{span}u$），线性系统可解就能挑到点；
$k\ge2$ 的条件是**谱**的（铅笔无实特征值），线性系统的解空间可能整体落在坏集里 ——
`candidate` 上 $t\ne0$ 时正是 0/57。

### 7.2 修正后的路线

1. **耦合构造**（非块对角）：需要 $C$ 或 $A$ 的交叉项，使两个"半块"共享方向 —— 随机搜不到，要设计；
2. 造出来之后再做 $d$ 的符号消元；
3. 若消元爆炸 → q1 = 真的具体证据，交给 Q1-TRUE；
4. 保底：$\rho^*\in\{0,1,\dim V\}$ 的多项式算法 + 夹逼 + 证书写成部分结果论文。

### 7.3 诊断：坏铅笔继承了 $A'$ 的特征值

对 `candidate`（$A'$ 的特征值 $\{3,1,-1\}$）：

| $V$ | 铅笔 $\lambda U-Y$ 的 gcd | 根 |
|---|---|---|
| $t{=}0$（好）| $1$ | 无 |
| $t{\ne}0$（坏）| $(\lambda-3)(\lambda-1)$ | $\{1,3\}\subset\operatorname{spec}(A')$ |

$$\boxed{\ \text{坏的 }V\ \text{让铅笔"继承"了 }A'\ \text{的部分特征值}\ }$$

但不是"实特征值就坏"：`middle_layer` 的 $A'$ 也有实特征值（判别式 $7449>0$），
却存在 $\rho{=}1$ 的中间层解。所以判据不是"实/复"，而是**$V$ 是否吸收了那些模式**。

$$\text{待精确化：哪些 }V\ \text{能让铅笔不含 }A'\ \text{的特征值？}$$

### 7.4 符号消元的尝试（失败，但失败得有信息）

[`tests/symbolic_t.py`](tests/symbolic_t.py)：把 $t$ 当符号，解 $27$ 未知量、$18$ 方程的线性系统。

结果：解空间 $9$ 维；把自由参数全设 $1$ 得到的"一般点"上

$$\gcd\{\text{子式}\}=0\quad(\text{三个子式恒为零})$$

$$\Longrightarrow\quad \text{该点铅笔恒降秩（很可能 }Y\propto U\text{）—— 是\textbf{退化点}，不是一般点。}$$

所以"自由参数随便取就是一般点"是错的：**解空间里有一大片退化轨迹**。
这也解释了 D51 的 57/59（不是 100%）：少数样本落在退化轨迹上。

正确的符号消元需要：
1. 先排除退化轨迹（$\operatorname{rank}U=k$、$\operatorname{rank}Y=k$ 的确定性条件）；
2. 再在剩余部分判定 $\gcd=1$；
3. 并处理 $t$ 的专门化（$\gcd$ 在 $\mathbb Q(t)[\lambda]$ 里为 $1$ 不代表每个 $t$ 处都为 $1$）。

**第二次尝试**（三组随机专门化）：$\gcd=(\lambda-3)(\lambda-1)$，与 $t$ 无关。
但直接用同一组参数在 $t{=}0$ 处检验，却得到合法解（$\operatorname{cond5b}{=}0$）。

$$\Longrightarrow\quad \text{符号解的自由参数基与数值解的基不同，"同一个下标"对应\textbf{不同点}}$$

所以符号 $\gcd$ 反映的是**所选那个点**，不是"$t$ 处的一般点"。要点：
**必须先限制到非退化点（$\operatorname{rank}L{=}q$）再算 $\gcd$**，否则结论无意义。
这正是"选一个对所有 $t$ 都一般、且非退化的点"的困难——也是这条路的真正障碍。
