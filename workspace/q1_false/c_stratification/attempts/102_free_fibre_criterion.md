# 自由区的充要判据（$q=3,\omega=2$）

> 2026-11-08。落实专家 49 号答复 §7 的 Priority B。工具：`tools/verification/free_fibre_criterion_check.py`。
> 状态：**M2**（纸面证明 + 1200 例机器核验；充分性的"一般选择"论证待复核）。

## 目标

在自由区（$\ker T=0$，即 $K\cap A^{-1}K=0$，底部行完全自由）给出 $q=3,\omega=2$ 的**充要判据**，
形式按专家要求：只依赖固定的顶块 $U_0=L_0N_K$、$V_0=L_0AN_K$ 与自由行数 $m=q-r$。

## 设想与理由

1. 自由区里底部行 $(B_1,B_2)$ 自由（专家 40 号定理：$\Theta$ 满射 $\iff\ker T=0$）；
2. 于是问题是一个**矩阵补全**：$H=[U_0;B_1]$、$H_A=[V_0;B_2]$，要 $\operatorname{rank}H=2$、
   $\ker H\subseteq\ker H_A$、铅笔 $\lambda H-H_A$ 好；
3. 在 $S=\operatorname{row}H$ 的坐标里，铅笔是 $3\times2$：$r$ 个固定行 $a_j(\lambda)=\lambda u_j-v_j$，
   $m$ 个自由行 $b_i(\lambda)=\lambda x_i-y_i$；问题变成"自由行能否把铅笔补成对所有 $\lambda$ 满列秩"；
4. 关键量不是 $\dim(E+F_0)$，而是**固定铅笔 $A(\lambda)=\lambda U_0-V_0$ 的法秩** $\rho$（见下"更正"）。

## 做法

**记号**：$E=\operatorname{row}(U_0)$、$F_0=\operatorname{row}(V_0)$、$m=3-r$、$\rho=\operatorname{nrank}_{\mathbb C(\lambda)}(\lambda U_0-V_0)$。

**定理（自由区判据）**：设 $\ker T=0$、$\operatorname{rank}L_0=r$，$k\ge2$。则 $q=3,\omega=2$ 可行 $\iff$

1. $\dim(E+F_0)\le2$；
2. $m\ge2-\dim E$；
3. 且满足以下之一：
   * **(a)** $\rho=2$ 且 $V_0\ne\lambda U_0\ (\forall\lambda)$：固定铅笔好，**或** $m\ge1$；
   * **(b)** $\rho=2$ 且 $V_0=\lambda_0U_0$（某 $\lambda_0$）：$m\ge2$；
   * **(c)** $\rho=1$：$m\ge2$；
   * **(d)** $\rho=0$：$m=3$。

**必要的证明**：

* 1：可容许 $S$ 必须含 $E$ 与 $F_0$（$H$ 与 $H_A$ 的行都在 $S$ 里），$\dim S=2$；
* 2：$\operatorname{rank}H\le\dim E+m$；
* (a) 中"固定铅笔坏且 $m=0$"：没有自由行，铅笔就是固定铅笔，坏；
* (b) $m=1$：在 $\lambda_0$ 处固定行全为 0，只剩一个自由行，秩 $\le1$；
* (c) $m=1$：$\rho=1$ 时固定行对所有 $\lambda$ 张成一条线 $L(\lambda)$；要秩 2 必须 $b(\lambda)\notin L(\lambda)$。
  但 $\det(a(\lambda),b(\lambda))$ 是 $\lambda$ 的 $\le2$ 次多项式；若它为非零常数，则 $\det(u,x)=0$，
  即 $x\in L$，与 $\operatorname{rank}H=2$（$x\notin\operatorname{row}U_0$）矛盾（$\dim E=0$ 时由条件 2 排除）。
  故它有根 $\lambda_1$，在该处 $b\parallel a$，秩 $\le1$；
* (d) $m=2$：铅笔是 $2\times2$ 的自由铅笔，行列式是二次式且首项 $\det(x_1,x_2)\ne0$（秩 2）$\Rightarrow$ 有根；$m<2$ 由条件 2 排除。

**充分的证明（构造）**：

* (a) 固定铅笔好：固定行本身对所有 $\lambda$ 张成 $S$，取 $B_1=B_2=0$ 即可；
  "固定铅笔坏（只有 rank-1 掉落）且 $m\ge1$"：对每个掉落点 $\lambda_i$，要求 $b(\lambda_i)\notin L_i$；
  这是关于 $y$ 的一条**真线性条件**（$x\notin L_i$ 时是一条线；$x\in L_i$ 时 $b(\lambda_i)\in L_i\iff y\in L_i$，仍是线），
  有限条线不能覆盖 $\mathbb C^2$，故可取到 $y$；于是所有 $\lambda$ 处秩 2；
* (b) $m\ge2$：在 $\lambda_0$ 处选两个自由行张成 $S$；$\lambda\ne\lambda_0$ 处固定行已张成 $S$。
* (c) $m\ge2$：用**incidence 维数**（专家 50 号答复 §2.2）。固定 $\lambda$（$a(\lambda)\ne0$）时，
  条件 $b_1(\lambda),b_2(\lambda)\in L(\lambda)$ 对每个 $(x_i,y_i)$ 是一条独立线性条件，余维 2；
  $(x_1,y_1,x_2,y_2)$ 的参数空间维数 8，$\lambda$ 再加 1 维，故 incidence 簇维数 $\le7<8$，投影不能填满。
  在 $a(\lambda_0)=0$ 的有限个 $\lambda_0$ 处，另加 $b_1(\lambda_0),b_2(\lambda_0)$ 线性无关（非空开条件）。
  再与 $\operatorname{rank}H=2$ 的开条件相交，即得非空开集。
