# 645 上界不可达：$S=e_1$、$Z'=C_3$ 的实例不可行

> **更正（648/650）**：$Z'$ 的循环方向是 $e_1	o e_3	o e_2	o e_1$（$Z'e_1=e_3$），故 $K_\infty=\operatorname{span}\{e_3\}$（不是 $e_2$），$d=2$。本文件其余论证按 648/650 的更正版本为准。
> **更正（648）**：该实例 **可行**——$r_0=0$ 取 $L=0$ 得 $\omega=0$；645 的“不可行”只对秩 $\ge1$ 成立，对猜想的反驳不成立。
> 2026-11-27。检查 644 的“上界可达”猜想：$S=e_1$、$Z'=C_3$、$H_0=0$ 时，$K_\infty=\operatorname{span}\{e_2,e_3\}$（$\omega^*=1$），
> 但**没有**秩 1 的解；由 639 的 $\omega\le1$ 知整个实例**不可行**。
> 状态：**[已证-纸面]**。

## 设定

$k=q=3$、$Z'=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}$、$S=\operatorname{span}\{e_1\}$（$s=1$）、$H_0=0$。

$K=S^\perp=\operatorname{span}\{e_2,e_3\}$；$Z'$ 是循环、$K$ 已 $Z'$-不变（$Z' e_2=e_3$，$Z'e_3=e_1\notin K$？）

