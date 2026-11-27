> **77 号审计更正**：固定 $q$ 多项式只是 sketch。缺参数化线性消去引理（$M(z)y=b(z)$，$z$ 固定维、$y$ 随输入增长，构造只含 $z$ 的等价公式，含所有秩层）。不能声称 $P$。

# 路线 C：固定 $q$ 的多项式算法（$Z,U$ 量化 + 线性消去）

> 2026-11-09。路线 C 的第一个正结果方向：**固定观测器阶 $q$** 时，$q1$ 可在多项式时间判定。
> 关键是把自由变量从 $n$ 维的 $L$ 换成**固定维**的 $Z$（$q\\times q$）与 $U=\\operatorname{im}H$（Grassmannian），
> 再用线性代数判定 $L$ 的存在性。
> 状态：**M2（纸面；模实 QE 与秩消去）**。

## 目标

证明：固定 $q$ 时 $q1\\in\\mathrm{P}$（或 FPT in $q$）。

## 设想与理由

$(5a)\\iff H_A=ZH$ 对某个 $Z$。于是
$$P(\\lambda)=(\\lambda I-Z)H.$$
$(5b)$ 只依赖 $Z$ 与 $U=\\operatorname{im}H$：
$$(5b)\\iff U\\cap E_\\lambda(Z)=\\{0\\}\\ \\forall\\lambda.$$
而 $H=LN$、$H_A=LAN$ 对 $L$ 是**线性**的；固定 $Z,U$ 后，$L$ 的条件是线性/秩条件，
可用线性代数消去。$Z,U$ 的维数只依赖 $q$（$q^2$ 与 $\\omega(q-\\omega)$），与 $n$ 无关。

## 做法

### 1. 固定 $Z,U$ 的 $L$ 条件

设 $P_U$ 是到 $U$ 的投影。$\\operatorname{im}(LN)=U$ 等价于
$$(I-P_U)LN=0,\\qquad \\operatorname{rank}(LN)=\\omega.$$
$(5a)$ 等价于
$$L(AN-ZN)=0.$$
两者都是 $L$ 的线性方程；$\\operatorname{rank}(LN)=\\omega$ 是秩条件。
固定 $Z,U$ 时，“是否存在 $L$ 满足这些条件”可用线性代数判定：
- 解线性方程组 $L\\,M(Z)=0$ 与 $(I-P_U)LN=0$；
- 在解空间上检查 $\\operatorname{rank}(LN)=\\omega$（矩阵秩，固定 $\\omega$）。
这一步的复杂度是 $\\operatorname{poly}(n)$（$r=q-r_0$ 固定；秩 $\\le r$）。

### 2. 谱条件

$U$ 避开 $Z$ 的所有特征空间，等价于：取 $U$ 的基 $B$（$q\\times\\omega$），
$$\\gcd\\{\\omega\\text{-子式 of }(\\lambda I-Z)B\\}=1.$$
这是 $Z,B$ 的多项式条件（$\\forall\\lambda$ 已消去），变量数只依赖 $q$。

### 3. 量词消去

$$\\exists Z\\in\\mathbb C^{q\\times q}\\ \\exists U\\in\\operatorname{Gr}(\\omega,q):\
\\text{谱条件}\\ \\wedge\\ \\exists L\\ (\\text{线性/秩条件}).$$
$Z,U$ 的维数只依赖 $q$；$L$ 的存在性是线性代数（可写成 $Z,U$ 的秩条件，子式大小 $\\le r$）。
由固定维数实 QE，整体复杂度
$$f(q)\\cdot\\operatorname{poly}(n,\\mathcal L).$$
所以固定 $q$ 时 $q1\\in\\mathrm{P}$（更强：FPT in $q$）。

## 进展

* 固定 $q$ 的算法骨架；
* $L$ 的线性消去；
* 谱条件化为 $Z,B$ 的 gcd。

## 最终结论

* 固定 $q$ 时 $q1$ 可多项式判定（模 QE/秩消去细节）；
* 变量 $q$ 仍开放；
* 这与 261（固定 $\\kappa_{\\rm obs}$）是两条不同的参数化路线：
  固定 $q$ 不固定 $k$，固定 $\\kappa_{\\rm obs}$ 固定 $k$。

## 放弃原因

* 未写出“解空间上 rank(LN)=ω”的显式秩条件；
* 未处理 $L$ 的线性系统与 $Z,U$ 的耦合的 QE 细节；
* 未实现。

## 残留价值

* 一个清晰的固定 $q$ 算法路线；
* 与固定 $\\kappa_{\\rm obs}$ 的 FPT 互补；
* 明确下一步：写出线性消去的秩判据。

## 相关文件

* [attempts/261](261_fpt_formal.md)
* [attempts/255](../../../q1_true/multiplication_gate/attempts/255_kappa_correction.md)
* [docs/05 Q10](../../../../docs/05_open_questions.md)

## 状态

* 固定 $q$：**[M2 纸面]**。
* 实现/细节：**[未做]**。
