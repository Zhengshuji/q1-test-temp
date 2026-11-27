# B.10 · 谱障碍的定域

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.10` 条目（§0.1 归并表）。

## 命题

**B.10（a）〔原 B.10〕（谱障碍的定域）** 设 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$，$Q_{\mathcal L}=D(\lambda)H$（$H=[\mathcal L;CA;C]$）。则
$$\lambda\notin\operatorname{spec}\Lambda\ \Longrightarrow\ \operatorname{rank}Q_{\mathcal L}(\lambda)=h .$$

## 纸面证明

*证明*：$D(\lambda)$ 分块上三角、对角块为 $\lambda I-\Lambda$ 与 $I$，故 $\lambda\notin\operatorname{spec}\Lambda$ 时 $D$ 可逆，左乘不改秩。$\square$
*推论*：$(5b)\iff$ 每个 $\lambda\in\operatorname{spec}\Lambda$ 处 $\operatorname{rank}Q_{\mathcal L}(\lambda)=h$；有限初等因子的根必在 $\operatorname{spec}\Lambda$ 内。

*位置*：[proof/eigenvalue_confinement](../eigenvalue_confinement/README.md)。

**B.10（b）〔原 B.10b〕（谱失败轨迹在每个层上是闭的；专家 2026-11-04 §Q6/§10.2 的建议）** 固定一个图卡，并在其上取
**局部闭层**
$$\Sigma=\{\theta:\ \operatorname{rank}[V\mid Z(\theta)]=\rho,\ \ h(\theta)=h_0,\ \ (5a)\ \text{成立}\}$$
（$\rho,h_0$ 固定；$(5a)$ 那一项本身是闭条件，故 $\Sigma$ 仍局部闭）。则
$$\{\theta\in\Sigma:\ (5b)\ \text{在}\ \theta\ \text{处失败}\}$$
在 $\Sigma$ 的 Zariski 拓扑中是**闭**的；等价地，$\Sigma$ 中**谱可行**的 $\theta$ 构成**开**集。

*证明*：在 $\Sigma$ 上 $\operatorname{rank}[\mathcal L;CA;C]=h_0$ 固定，故由 Cramer 法则可把
$\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ 的 $\Lambda$（$q\times q$）取成 $\theta$ 的**有理函数**，
分母（$[\mathcal L;CA;C]$ 的某个 $h_0$ 阶子式）在 $\Sigma$ 上不为零。于是
$$\mathcal D:=\{(\theta,\lambda)\in\Sigma\times\mathbb P^1:\ \operatorname{rank}P_{Z(\theta)}(\lambda)<\rho
\ \text{且}\ \det(\lambda I-\Lambda(\theta))=0\}$$
是 $\Sigma\times\mathbb P^1$ 中的闭集（前者由 $P$ 的 $\rho$ 阶子式全为零定义，后者是多项式方程）。
$\mathbb P^1\to\mathrm{pt}$ 是**紧合**（proper）的，故投影 $\pi:\Sigma\times\mathbb P^1\to\Sigma$ 是**闭映射**，
$\pi(\mathcal D)$ 闭。另一方面，在 $\Sigma$ 上 $(5a)$ 成立，故由零空间铅笔判据（本文件 2.4，文献 Thm 4）
$(5b)\iff\operatorname{rank}P_{Z(\theta)}(\lambda)=\rho\ \forall\lambda$；再由 B.10 的推论，
掉秩的 $\lambda$ 必满足 $\det(\lambda I-\Lambda(\theta))=0$，而掉秩处存在当且仅当 B.10 意义下的
$\operatorname{rank}Q<h_0$ 处存在。故 $\theta$ 在 $\Sigma$ 上谱失败 $\iff\exists\lambda$ 使
$(\theta,\lambda)\in\mathcal D$，即失败集 $=\pi(\mathcal D)$，闭。$\square$

*推论*：**层上**可行集开；**跨层**（取所有 $\rho$ 与 $h_0$ 的层之并）时，可行集只是
有限个"局部闭集 ∩ 开集"之并，即 **constructible**——两层陈述并不矛盾：
$\rho$ 或 $h$ 变化处可以出现"可行点列收敛到不可行点"。
*注（必须一起读）*：本条的"闭"是**在层内**；不能据此说全局可行集开。另外 $\Lambda$ 的正则选取
只在 $h$ 固定的层上成立（分母是某个 $h_0$ 阶子式），这正是必须分层的技术原因。
**2026-11-04 专家补充（采纳）**：Cramer 只保证"某个主元子式非零处"可解，单个主元未必在整层上非零；
故正确表述应再细分为**有限多个主元子图卡**（每个上取定一个非零 $h_0$ 阶子式来定义 $\Lambda$），
在每个子图卡上做上述紧合性论证。结论（层内闭）不变，只是层的"分层"要再细一层。

## Lean

* 无独立 Lean 内核（该条为纸面证明）。

## 精确验证

* 见等级行给出的精确验证数字。

## 状态与历史

*等级*：**[已证-纸面]** + **[精确验证 3/3]**（候选 #1 的坏根为复根，说明"扫有理 $\lambda$"不能当判据）。
*等级*：**[已证-纸面]**（用紧合性；不依赖任何计算）。**[未做]**：把该论证写成一维情形下的显式例子以交叉核对。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。



## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F1 |
| 导出等级 | **L2** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— **Lean 可行、尚未补**（分块可逆性） |


## 支撑目录

无（证据全部在本卷宗内）。

## 专家复核意见（成立）

不需要 $\Lambda$ 可对角化：$\lambda\notin\operatorname{spec}\Lambda$ 时 $D(\lambda)$ 可逆即可。
