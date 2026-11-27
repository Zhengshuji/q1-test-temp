> **77 号审计更正**：本证明没有控制 $q=r_0+r$（$r_0$ 可增长），$s=\binom{q}{\omega}\binom{k}{\omega}$ 随 $q$ 增长。
> 固定 $\kappa_{\rm obs}$ 的 FPT 改由 [277](277_gram_fpt.md) 的 Gram 证书（变量 $\kappa+2\omega$）证明；本文只保留为固定 $(q,c)$ 版本。

# 固定 $\\kappa_{\\rm obs}$ 的 FPT 定理（正式版）

> 2026-11-09。把 260 的骨架写成正式定理，补上 $(5a)$ 的秩分支、$(5b)$ 的 Bezout 次数界、
> 以及实量词消去的复杂度依赖。状态：**M2（纸面；模标准 QE/Bezout 界）**。

## 目标

把 260 的 FPT 骨架写成正式定理，补上分支与次数界。

## 设想与理由

用 $\kappa_{\rm obs}\ge rk$ 控制尺寸；用 Bezout 证书替代 $Q,R$ 的构造；用固定维数 QE 收尾。

## 做法

### 设定

输入：有理 $A\\in\\mathbb Q^{n\\times n}$、$C\\in\\mathbb Q^{p\\times n}$、$L_0\\in\\mathbb Q^{r_0\\times n}$、$q$。
$K_0=\\ker[C;CA]$，$N$ 有理基，$k=\\dim K_0$，$r=q-r_0$。
$$\\kappa_{\\rm obs}=r\\operatorname{rank}[N,AN].$$
问题 $q1$：是否存在 $L=[L_0;R]$（$R\\in\\mathbb C^{r\\times n}$）满足 $(5a)(5b)$。

## 引理 1（尺寸界）

$N$ 满列秩 ⇒ $\\operatorname{rank}[N,AN]\\ge k$ ⇒ $\\kappa_{\\rm obs}\\ge rk$。
若 $r\\ge1$：
$$k\\le\\kappa_{\\rm obs},\\qquad r\\le\\kappa_{\\rm obs},\\qquad q\\le\\kappa_{\\rm obs}+r_0.$$
（若 $r=0$，问题退化为固定 $L_0$ 的检查，可直接算。）

## 引理 2（$(5a)$ 的秩分支）

固定 $\\omega\\in\\{0,\\dots,q-1\\}$。
$$(5a)\\ \\text{且}\\ \\operatorname{rank}H=\\omega
\\iff
\\begin{cases}
\\text{所有 }(\\omega+1)\\text{-子式 of }[H_A;H]\\text{ 为零},\\\\
\\text{某个 }\\omega\\text{-子式 of }H\\text{ 非零}.
\\end{cases}$$
非零条件用辅助变量 $z$ 与所选子式 $h_S$ 写成 $z\\,h_S=1$（分支枚举 $S$）。
$[H_A;H]$ 是 $2q\\times k$，子式个数 $\\binom{2q}{\\omega+1}\\le2^{2q}=f(\\kappa)$。

## 引理 3（$(5b)$ 的 Bezout 证书）

设 $f_1,\\dots,f_s$ 是 $P(\\lambda)=\\lambda H-H_A$ 的全部 $\\omega$-子式（$s=\\binom{k}{\\omega}\\le2^k$）。
$$(5b)\\iff\\gcd(f_1,\\dots,f_s)=1
\\iff\\exists g_1,\\dots,g_s\\in\\mathbb C[\\lambda]:\\ \\sum_i g_i f_i=1.$$
$\\deg f_i\\le\\omega$；由 [262](262_bezout_qe_dependencies.md) 的引理 B1，可取 $\\deg g_i\\le(s-1)\\omega$。
把 $g_i$ 的系数作为未知量，方程 $\\sum g_i f_i=1$ 按 $\\lambda$ 的系数比较，
得到 $\\le2\\omega+1$ 个多项式方程，变量数 $\\le s((s-1)\\omega+1)=f(\\kappa)$。

## 定理（固定 $\\kappa_{\\rm obs}$ 的 FPT）

固定 $\\kappa_{\\rm obs}$ 时，$q1$ 有
$$f(\\kappa_{\\rm obs})\\cdot\\operatorname{poly}(\\mathcal L)$$
时间的精确算法，其中 $\\mathcal L$ 是输入比特长。

*证明*：
1. 由引理 1，$k,r,q\\le f(\\kappa)$；
2. 枚举 $\\omega=0,\\dots,q-1$ 与一个非零 $\\omega$-子式的指标 $S$（分支数 $f(\\kappa)$）；
3. 用 $t\\in\\mathbb C^{\\kappa_{\\rm obs}}$ 参数化 $(H,H_A)$（$T$ 的像的基）；
4. 写 $(5a)$ 的子式方程 + 非零方程 + $(5b)$ 的 Bezout 方程；
5. 变量数、方程数、次数都 $\\le f(\\kappa)$；
6. 实量词消去（变量数固定）的复杂度为
   $$(sd)^{O(m)}\\operatorname{poly}(\\mathcal L)=f(\\kappa)\\operatorname{poly}(\\mathcal L).$$
所以是 FPT。$\\square$

## 注意

- 常数 $f(\\kappa)$ 极大（$2^{O(\\kappa)}$ 级），是理论结果，不是实用算法。
- 复系数拆成实/虚部；QE 在实域上做；复点对应实点对，需在编码里显式加 $a+ib$ 的实/虚变量。
- 依赖两个标准事实：Bezout 次数界、固定维数实 QE 的多项式界。两者都在文献中，但本文未复述证明。
- 分支“某个 $\\omega$-子式非零”是析取；固定 $\\kappa$ 时分支数有限，可逐个 QE。

## 进展

* 固定 $\\kappa_{\\rm obs}$ 的 FPT 定理（模标准界）；
* 明确所有依赖与分支；
* 与 247/255 一致：固定 $(q,c)$ 是特例。

## 最终结论

* 固定 $\\kappa_{\\rm obs}$ ⇒ $q1\\in\\mathrm{FPT}$；
* 变 $\\kappa_{\\rm obs}$ 仍开放（可能 $\\exists\\mathbb R$-hard）；
* 下一步：补 QE/Bezout 的引用与常数，或转结构论文。

## 放弃原因

* 未写 QE 常数的显式形式；
* 未处理实点/复点的所有边界；
* 未实现算法。

## 残留价值

* 一个可引用的 FPT 定理；
* 参数化层级；
* 与专家的 Project 2 对齐。

## 相关文件

* [attempts/260](260_fpt_kappa.md)
* [attempts/255](../../../q1_true/multiplication_gate/attempts/255_kappa_correction.md)
* [docs/05 Q10](../../../../docs/05_open_questions.md)

## 状态

* 定理：**[M2 纸面]**。
* 实现：**[未做]**。