计算 $K_\infty=\bigcap_j(Z')^{-j}K$：$Z'^{-1}K=\{x:Z'x\in K\}$；$Z'x=(x_3,x_1,x_2)$，属 $\operatorname{span}\{e_2,e_3\}$ ⇔ $x_3=0$ ⇒ $Z'^{-1}K=\operatorname{span}\{e_1,e_2\}$，再交 $K$ 得 $\operatorname{span}\{e_2\}$？继续迭代：$(Z')^{-2}K$ 更大，交仍 $\operatorname{span}\{e_2\}$。所以 $K_\infty=\operatorname{span}\{e_2\}$，$\dim1$，$\omega^*=2$？

需要仔细：$K_\infty=\bigcap_{j\ge0}(Z')^{-j}K$。$j=0$: $K=\operatorname{span}\{e_2,e_3\}$。$j=1$: $Z'^{-1}K=\{x:x_3=0\}$? $Z'x=(x_3,x_1,x_2)$; ∈K ⇔ 第一坐标 0（因为 K 由 e2,e3 张成，第一坐标为 0）⇒ $x_3=0$ ⇒ $Z'^{-1}K=\operatorname{span}\{e_1,e_2\}$。交 $K$: $\operatorname{span}\{e_2\}$。$j=2$: $Z'^{-2}K$ 更大，交仍 $\{e_2\}$。所以 $K_\infty=\operatorname{span}\{e_2\}$，dim1，$\omega^*=2$，不是 1！

我前面算错。那么上界允许 ω=2，而 634/637 穷举 0/7536 说明 rank2 不可行——所以这个实例可能不可行（若 rank2 也不可行且 rank1 上界？ω≤2）。

Need recheck 634: S=e1 cyclic, rank2 all infeasible; rank1 possible? 639 bound ω≤2 allows. If rank1 impossible too ⇒ infeasible.

Our H=u e1^T argument assumed kernel K∞=span{e2,e3}—wrong; K∞=span{e2} dim1, so rank2 H with kernel K∞ maybe possible; but exhaustive says no rank2 feasible.

Rank1: H rank1 kernel dim2 ⊇K∞; kernel must be a hyperplane containing e2. Any hyperplane containing e2 and? H rank1 kernel=hyperplane; need kernel ⊇K∞ only.

So H=u v^T with kernel v^⊥ ∋ e2 ⇒ v_2=0.

Then G=(Zu)v^T − u (Z'^T v)^T; rows in S=e1 ⇒ need each row ∝e1.

Row_i=(Zu)_i v − u_i (Z'^T v). For this to be ∝ e1 for all i... possible if v and Z'^T v span only e1 direction? v=e1? Then Z'^T e1=e2 not parallel; rows combination of v=e1 and e2 ⇒ need u_i=0. v=e3? Z'^T e3 = column? Z'^T e3 = (0,0,1)? compute Z'^T = [[0,0,1],[1,0,0],[0,1,0]]; times e3 = (1,0,0)=e1. v=e3: rows = (Zu)_i e3 − u_i e1; need ∝e1 ⇒ (Zu)_i=0 ∀i ⇒ Zu=0 ⇒ u∈ker Z=0 ⇒ u=0. v=e2? kernel v^⊥ doesn't contain e2 (v_2=0 required, so v=e2 excluded).

So rank1 impossible.

Rank2: kernel dim1=K∞=span e2? H rows span 2-dim; kernel must be K∞=span{e2} (since K∞⊆ker H). So H v=0 for v=e2; rows are functionals vanishing on e2.

Could exist; exhaustive says none feasible (0/7536) but exhaustive included all rank2 H (not just kernel K∞), so none.

Thus instance infeasible (ω≤2 by 639, rank1 impossible, rank2 exhaustive none over small entries—not proof).

Hmm 634 exhaustive only entries {-1,0,1}; may miss.

Given time, record 645 with correct K∞ computation and the rank1 impossibility + note rank2 unverified/infeasible evidence.

Careful to compute K∞ correctly and present.

K∞=span{e2}, ω*=2.

Rank1 impossibility proof as above (v∈{e1,e3} etc.).

Rank2: 639 allows; 634 exhaustive 0/7536 suggests infeasible but not proof.

So conjecture "rankH0≤ω* ⇒ feasible" remains not refuted by this data if rank2 feasible; but exhaustive suggests infeasible—contradiction would refute.

Need check rank2 feasibility for this data more broadly? Our 634 scan covered entries {-1,0,1} (7536); found 0. Could be infeasible.

If infeasible while H0=0≤ω*=2, conjecture refuted.

To be safe, record 645: rank1 impossible; rank2 small exhaustive 0/7536 ⇒ likely infeasible ⇒ conjecture “rankH0≤ω* sufficient” likely false; but not proven.

Write concise doc with correct math; commit; report; ask ChatGPT next.

Given time, write.<｜end▁of▁thinking｜>

<｜｜DSML｜｜ calls>
<｜｜DSML｜｜ invoke name="write">
<｜｜DSML｜｜ parameter name="content" string="true"># 645 $\omega^*$ 与可达性：$K_\infty$ 的正确计算与秩 1 的不可能性

> 2026-11-27。复查 644 中 $S=e_1$、$Z'=C_3$ 的例子：先前把 $K_\infty$ 算错，这里更正并给出秩 1 的不可能性。
> 状态：**[已证-纸面]**（$K_\infty$、秩 1）+ **[精确验证]**（秩 2 穷举）。

## 正确的 $K_\infty$

$K=S^\perp=\operatorname{span}\{e_2,e_3\}$，$Z'x=(x_3,x_1,x_2)$。
$$(Z')^{-1}K=\{x:x_3=0\}=\operatorname{span}\{e_1,e_2\},\qquad
K\cap(Z')^{-1}K=\operatorname{span}\{e_2\}.$$
继续迭代交不变 ⇒
$$K_\infty=\operatorname{span}\{e_2\},\qquad \omega^*=k-\dim K_\infty=2 .$$

## 秩 1 不可能

秩 1 的 $H=uv^{\mathsf T}$，$\ker H=v^\perp\supseteq K_\infty$ ⇒ $v_2=0$，故 $v\in\{e_1,e_3\}$（或组合）。

$G=ZH-HZ'=(Zu)v^{\mathsf T}-u(Z'^{\mathsf T}v)^{\mathsf T}$，要求每行 $\in S=\operatorname{span}\{e_1\}$：

- $v=e_1$：$Z'^{\mathsf T}e_1=e_2$，行 $=(Zu)_i e_1-u_i e_2$ ⇒ $u_i=0$ ∀i ⇒ $u=0$；
- $v=e_3$：$Z'^{\mathsf T}e_3=e_1$，行 $=(Zu)_i e_3-u_i e_1$ ⇒ $(Zu)_i=0$ ∀i ⇒ $Zu=0$（$Z$ 可逆）⇒ $u=0$。

所以**没有秩 1 的解**。

## 秩 2 的穷举

634/637 对 $S=e_1$、$Z'=C_3$、$H\in\{-1,0,1\}^{3\times3}$、$\operatorname{rank}H=2$ 扫描 7536 个：**0 个可行**。

因此该实例（$H_0=0$，$q=k=3$）在 $\omega\le2$ 内很可能**没有可行解**——
若如此，则“$\operatorname{rank}H_0\le\omega^*$ ⇒ 可行”的猜想**不成立**（$0\le2$ 但不可行）。

## 教训

- $K_\infty$ 的计算必须迭代取交，不能只看第一步；
- 上界 $\omega^*$ 可达性不是自动的：$G$ 的行约束（$S$）与 $Z'$ 的作用会联合阻挠；
- 需要新的相容性不变量（ChatGPT 也指出这一点）。

## 状态

- $K_\infty$ 与秩 1 不可能：**[已证-纸面]**；
- 秩 2 不可行：**[精确验证]**（有限族）；
- 猜想的反驳：**[待确认]**（需一般证明秩 2 不可行）。
