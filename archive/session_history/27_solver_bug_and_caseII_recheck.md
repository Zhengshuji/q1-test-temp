# 本轮记录：求解器缺陷修正 + 情形 II 的独立复核（2026）

> 本文是**过程记录**。结论仍以 [`FINAL.md`](../FINAL.md) 为准。
> 记号与 FINAL §1、§2 完全一致。

---

## 0. 本轮一句话

> **主结论未被推翻**（情形 II 的 (A)∧T5a ⟹ (S) 失败，经穷举 1510 + 过滤搜索 2253 个点无例外）；
> **但发现并修复了一个会污染 (A)-分解类结论的求解器缺陷**，并把"独立复核"制度化。

---

## 1. 项目现状（进场时）

| 项 | 状态 |
|---|---|
| 主线 | 证明/证伪 **q1**（最小增广行数的 NP-hardness）—— **仍未定** |
| 硬度的唯一候选 | **情形 II**（$d_{CA}\ge q_0$）与支 B（$2p+q_0<n$） |
| 情形 II | **不平行** ⟹ NO（**T12 已证**）；**平行** ⟹ 猜想 **c6′**（平行 ∧ (A) ∧ T5a ⟹ (S) 失败）|
| Lean | `~/WorkSpace/lean4/MyProof`：**35 条定理**，`lake build` **零 error / 零 warning** ✓ |
| c6′ 的在 Lean 中的形态 | **条件式**（`c6'_final`：把 (A) 的**分解**当作假设）⚠️ |

---

## 2. 🔴 发现一：库 `solve` 的**零空间基不满足残差**

### 2.1 现象（可复现）

系统：$(A)$ 分解 $\;\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA\;$ 的线性方程组（12 方程 / 15 未知量）。

```
方程数 = 12 ；未知量 = 15 ；系数矩阵秩 = 12
【库 exact_count_thm7.solve】
  特解 y 的残差是否全零：True
  零空间基 3 个；其中**残差非零**的：3 个      ← ✗✗
```

$$\boxed{\ \textbf{库 } \texttt{solve}\ \textbf{返回的零空间基不是解}\ ✗\ \Longrightarrow\ \text{凡用}\ [y]+\text{nsol}\ \text{展开解集的脚本都拿到}\textbf{非解}\ ✗}$$

**受影响的下游（用库 solve 做 (A) 分解者）**：

| 脚本 | 用法 |
|---|---|
| `batch_c6p_k.py` | `solve_Lambda`（c6′ 批量验证）|
| `batch_c6p.py` | `solve_Lambda`，且 **rhs 用了 $-LA$**（符号也会得到 $-\Lambda$）|
| `check_S.py` | 同样的 $-LA$ 符号错误 |
| `verify_mechanism.py` | 走 `batch_c6p_k.solve_Lambda` |

### 2.2 ✅ **不受影响**的核心资产

$$\textbf{项目主统计 } \texttt{reliable\_S\_test.py}\ \textbf{用的判据是 } (H,F)\ \textbf{的子式 gcd}\ \Longrightarrow\ \textbf{不受影响}\ ✓$$

（已核对：其 `S_holds(H, Fm)` 直接对铅笔 $\lambda H-F$ 的全部 $\rho$ 阶子式求多项式 gcd，不经过任何 $\Lambda$ 包装。）

### 2.3 ✅ 对策（已实施）

| 动作 | 文件 |
|---|---|
| 新增**独立精确线性代数层**（**强制残差校验**，不通过即 `raise`） | **`scripts/core/linalg_q.py`** 🆕 |
| 修 `solve_Lambda`（改用独立求解器 + **rhs 由 $-LA$ 改为 $+LA$**） | `batch_c6p_k.py` |
| 修同一符号错误 | `check_S.py` |
| **未改动** `exact_count_thm7.py`（被大量旧脚本以绝对路径 `exec`，改动风险高） | —— |

**修复后的验证**（`check_S.py` / `batch_c6p_k.py`）：

```
修复前：F = Λ·H ？False（抽出的是 -Λ）        ⟹ (S) 判据被污染
修复后：F = Λ·H ？True  ；(S) 成立？False      ⟹ 结论不变，但依据现在是**真的** ✓
```

