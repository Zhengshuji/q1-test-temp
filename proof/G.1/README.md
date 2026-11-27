# G.1 · 判定问题的复杂度上界与编码

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `G.1` 条目（§0.1 归并表）。

## 命题

**G.1（a）〔原 G.1〕** $\mathrm{DEC}(q)\in\exists\mathbb R$（chart-free 编码；变量/方程 $O(n^3)$、次数 $\le n$、$O(n)$ 个 $s$ 分支）。
*证明要点*：$Z$-表述（无图卡析取）$+$ 核心引理 $\ker(CAZ)=Z\cap\mathcal V$（故 $(A)\iff A(S)\subseteq Z$）
$+$ 多项式左逆证书 $X(\lambda)P(\lambda)=I_t$（$\deg X\le t-1$）。
**等级**：[已证-纸面] $+$ 两实例精确验证 $+$ **部分 [Lean]**（`CoreLemma` 的核心引理、`ExistsRLemmas` 的左逆 $\Rightarrow$ 单射；$\exists\mathbb R$ 的**编码规模**不是 Lean 的对象）。
**完整证明**：[proof/dec_q_existsR/README.md](../dec_q_existsR/README.md)。

**编码为什么是多项式规模（2026-11-04 澄清，此前被我们自己的"更正"误伤）**：编码**不用**"列出全部极大子式"的
非结构化 Bézout $\sum u_im_i=1$（那个变体的规模是指数的：$N=\binom{n}{\rho}\binom{\rho+d}{\rho}$），而是
* **结构化左逆** $X(\lambda)P(\lambda)=I_t$（对 $X$ 的系数线性，未知数 $t^2q=O(n^3)$、次数 $\le t-1\le n$），
  次数界来自 Noferini–Van Dooren（LAA 658, 2023）Lemma 5.2 的右逆判据（转置使用），本文档已逐条核对条件；
* **退化层（$Z\cap\mathcal V=S\ne0$）**由**对 $s=\dim S$ 的 $O(n)$ 项析取**处理，并在商 $V/S$ 上做左逆——
  故不需要"一般秩的广义逆"或 Smith 酉模的次数控制。
⟹ **每个固定阶 $q$ 的 $\mathrm{DEC}(q)$ 都在 $\exists\mathbb R$**，且编码为多项式规模；这一点从未被推翻。
**注**：这是 $q1$ 的**上界**，不是答案；下界（$\exists\mathbb R$-hard）与多项式算法**均未知**。

**G.1（b）〔原 G.2〕（用可观性归约的**紧凑秩分层编码**；专家 2026-11-04 §4/§7 的 work package 2）** 固定阶 $q$。下列系统
（对 $s\in\{0,\dots,q\}$ 作**有限析取**）与"存在 $(5a)\wedge(5b)$ 的 $\mathcal L$"等价：

| 变量 | 尺寸 | 约束 |
|---|---|---|
| $\mathcal L$（或 $W$：$\mathcal Z=KW$）| $q\times n$（$W$：$k\times d$）| $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$；$Y_W W=I_d$；$\operatorname{rank}[C;\mathcal L]=p+q$（用 $\mathcal L$ 的行加 $C$ 的左逆证书）|
| $T$ | $q\times(q+2p)$ | $(5a)$：$\mathcal LA=T[\mathcal L;CA;C]$ |
| $\Lambda,G_0,G_1$ | $q\times q,\ q\times p,\ q\times p$ | $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ |
| $A,B$ | $q\times s,\ s\times d_V$ | $M:=\mathcal LV_0=AB$（$V_0$ 为 $V=\ker[C;CA]$ 的固定基）|
| $Y_A,Y_B$ | $s\times q,\ d_V\times s$ | $Y_AA=I_s$、$BY_B=I_s$（$\operatorname{rank}M=s$ 的证书）|
| $E$ | $(q-s)\times q$ | $EM=0$ |
| $Y_E$ | $q\times(q-s)$ | $EY_E=I_{q-s}$（$\operatorname{rank}E=q-s$ 的证书）|
| $E_0,\dots,E_{q-1}$ | $q\times(q-s)$ 各 | $E_0=E$、$E_{j+1}=E_j\Lambda$（**递推**，见下）|
| $Y_O$ | $q\times q(q-s)$ | $Y_O\widetilde{\mathcal O}=I_q$，$\widetilde{\mathcal O}=[E_0;E_1;\dots;E_{q-1}]$ |

