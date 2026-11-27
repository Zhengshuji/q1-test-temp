# B.9 · 边界与等号结构

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.9` 条目（§0.1 归并表）。

## 命题

**B.9（a）〔原 B.9〕（必要条件 $h<q+r_1$）** 设 $\mathcal L$ 行满秩、含 $L_0\ne0$，$h=\operatorname{rank}[\mathcal L;CA;C]$、$r_1=\operatorname{rank}[C;CA]$、$s=\operatorname{rank}\mathcal L$。则 $Q_{\mathcal L}=[\lambda\mathcal L-\mathcal LA;CA;C]$ 有 $2p-r_1$ 个零左指标，非零左指标个数为 $q+r_1-h$；因此
$$(5b)\ \Longrightarrow\ h<q+r_1 .$$

## 纸面证明

*证明*（**2026-11-04 按专家审阅意见补全"常值向量 ↔ 零指标"这一步**）：

1. **左零模的秩**：$m:=q+2p$ 行。左零模是 $Q_{\mathcal L}:\mathbb C[\lambda]^m\to\mathbb C[\lambda]^n$ 的核；
   核在 PID $\mathbb C[\lambda]$ 上**自由**，其秩 $=$ 分数域 $\mathbb C(\lambda)$ 上左核的维数 $=m-h$。
   故左最小指标（按重数）共 $q+2p-h$ 个。
2. **零指标的个数 $=$ 常值左零向量的维数**：取左零模的**约化最小基**（reduced minimal basis）$(b_1,\dots,b_k)$，
   其次数即最小指标。约化最小基的 predictable-degree 性质给出：常值元素只能是**零次基向量的常系数组合**。
   因此常值左零空间的维数 $=$ 零指标的个数。
3. **常值左零向量的计算**：$\varphi=(\varphi_1,\varphi_2,\varphi_3)$ 常值且 $\varphi^{\mathsf T}Q_{\mathcal L}(\lambda)=0$
   $\iff$ $\varphi_1\mathcal L=0$ 且 $-\varphi_1\mathcal LA+\varphi_2CA+\varphi_3C=0$。
   $\mathcal L$ 行满秩 ⟹ $\varphi_1=0$；余下 $(\varphi_2,\varphi_3)\in\ker_{\rm left}[CA;C]$，维数 $2p-r_1$。
   故零指标恰 $2p-r_1$ 个。
4. **非零指标个数** $=(q+2p-h)-(2p-r_1)=q+r_1-h$。一致性检查：$h\ge r_1$（行堆叠）与
   $h\le q+r_1$（$(5a)$ 给 $\operatorname{row}\mathcal LA\subseteq\operatorname{row}H$），故该数非负。
5. **两种情形必须分开（2026-11-05 按专家 §Q1(a)/§Q3 修订）**：
   * $h>q+r_1$：无非零左指标，$\sum\varepsilon=0$；而行数给出 $\operatorname{rank}Q_{\mathcal L}(\lambda)\le q+r_1<h$，
     故 $(5b)$ 不可能 ✓（**不需要** B.8）。
   * $h=q+r_1$：仍无非零左指标（$\sum\varepsilon=0$），但行数界退化为 $\operatorname{rank}Q\le h$，**不能**排除 $(5b)$。
     在**正确**的 Kronecker 恒等式 $h=\sum\varepsilon+\sum\eta+d_{\rm fin}+d_\infty$（B.8b）下只能推出
     $\sum_j\eta_j+d_{\rm fin}+d_\infty=h>0$——这只在额外假设 $\sum_j\eta_j+d_\infty=0$ 时才给出 $d_{\rm fin}>0$。
     **等号情形已由 B.22 关闭**（$h=q+r_1$, $q\ge1$ ⟹ $(5b)$ 必失败）；精确证据为 $22\,877$ 个
     （`tools/verification/equality_case.py`），但这不是证明。$\square$

*位置*：[proof/left_index_count](../left_index_count/README.md)。

**B.9（b）〔原 B.9b〕（"Type II" 是空类）** 在 B.9 的同一假设下，令 $k=q+r_1-h$（非零左指标个数）、$s=\operatorname{rank}\mathcal L$。则
$$k\le s\quad\text{恒成立；}\qquad\text{因此条件 }k>s\ \text{（"Type II"）永不可能发生。}$$
*证明*：一方面 $[\mathcal L;CA;C]$ 是 $[CA;C]$ 的**行堆叠超矩阵**，故 $h=\operatorname{rank}[\mathcal L;CA;C]\ge\operatorname{rank}[CA;C]=r_1$；于是 $k=q+r_1-h\le q$。另一方面 $\operatorname{rank}[C;\mathcal L]=p+q$（$C$ 与 $\mathcal L$ 行不交）蕴含 $\operatorname{rank}\mathcal L=q=s$。故 $k\le q=s$。$\square$
*推论*：$q_0$ 阶（或任意阶）的 $(5b)$ 失败**只有两类**：$h\ge q+r_1$（Type I，纯计数）与 $h<q+r_1$ 但 $d_{\rm fin}>0$（Type III，谱/几何）。专家原分类中的"计数不足"一类是空的，不需检查。

*位置*：[workspace/q1_false/feasibility_geometry/attempts/08_failure_types.md](../../workspace/q1_false/feasibility_geometry/attempts/08_failure_types.md)。

**B.9（c）〔原 B.19〕（顶层与等号互斥：$V\subseteq\mathcal Z$ 时 $h<q+r_1$）** 设 $q\ge1$、$\mathcal L$ 可容许、$\mathcal Z=\ker[C;\mathcal L]$、
$V=\ker[C;CA]$、$h=\operatorname{rank}[\mathcal L;CA;C]$。若 $V\subseteq\mathcal Z$ 则 $h<q+r_1$。

*证明（专家 2026-11-05 §Part III.1 的短证明）*：$V\subseteq\mathcal Z$ ⟹ $S=V\cap\mathcal Z=V$；由 B.21 的 $s=n-h$ 得
$n-h=\dim V=n-r_1$，故 $h=r_1<q+r_1$（$q\ge1$）。$\square$

*备注*：原证明走 B.11c 的 Type I 判据（$V\subseteq\mathcal Z\Rightarrow R\subseteq V^\perp=W\Rightarrow R\cap W=R\ne0\Rightarrow h<q+r_1$），
也正确；上面这条更短且更几何（$V\subseteq\mathcal Z$ 意味着商定义域为零，即"自动可行"，而它严格发生在等号之下）。


**B.9（d）〔原 B.20〕（等号情形的结构记账）** 设 $\mathcal L$ 可容许、$h=q+r_1$（等号）、$C\ne0$（$p\ge1$）、
$Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$（$q+2p$ 行、$n$ 列）、$S=V\cap\mathcal Z$。则

1. **常值右零空间恰是 $S$**：$\{v:\ Q_{\mathcal L}(\lambda)v=0\ \ \forall\lambda\}=S$，且 $\dim S=s$。
   故 Kronecker 形中**零次右最小指标的个数**为 $s$。
2. **$W\cap\mathcal Z^\perp=C$**：由 $h=\dim(\mathcal Z^\perp+W)=p+q+r_1-\dim(\mathcal Z^\perp\cap W)$ 与 $h=q+r_1$ 得
   $\dim(\mathcal Z^\perp\cap W)=p$；又 $C\subseteq W\cap\mathcal Z^\perp$ 且 $\dim C=p$，故相等。
3. 由 B.11c 的 Type I 判据，等号时还有 $R\cap W=0$、$s_0=r_1+r$、$R\cap S=\operatorname{row}L_0$。

*证明*：1. 由 $CAv=0$ 与 $Cv=0$ 得 $v\in V$；再由 $\lambda\mathcal Lv-\mathcal LAv=0$ 对一切 $\lambda$ 得
$\mathcal Lv=0$ 与 $\mathcal LAv=0$，故 $v\in V\cap\ker\mathcal L=S$；反向显然（$C,\mathcal L$ 在 $S$ 上为零且 $A(S)\subseteq\mathcal Z$，
后者用 B.16b）。2. 见文中推导。3. 即 B.11c。$\square$

*意义*：等号情形的 Kronecker 记账现在有了可用的锚点：
$$h=\sum_i\varepsilon_i+\sum_j\eta_j+d_{\rm fin}+d_\infty,\qquad
\#\{\text{左指标}\}=2p-r_1\ (\text{等号时全为零次}),\qquad
\#\{\text{零次右指标}\}=s .$$
故等号时 $d_{\rm fin}+d_\infty=q+r_1-\sum_j\eta_j$，**失败（$d_{\rm fin}>0$）等价于 $\sum_j\eta_j+d_\infty<q+r_1$**。
把这个不等式证明出来就是等号排除定理；目前只有精确证据（26\,822 个等号样本全部失败）。

## Lean（2026-11-06 已同步登记）

**[Lean-conditional]** —— 内核只覆盖代数/维数骨架，矩阵实例化与其余分部为纸面。

* 内核：`RowSpaceLayer.finrank_sup_lt_of_inf_ne_bot`、`inf_bot_of_finrank_sup_eq`；字面矩阵层 `MatrixBridge.rank_fromRows_lt_of_inf_ne_bot`、`inf_bot_of_rank_fromRows_eq`
* 均在 `tools/lean/MyProof/` 下，已登记进 `tools/lean/STATEMENT_MAP.md`；WSL 侧 `lake build MyProof` exit=0。
* 差异：矩阵实例化/行空间翻译与其余分部仍为纸面（详见 `## 状态与历史` 的等级行）。