---

## 3. 🔴 发现二：**我自己的**两次判据错误（记录以免重犯）

| # | 我写错的地方 | 真因 | 更正 |
|---|---|---|---|
| A | 把 (S) 判成「$\max_\lambda\operatorname{rk}(\lambda H-F)=\operatorname{rk}H$」（∃λ 满秩） | (S) 是「**∀λ**」 | 逐 λ 检查 ✓ |
| B | 用 $G^{\mathsf T}$ 求零空间时把转置写反（`gens[j][i]` 应为 `gens[i][j]`） | 未知量是 $G$ 的**行** | 直接对 $G$（行=生成元、列=未知量）求零空间 ✓ |

$$\textbf{教训}：\text{“(S)”与“零空间”这两处都是本项目历史上反复踩的坑（第 20、24 处同源）} \Longrightarrow \text{凡判据必写**显式反例自检**} ✓$$

---

## 4. ✅ 情形 II 的 (A)∧(S) **独立复核**：结论不变

### 4.1 完备穷举（$n=6$、$q_0=2$、参数化完备）

$T5a\iff \ell|_K=\mu\,(L_0|_K)$，故 $\ell=\mu L_0+z$，$z\in\operatorname{row}[C;CA]$ —— **这是全部候补** ✓

| 项 | 数 |
|---|---|
| 枚举到的候补 $\ell$ | **1950** |
| 其中 $(A)\wedge T5a$ 成立 | **1510** |
| 其中 **(S) 也成立** | **0** ✓ |

### 4.2 过滤搜索（$k\ge1$ 且 $H\ne0$，$n=4,5,6$）

| 项 | 数 |
|---|---|
| $(A)$-点 | 4503 |
| 且 $k\ge1$ | 4503 |
| 且 $H\ne0$ | 4503 |
| 且 $T5a$ | **2253** |
| 且 $(S)$ | **0** ✓ |

$$\Longrightarrow\ \textbf{情形 II 的 } (A)\wedge T5a\ \textbf{恒推出 } (S)\ \textbf{失败（本轮 3763 个点上无例外）}\ \Longrightarrow\ \textbf{支持 c6′}\ ✓$$

> ⚠️ **顺带澄清**：唯一出现 $(A)\wedge(S)$ 的"候选"全部是 $k=0$（**没有增广行**）的退化点 ⟹
> **c6′ 陈述中的「$H\ne0$」是必要假设**，不是装饰 ✓

### 4.3 机制（已数值确认，可作证明路线）

$$(A)\ \Longrightarrow\ \exists\Lambda:\ \mathcal LA=\Lambda\mathcal L(\bmod C,CA)\ \xrightarrow{\ \times N_{CA}\ }\ F=\Lambda H$$

（实测 910/910 个 $(A)$-点都**存在**这样的 $\Lambda$，且 $\Lambda H=F$ ✓）

**且**：$\operatorname{rk}[H;F]=\operatorname{rk}H$ 在 **1536/1536** 个 $d_{CA}\ge q_0$ 的 $(A)$-点上成立
⟹ 存在 $\Lambda$ 使 $\operatorname{im}H$ 为 $\Lambda$-不变 $\Longrightarrow$ $\Lambda|_{\operatorname{im}H}$ 有特征值 $\lambda$
⟹ $\operatorname{im}H\cap\ker(\lambda I-\Lambda)\ne0$ ⟹ **(S) 失败** ✓

$$\boxed{\ \textbf{c6′ 的最短证明路线}：\ \text{唯一缺口 = 「}(A)\Longrightarrow\ \text{分解存在}」\ \text{（纯线性代数）}\ }$$

---

## 5. ⚠️ 对 Lean 的真话：`c6'_final` 是**条件式**

`Theorems/C6.lean` 的最终定理把 $(A)$ 的**分解** $\;\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA\;$ 当作**假设**：

```lean
(hA : L ∘ A = Lam ∘ L + G0 ∘ C + G1 ∘ (C ∘ A))   -- ← 这是假设，不是从 (A) 推出的
```

**而数学上它可以从 $(A)$ 推出**（纯线性代数，且本轮已数值确认 910/910）：

