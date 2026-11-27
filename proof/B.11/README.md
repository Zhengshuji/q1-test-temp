# B.11 · Type I/II 的几何形式

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.11` 条目（§0.1 归并表）。

## 命题

**B.11（a）〔原 B.11〕（$h$ 的几何公式）** 设 $\mathcal L$ 行满秩、$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$，
$\mathcal Z=\ker[C;\mathcal L]$、$W=\operatorname{row}[C;CA]$。则
$$h=\operatorname{rank}[\mathcal L;CA;C]=\dim(\mathcal Z^{\perp}+W),$$
且 $h=q+r_1-\delta$，$\delta=\dim(\mathcal Z^{\perp}\cap W)-p\ge0$。

## 纸面证明

*证明*：$\operatorname{row}\mathcal L+W=\mathcal Z^{\perp}+W$（$\operatorname{row}[C;\mathcal L]=\mathcal Z^{\perp}$ 且 $\operatorname{row}C\subseteq W$）。$\square$

*推论*：$(5b)\Rightarrow\delta\ge1\iff\mathcal Z^{\perp}\cap W\supsetneq\operatorname{row}C\iff\exists w\in W\setminus\operatorname{row}C$ 使 $\mathcal Z\subseteq\ker(w^{\mathsf T})$；
若 $q+r_1>n$ 则整数障碍自动不触发。

*位置*：[proof/h_formula](../h_formula/README.md)。

**B.11（b）〔原 B.11b〕（Type I 的几何形式）** 记 $R=\operatorname{row}\mathcal L$、$\pi:\mathbb C^n\to\mathbb C^n/\operatorname{row}C$ 为商映射。则
$$h=q+r_1-\dim\bigl(\pi(R)\cap\pi(W)\bigr),$$
因此
$$\text{Type I}\ (h\ge q+r_1)\iff \pi(R)\cap\pi(W)=0\quad(\text{"}R\text{ 模 }C\text{ 避开 }W\text{"}).$$
*证明*：$\mathcal Z^\perp=\operatorname{row}[C;\mathcal L]=C+R$（$C=\operatorname{row}C$），故
$\dim(\mathcal Z^\perp\cap W)=\dim((C+R)\cap W)=\dim(W\cap C)+\dim(\pi(R)\cap\pi(W))$；代入 B.11 的 $h=q+r_1-\delta$、$\delta=\dim(\mathcal Z^\perp\cap W)-p$ 并用 $p=\dim C$、$\dim(W\cap C)=p-\dim\pi(W)$ 即得。$\square$
*推论（可判的二分）*：设 $w=\dim\pi(W)$、$\dim(\mathbb C^n/C)=n-p$。若 $q+w>n-p$，则**任何** $R$ 都与 $\pi(W)$ 相交，Type I 在该阶**不可能发生**；若 $q+w\le n-p$，则"避开"是 $\\operatorname{Gr}(q,\mathbb C^n/C)$ 中的**开稠**条件，Type I 是该阶的**一般情形**——要它不发生，必须靠 $(5a)$ 把可容许簇整个压进 incidence 子簇（这正是 incidence/occlusion 现象）。

*位置*：本文件 B.11；[workspace/q1_false/feasibility_geometry/attempts/57_gap_arithmetic.md](../../workspace/q1_false/feasibility_geometry/attempts/57_gap_arithmetic.md)。

**B.11（c）〔原 B.11c〕（$h$ 的**无条件**线性公式；取代原来依赖未定义 $V'$ 的"整族一致"）** 设 $\mathcal L$ 行满秩、
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$，记 $R=\operatorname{row}\mathcal L$、
$C=\operatorname{row}C$、$W=\operatorname{row}[C;CA]$、$S=\operatorname{row}[C;L_0]+W=\operatorname{row}[C;L_0;CA]$、
$s_0=\dim S$。则
$$\boxed{\,h=s_0+q-\dim(R\cap S)\,},\qquad\text{从而}\quad h\le s_0+q-r .$$
且 Type I（$h\ge q+r_1$）$\iff\dim(R\cap S)\le s_0-r_1$。
*证明*：$\mathcal Z^\perp=C\oplus R$（因 $\operatorname{rank}[C;\mathcal L]=p+q$）。由 $\operatorname{row}L_0\subseteq R\subseteq
\mathcal Z^\perp$ 得 $\mathcal Z^\perp+S=\mathcal Z^\perp+W$，故 $h=\dim(\mathcal Z^\perp+S)
=(p+q)+s_0-\dim(\mathcal Z^\perp\cap S)$。又 $C\subseteq S$、$C\cap R=0$，故
$\mathcal Z^\perp\cap S=(C\oplus R)\cap S=C\oplus(R\cap S)$，即 $\dim(\mathcal Z^\perp\cap S)=p+\dim(R\cap S)$。
代入得 $h=q+s_0-\dim(R\cap S)$。再由 $\operatorname{row}L_0\subseteq R\cap S$（$\operatorname{row}L_0\subseteq R$ 且
$\subseteq S$）得 $\dim(R\cap S)\ge r$，故 $h\le s_0+q-r$。$\square$
*推论 1（$s_0$ 的上界）*：$s_0=\dim(\operatorname{row}[C;L_0]+W)=(p+r)+r_1-\dim(\operatorname{row}[C;L_0]\cap W)$，
而 $\operatorname{row}C\subseteq\operatorname{row}[C;L_0]\cap W$，故 $s_0\le r_1+r$。
*推论 2（**无条件**排除计数障碍）*：若 $s_0<r_1+r$，则对**任何** $\mathcal L$ 都有
$h\le s_0+q-r<q+r_1$，即**不存在** Type I——计数障碍在该阶不可能触发，与 $\mathcal L$ 无关。
*推论 3（Type I 的唯一可能情形）*：由推论 1–2，Type I 只在 $s_0=r_1+r$ 时可能，此时
$\text{Type I}\iff\dim(R\cap S)=r\iff R\cap S=\operatorname{row}L_0$（等价地 $R\cap W=0$，即 B.11b）。

$\dim(\mathcal Z^\perp\cap S)=p+r$）$+$ **[精确验证]（$s_0<r_1+r$ 的 39 个样本中 Type I 出现 0 次）**。
*位置*：本文件 B.11、B.11b；[docs/08_results.md](../../docs/08_results.md) §3（3.1–3.3 已按本条重写）。

**B.11（d）〔原 B.11d〕（"计数-谱分离"下的可解性归约；专家 2026-11-04 §Q2 建议的形式）** 称实例满足
**计数-谱分离（CSS）**，若对每个可容许阶 $q$：每个满足 $(5a)$ 且 $h<q+r_1$ 的增广**也**满足 $(5b)$（即无 Type III）。
则在 CSS 下，对每个 $q$
$$\exists\mathcal L:\ (5a)\wedge(5b)\ \iff\ \exists\mathcal L:\ (5a)\wedge h<q+r_1 ,$$
（等号情形 $h=q+r_1$ 已由 **B.22** 关闭：该情形下 $(5b)$ 必失败，故不可作为可行见证。）
*证明*：$\Rightarrow$ 由 B.9b；$\Leftarrow$ 即 CSS。$\square$
**推论**：若**在指定输入类上**"存在 $(5a)$ 且 $h<q+r_1$ 的增广"可多项式时间判定，则该类上 $q_{\min}$
可多项式时间计算（逐阶 $O(n)$ 次调用；每候选的谱检验由 B.12 为多项式）。
**注意（必须一起读）**：两个前提都不可省：(i) CSS 是结构假设，C4 是它的反例；
(ii) 那个存在性判定在 $(5a)$ 限制可容许行空间时**不是自动的**（专家原话）——只有 $(5a)$ 自动成立（如 $h=n$，见 3.4）
时才退化为 Grassmannian 上的秩计算。
*注（等号情形 $h=q+r_1$，2026-11-05 按专家评审修订，**现已关闭**）*：$Q_{\mathcal L}$ 只有 $q+r_1$ 行，故
$\operatorname{rank}Q_{\mathcal L}(\lambda)\le q+r_1$。
* $h>q+r_1$：$(5b)$ **不可能**（行数界）✓；
* $h=q+r_1$：**由 B.22，$(5b)$ 必失败**（专家给出的块因子化证明：$Q$ 秩 $=$ 方块 $\begin{bmatrix}\lambda I_q-K_1&-K_2\\0&I\end{bmatrix}$ 的秩，
  其行列式为 $q$ 次首一多项式，$q\ge1$ 时必有根）✓。
故 $h\ge q+r_1\Rightarrow(5b)$ 失败，CSS 归约（本命题）**不再需要附加条件**。

## Lean

* 等级行引用的 Lean 声明：`TypeIGeom.B11_dim`、`TypeIGeom.mkQ_map_inf_eq`、`TypeIGeom.typeI_dim`、`TypeIGeom.typeI_geometric`、`Dims.b11c_modular`、`Dims.b11c_add`、`Logic.b11d_css`、`Logic.typeI_kills`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 见等级行给出的精确验证数字。

## 状态与历史

*等级*：**[已证-纸面]** + **[Lean]**（`TypeIGeom.B11_dim`：$\dim((C\sqcup R)\sqcup W)+(\dim((C\sqcup R)\sqcap W)-\dim C)=\dim R+\dim W$；**差异**：$\delta$ 写成维数差，非负性由 $C\le(C\sqcup R)\sqcap W$ 保证）$+$ **[精确验证 240/240]**。
*等级*：**[已证-纸面]** + **[Lean]**（`TypeIGeom.mkQ_map_inf_eq`：$\pi((C\sqcup R)\sqcap W)=\pi R\sqcap\pi W$；`TypeIGeom.typeI_dim`：维数形式；`TypeIGeom.typeI_geometric`：$\dim((C\sqcup R)\sqcup W)+\dim(\pi R\sqcap\pi W)=\dim R+\dim W$。**差异**：写成等式而非"$\iff$"，"$h\ge q+r_1\iff\pi R\sqcap\pi W=0$"由等式直接读出）$+$ **[精确验证 21/21]**（恒等式 $h=q+r_1-\dim(\pi(R)\cap\pi(W))$ 无违例）。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`Dims.b11c_modular`、`Dims.b11c_add`） + **[精确验证 35/35]**（公式）$+$ **[精确验证 54/54]**（不等式与等号判据
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`Logic.b11d_css` 逻辑骨架、`Logic.typeI_kills` 算术内核）（初等逻辑 + B.9b + B.12）。
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

## 专家复核意见（成立）

Type I 的二分只是**数值**分类，不覆盖子空间相对位置的全部几何型（$L_0$ 是否在 $W$ 内、$R$ 与 $W$ 的交、$\delta$ 的取值）；不要声称它穷尽所有几何型。