* (d) $m=3$：显式见证（$k=2$）
  $$H=\begin{pmatrix}1&1\\-1&2\\-1&-1\end{pmatrix},\qquad
  H_A=\begin{pmatrix}-1&-1\\-2&0\\1&2\end{pmatrix},$$
  三个 2-子式为 $3\lambda^2+\lambda-2$、$-\lambda-1$、$3\lambda^2+2\lambda-4$，gcd $=1$（在 $\lambda=-1$ 处第二个为 0，
  但第一、三个分别为 $0$ 与 $-3$，无公根）。$k>2$ 时把该例嵌入一个 2-平面并把其余坐标补 0 即可。

**整行秩的处理**（专家 50 号答复 §2.3）：设 $\operatorname{rank}L_0=r$。$\Psi(\ell)=(\ell N_K,\ell AN_K)$ 把顶行映入
$S\times S$（4 维），像维数 $\le r$，故商空间维数 $\ge4-r=m+1$。于是可选 $m$ 个底部对，使其像模顶行像线性无关；
它们对应的行提升模 $\operatorname{span}L_0$ 也无关，故 $\operatorname{rank}L=3$。独立性是开条件，与谱好条件
（也是开条件）在不可约参数空间里相交非空。

## 进展

* **一次自我更正**：最初用 $\dim(E+F_0)$ 分类，被反例
  $U_0=\binom{1\ 0}{0\ 0}$、$V_0=\binom{0\ 1}{0\ 0}$、$m=1$ 打掉——此时 $\dim(E+F_0)=2$，但固定铅笔
  $\binom{\lambda\ -1}{0\ 0}$ 的**法秩只有 1**，一个自由行补不成（$2\times2$ 行列式有根）。改用 $\rho$ 后判据通过。
* **机器核验**（`free_fibre_criterion_check.py`，纯 `Fraction`，seed 20261108）：
  $k=2,3$ × $r=0,1,2$ 各 200 个随机 $(U_0,V_0)$，共 **1200/1200** 与判据一致；
  预测 FEAS 的实例都构造出了好点，预测 INFEAS 的实例要么无 $S$、要么无 rank-2 $H$、要么所有样本都坏。

## 最终结论

* 自由区 $q=3,\omega=2$ 有了**充要判据**（定理 1–3），形式符合专家要求（只依赖 $(U_0,V_0,m)$；
  不需要额外的 $S$ 参数——$\rho$ 已把 $S$ 的信息吸收）。
* 这不是 $q1$ 的答案：只覆盖 $\ker T=0$ 的 $q=\omega+1$ 格；约束区（$\ker T\ne0$）仍只有"机制 + 猜想"。
* **为什么不直接用 $\dim(E+F_0)$**：它只控制"可容许 $S$ 是否存在"，不控制固定铅笔的秩；
  $\rho$ 才是决定自由行要补几维的量。

## 放弃原因

* 定理停在 **M2**：incidence 论证与整行秩已按 50 号答复补上；仍需把 $\operatorname{rank}L_0=r$ 与
  对任意 $k\ge2$ 的陈述写进论文，并请专家复核。
* 约束区（$\ker T\ne0$）没有做：那里 $y$ 被线性约束，判据会依赖 $\mathcal C_S$ 的几何，是下一个问题。

## 残留价值

* 一条可发表的判据：自由区 $q=3,\omega=2$ 的可行性 $\iff$ $(\dim(E+F_0),\,m,\,\rho,\,V_0\propto U_0)$ 的显式条件；
* 反例（$\dim(E+F_0)=2$ 但 $\rho=1$）说明"维数不是秩"，可写进论文的 remark；
* 工具与 1200 例核验；与 attempts/100（同 $S$ 反例）、101（RP）互补；
* 下一步：约束区（$\ker T\ne0$）或 $k-\omega=1$ 的一般化。

## 相关文件

* [tools/verification/free_fibre_criterion_check.py](../../../../tools/verification/free_fibre_criterion_check.py)
* [workspace/q1_false/c_stratification/attempts/100_q_omega_plus_1_w2.md](100_q_omega_plus_1_w2.md)（同 $S$ 反例）
* [workspace/q1_false/c_stratification/attempts/101_rp_k_omega.md](101_rp_k_omega.md)（RP 上界）
* [proof/B.24/README.md](../../../../proof/B.24/README.md)（块判据、$q=\omega+1$ 判据、专家第二十三轮）
* [workspace/for_expert/archive/49_same_S_and_q_omega_plus_1-answer.md](../../../for_expert/archive/49_same_S_and_q_omega_plus_1-answer.md)（专家 §7 Priority B）

## 专家复核（50 号答复，§2）

* **法秩 $\rho$ 是正确的不变量**；四情形分类被评价为"mathematically well motivated and appear complete"；
* **case (c) 需 incidence 维数论证**（$\lambda$ 连续，不能只说"有限条线"）——已补（见上）；
* **整行秩**：需显式设 $\operatorname{rank}L_0=r$，并用商维数 $4-r=m+1$ 一次论证——已补；
* **对任意 $k\ge2$** 成立（谱计算全在 2 维 $S$ 内；case (d) 的见证可嵌入任意 2-平面）——定理已改述；
* 1200 例仍只是实验，不是证明。

## 状态

* 定理：**[已证-纸面，M2]**；incidence 论证、整行秩、任意 $k\ge2$ 已按 50 号答复补上；$\rho$ 的精确计算仍待换成 Smith 形。
* 机器核验：**1200/1200 一致**；不构成证明。
* 与专家 50 号答复的对应：四项修正（$\rho$ 不变量、case (c) incidence、整行秩、任意 $k$）已落实。