$$\textbf{待证引理}\quad \operatorname{row}(LA)\subseteq\operatorname{row}[L;C;CA]\ \wedge\ \operatorname{rank}L=q_0\ \Longrightarrow\ \exists\Lambda,G_0,G_1:\ LA=\Lambda L+G_0C+G_1CA$$

**⟹ 这是把 c6′ 从"条件式"升级为"无条件"的、唯一且明确的 Lean 目标** ✓
（构造：$\Lambda$ 按 $V/\operatorname{row}(C,CA)$ 的**商空间代表元线性性**定义；$L$ 行满秩保证良定义 ✓）

---

## 6. 本轮新增脚本（`scripts/core/`）

| 脚本 | 作用 |
|---|---|
| **`linalg_q.py`** 🆕 | **独立精确线性代数层**（维数断言 + **强制残差校验**）——今后判定的标准底座 |
| **`diag_lib_solve.py`** 🆕 | 锁定库 `solve` 零空间基不满足残差（可复现）|
| **`diag_Lambda_map.py`** 🆕 | 逐解对照：库 vs 独立（暴露 $-LA$ 符号错与求解器缺陷）|
| **`certify_solveLambda_bug.py`** 🆕 | 提取缺陷证书 |
| **`probe_generalA_c6p.py`** 🆕 | 检验一般 $A$ 版 c6′ 的构造机制（6 个 $(A)$-点，$\Lambda H=F$）|
| **`probe_caseII_mechanism.py`** 🆕 | $\operatorname{rk}[H;F]=\operatorname{rk}H$ 的独立复核（18/18）|
| **`probe_caseII_broad.py`** 🆕 | 多结构大范围复核（**1536/1536**）|
| **`probe_exhaustive_q2.py`** 🆕 | $q_0=2$ **完备穷举**（**1510 个 $(A)\wedge T5a$，0 个 $(S)$**）|
| **`probe_YES_hunt2.py`** 🆕 | 带 $k\ge1,H\ne0$ 过滤的针对性搜索（**2253 点，0 例外**）|
| `probe_S_correct.py`、`probe_YES_certified.py`、`probe_YES_hunt.py`、`probe_F_rowspace.py`、`probe_A_decomp.py`、`probe_caseII_YES_q2.py`、`probe_solveLambda_bug.py`、`diag_solveLambda.py` | 排查过程中的对照脚本（保留以供复核）|

---

## 7. 下一步（按优先级）

| 序 | 动作 | 为什么 |
|---|---|---|
| **1** | **Lean：补上「$(A)\Longrightarrow$ 分解存在」引理**，把 `c6'_final` 变成**无条件定理** | c6′ 的唯一缺口；纯线性代数，可行 ✓ |
| **2** | 用 `batch_c6p_k.solve_Lambda`（已修）**重跑** §15–18 的 14/14 批量实验 | 那些脚本原先依赖有缺陷的求解器 ⟹ 结论需重新确认（预期不变）|
| **3** | 把 §4.3 的机制**写成完整证明**（$F=\Lambda H\Rightarrow \operatorname{im}H$ $\Lambda$-不变 $\Rightarrow$ (S) 失败）| 若成立，c6′ 的"平行 ⟹ (S) 失败"部分即有干净证明 ✓ |
| **4** | 攻**支 B**（$2p+q_0<n$）与 $q_0$ 下界 | q1 的另一候选硬度源 |

**禁区不变**：不用随机采样找稀有实例；不用优化器"没找到"当"不存在"；不用旧 `condS` 判据 ✓
**新增禁区**：**不要用库 `solve`（`exact_count_thm7.py`）展开解集** ✗ —— 改用 `linalg_q.solve` ✓

---

## 8. ⭐⭐ 续：**把 c6′ 升级为无条件定理**的关键引理（本轮主攻，数学已定）

### 8.1 缺口是什么

Lean 的 `c6'_final` 把 **(A) 的分解**当作**假设**：

```lean
(hA : L ∘ A = Lam ∘ L + G0 ∘ C + G1 ∘ (C ∘ A))   -- ← 假设，不是从 (A) 推出的
```

**要补的引理**：

