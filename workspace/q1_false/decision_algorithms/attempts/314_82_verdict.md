# 82 号裁决落实：$G=FX$ 简化、固定 $q$ 与 FPT 均获认可、$r=0$ 分支补上

> 2026-11-10。82 号审计的结论是正面的：
> - 两条算法骨架数学上成立；
> - 固定 $q$ 的 $\\mathcal L^{O(q^2)}$ 可接受，但应把 $F$ 换成 $G=FX$；
> - 固定 $\\kappa_{\\rm obs}$ 的 FPT 是强定理候选，需补 $r=0$ 与比特复杂度；
> - 硬度应暂停局部 gate，转向全局约束子空间/多项式矩阵。
> 状态：**M3（专家审计）+ 精确验证**。

## 目标

落实 82 号，更新 312/313 的表述与路线。

## 设想与理由

82 号认可两条骨架并给出两处改进；先落实改进，再更新论文主线。

## 做法：四条

### 1. 固定 $q$：用 $G=FX$ 替代 $F$

$H=XB$、$H_A=FH=FXB$。令
$$G=FX\\in\\mathbb R^{q\\times\\omega}.$$
则
$$H_A=GB,\\qquad P(\\lambda)=(\\lambda X-G)B.$$
$G$ 是**无约束**的存在变量：
- 若 $H_A=FH$，取 $G=FX$；
- 反之若 $H_A=GB$，取左逆 $X_L$（$X_LX=I_\\omega$），令 $F=GX_L$，则 $FH=FXB=GB=H_A$。

变量数从 $q^2+q\\omega$ 降到
$$q\\omega+q\\omega=2q\\omega,$$
且 $M,c$ 对 $X,G$ 的次数从 2 降到 1。固定 $q$ 的变量数
$$2q\\omega+2\\omega=O(q^2).$$

`c314` 在 244 实例上验证 $G=FX$、$H_A=GB$、$\\operatorname{rank}P=\\operatorname{rank}((\\lambda X-G)B)$。

### 2. 固定 $q$ 的复杂度

82 号接受 $\\mathcal L^{O(q^2)}$，但要求写清：
- 枢轴图 $\\binom{k}{\\omega}$ 个，每个单独判定；
- $M$ 的行数 $O(qk)$，$b$ 的变量数 $\\omega(k-\\omega)$，故 $d_1=O(qk)$；
- 秩一致性多项式个数 $O(qk)$、次数 $O(qk)$；
- 变量数 $O(q^2)$，单指数实可行性给 $\\mathcal L^{O(q^2)}$；
- 次数随 $k$ 增长，但固定 $q$ 时单项式数 $k^{O(q^2)}$ 仍是输入多项式。

### 3. FPT：$r=0$、$k=0$ 与比特复杂度

82 号确认 Gram/Bezout/Cauchy–Binet 正确，但要求：

- **$r=0$**：无自由行，$\\kappa_{\\rm obs}=0$，不能把 $\\omega$ 当有界。此时 $H,H_A$ 固定，直接判 $(5a)$；
  若成立，取 $H=XB$、$H_A=GB$，$(5b)\\iff Q(\\lambda)=\\lambda X-G$ 对所有 $\\lambda$ 满列秩；
  这等价于 $Q$ 有 polynomial left inverse $S(\\lambda)Q(\\lambda)=I_\\omega$，可用有理线性系统判定（多项式时间）。
- **$k=0$**：压缩条件空，直接判。
- **$\\omega=0$**：$H=H_A=0$，直接判固定行。
- **比特复杂度**：有理预处理、Gram 构造、$B^{\\mathsf T}B$、系数高度都在
  $$f(\\kappa_{\\rm obs})\\operatorname{poly}(\\mathcal L)$$
  内；最后用 Renegar 的单指数实可行性界，得
  $$f(\\kappa_{\\rm obs})\\operatorname{poly}(\\mathcal L).$$

### 4. 路线

82 号建议：
- **主定理 B**：固定 $\\kappa_{\\rm obs}$ 的 FPT；
- **定理 A**：固定 $q$ 的 $\\mathcal L^{O(q^2)}$ 多项式算法；
- 论文以 Cauchy–Binet Gram 引理为中心；
- 硬度暂停局部 gate，转向全局约束子空间/多项式矩阵；不声称 $\\exists\\mathbb R$-hardness。

## 进展

* $G=FX$ 简化；
* $r=0$ 分支补上；
* 固定 $q$ 复杂度论证补全；
* 路线与论文结构确定。

## 最终结论

* 两条算法获得专家认可，均为“强证明路线”，不是已完成定理；
* 固定 $q$ 与固定 $\\kappa_{\\rm obs}$ 互补；
* 硬度路线暂停。

## 放弃原因

* 未写完整比特复杂度常数；
* 未实现；
* 未 Lean 化。

## 残留价值

* 两处关键改进；
* 论文结构；
* 下一步清单。

## 相关文件

* [82 答复](../../../for_expert/archive/82_two_algorithms-answer.md)
* [attempts/312](312_fixed_q_proof_sketch.md)
* [attempts/313](313_fpt_proof_sketch.md)
* `tools/verification/c314_G_form.py`

## 状态

* 裁决落实：**[M3]**。
* 形式化/实现：**[未做]**。