**规模**：变量 $O(q^3+qn)$、约束 $O(q^3+qn)$、次数 $\le2$（全部线性/双线性）；析取 $q+1$ 项。
**必须用递推（专家 2026-11-04 §4.1 的更正）**：若直接展开 $\mathcal O=[E;E\Lambda;\dots;E\Lambda^{q-1}]$，
则 $E\Lambda^k$ 的条目次数是 $k+1$，**破坏"次数 $\le2$"**。改为引入辅助变量 $E_j$ 与双线性约束
$E_0=E$、$E_{j+1}=E_j\Lambda$，观测性矩阵用 $\widetilde{\mathcal O}$ 代替，则每条约束都是双线性的，
变量增加 $O(q^3)$ 而阶数不变。脚本已按递推实现并核验 $E_{j+1}=E_j\Lambda$ 与 $Y_O\widetilde{\mathcal O}=I_q$。

*必要性*：给定满足 $(5a)\wedge(5b)$ 的 $\mathcal L$——$T$ 由 $(5a)$ 存在；$\Lambda,G_0,G_1$ 由 $(5a)$ 的
行包含存在；$s=\operatorname{rank}M$、$A$ 取 $M$ 的 $s$ 个主元列、$B$ 取行最简形的 $s$ 行，则 $AB=M$；
$E$ 取 $\operatorname{im}M$ 的零化子则 $EM=0$、$\operatorname{rank}E=q-s$；$Y_O$ 存在由 B.12
（$(5b)\iff\operatorname{rank}\mathcal O=q$）。
*充分性*：由 $T$ 得 $(5a)$；由 $Y_W$ 得 $\dim\mathcal Z=d$；由 $EM=0$、$\operatorname{rank}E=q-s$、
$\operatorname{rank}M=s$ 得 $\ker E=\operatorname{im}M=\mathcal L(V)$；由 $Y_O\mathcal O=I_q$ 得
$\operatorname{rank}\mathcal O=q$ ⟹ $(E,\Lambda)$ 可观测 ⟹ 由 B.12 得 $(5b)$。$\square$

*等级*：**[已证-纸面]**（必要性 + 充分性如上一段）$+$ **[精确验证]**：`tools/verification/compact_obs_encoding.py`
在**两个已知可行见证**（C4 的 $q=4$ 见证、$n=5,p=2,r=1$ seed 3023 的 $q=2$ 见证）上**显式构造全部辅助变量**
并逐条核验 16 条约束（含 $Y_O\mathcal O=I_q$ 的数值验证），全部通过。
*注*：这是**编码**，不是算法；它把 $\exists\mathbb R$ 成员性做成"变量/约束多项式、次数 $\le2$"的形式，
* **规模记账（专家 2026-11-04 §4.2 的复杂度模型要求；脚本 `encoding_size_accounting.py`）**：
  模型为——输入有理、$\le B$ 比特；实数变量（复变量拆实/虚部，变量与约束各 $\times2$）；**位复杂度**；
  秩层析取**计入**规模（$\le(q+1)\times$单分支）。单分支在 $n=8,p=r=2,q=4,s=2$ 时为
  **变量 200 / 约束 208 / 次数 $\le2$**（含 $q+1=5$ 项析取：$\le1000$ / $\le1040$）；
  $n=12$ 时单分支约 570 / 515 ⟹ 均为 $O(q^3+qn)$，最大项来自 $E_j$ 递推与 $Y_O$（$q^2\cdot(q-s)$）。
  位长 $O(n^2(B+\log n))$（Hadamard + Cramer）。
与 G.1 的 Bézout 左逆编码相比更短（不需要 $t^2q$ 个左逆系数与 Noferini–Van Dooren 次数界）。
*位置*：本文件 B.12、G.1；专家 2026-11-04 §4/§7。
*位置*：本文件 B.10；[docs/08_results.md](../../docs/08_results.md) §4.11.1。

## 纸面证明

*（证明内联于下方等级行与支撑目录，未单独拆出）*

## Lean

* 无独立 Lean 内核（该条为纸面证明）。

## 精确验证

* 该条暂无独立精确验证脚本（纸面证明 + 支撑目录）。

## 状态与历史

* 等级：见 docs/02 同条目。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 支撑目录

[dec_q_existsR/](../dec_q_existsR/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（成立）

需显式写出：(i) 多项式左逆次数界的**定理依据**（不能只由 $P$ 次数为 1 推出）；(ii) 复变量到实变量的 **realification** 一步；(iii) 系数 bit-size 的多项式界。
