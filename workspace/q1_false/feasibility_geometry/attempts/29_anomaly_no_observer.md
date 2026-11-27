# 一个异常实例：功能可观测，但在所有阶都没有 $(5a)\wedge(5b)$ 的增广

> ## 2026-11-03 撤回（专家答复）
>
> **本文的结论错误**："该实例在所有阶都无解"不成立。专家给出了 $q=3$ 的**显式**见证
> $$\mathcal L_*=\begin{pmatrix}-1&0&0&0&-1&0&0\\ 1&0&0&0&0&0&1\\ 1&0&0&-1&0&-1&1\end{pmatrix}$$
> （第三行恰是 $CA$ 的第二行），并指出其两个 $5\times5$ 极大子式为**非零常数**（$-1$ 与 $+1$），
> 故 $\operatorname{rank}Q_*(\lambda)\ge5=h$ 对所有 $\lambda$，$(5b)$ 成立 ⟹ **$q_{\min}=3$**。
>
> 同时纠正本档的三处错误：
>
> | 错误 | 更正 |
> |---|---|
> | $q=2$ 的 $h=6$ | **$h=5$**（$\operatorname{rank}[L_0;CA;C]=5$）；$\gcd=\lambda-1$，在 $\lambda=1$ 处失败（是谱失败，不是整数失败）|
> | "$q=3$ 只有 3 个候选，全失败" | 采样**不穷尽** $\operatorname{Gr}(2,3)$；[gr23_enumeration.py](../../../../tools/verification/gr23_enumeration.py) 穷举后：$(5a)$-可行 **23** 个，其中 $(5b)$ 成立 **2** 个 |
> | "$q=4,5$ 也失败" | 有意义的阶区间是 $[q_0,\ n_0-p]$，$n_0=\operatorname{rank}\mathcal O_C=5$ ⟹ $[2,3]$；$q=4,5$ **不在其内**（$q=5$ 的 $\lambda=0$ 掉秩另有解释：$e_3\in\ker A\cap\ker C$）|
>
> 回归测试：[regression_Lstar.py](../../../../tools/verification/regression_Lstar.py)（结构、秩、两个常数子式、两路判据、$q=2$ 的修正）。
> 教训：**候选枚举必须穷尽**（$\operatorname{Gr}(2,3)=\mathbb P^2$ 可精确枚举，不该抽样）。


## 目标

在逐阶判定 $q_{\\min}$（[qmin_decide.py](../../../../tools/verification/qmin_decide.py)）时遇到一个实例：
它**功能可观测**，却在 $q=2,3,4,5$ 每一阶都找不到满足 $(5a)\\wedge(5b)$ 的增广。本档把该实例完整记录，
供专家判定：是公式理解有误，还是"功能可观测 $\\Rightarrow$ 存在观测器"有额外假设。

## 设想与理由

若"功能可观测 $\Rightarrow$ 存在观测器"成立，那么逐阶判定 $q_{\min}$ 时**至少有一阶可行**。
反之，若某实例每阶都失败，则要么公式表述有误，要么该充分条件有额外假设。
因此把遇到的第一个"全阶失败"实例完整记录，作为待判问题。

## 做法

[qmin_decide.py](../../../../tools/verification/qmin_decide.py) 逐阶处理：
$q=r$（单点，$L=L_0$）、$q_0<q<n-p$（$Z$-参数化抽样 60）、$q=n-p$（$d=0$，直接构造补，含**去掉** $L_0$ 约束的对照）；
$(5b)$ 用 Toeplitz 零度与极大子式 gcd 双路核验。

## 进展

（结果见下表。）

## 实例

$$A=\\begin{pmatrix}
1&0&0&-1&0&-1&1\\\\
1&0&0&0&1&0&0\\\\
1&1&0&-1&0&0&0\\\\
0&0&0&0&0&0&0\\\\
0&0&0&0&0&0&0\\\\
0&-1&0&0&1&0&0\\\\
0&-1&0&1&1&1&0
\\end{pmatrix},\\quad
C=\\begin{pmatrix}0&-1&0&0&1&0&0\\\\ 1&0&0&0&0&0&0\\end{pmatrix},\\quad
L_0=\\begin{pmatrix}-1&0&0&0&-1&0&0\\\\ 1&0&0&0&0&0&1\\end{pmatrix}.$$

$n=7$、$p=2$、$r=2$、$q_0=2$、$r_1=\\operatorname{rank}[C;CA]=4$。

**功能可观测性**：$\\operatorname{rank}\\mathcal O_C=5=\\operatorname{rank}[\\mathcal O_C;L_0]$ ⟹ $\\operatorname{row}L_0\\subseteq\\operatorname{row}\\mathcal O_C$ ✓。

## 逐阶结果

| 阶 $q$ | 情形 | 候选 | 成功 | $h$ | $q+r_1$ |
|---|---|---|---|---|---|
| 2（$=r$，可行族是**单点** $L=L_0$）| 单点 | — | **0** | 6 | 6 |
| 3 | 抽样 | 3 | **0** | 6 | 7 |
| 4 | 抽样 | 54 | **0** | 6–7 | 8 |
| 5（$=n-p$，$d=0$）| 抽样（含**不带** $L_0$ 约束的 300 个补）| 400 | **0** | 7 | 9 |

$q=5$ 处独立核验（极大子式 gcd）：$g(\\lambda)=\\lambda$，即 $\\lambda=0$ 处掉秩——与 Toeplitz 判据一致。

**注意**：即使去掉 $\\operatorname{row}L_0\\subseteq\\operatorname{row}\\mathcal L$ 的约束（$q=5$、300 个随机补），
$(5b)$ 仍全失败，所以问题不在 $L_0$ 的约束。

## 最终结论（待专家判定）

1. 按本项目的 $(5a)/(5b)$ 表述，该实例**没有任何阶**可行；
2. 但它满足功能可观测（这是"存在观测器"的标准充分条件之一）；
3. 因此三种可能：
   * (i) 本项目的 $(5a)/(5b)$ 表述与文献的观测器条件不完全一致（例如 $(5b)$ 是否要求**所有** $\\lambda$ 包括 $\\lambda=0$）；
   * (ii) 文献"功能可观测 $\\Rightarrow$ 存在观测器"需要额外假设（如 $\\det A\\ne0$ 或某种可稳性）；
   * (iii) 我们某处实现有误。
4. 该实例 $A$ 有**两行全零**（$\\operatorname{rank}A=5$），故 $\\lambda=0$ 是特征值且 $\\ker A$ 是 2 维；
   掉秩恰发生在 $\\lambda=0$。这提示可能和"$A$ 奇异"有关。

## 放弃原因

不适用（记录异常）。**未做**：判定到底是 (i)(ii)(iii) 哪一个——需要文献条文对照，超出本会话可及范围。

## 残留价值

* 一个**完整、可复算**的异常实例（矩阵全部列出，$q=2..5$ 逐阶有数据）；
* 一个明确的待判问题：$(5b)$ 是否应在 $\\lambda=0$ 上检查、以及"功能可观测"是否隐含 $A$ 非奇异；
* 如果确认是 (ii)，那这是一个**新的存在性反例**（比 Type III 更强：不是阶差，而是无解）。

## 相关文件

- [tools/verification/qmin_decide.py](../../../../tools/verification/qmin_decide.py)
- [workspace/q1_false/feasibility_geometry/attempts/28_type3_at_boundary.md](28_type3_at_boundary.md)
- [proof/fernando_2gap/README.md](../../../../proof/fernando_2gap/README.md)
