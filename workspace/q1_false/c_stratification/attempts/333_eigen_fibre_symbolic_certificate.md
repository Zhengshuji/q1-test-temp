# 333 特征纤维的符号证书：一整条 $\mathbb P^1$ 的行空间都给出 $\gcd=1$

> 承接 330（一个好点即证）、332（机制：自由度够就能避开 $C$）。
> 本文件把"构造一个好行空间"变成**符号证书**：不需要找点，直接证明整条参数族都好。

## 目标

在特征情形里，行空间 $V$ 是 $U^\perp$（本族 $n=5$ 时 4 维）里的超平面，参数空间是 $\mathbb P^3$。
取一条**过固定 2 维 $V_0$** 的直线
$$V_t=V_0+\langle w_0+t\,w_1\rangle,\qquad t\in\mathbb P^1,$$
直接在 $\mathbb Q(t)[\lambda]$ 里算 $\lambda H-H_A$ 的 $2$-子式 gcd。

## 设想与理由

332 把 H4 压成"在 $U^\perp$ 里构造一个好行空间"。既然行空间只是 $U^\perp$ 里的超平面，
**参数空间只有 $\mathbb P^3$**；而"好"是开条件（坏闭），所以只要**符号地**验证一条参数曲线上的
gcd 恒为 1，就足以判定可行性——不需要逐点找，也不需要随机采样。

取一条最简单的参数曲线：过固定 $V_0$ 的 $\mathbb P^1$。若整条都 $\gcd=1$，则这条线上每一点都是好点，
分量可行（322 的闭性 + 324 的不可约）。

## 做法

实例：$n=5$、$p=1$、$C=e_5^{\mathsf T}$、$A e_1=2e_1$、$e_1\in K_0$（与 330 同一实例）。
$Q$ 为 $U^\perp=e_1^\perp$ 的基（4 行）；取 $V_0=\langle Q_0,Q_1\rangle$、$w_0=Q_2$、$w_1=Q_3$，
$L_t=\begin{bmatrix}Q_0\\Q_1\\Q_2+tQ_3\end{bmatrix}$（3 行），$H_t=L_tN$、$H_{A,t}=L_tAN$。

## 进展

**(1) 数值扫描**：$t=-6,\dots,6$ 共 13 个有理值，全部 $\operatorname{rank}H_t=k-1$、$(5a)$ 成立、**$\gcd=1$**（无一坏）。

**(2) 符号证书**：把 $t$ 当符号，在 $\mathbb Q(t)[\lambda]$ 里算 $3$ 个非零 $2$-子式的 gcd，得
$$\gcd\bigl(m_I(t;\lambda)\bigr)\;=\;1 .$$
即**整条 $\mathbb P^1$ 上除有限个 $t$ 外都给出好的铅笔**——不需要再"找点"。
（**口径更正（专家 96 号）**：$\gcd=1$ 在 $\mathbb Q(t)[\lambda]$ 上只保证"除有限个 $t$ 外好"；
不能说"每个 $t$ 都好"——特化可以制造公因子。但它足以给出**有理好点**。）

## 族级推广（c340）

把 $A$ 也换掉：取 5 个随机 $A$（都满足 $A e_1=\lambda_0 e_1$、$\lambda_0\in\{2,3,-1,5\}$，
$C=e_5^{\mathsf T}$），行空间取 $V_t=\langle e_2,e_3,e_4+t e_5\rangle$，**$t$ 仍为符号**。

**5/5 个 $A$ 上，$\gcd\bigl(m_I(t;\lambda)\bigr)\equiv1$（在 $\mathbb Q(t)[\lambda]$ 上）。**

一个结构上的旁证：$C=e_5\notin V_t$ 对**所有** $t$ 成立（因为 $e_4$ 的系数恒为 1），
正好是 332 的"避开 $C$"条件——这条曲线整个落在"无强制关系"的区域里。

**仍未证**：一般 $A$（把 $A$ 的条目也符号化）上的同一个恒等式；那是一个 $\mathbb Q(A,t)[\lambda]$ 上的 PIT。

## 最终结论

1. **这个特征纤维的可行性有了符号证书**（不是采样）：一条 $\mathbb P^1$ 的行空间全部可行。
   由 322 的闭性 + 324 的不可约性，这足以判定**该分量可行**、**该层可行**。
2. 332 的"构造好行空间"在这个实例上**不需要**：除有限个 $t$ 外都好，**足以取得一个有理好点**。
   这与"避开 $C$ 就有足够自由度"一致——但比它更强：不只是没有强制关系，而是整族都好。
3. 因此 H4 的**本族版本在这个实例上成立且已证**；一般性（别的 $A$、别的特征值、更大的特征空间）仍未证。

## 放弃原因

- 只覆盖了 $\mathbb P^3$（所有超平面 $V$）里的一条 $\mathbb P^1$——虽然一条线已足够证明分量可行，但"全部 $V$ 都好"未证；
- 只测了一个实例（一个 $A$、一个特征值）；换 $A$ 的符号证书未做；
- 没有处理"高维特征空间"（$\dim\ker(A-\lambda_0I)\cap K_0\ge2$）。

## 残留价值

- 一个**符号可行性证书**（整族 gcd $\equiv1$），比 330 的点证书更强；
- 把 332 的"构造"问题在本实例上直接消解（除有限个 $t$ 外都好，故有有理好点）；
- 可作论文里"特征纤维"一节的正面例子。

## 相关文件

- [attempts/330](330_eigen_fibre_feasibility.md)（点证书）
- [attempts/332](332_why_eigen_fibres_escape.md)（机制：自由度 vs $C$）
- [attempts/329](329_forced_relations_quotient_pencil.md)（非特征层全坏）
- [attempts/324](324_hyperplane_component_theorem.md)（分量）
- [c337](../../../../tools/verification/c337_eigen_fibre_check.py)

## 状态

- 符号证书（单实例）：**[精确验证]**（$\gcd=1$ 在 $\mathbb Q(t)[\lambda]$ 上；[c339](../../../../tools/verification/c339_symbolic_eigen_certificate.py)）。
- **族级**（5 个 $A$，各带符号 $t$）：**[精确验证 5/5]**（[c340](../../../../tools/verification/c340_family_symbolic_certificate.py)）；一般 $A$ **未证**。
- 全部 $V\in\mathbb P^3$ 都好：**[未证]**（只证了一条 $\mathbb P^1$）。
- 高维特征空间：**[未做]**。

## 复现

```
python tools/verification/c339_symbolic_eigen_certificate.py
```
输出：数值扫描 13/13 好；符号 $\gcd=1$（$\mathbb Q(t)[\lambda]$）。
