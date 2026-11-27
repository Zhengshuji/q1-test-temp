# 81 号裁决落实：固定子空间 no-go 收窄；固定 $q$ 有新算法；主线转 FPT

> 2026-11-10。81 号确认了两件事并纠正了两处：
> 1. port rigidity 只是**条件性** no-go；固定子空间**可以**有移动端口（只要 $E_1\\cap E_2=0$ 且 $\\dim W$ 足够）；
> 2. 输入非零门的正确量词是“$\\exists R$ ⇔ $x\\ne0$”，不是“对每个 $R$，$(5b)\\iff x\\ne0$”；
> 3. 固定 $q$ 有一条具体的多项式路线：$H=XB$、规范化 $B$ 的枢轴列、用秩一致性消去 $B$；
> 4. 路线建议：**固定 $\\kappa_{\\rm obs}$ FPT 为主**，固定 $q$ 为第二主线，硬度退为次要的全局 $\\mathcal T$-约束方向。
> 状态：**M3（专家裁决 + 精确验证）**。

## 目标

落实 81 号，纠正 309/310 与 303C 的表述，记录固定 $q$ 的新路线。

## 设想与理由

81 号给出两处更正和一条新算法路线；先逐条记录，再更新优先级。

## 做法：逐条

### 1. 固定子空间 no-go 的收窄

81 号给出反例：在 $\\mathbb R^5$ 中
$$E_1=\\operatorname{span}(e_1,e_2),\\qquad
E_2=\\operatorname{span}(e_4,e_5),$$
$$W_t=\\operatorname{span}(e_1,e_2,e_3,e_4+t e_5).$$
则 $E_1\\subseteq W_t$、$E_1\\cap E_2=0$，但
$$W_t\\cap E_2=\\operatorname{span}(e_4+t e_5)$$
是移动的线。

所以：
- 309/310 的结论只对“$E_1\\cap E_2$ 已是一条固定线、且 $\\dim W$ 最小”成立；
- 一般固定子空间**不**排除移动端口；
- 309/310 应标为条件性结果，不是一般 no-go。

### 2. 输入非零门的量词

303C：
$$H=\\begin{bmatrix}1\\\\u\\end{bmatrix},\\quad
H_A=\\begin{bmatrix}0\\\\xv\\end{bmatrix},\\quad
P(\\lambda)=\\begin{bmatrix}\\lambda\\\\ \\lambda u-xv\\end{bmatrix}.$$
对**固定** $R=(u,v,w)$：
$$(5b)\\iff xv\\ne0,$$
不是 $x\\ne0$（$v=0$ 时即使 $x\\ne0$ 也失败）。
正确的 q1 可行性是
$$\\boxed{\\exists R:\\ (5a)\\wedge(5b)\\iff x\\ne0.}$$
303C 仍是 sound 的输入非零门；但表述要改。

### 3. 固定 $q$ 的新路线（81 号）

- 固定 $\\omega$，枚举枢轴列 $J$（$\\binom{k}{\\omega}$ 种）；
- 写 $H=XB$，$X\\in\\mathbb R^{q\\times\\omega}$ 满列秩，$B\\in\\mathbb R^{\\omega\\times k}$ 行满秩，$B_{:,J}=I_\\omega$；
- $(5a)$ 给 $H_A=FXB$，$F\\in\\mathbb R^{q\\times q}$；
- 固定行给线性方程，自由行给 $D[H_i;H_{A,i}]=0$（$\\ker D=\\mathcal T=\\operatorname{row}[N\\ AN]$）；
- 这些方程对剩余 $B$ 变量是**线性**的：
  $$M(F,X)b=c(F,X);$$
- 用秩一致性消去 $b$：
  $$\\Gamma=MM^{\\mathsf T},\\quad \\Gamma'=MM^{\\mathsf T}+cc^{\\mathsf T},$$
  $$\\exists b:Mb=c\\iff\\operatorname{rank}\\Gamma=\\operatorname{rank}\\Gamma'.$$
- 秩相等写成
  $$\\bigvee_{t=0}^{d_1}\\left[e_t(\\Gamma)>0\\wedge e_{t+1}(\\Gamma)=0\\wedge e_{t+1}(\\Gamma')=0\\right];$$
- $(5b)$ 只依赖 $F,X$：$\\operatorname{rank}((\\lambda I-F)X)=\\omega$ 对所有 $\\lambda$，用 $2\\omega$ 维 Gram–Bezout 证书；
- 变量数 $q^2+q\\omega+2\\omega=O(q^2)$，固定 $q$ 时是常数维实代数 ⇒
  $$\\boxed{q1\\in\\mathrm{P}\\ \\text{for fixed }q}$$
  （粗界 $\\mathcal L^{O(q^2)}$；XP 型）。

`c311` 在 200 个随机系统上验证了秩一致性恒等式。

### 4. 路线建议（81 号）

- **主线**：固定 $\\kappa_{\\rm obs}$ 的 Gram FPT——最接近完整定理；
- **第二主线**：固定 $q$ 的多项式算法（上面的 $H=XB$ + 秩一致性）；
- **次要**：硬度不要继续做局部 row-copy；转向全局 $\\mathcal T$-约束矩阵铅笔/子空间实现；目前没有 sound 乘法门，也没有 no-go。

## 进展

* 纠正 309/310 的一般性；
* 纠正 303C 的量词；
* 记录固定 $q$ 的具体算法路线；
* 路线优先级明确。

## 最终结论

* 309/310 降为条件性结果；
* 303C 的 sound 表述改为 $\\exists R\\iff x\\ne0$；
* 固定 $q$ 有新的 XP 路线；
* 主线转 FPT。

## 放弃原因

* 未写固定 $q$ 的完整比特复杂度；
* 未正式化固定 $q$ 算法；
* 未构造 sound 乘法门。

## 残留价值

* 两处重要更正；
* 固定 $q$ 的算法骨架；
* 路线优先级。

## 相关文件

* [81 答复](../../../for_expert/archive/81_wiring_and_routes-answer.md)
* [attempts/309](../../../q1_false/decision_algorithms/attempts/309_port_rigidity.md)
* [attempts/310](../../../q1_false/decision_algorithms/attempts/310_moving_port.md)
* [attempts/303](../../../q1_false/decision_algorithms/attempts/303_79_verdict_lifts.md)
* `tools/verification/c311_rank_consistency.py`

## 状态

* 裁决落实：**[M3]**。
* 固定 $q$ 形式化：**[未做]**。