$$\operatorname{row}(LA)\subseteq\operatorname{row}[L;C;CA]\ \Longrightarrow\ \exists\Lambda,G_0,G_1:\ LA=\Lambda L+G_0C+G_1CA$$

### 8.2 ✅ 数值判定：**(A) 确实蕴含分解**（48220/48220，零例外）

`scripts/core/probe_A_vs_decomp.py` 穷举 3 组 $A$ × 全部小整数 $(C,L)$：

| 统计 | 数 |
|---|---|
| 枚举实例 | 50700 |
| $(A)$ 成立 | **48220** |
| ① $(A)\checkmark$ 但**无分解** | **0** ✓ |
| ② $(A)\checkmark$ 有分解、$\Lambda H=F$ | **48220** ✓ |
| ③ $(A)\checkmark$ 有分解、$\Lambda H\ne F$ | **0** ✓ |

$$\Longrightarrow\ \textbf{「}(A)\Rightarrow\text{分解」成立}\ \checkmark\ \text{（且 }\Lambda H=F\ \text{自动成立）}$$

### 8.3 ⚠️⚠️ 期间**否掉的两个错误思路**（重要，以免重犯）

| # | 我一度以为 | 实测反例 | 真相 |
|---|---|---|---|
| **E1** | 分解可由 `ker L ≤ ker (L ∘ A)` 得出 | **25440** 个 $(A)$-点上 $\operatorname{row}(LA)\not\subseteq\operatorname{row}(L)$ | `ker L ⊆ ker(LA)` **不成立** ✗ |
| **E2** | 项目现有核形式（`KF∩`）足够做分解 | **46560** 个反例（`probe_kernelform_vs_A.py`）| 单项核包含关系都不成立 ✗ |

**教训**：**不要对单个 `ker` 做文章** —— 正确做法是**直接在 `M = (L,C,C\circ A)` 的像上定义 $\psi$**，
因为 `liftQ` 需要的那个核**恰好就是** `ker M` ✓

### 8.4 ✅ 正确的构造（数学已定，可照抄进 Lean）

记 $M:=(L,\ C,\ C\circ A):V\to W\times(G\times G)$，$K:=\ker M$。核形式即 $K\le\ker(L\circ A)$。

| 步 | 内容 |
|---|---|
| 1 | $v\mapsto L(Av)$ 沿 $M$ 分解（`Submodule.liftQ`）⟹ **$\psi:M.\text{range}\to W$，$\psi(Mv)=L(Av)$** ✓ |
| 2 | 对 $p\in M.\text{range}$ 写 $p=(w,g,h)$，令 $\psi_W p:=\psi(w,0,0)$，$\psi_G p:=\psi(0,g,0)$，$\psi_H p:=\psi(0,0,h)$ |
| 3 | 三者各用「子空间有补 ⟹ 映射可扩张」（**已 Lean 编译通过** ✓ `exists_extension_of_submodule`）扩张到 $W,G,G$，得 $\Lambda,G_0,G_1$ |
| 4 | 由 $Mv=(Lv,Cv,C(Av))$：$\Lambda(Lv)+G_0(Cv)+G_1(C(Av))=\psi(Mv)=L(Av)$ ⟹ 分解 ✓ |

### 8.5 Lean 进度

`scripts/lean/Decomp2.lean`（草稿在 `~/WorkSpace/lean4/MyProof/Draft/`）：

| 引理 | 状态 |
|---|---|
| **`exists_extension_of_submodule`**（子空间上的映射可扩张）| ✅ **已编译通过** ✓ |
| **`liftQ_mkQ_apply`**（`liftQ` 取值式，隐式参数写全）| ✅ **已编译通过** ✓ |
| **`range_liftQ_apply`**（沿 `M.range` 定义映射的取值式）| ✅ 已写出（同 `liftQ_mkQ_apply` 套路）|
| **`diag_sum_eq_id`**（三个对角映射之和 = 恒等）| ✅ 已写出 |
| `decomp_of_ker_form`（主引理）| ⏸ **只剩最后一步**（见下）|

### 8.6 ⏸ 精确剩余缺口（一句话）

主引理的最后一步是这条**纯 $\mathbb{Q}$-线性代数**恒等式：

