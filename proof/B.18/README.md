# B.18 · $p=r=1$ 的结构

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.18` 条目（§0.1 归并表）。

## 命题

**B.18（a）〔原 B.18〕（$p=r=1$ 的结构与降维）** 设 $p=r=1$（$C=c^{\mathsf T}$、$L_0=\ell^{\mathsf T}$）且 $(c,A)$ 可观测。则

1. $r_1=\operatorname{rank}[c;cA]=2$（若 $=1$，则 $cA=\alpha c$，故 $cA^k=\alpha^kc$，观测性矩阵秩为 $1$，矛盾），
   $\dim V=\dim K=n-2$，$\dim(V\cap K)=\dim\ker\{c,cA,\ell\}\ge n-3$；
2. $s_0=\dim(\operatorname{row}[c;\ell]+W)\in\{2,3\}$，且 $s_0=3\iff\ell\notin\operatorname{span}\{c,cA\}$；
3. 因 $r_1+r=3$：若 $\ell\in\operatorname{span}\{c,cA\}$ 则 $s_0=2<3$，**该实例任何阶都无 Type I**（B.11c）；
4. **降维**：若 $\mathcal Z\subseteq V\cap K$（当 $d=n-1-q\le\dim(V\cap K)$，即 $q\ge2$ 时可行），则 $S=\mathcal Z$，
$$\rho=\dim(V/S)=\dim V-d=q-1,$$
故商铅笔 $\overline N_{\mathcal Z}$ 的尺寸为 $(q+1)\times(q-1)$——形状只由 $q$ 决定；$q=2$ 时为 $3\times1$（单列）。

## 纸面证明

*证明*：1. 见括号内论证；维数公式由 $\operatorname{rank}[c;cA]=2$、$\operatorname{rank}[c;\ell]=2$ 直接得到。
2. 两个二维行空间都含 $c$，故并维数 $\in\{2,3\}$，取 $3$ 当且仅当 $\ell\notin W$。3. $s_0<r_1+r$ ⟹ 由 B.11c，任何可容许增广都不是 Type I。
4. $\mathcal Z\subseteq V$ ⟹ $V\cap\mathcal Z=\mathcal Z$；再由 $\dim V=n-2$、$d=n-1-q$ 得 $\rho=q-1$；商铅笔的列数即 $\rho$、行数 $n-d=q+1$。$\square$


第 2 条的二分在 393 个可观测实例上均取 $s_0=3$（$\ell\notin W$ 一般成立））。
*注（负结果）*：$q=2$ 时 $d=n-3=\dim(V\cap K)$，故 $\mathcal Z=V\cap K$ 是 $V\cap K$ 内唯一的 $(n-3)$ 维子空间；
在 77 个可构造实例上它**全部不可容许**（$(5a)$ 失败）——所以 $q=2$ 的候选必须落在 $s<d$ 的层里。
*观察（2026-11-04 扫描，**未证**）*：$p=r=1$ 的阶差远大于 $p=r=2$ 的两个反例。随机 $n=4..7$ 的 881 个可观测实例中，
$q_0$、$q_0+1$、$q_0+2$ 三阶**都没有**找到可行增广（多数小阶连 $(5a)$-可容许候选都没有）；
由文献 $q_{\min}\le n-1$ 得 $q_{\min}-q_0\ge3$（$n=7$ 样本）。机制不是直和放大，而是
"$d$ 接近 $\dim K=n-2$ 时 $(5a)$ 几乎不可满足"。详见 `attempts/82`。
*意义*：把 $p=r=1$、$n$ 增长的问题压成"每阶一个 $(q+1)\times(q-1)$ 的小铅笔"，
是 Class I 分类的第一步（专家 15 号评审 §2.6）。

**B.18（b）〔原 B.18b〕（$p=r=1$ 时终阶必然可行：$q=n-1$）** 设 $p=r=1$（$C=c^{\mathsf T}$、$L_0=\ell^{\mathsf T}$）、$(c,A)$ 可观测，
取 $q=n-1$（即 $d=0$、$\mathcal Z=0$），$\mathcal L$ 为任一满足 $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ 且
$[c;\mathcal L]$ 可逆的 $(n-1)\times n$ 矩阵。则 $(5a)$ 与 $(5b)$ **都成立**。

*证明*：$(5b)$：由 B.13c，失败 $\iff\exists x\in V\setminus\{0\},\lambda:\ (\lambda I-A)x\in\mathcal Z=\{0\}$，
即 $x$ 是 $A$ 在 $V\subseteq\ker c$ 中的特征向量；而 $(c,A)$ 可观测意味着 $\ker c$ 内没有特征向量，矛盾。
$(5a)$：由 $[c;\mathcal L]$ 可逆得 $\operatorname{rank}[\mathcal L;CA;C]=n$，故
$\operatorname{rank}[\mathcal LA;\mathcal L;CA;C]\ge n$，又只有 $n$ 列，故 $=n$。$\square$


*意义*：这是"终阶可行"（文献的 $q_{\min}\le n_0-p$）在 $p=r=1$ 情形下的**本证明**，
与下面的扫描一起给出 $q_{\min}$ 的定量位置。

**B.18（c）〔原 B.18c〕（$p=r=1$ 的"坏像"落在超平面 $\ker c$ 内；$d=1$ 的判据是像的包含）** 设 $p=r=1$、$C=c^{\mathsf T}$，
$$\psi:V\times\mathbb C\to\mathbb C^n,\quad (x,\lambda)\mapsto(\lambda I-A)x,\qquad
\operatorname{im}\psi=\bigcup_{\lambda}(\lambda I-A)V .$$
则

1. **$\operatorname{im}\psi\subseteq\ker c$**（对 $x\in V$ 有 $cx=0$、$cAx=0$，故 $c(\lambda I-A)x=\lambda cx-cAx=0$）；
2. 对 $d=1$（$\mathcal Z=\langle z\rangle$，$z\in K\setminus0$）且 $z\notin V$：
$$(5b)\ \text{在}\ \mathcal Z\ \text{处失败}\iff z\in\operatorname{im}\psi;$$
3. 因此在 $d=1$ 上**整族不可行 $\iff K\setminus\{0\}\subseteq\operatorname{im}\psi$**。
而 $\dim\ker c=n-1$、$\dim K=n-2$、$\dim\operatorname{im}\psi\le n-2$，故
$$K\subseteq\operatorname{im}\psi\iff K\ \text{是}\ \operatorname{im}\psi\ \text{的一个不可约分支（维数相配）}.$$

*证明*：1 见括号。2：$\ker\overline N_{\mathcal Z}(\lambda)\ne0\iff\exists x\in V\setminus\langle z\rangle:\ (\lambda I-A)x\in\langle z\rangle$；
若 $(\lambda I-A)x=tz$ 且 $t\ne0$，则 $z=(\lambda I-A)(x/t)\in\operatorname{im}\psi$；反之若 $z\in(\lambda I-A)V$，
取原像 $x$，若 $x\in\langle z\rangle$ 则 $x=sz$ 给 $(\lambda I-A)z=(t/s)z$（$z$ 成为特征向量方向，另行排除），
否则即得失败。3 由 2 逐 $z$ 取全称。$\square$


$\mathcal Z=\langle z\rangle$ 候选：$(5a)$ 全部成立、$(5b)$ **全部失败**，与"$K\subseteq\operatorname{im}\psi$"一致）。
*核验（2026-11-05）*：精确判据（增广铅笔 $[\lambda B_V-AB_V\mid z]$ 的 $(d_V+1)$ 阶子式 gcd 有正次数）
上，$229/229$ 个 $(z,\mathcal Z=\langle z\rangle)$ 样本满足"$(5b)$ 失败 $\iff z\in\operatorname{im}\psi$"；
另在 240 个随机 $z\in K$ 上的列联表为：**可容许 $\wedge$ $z\in\operatorname{im}\psi$：239**、
不可容许 $\wedge$ 成员：1、**可容许 $\wedge$ 非成员：0** ⟹ $d=1$ 上没有可行候选。

**撤回（2026-11-05）**：曾猜 $\operatorname{im}\psi=\ker c$——**为假**。专家给出 $n=3$ 反例
（$A$ 为循环移位、$c=e_1^{\mathsf T}$、$\ell=e_2^{\mathsf T}$）：$V=K=\langle e_3\rangle$、$\ker c=\langle e_2,e_3\rangle$、
$\operatorname{im}\psi=\{0\}\cup\{ae_2+be_3:a\ne0\}$，故 $e_3\notin\operatorname{im}\psi$。已核验，见
proof/refuted/psi_image_ker_c.md。
同时更正两处：$\dim\operatorname{im}\psi\le(n-2)+1=n-1=\dim\ker c$（**不是** $n-2$）；
$d=1$ 的整族条件应是 $\mathbb P(K)\setminus\mathbb P(K\cap V)\subseteq\mathbb P(\operatorname{im}\psi)$
（只排除 $S=0$ 的那些直线），且 $(5a)$ 必须**另行**处理（该反例的 $q=1$ 唯一候选正是 $(5a)$ 失败）。
*注（实施陷阱）*：判断 $z\in\operatorname{im}\psi$ **不能**只在有理 $\lambda$ 上取样——坏 $\lambda$ 可为代数数
（本项目已两次踩到此坑）；必须用消元/结式或对全部代数 $\lambda$ 判定。

**B.18（d）〔原 B.18d〕（标准（循环）坐标下 $\operatorname{im}\psi$ 的精确刻画；专家 2026-11-05 §3 建议的目标）** 设 $p=r=1$、$(c,A)$ 可观测，
取循环基使 $c=e_1^{\mathsf T},cA=e_2^{\mathsf T},\dots,cA^{n-1}=e_n^{\mathsf T}$（于是 $A$ 呈伴矩阵形状：
$Ae_1=-a_0e_n$、$Ae_j=e_{j-1}-a_{j-1}e_n$），则 $V=\operatorname{span}\{e_3,\dots,e_n\}$ 且
$$(\lambda I-A)x=\Bigl(0,\ -x_3,\ \lambda x_3-x_4,\ \dots,\ \lambda x_{n-1}-x_n,\
\lambda x_n+\sum_{k\ge3}a_{k-1}x_k\Bigr).$$
对 $w\in\ker c$（坐标 $w=(0,w_2,\dots,w_n)$）令
$$x_3=-w_2,\qquad x_{k+1}=\lambda x_k-w_k\ (k=3,\dots,n-1),\qquad
P_w(\lambda)=\lambda x_n(\lambda)+\sum_{k\ge3}a_{k-1}x_k(\lambda)-w_n .$$
则
$$w\in\operatorname{im}\psi\iff P_w\ \text{不是非零常数}\qquad(P_w\equiv0\ \text{也算}).$$

*证明*：把 $x=\sum_{k\ge3}x_ke_k$ 代入坐标表达式，前 $n-1$ 个分量给出递归 $x_3=-w_2$、$x_{k+1}=\lambda x_k-w_k$，
最后一个分量给出一个方程 $P_w(\lambda)=0$。故 $w\in\operatorname{im}\psi\iff P_w$ 在 $\mathbb C$ 有零点；
而多项式在 $\mathbb C$ 上必有零点**除非**它是非零常数（$\equiv0$ 时任意 $\lambda$ 都是解）。$\square$

*推论*：$\operatorname{im}\psi$ 是 $\ker c$ 中的**稠密真子集**（被排除的是 $P_w$ 为非零常数的那些 $w$，一个非空代数集），
这解释了为什么随机采样（534/534）看不到它——稠密真子集不能靠采样发现。

实现中修过一个下标 off-by-one：$w_k$ 对应 `w[k-1]`）。

**B.18（e）〔原 B.18e〕（$d=1$ 的三分解：两半已证，第三半是猜想）** $p=r=1$、$q=n-2$（$d=1$）、$\mathcal Z=\langle z\rangle$，$0\ne z\in K$。

1. **（已证）$z\in V$ ⟹ 不可容许**。此时 $\mathcal Z\subseteq V$，故 $S=V\cap\mathcal Z=\mathcal Z$；
   由 B.16b 的 $(5a)\Rightarrow A(S)\subseteq\mathcal Z$ 得 $Az\in\langle z\rangle$，即 $z$ 是 $A$ 在 $V\subseteq\ker c$
   中的特征向量——与 $(c,A)$ 可观测矛盾。故**不存在**可容许的 $\mathcal L$ 使 $\ker[C;\mathcal L]=\langle z\rangle$。
2. **（已证）$z_2\ne0$（即 $z\notin V$，在标准坐标下）⟹ 可容许性自动成立**。
   因 $\dim\ker[C;\mathcal L]=1$ 得 $\operatorname{rank}[C;\mathcal L]=n-1$，故
   $\operatorname{rank}[\mathcal L;CA;C]\in\{n-1,n\}$。若 $=n-1$，则 $\operatorname{row}[C;\mathcal L]=\operatorname{row}[\mathcal L;CA;C]$
   （维数相同且前者包含于后者），于是 $cA\in\operatorname{row}[C;\mathcal L]$，从而对 $z\in\ker[C;\mathcal L]$ 有
   $cAz=0$；但在伴矩阵坐标下 $cAz=(Az)_1=z_2\ne0$，矛盾。故 $\operatorname{rank}[\mathcal L;CA;C]=n$，此时 $(5a)$ 自动成立
   （两边都等于 $n$）。
3. **（已证）$z_2\ne0\Rightarrow z\in\operatorname{im}\psi$**。证明：由 B.18d 的递归，
   $x_3=-z_2\ne0$ 且 $x_{k+1}=\lambda x_k-z_k$，故 $x_k$ 的次数**恰为** $k-3$、首项系数为 $-z_2\ne0$（归纳）；
   于是 $P_z=\lambda x_n+(\text{次数}\le n-3\text{ 的项})$ 的次数**恰为** $n-2\ge1$；
   而 $\mathbb C$ 上正次数多项式必有根（代数基本定理），故 $P_z$ 有零点，即 $z\in\operatorname{im}\psi$。
   由 1、2、3 得：**$d=1$ 阶的每个可容许候选都违反 $(5b)$**（$z\in V$ 者不可容许；$z\notin V$ 者可容许但谱上失败）——准确说法不是"每个 $K$ 中的直线都可容许"（$K\cap V$ 内的直线被第 1 条排除），也不是"整族 $\mathcal Z$ 都失败"；
   结合 B.18b 得 **$d\le1$ 的两个阶**各自的结论**（$d=0$ 可行、$d=1$ 必失败）。**注意（专家 2026-11-05 §6 的提醒，现已解决）**：$d\ge2$ 对应**更小的** $q$，不能由 $d\le1$ 直接推出 $q_{\min}$。这一点已由 **B.27** 补上：$1\le q\le n-2$ 时任何可容许 $\mathcal L$ 都失败 ⟹ 配合 B.18b 得 **$q_{\min}=n-1$（定理）**。

*证据（第 3 条）*：伴矩阵实例 $n=5,6,7$ 的 $821$ 个 $z\in K$（$z_2\ne0$）样本**全部**落在 $\operatorname{im}\psi$ 中；
同时 $z\in V$ 的 $77$ 个样本**全部**不可容许（与第 1 条一致）、$z_2\ne0$ 的 $821$ 个**全部**可容许（与第 2 条一致）。

`PsiImage.natDegree_X_mul_add_of_lt`、`PsiImage.exists_root_of_natDegree_eq_two`：递归次数恰为 $k$、
加低次项不改次数、$\mathbb C$ 上次数 $n-2$ 必有根），差在"$P_w$ 的显式组装"（纸面 + 精确验证 **412/412**：
$w_2\ne0$ 时 $\deg P_w=n-2$ 全部成立）。
*位置*：本文件 B.16b、B.18b、B.18c、B.18d；`attempts/84`、`attempts/85`；`tools/verification/class_I_d1.py`。

## Lean（2026-11-06 已同步登记）

* 内核：`RowSpaceLayer.finrank_range_prod_le`
* 均在 `tools/lean/MyProof/` 下，已登记进 `tools/lean/STATEMENT_MAP.md`；WSL 侧 `lake build MyProof` exit=0。
* 差异：矩阵实例化/行空间翻译与其余分部仍为纸面（详见 `## 状态与历史` 的等级行）。

## 精确验证

* 见等级行给出的精确验证数字。

## 状态与历史

*等级*：**[已证-纸面]** $+$ **[精确验证]**（第 4 条的 $\rho=q-1$ 在 **714/714** 个 $(n,q,\mathcal Z\subseteq V\cap K)$ 样本上成立；
*等级*：**[已证-纸面]** $+$ **[精确验证 589/589]**（$n=4..8$ 各约 120 个实例，$(5a)$ 与 $(5b)$ 全部成立）。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`Dims.b18c_annihilate`：第 1 条）（1、2、3 的结构部分）$+$ **[精确验证]**（在一个 $n=6$ 实例上 12 个随机
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`PsiImage.recX_natDegree_and_ne` 等三条） $+$ **[精确验证 300/300]**（伴矩阵实例 $n=4,5,6$ 上，公式刻画与精确 gcd 判据完全一致；
*等级*：三条均 **[已证-纸面]**；第 3 条的**内核**已 **[Lean-conditional]**（`PsiImage.recX_natDegree_and_ne`、
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。




## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 支撑目录

无（证据全部在本卷宗内）。
