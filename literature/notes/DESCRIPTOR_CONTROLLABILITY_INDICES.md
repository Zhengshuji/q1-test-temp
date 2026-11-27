# Descriptor controllability indices —— 与 $Q_L$ 左指标的对应（2026-11-02）

> 目的（专家 2026-11-02 §4 的优先级 4）：把"$Q_L$ 的左最小指标"接到**已有理论**上。
> 本文件只记录**能点到的来源**与**我们自己能证的部分**，并明确区分二者。

## 1. 定义（来源）

SLICOT 库例程 **AG08BZ**（*Zeros and Kronecker structure of a descriptor system pencil*）的文档写明：
对系统铅笔
$$S(\lambda)=\begin{pmatrix}A-\lambda E&B\\C&D\end{pmatrix}$$
它计算"**right and left Kronecker indices**"；并且文档的示例程序把

* `P = 0`（即铅笔 $[A-\lambda E\ B]$）的那一组右 Kronecker 指标称为**可控性指标**（controllability indices），
  判据是"the system $(A-\lambda E,B)$ is completely controllable"；
* `M = 0`（即铅笔 $[A-\lambda E;C]$）的那一组左 Kronecker 指标称为**可观性指标**（observability indices）。

来源：<https://www.slicot.org/objects/software/shared/doc/AG08BZ.html>（访问于 2026-11-02）；
其引用文献是 P. Misra, P. Van Dooren, A. Varga, *Computation of structural invariants of generalized
state-space systems*, Automatica 30 (1994) 1921–1936。

**标准系统**（$E=I$）的特例是教科书结论：铅笔 $[\lambda I-A\ B]$ 的右最小指标 = $(A,B)$ 的可控性指标；
$[\lambda I-A;C]$ 的左最小指标 = $(A,C)$ 的可观性指标（Kailath, *Linear Systems*, 1980；
Wonham, *Linear Multivariable Control*, 1985）。本文件不把这条当作已核对的引文，只当"标准事实"。

## 2. 我们的映照（**我们自己能证**）

在 [proof/descriptor_reduction](../../proof/descriptor_reduction/README.md) 里我们证明了
$$R(\lambda)=J D(\lambda)^{\mathsf T}=[\lambda E-E X^{\mathsf T}\ \ B]$$
的**右**最小指标 $=$ $Q_L$ 的**左**最小指标。

把 $R$ 写成"system pencil"形式：$R(\lambda)=[A'-\lambda E'\ \ B']$，其中
$$E'=-E,\qquad A'=-EX^{\mathsf T},\qquad B'=B .$$
（符号只是左乘 $-I$，不改变 Kronecker 数据。）

于是由 SLICOT 文档给出的术语：

> **$Q_L$ 的左最小指标 = descriptor 系统 $(E',A',B')=(-E,\,-EX^{\mathsf T},\,B)$ 的可控性指标。**

其中 $[E\ B]=J$ 满行秩 $h$、$\operatorname{rank}E=\operatorname{rank}L=:r$。

**标准情形（$r=q=h$，$E$ 可逆）**：左乘 $E^{-1}$ 是严格等价，$R\sim[\lambda I-X^{\mathsf T},\ E^{-1}B]$，
故
$$\text{左指标}=(\text{可控性指标 of }(X^{\mathsf T},\,E^{-1}B)).$$

## 3. 与 B.7 的一致性

SLICOT 文档的示例（$L=9,N=9,M=3$、$[A-\lambda E,B]$ 完全可控）给出右 Kronecker 指标 $[2,2,2]$，**和 = 9 = 阶数**；
这与我们的 B.7 + 恒等式（$(5b)$ 下 $\sum\varepsilon=\operatorname{rank}L=r$）一致：
**可控性指标之和 = $\operatorname{rank}E'=r$**。

## 4. 不能当结论的东西（诚实标注）

1. 我**没有**完整读过 Misra–Van Dooren–Varga (1994) 原文，只读到 SLICOT 的文档页；
   "右 Kronecker 指标 = 可控性指标"的**精确定义**（是否要求可控、是否含零指标）应以原文为准。
2. 我**没有**在本次会话中检索到"descriptor 系统的可控性指标序列能取哪些划分"的完整刻画；
   这一类问题在标准系统里是"可控性指标的分配问题"（Wonham），descriptor 情形需另查。
3. 因此第 2 节的映照是**术语层面**的（把我们的量识别成文献里的量），不是把文献定理搬过来。

## 5. 检索记录（2026-11-02）

| 查询 | 结果 |
|---|---|
| `descriptor system controllability indices right minimal indices pencil [sE-A B] Kronecker` | 命中 SLICOT AG08BZ、Varga 报告（PDF 无法取文本）、Atay–Özçaldıran（Semantic Scholar，内容未取到）|
| `"right minimal indices" "controllability indices" pencil [sI-A B]` | 多为片段；命中 De Terán 的 actas（奇异铅笔最小指标约定）、Dopico 的 LAA 2022（左最小指标）|
| `"left minimal indices" "observability indices" pencil system` | 同上，无直接可引语句 |
| `descriptor system "controllability indices" definition "Kronecker indices" system pencil survey Lewis singular systems` | 命中 Iwata 的 *Kronecker canonical form of singular mixed matrix pencils*（PDF，未取文本）、SLICOT 文档 |

**待办**（若继续这条线）：读 Misra–Van Dooren–Varga 1994 与 Iwata 的 KCF 论文，
确认"右 Kronecker 指标 = 可控性指标"的精确定义与零指标的约定。