$$\psi\,(Mv)\ =\ \psi_W\langle Mv,\_\rangle+\psi_G\langle Mv,\_\rangle+\psi_H\langle Mv,\_\rangle$$

其中 $\psi_W:=\psi\circ(\varphi_W\text{的下降})$ 等。**数学上显然**（因 $\varphi_W+\varphi_G+\varphi_H=M$ 且 $\psi$ 线性），
只需把它写成 `M.range` 上两个映射相等的命题。

**推荐的收尾写法**（一次到位，避免零散的 `rw`）：

```lean
-- 1) 定义 Ψ : M.range →ₗ W 如下（用 Submodule.liftQ 沿 M.ker 定义 ψ∘φᵢ 之和）：
--    Ψ := ((liftQ M.ker φW hW).comp …) + ((liftQ M.ker φG hG).comp …) + ((liftQ M.ker φH hH).comp …)
--    本质上是把 ψ∘φW + ψ∘φG + ψ∘φH 下降到 M.range。
-- 2) 证明两条：
--    (a) Ψ = ψW + ψG + ψH                （展开定义 + funext）
--    (b) Ψ = ψ                            （在 ⟨M v, _⟩ 处：Ψ(⟨Mv,_⟩)=ψ(φW v)+ψ(φG v)+ψ(φH v)
--                                          = ψ(M v)，再对 M.range 的生成元取 ext）
-- 3) 由 (a)(b) 即得 hsplit ✓
```

**⚠️ 关键提示**：**不要**试图证明 "`(L v, 0, 0) ∈ M.range`"（那需要**再解一次方程**）✗；
应当**在 $V$ 层面**用 $\varphi_W+\varphi_G+\varphi_H=M$，再把等式**下降到 $M.\text{range}$** ✓
（这也是本轮绕了不少弯路才想通的点。）

### 8.7 踩过的 Lean 坑（本轮新增，均已定位）

| # | 坑 | 解法 |
|---|---|---|
| 1 | `p.liftQ f (fun x hx => h hx)` 参数错位 ✗ | `h` 是**隐式**参数 ⟹ 写 `Submodule.liftQ p f h` ✓ |
| 2 | `Submodule.liftQ_apply p f h v` 把 `h` 当成显式 `x` ✗ | 包一层 `liftQ_mkQ_apply` ✓ |
| 3 | `set f' : V ⧸ L.ker →ₗ W := …` 后再 `set e : V ⧸ L.ker ≃ₗ …` 触发 `HasQuotient` 合成失败 ✗ | 用 `let`，避免 `set` 链 ✓ |
| 4 | `hA v hv (map_zero C) …` 位置参数推断脆 ✗ | 显式命名中间假设 `have h2 : C v = 0 := …` ✓ |
| 5 | **`W × G × G` 在 Lean 里是 `W × (G × G)`** ✗（我一度按 `(W × G) × G` 写）| 与 `L.prod (C.prod (C.comp A))` 的**右结合**保持一致 ✓ |
| 6 | `LinearMap.coprod f g` 的两个参数**必须同目标** ✗（对"取坐标"这类映射不适用）| 对角映射要用 `coprod` 作用于**各坐标的插入**、而非**投影** ✓ |
| 7 | `LinearMap.add_apply` 作用在 `↥M.range` 上时，`ψ.comp (…)` 的类型推断会卡住 ✗ | 用 `LinearMap.comp ψ (…)` 并**显式给出中间类型** ✓ |
| 8 | 对 `LinearMap` 的加法做 `ext p; obtain ⟨⟨w,g⟩,h⟩` 会报 `HAdd` 合成失败 ✗ | 先把**目标化为逐点 `map` 等式**再 `ext` ✓ |

### 8.6′ ⏸ 本轮的实际状态（诚实标注）

#### ✅ 数学事实（穷举 **48220/48220**，`scripts/core/probe_equiv_forms.py`）

$$\boxed{\ \text{(A)row}\ \Longleftrightarrow\ \text{KF}_\cap\ \Longleftrightarrow\ \text{DEC（分解存在）}\qquad\text{逐点等价，0 反例}}$$

