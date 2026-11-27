# B.24 · 内蕴形式 $\Phi$

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.24` 条目（§0.1 归并表）。

## 命题

**B.24（内蕴形式：偏算子 $\Phi$ 的特征向量；专家 2026-11-05 §2.1 的改进）** 设 $\mathcal L$ 满足 $(5a)$、
$\operatorname{rank}\mathcal L=q$，$W:=\mathcal LV\subseteq\mathbb C^q$。定义**偏算子**
$$\Phi:W\longrightarrow\mathbb C^q,\qquad \Phi(\mathcal Lx):=\mathcal LAx\quad(x\in V).$$
则

1. **$\Phi$ 良定义**：若 $\mathcal Lx_1=\mathcal Lx_2$（$x_i\in V$），则 $s=x_1-x_2\in S=V\cap\ker\mathcal L$；由 $(5a)$ 的因子化
   $\mathcal LA=K_1\mathcal L+K_2B$ 得 $\mathcal LAs=K_1\mathcal Ls+K_2Bs=0$，故 $\mathcal LAx_1=\mathcal LAx_2$。
2. **$\Phi=K_1|_W$**（对任何因子化）：$K_1$ 的选取只影响它在 $W$ 外的延拓，**在 $W$ 上的限制唯一**。
3. **判据**：
$$\boxed{(5b)\ \text{失败}\iff\exists\,0\ne u\in W:\ \Phi(u)\in\operatorname{span}\{u\}}$$
4. **维数**：$\dim W=\dim V-s=(n-r_1)-(n-h)=h-r_1$；Class I（$r_1=2$）时 $\dim W=h-2$。
5. **推论（谱维数上界）**：若 $(5b)$ 成立，则 $\dim W\le q-1$。
   *证明*：$\Phi:W\to\mathbb C^q$ 有特征值 $\lambda_0$，$E_{\lambda_0}(\Phi)\ne0$；判据 3 给出 $W\cap E_{\lambda_0}=0$，故 $\dim W\le q-1$。$\square$

## 纸面证明

*证明*：1、2 见上；3 由 B.23 的秩公式（$\ker P(\lambda)=\ker(\lambda I_q-K_1)\oplus\{0\}$、$\ker B=V$）得
$\ker P\cap\operatorname{im}H_0\ne0\iff\exists x\in V:\ \mathcal Lx\ne0,\ K_1\mathcal Lx=\lambda\mathcal Lx$；4 用 B.21 的 $s=n-h$。$\square$

*为何这是最终形式*：$h<q+r_1$ 时 $H_0$ 不满行秩、$K_1$ **不唯一**，但判据只涉及 $K_1|_W$，故与选取无关 ✓。
*注（"一般位置可避开"需要修正，专家 §2.2）*：单个矩阵不一定只有有限条特征向量**直线**——特征空间维数 $\ge2$ 时含无穷多方向；
且 $k$ 维子空间与固定 $g$ 维特征空间必有正维交当 $k+g>q$。故"维数不禁止"只在特征空间都小（如单谱）时成立。

$\iff$ $(5b)$ 失败，与 B.12 判据完全一致；`tools/verification/partial_operator.py`）。
*关于"不变子空间"（专家 §4 方向 A 的诊断）*：一维不变子空间 $\langle u\rangle$（$\Phi(u)\in\langle u\rangle$）**就是**失败条件本身，
故"存在非零不变子空间"与失败**等价**（高维不变子空间也给出特征向量）。测试"整个 $W$ 不变"（$\Phi(W)\subseteq W$）：
$2187/3453$ 的样本成立（那些样本必然失败），其余 1266 个**不**成立——所以不能指望"$W$ 整体不变"这条强形式。

## Lean

**辅助内核（F1，不升级本条等级）**：`B24Phi.lean` 三条声明（`lake env lean` exit=0，已登记）：
* `b24_factor`：$\ker\pi\le\ker\sigma$ ⟹ $\sigma$ 沿 $\pi$ 在商上因子化（存在线性 $\Phi:E/\ker\pi\to F'$ 使 $\Phi([x])=\sigma x$）；
* `b24_factor_unique`：该 $\Phi$ 唯一；
* `b24_no_full_row_rank`：因子化**不要求** $\pi$ 满射（不要求 $L$ 行满秩）。

**未形式化（因此仍记 F1）**：把 $\pi=(\cdot)L$、$\sigma=(\cdot)\Lambda$ 具体化，并由 $(5a)$ 证 $\ker(\cdot L)\subseteq\ker(\cdot\Lambda)$ —— 这是本条的项目特定内容，也是"$\Phi$ 良定义"的真正难点。

## 精确验证

* 见等级行给出的精确验证数字。

## 状态与历史

*等级*：**[已证-纸面]** $+$ **[精确验证 3453/3453]**（把 $\Phi$ 具体算成矩形铅笔 $D-\lambda U$，其极大子式 gcd 有正次数
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。



## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F1 |
| 导出等级 | **L2** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— **Lean 部分**（商泛性质已 Lean 化；实例化待补） |


## 支撑目录

无（证据全部在本卷宗内）。

## 专家复核意见（成立）

$\Phi$ 的良定义只需 (5a)，**不需要** $L$ 行满秩；$\Phi(w)=K_1w$ 需要 B.23，但不需要满行秩。


## 专家第二十二轮（48 号答复，2026-11-08）：块判据被确认 + $k=\omega$ 复杂度降级 + 下一靶子

**来源**：`workspace/for_expert/archive/48_block_criterion_and_status-answer.md`（1028 行）。

### 裁决（对应答复 §13 的表）

* **定理 A**：正确；但算法后果取决于**不可约分量分解 + 分量函数域运算**的复杂度（仍不是多项式算法）。
* **块判据**：正确，且被专家称为"本轮最重要的新结果"。要求：$(A,B)$ 是 $Z$ 在 $W/W'$ 上的**坐标块**，
  不是对 $H_A$ 的任意分块；坐标无关形式为 $\text{坏}\iff\exists0\ne w\in W,\ Zw\in\mathbb Cw$；
  建议把诱导算子记作 $\Phi$（避免与 $Z_1,Z_2$ 冲突）。
* **$q=\omega$ 恒坏**：正确；**用到了 $\mathbb C$ 代数闭**（$\mathbb R$ 上不成立）。
* **$q\ge2\omega$ 且 $\ker B=0$**：正确，但只是**充分非必要**；可容许集是**局部闭**而非闭，
  真正的问题是"可达族里能否出现 $B$ 满列秩"（synthesis problem）。
* **$\omega=1$**：正确；$\operatorname{rank}[H\ H_A]=2$ 是**谱**判据（横向），与 $(5a)$ 的竖向秩**角色不同**。
* **$q=\omega+1$**：正确；专家给出更一般的形式（见下）。
* **$q_{\min}=+\infty$ 例**：正确且完整；一般障碍命题只对**可逆** $\mathcal L$ 成立，非方阵不能直接推出。
* **$k=\omega$ 的多项式算法**：**需降级**（见下）。

### $k=\omega$ 的复杂度限定（答复 §8.4）

已写的算法要枚举 $\binom{q}{\omega}$ 个极大子式并做函数域 gcd；$\binom{q}{\omega}$ 可随维数指数增长。专家的替换措辞：

> $k=\omega$ admits an exact generic-pencil reduction. For fixed $q,\omega$, the resulting test has a
> polynomial-time implementation using bounded-degree algebraic computations. A uniform polynomial-time
> bound for variable $q,\omega$ requires further analysis.

**待核的可能加强（本卷宗自己的标注，不是专家结论）**：取一个一般的有理点 $R_0$（避开有限个真闭集），
$\lambda H(R_0)-H_A(R_0)$ 的极大子式 gcd 可由 Smith 形/第 $\omega$ 个行列式因子在多项式时间内算出，
不必枚举子式；由"坏集闭 + 一般点"应能给出 **RP/ZPP** 型判定。缺的是随机特殊化的次数界与 Smith 形的位复杂度记账。
**未证，待专家确认。**

### $q=\omega+1$ 的一般特征空间定理（答复 §5.1）

$$\text{好}\iff\text{每个特征空间一维，且 }B\text{ 在每条特征线上非零}
\iff B|_{E_\mu(A)}\ \text{对每个特征值}\ \mu\ \text{单射}.$$
必要条件：**几何**重数处处为 1（Jordan 块不排除；代数重数无所谓）。$\omega=2$ 的 $\det[w,Aw]\ne0$ 是本定理的特例。

### 下一阶段的靶子（答复 §10–§12）

* 目标定理：$\text{可行}\iff\mathscr R_\omega\cap\mathcal G\ne\varnothing$，其中 $\mathscr R_\omega$ 是可达块对、$\mathcal G$ 是好块对；
* **下一交付物（专家指定）**：$q=\omega+1,\ \omega=2$ 的完全分类——把可达的 $(A,w)$ 用 Grassmann 纤维表出，
  判定 $\det[w,Aw]$ 能否非零；
* 四个实验：**A** 块判据独立核验（$\gcd\{\text{极大子式 of }\binom{A-\lambda I}{B}\}=1$，精确算术）·
  **B** **同一 $S$ 好坏并存**（专家称"最有信息量"）· **C** $q=\omega+1,\omega=2$ 的四种情形 ·
  **D** **无固定恒等式的坏分量**（$\deg\gcd>0$ 但无常数 $Z_0$ 使 $H_A\equiv-HZ_0$）；
* 五阶段：① 形式化块定理（"ready to write"）② $q=\omega+1,\omega=2$ 分类 ③ 兼容纤维 ④ 逐分量算法 ⑤ 再评估硬度。
  **暂不优先硬度。**

### 本轮的机器检查（验证 ≠ 证明）

`check_block_criterion.py`（纯 `Fraction`，seed $=20261108$，738 例全过）：
块判据 187/187、$q=\omega$ 恒坏 49/49、$q\ge2\omega$ 且 $\ker B$ 满列秩 75/75、$\omega=1$ 91/91、
$q=\omega+1$ 特征空间定理 240/240、$n=4$ 实例 $q=4$ 96/96。
复现：`python proof/B.24/check_block_criterion.py`。

## 专家第二十三轮（49 号答复，2026-11-08）：同 $S$ 例被确认；II.3 降为判定策略；RP 路线

**来源**：`workspace/for_expert/archive/49_same_S_and_q_omega_plus_1-answer.md`（489 行）。

### 裁决

* **实验 B：决定性**（"Experiment B is decisively answered"）。同 $S$、同 $H$、一好一坏已被确认；
  自由区 $\mathcal C_S=S\times S$ 是线性的，施加满秩开条件后不可约 ⟹ 本例子已经是"**同一不可约纤维内**的混合"，
  比"不同分量"版本更强；不必再花一轮找不同分量。
* **II.3 不是精确算法**：点态代数正确，但"逐 $S$ 枚举 + 每个不可约分量取一点"不成立——任意点可能落在零集里。
  应称 **结构归约 + 判定策略**；正确检验是函数域 / 坐标环 / 构造集（在 $B\ne0$ 的开集上，好条件是一个齐次行列式的非零性）。
* **$B=0$ 单列**：$B=0\Rightarrow\ker B=W\Rightarrow$ 恒坏（复 $2\times2$ 矩阵必有特征向量）；
  $\det[w,Aw]$ 只在 $B\ne0$ 时有效。
* **约束例**：200 个测试点全坏只是**猜想**；采样不能排除开稠密好集；需按分量做函数域证明
  （参数化、分量、$B\ne0$ 与 $\det=0$ 的多项式形式、恒零性、秩开条件是否移走分量）。
* **RP 路线**：原则上成立，正确目标是 **RP，不是 ZPP**。需补：
  (i) 有理输入模型；(ii) 例外集次数界——取两个常系数组合 $f,g$（在 $\mathbb Q(R)[\lambda]$ 上 gcd 为 1），
  $\operatorname{Res}_\lambda(f,g)$ 是 $R$ 的非零多项式，总次数 $\le2k^2$；
  (iii) 有限网格采样与拒绝重采；(iv) Smith 形 / 第 $k$ 个行列式因子的位复杂度。
  fixed-$(q,\omega)$ 的陈述已由有界次数消元支撑，**不必再弱化**；变量维数的 RP 是单独的更强结果。

### 优先级（专家 §7）

* **A** 完成 $k=\omega$ 的 RP 定理（最可交付的复杂度结果）；
* **B** 自由区 $q=3,\omega=2$ 的充要判据（允许依赖 $(S,U_0,V_0,m)$，不要先假定只依赖 $U_0,V_0$）；
* **C** 证明/否定约束例的"整族全坏"。

## 约定修正（列约定，2026-11-07）

原文写 $\Phi(x\mathcal L):=x\Lambda$（行约定）。这里把它改写成**列约定**下无歧义的形式，
并指出良定义性到底用哪条。

**列约定**：$A\in\mathbb C^{n\times n}$、$\mathcal L\in\mathbb C^{q\times n}$ 作用于列向量；
$V\le\mathbb C^n$（$\operatorname{row}[\mathcal L;C]$ 的转置）；$W:=\mathcal LV\le\mathbb C^q$。

**定义**：设 $\Lambda$ 满足 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$（存在 $\iff(5a)$，见 B.28(a)/B.10）。令
$$\Phi:W\longrightarrow\mathbb C^q,\qquad \Phi(w):=\Lambda w\quad(w\in W).$$

**关键恒等式**：若 $v\in V$ 且 $v\in\ker[C;CA]$（即 $Cv=CAv=0$），则
$$\Lambda\mathcal Lv=\mathcal LAv-G_0\underbrace{Cv}_{0}-G_1\underbrace{CAv}_{0}=\mathcal LAv .$$
所以在 $V_0:=V\cap\ker[C;CA]$ 上 $\Phi(\mathcal Lv)=\mathcal LAv$。

**良定义性用在哪**：若把 $\Phi$ 定义为 $\Phi(\mathcal Lv):=\mathcal LAv$（$v\in V_0$），则需
$$\mathcal Lv=0\ \Longrightarrow\ \mathcal LAv=0,$$
而这正是 $(5a)$ 的转置形式（$\ker[\mathcal L;CA;C]\subseteq\ker(\mathcal LA)$）。若按上式定义为 $\Phi(w)=\Lambda w$，
良定义性是平凡的，但"$\Phi=\mathcal LA$ 在 $V_0$ 上"这一步才用到 $(5a)$ 与 $v\in\ker[C;CA]$。
**两种写法给出同一个 $\Phi|_{\mathcal LV_0}$；差别只在良定义性归因于谁。**

**失败判据（列约定）**：
$$(5b)\ \text{失败}\iff\exists\,0\ne v\in V_0:\ \mathcal Lv\ne0\ \text{且}\ \mathcal LAv=\lambda\mathcal Lv
\iff\exists\,0\ne w\in W_0:\ \Phi(w)\in\mathbb C w,$$
其中 $W_0:=\mathcal LV_0$。

**由此产生的一个待确认问题**：B.24 的域该写 $W=\mathcal LV$ 还是 $W_0=\mathcal L(V\cap\ker[C;CA])$？
两者在 $S\ne0$ 时不同。已向专家提出（见 30 号送审件）。




## 判据的**直接证明**（专家第六轮 §6.1）：不依赖 Kronecker 记账

记 $D:=K\cap\ker\mathcal L$。由 $(5a)$，若 $v\in D$ 则 $v\in\ker[\mathcal L;CA;C]\subseteq\ker(\mathcal LA)$，故
$$\mathcal Lv=CAv=Cv=0\ \Longrightarrow\ \mathcal LAv=0,$$
即 $D\subseteq\ker Q_{\mathcal L}(\lambda)$ 对**一切** $\lambda$。

**关键维数恒等式**：对每个 $\lambda$，映射
$$\ker Q_{\mathcal L}(\lambda)\longrightarrow\ker P_K(\lambda),\qquad v\longmapsto\mathcal Lv$$
是**满射**（若 $w\in\ker P_K(\lambda)$ 且 $w=\mathcal Lv$，则 $\mathcal LAv=\Phi_K(w)=\lambda w=\lambda\mathcal Lv$，且 $Cv=CAv=0$），
核为 $D$。故
$$\boxed{\dim\ker Q_{\mathcal L}(\lambda)=\dim D+\dim\ker P_K(\lambda).}\qquad(12)$$

**$P_K$ 的满列法秩**：$\iota_K$ 单射，取左逆 $J$，则 $JP_K(\lambda)=\lambda I-J\Phi_K$ 的行列式是 $\omega$ 次首一多项式，
故 $P_K(\lambda)$ 对除有限个 $\lambda$ 外满列秩，法秩 $=\omega=\dim W_K$。

**结论**：由 (12)，
$$\operatorname{nrank}Q_{\mathcal L}=n-\dim D,$$
且 $Q_{\mathcal L}(\lambda)$ 的秩**低于法秩** $\iff\ker P_K(\lambda)\ne0$ $\iff\exists\,0\ne w\in W_K:\ \Phi_K(w)=\lambda w$。

**意义**：这条证明**不用** Kronecker 记账恒等式，也不依赖 $W_0$ 或 $V/S$ 的识别，
应作为 B.24 判据的**主证明**（原来经 $\Phi=K_1|_W$ 的路线保留为第二条路径）。



## 登记策略（文件级豁免，2026-11-07）

`tools/lean/MyProof/Theorems/`（16 文件 / 78 声明）是早期会话的辅助内核，按
`tools/lean/EXEMPT_AUXILIARY.md` 做**文件级豁免**：

* 豁免文件的声明**仍被收集**（用于"对照表条目必须真实存在"的检查），但**不要求逐条登记**；
* 豁免文件里若有**命题级**声明，必须在 `EXEMPT_AUXILIARY.md` 点名并在 `STATEMENT_MAP` 单列；
* 现有唯一命题级声明：`decomp_iff_ker`（$=$ L1）；
* `audit_lean_statements.py` 现在扫两层子目录、识别 `public` 前缀、并校验豁免清单里的文件真实存在。

**效果**：声明总数从 222 涨到 **289**（含豁免内的 67 条），条目 212，**0 问题**——
即"已证但未登记"的盲区被收口，同时不需要为 78 条工具声明写 78 行文档。

## L1 已存在（WSL 树中，未登记）—— 修正 L1–L7 的状态

查找既有代码时发现：**L1 早已形式化**，在 WSL 树的 `MyProof/Theorems/Factor.lean`（命名空间
`QProofFactor.Decomp`）。关键声明：

| 声明 | 陈述 |
|---|---|
| `decomp_iff_ker` | $\bigl(\exists\Lambda,G_0,G_1:\ L\circ A=\Lambda\circ L+G_0\circ C+G_1\circ(CA)\bigr)\iff\ker(L,C,CA)\subseteq\ker(LA)$ |
| `ker_tuple_le_of_decomp` | $(\Leftarrow)$ 方向 |
| `decomp_of_ker_tuple_le` | $(\Rightarrow)$ 方向，用 `exists_comp_eq_of_ker_le`（**正是专家建议的 factor-and-extend 引理**）|
| `tuple_eq` | $\Theta=\iota_1L+\iota_2C+\iota_3(CA)$ 的拆分 |

**所以 L1 的数学内容是 $(5a)\iff\exists(\Lambda,G_0,G_1)$ 的完整双向证明，已有机器检查。**

**但**：该文件在 `MyProof/Theorems/` 子目录，**不在** `tools/lean/MyProof/` 的登记范围内
（我们的 `audit_lean_statements.py` 只扫顶层），故 **STATEMENT_MAP 里没有它**。这是登记缺口，不是证明缺口。

**L1–L7 的最新状态**

| 里程碑 | 状态 |
|---|---|
| L1 | ✅ **已形式化**（`QProofFactor.Decomp.decomp_iff_ker`），但**未登记** |
| L2 | ✅ `B37Domain.l2_factor` |
| L3 | ✅ `B37Domain.l3_unique` |
| L4 | ⬜ 未做（核 ↔ 部分特征向量，模永久核）|
| L5 | ❌ **已否证**（$\mathcal LK\ne\mathcal L(V\cap K)$，反例 + 382/382 扫描）|
| L6 | ✅ `B37Domain.l6_finrank` |
| L7 | ⬜ 未做（修正铅笔的行列式因子判据）|

**待办**：把 `Theorems/Factor.lean`（及其子目录）纳入 `tools/lean/MyProof/` 的登记范围，
或在 `audit_lean_statements.py` 里增加子目录扫描——否则同类"已证但未登记"会继续出现。

## Lean 里程碑 L2/L3/L6 已形式化（`B37Domain.lean`，exit=0）

| 里程碑 | 陈述 | Lean 声明 |
|---|---|---|
| **L2** | $\ker(L|_K)\le\ker(T|_K)$ ⟹ $T|_K$ 沿 $L|_K$ 因子化：$\exists\Phi:K/\ker(L|_K)\to F$，$\Phi([v])=Tv$ | `l2_factor` |
| **L3** | 该 $\Phi$ **唯一** ⟹ 与 $\Lambda$ 的选法无关 | `l3_unique` |
| **L6** | $\dim(LK)=\dim K-\dim\ker(L|_K)$ | `l6_finrank` |

差异：L2 给的是**商形式**（$K/\ker(L|_K)$），与"像 $W_K=LK$"的同一化仍用纸面（商 ≅ 像，标准同构）。

L1（$(5a)\iff\exists(\Lambda,G_0,G_1)$）仍是纸面：需要"沿满射因子化 + 把映射延拓到整个乘积空间"的
线性代数引理，未形式化。L4、L7 仍未做。

## L5 已被否证：$\mathcal LK\ne\mathcal L(V\cap K)$（反例 + 统计）

专家把"证或反证 $\mathcal LK=\mathcal L(V\cap K)$"列为第一任务。结论：**等式在一般可容许实例上不成立**。

**固定反例**（满足 $(5a)$）：
$$A=\begin{pmatrix}0&-1&2&1\\0&0&-1&2\\0&-1&0&2\\2&1&2&-1\end{pmatrix},\quad
C=\begin{pmatrix}1&1&-2&2\end{pmatrix},\quad
\mathcal L=\begin{pmatrix}-1&-2&-2&0\\0&-1&-1&1\end{pmatrix},$$
实测 $\dim K=2$、$\dim(V\cap K)=1$、$\dim\mathcal LK=2$、$\dim\mathcal L(V\cap K)=1$，故两者不相等。

**随机扫描**（$n=4$、$p=1$、$q=2$、$r=1$、有理随机、仅取满足 $(5a)$ 的实例）：
可容许 **382** 组，其中 $\mathcal LK=\mathcal L(V\cap K)$ 的有 **0** 组，不相等 **382** 组。

**证书**：`tools/verification/lk_eq_vik.py`（固定实例 + 断言 + 扫描统计；`assert` 会在坏输入上打挂）。

**结论**：主域必须取
$$\boxed{W_K=\mathcal LK,\qquad \Phi_K(\mathcal Lv)=\mathcal LAv\ (v\in K),}$$
**不能**用 $W_0=\mathcal L(V\cap K)$ 替代（专家已同步撤回其 $W_0$ 建议）。



## L4 已形式化（`B24L4.lean`，exit=0）

| 声明 | 陈述 |
|---|---|
| `l4_ker_fiber` | $\ker(T-\lambda L)\cap K=K\cap L^{-1}\bigl(\ker(\Phi-\lambda\,\mathrm{id})\bigr)$，条件 $\Phi(Lv)=Tv$（$v\in K$）|
| `l4_finrank` | 两边 $\dim$ 相等（随集合层）|

**意义**：这是 (12) 的**集合层**——把"$v$ 是 $Q_{\mathcal L}$ 在 $\lambda$ 处的核向量"精确化为
"$Lv$ 是 $\Phi$ 的 $\lambda$-特征向量"。

**覆盖范围（诚实标注）**：(12) 的"$\dim\ker Q=\dim D+\dim\ker P_K$"中"$+\dim D$"这一步
由 $v\mapsto Lv$ 的秩-零化度给出，**仍在纸面**；本模块只形式化了集合层。故本条为 **F2**（非平凡核心），非 F3。

### L1–L7 终态

| 里程碑 | 状态 |
|---|---|
| L1 $(5a)\iff\exists\Lambda$ | ✅ `QProofFactor.Decomp.decomp_iff_ker`（已入册）|
| L2 $\Phi_K$ 良定义 | ✅ `B37Domain.l2_factor` |
| L3 $\Phi_K$ 与选法无关 | ✅ `B37Domain.l3_unique` |
| L4 核 ↔ 部分特征向量 | ✅ **`B24L4.l4_ker_fiber` / `l4_finrank`（集合层；维数加法在纸面）** |
| L5 $\mathcal LK=\mathcal L(V\cap K)$ | ❌ **已否证**（反例 + 382/382）|
| L6 $\dim\mathcal LK$ | ✅ `B37Domain.l6_finrank` |
| L7 $P_K$ 的行列式因子 | ✅ 纸面（含规模推论 $\binom{q}{\omega}$）|

**7/7 全部有结论：5 已证、1 已否证、1 已证（纸面）。**



## Stage 2（部分）：最小案例 $n=4,p=1,q=2,r=1$ 的精确分析

脚本：`tools/verification/stage2_minimal_case.py`、`stage2_family.py`（sympy **精确有理**符号运算）。

### 数据

$C=e_1^{\mathsf T}$、$\dim K=2$（$K=\langle e_3,e_4\rangle$）；3 个 $A$ × 4 个 $L_0=e_i^{\mathsf T}$ 共 12 组；
$R=(r_1,\dots,r_4)\in\mathbb R^{1\times4}$，$H(R)=\mathcal L(R)N_K$（$2\times2$）、$H_A(R)=\mathcal LA(R)N_K$。

### 结果（12 组）

| 组 | $\det H$ | 判定 |
|---|---|---|
| $A_1,L_0=e_3$ | $r_4$ | $\omega=2$ 不可行；$\det H=0$ 时 $(5a)\Rightarrow r_2=0$，此时非不变行列式 $\equiv0$ ⟹ **不可行** |
| $A_1,L_0=e_4$ | $-r_3$ | $\det H=0$ 上 $(5a)$ 要求常数 $1=0$ ⟹ **不可行** |
| $A_2,L_0=e_3$ | $r_4$ | 同上（常数 $1$）⟹ **不可行** |
| $A_2,L_0=e_4$ | $-r_3$ | $(5a)\Rightarrow r_2=0$，非不变行列式 $\equiv0$ ⟹ **不可行** |
| $A_3,L_0=e_3$ | $r_4$ | 非不变行列式 $\equiv0$ ⟹ **不可行** |
| $A_3,L_0=e_4$ | $-r_3$ | 同上 ⟹ **不可行** |
| $L_0=e_1,e_2$（6 组）| $\equiv0$ | **退化**（$L_0|_K=0$）：$\omega\le1$ 恒成立，需另做分析（未做） |

### 结论（限定在**这 12 组具体数据**）

1. 在 $\det H$ 非退化退化的 6 组里，$q=2$ **全部不可行**——即 $q_{\min}\ge3$；
2. 不可行的原因**只出现三种**，且都被显式算出：
   * $\omega=2=q$：方阵自同态必有特征向量（专家 §4.2）；
   * $\det H=0$ 与 $(5a)$ **不相容**（$(5a)$ 在该层退化为常数 $1=0$）；
   * $\det H=0$ 上 $\Phi_K$ **恒**有不变线（非不变行列式 $\equiv0$）。
3. 因此在这批数据里，专家 §4.6 的"情形 (a)（可行集为空或很低维）"成立——
   但**不能**推广：$L_0\in\{e_1,e_2\}$ 的退化组尚未分析，且 $A$ 的选取很小。

**未做**：退化组（$\det H\equiv0$）、更大的 $A$ 集合、$q=3$ 的验证、以及"可行集维数/次数"（需要非空样本）。
**下一步**：先找到一个 $q=2$ **可行**的实例（若存在），否则这批数据只说明 $q_{\min}\ge3$。


### Stage 2（续）：可行集在必要超平面上开稠密（找到一个 $q=2$ 可行的实例）

上一批 12 组全不可行，是**$A$ 取太小**所致，不是一般现象。按 $\Phi_K(w)\notin\mathbb Cw$ 反向设计：

$$C=e_1^{\mathsf T},\quad L_0=e_2^{\mathsf T},\quad
A=\begin{pmatrix}0&0&0&1\\0&1&0&0\\0&0&0&0\\0&1&0&0\end{pmatrix}$$
则 $CA=e_4^{\mathsf T}$、$K=\ker\{e_1,e_4\}=\langle e_2,e_3\rangle$（$k=2$），
$$H(R)=\begin{pmatrix}1&0\\ r_2&r_3\end{pmatrix},\ \det H=r_3;\qquad
H_A(R)=\begin{pmatrix}1&0\\ r_2+r_4&0\end{pmatrix}.$$
$\omega=1$ 层（$r_3=0$）：$W_K=\langle(1,r_2)\rangle$，$(5a)$ 自动满足，
$$\det\bigl[w,\Phi_K(w)\bigr]=\det\begin{pmatrix}1&1\\ r_2&r_2+r_4\end{pmatrix}=r_4
\ \Longrightarrow\ \textbf{可行}\iff r_3=0,\ r_4\ne0$$
即在 $\mathbb R^4$ 中"**必要超平面 $\{r_3=0\}$ 去掉 $\{r_4=0\}$**"——非空开稠密、维数 3。

**机器核对**（`stage2_feasible_instance.py`，走 `consistency_checks`）：$(0,1,0,1)$ 与 $(5,0,0,3)$ 可行
（$(5a)$✓$(5b)$✓）；$(0,1,1,1)$ 因 $\omega=2$ 不可行（与专家"$\omega=q$ 必失败"一致）；
$(0,1,0,0)$ 被**秩约定**排除（$\operatorname{rank}[C;\mathcal L]=2\ne p+q=3$，$R=L_0$ 为冗余行）。

**结论**：该实例的可行集**非空且开稠密于必要超平面**（专家 §4.6 的**情形 (b)**，非 (a)）。
故"$q=2$ 普遍不可行"的推测**被修正**：可行集是**余维 1 的开子集**，支持"$q_{\min}$ 为某秩条件临界值"的图景。
**未做**：一般 $A$ 的维数/次数；$\dim K\ge3$；退化组（$\det H\equiv0$）。


## 猜测（可检验）：$q_{\min}$ 由"秩条件 + 非不变（开条件）"决定

Stage 2 的实例与专家三条结论拼起来，给出一个**可检验**的图景：

$$\mathcal L=[L_0;R],\qquad \omega(R)=\operatorname{rank}(\mathcal L|_K),$$
$$(5b)\ \text{成立}\iff\Phi_K\ \text{在}\ W_K\ \text{上无不变线};\qquad
\omega=q>0\Rightarrow\text{必失败};\quad \omega=0\Rightarrow\text{必成立}.$$

又：$(5a)$ 成立时 $\operatorname{nrank}Q_{\mathcal L}=\operatorname{rank}B$，且**非不变条件对 $R$ 是开的**（是若干行列式 $\ne0$）。
于是自然的猜测是

$$\boxed{\ q_{\min}\ \overset{?}{=}\ \max\Bigl(q_0,\ \min\{q:\exists R\ \text{使}\ (5a)\ \text{且}\ \omega(R)<q\}\Bigr)\ }$$

（$q_0$ 为文献的下界；第二个量是"秩条件临界值"。）

**支持它的两个观察**
1. $\min_R\omega(R)=\operatorname{rank}(L_0|_K)$：取 $R\in K^\perp=\operatorname{row}[C;CA]$ 即可让 $R|_K=0$；
   故 $L_0|_K\ne0$ 时 $\min\omega=1$，于是**只要 $q\ge2$ 且 $(5a)$ 可满足**，秩条件就不阻碍可行性；
2. Stage 2 的实例正是这样：$q=2$ 可行，可行集 $=\{r_3=0,\ r_4\ne0\}$——秩条件给出超平面，非不变给出开条件。

**它的直接推论（强、易测）**：若 $L_0|_K\ne0$ 且存在满足 $(5a)$ 的 $R$（秩独立于 $C$ 的行），则 $q_{\min}\le2$。
对 $p=1$ 的情形这预言 $q_{\min}\le2$，可与 `tools/ledger/c189_ledger.py` 记录的实例对账。

**风险与限定**
* $\omega<q$ 只是**必要**条件；"非不变是开条件"意味着它一般可满足，但**不保证**在 $(5a)$ 的约束下可满足
  （Stage 2 上一批 12 组正是"$(5a)$ 把开条件压成空集"的例子）；
* 因此猜测的**真正内容**是："$(5a)$ 与 $\omega<q$ 的交集非空 ⟹ 存在非不变点"——这是需要证明的地方；
* 若对账出反例，猜测立即被否证，且反例本身指示 $(5a)$ 的约束有多强。


### 对账实验：$p=1$ 时 $q=2$ 可行有多常见？

脚本 `tools/verification/stage2_q2_prevalence.py`。**只给充分见证**：对小整数实例枚举
$R\in\{-1,0,1\}^3$，用 `consistency_checks.check_candidate` 精确判定 $(5a)\wedge(5b)$；
找到一个见证即**证明**该实例 $q_{\min}\le2$。找不到**不**作否定结论（候选集太小）。

**数据**：$n=3$、$p=1$、$q=2$；$C=e_1^{\mathsf T}$；$A$ 的第一行固定为 $e_2^{\mathsf T}$（故 $\operatorname{rank}[C;CA]=2$、
$\dim K=1$），其余 6 个位置枚举 $\{-1,0,1\}$；$L_0\in\{e_1,e_2,e_3\}$。共 **2187** 个实例。

**结果**：**972/2187 = 44%** 的实例存在 $q=2$ 的可行见证。

**解读**
* 全部实例都是 $\dim K=1$。此时 $\omega=\operatorname{rank}(\mathcal L|_K)\in\{0,1\}$；
  $\omega=1$ 时非不变条件只是**一个标量条件**（$\det[w,\Phi_K(w)]\ne0$，$W_K$ 一维），
  在 $(5a)$ 的解集上通常是开稠密集 ⟹ 与"$q_{\min}\le2$ 常见"一致 ✓；
* 其余 56% **未定**：可能是 $(5a)$ 不可满足、可能是秩约定排除、也可能只是我的候选集
  $\{-1,0,1\}^3$ 太小（**不能**据此说它们 $q_{\min}>2$）；
* 因此本实验**支持**猜测（"秩条件是主障碍、非不变是开条件"），但**不是**证明。

**下一步（把 56% 定性）**：对每个实例符号求解 $(5a)$ 的解集，再判定其上非不变条件是否开稠密——
这需要一个"$\exists R$ 使线性条件 + 开条件同时成立"的精确判定器（正是 Stage 1 要写的东西）。






## Stage 4（第一步）：嵌入 vs 分离——我们的族在"一般仿射铅笔问题"里的位置

### 1. 参数化是**线性**的

$$H(R)=\mathcal L(R)N_K=M(R)N_K,\qquad H_A(R)=\mathcal L(R)AN_K=M(R)AN_K,\qquad M(R)=\begin{bmatrix}L_0\\R\end{bmatrix}.$$
故 $(H,H_A)$ 完全由 $M(R)$ 决定，且**线性**（仿射）依赖 $R$；决定它的核是
$\{M:\ MN_K=0\ \text{且}\ MAN_K=0\}$。所以我们的族是"**铅笔对空间里的一个仿射线性截面**"，
而**不是**所有铅笔对。

### 2. 维数账（决定"表达力"的关键）

* 参数维数：$(q-r)n$；
* 铅笔对空间维数：$2qk$（$H,H_A$ 各 $q\times k$）；
* 若 $(q-r)n\ge 2qk$，像才**可能**填满整个对空间；否则必是真截面。

| 实例 | $(q-r)n$ | $2qk$ | 判定 |
|---|---|---|---|
| $n=4,\ p=1,\ q=2,\ r=1,\ k=2$ | 4 | 8 | **真截面**（4 < 8）|
| $n=10,\ q=5,\ r=1,\ k=5$ | 40 | 50 | 真截面 |
| $n=10,\ q=9,\ r=1,\ k=5$ | 80 | 90 | 真截面 |
| $n=10,\ q=9,\ r=1,\ k=2$ | 80 | 36 | **可能填满**（80 ≥ 36）|

**结论**：表达力由 $\dim K=k$ 相对 $n$ 的大小决定——$k$ 小（$K$ 窄）时我们几乎能实现**任意**铅笔对；
$k$ 大时只能实现一个薄截面。这给出一个**结构性二分**，对 $q1$ 有两面意义：
* $k$ **小**：我们族包含（经合适编码）大得多的铅笔对集合 ⟹ **硬度有希望继承**；
* $k$ **大**：族是薄截面 ⟹ 一般问题的硬度**不能**直接转，但算法也可能因此更容易。

### 3. 逻辑关系（必须说清，避免误推）

我们的问题 = "在**仿射线性子空间**上做 generic rank-drop 判定"。因此
* 一般问题**容易** ⟹ **不能**推出我们容易（我们的量词域更小，谓词更强）；
* 一般问题**难** ⟹ **不能**推出我们难（子问题可能容易）；
* 两个方向都**必须**单独论证：要么把某个源问题**归约到我们的截面**（硬度），
  要么证明该截面的消元理想对某类数据**永远非零**（算法）。

### 4. 因此 $q1$ 真正剩下的两条路

| 路 | 要做的事 | 障碍 |
|---|---|---|
| **硬度** | 找源问题，其实例能映射到"由 $(A,C,L_0)$ 实现的截面" | 必须同时控制**所有**层与图卡（专家 §7.2 的告诫）；$k$ 大的情形截面薄，难以承载任意实例 |
| **算法** | 证明某类数据上消元理想非零，并给出多项式实现 | 需处理函数域算术与实点稠密（Stage 3.5）|

### 5. 状态

Step 1 只给出**定位**（线性截面 + 维数二分 + 逻辑关系），**不**给出复杂度结论。
下一步（Step 2）应是：在 $k$ 小的情形尝试**具体归约**（这是表达力最强的一侧）。





## 逐层 RAZE 的复杂度初探：$\omega=0,1$ 是 P；一般层给出**单侧随机判定**

### 0. 层的显式判据（用 $(5a)\iff\ker H\subseteq\ker H_A$）

### 1. $\omega=0$：**P（常数时间检查）**

$\operatorname{rank}H=0$ ⟹ $H=0$；$\ker H=\mathbb C^k\subseteq\ker H_A$ ⟹ $H_A=0$。
故该层是**单点** $\{(0,0)\}$：可行 ⟺ 指定顶部块 $H^{(0)}=L_0N_K$ 与 $H_A^{(0)}=L_0AN_K$ **都为零**。
这是一个 $O(rk)$ 的检查 ✓（条件 3 空洞）。

### 2. $\omega=1$：**P（线性代数）**

$\operatorname{rank}H=1$，取列 $s$ 使 $H_{[:,s]}\ne0$；降阶铅笔 $P_S$ 是 $q\times1$，条目为
$p_i(R,\lambda)=\lambda H_{i,s}(R)-H_{A,i,s}(R)$（$q$ 个**一次**多项式）。
gcd 为非零常数 ⟺ **无公共根** ⟺ 不存在 $\lambda_0$ 使 $H_{i,s}\lambda_0=H_{A,i,s}\ \forall i$。

这等价于：投影点 $[H_{i,s}:H_{A,i,s}]$（对 $(H_{i,s},H_{A,i,s})\ne0$ 的 $i$）**不全相同**，且
若某个 $H_{i,s}=0$ 则须 $H_{A,i,s}=0$。即
$$\text{坏}\iff \forall i,j:\ \det\begin{pmatrix}H_{i,s}&H_{A,i,s}\\H_{j,s}&H_{A,j,s}\end{pmatrix}=0\ \text{且}\ (H_{i,s}=0\Rightarrow H_{A,i,s}=0).$$
坏条件是**二次齐次方程组**；可行 ⟺ 这些二次式在层上**不恒为零**——这是**多项式恒等测试**，
在 $\omega=1$ 时可直接由线性代数判定（只需查是否有某一对 $(i,j)$ 的行列式在层上非恒零）⟹ **P** ✓。

### 3. $\omega\ge2$：开放条件 ⟹ **单侧随机判定**（这是本轮的关键）

由闭性定理（Stage 3 定稿），坏集 $\mathcal B$ 在层上是**闭**的，故
$$\text{可行}\iff \mathcal B\subsetneq U .$$
于是：**在层上随机取一点 $R$，若该点可行，则层可行（单侧、无假阳性）**；
若层不可行（$\mathcal B=U$），随机点必不可行。若要给出概率界，需 Schwartz–Zippel 型的次数界
（$\mathcal B$ 由次数 $\le D$ 的多项式定义，随机点落入的概率 $\le D/|\mathbb F|$）。

**如何"在层上随机取点"**（专家 §5.4 的告诫：不能在环境空间乱采样）：
用秩参数化 $H=UV^{\mathsf T}$（$U\in\mathbb C^{q\times\omega}$、$V\in\mathbb C^{k\times\omega}$ 随机），
再解线性方程组 $H(R)=UV^{\mathsf T}$、$H_A(R)=$（相应目标）得 $R$；可解则得到层上的一个随机点。
**在 $K\cap AK=0$ 区域（$n-p\ge2k$），该线性系统对任意目标对都可解**（可实现性引理）✓
⟹ 采样可行。

### 4. 因此得到一个**复杂度上界**（有条件）

$$\boxed{\ \mathrm{DEC}(q)\ \in\ \mathrm{RP}\quad(\text{复版本；实版本需实点稠密})\ }$$
条件是：① 层用秩参数化可采样；② $K\cap AK=0$ 或相应区域使线性系统可解；
③ 给出 $\mathcal B$ 的显式次数界。

**推论（重要的负面结论）**：若上述成立，则
$$\boxed{q1\ \text{为 NP-hard}\ \Longrightarrow\ \mathrm{NP}\subseteq\mathrm{RP}\ }$$
即**在标准假设下 $q1$ 很可能为假**（不是 NP-hard）；$q_{\min}$ 的优化版则落在 $\mathrm{FP}^{\mathrm{RP}}$。

这与专家第九轮关于 AZE 的 RP 论证**一致**，且把该论证**推广到降秩层**（即 RAZE 全层）。





## 闭性定理：**独立陈述与完整证明**（专家第十轮优先级 2）

**定理（闭性）** 设 $U\subseteq\mathbb C^{N}$ 是一个代数集，在其上 $\operatorname{rank}H(R)=\omega\ge1$ 恒定
（$H,H_A$ 是 $R$ 的多项式矩阵，$H$ 为 $q\times k$）。令 $P(R,\lambda)=\lambda H(R)-H_A(R)$ 与
$$\mathcal B:=\{R\in U:\ \exists\lambda_0\in\mathbb C,\ \operatorname{rank}P(R,\lambda_0)<\omega\}.$$
则 $\mathcal B$ 是 $U$ 中的 **Zariski 闭集**。

*证明*（四步）

**① 齐次化**：令
$$P^{\rm h}(R;\alpha,\beta):=\alpha H(R)-\beta H_A(R)\qquad([\alpha:\beta]\in\mathbb P^1),$$
则 $P^{\rm h}(R;\lambda_0,1)=P(R,\lambda_0)$，且每个 $\omega$ 阶子式对 $(\alpha,\beta)$ **齐次**。

**② 关联簇闭**：令
$$\mathcal X:=\bigl\{(R,[\alpha:\beta])\in U\times\mathbb P^1:\ \text{全部 }\omega\text{ 阶子式 of }P^{\rm h}(R;\alpha,\beta)\ \text{为零}\bigr\}.$$
它由"$R$ 的多项式 × $(\alpha,\beta)$ 的齐次多项式"定义，故在 $U\times\mathbb P^1$ 中**闭** ✓

**③ 无穷远处为空**：在 $[\alpha:\beta]=[1:0]$ 处 $P^{\rm h}=H(R)$，而 $\operatorname{rank}H(R)=\omega$ ⟹
某个 $\omega$ 阶子式非零 ⟹ **不是全部为零** ⟹
$$\mathcal X\cap\bigl(U\times\{[1:0]\}\bigr)=\varnothing.$$
故 $\mathcal X$ 上处处 $\beta\ne0$。

**④ proper 投影**：$\mathrm{pr}_1:U\times\mathbb P^1\to U$ 是 proper（第二因子射影）⟹ **闭映射** ⟹
$\mathrm{pr}_1(\mathcal X)$ 在 $U$ 中闭 ✓

**⑤ 等同**：由 ③，$R\in\mathrm{pr}_1(\mathcal X)$ $\iff$ 存在 $\lambda_0=\alpha/\beta\in\mathbb C$ 使
$P^{\rm h}(R;\lambda_0,1)=P(R,\lambda_0)$ 的全部 $\omega$ 阶子式为零 $\iff\operatorname{rank}P(R,\lambda_0)<\omega$
$\iff R\in\mathcal B$ ✓ 故 $\mathcal B=\mathrm{pr}_1(\mathcal X)$ 闭。$\square$

### 推论 1（二分）：$U$ 不可约时
$$\mathcal B=U\quad\text{或}\quad\mathcal B\subsetneq U\ (\text{则}\ U\setminus\mathcal B\ \text{非空开稠密}).$$

### 推论 2（消元理想三情形）
设 $A$ 为 $U$ 的坐标环（整环）、$J=\langle\text{全部 }\omega\text{ 阶子式}\rangle\subseteq A[\lambda]$、$E=J\cap A$。则
$$\mathcal B=V(E),\qquad
E=(0)\iff\mathcal B=U;\quad 0\ne E\ne A\iff\mathcal B\ \text{真闭};\quad E=A\iff\mathcal B=\varnothing .$$
（**注意**：可行性判据是 $E\ne(0)$，**不是**"$E$ 是真理想"——专家第九轮 §3 的更正。）

### 三点限定
1. 结论只需"$\operatorname{rank}H=\omega$ 在 $U$ 上恒定"，**不需要**图卡（$\det H_{[:,S]}\ne0$）；
   图卡只是让计算显式化；
2. $\omega=0$ 时 $\mathcal B$ 的定义空洞（无 $\omega$ 阶子式），$(5b)$ 自动成立——单列；
3. 反例说明"首项满列秩"这一条**不可省**：一般情形 $\{R:\exists\lambda,\ Rp(\lambda)=0\}$ 可以**不闭**
   （专家给的 $\langle R\lambda-1\rangle$：坏集 $=\mathbb C\setminus\{0\}$，其消元理想为零 ⟹ 消元只给闭包）。

**Lean 状态**：暂不形式化。需要"射影空间 + proper 态射 + 闭映射"——Mathlib 有 `ProjectiveSpace` 与
`IsProper` 的部分基础设施，但把"多项式矩阵的 $\omega$ 阶子式"接到射影簇语言上工作量很大。
按专家建议（§6 优先级 2），本定理**纸面独立核验**价值最高，Lean 化列后续。




## 定理（RAZE ⟺ DEC，独立陈述；**含 $\omega=0$**）

### 定义

**观测器数据** $(A,C,L_0,q)$；$\mathcal L(R)=\begin{bmatrix}L_0\\R\end{bmatrix}$、$K=\ker[C;CA]$、$k=\dim K$、
$N_K$ 为 $K$ 的基（$n\times k$ 满列秩）、$h=\operatorname{rank}[\mathcal L;CA;C]$。
$$\mathrm{DEC}(q):\quad \exists R\in\mathbb C^{(q-r)\times n}:\ (5a)\wedge(5b).$$

**RAZE（由观测器数据诱导）**：$\exists R$ 与 $\omega\in\{0,1,\dots,k\}$ 使
1. $\operatorname{rank}H(R)=\omega$，其中 $H=\mathcal L(R)N_K$、$H_A=\mathcal LA(R)N_K$；
2. $\ker H(R)\subseteq\ker H_A(R)$；
3. 取列图卡 $S\subseteq\{1..k\}$、$|S|=\omega$、$H_{[:,S]}$ 满列秩，令 $U=H_{[:,S]}$、$G=H_{A,[:,S]}$，
   则 $\lambda U-G$ 的全部 $\omega$ 阶子式的 gcd 为**非零常数**；$\omega=0$ 时此条**空洞、自动成立**。

### 定理
$$\boxed{\ \mathrm{DEC}(q)\iff\mathrm{RAZE}(q)\ }$$

### 证明

**(⇒)** 取满足 $(5a),(5b)$ 的 $R$，令 $\omega=\operatorname{rank}H(R)$。
* 条件 1 按定义 ✓
* 条件 2：$(5a)\iff\ker H\subseteq\ker H_A$（恒等式；Lean：`B36FiveA.ker_inf_le_iff_restrict`）✓
* 条件 3：$\omega=0$ 时自动；$\omega>0$ 时由 **L7**（专家已核验）得"无有限秩降 $\iff$ gcd 常数"；
  再由第十二轮引理 $P_{[:,S]}=P_{\rm red}=\lambda U-G$ 与 $\operatorname{rank}P=\operatorname{rank}P_{\rm red}$
  （$V^{\mathsf T}$ 行满秩）把判据搬到降阶铅笔 ✓

**(⇐)** 取满足条件 1–3 的 $(R,\omega)$。
* $(5a)$：由条件 2 + 恒等式 ✓
* $(5b)$：由 **(12)**，$\dim\ker Q_{\mathcal L}(\lambda)=\dim D+\dim\ker P_K(\lambda)$（$D=K\cap\ker\mathcal L$），
  故 $(5b)\iff\ker P_K(\lambda)$ 维数恒定 $\iff\Phi_K$ 在 $W_K$ 上无不变线；
  而条件 3（L7 的降阶形式）恰好说"无有限秩降"，即 $\operatorname{rank}(\lambda U-G)=\omega$ 对一切 $\lambda$；
  由 $\operatorname{rank}P=\operatorname{rank}P_{\rm red}$ 得全铅笔无秩降，再由 L7 与 (12) 得 $(5b)$ ✓
  （$\omega=0$：$H=H_A=0$ ⟹ 条件 2 自动；由 L7 的 $\omega=0$ 分支 $(5b)$ 自动成立 ✓）

### 依赖清单（每一项的状态）

| 依赖 | 状态 |
|---|---|
| $(5a)\iff\ker H\subseteq\ker H_A$ | ✅ **Lean**（`ker_inf_le_iff_restrict`）|
| (12) 集合层 | ✅ **Lean**（`l4_ker_fiber`）；"$+\dim D$"纸面（秩-零化度）|
| L7（降阶判据，含 $\omega=0$） | ✅ **专家核验通过** |
| $P_{[:,S]}=P_{\rm red}$、$\operatorname{rank}P=\operatorname{rank}P_{\rm red}$ | ✅ **专家核验通过**（第十二轮）|

### 三点说明

1. **$\omega=0$ 必须在内**（专家强调）：否则无法排除"$H=0$ 而 $(5b)$ 自动成立"这一类可行解；
2. 本定理是**等价**而非归约：它只是把同一判定问题换成"降阶铅笔 + 秩分层"的语言，
   **不**含复杂度内容；
3. RAZE 的输入除观测器数据外还带 $(L_0N_K,L_0AN_K)$ 两个顶部块（由数据决定，不是自由参数）——
   这与可实现性引理（含固定行）的像刻画一致 ✓

































## 命题：$q=3$ 的 $\omega=2$ 层**整层全坏**（结构证明）⟹ $q_{\min}\ge4$

扫描（`q3_w2_good_point.py`）显示 496 个非奇异 $B_1$ 取法**全坏**。这不是偶然——有严格原因：

**关键恒等式**：在该层上 $Z_2=I$、$Z_1=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}$，且
$$F_0=(1,0)=-E\,Z_1\qquad(\text{直接验算：}E=(0,1),\ EZ_1=(-1,0)).$$
于是对**任意**可达对（约束 $B_1Z_1+B_2Z_2=0$、$Z_2=I$ ⟹ $B_2=-B_1Z_1$）：
$$H_A=\begin{bmatrix}F_0\\B_2\end{bmatrix}=\begin{bmatrix}-EZ_1\\-B_1Z_1\end{bmatrix}
=-H\,Z_1 .$$
故铅笔
$$P(\lambda)=\lambda H-H_A=H\bigl(\lambda I+Z_1\bigr).$$
而 $Z_1$ 的特征值是 $\pm1$，故 $\lambda=1$ 时 $I+Z_1$ **奇异** ⟹
$$\operatorname{rank}P(1)\le\operatorname{rank}H-\dim\ker(I+Z_1)<\omega=2 .$$
$$\boxed{\text{该层上每一个可容许点都是坏的}\ \Longrightarrow\ q=3\ \text{的}\ \omega=2\ \text{层不可行}}$$

**与 $q=2$ 的结论合并**（$q=2$ 三层皆不可行，前面已证）：
$$\boxed{q_{\min}\ \ge\ 4\ \ \text{（该实例，结构证明）}}$$

**注**：扫描的 $496/496$ 全坏正是这条恒等式的表现（$H_A\equiv-HZ_1$ 与 $B_1$ 无关）。
**这是本项目第一个**"整层全坏"的**证明**（此前只有单位缩放论证的射线族版本与网格证据）。

## $q=3$ 的 $\omega=2$ 层：**非空**（Grassmann 满足）且构造点**坏**

**数据**（用显式基 $N_K=[e_2,e_3]$，$K=\langle e_2,e_3\rangle$）：$L_0=e_3^{\mathsf T}$ ⟹
$$E=\operatorname{row}(0,1),\qquad F_0=\operatorname{row}(1,0),\qquad \ker T=\langle(-e_3,e_2),(-e_2,e_3)\rangle,$$
$$Z_1=\begin{pmatrix}0&-1\\-1&0\end{pmatrix},\qquad Z_2=I_2 .$$

**Grassmann 判据（$q=3$、$\omega=2=k$）**：$S\in\operatorname{Gr}(2,2)$ 只能是整个 $\mathbb F^2$ ⟹
$E+F_0\subseteq S$ ✓；$X_S=\{x:\exists y,\ xZ_1+yZ_2=0\}=\mathbb F^2$（取 $y=-xZ_1$）⟹ $E+X_S=S$ ✓；
$(N1)$ $\dim(E+F_0)=2\le2$ ✓、$(N2)$ $1\le m=2$ ✓
$$\boxed{\omega=2\ \text{层（}q=3\text{）非空}}$$

**构造并判定**（$d=\omega-\dim E=1$）：取 $x_1=(a,b)$、$a\ne0$，$y_1=-x_1Z_1=-(b,a)$；$B_1=[x_1;0]$、$B_2=[y_1;0]$。
$$H=\begin{pmatrix}0&1\\ a&b\\ 0&0\end{pmatrix},\qquad
P(\lambda)=\lambda H-H_A=\begin{pmatrix}-1&\lambda\\ \lambda a+b&\lambda b+a\\ 0&0\end{pmatrix}$$
三个 $2$ 阶子式：$\{-a\lambda^2-2b\lambda-a,\ 0,\ 0\}$ ⟹
$$\gcd\ \text{的次数}=2>0\ \Longrightarrow\ \textbf{坏}$$

**结论**：
* $\omega=2$ 层非空但**至少这一点是坏的**；
* 是否**整层都坏**（$\forall(a,b)$ 及更一般的行配置）**未证**——需按专家的函数域方法；
* 故 $q_{\min}$ 目前**只知 $\ge3$**，是否 $=3$ 待定。




### 定理的数值核对（一个 $k=\omega$ 实例）

实例：$n=4,p=1,q=3,r=1$、$C=e_1^{\mathsf T}$、$L_0=e_3^{\mathsf T}$、$A$ 使 $Ae_2=e_3,\ Ae_3=e_2$ ⟹ $K=\langle e_2,e_3\rangle$、$k=2$、$\omega=2=k$。
脚本：`tools/verification/k_equals_omega_check.py`。

**结果**：400 个随机 $R$ 中 $394$ 个满足 $\operatorname{rank}H=2$，其中**好 $0$ / 坏 $394$** ⟹ 好点比例 $0.000$。

**原因（可证）**：$RAN_K$ 是 $RN_K$ 的**列交换**（因 $Ae_2=e_3$、$Ae_3=e_2$），且 $F_0=E\,P$（$P$ 为交换矩阵），故
$$H_A=H\,P\qquad\Longrightarrow\qquad P(\lambda)=H\bigl(\lambda I-P\bigr),$$
$P$ 的特征值为 $\pm1$ ⟹ $\lambda=1$ 时 $I-P$ 奇异 ⟹ $\operatorname{rank}P(1)<2$ ⟹ **处处坏** ✓

**与定理一致**：定理预言"好集要么空、要么开稠密"；这里**空**（样本 $0/394$ 正是空的数值表现），
且 generic gcd 因 $H_A\equiv HP$ 而**非常数** ⟹ $\mathcal B=V$ ⟹ 该层不可行 ✓

**与专家第二十轮的机制完全同源**：第五轮专家早先给过的一般事实是"$Z$ 在 $\operatorname{im}H$ 上有不变线"即障碍；
这里 $Z=P$ 的特征向量 $v_+=(1,1)$ 给出不变线 ⟹ 障碍成立。




### 更正（第 10 次自我更正）：**不要**把 "$Z$ 在 $\operatorname{im}H$ 上无不变线" 误读成"$Z|_{\operatorname{im}H}$ 无特征值"

我在本轮口头推理中写过"$\omega=1$ 时 $\operatorname{im}H$ 是 1 维 ⟹ $Z$ 必有特征向量 ⟹ 必坏"——**错**。

原因：$Z$ 把 $\operatorname{im}H$ **映入 $\mathbb C^q$**（$q>\omega$ 时不是自映射），
故"$Zy=\lambda y$"**不是**自动的：它要求 $Zy$ 与 $y$ **共线**。

$\omega=1$ 时的正确判据：$H=uv^{\mathsf T}$、$H_A=gv^{\mathsf T}$，$P(\lambda)=(\lambda u-g)v^{\mathsf T}$，故
$$\text{坏}\iff\exists\lambda:\ \lambda u=g\iff g\in\operatorname{span}\{u\}\iff\operatorname{rank}[H\ H_A]=1,$$
即**专家定理** $(5b)\iff\operatorname{rank}[H\ H_A]=2$ ✓ **自洽**。

**由此得到一条正确的推论**（而不是我先前那条错的）：
$$\omega=1\ \text{时}\quad\text{坏}\iff g\parallel u;\qquad\text{可行}\iff\exists R\ \text{使}\ g\not\parallel u .$$
实验 1 的 12 组"全坏"正是"可容许性**迫使** $g\parallel u$"的情形（Stage 2 已用 $(5a)\Rightarrow r_2=0$ 独立验证）。

**教训**：这类"$\dim=1$ ⟹ 必有特征值"的直觉只在**自映射**上成立；本例中 $Z$ 是**跨空间**的。
已并入 §10.1 的禁区清单（"跨空间用自映射的谱直觉"）。




### 探针（$q=\omega+1$ 判据的数值检验）：**不可结论**——采样又落在余维 1 层上

脚本 `tools/verification/q_omega_plus_1_det.py`：随机取 $b_1\in\{-2..2\}^{2\times3}$、$b_2$ 按可达性（第 1 列 $=-b_1Z_1$，第 2、3 列自由），
用"基无关"形式检验 $\det[w,Aw]\ne0$ 是否可达（判据：对每个 $x$ 满足 $H_Ax\in\operatorname{im}H$、$Hx\ne0$，测 $\operatorname{rank}[H_Ax,\ Hx]=2$）。

**结果**：300 次抽样的 71 次满足 $\operatorname{rank}H=2$，其中好 $0$ / 坏 $71$。

**但这不能作结论**：$H$ 是 $3\times3$，$\operatorname{rank}H=2$ 是**余维 1** 条件（$\det H=0$）；
随机整数抽样命中的那 71 个是**算术巧合**（$\det=0$ 的稀疏子集），代表性可疑。
⟹ 与 §10.1 的"薄集不许采样"同一陷阱（本会话第 4 次踩）。

**正确做法（下次）**：**按构造**把秩压到 2，例如取 $b_1$ 使 $H$ 的第 3 行是前两行的组合，或直接在
$\{H:\operatorname{rank}H=2\}$ 的图卡上参数化（$H=UV$，$U\in\mathbb C^{3\times2}$ 满列秩、$V\in\mathbb C^{2\times3}$ 满行秩），
再把 $(H,H_A)$ 与可达性约束联立。

**状态**：本探针**未得出结论**，不计入证据。判据本身（$q=\omega+1$ 的 $\det[w,Aw]$ 形式）已在上一节**证明**，
本探针只是想做数值印证，失败原因已定位。

## 命题（$q=\omega+1$ 的显式判据）：坏 $\iff$ 存在特征线落在超平面 $\ker B$ 内

由块判据，$q=\omega+1$ 时 $B$ 是**行向量**，$\ker B$ 是 $W$ 中的**超平面**（$\dim\omega-1$）。于是

$$\text{坏}\iff\exists\ 0\ne y\in\ker B,\ Ay\parallel y\iff \exists\ \text{1 维特征空间}\ \subseteq\ker B .$$

* 若某特征空间 $\dim\ge2$：$\dim(E_\lambda\cap\ker B)\ge2+(\omega-1)-\omega=1$ ⟹ 含特征线 ⟹ **坏** ✓
* 反之若每条特征线都**不**含于 $\ker B$ ⟹ 无 $y$ 满足 ⟹ **好** ✓

**$\omega=2$、$q=3$ 的完全显式形式**：$\ker B$ 是一条线 $\operatorname{span}\{w\}$（$w\ne0$），
$$\boxed{\text{好}\iff \det\bigl[w\ \ Aw\bigr]\ne0\quad(\text{即 }w\ \text{与}\ Aw\ \text{线性无关})}$$
等价说法：$w$ 不是 $A$ 的特征向量（注意 $A=\mu I$ 时 $Aw=\mu w$ 与 $w$ 相关 ⟹ 判为坏 ✓ 与该情形一致）。

**与 $k=\omega$ 的对照**：$k=\omega$ 时 $d=0$、$W=K$ 固定、$Z$ 自由度大；$q=\omega+1$ 时
判据化归为**一个行列式** $\det[w,Aw]$，其中 $(A,B)$ 是 $Z$ 的块、$Z$ 由 $(H,H_A)$ 决定。
于是 $q=\omega+1$ 的可行性问题变成：
$$\boxed{\exists\ \text{可达对使 }\det\bigl[w,\ Aw\bigr]\ne0\ \ (w\in\ker B,\ w\ne0)}$$
——一个**关于 $(A,B)$ 的开条件**（与可容许性的闭条件相交处正是难点）。

**状态**：本命题**已证**（由块判据一行推出）。"可达对能否满足该行列式条件"未解决。
专家 48 号答复 §5.1 把它推广为**一般特征空间定理**：好 $\iff$ 每个特征空间一维且 $B$ 在每条特征线上非零
（等价于 $B|_{E_\mu(A)}$ 对每个特征值单射）；$\omega=2$ 的 $\det[w,Aw]\ne0$ 是该定理的特例。

## 命题（块判据）：坏 $\iff$ $\exists y\in\ker B$ 使 $Ay\parallel y$ —— 并由此重得 $q=\omega$ 的不可行性

**设定**：在秩 $\omega$ 层上 $(5a)$ 成立，故 $\exists Z$（定义在 $W:=\operatorname{im}H$ 上，$\dim W=\omega$）使 $H_A=ZH$（L7）。
取补空间 $W'$（$\dim q-\omega$），把 $Z$ 写成块形式
$$Z=\binom{A}{B},\qquad A\in\mathbb C^{\omega\times\omega},\quad B\in\mathbb C^{(q-\omega)\times\omega},$$
即 $Z|_W$ 的 $W$-分量是 $A$、$W'$-分量是 $B$。

**命题**：$P(\lambda)=(\lambda I-Z)H$ 在某个有限 $\lambda$ 处秩降 $\iff$
$$\exists\,0\ne y\in\ker B\ \text{使}\ Ay\in\operatorname{span}\{y\}.$$

**证明**：秩降 $\iff\exists 0\ne y\in W$，$\lambda$：$Zy=\lambda y$。按块分解，$Zy=\lambda y$ 等价于
$Ay=\lambda y$（$W$-分量）与 $By=0$（$W'$-分量）同时成立。而 $Ay=\lambda y$ 即 $Ay\in\operatorname{span}\{y\}$ ✓ $\square$

**推论 1（$q=\omega$ 的不可行性——专家定理的新证明）**：$q=\omega$ ⟹ $W'=0$ ⟹ $B=0$ ⟹ $\ker B=W$，
故坏 $\iff$ $A$ 有特征向量。$A$ 是 $\omega\times\omega$ 复矩阵且 $\omega\ge1$ ⟹ 有特征值 ⟹ 坏 ✓
$$\boxed{q=\omega\ \Longrightarrow\ \text{处处坏}\ \Longrightarrow\ \text{不可行}}$$

**推论 2（充分条件：$q\ge2\omega$ 时可"逃出"谱条件）**：
$$\ker B=0\ \Longrightarrow\ \text{坏不可能}\ \Longrightarrow\ \text{好}$$
而 $\ker B=0$ 要求 $q-\omega\ge\omega$，即 $q\ge2\omega$。故
$$\boxed{q\ge2\omega\ \text{且存在可达对使}\ \ker B=0\ \Longrightarrow\ \text{该层可行}}$$
**这不是自动的**：$\ker B=0$ 是 $R$ 的一个**开条件**，需与可容许性兼容（正是 $k>\omega$ 的困难所在）。

**推论 3（$\omega=1$ 的一致性）**：$\omega=1$ 时 $A=(a)$ 标量、$B\in\mathbb C^{q-1}$；坏 $\iff$ $\exists y\ne0$，
$By=0$ 且 $Ay\in\mathrm{span}\{y\}$ ⟺ $B=0$ 且（$a$ 任意）⟺ $g\parallel u$ ✓ 与专家的
$(5b)\iff\operatorname{rank}[H\ H_A]=2$ 完全一致 ✓
（专家 48 号答复 §4.3：这里用的是**横向**秩 $\operatorname{rank}[H\ H_A]=2$，它是**谱**判据；
$(5a)$ 用的是**竖向** $\operatorname{rank}\binom{H}{H_A}=\operatorname{rank}H$。两者角色不同，不可混用。）

**状态**：本命题**已证**（一行块分解）；推论 1、3 已证；推论 2 的条件化形式已证，
"何时可同时满足 $\ker B=0$ 与 $(5a)$" 未解决——这就是 $k>\omega$ 的剩余困难。

专家 48 号答复 §3 确认本判据，并强调：$(A,B)$ 是 $Z$ 在 $W$ 与补空间 $W'$ 上的**坐标块**
（不是对 $H_A$ 的任意分块）；坏条件本身**坐标无关**：$\exists0\ne w\in W$ 使 $Zw\in\mathbb Cw$；
建议把诱导算子记作 $\Phi$（避免与 $Z_1,Z_2$ 冲突）——本卷宗正文保留 $Z$，读时注意区分。

## 定理 A（逐分量二分，专家 Workstream A）：由闭性 + 不可约性直接得到

**陈述**：设 $X\subseteq\mathbb C^{(q-r)\times n}$ 是**不可约**的局部闭子集，且 $X$ 含于秩 $\omega$ 的 $(5a)$-可容许轨迹
（即每点满足 $\operatorname{rank}H=\omega$ 与 $\ker H\subseteq\ker H_A$）。则
$$\text{要么 } X\subseteq\mathcal B\ (\text{全坏}),\qquad\text{要么 } X\setminus\mathcal B\ \text{在 } X\ \text{中非空 Zariski 开稠密}.$$
且两案由 $\mathbb C(X)$ 上 $\gcd_\lambda\{\omega\text{-子式}\}$ 是否为常数判定。

**证明**（三步）

1. $\mathcal B$ 在 $X$ 中 Zariski 闭——直接引用**闭性定理**（专家第五轮核验：齐次化到 $\mathbb P^1$、$[1:0]$ 处由
   $\operatorname{rank}H=\omega$ 排除、$X\times\mathbb P^1$ 上投影真 ⟹ 投影像闭）。
2. 若 $\mathcal B\ne X$：$X\setminus\mathcal B$ 非空开；$X$ 不可约 ⟹ 非空开集在 $X$ 中**稠密** ✓
3. 若 $\mathcal B=X$：全坏 ✓。两案的判定：$\mathcal B=X\iff X$ 的一般点在 $\mathcal B$
   $\iff$ 在 $\mathbb C(X)$ 上存在 $\lambda$ 使全部 $\omega$-子式为零 $\iff$ 该 gcd 非常数（代数闭域上公共根判据）✓

**推论（$k=\omega$ 定理是它的特例）**：$k=\omega$ 时 $(5a)$ 自动成立，可取 $X=\{\operatorname{rank}H=k\}$（非空开、$V$ 不可约 ⟹ 不可约）⟹
即得上节的定理 ✓

**这说明剩下的困难在哪**：谱判定（第 3 步）与闭性（第 1 步）都已具备；
真正的未知是**可容许轨迹的不可约分量如何描述**——分量描述不出，就不能把"逐分量二分"落实为算法。
这正是专家 §8 Workstream C 指出的 $k>\omega$ 困难所在。

---

## 命题（$k-\omega=1$ 的结构）：该层上 $d=1$，且 $(5b)$ 化为固定矩阵的谱条件

设 $k=\omega+1$。在秩 $\omega$ 层上：

1. $\dim\ker H=k-\omega=1$，记 $\ell=\ker H$（$K$ 中一条线）；
2. 由 $D=K\cap\ker\mathcal L=\ker(\mathcal L|_K)=\ker H$ 得 $d=\dim D=1$——**$d$ 被完全钉住**（与 $\omega=k$ 时 $d=0$ 相对）；
3. $(5a)\iff H_A=ZH$ 对某个 $Z$（在 $\operatorname{im}H$ 上定义、任意延拓到 $\mathbb C^q$）✓（L7，专家核验）
4. $(5b)\iff$ 对一切有限 $\lambda$：$\operatorname{rank}\bigl((\lambda I-Z)H\bigr)=\omega$
   $\iff\exists 0\ne y\in\operatorname{im}H$ 使 $Zy=\lambda y$ **不**发生
   $\iff$ **$Z$ 在 $\operatorname{im}H$ 中没有不变线** ✓

于是 $k-\omega=1$ 的可行性问题是：
$$\boxed{\exists\ \text{可达对 } (H,H_A)\ \text{使 } Z\ \text{在 } \operatorname{im}H=\operatorname{im}H\ (\dim\omega)\ \text{上无特征向量}}$$
而 $\operatorname{im}H\cong K/\ell$（$\ell=\ker H$），故等价地：**$Z$ 诱导的映射在 $K/\ell$ 上无特征值**。

**与 $k=\omega$ 的对比**：$k=\omega$ 时 $\operatorname{im}H=K$ 固定、$Z$ 可取遍一个大族 ⟹ 谱条件"易满足"；
$k-\omega=1$ 时 $\operatorname{im}H\cong K/\ell$ **随 $R$ 变**，且 $Z$ 与 $\ell$ 耦合 ⟹ 这是真正的新困难。

**状态**：定理 A **已证**（三步，依赖专家核验过的闭性定理）；$k-\omega=1$ 的结构命题**已证**（四条，依赖 L7 与 $D=\ker H$）。
$k-\omega=1$ 的**判定结论未得到**。

## 专家优先级 3 的试探：$k>\omega$ 的"同一 $S$ 上好坏并存"——**本轮未找到**（附结构性原因）

### 尝试

实例：$n=5$、$p=1$、$q=3$、$r=1$ ⟹ $k=3$、$\omega=2$、$m=2$；取 $\dim\ker T=d=1$（最简）：
$C=e_1^{\mathsf T}$、$A$ 第一行 $e_5^{\mathsf T}$、列 $2,3,4=e_3,e_5,e_1$ ⟹ $K=\langle e_2,e_3,e_4\rangle$、$\ker T=\{(-e_3,e_2)\}$，
$Z_1=(0,-1,0)$、$Z_2=(1,0,0)$（K-坐标）；$L_0=e_4^{\mathsf T}$ ⟹ $E=(0,0,1)$、$F_0=0$。

* 搜索脚本 `tools/verification/same_S_good_and_bad.py` 的 $S$ 参数化写错（候选 0 个）——**未修**；
* 手算两条路径（$S=\mathrm{span}\{e_1,e_3\}$，$x_1=e_1$，$y_1=t\,e_3$，第二行取 $0$ 或 $e_3$）**均为坏**。

### 结构性原因（可写下来）

当 $E\subseteq S$ 且取 $x_1$ 与 $E$ 在列指标上"错开"时（$E=e_3$ 而 $x_1=e_1$），$\{E,x_1\}$ 这两行给出的子式是
$$\lambda\cdot\text{(线性)}|_{\text{列 }(1,3)}=-\lambda^2 ,$$
它**恒含根 $\lambda=0$** ⟹ 该 $S$ 上的**每个**兼容对都是坏的，与 $y$ 的选取无关。这与 $d=1$ 的刚性一致：
$\mathcal C_S$ 中 $y$ 的自由度只有 $\ker(y\mapsto yZ_2)\cap S$ 的 1 维，不足以改变 gcd 的根。

### 结论（诚实）

* **本轮没有找到**专家 §9 优先级 3 要求的"同一 $S$ 上好坏并存"的例子；
* 已定位两个待修点：① $S$ 的参数化（用图卡 $\begin{bmatrix}I_2&T\end{bmatrix}$ 或余向量统一处理）；
  ② 需要 $d\ge2$ 或更大的 $m$ 才有足够自由度；
* 这**不**否定专家的判断（$\mathcal C_S$ 确实可含多解），只是本轮未能展示；
  故本项标为**未完成**，不算证据。

## 定理（$k=\omega$ 的仿射族）：可行性 $\iff$ 非空 + generic gcd 为常数 —— 并给出算法

**设定**：$k=\omega$（即 $\ker H=0$、$H$ 满列秩）。此时 $R$ 跑遍仿射空间 $V=\mathbb C^{m\times n}$，
$H:V\to\mathbb C^{q\times k}$、$H_A:V\to\mathbb C^{q\times k}$ **仿射线性**。
记 $m_I(R,\lambda)$（$|I|=k$）为 $P(R,\lambda)=\lambda H(R)-H_A(R)$ 的极大子式，$\mathcal U=\{R:\operatorname{rank}H(R)=k\}$，
$\mathcal B=\{R\in V:\exists\lambda,\ \text{全部 }m_I(R,\lambda)=0\}$（**坏集**）。

**定理**：设 $\mathcal U\ne\varnothing$。则
$$\exists R\in\mathcal U\ \text{好}\quad\Longleftrightarrow\quad
\deg_\lambda\ \gcd_{\mathbb C(V)[\lambda]}\{m_I\}=0 .$$
且若成立，好集在 $\mathcal U$ 中**非空 Zariski 开稠密**；若不成立，则 $\mathcal B=V$（处处坏）。

**证明**（四步）

1. **$(5a)$ 自动成立**：$\operatorname{rank}H=k$ ⟹ $\ker H=0$ ⟹ $\ker H\subseteq\ker H_A$ ✓；故 $\mathcal U$ 就是秩 $k$ 可容许集。

2. **坏集 $\mathcal B$ 是 Zariski 闭**：$\mathcal B$ 是关联集
   $\mathcal I=\{(R,\lambda):\ \text{全部 }m_I(R,\lambda)=0\}\subseteq V\times\mathbb A^1$
   的投影；用齐次化到 $V\times\mathbb P^1$（$[1:0]$ 处由 $\operatorname{rank}H=k$ 排除：$\lambda\to\infty$ 时
   $P\sim\lambda H$ 的极大子式有非零首项），投影从 $V\times\mathbb P^1$ 出发是**真映射** ⟹ 投影像闭 ✓
   （与专家核验的闭性定理同型，这里 $k=\omega$ 使"无穷远处"处理更简单）。

3. **generic 判据**：$F:=\mathbb C(V)$。因 $\mathcal B$ 闭，$\mathcal B=V\iff$ 一般点 $R_{\rm gen}$ 落在 $\mathcal B$
   $\iff$ 在 $\overline F$ 上存在 $\lambda$ 使全部 $m_I(R_{\rm gen},\lambda)=0$ $\iff$
   $\gcd_{F[\lambda]}\{m_I\}\notin F^\times$ ✓。（代数闭域上"有公共根 $\iff$ gcd 非常数"。）

4. **两端结论**：
   * 若 $\deg_\lambda\gcd=0$：$\mathcal B\ne V$，故 $V\setminus\mathcal B$ 非空开；又 $\mathcal U$ 非空开（秩 $k$ 是开条件），
     $V$ 不可约 ⟹ $\mathcal U\cap(V\setminus\mathcal B)\ne\varnothing$ ✓ 且开稠密 ✓
   * 若 $\deg_\lambda\gcd>0$：$\mathcal B=V$ ⟹ 每个 $R$ 都坏 ⟹ 不可行 ✓

**算法**（**固定 $(q,\omega)$** 有界次数实现；"变动 $(q,\omega)$ 仍 $\mathrm{DEC}\in\mathbf P$"**未证**——专家 48 号答复 §8.4 要求降级，见下方"专家第二十二轮"）：
1. 算 $\operatorname{rank}_{\mathbb C(V)}H$（一般秩；$<k$ ⟹ 不可行）；
2. 在 $F=\mathbb C(V)$ 上算 $\gcd_\lambda\{m_I\}$（一元 Euclid，系数为有理函数）；
3. 判 $\deg_\lambda\gcd=0$。
两步都是有理函数域上的精确线性代数，规模 $O(\binom{q}{k}^2)$ 次一元 Euclid，次数与 $R$-次数 $O(k)$。

**边界情形都吻合**：
* $q=k$（方阵）：只有一个子式 $=\det(\lambda H-H_A)$，$H$ 可逆 ⟹ 次数 $k>0$ ⟹ $\mathcal B=V$ ⟹ 不可行 ✓（专家定理）；
* $\omega=0$：单列，条件退化为 $\mathcal B$ 是否满，与既有结论一致。

**与专家的判断一致**：这正是他 §8 Workstream B 与 §10 Theorem C 所要求的"$k=\omega$ 仿射族可解性定理"。

## 专家第二十一轮（47 号答复）：**撤回 $q_{\min}=2$**、$n=4$ 例强化为**全阶不可行**、策略调整

### 1. **撤回**（我的第 8 次自我更正，且是最严重的一类）

上一段我写"该实例 $\omega=1$ 可行 ⟹ $q_{\min}=2$"——**错**，专家否决，两条错误：

* **错误 A（用错了秩条件）**：我把 $\operatorname{rank}[H\ H_A]$（**横向拼接**，$\omega=1$ 的谱判据）与
  $\operatorname{rank}\binom{H}{H_A}$（**纵向堆叠**，$(5a)$ 的可容许条件）混为一谈。这正是 §7.2 记了四次的同一类错。
* **错误 B（构造违反 $(5a)$）**：我取的 $B_1$ 行在 $\mathrm{span}\{(0,0,1)\}$ 内，
  于是 $\operatorname{row}H=\mathrm{span}\{(0,1,0),(0,0,1)\}$，而其顶部固定行 $F_0=(1,0,0)\notin\operatorname{row}H$ ⟹ $(5a)$ 失败。
* **独立的否证**：$(N1)$ 直接给出 $\dim(E+F_0)=2>1=\omega$ ⟹ **$\omega=1$ 层是空的**（Grassmann 判据的推论）。

**正确结论**：该 $n=5$ 实例在 $q=2$ 与 $q=3$ 都不可行（$\omega=0,1$ 空、$\omega=2=q$ 方阵、$\omega=2$ 于 $q=3$ 整层全坏）
⟹ $q_{\min}\ge4$；"坏层 ⟹ 实例不可行"这条**降级本身被撤销**（该实例确实不可行）。

### 2. $n=4$ 例强化：**全阶不可行**（专家给完整证明）

$A$ 作用：$Ae_1=0$、$Ae_2=e_3$、$Ae_3=e_2$、$Ae_4=e_1$。故 $v_\pm=e_2\pm e_3$ 是特征向量（特征值 $\pm1$），且
$$Cv_\pm=0,\qquad CA\,v_\pm=0\quad(\text{因 }CA=e_4^{\mathsf T}).$$
**一般障碍**：若 $Av=\lambda v$ 且 $Cv=CAv=0$，则对**任何** $\mathcal L$：
$$\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\CA\\C\end{bmatrix}v=0 .$$
$q=4=n$ 时 $\mathcal L$ 可逆，故 $\operatorname{rank}\begin{bmatrix}\mathcal L\\CA\\C\end{bmatrix}=4$，而左边 $\le3$ ⟹ **$(5b)$ 在 $\lambda=\pm1$ 失败**。
加上已证的 $q\le3$ ⟹
$$\boxed{q_{\min}=+\infty\quad(\text{该实例无任何可行阶})}$$

**推广（专家给的障碍）**：$A$ 有特征向量 $v$ 使 $Cv=CAv=0$ ⟹ 在 $\mathcal L$ **可逆**时 $(5b)$ 必失败。
（$\mathcal L$ 非方阵时结论更微妙：$(5b)$ 右侧秩也会亏。）

### 3. 关键否证：我提的"空或刚性全坏"模式**不是定理**

专家：对固定 $S$，兼容行对的集合是
$$\mathcal C_S=\{(x,y)\in S\times S:\ xZ_1+yZ_2=0\},$$
它**允许多个 $y$ 对应同一 $x$**，也允许多种选行方式。故 $H_A$ **不被** $H$ 唯一决定，
$P(\lambda)=\lambda H-H_A$ 在同一纤维内可变。**恒等式 $H_A\equiv-HZ$ 是例子的特殊性，不是 Grassmann 判据的推论。**

### 4. 策略调整（专家 §8–§12）：从"继续收窄"改为"三项工作流 + 五阶段"

**三条工作流**
* **A 逐分量定理**：设 $X$ 是固定秩 $\omega$、$(5a)$ 可容许参数簇的一个不可约分量，则
  **要么 $X$ 全坏，要么好点在 $X$ 中 Zariski 开稠密**；$\mathbb C(X)$ 上 generic gcd 给出精确判据。（闭性论证支持）
* **B 定案 $k=\omega$**：此时 $\ker H=0$，$(5a)$ 在受限映射层面自动成立，参数族**仿射**，
  生成性定理适用 ⟹
  $$\boxed{\text{秩满的仿射族存在好设计}\iff\text{generic 铅笔是好的}}$$
  这是通向"paper-ready 定理"的最佳候选。
* **C 把 $k>\omega$ 当真正困难区**：先做 **$k-\omega=1$** 与 **固定 $k-\omega$**；
  理由：$\dim\operatorname{Gr}(\omega,k)=d\omega$ 随 $k$ **线性**增长。

**优先级（专家明确）**：① 修正当前例子 ② **证 $k=\omega$ 的仿射族定理** ③ 在 $k>\omega$ 造"**同一 $S$ 上既有好点又有坏点**"的例子
④ $k-\omega=1$ ⑤ **之后**才决定是否做硬度归约。**明确不要**在下一轮去做"刚性恒等式模式"的一般证明。

**"什么算确定结果"（专家 §10）**：定理 A（Grassmann 精确刻画）· B（逐分量谱二分）· C（仿射族可解性）·
D（低维完全分类，如 $q=3,\omega=2,k\le3$ 或 $k-\omega=1$）。

**专家最强建议（§12）**：下一个可交付 = **$k=\omega$ 的严格、可发表定理** + **两个例子的完整精确审计**。

### 5. 对 DEC/OPT/FIND 的一处修正（专家 §1/§11）

**不要**断言"二分等价"——**可行性对 $q$ 的单调性未证**。改为：DP 逐项扫描 $\le n-r+1$ 个 $q$（仍是多项式多个），
故 $\mathrm{OPT}\equiv\mathrm{DEC}$ 依然成立；另需**声明输出域**并**允许 $q_{\min}=+\infty$**。（`docs/00 §0.1.2` 已改）

## 全层不可行实例（第一个**可证下界**）：$q_{\min}\ge3$

**实例**：$n=4$、$p=1$、$r=1$、$q=2$、$C=e_1^{\mathsf T}$、
$$A=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&1&0&0\\0&0&0&0\end{pmatrix},\qquad L_0=e_3^{\mathsf T},$$
$K=\langle(0,-1,-1,0),(0,-1,0,0)\rangle$（$k=2$，$\operatorname{rank}[C;CA]=2$）。
脚本：`tools/verification/all_strata_infeasible.py`。

**逐层判定（全部为结构性论证，非采样）**

| 层 | 判据 | 结论 |
|---|---|---|
| $\omega=0$ | Grassmann 判据在 $\omega=0$ 时 $S=0$，需 $E+F_0=0$；而 $E=\operatorname{row}(-1,0)\ne0$ | **空** |
| $\omega=1$ | $(N1)$：$\dim(E+F_0)$；$E=\mathrm{span}\{(-1,0)\}$、$F_0=\mathrm{span}\{(-1,-1)\}$ 独立 ⟹ $\dim(E+F_0)=2>1=\omega$ | **空**（$(N1)$ 直接排除）|
| $\omega=2$ | $q=2=\omega$ ⟹ **方阵** ⟹ 专家定理：必失败 | **不可行** |

$$\boxed{\text{三层全不可行}\ \Longrightarrow\ \text{该实例在 }q=2\ \text{不可行}\ \Longrightarrow\ q_{\min}\ge3}$$

**为什么这次算"可证"而不是"网格证据"**：三个层的排除都来自**结构性条件**
（$E\ne0$、$(N1)$ 失败、方阵障碍），**不依赖**对 $R$ 的枚举。脚本里的 $R$ 枚举只是旁证。

**这是本项目第一个 $\boxed{q_{\min}\ge3}$ 的**具体实例 + 结构证明**。
$q_{\min}$ 的准确值还需查 $q=3$（三个层 $\omega=0,1,2$，其中 $\omega=3=q$ 为方阵、$\omega\le2$ 需逐个判）。

## **重要的降级**：该实例的 $\omega=2$ 层全坏，但**实例本身可行**（经 $\omega=1$）

上节证明了该实例的秩-2 可容许层整族全坏。**但这不推出实例不可行**——$\omega=1$ 层可行：

**构造（$\omega=1$）**：取 $B_1$ 的行都是 $\alpha_j(0,0,1)$、$B_2$ 的行都是 $\beta_j(0,0,1)$。则
* $\operatorname{rank}H=1$（$H$ 的行全在 $\mathrm{span}\{(0,0,1)\}$ 上）✓
* $(5a)$：$H_A$ 的行也在同一 span 内 ⟹ $\operatorname{row}H_A\subseteq\operatorname{row}H$ ✓
* 可达性：$B_1Z_1=0$、$B_2Z_2=0$（因 $Z_1,Z_2$ 的第三行都是 0）✓ ⟹ 由 Prop 2 存在 $R$
* 谱条件（$\omega=1$ 判据）：$\operatorname{rank}[H\ H_A]=2$ ⟺ 存在 $j$ 使 $\beta_j\ne0$ ✓

⟹ **$\omega=1$ 可行** ⟹ 该实例在 $q=3$ **可行**；同理 $q=2$ 时 $m=1$、$B_1$ 只有 1 行，构造同样成立 ⟹ **$q=2$ 也可行**。
而 $q=1$：$m=0$、$H=E$ 秩 1 $=\min(q,k)$ ⟹ 方阵 ⟹ 不可行；$\omega=0$：$E\ne0$ ⟹ 空。
$$\boxed{\text{该实例 }q_{\min}=2}$$

### 结论（必须记下的教训）

$$\boxed{\text{"某层可容许但全坏"}\ \textbf{不}推出"实例不可行"——可行性可由更低层提供}}$$

故"坏的可容许分量"**不是**硬度的充分条件，硬度需要**更强的组合**：
$$\text{所有层}\ \omega=0,1,\dots,\min(q,k)\ \text{都不可行（空或全坏）}$$
而这正是 $q_{\min}$ 的定义所要求的。**这是对本轮"首个坏分量例子"意义的重要降级**——
它仍是"可容许层非空但全坏"的严格例子（数学上真实），但**不能**作为硬度靶子。

**下一步的真正目标**：找一个实例，使**全部** $\omega$ 层都不可行（$q_{\min}>q$ 对某个 $q$）。

## 命题：上述实例的秩-2 可容许层**整个都是坏的**（单位缩放论证）

设该实例的可容许层由两个"射线族"组成（Grassmann 判据给出 2 个 $S$），每个族有标量自由度 $t$：
$$B_1(t)=t\,B_1^{(1)},\quad B_2(t)=t\,B_2^{(1)},\qquad t\ne0 .$$
（$t=0$ 时 $\operatorname{rank}H=1$，不在秩-2 层上。）

由 $RN_K=B_1$、$RAN_K=B_2$ 的**线性性**，$R(t)=t\,R(1)$；而顶部块与 $t$ 无关，故
$$H(t)=\begin{bmatrix}E\\ tB_1^{(1)}\end{bmatrix},\qquad
H_A(t)=\begin{bmatrix}0\\ tB_2^{(1)}\end{bmatrix},\qquad
P(t,\lambda)=\lambda H(t)-H_A(t)=\begin{bmatrix}\lambda E\\ t\bigl(\lambda B_1^{(1)}-B_2^{(1)}\bigr)\end{bmatrix}.$$

于是 $P$ 的每个 $\omega$ 阶子式都等于 $t^{s}$（$s\in\{0,1,2\}$）乘以 $t=1$ 时对应子式。在**函数域** $\mathbb Q(t)$ 中
$t$ 是**单位**，故
$$\boxed{\gcd_{\mathbb Q(t)[\lambda]}\{\text{子式 of }P(t,\cdot)\}\ \text{的 }\lambda\text{-次数}\ =\ t=1\ \text{时的次数}}$$
而 $t=1$ 时已算出该次数 $=2>0$ ⟹ **整族（除退化点 $t=0$）都是坏的** ✓

**结论（严格）**：
$$\boxed{\text{该实例在 }\omega=2\text{ 的整个可容许层都是坏的} \Longrightarrow \omega=2\ \text{层不可行}}$$

**限定**：这只说明 $\omega=2$ 层不可行；该实例在 $q=3$ 是否可行还要看 $\omega\in\{0,1\}$ 两层
（$\omega=1$ 时判据是 $\operatorname{rank}[H\ H_A]=2$，可另算）。

**意义**：这是**第一个"可容许层非空但全坏"的严格例子**（$k=3>\omega=2$）——
即专家所说"坏的可容许分量"这一硬度靶子的第一个真实实例；且证明只用了**单位缩放**，很短。

## Grassmann 判据 → $R$ 回代：**脚本报不相容**（与 Prop 2 冲突 ⟹ 我方编码有 bug）

脚本 `tools/verification/grassmann_recover_and_test.py`：对两个可容许 $S$（$\sigma=(1,\pm1,0)$）构造
$B_1$（$x_1$ 张成 $S/E$ + 补零行）与 $B_2$（解 $xZ_1+yZ_2=0$），再解 $RN_K=B_1$、$RAN_K=B_2$。

**结果**：$H$ 与 $[H;H_A]$ 的秩都是 2 ✓（层上的点造对了），但
$$\boxed{R\ \text{的线性系统报"不相容"}$$
而按 **Prop 2（精确像定理，专家核验过）**，只要 $B_1Z_1+B_2Z_2=0$ 就应可解——构造时正是按此施加的。
⟹ **矛盾**，说明我方脚本在**编码约定**上有 bug（候选：$N_K$ 的摆放、$ANK$ 与 $A$ 作用方向、
或 $B_1,B_2$ 与 $Z_1,Z_2$ 的行/列约定不一致）。

**状态**：Grassmann 判据部分**成功**（层非空、2 个 $S$）；$R$ 回代部分**未成功**（非数学问题，
是脚本约定问题）。**下一步只需修这一处编码**，修好后即可算出该实例的"好/坏"。

**教训（已记）**：$B$、$Z$、$N_K$ 三处都涉及"行/列 + K-坐标 vs 环境坐标"的双重约定，
本项目历史上已在此类约定上出错多次（§7.2、§10.1）；本次应先把三者的形状**逐一 assert** 再解系统。

### 修复后（两处约定 bug）**回代成功**，谱判定：两个可容许 $S$ **都是坏**

修的两处（都是约定错误）：
1. $N_K$ 的**列**才是 $K$ 的基——原来把行当成了基，导致系统不相容；修正后 **$R$ 可解** ✓（Prop 2 得到印证）；
2. $H_A$ 少了一个**零行**（$L_0AN_K=0$ 仍是行），补上后矩阵才是 $q\times k$；
3. 子式原来只取**列对** $(0,1)$，改为遍历全部 $\binom{3}{2}=3$ 个列对。

**修正后的结果**（`grassmann_recover_and_test.py`）：
| $\sigma$ | $S$ | $\operatorname{rank}H$ | $\operatorname{rank}[H;H_A]$ | $R$ 可解 | 子式 gcd 次数 | 判定 |
|---|---|---|---|---|---|---|
| $(1,1,0)$ | $\{x_1+x_2=0\}$ | 2 | 2 | ✓ | 2 | **坏** |
| $(1,-1,0)$ | $\{x_1-x_2=0\}$ | 2 | 2 | ✓ | 2 | **坏** |

**结论**：
$$\boxed{\text{该实例（}k=3>\omega=2\text{）的秩-2 可容许层**非空但全坏** ⟹ 该实例在 }\omega=2\text{ 不可行}}$$
即**存在"可容许但全坏"的实例**——正是专家所说"坏的可容许分量"这一硬度靶子的**第一个真实例子**。

**仍需补的限定**（诚实）：
* 每个 $S$ 对应的 $B_1$ 有一个**标量自由度**（$x_1$ 的倍数）；标量不改变"坏"的判定，故沿该族应恒坏，
  但**严格**的做法是在函数域上算 $\Delta$ 的**次数**（专家 §2 方法 2）；
* 该层的可容许集是否**恰好**是这两个单参数族（而非更多），需由 Grassmann 判据的**完备性**保证
  （判据是 $\iff$，故完备 ✓，但"每个 $S$ 对应一族"这一点还需写清）。

## Grassmann 判据的**首次实现**（$L_0=e_4^{\mathsf T}$）：层**非空**，但只对应 **2 个** $S$

脚本：`tools/verification/grassmann_criterion_l0e4.py`（纯 Fraction 精确有理，**不用任何 CAS**）。

**数据**（$n=5$、$p=1$、$q=3$、$r=1$ ⟹ $k=3$、$m=2$、$\omega=2$）：$C=e_1^{\mathsf T}$；$A$ 第一行 $e_5^{\mathsf T}$、
列 $2,3,4=e_3,e_2,e_5$；$K=\langle e_2,e_3,e_4\rangle$，$N_K=[e_2,e_3,e_4]$；$L_0=e_4^{\mathsf T}$。
在 $K$-坐标里：$E=\operatorname{row}(0,0,1)$、$F_0=0$、$\ker T$ 由 $(-e_3,e_2)$、$(-e_2,e_3)$ 生成。
$S$ 用余向量 $\sigma\in\mathbb F^{1\times3}$ 参数化：$S=\{x:x\sigma=0\}$。

**结果**：
* $(N1)$ $\dim(E+F_0)=1\le2$ ✓；$(N2)$ $\omega-\dim E=1\le m=2$ ✓（两条必要条件都过；
  这正是 $L_0=e_2^{\mathsf T}$ 过不了 $(N1)$、而 $e_4^{\mathsf T}$ 能过的差别）；
* 枚举 49 个 $\sigma$（归一化射影点）：满足 $E+F_0\subseteq S$ **且** $E+X_S=S$ 的**只有 2 个**：
$$\sigma=(1,1,0)\ \Rightarrow\ S=\{x_1+x_2=0\},\qquad \sigma=(1,-1,0)\ \Rightarrow\ S=\{x_1-x_2=0\}$$
（两者的 $\dim X_S=2$、$\dim(X_S+E)=2$ ✓）

**结论**：
$$\boxed{\text{秩-2 可容许层**非空**（Grassmann 判据给出存在性），但只对应 }\mathbb P^1\text{ 参数族中的 2 个 }S}$$

**这把先前 6 次实验失败解释清楚了**：可容许的 $R$ 全部落在**两个离散的 $S$** 之上，
在 $R$-空间里是**低维薄集**，随机采样（无论多细）都几乎不可能命中。

**下一步**：按专家建议的"结果 ③"——由这两个 $S$ 构造出精确的 $R$（解线性系统），
再在该点上算 generic gcd（"好/坏"），从而判定该实例的可行性。

## 专家第二十轮：**Grassmann 非空判据**（定理）+ 实验裁决 + 下一步

### 1. 新定理（专家给，本轮最重要的结果）

记 $E:=\operatorname{row}(L_0N_K)$（顶部块的**行空间**）、$F_0:=\operatorname{row}(L_0AN_K)$、
$Z=\begin{bmatrix}Z_1\\Z_2\end{bmatrix}$ 为 $\ker T$ 的基、$m=q-r$，并对 $S\in\operatorname{Gr}(\omega,k)$ 定义
$$X_S:=\{x\in S:\ \exists y\in S,\ xZ_1+yZ_2=0\}.$$
**定理（秩 $\omega$ 可容许性的 Grassmann 判据）**
$$\boxed{\exists R:\ \operatorname{rank}H(R)=\omega\ \wedge\ \operatorname{rank}\begin{bmatrix}H\\H_A\end{bmatrix}=\omega
\iff\exists S\in\operatorname{Gr}(\omega,k):\ \ E+F_0\subseteq S,\quad E+X_S=S,\quad \omega-\dim E\le m.}$$
*必要性*：取 $S=\operatorname{row}H(R)$；顶部块给出 $E,F_0\subseteq S$；底块每行 $x_i\in X_S$ 且 $S=E+\mathrm{span}\{x_i\}$；
加 $m$ 行最多升 $m$ 维 ⟹ $\omega-\dim E\le m$。
*充分性*：取 $d=\omega-\dim E$ 个 $x_i\in X_S$ 张成 $S/E$，配对应 $y_i$，补零到 $m$ 行；由可达对刻画（Prop 2）得 $R$ ✓

**两条廉价必要条件**：
$$(N1)\ \dim(E+F_0)\le\omega,\qquad (N2)\ \omega-\dim E\le m.$$
**这正是 $L_0=e_2^{\mathsf T}$ 层为空的解释**：$E=\mathrm{row}(1,0,0)$、$F_0=\mathrm{row}(0,1,0)$ ⟹ $\dim(E+F_0)=2>1=\omega$ ⟹ 空 ✓

### 2. 实验裁决（专家 §2）

* **实验 1 的 12 个"全坏"实例**：只能记作"**在枚举网格上未找到好点**"，**不能**记作"可容许轨迹全坏"，
  更不能断言**坏分量存在**（网格不是 Zariski 稠密）；混合实例只证"坏集非空且真"；
* 要证坏分量须逐分量：① 精确不可约分解 ② 函数域上算 generic gcd ③ 或用 $(A,C,L_0)$ 的结构恒等式（实验 5 就是第三种）；
* **实验 4**：有效**单侧**存在性证据；但谱检验应给**精确 Bézout 证书** $\sum_I u_Im_I=1$，不要浮点求根；
* **结构澄清**：$K\cap AK=0$ **不够**，须 $\ker(A|_K)=0$ **且** $K\cap AK=0$（即 $K\cap A^{-1}K=0$）。
  实验 4 的构造满足（$Ae_7=e_4,e_8=e_5,e_9=e_6$ 在 $K$ 上单射 ✓）。

### 3. 下一步（专家 §6–7）：先实现 Grassmann 判据，再做定向实验，最后逐分量

**理由**：逐分量需要可用的不可约分解；而目前连 $L_0=e_4^{\mathsf T}$ 那一个实例的**非空性**都还没可靠建立。
正确顺序：**判空 → 精确取点 → 定分量 → 算 generic gcd**。

**$L_0=e_4^{\mathsf T}$ 的具体方案**（$k=3,\omega=2$ ⟹ $\operatorname{Gr}(2,3)$ 只有 2 维）：
用**余向量**参数化 $S=\ker\sigma$（$[\sigma]\in\mathbb P^2$）；$E+F_0\subseteq S$ 变成 $\sigma$ 的线性方程；
再对每个候选 $S$ 算 $X_S$ 并测 $E+X_S=S$。三种结果：
① 无 $S$ ⟹ 层空（结构性结论）② 有 $S$ 但脚本取不到 $R$ ⟹ 数学非空、纯计算问题 ③ 取到 $R$ ⟹ 算该分量的 generic gcd。

## 实验 C（约束区域，$L_0=e_4$ 版）：脚本报 sympy 错误，**未得出结论**

按上一节教训把 $L_0$ 换成 $e_4^{\mathsf T}$（顶部块 $(0,0,1)$ 与 $(0,0,0)$ 相容）后重跑，
脚本在 sympy 的 `strongly_connected_components`（`rank` 内部）抛出 `NonSquareMatrixError`，**崩溃**。

**未解决的原因**：疑在 `H.rank()`/`sp.Matrix.vstack(H,HA).rank()` 于非方阵上触发了 sympy 的某条路径
（也可能是 `v3` 的构造使 `B1` 形状异常）。**未定位到底**（本轮预算用尽）。

**正确做法（下次）**：
1. 不再依赖 sympy 的 `rank`，改用项目自己的 `linalg_q.rank`（精确有理、已在别处稳定使用）；
2. 判据也用项目自己的 gcd 工具，而不是 sympy 的 `gcd`/`degree`；
3. 并**显式 assert** 形状（$H$ 是 $3\times3$、$B_1$ 是 $2\times3$），避免 sympy 静默走别的路径。

**状态**：约束区域的实验**仍未完成**（5 次尝试：随机采样、$n{=}6$、$n{=}9$ 自由区、$L_0{=}e_2$ 空层、
$L_0{=}e_4$ 脚本崩溃）。前三次的教训都已固化（薄集不采样、$n-p\ge2k$、顶部块相容性）。

### 追加：换成自写 `my_rank`（精确有理高斯消元）后**仍然崩溃**

已把全部 `linalg_q.rank` 调用换成脚本内的 `my_rank`（Fraction 高斯消元），
崩溃**依旧**出现在 sympy 的 `strongly_connected_components`（`NonSquareMatrixError`），
故**不是** `rank` 的问题，而在另一条 sympy 路径（候选：`sp.gcd` 对含 `lam` 表达式、
或 `sp.Matrix` 的 `det` 在某些输入上）。**未定位。**

**结论**：约束区域的实验在本会话内**未能完成**（6 次尝试：随机采样、$n{=}6$、$n{=}9$ 自由区成功、
$L_0{=}e_2$ 空层、$L_0{=}e_4$ 崩溃 ×2）。
**修法**：彻底去掉 sympy——用 `sympy` 只做符号表示，gcd 用自写 Euclid（Fraction 系数），
或直接用项目的 `poly_smith`／`spectral_gcd` 工具。

**已固化的三条实验教训**（都对以后有用）：
1. **薄集不采样**（余维 $\ge1$ 的层，随机命不中）；
2. **区域要对**（自由区需 $n-p\ge2k$）；
3. **顶部块要相容**（否则该 $\omega$ 层为空）。

## 实验 C（约束区域）：探针**再次空集**，但定位到**$L_0$ 可使层为空**

**设定**：$n=5$、$p=1$、$q=3$、$r=1$ ⟹ $k=3$、$\operatorname{rank}[C;CA]=2$、$\dim(K+AK)=4<6$ ✓ **约束区域**；
按 Prop 2 参数化（$B_2e_2=B_1e_3$、$B_2e_3=B_1e_2$），$H=\begin{bmatrix}L_0N_K\\B_1\end{bmatrix}$；
为避开"随机采样打不中余维 1 层"，这次**按构造**令 $\operatorname{rank}H=2$（$H$ 第 3 行 $=\alpha\cdot$第 1 行 $+\beta\cdot$第 2 行）。

**结果**：3000 次采样，**可容许点 0**。

**诊断（结构性，非探针错）**：取 $L_0=e_2^{\mathsf T}$ 时顶部块是
$$L_0N_K=(1,0,0),\qquad L_0AN_K=(0,1,0).$$
要求 $\operatorname{rank}H=2$ 且 $\operatorname{row}H_A\subseteq\operatorname{row}H$ ⟹ $\operatorname{row}H$ 必须同时含 $(1,0,0)$ 与 $(0,1,0)$
⟹ $\operatorname{row}H=\operatorname{span}\{e_1,e_2\}$ ⟹ $H_A$ 的各行第三分量为零；但可达性约束 $B_2e_3=B_1e_2$ 又迫使
$B_2$ 的第三列等于 $B_1$ 的第二列，于是 $\operatorname{rank}H=2$ 与第三分量为零**不可同时满足**（除退化情形 $\operatorname{rank}H\le1$）。
$$\boxed{\text{故对 }L_0=e_2^{\mathsf T}\text{ 该实例的 }\omega=2\ \textbf{层是空的}}$$

**这本身是一个发现**：$\omega=2$ 层是否非空**依赖 $L_0$**（顶部块必须相容）。例如 $L_0=e_4^{\mathsf T}$ 时
$$L_0N_K=(0,0,1),\qquad L_0AN_K=(0,0,0),$$
顶部块相容（第二个为零），层应非空 ⟹ **下次探针应改用 $L_0=e_4^{\mathsf T}$**（或先枚举 $L_0$ 判层是否非空再实验）。

**状态**：约束区域的探针**未得出结论**（层为空），但得到两条可复用的教训：
1. **必须先用顶部块相容性筛掉 $L_0$**（否则层为空、实验无意义）；
2. 若要让 $\operatorname{rank}H=\omega$ 成立，须**按构造**而不是随机（随机命不中余维 $\ge1$ 层）。

## 实验 C（成功版）：$k=3>\omega=2$ **自由区域**上**存在可行点**（125 好 / 75 坏）

**数据**（`tools/verification/exp_c_n9p3.py`）：$n=9$、$p=3$、$q=3$、$r=1$ ⟹
$C=[I_3\ 0]$、$A$ 的列 $4,5,6=e_1,e_2,e_3$、列 $7,8,9=e_4,e_5,e_6$ ⟹
$$\operatorname{rank}[C;CA]=6\ ✓,\qquad k=3\ ✓,\qquad K=\langle e_7,e_8,e_9\rangle,\ AK=\langle e_4,e_5,e_6\rangle,\
K\cap AK=0\ ✓$$
（**自由区域**：可实现性引理适用，$L_0N_K=(1,0,0)$、$L_0AN_K=(0,0,0)$。）

**构造式采样**：随机满列秩 $U$（$3\times2$，首行 $(1,0)$）、$G$（首行 $(0,0)$），$V=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix}$，
$H=UV$、$H_A=GV$；解 $RN_K=H_{2:3,:}$、$RAN_K=(H_A)_{2:3,:}$ 得 $R$；判据 = $3\times2$ 铅笔 $\lambda U-G$ 的三个 2 阶子式的 gcd 是否常数。

**结果**：
$$\text{200 次构造：线性系统不可解 }0,\qquad \textbf{好 }125,\qquad \textbf{坏 }75$$
⟹ 该层（$k=3>\omega=2$，自由区域）**存在可行点**；坏点构成**真闭子集**（75/200 落在其上）✓

### 结论（对 $q1$ 的意义）

1. **$k>\omega$ 的"自由"部分有可行点**：$125/200$ 的构造可行 ⟹ 该层**不是全坏分量**；
2. 与闭性定理一致：坏集是真闭子集，可行集开稠密；
3. **仍未检验**的是**约束区域**（$K\cap AK\ne0$，即 $n-p<2k$）——那才是专家第十九轮指认的
   "非线性可容许簇"所在，也是目前**唯一未排除**的硬度潜在来源；
4. 本轮的两次失败（随机采样、$n=6,p=2$）已在前两节记录，修法（结构化采样 + 维数条件 $n-p\ge2k$）已固化。

**状态**：实验 C 的**自由部分完成**（有可行点）；约束部分仍未做。

## 实验 C（结构化版）：再次失败，但**定位到维数障碍**——$k=3$ 的"自由区域"需要 $n\ge9,p\ge3$

**尝试**（`tools/verification/exp_c_structured_k3w2.py`）：$n=6$、$p=2$、$q=3$、$r=1$，想用
"$H=UV$、$H_A=GV$ 构造目标对，再解线性系统得 $R$"的结构化采样（修法 ①/②）。

**实测**：$\operatorname{rank}[C;CA]=4$、$\dim K=2$（**不是** 3）⟹ 构造出错。

**定位（这才是真正的收获）**：$CA=C A$ 只用 $A$ 的**前 $p$ 行**；为使 $\operatorname{rank}[C;CA]=n-k$ 恰好，
这 $p$ 行被迫承担全部"新增方向"，于是 $A$ 的列 4..6 在前 $p$ 行上必须为零，
从而 $A(K)\subseteq\ker C$；又 $K\subseteq\ker C$（$\dim\ker C=n-p$），故
$$\dim\bigl(AK\cap K\bigr)\ \ge\ k+k-(n-p)=2k-(n-p).$$
于是 **$\dim(AK\cap K)=0$（自由区域）要求 $\boxed{n-p\ \ge\ 2k}$**——与第九/十三轮的条件一致，
但这里给出了它对本实验的**具体算术**：

| 目标 | 需要 | 最小实例 |
|---|---|---|
| $k=3$ 自由区域 | $n-p\ge6$ 且 $n-k\le2p$（因 rank$[C;CA]\le2p$）| $p\ge3,\ n\ge9$（取 $p=3,n=9$）|
| $k=2$ 自由区域 | $n-p\ge4$、$n-2\le2p$ | $p=1,n=4$ ✗（$4-1=3<4$）；$p=2,n=6$ ✓ |

**结论**：$k=3$ 的结构化实验**必须**在 $n\ge9,p\ge3$ 上做（$n=6,p=2$ 必然落在约束区域，
而约束区域里"$H=UV$ 再解线性系统"不一定可解——实测 287/300 不可解，正是这个原因）。

**状态**：本探针**未得出结论**（构造前提不成立），但把"实验 C 该在什么维数上做"算清楚了：
$$\boxed{k=3\ \text{层的最小自由实例}:\ n=9,\ p=3,\ \operatorname{rank}[C;CA]=6}$$
这是下一次实验的**明确接口**。

## 实验 C（续，$k=3$、$\omega=2$）：**探针设计失败**（随机采样打不中该层）

**尝试**：$n=5$、$p=1$、$q=3$、$r=1$ ⟹ $k=3$、$m=2$；$C=e_1^{\mathsf T}$、$A$ 第一行 $e_5^{\mathsf T}$（$K=\langle e_2,e_3,e_4\rangle$）、
其余行随机；$R$（$2\times5$，10 个条目）在 $\{-2,\dots,2\}^{10}$ 中随机采 600 点，用 `consistency_checks` 精确判定。

**结果**：6 个实例**全部**得到"可容许点数 $=0$"。

**诊断（不是"可容许集空"，而是探针错了）**：
* 该实例里 $H=\mathcal L N_K$ 是 $3\times3$，要求 $\operatorname{rank}H=2$ 是**余维 1** 条件（$\det H=0$）；
* 再叠加 $\ker H\subseteq\ker H_A$（又一个闭条件）；
* 在 $\{-2..2\}^{10}$ 上随机采样，命中"余维 $\ge1$ 闭层"的概率极低 ⟹ 采样几乎必空。
  （这正是 §10.1 记录的"薄集不许采样"禁区：**可行集/目标层是余维 $\ge1$ 的代数集**时，随机采样必错过。）

**正确做法（下次）**：
1. 用**结构化采样**：取满列秩的 $U\in\mathbb R^{q\times2}$、满行秩 $V\in\mathbb R^{2\times k}$，令 $H=UV$；
   再对 $R$ **解线性系统** $RN_K=H_{\text{bot}}$（必要时叠加 $RAN_K=(H_A)_{\text{bot}}$），得层上的点；
2. 或按 Prop 2 直接在**可达族**上参数化（$B_1,B_2$ 满足 $B_1Z_1+B_2Z_2=0$），再回代求 $R$；
3. 注意维数条件：$k=3$、$n=5$ 时 $2k=6>n$ ⟹ **必然** $K\cap AK\ne0$（约束区域）；
   若要进"自由区域"须 $n\ge2k$，例如 $n=6,p=2$（rank$[C;CA]=3$ ⟹ $k=3$，$2k=6=n$ 恰临界）。

**状态**：本探针**未得出结论**（不计入证据）；已记录设计与修法。

## 实验 C（专家清单）：$k>\omega$ 时**坏的可容许分量确实存在**（但 $\omega=1$ 仍秩可判）

**设定**：$n=4$、$p=1$、$q=2$、$r=1$（$k=2>\omega=1$）；$C=e_1^{\mathsf T}$、$A$ 第一行 $e_4^{\mathsf T}$（$K=\langle e_2,e_3\rangle$）、
其余行随机；$R\in\{-1,0,1\}^4$ 枚举，用 $\omega=1$ 的判据（专家定理）：
可容许 = $\operatorname{rank}H=1\wedge\operatorname{row}H_A\subseteq\operatorname{row}H$；好 = $\operatorname{rank}[H\ H_A]=2$。

**结果**（`tools/verification/exp_c_bad_component.py`，32 个实例）：

| 类别 | 个数 |
|---|---|
| 可容许集**空** | 16 |
| 可容许但**全坏** | **12** |
| 可容许且**全好** | 2 |
| 同一实例**既好又坏** | 2 |

**结论 1（回答实验 C 的问题）**：**坏的可容许分量确实存在**（12/32），且"同实例含好点与坏点"也出现（2/32）
⟹ 逐分量分析**不是形式上的可能性，而是真实现象** ✓

**结论 2（重要的nuance）**：**"坏分量存在" ≠ "难"**。在 $\omega=1$ 层，专家已证判定是
$$(5b)\iff\operatorname{rank}[H\ H_A]=2,$$
即**秩可判**。所以这些"全坏"实例虽然展示了坏分量，但**判定仍是容易的**。

**结论 3（更精确的靶子）**：硬度目标必须同时满足**两条**
$$\boxed{\omega\ge2\quad\text{且}\quad k>\omega}$$
——比专家清单里"$\omega\ge2$"（第五轮）与"$k>\omega$"（第十九轮）**各自单独**的条件都更窄。
$\omega=1$ 的坏分量再普遍也不构成硬度；$\omega=2$ 且 $k=\omega$ 时是仿射族（专家判定"倾向可解"）。
⟹ **唯一未排除的战场：$\omega\ge2$ 且 $k>\omega$。**

## 专家第十九轮：三处更正 + 证据评估（**否证 ≠ 硬度**）+ 实验清单

### 1. 更正的**子式计数**（我错了）

$U=[I_\omega;0]$ 时，$q\times\omega$ 铅笔的极大子式按行分布：

| 用到的行 | 个数 | $\lambda$ 次数 |
|---|---|---|
| 全为活跃行 | $1$ | $\omega$ |
| 一活跃一非活跃 | $2(q-2)$ | $\le1$ |
| 两行都非活跃 | $\binom{q-2}{2}$ | $0$ |

故 $\omega=2$ 正确的描述是
$$\boxed{1\ \text{个二次}+2(q-2)\ \text{个线性}+\tbinom{q-2}{2}\ \text{个常数}}$$
（我写的"$1+(q-2)$ 个线性"**错**；$q=3$ 时恰好也是 1+2 ⟹ 之前没暴露。）

### 2. 术语更正：这是 **right primeness**（右互质），不是"正则"

对**矩形**铅笔，正确说法是"对一切有限 $\lambda$ 满列秩"，即多项式矩阵理论中的 **right prime**；
"regular" 是方阵铅笔的术语，不可混用。本项目的谱条件 = 降阶铅笔的 right primeness。

### 3. 我的反例**范围要缩小**（重要）

* 它否证的是"**那几个普通秩不变量**足以判定"，**不是**"一切基于秩或代数的判据"；
* 它**没有**证明 $G_a,G_b$ 属于**同一个**观测器诱导的可达族——若要用它支撑关于 REAL-AUG 的定理，须核验这一点；
* 另有冗余：$U$ 满列秩时 $\operatorname{rank}[U;G]=\omega$ 自动成立，四元组里该项无信息。

### 4. 更好的 resultant 构造（专家给）

取全部子式的两组**一般线性组合** $f_a=\sum a_im_i$、$f_b=\sum b_im_i$，令
$$\mathcal R(t,a,b)=\operatorname{Res}_\lambda(f_a,f_b)$$
则在 $\mathbb C(t,a,b)$ 上
$$\boxed{\mathcal R\not\equiv0\iff\gcd(m_1,m_2,m_3)=1}$$
且 **$\deg_t\mathcal R\le8$**（每个子式对 $t$ 二次 ⟹ 系数二次 ⟹ Sylvester 为 $4\times4$）。
**注意**：齐次 resultant 会检测**无穷远公共根**；$U$ 满列秩保证一处子式非零，一般组合避开无穷远，
但实现时须显式检查首项秩或用子结式/gcd 直接测**有限**公共根。

### 5. 证据评估（专家给的平衡表述）

| 主张 | 评估 |
|---|---|
| 普通秩不变量在 $\omega=2$ 决定可行性 | **已被否证** |
| 固定铅笔的谱可行性困难 | **不**；是一元 gcd |
| **$k=\omega=2$ 的仿射族可行性困难** | **证据指向可解**（生成性定理给有限精确计算，次数与参数个数无关）|
| 一般 $k>\omega$ 的观测器综合可解 | **开放** |
| 一般 $k>\omega$ 为 $\exists\mathbb R$-hard | **未证** |
| **可容许行列式簇是剩余复杂度的可能来源** | **强结构假设，值得追** |

**他的结论**："秩-only 是错的，但证据**尚不支持硬度猜想**；仿射谱子问题有生成性代数判据；
真正的障碍更可能来自 $(5a)$ 的非线性可容许簇，尤其 $k>\omega$ 时。"

### 6. 修订优先级 + 四个实验

1. **先改正并固化 $\omega=2$ 的代数**（子式计数、三个显式子式、反例范围、实现 $\deg\le8$ 的 resultant）；
2. **继续逐分量分类**（主方向：$k>\omega$；图卡上的可容许轨迹；最小非平凡例的不可约分量；逐分量 generic gcd）；
3. **识别真正的非线性瓶颈**（实点？分量选择？generic 谱可行性？相互作用？）；
4. **最后才试归约**（目标应是**非线性可容许几何**，不是 $\omega=2$ 的仿射公共根条件）。

四个实验：**A** 计算验证仿射生成性定理（generic resultant + 采样比对）；**B** 同数据下比较 $k=\omega$ 与 $k>\omega$；
**C** 搜索"坏的可容许分量"（$k>\omega$、可容许轨迹非空、某分量 generic gcd 非常数、另一分量或另一实例为常数）；
**D** 之后才试二次编码（须满足**六条**：源问题编码、变量表示、方程强制、两个方向的对应、位复杂度）。

**归约的六条要求**里他最强调：**"每个可行增广都对应源解"**（没有意外的可行增广）——这比"源解 ⟹ 可行"难得多。

## Stage 3 入口：$\omega=2$ 的谱条件 = "**1 个二次 + $(q-2)$ 个线性**无公共根"

### 1. 结构（机器已印证）

$q=3$、$\omega=2$、$k=2$ 时，$P=\lambda U-G$ 的三个 $2$ 阶子式（按行对 $(12),(13),(23)$）为
$$M_{12}=(\lambda-g_{11})(\lambda-g_{22})-g_{12}g_{21}\quad(\lambda\ \text{的二次}),\qquad
M_{13},M_{23}\quad(\lambda\ \text{的**线性**})$$
（`rank_only_omega2.py` 的输出印证：E1 的子式是 $[\lambda^2,\ -1,\ \lambda]$——一个二次 + 两个低次的。）

**一般 $q$**：$U$ 有 $\omega$ 个"活跃"行（$U_{I,:}$ 可逆）⟹ 该行对的子式是 $\lambda$ 的 $\omega$ 次；其余含"非活跃"行的子式
是**低次**的（对 $\omega=2$：一个二次 + $(q-2)$ 个线性）。

### 2. 于是坏条件是"1 个二次 + 若干线性有公共根"

其刻画 = 线性的公共根（一个**行列式条件**）∧ 二次在该点为零 ⟹ 坏集由**低次**多项式切出。
这解释了为什么 $\omega=2$ 的秩-only 失败：坏条件混合了 $g$ 的**乘积**（如 $g_{32}g_{11}$），不是秩能表达的。

### 3. 编码机会（Stage 3 的具体入口）

$G$ 的条目对 $R$ **仿射**，故坏条件中的乘积 $g_{ij}g_{kl}$ 是 $R$ 的**二次**式。因此：
* 若想让源问题的某个二次约束"变成"坏条件的一部分，应把它安排到**乘积分量**上；
* $\omega=2$ 恰好是**最小**的出现乘积的层（$\omega=1$ 时专家已证只是秩条件，无乘积自由度）；
* 与 $\omega=3$ 相比，$\omega=2$ 的坏条件次数最低 ⟹ **最可能给出硬度的层**。

### 4. 诚实状态

* 本节只给**结构**（子式次数分布 + 坏条件的形状），**未**给出归约；
* 要成归约，需证明：给定任意（或某个已知难的）二次约束族，能选 $(A,C,L_0)$ 与 $U$ 使坏条件恰好等价于它
  （且可达的 $G$ 覆盖所需范围）——这是 Stage 3 的正式任务；
* 已知障碍：$G$ 的可达集是**线性**的（Prop 2），而坏条件是**二次**的 ⟹ 这一不匹配正是归约要克服的核心困难，
  也可能是硬度真正的来源。

## **秩-only 猜想在 $\omega\ge2$ 不成立**（$\omega=1$ 成立）—— 机器核对的反例

专家第十八轮证明了 $\omega=1$ 时 $(5b)\iff\operatorname{rank}[H\ H_A]=2$（**秩决定**）。
本轮检验 $\omega=2$：**秩-only 失败**。

**设定**：$q=3$、$\omega=2$、$k=2$，故 $P=\lambda U-G$ 是 $3\times2$ 铅笔，判据 = 三个 2 阶子式的 gcd 是否常数。
固定 $U=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}$，枚举 $G\in\{-1,0,1\}^{3\times2}$，
按**同一组秩不变量** $(\operatorname{rank}U,\operatorname{rank}G,\operatorname{rank}[U\ G],\operatorname{rank}[U;G])=(2,2,3,2)$ 分组。

**结果**（`tools/verification/rank_only_omega2.py`）：
$$\text{该组不变量下：可行 }464\text{ 个，不可行 }112\text{ 个}$$
最小的一对（只差一个元素）：
$$G_a=\begin{pmatrix}-1&-1\\-1&-1\\-1&0\end{pmatrix}\ \Rightarrow\ \gcd=1\ (\text{可行}),
\qquad
G_b=\begin{pmatrix}-1&-1\\-1&-1\\-1&1\end{pmatrix}\ \Rightarrow\ \gcd=\lambda+2\ (\text{不可行}).$$
（两者秩不变量完全相同。）

### 结论

$$\boxed{\text{秩-only 猜想在 }\omega=1\text{ 成立（专家定理），在 }\omega\ge2\text{ **不成立**}}$$

* 故"可行性可由普通秩计算判定"（专家第十八轮列为**猜想**）在 $\omega\ge2$ **被否证**；
* 但**不是**说问题一定硬：判定仍是"$3\times2$ 铅笔的广义特征值是否存在"这类**可多项式判定**的问题
  （固定 $R$ 时是一元 gcd）；难的是"**$\exists R$**"。
* 意义：$\omega\ge2$ 保留了真正的代数内容（Kronecker/广义特征值结构），**不能**只用秩来判断——
  这为"硬度可能存在于 $\omega\ge2$"提供了正面证据，与专家 §9 的状态表一致（"秩-only 猜想"未证）。

## 专家第十八轮：可容许轨迹的正确几何 + **$\omega=1$ 的精确判据** + 五阶段修订计划

### 1. 正确的对象：可容许轨迹

$$\mathcal X_\omega=\Bigl\{R:\ \operatorname{rank}H(R)=\omega,\ \ \operatorname{rank}\begin{bmatrix}H(R)\\H_A(R)\end{bmatrix}=\omega\Bigr\}$$
（第二条等价于 $\operatorname{row}H_A\subseteq\operatorname{row}H$，即 $(5a)$。）
它是**局部闭行列式簇**，**不是**有限个仿射线性片之并。

*反例（专家给）*：$q=k=2$、$\omega=1$、$H=R$、$H_A=0$ ⟹ $\mathcal X_1=\{R\ne0,\ \operatorname{rank}R=1\}$，
其闭包是 $ad-bc=0$（不可约二次超曲面），**不**含于有限个真仿射子空间之并 ✓

### 2. 有用的替代：**固定行空间的纤维分解**

$\operatorname{Gr}(\omega,k)\ni S=\operatorname{row}H$：对固定 $S$，
$$\mathcal X_{\omega,S}=\{R:\ \operatorname{row}H(R)\subseteq S,\ \operatorname{row}H_A(R)\subseteq S\}$$
对 $R$ 是**仿射线性**条件，加上开条件 $\operatorname{rank}H=\omega$ ⟹
**纤维原理**：每个纤维是仿射线性子空间的相对开子集。且 $\mathcal X_\omega=\bigcup_{S}\mathcal X_{\omega,S}$。
（但 Grassmann 的标准有限图卡**不能**把整体化成有限仿射片——图卡里的方程仍是多项式的。）

### 3. 维数比较必须**逐分量**

$$\dim\mathcal B_\omega\ \text{vs}\ \dim\mathcal X_\omega\quad(\text{或逐不可约分量})$$
与 $\dim\mathscr R$ 比较**不够**（这正是我上一轮失败的原因）。

### 4. **新结果：$\omega=1$ 的精确判据**（专家给，极干净）

$\omega=1$ 时 $H=uv^{\mathsf T}$、$H_A=gv^{\mathsf T}$（$0\ne v$、$u,g\in\mathbb C^q$），故
$$\lambda H-H_A=(\lambda u-g)v^{\mathsf T}\ \Longrightarrow\ (5b)\iff\operatorname{rank}[u\ g]=2
\iff\boxed{\operatorname{rank}[H\ H_A]=2}.$$
* 若 $q=1$：$\omega=1$ **必不可行**；
* 若 $q\ge2$：需 $u,g$ 线性无关；若可容许约束迫使 $g\in\operatorname{span}\{u\}$，则该纤维**全坏**（正是 12 组的机制）。
* **实用诊断**：每个 $\omega=1$ 实例只需记录 $\operatorname{rank}[H\ H_A]$。

### 5. 状态表（专家给的"证明 vs 猜想"分界）

| 陈述 | 状态 |
|---|---|
| 环境拉回余维论证一般不成立 | **已证** |
| 可容许轨迹是局部闭行列式簇 | **已证** |
| 它一般**不是**有限仿射片之并 | **已证**（行列式反例）|
| 固定行空间纤维 = 仿射线性 + 开秩条件 | **已证** |
| 坏集相对可容许轨迹闭 | **已证** |
| 每个不可约分量"全坏或一般可行" | **已证** |
| 函数域 gcd 判定分量是否全坏 | **已证** |
| 12 组不可行由"可容许性塌缩"造成 | **有计算支持** |
| 塌缩是**唯一**不可行机制 | **未证；作为普适解释一般不对** |
| 可行性可由普通秩计算判定 | **猜想** |
| 多项式可判 / $\exists\mathbb R$-hard | **均未证** |
| 三个硬子族失败 ⟹ 可解 | **未证**（"未找到" $\ne$ "不可能"）|

### 6. 五阶段修订计划（专家）

1. **补完可容许轨迹几何**：用 Grassmann 关联簇 $\mathfrak I_\omega=\{(R,S):\operatorname{row}H\subseteq S,\operatorname{row}H_A\subseteq S\}$ +
   开条件；每个图卡里写出 $S$、导出方程、算纤维维数、定可达 Grassmann 子集、识别分量来源；
   目标是"用 $T$ 与 $L_0$ 描述 $\mathcal X_\omega$ 的维数与不可约分量"的定理；
2. **逐分量分类谱障碍**：对每个分量 $X_i$ 在 $\mathbb C(X_i)$ 上算 $\Delta_i=\gcd\{\text{极大子式}\}$；
   $\deg\Delta_i>0$ ⟹ 全坏；$=0$ ⟹ 一般可行；问 $\deg\Delta_i$ 能否由更简单的 $(A,C,L_0)$ 不变量表达；
3. **检验"秩-only 猜想"**：不要先当定理；问 $\Delta$ 是否由 $\operatorname{rank}(L_0N_K)$、$\operatorname{rank}(L_0AN_K)$、
   $\dim(K\cap AK)$、可达行空间族的维数等控制；
4. **选择性恢复硬度搜索**：只在找到"真正灵活"的族后做二次编码；目标族需：可容许轨迹正维、
   降阶铅笔非平凡变化、无自动的秩一/方阵障碍、谱条件的系数能编码独立变量、且能由原观测器数据实现；
5. **形式化与论文写作**。

## 自查：维数上界 "$\dim(\text{坏})<mk$" 的尝试**失败**（并找出原因）

**尝试**：把坏集写成 $\phi^{-1}(Z)$，其中 $\phi:R\mapsto\lambda H(R)-H_A(R)$ 线性、$Z=\{M:\operatorname{rank}M<\omega\}$。
用"线性拉回不降余维"：
$$\operatorname{codim}\bigl(\phi^{-1}(Z)\bigr)\ \ge\ \operatorname{codim}Z=(q-\omega+1)(k-\omega+1),$$
于是 $\dim(\text{坏})\le\dim\mathscr R-(q-\omega+1)(k-\omega+1)$；若 $q>\omega$ 且 $k\ge\omega$ 则右边 $<\dim\mathscr R$
⟹ 坏集真包含 ⟹ **可行**。若该论证成立，$q1$ 将平凡地答"假"（$q>\omega$ 时总可行）。

**它错了**——反例就是本项目**第一批 12 组数据**：
$k=q=2$、$r=1$、$\omega=1<q$（故 $q>\omega$ 满足）且 $(q-\omega+1)(k-\omega+1)=4$，
按上述论证应**可行**；但实测（Stage 2，精确符号计算）为**全部不可行**（$(5a)$ 迫使 $r_2=0$，此时非不变行列式恒零）。

**错在哪**：$\phi^{-1}(Z)$ 的余维界是关于**整个可达线性空间** $\mathscr R$ 的，而可行集只在
"**$(5a)$ 成立的子集**"上定义。$(5a)=\ker H\subseteq\ker H_A$ 是**额外**的条件，它可能把 $\mathscr R$ 切得很小
（例中切成 $r_2=0$ 的超平面），坏集可以在**那个小集合**上填满——与"在 $\mathscr R$ 里是否真包含"无关。

**教训（已记）**：凡"维数计数 ⟹ 存在性"的论证，必须核对**计数所在的空间是否就是可行集所在的空间**；
$(5a)$ 是硬约束，不能默认自动满足。（这与 §10.2 "维数计数只给单向结论"的旧教训同型。）

**修正后的问题（仍未解决）**：
$$\dim\bigl(\text{坏}\cap\{(5a)\text{ 成立}\}\bigr)\ <\ \dim\{(5a)\text{ 成立}\}\ ?$$
即必须在**可容许子集**上做维数计数，而不是在 $\mathscr R$ 上。

## Stage 2 的一般性观察：可达集**永远至少占一半** ⟹ 可行从不"稀薄"

由专家核验的维数公式（第十三轮）：
$$\dim\operatorname{im}\Theta=m\bigl(2k-\dim(K\cap A^{-1}K)\bigr)=m(2k-\dim\ker T),$$
而 $\ker T\cong\{w\in K:Aw\in K\}\subseteq K$ ⟹ $\dim\ker T\le k$。故
$$\boxed{\dim\operatorname{im}\Theta\ \ge\ mk\ =\ \tfrac12\,(2mk)}$$
即**可达集在任何区域都至少占满空间的一半维数**（自由区域 $\dim\ker T=0$ 时为全体）。

结合闭性定理的二分，得到一条**与"是否硬"直接相关的结构事实**：

> **可行集要么空、要么在可达集里开稠密；而可达集本身维数 $\ge$ 全空间的一半。**

**推论（为什么"稀薄型难度"不可能）**
* 若某实例可行，则**随机取一个可达点就以高概率可行**（开稠密 + 维数 $\ge$ 半）；
* 故"找可行点"不是稀薄搜索——**这与 NP-hard 归约通常需要的"稀薄可行集"相反**；
* 于是 $q1$ 若要 hard，必须来自"**判坏集是否填满可达集**"这一**理想论**问题，
  而不是"在巨大空间里找一个可行点"。

**这与三次探针的结论一致**：
| 探针 | 结果 |
|---|---|
| 自由区域（$\dim\ker T=0）$ | 可达集 = 全体 ⟹ 平凡可行 |
| 最小约束区域（$\dim\ker T=k=2$）| 约束是线性同构 ⟹ 刚性、易判 |
| 一般情形 | 可达集维数 $\ge$ 半 ⟹ 可行不稀薄 |

**下一步（若继续）**：只需回答一个问题——**"坏集能否填满一个维数 $\ge$ 半的线性空间？"**
若能（需具体例子），hardness 仍有空间；若在结构上不可能（例如坏集维数总有上界 $<mk$），
则 $q1$ 的答案为"不 hard"。

**状态**：Stage 2 **未找到硬子族**；三次尝试（自由/最小约束/维数下界）都指向"可行不稀薄"。

## Stage 2 探针 #1：最小**约束区域**实例是**刚性的、且容易**

**实例**：$n=4,p=1,q=2,r=1$（$n-p=3<2k=4$ ⟹ 约束区域）；$C=e_1^{\mathsf T}$；$A$ 的第一行 $e_4^{\mathsf T}$（故 $CA=e_4^{\mathsf T}$、
$K=\langle e_2,e_3\rangle$），$A$ 在 $K$ 上是**交换** $e_2\leftrightarrow e_3$（故 $AK=K$、$K\cap AK=K\ne0$）。

**机器核对**（`tools/verification/stage2_constrained_probe.py`）：
* $CA=e_4^{\mathsf T}$ ✓、$\dim K=2$ ✓、$Ae_2=e_3$、$Ae_3=e_2$ ✓；
* **$H_A=H\cdot P$ 对每个试过的 $R$ 都成立**（$P$ 为交换矩阵）——即兼容约束退化为
  $$\boxed{B_2=B_1P}$$
  一个**线性同构**，不是真约束。

**结构后果**：$\lambda H-H_A=H(\lambda I-P)$。$P$ 的特征值是 $\pm1$，故秩降只可能发生在 $\lambda=\pm1$：
* $\lambda=1$：$\ker(I-P)=\langle(1,1)\rangle$ ⟹ 秩降 $\iff H(1,1)^{\mathsf T}=0$；
* $\lambda=-1$：$\ker(-I-P)=\langle(1,-1)\rangle$ ⟹ 秩降 $\iff H(1,-1)^{\mathsf T}=0$。
于是可行 ⟺ 能选 $(r_2,r_3)$ **避开**这两条线性条件——**再次是"线性条件 + 开条件"**，容易判定。

### 结论（诚实）

* **最小约束实例没有编码能力**：约束是线性同构，铅笔被刚性绑定为 $H(\lambda I-P)$，难度与自由区域同量级；
* ⟹ **硬度（若存在）需要更大的 $k$**，使 $B_1Z_1+B_2Z_2=0$ 留下**真正的自由度**（$\dim\ker T$ 介于 $0$ 与 $k$ 之间）；
* 下一探针应取 $\dim\ker T$ 严格介于两者之间的最小例子（例如 $k=3$、$\dim\ker T=1$）。

**状态**：Stage 2 第一探针**完成**，结果为**负**（该子族容易），且指出了下一探针的判据（$\dim\ker T$ 中间值）。

## Stage 1（专家四阶段计划的第一步）：可达系数对的刻画与"两个区域"

### 1. 精确刻画（= Prop 2，专家已核验）

$M=\begin{bmatrix}L_0\\R\end{bmatrix}$ 时，可达到的**下块对** $(B_1,B_2)=(RN_K,RAN_K)$ 恰为
$$\operatorname{im}\Theta=\bigl\{(B_1,B_2):\ B_1v+B_2w=0\ \ \forall(v,w)\in\ker T\bigr\},\qquad T(v,w)=v+Aw,$$
且 $\ker T\cong\{w\in K:Aw\in K\}$、$\dim\ker T=\dim(K\cap A^{-1}K)$。
等价地：取 $\ker T$ 的基 $Z=\begin{bmatrix}Z_1\\Z_2\end{bmatrix}$（$Z_i$ 为 $k\times d$、$d=\dim\ker T$），则
$$\boxed{B_1Z_1+B_2Z_2=0}$$
即可达集是**线性子空间**，余维 $m\dim(K\cap A^{-1}K)$（$m=q-r$）。顶部块 $(L_0N_K,\ L_0AN_K)$ 由 $L_0$ 固定。

### 2. 由此得到**两个区域**（这是本轮的结构性结论）

**自由区域**：$\ker T=0$ ⟺ $\ker(A|_K)=0$ 且 $K\cap AK=0$（需 $n\ge2k$，第九/十三轮）。
此时**每个**下块对都可实现，即观测器能"任意摆布"铅笔 $P=\lambda H-H_A$（除固定的顶部块）。

**约束区域**：$\ker T\ne0$（例如 $n-p<2k$）⟹ 下块对受**线性约束** $B_1Z_1+B_2Z_2=0$。

### 3. 为什么这个二分对硬度归约是决定性的

* 在**自由区域**，谱条件是"**开**条件"（无有限秩降是开集），而可达集是整个空间 ⟹
  可行性几乎自动成立（等价于"是否存在一个无秩降的铅笔"，这在自由度大时总是成立）⟹ **难以承载硬度**。
  这与路线 2 的失败经验一致：自由度越大，"存在好点"越平凡。
* 在**约束区域**，线性约束 $B_1Z_1+B_2Z_2=0$ 与"开条件"相互作用：约束可能迫使所有可达铅笔都掉秩 ⟹
  **不可行**；而判断"约束是否把可行点杀光"正是**理想论/消元**问题（闭性定理之后的那一层）。
  ⟹ **硬度若有，只能来自约束区域**。

### 4. 于是 Stage 2 的目标被精确指认

> 在**约束区域**（$\ker T\ne0$，特别 $n-p<2k$）里，找一族 $(A,C,L_0)$ 使
> "$\exists R$ 可行"等价于一个已知难问题（如某个二次可行性 / 双线性等式可行性）。

**注意**：约束区域的约束是**线性**的（$B_1Z_1+B_2Z_2=0$），这是可以精确编码到源实例里的
——这正是 Stage 3（编码二次约束）的入口：把源问题的变量放进 $B_1,B_2$ 的自由部分，把约束放进 $Z_1,Z_2$。

### 5. 状态

Stage 1 **完成**（刻画是他核验过的 Prop 2，二分为本轮新论）；
Stage 2 目标已指认（约束区域 + 最小硬子族）；
Stage 3/4 未开始。

## **撤回**：坏集**不**是"单参数仿射子空间族的并"（专家第十七轮）

我上一节的路线 2 试探建立在一个错的前提上：

**错在哪**：$P(R,\lambda)$ 的条目对 $R$ 仿射，但一个 $\omega\times\omega$ **行列式是 $\omega$ 个条目之积的和** ⟹
$p_i(R,\lambda)$ 对 $R$ 的次数是 $\le\omega$，**不是** 1。专家的反例：$\det\begin{pmatrix}x&y\\ z&w\end{pmatrix}=xw-yz$ 对设计变量**二次**。
故 $p_i=0$ 在 $R$ 中定义的是**代数簇**，不是仿射子空间；$L(\lambda)R=b(\lambda)$ 的写法**没有导出**。

**第二处错**：$\lambda\in\mathbb C$ 是**复**参数（实维 2），我把它当单参数实变量，故 "+1" 的维数界不成立。

**仍然有效的部分**（专家确认）
* 固定 $R$：一元行列式 gcd 精确可判 ✓
* 变 $R$：**关联集**（incidence）与投影是对的，但方程对 $R$ **是多项式的** ⟹ 正确几何是
  **参数化行列式簇及其投影**，不是仿射子空间并；
* 射影紧化 $[\alpha:\beta]\in\mathbb P^1$ 有用，且 $[1:0]$ 处由 $\operatorname{rank}H=\omega$ 排除 ✓

### 正确的几何对象（专家给的）

$$\mathcal I_\omega=\bigl\{(R,[\alpha:\beta])\in\mathbb R^N\times\mathbb P^1:\ \operatorname{rank}(\alpha H(R)-\beta H_A(R))<\omega\bigr\}$$
投影闭（闭性定理）；它才是"generic feasibility / 例外参数层 / 实点"的正确载体。

### 专家建议的**修正研究计划**

1. **改正标准表述**（Part I 保留：它是 $\exists\mathbb R$ 的合法上界，由二次证书给出，**不**由几何给出）；
2. **主张量改为"$\exists\mathbb R$-硬度的归约"**，但**不**从一般 BMI 出发（Toker–Özbay 是不等式，我们更受限）；
   四阶段：
   * **Stage 1**：精确刻画**可达系数对** $(H,H_A)$（二者共享 $R$，**不能**当独立）；
   * **Stage 2**：找**最小硬子族**（小 $\omega$、简单 $K$、特殊 $A,C,L_0$）；
   * **Stage 3**：用 $U,V,G$ 与左逆恒等式**编码二次约束**（难点在"通过共享 $R$ 强制代数关系"）；
   * **Stage 4**：证多项式多一归约（四条都要：源实例 ⟹ 有理观测器数据、解对应、规模与位长多项式）；
3. **保留一个小型结构几何工作流**（围绕 $\mathcal I_\omega$），但不当作算法。

### 专家给的文献组织（三主题）

* **A 最小阶函数观测器理论**：Fernando–Trinh–Jennings (2010)；Fernando–Trinh (2013, 2014)；
  Darouach–Fernando (2020, 2023, 2025)；**Fernando (2026) 两篇预印本**（阶谱与中间阶）
  —— 特别提醒：**先核对定义与定理陈述再声称新颖性**；
* **B 实代数几何与判定**：实量词消去/$\exists\mathbb R$、行列式簇与关联簇、消元理想与射影投影、
  复簇的实点、Smith 形与行列式因子；
* **C 非凸控制综合**：Toker–Özbay 与静态输出反馈文献——**只作动机，不作硬度证明**
  （我们不是标准 SOF-BMI，而是带矩阵铅笔证书的**结构多项式等式可行性**）。

**论文比较表（专家建议七列）**：观测器类 · 阶参数 · 代数条件 · 谱条件 · 增广方式 · 计算（构造/判定/存在性）· 复杂度。
最后一列特别重要：**"存在性充要条件"不等于"判定复杂度"**。

## （以下为路线 2 的试探，前提已被上节撤回）
## 路线 2 的试探（部分进展）：把"坏"写成**λ-族的仿射子空间**，并给一个多项式时间充分条件

### 1. 结构性观察：对固定 λ，坏条件对 $R$ 是**线性**的

$p_i(R,\lambda)$（$\omega$ 阶子式）对 $R$ **仿射**、对 $\lambda$ 次数 $\le\omega$。故"全部 $p_i(R,\lambda)=0$"是
$$L(\lambda)\,R=b(\lambda)$$
形式的**线性**系统（未知量 $R$，系数为 $\lambda$ 的多项式）。于是
$$\text{bad}(R)\iff\exists\lambda:\ L(\lambda)R=b(\lambda),\qquad
\text{bad}=\bigcup_{\lambda\in\mathbb C}A(\lambda),\quad A(\lambda):=\{R:\ L(\lambda)R=b(\lambda)\}$$
每个 $A(\lambda)$ 是**仿射子空间**。

### 2. 关键：一族（1 参数）仿射子空间的并，维数至多 "+1"

$$\dim\ \bigcup_{\lambda}A(\lambda)\ \le\ \max_{\lambda}\dim A(\lambda)\ +\ 1
\qquad(\dim\varnothing:=-\infty)$$
（$\lambda$ 只在 1 维里跑。）记 $N=(q-r)n$ 为 $R$ 的维数。

### 3. 由此得到**多项式时间的充分条件**

$$\boxed{\max_{\lambda}\dim A(\lambda)\ \le\ N-2\ \Longrightarrow\ \text{bad}\ne\mathbb R^N\ \Longrightarrow\ \exists R\ \text{可行}}$$
且此时可行集是**非空开稠密**（与闭性定理一致）。

**可计算性**：$\max_\lambda\dim A(\lambda)=N-\min\{\operatorname{rank}L(\lambda):A(\lambda)\ne\varnothing\}$；
而"$\min_\lambda\operatorname{rank}L(\lambda)$ 是否 $\le$ 某值"等价于"某族子式有公共根"，即**一元 gcd 测试** ⟹ **多项式时间** ✓

### 4. 剩余情形（本路线未解决）

$\max_\lambda\dim A(\lambda)\in\{N-1,N\}$——即坏集**几乎**填满或填满 $R$-空间。此时"+1"的界不足以判定，
需要更细的信息（该族是否真的覆盖、以及覆盖的维数）。**这正是本路线卡住的地方**：
* 若 $\max\dim A(\lambda)=N$：某 λ 使整个 R-空间都坏 ⟹ **不可行**（可直接判定 ✓）
* 若 $=N-1$：坏集是余维 1 的并，可能覆盖也可能不覆盖 ⟹ **未解决**

### 5. 意义

* 给出一个**多项式时间可判的充分条件**（第 3 条），并且它是"绝大多数"情形（余维 $\ge2$ 时必然可行）；
* 把问题**精确定位**到"$\max\dim A(\lambda)=N-1$ 的临界层"——比原来的"图卡覆盖"更窄、更可算；
* 与左逆证书的关系：$L(\lambda)R=b(\lambda)$ 的秩比较就是 (B') 的系数方程的秩比较，两种写法一致。

### 6. 状态（诚实）

**部分进展，未成算法**。缺口只在 $\max\dim A(\lambda)=N-1$ 的临界情形；
若能在该情形判定"覆盖与否"，路线 2（$\mathbf P$ 算法）即成立；若该情形本质上就是难的，则它是 $q1$ 的硬度来源。

## 形状定位与文献匹配（2026-11-07）

REAL-AUG$_\omega$ 的 (A)+(B') 是**双线性等式组**：
$$H(R)=UV,\quad H_A(R)=GV,\quad JU=I_\omega,\quad VZ=I_\omega,\quad X_jU-X_{j-1}G=0\ (j)\quad X_{2\omega-2}U=0 .$$
每一项都**恰好双线性**（两个未知量之积，无三次项）⟹ 它是 **BMI 型等式可行性**的一个特例。

**已知的两端**
* **线性**等式可行 $\in\mathbf P$（LP）；
* **BMI 可行性** $\mathbf{NP}$-hard（**Toker–Özbay 1995**，ACC'95）；
* **QES**（一般二次）$\exists\mathbb R$-完全（BSS 1998；Schaefer–Cardinal–Miltzow 汇编 arXiv:2407.18006）。

**由此 $q1$ 的两条可能路线**
1. **硬度**：把一般 BMI 可行性（或某个 $\mathbf{NP}$-hard 的双线性等式族）**编码进 REAL-AUG** ⟹
   $q1$ hard（甚至 $\exists\mathbb R$-hard ⟹ $\mathbf{NP}\subseteq\exists\mathbb R$，更强）；
2. **算法**：利用 REAL-AUG 的**特殊结构**（$H,H_A$ 共享 $\mathcal L(R)$、$X$ 的最高次约束 $X_{2\omega-2}U=0$、
   $U$ 满列秩由 $JU=I$ 强制）给出多项式判定 ⟹ $q1$ 假。

**判断**：REAL-AUG 比一般 BMI **更受限**（共享 $\mathcal L$、$U$ 列满秩、$X$ 的阶梯结构），
故（1）需要精心的编码，（2）有机会。这正是下一步要试的。

## 专家第十六轮：(B) 是**三次**不是二次 —— 改用降阶铅笔的 (B')

### 1. 更正：(B) 的次数

$PYP=P$ 中 $P$ 对 $R$ **仿射**、$Y$ 对自身系数**线性** ⟹ 系数方程含 $R_iR_j(Y_\ell)_{ab}$ ⟹ **三次**。
（标量例：$(\lambda h-a)y(\lambda h-a)$ 对 $h$ 二次、对 $y$ 线性 ⟹ 总次数 3。）
故我写的"次数 $\le2$"**错**。

### 2. 修复：换成降阶铅笔的左逆证书 (B')

由 (A)：$P=(\lambda U-G)V$、$V$ 满行秩 ⟹ $\operatorname{rank}P(\lambda)=\operatorname{rank}(\lambda U-G)$。令
$$S(\lambda):=\lambda U-G\in\mathbb R[\lambda]^{q\times\omega},\qquad
\text{(B}'\text{)}\quad X(\lambda)S(\lambda)=I_\omega,\quad \deg X\le2\omega-2,\quad X_j\in\mathbb R^{\omega\times q}.$$
$S$ 对 $(U,G)$ **仿射**、$X$ 对自身系数**线性** ⟹ **(B') 对联合变量双线性，次数 $\le2$** ✓

### 3. 更正后的定理（专家给的定稿形态）

**Theorem（无图卡二次证书）** 固定 $\omega\ge1$，以下等价：
1. $\exists$ 实 $R$ 使 $(5a)$、$(5b)$、$\operatorname{rank}H(R)=\omega$；
2. $\exists$ 实 $R,U,V,G,J,Z$ 与实多项式矩阵 $X=\sum_{j<2\omega-1}X_j\lambda^j$ 使
   $$H(R)=UV,\quad H_A(R)=GV,\quad JU=I_\omega,\quad VZ=I_\omega,\quad X(\lambda)(\lambda U-G)=I_\omega .$$

*证明*（专家）：(⇒) 用第十六轮 Q1 的因子化 + 降阶判据 + 多项式左逆定理；
(⇐) $JU=I$、$VZ=I$ 给两条满秩 ⟹ $\operatorname{rank}H=\omega$；$Hx=0\Rightarrow Vx=0\Rightarrow H_Ax=0$ ⟹ $(5a)$；
(B') ⟹ $\operatorname{rank}(\lambda U-G)=\omega$ 且 $V$ 满射 ⟹ $\operatorname{rank}P(\lambda)=\omega$ ⟹ $(5b)$ ✓

### 4. 三个确认（专家）

* **Q1**：$H_A=G_0H$ 的因子化与 $G=G_0U$ ✓（他建议记法上 $G_0$ 只用于证明、$G$ 留给 (A) 的未知量）；
* **Q2**：法秩 $\omega$ **由 (A) 单独推出**（取 $\det U_{I,:}\ne0$ 的那个 $\omega$ 阶子式，$\det(\lambda U_{I,:}-G_{I,:})$ 是 $\omega$ 次非零多项式 ⟹ 有实根 ⟹ 该 $\lambda$ 处满列秩），**不需 (B)** ✓；
* **Q3**：**实 gcd 步正确**——共同根 $\alpha$ 若实取 $\lambda-\alpha$，若非实取 $(\lambda-\alpha)(\lambda-\bar\alpha)$，都是**实**非定常公因子 ⟹
  $\gcd_{\mathbb C}\in\mathbb C^\times\iff\gcd_{\mathbb R}\in\mathbb R^\times$ ✓（关键是"公共根"而非"某个子式的根"）

### 5. 决策问题的正式命名（专家建议）

$$\mathrm{REAL\text{-}AUG}(q):\ \exists R\in\mathbb R^{(q-r)\times n}\ \text{使}\ (5a)\wedge(5b);\qquad
\mathrm{REAL\text{-}AUG}_\omega(q):\ \text{同上并}\ \operatorname{rank}H(R)=\omega,$$
$$\mathrm{REAL\text{-}AUG}(q)\iff\bigvee_{\omega=0}^{\min(q,k)}\mathrm{REAL\text{-}AUG}_\omega(q),$$
$\omega=0$ 单独陈述。**固定 $\omega$ 的每个分支都是多项式规模的二次方程组** ⟹ $q1$ 的复杂度 = 这个析取的判定复杂度。

## 中心定理（无图卡、实系数）的证明：$\exists R\iff$(A)+(B) 有实解

**设定**：$A,C,L_0$ 实；$R\in\mathbb R^{(q-r)\times n}$；$H=\mathcal L(R)N_K$、$H_A=\mathcal LA(R)N_K$；
固定 $\omega\in\{1,\dots,\min(q,k)\}$；$P(\lambda)=\lambda H-H_A$。

**系统 (A)+(B)**
$$\text{(A)}\ \ H(R)=UV,\quad H_A(R)=GV,\quad JU=I_\omega,\quad VZ=I_\omega,
\qquad
\text{(B)}\ \ P(\lambda)Y(\lambda)P(\lambda)=P(\lambda),\ \deg Y\le2\omega-2,$$
未知量 $U\in\mathbb R^{q\times\omega}$、$V\in\mathbb R^{\omega\times k}$、$G\in\mathbb R^{q\times\omega}$、
$J\in\mathbb R^{\omega\times q}$、$Z\in\mathbb R^{k\times\omega}$、$Y_j\in\mathbb R^{k\times q}$（$j<2\omega-1$），以及 $R$。

**定理** $\omega\ge1$ 时：
$$\exists R\in\mathbb R^{(q-r)\times n}\ \text{使}\ (5a)\wedge(5b)\wedge\operatorname{rank}H(R)=\omega
\quad\iff\quad\text{(A)+(B) 有实解}.$$

### 证明

**(⇒)** 取这样的 $R$。由 $(5a)\iff\ker H\subseteq\ker H_A$，$H_A$ 分解为 $H_A=G_0H$；
又 $\operatorname{rank}H=\omega$，取因子化 $H=UV$（$U$ 满列秩、$V$ 满行秩，例如用列图卡 $V_{[:,S]}=I_\omega$）⟹
$H_A=GV$（$G:=G_0U$）✓。$U$ 满列秩 ⟹ $\exists J$：$JU=I_\omega$；$V$ 满行秩 ⟹ $\exists Z$：$VZ=I_\omega$ ✓。
$(5b)$ + L7 ⟹ $P$ 的 $\omega$ 阶子式 gcd 为**非零实常数**（实系数即可，因非实根成对出现 ⟹ 实二次因子整除全部子式）⟹
由广义逆/左逆定理（对因子 $P_1$ 用）$\exists Y$ 使 $PYP=P$，且**可选取 $\deg Y\le2\omega-2$**
（$Y=\sum_I u_I\operatorname{adj}(P_I)E_I$，$\deg u_I\le\omega-1$、$\deg\operatorname{adj}\le\omega-1$）。全部数据都是实的 ✓

**(⇐)** 取 (A)+(B) 的实解。
1. **秩**：$JU=I_\omega$ ⟹ $U$ 单射；$VZ=I_\omega$ ⟹ $V$ 满射。故 $\operatorname{rank}H=\operatorname{rank}(UV)=\omega$
   （$\le\min=\omega$，且 $UVZ=U$ ⟹ $\ge\operatorname{rank}U=\omega$）✓
2. **$(5a)$**：$x\in\ker H$ ⟹ $UVx=0$ ⟹ $Vx\in\ker U=0$ ⟹ $H_Ax=GVx=0$ ⟹ $\ker H\subseteq\ker H_A$ ✓（再用恒等式）
3. **法秩**：$P=(\lambda U-G)V$，$V$ 满射 ⟹ $\operatorname{rank}P(\lambda)\le\omega$；取 $\lambda$ 使 $\lambda U-G$ 满列秩
   （在 $\mathbb R$ 上稠密）⟹ $\operatorname{nrank}P=\omega$ ✓
4. **无有限秩降**：由 (B)（$PYP=P$ 为多项式恒等式）与 $\operatorname{nrank}P=\omega$，套**广义逆定理**得
   $\gcd\{\omega\text{ 阶子式}\}\in F^\times$ ⟹ 由 **L7** 得 $(5b)$ ✓

$$\square$$

### 这条定理做了什么

* "$(5a)$" ⟸ (A) 的两条满秩条件（**不需要**图卡）；
* "$\operatorname{rank}H=\omega$" ⟸ 同两条；
* "$(5b)$" ⟸ (B)（广义逆证书）；
* **全部变量实、方程多项式次数 $\le2$（对 $(R,U,V,G,J,Z,Y)$ 联合双线性/线性）**，规模 $(2\omega-1)\omega q+O(\omega^2+qr)$ ✓

**未解决的（仍是）**：(A)+(B) 的**判定复杂度**；$\omega$ 遍历 $\{0..k\}$ 时的**层数**（$k+1$，多项式 ✓，
这一点本轮澄清：层本身不是问题，问题在图卡/分量——而 (A)+(B) 已无图卡）；
实点稠密在 (A)+(B) 表述下**不再需要**（因为 (A)+(B) 本身就是实方程组）✓ —— 这是相对 Stage 3.5 的一个实质简化。

## 专家第十五轮：**广义逆证书** —— 图卡覆盖可从**存在性表述**中完全去掉

### 1. 核心：广义逆恒等式（专家给的，比我的 $P_1R$ 好）

$$\boxed{P(\lambda)\,Y(\lambda)\,P(\lambda)=P(\lambda),\qquad \deg Y\le2\omega-2}$$
（$P=\lambda H-H_A$，$Y\in F[\lambda]^{k\times q}$）。在正确的法秩假设下，此式**等价于**"无有限秩降"，
且**不需要选列图卡、不需要枚举极大子式**。

**我的 $P_1R$ 提法不够**（专家指出）：$P=P_1R$ 还需 $R$ **处处满行秩**，否则不保证 $\operatorname{rank}P=\omega$；
广义逆没有这个问题。

### 2. 三处更正

1. **不是"线性"而是"双线性"**：$X_jU$、$X_jG$ 是关于**联合变量** $(R,X)$ 的双线性表达式 ⟹
   证书方程在 $(R,X)$ 上**次数 $\le2$**，但**仍多项式规模**（未知量 $(2\omega-1)\omega q$）；
2. **次数界 ≠ 几何次数**：$\deg_\lambda$ 或证书的次数界**不能**直接当作坏集的**几何次数**界，需另证；
3. $P_1R$ 需补 $R$ 满行秩（见上）。

### 3. 可选的**无图卡**拆分（专家确认正确，但第二项建议用广义逆）

$$(5b)\iff\bigl[\text{全部 }(\omega+1)\text{ 阶子式恒零}\bigr]\wedge\bigl[\omega\text{ 阶子式无公共有限根}\bigr]$$
* 在他的问题里**第一项自动成立**（由 $(5a)$ 与 $\operatorname{rank}H=\omega$，因 $P=(\lambda U-G)V$ 内维 $\omega$）；
* 一般 $P$ 时第一项非冗余（法秩可能 $<\omega$，此时"零族的 gcd"是 $0$ 而非单位元）。
* **推荐的可判定形式**：$\operatorname{nrank}P=\omega\ \wedge\ PYP=P$（后者用广义逆）✓

### 4. **实/复**：全程可在 $\mathbb R$ 上做

对**实**多项式矩阵 $P$，以下等价：① $P(\lambda)$ 对一切 $\lambda\in\mathbb C$ 秩 $\omega$；
② 极大子式无公共**复**根；③ 它们在 $\mathbb R[\lambda]$ 中的 gcd 为非零常数；④ $\exists Y\in\mathbb R[\lambda]^{k\times q}$ 使 $PYP=P$。
（②⟹③ 用"非实公共根成对出现，对应实二次不可约因子整除所有子式"。）
⟹ **实综合问题可全程用实系数**，即使谱参数取复——这对 $\exists\mathbb R$ 上界讨论很重要。

### 5. 专家建议的**中心定理**（下一阶段的目标）

固定 $q$ 与 $\omega$，引入存在量 $U\in\mathbb R^{q\times\omega}$、$V\in\mathbb R^{\omega\times k}$、$G\in\mathbb R^{q\times\omega}$、
$J\in\mathbb R^{\omega\times q}$、$Z\in\mathbb R^{k\times\omega}$，施加
$$\text{(A)}\quad H(R)=UV,\quad H_A(R)=GV,\quad JU=I_\omega,\quad VZ=I_\omega$$
（编码 $\operatorname{rank}H=\omega$ 与 $\ker H\subseteq\ker H_A$），再令
$$Y(\lambda)=\sum_{j=0}^{2\omega-2}Y_j\lambda^j,\qquad\text{(B)}\quad
\bigl(\lambda H(R)-H_A(R)\bigr)Y(\lambda)\bigl(\lambda H(R)-H_A(R)\bigr)=\lambda H(R)-H_A(R).$$
**定理（待证/待核）**：$\omega>0$ 时，存在实 $R$ 满足 $(5a),(5b)$ 与秩条件 $\iff$ (A)+(B) 有实解。

**意义**：这把"$\exists$ 图卡 + $\exists$ 分量"从**存在性表述**里彻底去掉；图卡/分量/实点稠密只留给
"几何分析"（generic feasibility、坏集几何、不可约分量、实点密度）。

### 6. 仍未解决的（专家明确）

* 秩 $\omega$ 层的**不可约性**未证；不同不可约分量可能需要不同图卡；
* **图卡数的多项式界**没有依据（他明确建议**不要**把它当作复杂度表述的前提）；
* **多项式时间判定**未建立；
* 实点稠密仍未解决。

## 用左逆证书重做编码（规模与次数都变小）

### 1. 证书系统（$X$ 的次数界 $2\omega-2$）

$$X(\lambda)=\sum_{j=0}^{2\omega-2}X_j\lambda^j,\qquad X(\lambda)(\lambda U-G)=I_\omega .$$
匹配 $\lambda^0,\dots,\lambda^{2\omega-1}$ 的系数得 $2\omega$ 个**矩阵**方程
$$-X_0G=I_\omega,\qquad X_{j-1}U-X_jG=0\ (1\le j\le2\omega-2),\qquad X_{2\omega-2}U=0 .$$
未知量：$(2\omega-1)\omega q$ 个标量；这些都是 $(U,G)$ 的**双线性**表达式。

### 2. 一处我差点写错的自查（重要）

我一度"推出"：由 $X_{2\omega-2}U=0$ 与 $U$ 满列秩得 $X_{2\omega-2}=0$，再归纳得 $X=0$，
与 $-X_0G=I_\omega$ 矛盾——**这个归纳是错的**：
$$X_jU=0\ \text{只说明 }X_j\ \text{在}\ \operatorname{im}U\ \text{上为零，不说明 }X_j=0$$
（$U$ 只是列满秩，不是可逆方阵）。反例：$P=\binom{\lambda}{-1}$（$q=2,\omega=1$）、$X=(0,-1)$ 为常数，
$XU=0$ 而 $XG=-1$，证书成立 ✓。**已记下，避免写进文档。**

### 3. 规模与次数（对比旧编码）

| 项 | 子式 + Bézout（旧） | **左逆证书（新）** |
|---|---|---|
| 未知量 | $N\omega$，$N=\binom{q}{\omega}$ | $(2\omega-1)\omega q$ —— **多项式** |
| 方程 | $2\omega$ 标量 | $2\omega$ **矩阵**（$=\omega q$ 标量级/条） |
| 系数对 $R$ 的依赖性 | $p_i$ 的 $\lambda$-系数，次数 $\omega$ | $U,G$ 的条目，**次数 1** |
| 坏集的次数界 | $\deg_R\le2\omega^2$ | $\deg_R\le\boxed{2\omega}$（子式阶 $\le2\omega$、条目次数 1） |

**结论**：左逆证书同时把**规模**从指数降到多项式、把**次数**从 $2\omega^2$ 降到 $2\omega$。
Stage 1 / T2 / T3 中关于 $N_{\min}=\binom{m}{h}\binom{n}{h}$ 与"中间层指数"的讨论**应据此更新**：
那个瓶颈只在"逐子式 Bézout"编码下存在，在证书编码下消失。

### 4. 于是复杂度图景重写

* 可行集（每个层-图卡）= "线性系统的秩比较"成立处 ⟹ **构造集**；坏集**闭**（闭性定理照旧）；
* **$\mathscr C$ 是线性空间**（Prop 2）⟹ **均匀采样容易**（此前"采样器未构造"的障碍消失一半）；
* 剩下的障碍只有两条：
  1. **图卡与分量的覆盖**（$\sum_\omega\binom{k}{\omega}$ 个字图卡；不可约分量的分解）；
  2. **实点**（实版本需实点稠密，Stage 3.5 的判据）；
* 因此"单侧随机判定"现在有了**多项式规模证书 + 线性相容空间 + 低次（$2\omega$）**三重支撑；
  但**仍不**等于 $\mathrm{DEC}\in\mathrm{RP}$——因为第 1 条（覆盖）没有多项式界、第 2 条未解决。

## 专家第十四轮：左逆证书（**把子式枚举换成多项式规模编码**）+ 三处更正

### 1. **主要收获：多项式左逆定理**

**定理（多项式左逆）** 设 $P(\lambda)\in F[\lambda]^{q\times\omega}$、$q\ge\omega$、满列法秩。则
$$\gcd\{\text{全部 }\omega\text{ 阶子式 of }P\}\in F^\times
\iff\exists X(\lambda)\in F[\lambda]^{\omega\times q}:\ X(\lambda)P(\lambda)=I_\omega .$$

*证明*（专家给）
* (⇐) Cauchy–Binet：$XP=I_\omega$ 的每个条目是**极大子式的多项式组合** ⟹ 子式生成单位理想 ✓
* (⇒) 由有界次数 Bézout：$\sum_I u_Ip_I=1$、$\deg u_I\le\omega-1$；令 $P_I=E_IP$（方阵），则
  $\operatorname{adj}(P_I)E_IP=\det(P_I)I_\omega=p_II_\omega$，故
  $$X(\lambda):=\sum_I u_I(\lambda)\operatorname{adj}(P_I(\lambda))E_I
  \quad\text{满足}\quad X(\lambda)P(\lambda)=I_\omega,\qquad \boxed{\deg X\le2\omega-2}$$
  （$\operatorname{adj}(P_I)$ 的条目次数 $\le\omega-1$）✓

**编码规模（关键）**：取 $X=X_0+X_1\lambda+\cdots+X_{2\omega-2}\lambda^{2\omega-2}$，未知量为
$$\boxed{(2\omega-1)\omega q\ \text{个标量}}$$
——**多项式规模**，不再需要 $\binom{q}{\omega}$ 个子式！系数比较给 $2\omega$ 个**矩阵**方程
$$-X_0G=I_\omega,\qquad X_{j-1}U-X_jG=0\ (1\le j\le2\omega-2),\qquad X_{2\omega-2}U=0 .$$

**限定（专家明确）**：左逆证书只编码"无有限谱点"这一条；$U$ 的满列秩须**另加**（引入 $J$ 使 $JU=I_\omega$）。

**意义**：这把"精确编码"的规模从 $\binom{q}{\omega}$（中间层指数）降到 $O(\omega^2q)$——
**此前被当作瓶颈的规模问题消失了**。Stage 1 与 T2/T3 的规模讨论应据此更新。

### 2. 三处更正

1. **主从关系**：**Prop 2（精确像 $\ker T\subseteq\ker B$）应为主定理**，Prop 1（满射判据）作为其推论
   （专家：$\ker T\subseteq\ker B\iff B$ 通过 $T$ 分解，商空间的泛性质）；
2. **转置笔误**：$V\in\mathbb C^{\omega\times k}$ 时归一化是 $\boxed{V_{[:,S]}=I_\omega}$，我写成 $V^{\mathsf T}_{[:,S]}=I_\omega$ 是笔误；
3. **$\omega=1$ 的陈述要拆成两个问题**：
   * **问题 A**：秩一层是否**全部**坏（多项式恒等测试）；
   * **问题 B**：是否存在**一个**好点；
   二者**不同**。若层是**显式仿射参数化**，恒等测试可化为系数比较；若层只由秩条件**隐式**给出，
   恒等测试可能要算该层的理想/坐标环——**不**自动是普通线性代数。
   专家建议的措辞：
   > "对 $\omega=1$，候选的谱验证归结为检验 $\operatorname{rank}[u\ g]=2$；对**显式参数化**的仿射族，
   > 一般可行性可由"wedge 多项式是否恒零"判定；**一般**存在性仍是实代数判定问题，除非另有结构。"
4. $\omega\ge2$：**没有**理由声称 $\omega=2$ 是复杂度阈值。

### 3. CTS：把相容关系**放进输入**（专家建议的表述）

$$\mathrm{CTS}:\quad\text{给定 } H_0,H_{A,0}\ \text{与线性相容空间}\ \mathscr C\subseteq\mathbb R^{m\times k}\times\mathbb R^{m\times k},
\quad\text{问是否存在 }(B_1,B_2)\in\mathscr C\ \text{使 }\ker H\subseteq\ker H_A\ \text{且降阶铅笔无有限秩降};$$
其中 $H=\begin{bmatrix}H_0\\B_1\end{bmatrix}$、$H_A=\begin{bmatrix}H_{A,0}\\B_2\end{bmatrix}$，
$$\mathscr C=\{(B_1,B_2):\ B_1v+B_2w=0\ \forall(v,w)\in\ker T\}\quad(\text{由 Prop 2}).$$

**两个逻辑上独立的结果**（专家强调）：
1. **归约**：由观测器数据 $(A,C,L_0)$ 算出 $K,N_K,T$、固定顶部块与 $\ker T$ 的基 ⟹ 得 $\mathscr C$（用 Prop 2）；
2. **复杂度分析**：把 $\mathscr C$ 当输入，研究由此产生的多项式约束族（**不再提** $R$、$A|_K$、延拓论证）。

**注意（专家给的 caveat）**：若允许**任意**线性子空间 $\mathscr C$，CTS 可能包含"观测器造不出来"的族；
原始问题的 $\mathscr C$ 有特殊结构 $\mathscr C=\operatorname{im}\Theta$。故"CTS 的复杂度"与"$q1$ 的复杂度"之间还需
一步：**CTS 的硬度 ⟹ $q1$ 硬度**成立；**反向不**成立（除非证明 $\mathscr C$ 可任意化）。

## 漏洞自查（全链条，2026-11-07）

按"每个命题的假设是否写全 / 有无方阵-矩形混淆 / 有无秩-子式混淆 / 计数是否正确"逐条自查。
**已发现并修正的三类错误**（都曾实际发生）：
1. **计数错**：Bézout 方程数 $2\omega-1$ → $2\omega$（第十轮）；
2. **假设漏**：可实现性漏 $\ker(A|_K)=0$（第十三轮，$A=0$ 反例）；
3. **方阵-矩形混淆**：图卡按行 → 按列；"单个行列式" → gcd；"一个子式有根 ⟹ 降秩" → 全子式 gcd（第七、八轮）。

### 逐条状态

| 命题 | 关键假设 | 状态 | 残余风险 |
|---|---|---|---|
| $(5a)\iff\ker H\subseteq\ker H_A$ | $K=\ker(C,CA)$ | ✅ Lean | 无 |
| (12) $\dim\ker Q=\dim D+\dim\ker P_K$ | $(5a)$；$D\subseteq\ker Q(\lambda)\ \forall\lambda$ | 集合层 Lean；$+d$ 纸面（秩-零化度） | 低 |
| L7（降阶判据） | $\ker H\subseteq\ker H_A$；$\mathbb C$ 代数闭 | ✅ 专家核验 | 无 |
| 闭性定理 | $H,H_A$ 对 $R$ **代数依赖**；$\operatorname{rank}H=\omega$ 恒定 | ✅ 专家核验 | 需在陈述中保留"代数依赖" |
| 消元三情形 | 图卡坐标环**局部化** | ✅（假设已写） | 局部化细节 |
| Bézout（降阶） | 固定列图卡 $S$；$U,G$ **仿射**；$M$ 条目次数 $\omega$ | ✅ 专家核验 | 无 |
| 含固定行像 | **$\ker(A|_K)=0$ 且 $K\cap AK=0$** | ⚠️ 本轮更正 | 待专家复核 |
| 精确像定理 $\ker T\subseteq\ker B$ | 无（对任意 $A,K$） | ✅ 专家给的 | 无 |
| RAZE ⟺ DEC | 含 $\omega=0$；条件 3 是**降阶**铅笔的 gcd | ✅ 专家核验 | 无 |
| 实点稠密 | 不可约分量上有**非奇异实点** | 判据 + 实例 | 一般情形未系统检查 |
| 逐层复杂度 | **输入模型未钉** | § | 高（专家要求先钉模型） |
| RP / 硬度 | — | ❌ 已撤回 | — |

### 自查中发现的两处"应当写明但尚未写明"的

1. **$\operatorname{rank}P=\operatorname{rank}P_{\rm red}$ 与 $P_{[:,S]}=P_{\rm red}$**：依赖 $V^{\mathsf T}_{[:,S]}=I_\omega$，
   而 $V$ 的存在唯一性依赖"$U$ 满列秩"与"$\operatorname{rank}H=\omega$"。**在陈述 RAZE 条件 3 时必须先固定 $S$ 并声明 $U$ 满列秩**，
   否则"gcd 判据"作用在哪个矩阵上不清楚。
2. **$\min_R\operatorname{rank}(\mathcal L|_K)=\operatorname{rank}(L_0N_K)$**（用于"$\min\omega=1$"）：需声明 $R$ 可任取
   （含 $RN_K=0$），且这只给**下界**，与实际可行集无关。

## **更正**：含固定行的像定理（我上一版的条件不够；专家第十三轮）

我写"$\operatorname{im}\Psi_{L_0}=$ 顶部块匹配族 $\iff K\cap AK=0$"——**错**。

**反例（专家给）**：$A=0$、$K\ne\{0\}$。则 $AK=\{0\}$、$K\cap AK=\{0\}$ ✓，但 $AN_K=0$ 秩为 0，
故 $B_2=RAN_K=0$ 对一切 $R$，像**不可能**是整个匹配族。

**正确条件**：设 $m=q-r$、$T:K\oplus K\to\mathbb C^n$、$T(v,w)=v+Aw$。则
$$\boxed{\operatorname{im}\Theta=\operatorname{Hom}(K,\mathbb C^m)^2\iff T\ \text{单射}\iff
\ker(A|_K)=0\ \text{且}\ K\cap AK=0}$$
*证明*：$T(v,w)=0$ ⟹ $Aw=-v\in K$；若 $A|_K$ 单射且 $K\cap AK=0$ 则 $Aw\in K\cap AK$ 迫使 $Aw=0$，
再单射给 $w=0$、$v=0$。反向：$Aw=0$（$w\in K$）⟹ $T(0,w)=0$ ⟹ $w=0$；$v=Aw\in K$ ⟹ $T(-v,w)=0$ ⟹ $v=w=0$ ✓

**更强的精确像定理（专家给）**：对**任意** $A,K$，
$$\boxed{(B_1,B_2)\in\operatorname{im}\Theta\iff \bigl[\,v+Aw=0\ \Rightarrow\ B_1v+B_2w=0\,\bigr]}$$
即 $\ker T\subseteq\ker B$（$B(v,w):=B_1v+B_2w$）。证明：若 $(B_1,B_2)=\Theta(R)$ 则 $B_1v+B_2w=R(v+Aw)$；
反之 $\ker T\subseteq\ker B$ 使 $\widetilde R(T(v,w)):=B_1v+B_2w$ 良定义，延拓到 $\mathbb C^n$ 即得 $R$ ✓

**两个量化推论**
* $\ker T=\{(v,w):v=-Aw\}\cong\{w\in K:\ Aw\in K\}$ ⟹ $\dim\ker T=\dim(K\cap A^{-1}K)$
  （注意：**不是** $\dim(K\cap AK)$——差别正是 $\ker A\cap K\ne0$ 的可能）；
* 可达到的像维数：$\boxed{\dim\operatorname{im}\Theta=m\bigl(2k-\dim(K\cap A^{-1}K)\bigr)}$

**"关系数"**：独立相容条件的个数是 $m\dim\ker T=m\dim(K\cap A^{-1}K)$，**不是** $m\dim(K\cap AK)$（专家 §5）。

**这条更正也适用于第九轮的可实现性引理**：那里写"$\Psi$ 满射 $\iff K\cap AK=0$"同样漏了 $\ker(A|_K)=0$。
本项目的区域应改为
$$\boxed{\ker(A|_K)=0\ \text{且}\ K\cap AK=0}$$
（后者需要 $n\ge2k$；前者与 $A$ 的选择有关，第九轮的显式构造 $A:e_1\mapsto e_5,e_2\mapsto e_6$ 在 $K=\langle e_1,e_2\rangle$ 上
单射 ✓，故那个构造**仍然合格**。）

### 定理 2（RAZE ⟺ DEC）：专家确认**正确**（含 $\omega=0$ 分支）

他还建议：用"选定列因子化"可把证明写得更短（$P_{[:,S]}=\lambda U-G$ 直接给出条件 3 的等价）。

### 复杂度表述：专家要求更谨慎

* $\omega=0$：$(H,H_A)$-空间里的目标是**单点**，但其在 **$R$-空间的原像不必是单点**；
* $\omega=1$：坏条件对观测器变量确实是**二次**的，但这**不**足以给出该存在性判定问题的多项式算法；
* 任何多项式时间断言都需**精确的输入模型**与**精确说明判定什么**。
⟹ 我方原计划"$\omega=0,1$ 是 P"须降级为"具体判定过程的复杂度陈述"，且需先钉输入编码。

## （以下为上一版，条件不够；已被上节更正）
## 可实现性**含固定行**的精确版本（专家第九/十轮缺口 ④ 的修复）

**引理（像 = 顶部块匹配）** 设 $M=\begin{bmatrix}L_0\\R\end{bmatrix}$、$L_0\in\mathbb C^{r\times n}$ 固定、
$R\in\mathbb C^{(q-r)\times n}$ 自由、$N_K$ 满列秩 $k$。则
$$\operatorname{im}\Psi_{L_0}
=\Bigl\{(H,H_A)\in(\mathbb C^{q\times k})^2:\ H_{1:r,:}=L_0N_K,\ \ (H_A)_{1:r,:}=L_0AN_K\Bigr\}$$
**当且仅当** $K\cap AK=0$。

*证明*
**(⇐)** 给定满足顶部块匹配的 $(H,H_A)$，把问题**逐行块分离**：
$$MN_K=H\iff\begin{cases}L_0N_K=H_{1:r,:}&(\text{已知匹配})\\ RN_K=H_{r+1:q,:}&=:B_1\end{cases}
\qquad
MAN_K=H_A\iff\begin{cases}L_0AN_K=(H_A)_{1:r,:}&(\text{已知匹配})\\ RAN_K=(H_A)_{r+1:q,:}&=:B_2\end{cases}$$
故只需解
$$\boxed{RN_K=B_1,\qquad RAN_K=B_2}$$
这是**同一个**"自由 $R$ vs 固定 $N_K,AN_K$"的问题；由可实现性引理（对 $M$ 的那条，证明只用 $N_K$、$AN_K$ 的满列秩
与 $K\cap AK=0$），它对任意 $(B_1,B_2)$ 可解 ✓
（必要维数条件 $(q-r)n\ge2(q-r)k\iff n\ge2k$，与 $K\cap AK=0$ 相容。）

**(⇒)** 若 $K\cap AK\ne0$，取 $0\ne v\in K\cap AK$；写 $v=Aw$、$w\in K$。则对任意 $R$，
$R N_K$ 在 $v$ 上的信息与 $RAN_K$ 在 $w$ 上的信息**被同一条约束联系**（$v=Aw$ ⟹ $Rv=R(Aw)=(RA)w$），
故 $(B_1,B_2)$ 不能任意选取 ⟹ 像真包含于顶部块匹配集 ✓ $\square$

### 这条修复了什么

专家第九/十轮指出："可实现性引理是**无约束** $M$ 的；观测器的首 $r$ 行固定 ⟹ 随机因子不满足顶部块 ⟹
采样器未构造。" 本引理说明：**只要 $K\cap AK=0$，固定行不带来额外障碍**——只需把采样目标限制在
"顶部块匹配"的那一族上，而这一族**恰是**像。

于是采样协议可写成：随机取 $B_1,B_2$（$(q-r)\times k$ 各一个），解 $RN_K=B_1$、$RAN_K=B_2$ 得 $R$，
（在 $K\cap AK=0$ 时必可解），再用 $(H,H_A)=(MN_K,MAN_K)$ 构造目标对 ✓

### 仍存的限定

* $K\cap AK=0$ 需要 $n\ge2k$ 且 $\ker C$ 足够大（第九轮已给显式构造与核验）；否则像是真子集，
  须把上面的线性关系显式写进采样目标；
* 本引理只给**像的刻画**，不给"覆盖所有秩层"或"多项式时间采样"——那两项仍需单独处理；
* 秩 $\omega<k$ 的层：采样目标须额外满足 $\operatorname{rank}H=\omega$（用矩形因子 $U,G$ 参数化，见第十二轮）。

## 专家第十二轮裁决：降阶铅笔 Bézout 定理**通过**，两处必改

### 1. 选定列的**正确构造**（替代我的 $J\subseteq\{1..\omega\}$，那是平凡的）

取 $S\subseteq\{1,\dots,k\}$、$|S|=\omega$，使 $U(R):=H(R)_{[:,S]}\in\mathbb C^{q\times\omega}$ 满列秩；令
$$G(R):=H_A(R)_{[:,S]} .$$
由 $\operatorname{rank}H=\omega$，每个列向量都可唯一表为 $U$ 的列的组合，故存在唯一的 $V(R)^{\mathsf T}\in\mathbb C^{\omega\times k}$ 使
$$H=UV^{\mathsf T},\qquad V^{\mathsf T}_{[:,S]}=I_\omega .$$
再由 $\ker H\subseteq\ker H_A$ 逐列推得
$$\boxed{H_A=GV^{\mathsf T}}$$
（对列 $j$：$H(e_j-E_Sv_j)=0$ ⟹ $H_A(e_j-E_Sv_j)=0$ ⟹ $H_{A[:,j]}=Gv_j$）。

**关键推论**：$V^{\mathsf T}_{[:,S]}=I_\omega$ ⟹ $P_{[:,S]}=\lambda U-G=P_{\rm red}$
——**降阶铅笔就是原铅笔的选定列**，无需 $V$ 的显式形式（$V$ 对 $R$ 只是**有理**的，不是仿射）。

### 2. $M_\omega$ 的条目是**次数 $\omega$ 的多项式**，不是线性的

我写"$M_\omega(R)$ 的条目对 $R$ 线性"——**错**：$p_i$ 的 $\lambda$-系数是 $R$ 的**$\omega$ 次**多项式。
但最终界 **$2\omega^2$ 仍正确**（$s$ 阶子式次数 $\le s\cdot\omega$，$s\le2\omega$）。

### 3. **$4\omega^2$ 不必要**，删掉

在固定归一化列图卡上，选定列因子是 $I_\omega$、$P_{\rm red}=\lambda U-G$ 的条目**仿射**，故相关界就是
$$\boxed{\deg_R\le 2\omega^2}$$
（$4\omega^2$ 只在"保留全部未降阶子式且用任意因子坐标"时才是粗糙界，本项目不用。）

### 4. 专家给的定稿形态（接受）

> 固定 $S$、$U=H_{[:,S]}$、$G=H_{A,[:,S]}$、$H=UV^{\mathsf T}$、$H_A=GV^{\mathsf T}$、$V^{\mathsf T}_{[:,S]}=I_\omega$；
> $P_{\rm red}=\lambda U-G$（$q\times\omega$，**仿射**）；$N=\binom{q}{\omega}$ 个极大子式；四条件等价；
> 坏集 $=\{\operatorname{rank}[M|b]>\operatorname{rank}M\}$（**精确**）+ 秩分层构造集；$\deg_R\le2\omega^2$；
> $\omega=0$ 单列。

### 5. 它**不**解决的事（专家明确）

* 完整参数空间可能需**多个列图卡** $S$；
* 秩 $\omega$ 的观测器轨迹可能**可约**；
* 固定行 $L_0$ 限制哪些 $(U,G)$ 可出现；
* **多项式时间采样器**未构造；
* 构造性描述**不**推出 $\mathrm{DEC}\in\mathrm{RP}$。

**状态**：本条（降阶铅笔 Bézout 定理）经专家核验**通过**，可作为论文的独立命题；
两处必改（选定列构造、条目次数）已在本节写入。

## L7 的**独立陈述与完整证明**（专家第十轮优先级 1 要求的形态）

**定理（L7）** 设 $H,H_A\in\mathbb C^{q\times k}$、$q\ge k$、$\omega=\operatorname{rank}H$，且
$$\ker H\subseteq\ker H_A\qquad(\text{即 }(5a)) .$$
令 $P(\lambda)=\lambda H-H_A$。则

* **(i) $\omega=0$**：$H=0$，由 $\ker H=\mathbb C^k\subseteq\ker H_A$ 得 $H_A=0$、$P\equiv0$；$(5b)$ 自动成立（$W_K=0$）；
* **(ii) $\omega>0$**：$P$ 的**法秩**等于 $\omega$，且
$$\boxed{(5b)\iff\gcd\{\text{全部 }\omega\times\omega\text{ 子式 of }P\}\in\mathbb C^\times
\iff\operatorname{rank}P(\lambda_0)=\omega\ \ \forall\lambda_0\in\mathbb C}$$

*证明*（三类要素，逐条）

**① 因子化**：$\ker H\subseteq\ker H_A$ ⟹ $H_A$ 在 $\ker H$ 上为零 ⟹ $H_A$ 通过 $\operatorname{im}H$ 分解：
存在 $Z\in\mathbb C^{q\times q}$ 使
$$H_A=Z H .$$
（取 $Z$ 在 $\operatorname{im}H$ 上等于 $H_AH^{+}$、在补空间上任取。）

**② 铅笔变成 $(\lambda I-Z)H$**：
$$P(\lambda)=\lambda H-ZH=(\lambda I-Z)\,H .$$

**③ 秩与核**：对任意 $\lambda_0$，
$$\operatorname{rank}P(\lambda_0)=\operatorname{rank}\bigl((\lambda_0 I-Z)H\bigr)\le\operatorname{rank}H=\omega,$$
且
$$\ker P(\lambda_0)=\{x:\ Hx\in\ker(\lambda_0 I-Z)\}\ \supseteq\ \ker H,$$
故
$$\operatorname{rank}P(\lambda_0)=\omega\iff\ker P(\lambda_0)=\ker H\iff \ker(\lambda_0 I-Z)\cap\operatorname{im}H=\{0\}.$$

**④ 法秩 $=\omega$**：取 $\lambda_0$ 避开 $Z$ 的谱（有限多个点），则 $\lambda_0I-Z$ 可逆 ⟹
$\operatorname{rank}P(\lambda_0)=\operatorname{rank}H=\omega$ ✓

**⑤ 子式判据**：对固定 $\lambda_0$，"$\operatorname{rank}P(\lambda_0)\ge\omega$" $\iff$"某个 $\omega$ 阶子式非零"（秩的定义）。
故
$$\operatorname{rank}P(\lambda_0)=\omega\ \forall\lambda_0\iff \text{全部 }\omega\text{ 阶子式无公共根}
\iff \gcd\{\text{全体}\}\in\mathbb C^\times$$
（$\mathbb C$ 代数闭 + 单变量多项式的 gcd 非常数 $\iff$ 有公共根。）$\square$

**与 B.24 判据的一致性**：$\operatorname{rank}P(\lambda_0)<\omega\iff\exists0\ne x:\ Hx\in\ker(\lambda_0I-Z)$，
即 $\exists0\ne w\in\operatorname{im}H$ 与 $Z$ 的某特征值 $\lambda_0$ 使 $Zw=\lambda_0w$ ——
正是"$Z$ 在 $\operatorname{im}H=W_K$ 上有特征向量"✓（$\Phi_K$ 的坐标形式就是 $Z|_{\operatorname{im}H}$）。

**Lean 状态**：暂不形式化。障碍：Mathlib 无 Smith 形 / 多项式矩阵 gcd 基础设施；
而本定理的**核心**（因子化 $H_A=ZH$ + 秩-核关系）是可形式化的，但"gcd 为常数 $\iff$ 无公共根"
需要 $\mathbb C$ 代数闭 + 多项式根的理论（Mathlib 有 `Polynomial.exists_root` 于代数闭域），可行但工作量大。
按专家建议，**本定理的纸面证明先交他审核**，Lean 化留作后续。

## **撤回**：Bézout 系统的方程数与"全部极大子式为零"的刻画（专家第十轮）

上一节（"逐层 RAZE …次数界"）有两处**硬错**，已被专家逐条指出：

### 1. 方程数是 $2\omega$，不是 $2\omega-1$

$\deg\bigl(\sum_i u_ip_i\bigr)\le(\omega-1)+\omega=2\omega-1$，故要匹配的系数是
$\lambda^0,\dots,\lambda^{2\omega-1}$，共 $\boxed{2\omega}$ 条方程，**我漏了最高次那一条**。
$\omega=1$ 的检验最清楚：$\sum u_i(a_i\lambda+b_i)=1$ 需要 $\sum u_ia_i=0$ **与** $\sum u_ib_i=1$ 两条；
只写一条会把大量不可解系统误判为可解。

故正确的系统是
$$M_\omega(R)\,u=b_\omega,\qquad M_\omega(R)\in\mathbb C^{2\omega\times N\omega},\quad b_\omega=(1,0,\dots,0)^{\mathsf T}.$$

### 2. "全部 $(2\omega-1)$ 阶子式 of $[M|b]$ 为零"**不**刻画不相容

不相容是 $\operatorname{rank}[M|b]>\operatorname{rank}M$，**不是** $\operatorname{rank}[M|b]<$(行数)。
反例：$\operatorname{rank}M=m-1,\ \operatorname{rank}[M|b]=m$ ⟹ 不相容但 $[M|b]$ 有非零 $m$ 阶子式；
反之 $\operatorname{rank}M=m-2,\ \operatorname{rank}[M|b]=m-1$ ⟹ 不相容但全部 $m$ 阶子式为零。

**正确刻画：秩分层构造集**
$$\mathcal B_\omega=\bigcup_{s=0}^{2\omega-1}\Bigl\{R:\ \operatorname{rank}M_\omega(R)=s,\ \operatorname{rank}[M_\omega(R)\mid b_\omega]\ge s+1\Bigr\}.$$
（"秩恰 $s$" = 全部 $(s{+}1)$ 阶子式为零 **且** 某个 $s$ 阶子式非零；"秩 $\ge s+1$" = 某个 $(s{+}1)$ 阶子式非零。）

**但**——秩比较式本身是**精确**的：$\mathcal B_\omega=\{R:\operatorname{rank}[M|b]>\operatorname{rank}M\}$ ✓
（线性系统相容性判据；不需要闭性定理）。

### 3. 次数界的更正

$M_\omega$ 有 $2\omega$ 行、条目对 $R$ 次数 $\le\omega$ ⟹ $s$ 阶子式次数 $\le s\omega$ ⟹ 均匀界
$$\boxed{\deg_R\le 2\omega^2}\quad(\text{我在上一节写的 }2\omega(2\omega-1)\text{ 因方程数错而不对})$$

### 4. 秩分解要**三个**因子

$H=UV^{\mathsf T}$ 只给 $H$；还需 $H_A=ZV^{\mathsf T}$（因为 $\ker H\subseteq\ker H_A\iff H_A=ZV^{\mathsf T}$）。
于是 $\lambda H-H_A=(\lambda U-Z)V^{\mathsf T}$，$(\omega\times\omega)$ 子式**分解**为
$\det((\lambda U-Z)_{I,:})\cdot\det(V_{J,:}^{\mathsf T})$。
在 $(U,V,Z)$ 上：每个子式对 $(U,Z)$ 次数 $\le\omega$、对 $V$ 次数 $\le\omega$ ⟹ 总次数 $\le2\omega$；
配合 $2\omega$ 阶子式 ⟹
$$\boxed{\deg_{(U,V,Z)}\le 4\omega^2}$$

### 5. 抽样对**固定行**不成立；RP 结论**未证**

* 可实现性引理是**无约束** $M$ 的；观测器 $M=[L_0;R]$ 的首 $r$ 行固定 ⟹ 随机 $(U,V,Z)$ 一般**不满足**
  $H_{1:r}=L_0N_K$、$(H_A)_{1:r}=L_0AN_K$ ⟹ 采样器**未构造**（$r=0$ 时可，$r>0$ 需专门的参数化）；
* 且需"用多项式个参数空间覆盖所有候选"，未做；分量分解无多项式界；
* 故**只能**断言**逐图卡的条件命题**（专家 §8 的形式），**不能**断言 $\mathrm{DEC}\in\mathrm{RP}$。

### 6. 若将来真证出 RP，正确的推论是 $\mathrm{NP}=\mathrm{RP}$（不是"不可能"）

$L$ 属 RP 且 NP-hard（确定性多项式多一归约）⟹ $\mathrm{NP}\subseteq\mathrm{RP}$，又 $\mathrm{RP}\subseteq\mathrm{NP}$ ⟹
$$\boxed{\text{NP-hard}\ \Longrightarrow\ \mathrm{NP}=\mathrm{RP}}$$
这是**条件性推论**，不是"$q1$ 非 NP-hard"的证明。

### 7. 专家给的核验优先级

1. **L7**（降阶判据）——几乎所有后续论证都依赖它，最该先形式化；
2. **闭性定理**（射影证明；Lean 化可能不如纸面经济）；
3. **Bézout 系统**（两条引理：有界次数 Bézout；恒等式 ⟺ 系数线性系统可解）——**不要**形式化错的极大子式式；
4. **可实现性（含固定行）**——要单独的"像 = 指定块"陈述；
5. **RAZE ⟺ DEC**（含 $\omega=0$ 层，必须显式包含）；
6. 逐层复杂度（$\omega=2$ 的"边界"不要轻言，需输入规模分析）。

### 6. 次数界（补上 RP 论证的缺口 ③）——用 **Bézout 矩阵**

**构造**：在层-图卡上，$p_1,\dots,p_N$（$N=\binom{q}{\omega}$）为 $\lambda$ 的次数 $\le\omega$ 的多项式，
系数是 $R$ 的**线性**函数（因为 $H_S,H_{A,S}$ 对 $R$ 仿射、子式是 $\omega$ 次）。

由 **T1**（有界次数 Bézout，$D=\omega-1$）：$\gcd$ 是单位 $\iff\exists u_i$，$\deg u_i\le\omega-1$，使
$$\sum_{i=1}^N u_i(\lambda)\,p_i(\lambda;R)=1 .$$
把 $u_i=\sum_{j=0}^{\omega-1}u_{ij}\lambda^j$ 代入、匹配 $\lambda^0,\dots,\lambda^{2\omega-2}$ 的系数，得**线性系统**
$$M(R)\,u=b,$$
* $u$ 有 $N\omega$ 个未知量；
* 方程 $2\omega-1$ 条；
* $M(R)$ 的条目是 $p_i$ 的 $\lambda$-系数 ⟹ 对 $R$ **线性**；
* $b$ 是常数向量（$1$ 的系数）。

于是
$$\text{坏}\iff M(R)u=b\ \text{不可解}\iff \operatorname{rank}[M(R)\mid b]>\operatorname{rank}M(R)
\iff \text{全部 } (2\omega-1)\text{ 阶子式 of }[M(R)\mid b]\ \text{为零}.$$
故**坏集被次数**
$$\boxed{\ \deg\le(2\omega-1)\cdot 1=2\omega-1\ }\quad(\text{对 }R\text{ 而言})$$
的多项式切出（$M$ 的条目对 $R$ 线性、$b$ 为常数）✓

**在秩参数化坐标 $(U,V)$ 下**（$H=UV^{\mathsf T}$，$q\times\omega$ 与 $k\times\omega$）：
$M$ 的条目对 $U$ 与对 $V$ 各是 $\omega$ 次 ⟹ 子式次数 $\le(2\omega-1)\omega$ ⟹ 总次数
$$\boxed{\deg\le 2\omega(2\omega-1)=O(\omega^2)\ \text{（对 }(U,V)\text{ 而言）}}$$

**结论**：Schwartz–Zippel 给出失败概率 $\le 2\omega(2\omega-1)/|\mathbb S|$，
于是**单侧随机判定**在 $\omega$ 固定时是多项式次数的 ✓ —— 缺口 ③ **已补**（在 Bézout 形式下）。

**仍存的限定**
* 需要图卡分母 $\det H_S\ne0$ 的清晰处理（在层上它恒非零，故可用局部化）；
* 采样的正确性（秩参数化是否覆盖层的不可约分量）仍需逐支检查；
* "$\mathcal B$ 的定义多项式"是 $[M|b]$ 的极大子式，其**公共零点集**恰是坏集（双向）✓。

### 5. 限定（必须写清）

* 上面第 4 条是**条件性**结论：需要 ③ 的次数界、① 的采样正确性、② 的区域假设；
* **实版本**：需实点稠密（Stage 3.5）才能把复结论转实；否则只能得"复可行"；
* $\omega=1$ 的"P"依赖"行列式在层上是否恒零"的判定——这在**仿射层**上是线性代数，
  但层若由多个分支组成，须逐分支判定；
* **未做**：显式次数界；采样算法的实现与检验；$\omega=2$ 的显式判定。

## Stage 4 修复（专家第九轮第 3 步）：把目标换成**秩分层的 RAZE**

### 1. 目标问题 RAZE（Rank-stratified Affine Zero Exclusion）

**输入**：仿射线性族 $H(t),H_A(t)\in\mathbb C[t_1..t_s]^{q\times k}$，以及**指定的顶部块**
$H^{(0)}\in\mathbb C^{r\times k}$、$H_A^{(0)}\in\mathbb C^{r\times k}$（对应 $L_0N_K$ 与 $L_0AN_K$）。

**问**：是否存在 $t$ 与 $\omega\in\{0,\dots,k\}$，使
1. $\operatorname{rank}H(t)=\omega$（且顶部块等于指定值）；
2. $\ker H(t)\subseteq\ker H_A(t)$（由 $(5a)$ 的恒等式，见上一节）；
3. 任一 $\omega$ 列图卡 $S$ 上，$q\times\omega$ 的 $P_S=\lambda H_{[:,S]}-H_{A,[:,S]}$ 的全部 $\omega$ 阶子式的 gcd 为**非零常数**？

（$\omega=0$ 时条件 3 空洞、自动成立。）

### 2. 引理 A（DEC = RAZE，**精确等价**）

对观测器数据 $(A,C,L_0,q)$，令 $k=\dim K$、$N_K$ 为基。则
$$\boxed{\mathrm{DEC}(q)\iff \mathrm{RAZE}\ \text{在}\ (H(t)=\mathcal L(t)N_K,\ H_A(t)=\mathcal L(t)AN_K)\ \text{上为 YES}}$$
*证明*：$R\mapsto(H,H_A)$ 是仿射线性映射（Stage 4 第一步）；$(5a)\iff\ker H\subseteq\ker H_A$（专家恒等式）；
$(5b)$ 在 $\omega=\operatorname{rank}H$ 上 $\iff$ 降阶铅笔 $\omega$ 阶子式 gcd 常数（Stage 1 定稿 + L7）。
三个条件逐条对应，$\omega$ 遍历 $\{0..k\}$ 与 $R$ 的取值一一对应 ✓。$\square$

**这一步补上了专家指出的缺口**：原先把目标写成 AZE（只含 $\omega=k$），漏掉 $\omega<k$ 的候选；
RAZE **显式**量化全部 $\omega$，与 DEC 的候选类完全相同。

### 3. 引理 B（逐层可实现性）

若 $K\cap AK=0$，则对**每个** $\omega\in\{0,\dots,k\}$ 以及**每个**满足
$H^{(0)}=L_0N_K$、$H_A^{(0)}=L_0AN_K$ 的秩 $\omega$ 对 $(H,H_A)$，存在 $M$（顶部 $r$ 行为 $L_0$）实现它。
*证明*：由可实现性引理（$K\cap AK=0$ ⟹ $\Psi$ 满射），满射限制在秩 $\omega$ 子集上仍满射到该子集 ✓。$\square$

### 4. 于是归约**形式上成立**（但仍是有条件的）

$$\boxed{K\cap AK=0\ (\text{即 }n-p\ge2k)\ \Longrightarrow\ \bigl(\text{RAZE\ with prescribed blocks 是硬的}\ \Rightarrow\ q1\ \text{是硬的}\bigr)}$$

**与上一版的区别**：上一版把目标写成 AZE（只 $\omega=k$），**不成立**；本版目标 RAZE 覆盖全部 $\omega$，
故不再有"降秩候选造成假阳性"的漏洞 ✓。

**仍然存在的两个条件**
1. **指定顶部块**：RAZE 的实例带 $H^{(0)},H_A^{(0)}$（由 $L_0,A,K$ 决定）。故硬度必须对**带指定块的 RAZE** 成立，
   或需给出从无块 RAZE 到带块 RAZE 的多项式变换（专家 §2 的要求）；
2. **变量域**：RAZE 若要求 $t\in\mathbb R$，则还需实点稠密（Stage 3.5）；若 $t\in\mathbb C$，则归约给出的是复版本的硬度。

### 5. 状态与下一步

* 引理 A、B 都是**一行级**的组装（都已证）；
* **RAZE 的复杂度未知**：它既含 $\omega=k$（AZE 那一层，专家认为可能容易），又含 $\omega<k$（降秩层）；
* 由于 AZE 很可能容易（专家 §6.5 的 RP 论证），**$q1$ 的硬度若有，必须来自降秩层**——这是本版给出的
  **明确指认**：难度不在"满秩族的零排除"，而在"**降秩候选 + $(5a)$ 相容 + 实点**"的联合。
* 下一步：研究 $\omega=0$ 与 $\omega=1$ 两层的 RAZE（层数最小、条件最显式），看它们是否已是硬的；
  若这两层容易，再往 $\omega=2$ 走。

## 专家第九轮裁决：归约**未成立**（秩层缺口）+ 一个新恒等式 + AZE 的泛性质定理

### 1. 哪些对、哪些不对（专家逐条）

| 条目 | 裁决 |
|---|---|
| $K\cap AK=0$ 的可实现性引理 | ✅ **正确**（他给了更干净的表述：$\Psi:M\mapsto(MN_K,MAN_K)$ 满射 ⟺ $(v,w)\mapsto v+Aw$ 单射 ⟺ $K\cap AK=0$）|
| 维度条件 $n-p\ge2k$ | ✅ **正确** |
| 临界情形的显式构造 | ✅ 一致 |
| "首 $r$ 行固定"的处理 | ⚠️ **不够**：固定的**不只是 $H$ 的首 $r$ 行，还有 $(H_A)$ 的首 $r$ 行**，且两者由同一个 $L_0$ 联系 |
| AZE hard ⟹ DEC hard | ❌ **未成立** |
| AZE 硬度的文献 | ❌ **未找到**直接结果 |

### 2. 关键缺口：**秩层**

AZE 要求 $\operatorname{rank}H=k$（满列秩），但观测器问题允许 $\omega=\operatorname{rank}H<k$。
于是存在**假阳性路线**：AZE 实例在"满列秩意义下"是 no-instance，
但观测器可能存在一个 $\omega<k$ 的候选（满足 $\ker H\subseteq\ker H_A$）使 $(5b)$ 成立 ⟹ DEC 是 yes-instance。
⟹ **硬度不能传递**。

**三种修复（专家给）**
1. **强制满列秩**：令 $\operatorname{rank}(L_0N_K)=k$（需 $r\ge k$）——最干净，但改变 AZE 子类；
2. **秩分层 AZE 目标**：把 $\omega=0,\dots,k$ 全部纳入，每层带 $\ker H\subseteq\ker H_A$ 与对应降阶铅笔——
   这是 DEC 的**忠实**重述；
3. **秩排除 gadget**：加数据使所有 $\omega<k$ 候选不可行——需新构造。

### 3. 专家新给的恒等式（已证，本项目采纳）

$$\boxed{(5a)\iff \ker H\subseteq\ker H_A}$$
*证明*：$(5a)$ ⟺ $\ker[M;CA;C]\subseteq\ker(MA)$；左核 $=K\cap\ker M$，其元素形如 $N_Kx$ 且 $Hx=0$；
而 $MAN_Kx=H_Ax$。故包含关系 ⟺ $\ker H\subseteq\ker H_A$ ✓。
**推论**：若 $H$ 满列秩 $k$，则 $(5a)$ **自动成立**；若 $H$ 降秩，则 $(5a)$ 是额外约束。

### 4. AZE 的**泛性质定理**（专家给的，是本轮最重要的数学）

设 $H(t),H_A(t)\in\mathbb C[t_1..t_s]^{q\times k}$ 仿射线性、$U=\{\operatorname{rank}H=k\ne\varnothing\}$、$F=\mathbb C(t)$。则
$$\mathrm{AZE}\ \text{YES}\iff \gcd_{F[\lambda]}\{\text{全部 }k\text{ 阶子式 of }\lambda H-G\}=1 .$$
即**AZE 是"泛性质"，不是"找例外点"**；有解 ⟹ 解集 Zariski 开稠密（与我们的 Stage 3 同一机制）。

**推论（方阵情形完全解决）**：$q=k>0$ ⟹ **AZE 恒为 NO**；$q<k$ ⟹ 不可能满列秩，也是 NO。
**非平凡区域只有 $q>k$**。且一般对 $(H,G)$ 确实存在无有限秩降的满列秩铅笔，例如
$P(\lambda)=\begin{pmatrix}\lambda I_k\\-I_k\end{pmatrix}$。

### 5. 复杂度现状（专家结论）

* **未找到** AZE 的 NP-hard / $\exists\mathbb R$-hard 结果；文献主要是 Smith 形算法与结构理论，**不是**判定分类；
* 而且**有理由怀疑 AZE 容易**：泛性质 ⟹ 随机取一个 $t$ 即单侧判定（no-instance 无人能过，yes-instance 高概率通过）⟹
  若该单侧算法属 RP，则"AZE NP-hard"会推出 $\mathrm{NP}\subseteq\mathrm{RP}$；
* 因此：**不应**把多项式优化/矩阵补全/特征值问题的 NP-hard 结果当作自动适用于 AZE。

### 6. 文献（专家给，供 `docs/07` 采用）

1. Kaltofen, Krishnamoorthy, Saunders, *Fast parallel computation of Hermite and Smith forms*, SIAM J. Alg. Disc. Meth.
2. Storjohann, Labahn, *A fast Las Vegas algorithm for Smith normal form*, LAA 253 (1997) 155–173
3. Villard, *Generalized subresultants for Smith normal form*, JSC 20 (1995) 269–286
4. Murota, *On the Smith normal form of structured polynomial matrices*
5. Giesbrecht, Haraldson, Labahn, *Computing nearby non-trivial Smith forms*, JSC 102 (2021) 304–327

（**不可**把它们当作 AZE 的硬度或多项式可解性结论。）

### 7. 专家建议的四步

1. **形式化 AZE 泛性质定理**（含 projective no-infinity 论证）——独立定理；
2. **定该 gcd 检验的复杂度**（Smith/Popov、行列式因子、随机特殊化；分算术/位/随机三种模型；不要枚举子式）；
3. **修观测器归约**：形式化 $(5a)\iff\ker H\subseteq\ker H_A$；决定能否强制 $\operatorname{rank}H=k$；否则改用秩分层 AZE；
4. **最后**才谈硬度（实观测器问题：实点存在性，那里才可能有真正的实代数困难）。

## Stage 4（第二步）：**可实现性定理**——$k\le n/2$ 时我们的族覆盖"任意铅笔对（首行固定）"

### 1. 命题

设 $k=\dim K$、$N_K$（$n\times k$，满列秩）为 $K$ 的基，且 $K\cap AK=0$（下面说明可安排）。
则对**任意**给定的 $q\times k$ 矩阵对 $(H,H_A)$，存在 $q\times n$ 的 $M$ 使
$$MN_K=H,\qquad MAN_K=H_A ,$$
且 $M$ 的自由度为 $qn-2qk=q(n-2k)$（在 $K\oplus AK$ 上钉死 $M$，其余自由）。

*证明*：$M|_{K}$ 由 $H$ 唯一确定（$N_K$ 满列秩）；$M|_{AK}$ 由 $H_A$ 唯一确定（$AN_K$ 满列秩，因为 $K\cap AK=0$）；
因 $K\cap AK=0$，两个约束**互不干扰** ⟹ 可同时满足；$M$ 在 $K\oplus AK$ 之外任取即可。$\square$

**推论**：只要 $k\le n/2$ 且 $K\cap AK=0$，我们的族（$R$ 遍历、$L_0$ 固定）在铅笔对空间里**不是薄截面**，
而是"**首 $r$ 行固定**"的整个（仿射）空间。

### 2. $K\cap AK=0$ 与 $K=\ker[C;CA]$ 可**同时**安排的显式构造（已核验）

**必要条件**：$K\subseteq\ker C$ 且 $AK\subseteq\ker C$ 且 $K\cap AK=0$ ⟹ $\dim\ker C\ge 2k$ ⟹
$$\boxed{\ n-p\ \ge\ 2k\ }\quad(\text{即 }k\le (n-p)/2).$$

**构造（$n=6,p=2,k=2$，$n-p=4=2k$ 的临界情形）**：取 $K=\langle e_1,e_2\rangle$、
$$C=\begin{pmatrix}0&0&1&0&0&0\\0&0&0&1&0&0\end{pmatrix},\qquad
A:\ e_1\mapsto e_5,\ e_2\mapsto e_6,\ e_5\mapsto e_3,\ e_6\mapsto e_4,\ e_3,e_4\mapsto0 .$$
于是 $\ker C=\langle e_1,e_2,e_5,e_6\rangle$、$AK=\langle e_5,e_6\rangle\subseteq\ker C$、
$K\cap AK=0$、$\operatorname{rank}[C;CA]=4=n-k$，故 $K=\ker[C;CA]$ ✓。

**核验**（`tools/verification/check_realizability.py`，精确有理）：
$$\operatorname{rank}[C;CA]=4\ ✓,\quad \dim K=2\ ✓,\quad \dim(K\cap AK)=0\ ✓,\quad
\text{随机目标对可解 } \mathbf{20/20}\ ✓$$
即对**任意** $(H,H_A)\in(\mathbb Q^{3\times2})^2$，方程组 $MN_K=H$、$MAN_K=H_A$ 都有解。

**结论**：在 $n-p\ge 2k$ 的区域，我们的族确实覆盖"首 $r$ 行固定"的**整个**铅笔对空间
（不是薄截面）⟹ Stage 4 第二步的条件性归约在该区域**成立**。

### 3. 于是 $q1$ 的硬度问题**归约到**一个标准问题

$$\boxed{\ q1\ \text{的硬度}\ \Longleftarrow\ \text{"仿射铅笔零排除(AZE) + 首行固定"的硬度}\ }$$

即：若 AZE（在给定仿射线性族里找一组参数使 $q\times\omega$ 铅笔对所有有限 $\lambda$ 满列秩）是硬的，
则我们的判定问题也是硬的（在 $k\le n/2$ 的区域内）。

**反向**：AZE 的算法 ⟹ 我们（$k\le n/2$ 区域）的算法。

**因此**：$q1$ 的复杂度**不再是本族的私有问题**，而是与 AZE 的复杂度绑定。
这既可能帮我们（若 AZE 有已知结果），也可能说明 $q1$ 的难度是"一般铅笔问题"的难度。

### 4. 分离的另一侧（$k>n/2$）

$k>n/2$ 时 $K\cap AK\ne0$ 必然（维数），故 $(H,H_A)$ 必须满足**线性约束**（$M$ 在 $K\cap AK$ 上的两个作用相容）
⟹ 族是**薄截面**，一般 AZE 实例**不能**任意实现 ⟹ 该区域的难度须单独论证。

### 5. 状态与待办

* 命题 1 的证明是**一行线性代数**（在两子空间上分别钉死 $M$），可靠；
* "$K\cap AK=0$ 且 $K=\ker[C;CA]$ 可同时安排"**未逐条核验**——须给构造 + 小例（$n=4,k=2$ 不行，需 $n\ge 4,k\le2$ 且 $\dim\ker C\ge 4$，
  例如 $p=1$ 时 $\dim\ker C=3<4$ ⟹ **$p=1$ 时此构造不成立**！须 $p\ge2$ 或 $k< n/2$ 更严）；
* 因此本条目前是**条件性归约**：须先修好第 2 条的可安排性。这是下一步的明确任务。

## Stage 3.5：实点稠密性（专家优先级 3）

### 1. 要证的是什么

复结论（Prop A/B/C）说的是 $\mathcal B_{\mathbb C}\subsetneq U_{\mathbb C}$；要推出**实**可行，需要
$$\mathcal F_{\mathbb C}=U_{\mathbb C}\setminus\mathcal B_{\mathbb C}\ \text{非空开稠密}\ \Longrightarrow\ \mathcal F_{\mathbb C}\cap U(\mathbb R)\ne\varnothing .$$
充分条件：$U(\mathbb R)$ 在 $U_{\mathbb C}$ 中 **Zariski 稠密**（专家 §5.2）。

### 2. 一条标准判据（本项目可直接用）

**事实**（实代数几何的标准结论）：若不可约实代数集 $U$（定义在 $\mathbb R$ 上）有一个**非奇异实点**，
则 $U(\mathbb R)$ 在 $U$ 中 Zariski 稠密。

**本项目的情形**：所有定义多项式（$H=\mathcal L N_K$、$H_A=\mathcal L AN_K$、$\det H_{T,S}$、$(5a)$ 的秩条件）
的系数都是**有理数**（$A,C,L_0,N_K$ 有理），故每个层-图卡都定义在 $\mathbb R$ 上 ✓。
于是"实点稠密"的检验退化为：**在每个不可约分量上找到一个非奇异实点**。

### 3. 在 Stage 2 的实例上核对

数据：$C=e_1^{\mathsf T}$、$L_0=e_2^{\mathsf T}$、$A$ 如 Stage 2、$k=q=2$；$\omega=1$ 层 = 超平面 $\{r_3=0\}$。

* 图卡：$S=\{1\}$（$H$ 的第 1 列 $=(1,r_2)\ne0$ ✓）、$T=\{1\}$（$1\times1$ 子式 $=1\ne0$ ✓）；
* 该图卡 = $\mathbb R^4$ 中的**线性子空间** $\{r_3=0\}$（维 3），显然不可约有大量实点；
* 取实点 $R=(0,1,0,1)$：$\det H_{T,S}=1\ne0$ ✓（非奇异），且**可行**（Stage 2 已用 `consistency_checks` 验证）⟹
  该分量的实点稠密成立，**且可行集含实点**（直接验证，不需要稠密性）。

### 4. 一般情形的诚实评估

* 图卡由"秩条件 + 开条件"定义 ⟹ 通常是**不可约**的（秩条件在层内是恒等式，开条件不切割）；
  真正可能的不可约分解发生在 $(5a)$（秩等式）与 $\operatorname{rank}H=\omega$ 的**交集**上；
* 但**不**能排除"实点稀少"的退化分量（专家给的 $x^2+y^2=0$ 型）；
  本项目是否需要这类检验，取决于 $A,C,L_0$ 是否会产生"实点少"的层-图卡——**未做系统检查**；
* 因此：**逐层-图卡检验非奇异实点**是可执行的步骤，但目前只在个别实例上做过。

### 5. 结论与状态

* Stage 2 的实例：实点稠密 ✓（线性图卡，且可行点已显式给出）；
* 一般情形：需对每个不可约分量找非奇异实点；这是"存在性 + Jacobi 秩"的检验，**弱于**一般实可行性，
  但仍不是多项式算法；
* **未做**：$n=4$、$p=1$ 的更大实例族上的系统检查；$(5a)$ 引起的分量分解。

## Stage 3 定稿（专家第八轮）：闭性定理、消元理想三情形、函数域 gcd 判据

上一节（Stage 3 初稿）的二分方向对，但**用错了"真理想"这个术语**。专家的更正与补充：

### 1. **闭性定理（Proposition A）**——坏集是 Zariski 闭的

在可容许层-图卡 $U$ 上（$\operatorname{rank}H_S=\omega$ 恒定），令 $p_1,\dots,p_N$ 为 $P_S=\lambda H_S-H_{A,S}$ 的
全部 $\omega$ 阶子式，齐次化为 $p_i^{\rm h}(R;\alpha,\beta)$（即 $\alpha H_S-\beta H_{A,S}$ 的对应子式）。

* **无穷远处无根**：$[\alpha:\beta]=[1:0]$ 时 $\alpha H_S-\beta H_{A,S}=H_S$，而 $\operatorname{rank}H_S=\omega$
  ⟹ 至少一个 $\omega$ 阶子式非零 ⟹ 齐次子式在无穷远处**不能**同时为零；
* 故关联簇 $\mathcal X=\{p_i^{\rm h}=0\ \forall i\}\subseteq U\times\mathbb P^1$ 是闭的，且其所有点的 $\beta\ne0$；
* 投影 $\mathrm{pr}:U\times\mathbb P^1\to U$ 是**proper**（$\mathbb P^1$ 射影）⟹ **闭映射** ⟹
  $$\boxed{\ \mathcal B_S=\mathrm{pr}(\mathcal X)\ \text{是}\ U\ \text{中的 Zariski 闭集}\ }$$
  且**恰好等于**有限 $\lambda$ 的公共根集（不是它的闭包）——这正是对"消元只给闭包"的疑问的答案
  （一般反例 $\langle R\lambda-1\rangle$ 的机制在这里被"首项满列秩"排除）。

### 2. **消元理想的三情形**（更正我的"真理想"错误）

设 $A$ 是图卡的坐标环（整环）、$J=\langle p_i\rangle\subseteq A[\lambda]$、$E=J\cap A$。则

| $E$ | $\mathcal B$ | 可行集 |
|---|---|---|
| $E=(0)$ | $\mathcal B=U$ | **空** |
| $0\ne E\ne A$ | 真闭子集 | **非空开稠密** |
| $E=A$ | $\mathcal B=\varnothing$ | 整个 $U$ |

**关键**：可行 $\iff E\ne(0)$，**不是**"$E$ 是真理想"——在整环里 $E=(0)$ 与 $0\ne E\ne A$ **都**是真理想，
但结论相反。等价地：**判投影 $\pi:\mathcal X\to U$ 是否 dominant**（不 dominant ⟺ 有可行点）。

### 3. **函数域 gcd 判据（Proposition C）**——最可算的形式

设 $F=\mathbb C(U)$ 为不可约图卡分量的函数域，$P_S(\lambda)\in F[\lambda]^{q\times\omega}$。则
$$\deg_{\lambda}\gcd_{F[\lambda]}\{\text{全部 }\omega\text{ 阶子式 of }P_S\}>0
\iff \mathcal B=U\ (\text{该分量全不可行});\qquad =0\iff \mathcal B\subsetneq U .$$
即**把"$\exists$ 参数"的族级问题化成"一个函数域上一次 gcd 的次数"**。

### 4. **不要枚举子式**：用多项式矩阵的**最大行列式因子**

$$\boxed{d_\omega(\lambda)=\gcd\{\text{全部 }\omega\text{ 阶子式}\}\ \sim\ \prod_{i=1}^{\omega}s_i(\lambda)}$$
（$s_i$ 为 Smith 不变因子）。故可用 Smith/Popov 形算法**避开 $\binom{q}{\omega}$ 个组合**。
限定：系数域是函数域 $F$，其算术本身可能昂贵；"$F$ 上的多项式时间"≠"二进制位复杂度"。

### 5. **复 ≠ 实**（重要限定）

上面的闭性/二分是**复**的。$R$ 是**实**变量，故
* **单向**：实可行 ⟹ $\mathcal B_{\mathbb C}\ne U_{\mathbb C}$；
* **反向需要实点稠密**（例如某分量有不奇异实点 ⟹ 实点 Zariski 稠密 ⟹ 可推）；
* 反例（专家给）：$x^2+y^2=0$ 的复维数是 1，实点只有原点——复开稠密**不**保证实可行。

### 6. 更正后的 $q_{\min}$ 形式

$$q_{\min}=\min\{q:\ \exists\omega,\ S,\ \nu:\ (U_{\omega,S,\nu}\setminus\mathcal B_{\omega,S,\nu})(\mathbb R)\ne\varnothing\},$$
其中 $U_{\omega,S,\nu}$ 是**可容许**层-图卡的**不可约分量**，$\nu$ 是分量指标。
若实点稠密成立，末条可简化为 $\mathcal B_{\omega,S,\nu}\subsetneq U_{\omega,S,\nu}$。

### 7. 专家给的优先级

1. **证闭性定理**（$\mathbb P^1$ 紧化；已在上文给出）——**做掉**；
2. **导出函数域 gcd 判据**——**做掉**（Proposition C）；
3. **解决实点问题**（实点是否稠密）——未做，**关键缺口**；
4. **复杂度**（先研究"仿射矩形铅笔的一般判"的硬度，再看能否嵌入本族）——未做。

## （以下为 Stage 3 初稿，已被上节取代；"真理想"的表述是错的）
## Stage 3：与企业级候选问题的对照 + 一个结构性的**二分**结论

### 1. 我们的问题的规范形状

由 Stage 1 定稿：
$$\mathrm{FEAS}(q)\iff\exists\omega\ \exists S\ \exists R:\ R\in U_S,\ (5a),\ 
\gcd\bigl\{\omega\text{ 阶子式 of }\lambda H(R)-H_A(R)\bigr\}\in\mathbb C^\times ,$$
其中 $H(R)=\mathcal L(R)N_K$、$H_A(R)=\mathcal L(R)AN_K$ ——**两个矩阵共享同一个 $\mathcal L(R)$**，且都**线性**依赖 $R$。

### 2. 与三个候选问题的关系

| 候选问题 | 包含关系 | 说明 |
|---|---|---|
| **(A) 仿射铅笔零排除**（∃ 参数使 pencil 处处满列秩）| 我们 $\subset$ (A) **真子类** | (A) 允许 $H,H_A$ 独立仿射；(A) 可写成 $\lambda H-H_A$ 的一般仿射对。我们的额外结构：$H_A=\mathcal L AN_K$、$H=\mathcal L N_K$（同一 $\mathcal L$，右侧固定乘子 $N_K$、$AN_K$）。**未见**把一般 (A) 归约到我们的途径 |
| **(B) 多项式矩阵左互质补全** | 我们 $\subset$ (B) 真子类 | (B) 的矩阵可任意次数；我们是**一次**铅笔，且自由项以线性方式进入系数对 |
| **(C) 参数化行列式簇的非空性** | 判据可化为 (C) | "子式有公共根"= 某个**消元理想**的零点集；见下面第 3 条 |

### 3. 结构性二分（**本轮的主要新结论**）

**观察**："全部 $\omega$ 阶子式有公共复根"是一个**闭**条件——它由消元理想 $I\cap\mathbb C[R]$ 刻画
（$I=\langle p_1,\dots,p_N\rangle\subseteq\mathbb C[R,\lambda]$ 消去 $\lambda$）。故在固定层与图卡上：

$$\text{坏集}\ \mathcal B_S:=\{R\in U_S:\ \text{子式有公共根}\}\ \text{是闭集(相对}\ U_S\text{)};\qquad
\text{可行集}=U_S\setminus\mathcal B_S\ \text{是开集}.$$

于是对每个（不可约的）层与图卡只有两种可能：

$$\boxed{\ \mathcal B_S=U_S\ (\text{该卡全不可行})\quad\text{或}\quad \mathcal B_S\subsetneq U_S\ (\text{可行集是开稠密集})\ }$$

即**没有"部分可行"的中间情形**：可行要么空、要么开稠密。

**这与 Stage 2 的两个观察完全一致**：可行实例的可行集 $=\{r_3=0\}\setminus\{r_4=0\}$ 是开稠密 ✓；
上一批 12 组"全不可行"正是 $\mathcal B_S=U_S$ 的情形 ✓。

**对 $q1$ 的含义**（这是关键）
$$\text{"该卡可行"}\iff \mathcal B_S\subsetneq U_S\iff \text{消元理想 } I\cap\mathbb C[R]\ \text{不是整个坐标环（且在 }U_S\text{ 上非饱和）},$$
即一个**理想论**问题（理想是否为真/是否饱和），而**不是**数值搜索问题。这解释了为什么
* 采样/随机 $R$ 找到可行点就足以**证明可行**（开稠密！）；
* 找不到永远不能证明不可行（需要理想论）。

### 4. 于是 $q1$ 的形状可以精确写成

$$q_{\min}=\min\{q:\ \exists\omega<\min(q,k),\ \exists S:\ \mathcal B_S^{(q)}\subsetneq U_S^{(q)}\},$$

即"**最小使某族的消元理想为真的阶**"。这是**参数化消元 + 层选择**的问题；
它的难度来源不再是谱条件本身（已完全消解为 gcd），而是

* 消元理想的计算/判定（Gröbner 基的最坏复杂度是指数），
* 层与图卡的**组合选择**（$\sum_\omega\binom{k}{\omega}\binom{q}{\omega}$ 个卡）。

### 5. 限定

* "可行 = 开稠密"只在**不可约层**上成立；层与图卡都是构造集，可能有多个不可约分支，须逐个讨论；
* $\mathcal B_S$ 的"闭"是相对 $U_S$（$U_S$ 本身是开集）；带分母的写法要小心；
* 上述二分**不**给出算法，也**不**给出硬度——它只说明问题的**类型**（理想论，而非可行性搜索）。

## Stage 1：层上图卡化的**族级**判据（专家第七轮 §6 要求的表述）

### 1. 输入模型（先钉死，避免"隐含约定"）

* 数据 $A\in\mathbb Q^{n\times n}$、$C\in\mathbb Q^{p\times n}$、$L_0\in\mathbb Q^{r\times n}$，条目用**二进制**编码；
* 整数 $q\ge r$ 用**二进制**入输入（另设 $q$ 固定为常数的版本 $\mathrm{DEC}_{\rm fix}$）；
* 设计变量 $R\in\mathbb R^{(q-r)\times n}$（**实**）；谱量词 $\forall\lambda\in\mathbb C$（**复**）；
* 判定对象：$\mathrm{DEC}(q)$ = 是否存在 $R$ 使 $(5a)\wedge(5b)$；优化版 $q_{\min}$ 的阈值判定即 $\mathrm{DEC}$；
* $q_{\min}$ 有已知有限上界（文献 $\Sigma_{FO}\subseteq[q_0,n_0-p]$），故搜索范围有限。

### 2. 分层 + 图卡

固定 $K=\ker[C;CA]$（$k=\dim K$）、$N_K$ 为 $K$ 的**有理**基，$H(R)=\mathcal L(R)N_K$（$q\times k$）、$H_A(R)=\mathcal LA(R)N_K$。

**层**：$\mathcal W_\omega:=\{R:\operatorname{rank}H(R)=\omega\}$，$\omega\in\{0,\dots,\min(q,k)\}$（构造集：秩条件）。

**图卡**：在 $\mathcal W_\omega$ 上取 $S\subseteq\{1,\dots,q\}$、$|S|=\omega$，图卡
$$U_S:=\{R\in\mathcal W_\omega:\ \det H_S(R)\ne0\},$$
其中 $H_S$ 是 $H$ 的 $S$-行（$\omega\times\omega$）。$\{U_S\}$ 覆盖 $\mathcal W_\omega$，
图卡数 $=\binom{q}{\omega}$（列的选择已由 $N_K$ 固定）。

**卡内坐标**：$w=Hc$（$c\in\mathbb C^k$，$\operatorname{rank}H=\omega$ ⟹ $w$ 只依赖 $c\bmod\ker H$）；
在 $U_S$ 上 $H_S$ 可逆，故 $W_K$ 的基取 $S$-行；$\Phi_K(w)=H_Ac$。

### 3. 卡内的构造性条件（**关键：清分母**）

在 $U_S$ 上 $\omega\ge1$。记 $P_S(\lambda):=\lambda H_S-\mathcal LA_S$（$\omega\times\omega$）。
"$\Phi_K$ 在 $W_K$ 上无不变线" $\iff$ $P_S$ 在 $\mathbb C$ 上无特征值 $\iff$
$$\gcd\bigl\{\text{全部 }\omega\times\omega\text{ 子式 of }P_S\bigr\}\in\mathbb C^\times .$$
（$\omega=\min(q,k)$ 时 $P_S$ 方阵，就是 $\det P_S\in\mathbb C^\times$。）

用 **Bézout 形式**并**清分母**：子式的分子记为 $\tilde p_i(R,\lambda)$（$R$ 的多项式），则卡内条件等价于
$$\boxed{\ \exists u_i:\ \sum_i u_i(\lambda)\,\tilde p_i(R,\lambda)=\bigl(\det H_S(R)\bigr)^{N}\ }$$
（$N$ 为清分母所需的幂；$\deg_\lambda u_i$ 由 T1 的 $D$-界控制）。
右端固定为 $(\det H_S)^N$ 后，这是**关于 $u$ 的线性系统**，数据是 $R$ 的多项式 ⟹
可解性 = 秩条件 $\operatorname{rank}[M(R)\mid b(R)]=\operatorname{rank}M(R)$ ⟹ **卡内条件是构造集** ✓

于是族级判据：
$$\mathrm{FEAS}=\bigcup_{\omega=0}^{\min(q,k)}\ \bigcup_{|S|=\omega}\Bigl[\,U_S\ \cap\ \{(5a)\}\ \cap\ \{\text{上述线性系统可解}\}\,\Bigr]
\quad(\omega=0\ \text{项为}\ \{H=0\}\cap\{(5a)\}).$$

### 4. 规模记账与**两处更正**（方阵/矩形混淆）

| 项 | 量 |
|---|---|
| 层数 | $\le\min(q,k)+1$ |
| 图卡数 | $\sum_\omega\binom{k}{\omega}$（按 $K$ 的**列**选）|
| 卡内子式数 | $\binom{q}{\omega}$（$P_S$ 是 $q\times\omega$，$\omega$ 阶子式）|
| $R$ 的自由参数 | $(q-r)n$ |

**更正 1（图卡按列，不按行）**：$W_K=\operatorname{im}H$ 由 $H$ 的**列**张成，故图卡应选 $\omega$ **列**
（$S\subseteq\{1..k\}$、$\det H_{[:,S]}\ne0$），不是选行。选行的版本我先前写错了。

**更正 2（卡内判据是 gcd，不是单个行列式）**：我曾写"$P_S$ 是方阵 ⟹ 只有一个子式 $\det P_S$ ⟹
条件退化为 $\det P_S$ 为常数"。**这是错的**：$P_S=\lambda H_{[:,S]}-H_{A,[:,S]}$ 是 $q\times\omega$
（$\omega\le\min(q,k)$，通常 $q>\omega$），**矩形** ⟹ 有 $\binom{q}{\omega}$ 个 $\omega$ 阶子式，
条件是它们的 **gcd 为非零常数**（等价地：无公共复根）。这正是 L7/B.8 的判据，也解释了为什么
"某个子式有根"不能推出"降秩"（见上面的撤回节）。

**机器核对**（`tools/verification/check_rectangular_criterion.py`）：

| 数据 | $\omega$ | $\omega$ 阶子式 | gcd | 判定 | 与 `consistency_checks` |
|---|---|---|---|---|---|
| $A=(0,1,0;-1,-1,-1;-1,-1,-1)$、$C=e_1^{\mathsf T}$、$L_0=e_3^{\mathsf T}$、$R=(-1,-1,-1)$ | 1 | $\lambda+1,\ -\lambda-2$ | $1$（常数）| $(5b)$ 成立 | ✓ 一致 |
| 同上，$R=(0,0,0)$ | 1 | $\lambda+1,\ 0$ | $\lambda+1$（非常数）| $(5b)$ 失败 | ✓ 一致 |

**结论（Stage 1 定稿）**：
$$(5b)\iff\gcd\bigl\{\text{全部 }\omega\text{ 阶子式 of }\lambda H-H_A\bigr\}\in\mathbb C^\times,\qquad
H=\mathcal L N_K,\ H_A=\mathcal LA N_K .$$
族级版本 = 按 $\omega$ 分层、层内按 $\binom{k}{\omega}$ 个图卡覆盖、卡内清分母后化为线性系统可解性（构造集）。


### 5. 限定与未做

* **域**：$R$ 实、$\lambda$ 复；上面的构造集是在 $\mathbb C[R]$ 上算的，取实点仍需"实构造集非空"，
  故这**不**等于给出了算法；
* $\det H_S$ 作分母 ⟹ 卡内条件只在 $U_S$ 上成立，跨卡须并集（已写成并集）；
* **未做**：$\deg_\lambda$ 与 $N$ 的显式界；卡数与 $q$ 同时增长时的复杂度分析；
  "$\exists R$ 使 $\det P_S$ 常数"这一具体问题的**判定算法**（这正是 Stage 3/4 的入口）。


## **撤回**：把专家的 $\omega=q$ 推广成 $\omega=\min(q,k)$ 是**错的**

我曾写下"若 $\omega=\min(q,k)$ 则 $(5b)$ 失败"，并给"两情形"证明。**第二种情形（$k<q$，即 $\omega=k$）无效**，
已被有限检验**否证**。

**错在哪**：$k<q$ 时铅笔 $\lambda H-H_A$ 是 $q\times k$ **矩形**。我用"某个 $k$ 阶子式
$m_T(\lambda)=\det(\lambda H_T-H_{A,T})$ 在 $\lambda_0$ 为零"去推 $\operatorname{rank}(\lambda_0H-H_A)<k$——
**不成立**：一个 $k$ 阶子式为零只说明**那个**子式奇异，别的 $k$ 阶子式仍可非零。
（方阵情形（专家的 $\omega=q$）没问题：方阵 $\det=0$ **等价于**降秩 ✓。）

**反例**（`tools/verification/check_omega_max_infeasible.py` 报告 8748 个）：
$$A=\begin{pmatrix}0&1&0\\-1&-1&-1\\-1&-1&-1\end{pmatrix},\quad C=e_1^{\mathsf T},\quad L_0=e_3^{\mathsf T},\quad
q=2,\quad R=(-1,-1,-1)$$
$K=\langle e_3\rangle$（$k=1$）、$L_0|_K\ne0$ 故 $r_0=1=k$；按（错误的）命题应不可行，
但 `consistency_checks` 精确判定 $(5a)$ ✓、$(5b)$ ✓，**可行**。

**仍成立的**（专家 §4.2，方阵情形）：$\omega=q>0\ \Longrightarrow\ (5b)$ 失败。

**教训**：矩形铅笔的障碍是"**全部** $k$ 阶子式的 gcd 非常数"，**不是**"某一个 $k$ 阶子式有根"。
这是 §10.1 已记录的"用一个子式/一个左零向量刻画秩降"老坑的变形。
**规则**：凡从"某个子式"推"降秩"，先写清矩阵是方阵还是矩形。


## 专家第七轮的**结构性推论**：$\omega=q$ 自动不可行（已验证）

专家在 33 号答复 §4.2–§4.4 指出三条按 $\omega=\dim W_K$ 分的情形。本条照录并核验：

**命题（$\omega=q$ ⟹ $(5b)$ 必失败）** 若 $\omega=q>0$，则 $P_K(\lambda)=\lambda\iota_K-\Phi_K$ 是**方阵**；
$\Phi_K$ 是 $\mathbb C^q$ 上的自同态，在 $\mathbb C$ 上必有特征向量 ⟹ 存在 $0\ne w\in W_K$ 与 $\lambda$ 使
$\Phi_K(w)=\lambda w$ ⟹ 由 B.24 判据 $(5b)$ 失败。
**推论（必要条件）** 可行（$(5b)$ 成立）必须 $\omega<q$ 或 $\omega=0$。**本项目的 $q_{\min}$ 因此**：
在 $\omega=q$ 的层上不可能可行——这类层可**直接排除**，不必算行列式因子。
*证明要点*：代数闭域上任意非零方阵有特征值（特征多项式有根）✓。

**命题（$\omega=0$ ⟹ $(5b)$ 成立）** $W_K=0$ 无 $0\ne w$，判据空洞 ⟹ 成立（与 B.24 的"推论 2"一致）。
**注意**：这不推出 $(5a)$；$(5a)$ 仍须单独满足。

**命题（$\omega=1$ 的判据退化为单个非零条件）** $W_K=\langle w\rangle$ 时，
$$(5b)\ \text{失败}\iff\Phi_K(w)\in\mathbb Cw\iff\det\bigl[\,w\ \ \Phi_K(w)\,\bigr]=0\quad(\text{在固定坐标下})$$
即 $\omega=1$ 的谱条件**不是**一堆多项式不等式，而是**一个非零判定**。

**为什么重要**：这三条把 $\omega$ 的**三个可能值全部显式化**，并且给出
* $\omega=q$：**自动排除**（$q_{\min}$ 的可达集立刻缩小）；
* $\omega=0$：**自动可行**（剩下只需 $(5a)$）；
* $\omega=1$：**单个行列式**（最容易算，也是最小案例的主情形）。

### 更正记录（专家 §0 指出）

33 号报告里把 $(5b)$ 写成 $\lambda\mathcal L-\lambda\mathcal LA$（**错**）：正确的观测器铅笔是
$$Q_{\mathcal L}(\lambda)=\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\ CA\\ C\end{bmatrix}.$$
前者是 $\lambda(\mathcal L-\mathcal LA)$ 的标量倍，谱性质完全不同。本条更正**已记入卷宗**，
并在下一份报告中显式改正（33 号已归档，按"归档只读"规则不改原文件）。
同理 $n=4,p=1,q=2,r=1$ 时 $R\in\mathbb R^{(q-r)\times n}=\mathbb R^{1\times 4}$（33 号误写为 $2\times4$）。

## L7：修正铅笔 $P_K$ 的行列式因子判据（含**规模改进**）

### Theorem（修正域上的精确判据）

设 $\omega=\dim W_K$、$\iota_K:W_K\hookrightarrow\mathbb C^q$、$\Phi_K$ 如前述，$P_K(\lambda)=\lambda\iota_K-\Phi_K$（$q\times\omega$）。则
$$\boxed{(5b)\iff\gcd\bigl\{\text{全部 }\omega\times\omega\text{ 子式 of }P_K\bigr\}\in\mathbb C^\times .}$$

*证明*：
1. **$P_K$ 的法秩 $=\omega$**：取左逆 $J$（$\iota_K$ 单射），$JP_K(\lambda)=\lambda I_\omega-J\Phi_K$ 的行列式是 $\omega$ 次首一多项式，
   不恒为零 ⟹ 存在 $\lambda$ 使 $JP_K(\lambda)$ 可逆 ⟹ $P_K(\lambda)$ 满列秩 ⟹ 法秩 $=\omega$ ✓
2. **由 (12)**（上面的直接证明）：$\dim\ker Q_{\mathcal L}(\lambda)=\dim D+\dim\ker P_K(\lambda)$，故
   $$(5b)\ \text{失败}\iff\exists\lambda:\ \ker P_K(\lambda)\ne0\iff\exists\lambda:\ \operatorname{rank}P_K(\lambda)<\omega .$$
3. **由 B.8**（取 $h=\omega$、$F=\mathbb C$、矩阵 $P_K$）：$\operatorname{rank}P_K(\lambda)=\omega\ \forall\lambda$
   $\iff$ 全部 $\omega$ 阶子式的 gcd 是**非零常数** ✓。$\square$

### 推论（**规模改进**）

原判据（B.8 用在 $Q_{\mathcal L}$ 上）要枚举 $N_Q=\binom{q+2p}{h}\binom{n}{h}$ 个子式；修正后的判据只枚举
$$\boxed{N_K=\binom{q}{\omega}}$$
个。**这是单个二项式而不是乘积**，故
$$N_K\ \text{多项式}\iff\min(\omega,\ q-\omega)=O(1),$$
比原判据的两条条件（$\min(h,m-h)$ 与 $\min(h,n-h)$ 同时有界）**弱得多**。

**意义**：专家反复强调"正确域"不只是概念洁癖——把判据搬到 $W_K$ 后，
① 不再需要 Kronecker 记账、② 子式个数从"乘积"降为"单个二项式"、③ 与 T2/T3 的构造性论证兼容。

### 状态与限定

* 本条是 (12)、B.8、"法秩 $=\omega$"三者的**组装**，三者均已证 ⟹ **M3/F1**；
* **限定**：$\omega=\omega(R)$ 依赖 $R$，族内仍须按 $\omega$ 分层（与 B.8 的 $h$ 分层同理）；
* 待办：把 $N_K$ 的规模界写进 T2/T3 的定理陈述。

## Q1 定稿（专家第五轮）：主域是 $W_K=\mathcal LK$（本节取代上面两节的 $W$ 与 $W_0$）

专家在 30 号答复 §7 明确：**核方程本身不要求 $v\in V$**，故
$$\ker Q_{\mathcal L}(\lambda)=\{v\in K:\ \mathcal LAv=\lambda\mathcal Lv\},\qquad K=\ker[C;CA],$$
直接从核方程得到的域是
$$\boxed{W_K:=\mathcal LK}.$$

**定义**：$\Phi_K(\mathcal Lv):=\mathcal LAv$（$v\in K$）。
**良定义**：$\mathcal Lv_1=\mathcal Lv_2$、$u=v_1-v_2$ ⟹ $\mathcal Lu=Cu=CAu=0$ ⟹ 由 $(5a)$ 得 $\mathcal LAu=0$ ✓。
**内在性**：由 $(\ast)$ 对 $v\in K$ 有 $\mathcal LAv=\Lambda\mathcal Lv$，故 $\Phi_K=\Lambda|_{\mathcal LK}$，
**与 $\Lambda$ 的选法无关**（专家 §2.2 的另一证）。
**判据**：$(5b)$ 失败 $\iff\exists\,0\ne w\in W_K:\ \Phi_K(w)\in\mathbb Cw$（$w=0$ 是永久核，须排除）。
**矩形铅笔**：$P_K(\lambda)=\lambda\iota_K-\Phi_K$，$\iota_K:W_K\hookrightarrow\mathbb C^q$。

**维数**：$\dim W_K=\dim K-\dim(K\cap\ker\mathcal L)$（专家给的 L6）。

**待定（专家留给我们的第一任务）**：
$$\boxed{\ \mathcal LK\overset{?}{=}\mathcal L(V\cap K)\ }$$
一般情形**不**由定义自动成立（$S=0$ 也不够）。若成立，可用 $W_0$ 作等价实现；若不成立，以 $W_K$ 为准。
专家明确：在这一点解决前，**不要**重跑依赖域定义的 Lean 定理。

**专家给的 Lean 里程碑（L1–L7）**：
L1 $(5a)\iff\exists(\Lambda,G_0,G_1)(\ast)$；L2 $\Phi_K$ 良定义；L3 $\Phi_K=\Lambda|_{\mathcal LK}$；
L4 $\ker Q(\lambda)$ 与部分特征向量（模永久核）对应；L5 $\mathcal LK=\mathcal L(V\cap K)$（或反例）；
L6 $\dim\mathcal LK=\dim K-\dim(K\cap\ker\mathcal L)$；L7 修正后矩形铅笔的行列式因子判据。

## Q1 的自答（待专家确认）：正确域应是 $W_K=\mathcal L\ker[C;CA]$

上一节把待确认问题写成"$W$ 还是 $W_0$"。推一遍失败判据后，两者都不对，正确的域是**整个核的像**：

$$W_K:=\mathcal L K,\qquad K=\ker[C;CA].$$

**推导**。$(5b)$ 失败 $\iff\exists\lambda$ 使 $\operatorname{rank}Q_{\mathcal L}(\lambda)<h$ $\iff$
$$\exists\lambda,\ \exists\,0\ne v:\quad (\lambda\mathcal L-\mathcal LA)v=0,\quad Cv=0,\quad CAv=0
\iff\exists\lambda,\ \exists\,0\ne v\in K:\ \mathcal LAv=\lambda\mathcal Lv .$$
注意 $v$ **不需要**属于 $V$——这是上一节两种读法都不对的原因。

**良定义性**：定义 $\Phi(w):=\mathcal LAv$（$w=\mathcal Lv$，$v\in K$）。若 $\mathcal Lv=0$ 且 $v\in K$，则
$v\in\ker[\mathcal L;CA;C]$，由 $(5a)$ 的转置形式 $\ker[\mathcal L;CA;C]\subseteq\ker(\mathcal LA)$ 得 $\mathcal LAv=0$ ✓。
所以 $\Phi:W_K\to\mathbb C^q$ 良定义，**且这一步用的正是 $(5a)$**。

**判据**：设 $w=\mathcal Lv$。若 $w=0$，则 $v$ 对**一切** $\lambda$ 都在核里，属永久核，不造成法秩以下的跌落，
必须排除。故
$$(5b)\ \text{失败}\iff\exists\,0\ne w\in W_K:\ \Phi(w)\in\mathbb C w .$$
等价地 $\Phi(w)=\Lambda w$（$\Lambda$ 由 $(\ast)$ 给出），与上一节的定义一致，只是在 $W_K$ 上。

**与 B.17 的关系**：$W_K$ 的维数与 $\overline N_{\mathcal Z}$ 的有效空间 $V/S$ 的维数（即 $\rho$）应当相同；
这一点需要按 $(5a)$ 与 $S=\mathcal V\cap\mathcal Z$ 的定义核一遍（未做）。

**状态**：这是本轮自答，**未经专家确认**；若确认，B.37 的四等价应把 $W$ 改为 $W_K$、$\iota:W_K\hookrightarrow\mathbb C^q$。
## 内蕴谱刻画（B.23 + B.24 合并视角）

把两条合起来看，失败判据可以写成**只依赖 $(K_1,W)$ 的内蕴形式**：

1. 由 B.23，$Q_{\mathcal L}(\lambda)=P(\lambda)H_0$，其中 $P(\lambda)=\begin{pmatrix}\lambda I_q-K_1&-K_2\\0&I_{r_1}\end{pmatrix}$，
   且 $\det P(\lambda)=\det(\lambda I_q-K_1)$；
2. 由 B.24，偏算子 $\Phi:W=\mathcal LV\to\mathbb C^q$ 良定义（只需 $(5a)$），且 $\Phi=K_1|_W$（因 $Bx=0$ 对 $x\in V$ 成立）。

因此
$$\boxed{(5b)\ \text{失败}\iff\exists\,0\ne w\in W:\ \Phi(w)\in\mathbb C\,w\ (\text{即 } \mathcal E_\Phi\ne\varnothing),}$$
其中 $\mathcal E_\Phi:=\{[w]\in\mathbb P(W):\ \Phi(w)\in\mathbb C w\}$；于是
$$(5b)\iff\mathcal E_\Phi=\varnothing .$$
注意 $\Phi:W\to\mathbb C^q$ **不是** $W$ 上的自同态，故不能称"$W$ 上的算子"；恰当的措辞是**部分特征向量条件**（partial eigenvector condition）。若引入扩张 $K_1$ 则 $\Phi(w)=K_1w\ (w\in W)$，但结论**不依赖**扩张的选法。

**与商铅笔的关系**：设 $\overline N_{\mathcal Z}(\lambda):V/S\to X/\mathcal Z$。则在 $(5a)$ 下有
$$(5b)\iff\ker\overline N_{\mathcal Z}(\lambda)=0\ \ \forall\lambda .$$
两条路线（$\Phi$ 的特征向量 / 商铅笔的逐点单射）描述的是**同一个障碍**：前者把障碍压到 $q$ 维的 $\mathbb C^q$ 上，
后者把它留在 $V/S$ 上；二者的等价由 $\Phi=K_1|_W$ 与 B.23 的因子化给出。

**为什么这是更好的形式**：不需要人为引入整空间的扩张 $\Lambda$（B.12 的 $\Lambda$ 只是 $\mathcal LA=\Lambda\mathcal L+\dots$
的一个解，不唯一），$\Phi$ 与 $W$ 都由 $\mathcal L$ 与 $(C,A)$ 内蕴地决定。

## 固定候选的多项式判据（专家第四轮 §5.2、§5.4）

设 $\iota:W\hookrightarrow\mathbb C^q$ 为包含，$\Phi:W\to\mathbb C^q$ 线性。则
$$(5b)\iff\operatorname{rank}(\lambda\iota-\Phi)=\rho\quad\forall\lambda\in\mathbb C
\iff\gcd\{\text{全部 } \rho\times\rho\text{ 极大子式 of }\lambda\iota-\Phi\}\in\mathbb C^\times .$$
这是**单参数**矩形铅笔，只需多项式 gcd，不需要特征向量枚举或数值搜索；
但"$R$ 自由"时 $\Phi=\Phi_R$ 随 $R$ 变化，$\gcd$ 非常数的条件变成**参数化**问题（仍开放）。

## 四等价（专家建议的中央定理形式）

$$(5b)\iff\text{商铅笔逐点满列秩}\iff\nexists\,0\ne w\in W:\Phi(w)\in\mathbb Cw
\iff\gcd\{\text{极大子式 of }\lambda\iota-\Phi\}\in\mathbb C^\times .$$
四种视角：原秩形式 / 商铅笔 / 部分特征向量 / 行列式因子。

**注意（专家第四轮 §8.2）**：$\det(\lambda I_q-K_1)$ 只在**满行秩的等号情形**（B.22 的假设 $h=q+r_1$）下直接对应失败；
一般情形必须用上面的部分特征向量/矩形铅笔判据，不能把该行列式当万能判据。