## 精确验证

* `tools/verification/failure_types.py`

## 状态与历史

*等级*：$h>q+r_1$ 半 **[已证-纸面]**；$h=q+r_1$ 半 **[已证-纸面]**（由 B.22）。$+$ **[精确验证 56/56]**、**[精确验证 698/698]**、**[精确验证 22877/22877]（等号处全部失败）**。
*等级*：**[已证-纸面]** + **[Lean]**（`TypeII.typeII_rank_mono`：$\dim J\le\dim(V\sqcup J)$；`TypeII.typeII_vacuous`：$s=q$ 与 $r_1\le h$ 之下 $\neg(s<q+r_1-h)$；`TypeII.typeII_vacuous_geometric`：维数版。**差异**：$h\ge r_1$ 与 $s=q$ 作为假设给入——前者由 `typeII_rank_mono` 提供，后者即 $\operatorname{rank}\mathcal L=q$）$+$ **[精确验证 93/93]**（$k>s$ 的违例 0；`tools/verification/failure_types.py` 的分类计数中 Type II 恒为 0）。
*等级*：**[已证-纸面]**。
*等级*：**[已证-纸面]**（1、2、3 都只是秩/核的直接计算）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。






## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F3 |
| 导出等级 | **L4** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（字面） |


## 支撑目录

[h_formula/](../h_formula/README.md)、[h_bound/](../h_bound/README.md)、[l0_reduction/](../l0_reduction/README.md)、[fernando_2gap/](../fernando_2gap/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（成立）

真正本质的假设是 $q\ge1$；$L_0\ne0$（配 $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$）只是保证 $q\ge1$ 的一种方式。