| 形式 | 内容 |
|---|---|
| **(A)row** | `rk[LA; L; C; CA] = rk[L; C; CA]`（项目的 (A)，FINAL T1）|
| **KF∩** | `ker[L;C;C∘A] ⊆ ker(L∘A)` |
| **DEC** | `∃ Λ,G₀,G₁, L∘A = Λ∘L + G₀∘C + G₁∘(C∘A)` |

#### ⭐⭐ 正确的证明路线（本轮定稿）：**对偶 / 分裂构造**

$$\text{把"行向量"看作 }V^*\text{ 的元素，令}\quad \Omega:W^*\times G^*\times G^*\to V^*,\qquad
\Omega(y_1,y_2,y_3):=L^*y_1+C^*y_2+(C\circ A)^*y_3$$

则 **(A) 恰好是** $\operatorname{range}\big((L\circ A)^*\big)\subseteq\operatorname{range}\Omega$（数值确认 48220/48220 等价）。

**构造**（域上恒可行）：

| 步 | 内容 |
|---|---|
| 1 | $\operatorname{range}\Omega$ 是 $W^*\times G^*\times G^*$ 的子空间 ⟹ 有补 ⟹ 有投影 $\pi$ |
| 2 | $\Omega$ 限制在 $\operatorname{range}\Omega$ 上满射 ⟹ 有右逆 $\sigma$ |
| 3 | $h:=\sigma\circ\pi$ 满足 $h\circ\Omega=\mathrm{id}$ ✓ |
| 4 | 令 $\Lambda^*:=h_1,\ G_0^*:=h_2,\ G_1^*:=h_3$（$h$ 的三个分量） |
| 5 | 由 (A)：$(L\circ A)^*y=\Omega(h((L\circ A)^*y))$ ⟹ 逐分量展开 ⟹ **取转置即得 (DEC)** ✓ |

$$\boxed{\ \textbf{这条路完全不需要}\ \text{"核包含"条件}\ \Longrightarrow\ \text{避开了我前几轮撞的全部墙}\ ✓}$$

#### ❌ 排除掉的三条错误路线（记录，避免重犯）

| # | 错误路线 | 反例（`scripts/core/probe_hand_countexample.py` 可复现）|
|---|---|---|
| **E1** | 沿 `L.range` 定义 `Λ`（需 `ker L ≤ ker (L∘A)`）| `L=e₁*`、`C=e₂*`、`A e₁=e₂`：DEC 成立，但 `e₂ ∈ ker L` 且 `L(A e₂)=1≠0` ✗ |
| **E2** | 在 `M=(L,C,C∘A)` 的像上对**坐标分量**做文章 | `dW(Mv)=(Lv,0,0)` **未必** ∈ `M.range` ✗（同上例 `M.range=span{(1,0,0)}`，而 `(0,1,0)∉`）|
| **E3** | 试图证明 `pW+pG+pH=ψ`（`LinearMap` 层面加法）| 三者目标空间分别 `W,G,G`，**不能相加** ✗ |

#### ✅ `scripts/lean/Decomp2.lean` 已编译通过的砖块（零 error；`lake build` 全绿）

| 砖块 | 内容 |
|---|---|
| `dW` / `dG` / `dH` | 三个**对角映射**（显式 lambda 定义）|
| **`diag_decomp`** | `dW a + dG a + dH a = a` |
| `exists_extension_of_submodule` | 子空间上的映射可扩张到整个空间 |
| `liftQ_mkQ_apply`、`range_liftQ_apply` | `liftQ` 的取值式 |
| **`descent`** | 在 `ker M` 上为零的映射下降为 `M.range` 上的映射 |

#### ⏸ 尚未完成

`decomp_of_ker_form`：按上面的**对偶 / 分裂路线**形式化即可。所需工具已**全部确认存在于 mathlib**：

| 工具 | 用途 | 状态 |
|---|---|---|
| `Submodule.exists_isCompl` | 每个子空间有补 | ✅ |
| `Submodule.prodEquivOfIsCompl` + `_symm_apply_left/right` | 直和分解 | ✅ |
| `LinearMap.quotKerEquivRange` | `P ⧸ ker Ω ≃ range Ω` | ✅ |
| `Submodule.liftQ` / `liftQ_apply` | 过商分解 | ✅ |
| `LinearMap.dualMap`、`LinearMap.coprod`、`LinearMap.prod` | 对偶与积 | ✅ |

