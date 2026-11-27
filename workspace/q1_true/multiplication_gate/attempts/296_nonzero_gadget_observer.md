# $2\\times1$ 谱 gadget 的完整观测器实现：$(5b)\\iff f\\ne0$

> 2026-11-09。78 号给出了压缩 $2\\times1$ gadget：
> $$H=\\begin{bmatrix}1\\\\0\\end{bmatrix},\\quad H_A=\\begin{bmatrix}0\\\\f\\end{bmatrix},\\quad P(\\lambda)=\\begin{bmatrix}\\lambda\\\\-f\\end{bmatrix},$$
> 并问它能否满足逐行提升。本文件给出一个**完整观测器实现**：
> $$n=3,\\ p=1,\\ q=2,\\ r_0=1,\\ r=1,\\ k=1,\\ \\omega=1,$$
> 且
> $$(5a)\\ \\text{对所有 }f\\text{ 成立},\\qquad (5b)\\iff f\\ne0.$$
> 状态：**M2 + 精确验证**。

## 目标

把 78 号的 $2\\times1$ 压缩 gadget 落成真实的 $A,C,L_0$。

## 设想与理由

gadget 的两行是
$$(H_1,H_{A,1})=(1,0),\\qquad (H_2,H_{A,2})=(0,f).$$
取 $q=2$、$k=1$，让固定行给 $1$，自由行给 $f$：
$$L_0N=1,\\quad L_0AN=0,\\quad RN=0,\\quad RAN=f.$$

## 做法：显式数据

取
$$C=\\begin{bmatrix}0&0&1\\end{bmatrix},\\qquad
A=\\begin{bmatrix}0&0&0\\\\1&0&0\\\\0&1&0\\end{bmatrix},\\qquad
L_0=\\begin{bmatrix}1&0&0\\end{bmatrix},\\qquad
R(f)=\\begin{bmatrix}0&f&0\\end{bmatrix}.$$
（$A$ 的列：$Ae_1=e_2$、$Ae_2=e_3$、$Ae_3=0$。）

**核空间**：
$$Cx=x_3,\\qquad CA=C A=e_2^{\\mathsf T}\\ (\\text{即 }x_2),$$
所以
$$K_0=\\ker[C;CA]=\\{(x_1,0,0)\\}=\\operatorname{span}(e_1),\\qquad N=e_1.$$

**压缩数据**：
$$L_0N=1,\\quad RN=0\\ \\Rightarrow\\ H=\\begin{bmatrix}1\\\\0\\end{bmatrix};$$
$$L_0AN=L_0e_2=0,\\quad RAN=f\\ \\Rightarrow\\ H_A=\\begin{bmatrix}0\\\\f\\end{bmatrix}.$$

## 验证（c296）

- $K_0=\\operatorname{span}(e_1)$，$N=e_1$；
- $\\operatorname{rank}H=1$ 对所有 $f$；
- $(5a)$：$\\operatorname{row}H_A\\subseteq\\operatorname{row}H$（$H_0=1$ 张成整个 $\\mathbb C^1$，$H_{A,1}=f$ 总在行空间中）；
- $P(\\lambda)=\\lambda H-H_A=(\\lambda,-f)^{\\mathsf T}$；
- $f\\ne0$：$P$ 的第二个分量恒非零，$\\operatorname{rank}P=1$ 对所有 $\\lambda$；
- $f=0$：$P(0)=0$，$\\operatorname{rank}P(0)=0<1$；
- 所以
  $$(5b)\\iff f\\ne0.$$

逐行提升：
$$(H_1,H_{A,1})=(1,0)=L_0[N\\ AN],\\qquad
(H_2,H_{A,2})=(0,f)=R(f)[N\\ AN],$$
自动满足 $\\operatorname{row}[N\\ AN]$。

## 进展

* **第一个完整的、逐行可提升的 $(5b)\\iff f\\ne0$ gadget**；
* 只需 $n=3,p=1,q=2,k=1,\\omega=1$；
* 固定行给常数 $1$，自由行的 $f$ 给参数；
* 与 78 号的压缩 gadget 完全一致。

## 最终结论

* 78 号问的“$2\\times1$ gadget 能否落地”答案是**能**；
* 这是一个非零/开条件 gadget，不是乘法门；
* 它证明 $(5b)$ 可以编码“某参数非零”，这是 $\exists\mathbb R$ 归约所需的非零部分。

## 放弃原因

* 未组合成乘法门；
* 未处理多参数/多块；
* 未给出硬度归约。

## 残留价值

* 一个完整的观测器 gadget；
* $(5b)$ 非零编码的最小实现；
* Route B 的第一个落地正结果。

## 相关文件

* [78 答复](../../../for_expert/archive/78_status_and_rank_bounds-answer.md)
* [attempts/269](../../../q1_false/decision_algorithms/attempts/269_spectral_polarity.md)
* `tools/verification/c296_nonzero_gadget_observer.py`

## 状态

* 完整实现：**[M2 + 精确验证]**。
* 乘法组合：**[未做]**。