**下轮照做的 4 个 Lean 目标（按依赖顺序）**：

```lean
-- T1（已试写成功 ✓，见下）投影引理
theorem exists_proj_of_isCompl (p q : Submodule K P) (hq : IsCompl p q) :
    ∃ pr : P →ₗ[K] P, (∀ x : ↥q, pr x = x) ∧ (∀ x : ↥p, pr x = 0)
-- 构造：pr := coprod 0 q.subtype ∘ (prodEquivOfIsCompl p q hq).symm
-- 取值用 prodEquivOfIsCompl_symm_apply_left / _right（**已实测通过** ✓）

-- T2 投影的核
theorem ker_of_proj ... : pr.ker = p
-- 用 hq.sup_eq_top + Submodule.mem_sup 把 z 写成 a + b（a ∈ p, b ∈ q），
-- 再用 pr(a+b) = 0 + b = b 与 pr z = 0 得 b = 0 ⟹ z = a ∈ p ✓

-- T3 商截面
theorem exists_section_of_isCompl (p q : Submodule K P) (hq : IsCompl p q) :
    ∃ s : (P ⧸ p) →ₗ[K] P, ∀ y, p.mkQ (s y) = y
-- s := p.liftQ pr hker（hker : p ≤ pr.ker 来自 T1 的第二个性质）
-- 验证：对代表元 z，s (mkQ z) = pr z，需证 mkQ (pr z) = mkQ z ⟸ z - pr z ∈ ker pr = p（T2）✓

-- T4 右逆
theorem exists_rightInverse (Ω : P →ₗ[K] V) : ∃ h : V →ₗ[K] P, h ∘ Ω = id
-- 取 q 为 ker Ω 的补（exists_isCompl）；s := T3 的截面；
-- h := (s ∘ (quotKerEquivRange Ω).symm) ∘ (range Ω 上的投影)
-- 验证 h (Ω p) = p：s (mkQ p) = pr p = p（p 在 Ω.ker 的补上）✓
```

**T1 已实测编译通过** ✓（用 `Submodule.prodEquivOfIsCompl_symm_apply_left/_right` + `rw` + `rfl`）。
**T2、T3 也已实测编译通过** ✓（见 `scripts/lean/Decomp2.lean`：`proj_ker_eq`、`section_mkQ_eq_proj`）。

#### 🚨 T4（右逆）的**根本性障碍**（本轮实测 —— **这是一个数学事实，不是技术问题**）

$$\boxed{\ \Omega\ \text{有右逆}\ h\ (\text{即}\ h\circ\Omega=\mathrm{id})\ \Longleftrightarrow\ \ker\Omega=0\ }$$

**理由**：`h ∘ Ω = id` 意味着 `Ω` 左可逆 ⟹ `Ω` **单射** ⟹ `ker Ω = 0`。

**反例**（本轮实测）：
$$P=\mathbb{R}^2,\ \Omega(x_1,x_2)=x_1,\ \ker\Omega=\{0\}\times\mathbb{R}\ne 0\
\Longrightarrow\ \textbf{不存在}\ h\ \text{使}\ h(\Omega x)=x\ \forall x\ ✗$$

（因 `Ω(1,1) = Ω(1,0)`，而 `h` 只能给一个值。）

**而我们对偶路线需要的 `Ω` 恰恰有非平凡核**（`ker Ω` 对应 `L,C,CA` 的行空间关系），
故 **"右逆"这条路从根上不通** ✗。

#### ✅ 正确的替代：**只在 `range Ω` 上取逆**（恒可行 ✓）

$$\Omega\ \text{在}\ \texttt{range}\ \Omega\ \text{上满射（显然）}\ \Longrightarrow\ \exists\, h_0:\texttt{range}\ \Omega\to P,\ h_0(\Omega x)=x\ \text{（对 } x\ \text{取商类代表）}$$

具体：用 `LinearMap.quotKerEquivRange Ω` 的**逆**复合商截面，得 `h₀ : ↥Ω.range →ₗ P`；
再沿 `range Ω` 的补空间取 0 扩张到 `V`，得所需的映射。
**验证 `h₀ ∘ Ω = id` 的关键**：`h₀ ⟨Ω x, _⟩ = s (mkQ x)`，而由 `s` 的截面性质
（`mkQ (s y) = y`）取 `y = mkQ x` 即得 `mkQ (h₀ ⟨Ω x,_⟩) = mkQ x` ——
但**这不是** `h₀ ⟨Ω x,_⟩ = x`！**仍差一个 `ker Ω` 分量** ✗

$$\Longrightarrow\ \textbf{即使用"}\texttt{range}\ \Omega\ \textbf{上的逆"，也只能得到 } h_0(\Omega x)\equiv x \pmod{\ker\Omega}\ ✗$$

**⟹ 结论（本轮最重要的数学发现）**：**对偶路线的"分裂"构造需要"线性右逆"，
而右逆存在 ⟺ 核平凡；对偶路线所需的映射核不平凡 ⟹ 右逆不存在** ✗

#### ✅ 修正后的正确形式（本轮末尾想通）

$$\boxed{\ h:\texttt{range}\ \Omega\to W^*\times G^*\times G^*,\quad \text{由}\ \texttt{range}\ \Omega\ \text{的补空间得}\ \pi,\ \text{再取}\ \Omega|_{\texttt{range}}\ \text{的逆}\ }$$

（**不需要** `h ∘ Ω = id` 于整个 `W^*×G^*×G^*`；只需 `Ω (h y) = y` 于 `y ∈ range Ω`，
这**恒可构造** ✓）

**证明链**（全部是 `Ω` 的定义 + `LinearMap.coprod` 的取值式）：

| 步 | 内容 |
|---|---|
| 1 | 由 (A)：`(L∘A)^* y ∈ range Ω` ⟹ `Ω (h ((L∘A)^* y)) = (L∘A)^* y` |
| 2 | 展开 `Ω = (L^* ∘ inl₁) + (C^* ∘ inl₂) + ((C∘A)^* ∘ inl₃)`（**定义**） |
| 3 | 即 `L^* (h₁y') = (L∘A)^*(y)_{(L^*\text{-部分})}` 等 ⟹ 取三个分量 |
| 4 | 令 `Λ^* := h₁, G₀^* := h₂, G₁^* := h₃` ⟹ `Λ^*∘L^* + G₀^*∘C^* + G₁^*∘(C∘A)^* = (L∘A)^*` |
| 5 | **有限维**：双对偶 `** ≅ id` ⟹ 取转置即得 `L∘A = Λ∘L + G₀∘C + G₁∘(C∘A)` ✓ |

> ⚠️ **本轮实况**：`decomp_of_ker_form` 仍未完成 ✗ —— 但我**先排除了一个不可能的构造**
> （"在整个 `W^*×G^*×G^*` 上取右逆"，**数学上不存在**，见上面的充要条件），
> 然后**确定了正确的形式**（只在 `range Ω` 上取逆）。
> 已机器验证的砖块（`proj_exists`、`proj_ker_eq`、`section_mkQ_eq_proj` + 对角映射等）
> 全部保留在 `scripts/lean/Decomp2.lean`（**零 error** ✓）。



> ⚠️ **本轮实况**：`decomp_of_ker_form` 本轮**未完成** ✗。
> 但：**T1–T3 已机器验证** ✓；**T4 的正确形式已确定**（改"右逆"为"`range Ω` 上的逆+扩张"）；
> 数学结论（DEC 成立）有 **48220/48220** 穷举支撑 ✓。








### 8.8 下一步（照 §8.6 的写法即可）

| 序 | 动作 |
|---|---|
| **1** | 按 §8.6 补完 `decomp_of_ker_form` 的最后一步 |
| **2** | 用它把 `c6'_final` 的 `hA` 假设**替换掉** ⟹ **c6′ 无条件** ✓ |
| **3** | 结合 **T12** ⟹ 情形 II 恒 NO ⟹ 分支 A 无硬度 ⟹ **q1 的硬度不在分支 A** ✓ |


