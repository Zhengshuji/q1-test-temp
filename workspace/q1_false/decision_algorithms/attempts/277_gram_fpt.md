# 固定 $\\kappa_{\\rm obs}$ 的 FPT（Gram 证书版）：变量 $\\kappa_{\\rm obs}+2\\omega$

> 2026-11-09。77 号审计指出 261 的 FPT 证明没有控制 $q=r_0+r$（$r_0$ 可增长），
> 但给出了一条修复路线：
> $(5a)$ 用 $k\\times k$ Gram 矩阵的初等对称多项式编码；$(5b)$ 用 $2\\omega$ 维 Gram 证书，
> 通过 Cauchy–Binet 把极大子式族压缩成 $K(\\lambda,\\mu)$。本文件写出这条路线。
> 状态：**M2（纸面；模实 QE 与比特复杂度）**。

## 目标

证明：固定 $\\kappa_{\\rm obs}$ 时 $q1\\in\\mathrm{FPT}$，且 $q$ 只进多项式时间的系数计算，
不进变量数。

## 设想与理由

77 号审计指出 $q$ 不受 $\kappa_{\rm obs}$ 控制；用 Gram 矩阵把 $(5a)(5b)$ 写成常数维对象，$q$ 只进系数计算。

## 做法

### 设定

$q1$ 的压缩形式：$H=LN$（$q\\times k$）、$H_A=LAN$，$\\omega=\\operatorname{rank}H$，
$(5a)\\iff\\operatorname{rank}[H_A;H]=\\operatorname{rank}H$，$(5b)\\iff$ $P(\\lambda)=\\lambda H-H_A$ 的 $\\omega$-子式 gcd 为 1。

$\\kappa_{\\rm obs}=r\\operatorname{rank}[N,AN]$；$N$ 满列秩 ⇒ $k\\le\\kappa_{\\rm obs}$、$r\\le\\kappa_{\\rm obs}$。
$q=r_0+r$ 可以随 $r_0$ 增长（77 号审计）。

## 引理 1（$(5a)$ 的 Gram 形式）

令
$$G_H=H^{\\mathsf T}H,\\qquad G_S=H^{\\mathsf T}H+H_A^{\\mathsf T}H_A.$$
则
$$\\operatorname{rank}G_H=\\operatorname{rank}H,\\qquad
\\operatorname{rank}G_S=\\operatorname{rank}\\begin{bmatrix}H\\\\H_A\\end{bmatrix}.$$
对半正定 $G$，设 $e_j(G)$ 是特征值的第 $j$ 个初等对称多项式。则
$$e_j(G)>0\\iff\\operatorname{rank}G\\ge j.$$
所以，在 rank-$\\omega$ 层上
$$\\boxed{(5a)\\iff e_\\omega(G_H)>0\\ \\text{且}\\ e_{\\omega+1}(G_S)=0.}$$

*证明*：$e_j$ 是特征值乘积之和；半正定矩阵的 $e_j>0$ 当且仅当至少 $j$ 个正特征值。
$e_\\omega(G_H)>0$ 给 $\\operatorname{rank}H\\ge\\omega$；$e_{\\omega+1}(G_S)=0$ 给
$\\operatorname{rank}[H_A;H]\\le\\omega$。后者包含 $H$，故两者都等于 $\\omega$。$\\square$

**注**：$G_H,G_S$ 是 $k\\times k$，$k\\le\\kappa_{\\rm obs}$；$e_j$ 的次数 $\\le j\\le k$。
$G$ 的条目是 $q$ 行的和，$q$ 只影响求和的计算量。

## 引理 2（$(5b)$ 的 $2\\omega$ 维 Gram 证书）

设 $f_1,\\dots,f_s$ 是 $P$ 的全部 $\\omega$-子式，$\\deg f_i\\le\\omega$。
对每个 $i$ 与 $t=0,\\dots,\\omega-1$，取 $\\lambda^t f_i$ 的系数向量（次数 $\\le2\\omega-1$），
把这些行排成矩阵 $B$（行数 $s\\omega$，列数 $2\\omega$）。令
$$e_0=(1,0,\\dots,0)^{\\mathsf T}\\in\\mathbb R^{2\\omega}.$$
则
$$\\boxed{(5b)\\iff e_0\\in\\operatorname{row}(B)\\iff\\exists x\\in\\mathbb R^{2\\omega}:\\ B^{\\mathsf T}B\\,x=e_0.}$$

*证明*：
$\\operatorname{row}(B)$ 恰是多项式
$$\\sum_{i=1}^s g_i(\\lambda)f_i(\\lambda),\\qquad \\deg g_i<\\omega$$
的系数向量空间。

**Bezout 次数 $<\\omega$**：若 $\\gcd(f_1,\\dots,f_s)=1$，取非零 $g=\\sum a_i f_i$；
$g$ 的复根有限。对每个根 $\\alpha$，条件 $h(\\alpha)=0$（$h=\\sum b_i f_i$）是系数 $b$ 的一个真实线性方程
（因为 $f_i(\\alpha)$ 不全为零）。有限个真子空间不能覆盖系数空间，故可选 $h$ 使 $h(\\alpha)\\ne0$ 对所有根成立，
于是 $\\gcd(g,h)=1$。扩展 Euclid 给 $ug+vh=1$，$\\deg u,\\deg v<\\omega$。
展开得 $\\sum (u a_i+v b_i)f_i=1$，且 $\\deg(ua_i+v b_i)<\\omega$。

于是 $e_0\\in\\operatorname{row}B$ 当且仅当存在这样的表示，即 $(5b)$。
最后，$\\operatorname{row}(B)=\\operatorname{im}(B^{\\mathsf T})=\\operatorname{im}(B^{\\mathsf T}B)$（实矩阵），
故 $e_0\\in\\operatorname{row}B\\iff\\exists x: B^{\\mathsf T}Bx=e_0$。$\\square$

**变量数**：$x$ 只有 $2\\omega$ 个分量，与 $s$、$q$ 无关。

## 引理 3（Cauchy–Binet 压缩 $B^{\\mathsf T}B$）

不必枚举 $s=\\binom{q}{\\omega}\\binom{k}{\\omega}$ 个 $f_i$。定义
$$K(\\lambda,\\mu)=\\sum_{|J|=\\omega}\\det\\big(P(\\lambda)_{:,J}^{\\mathsf T}P(\\mu)_{:,J}\\big),$$
其中 $J\\subseteq[k]$。由 Cauchy–Binet，
$$K(\\lambda,\\mu)=\\sum_{i}f_i(\\lambda)f_i(\\mu).$$
$B^{\\mathsf T}B$ 的 $(d,e)$ 条目是
$$\\sum_{i,t}\\operatorname{coeff}_{\\lambda^d}(\\lambda^t f_i)\\operatorname{coeff}_{\\mu^e}(\\mu^t f_i)
=\\operatorname{coeff}_{\\lambda^d\\mu^e}\\left(\\Big(\\sum_{t=0}^{\\omega-1}(\\lambda\\mu)^t\\Big)K(\\lambda,\\mu)\\right).$$
所以 $B^{\\mathsf T}B$ 可由 $K$ 的系数读出。

$K$ 只有 $\\binom{k}{\\omega}\\le2^{\\kappa_{\\rm obs}}$ 项，每项是 $\\omega\\times\\omega$ 行列式，
$P$ 次数 1 ⇒ 每项次数 $\\le2\\omega$。因此 $B^{\\mathsf T}B$ 可在
$$f(\\kappa_{\\rm obs})\\operatorname{poly}(q,\\mathcal L)$$
时间算出，$q$ 只进多项式因子。

## 定理（固定 $\\kappa_{\\rm obs}$ 的 FPT）

固定 $\\kappa_{\\rm obs}$ 时，$q1$ 有
$$f(\\kappa_{\\rm obs})\\operatorname{poly}(\\mathcal L)$$
时间的精确算法（模实 QE 标准界）。

*证明路线*：
1. 用 $t\\in\\mathbb R^{\\kappa_{\\rm obs}}$ 参数化 $(H,H_A)$（$T(R)=(RN,RAN)$ 的像）；
2. 写 $G_H,G_S$；加辅助变量 $z$ 把 $e_\\omega(G_H)>0$ 写成 $z\\,e_\\omega(G_H)=1$；
3. 写 $B^{\\mathsf T}B$（引理 3），加 $x\\in\\mathbb R^{2\\omega}$ 与方程 $B^{\\mathsf T}Bx=e_0$；
4. 变量数 $\\le\\kappa_{\\rm obs}+2\\omega+1=f(\\kappa_{\\rm obs})$；方程数/次数只依赖 $\\omega,k$；
5. 实 QE 给 $f(\\kappa_{\\rm obs})\\operatorname{poly}(\\mathcal L)$。

$\\square$

## 注意

- 复数据：把 $\\mathbb C$ 变量拆成实/虚部；Gram 用 Hermitian $H^*H$；$x$ 拆实/虚。
- $\\omega=0$：$e_0(G_H)=1$，$e_1(G_S)=0$（即 $G_S=0$），单独处理。
- 比特复杂度：$K$ 的行列式在 $\\mathbb Q$ 上精确计算，规模 $\\operatorname{poly}(q,\\mathcal L,f(\\kappa))$；
  尚未写显式常数。
- 这修复了 261/262 中 $q$ 不受控的漏洞；261/262 只能保留为固定 $(q,c)$ 的版本。

## 进展

* $(5a)$ 的 Gram 形式（引理 1）；
* $(5b)$ 的 $2\\omega$ 维 Gram 证书（引理 2）；
* Cauchy–Binet 压缩（引理 3）；
* FPT 变量数 $\\kappa_{\\rm obs}+2\\omega$，$q$ 只进多项式。

## 最终结论

* 固定 $\\kappa_{\\rm obs}$ 的 FPT 有了新的、对 $q$ 稳健的证明骨架；
* 关键外部依赖只剩实 QE 标准界；
* 261/262 的旧 Bezout 展开版本应降级为固定 $(q,c)$。

## 放弃原因

* 未写比特复杂度常数；
* 未实现；
* 未处理所有实/复边界。

## 残留价值

* 一个更可信的 FPT 定理候选；
* 两个可复用的 Gram 引理；
* 明确 $q$ 只进多项式计算。

## 补充：复数据、$\omega=0$、比特复杂度

**复数据**：把 $\mathbb C$ 变量拆成实/虚部；Gram 用 Hermitian $H^*H$；$x$ 拆实/虚。
若只要求实 $L$，这一步必要；若允许复 $L$，可直接对 Hermitian 形式做实 QE。

**$\omega=0$**：$\operatorname{rank}H=0$ ⇒ $H=0$；$(5a)$ 给 $H_A=0$；$(5b)$ 对 $P=0$ 自动。
所以条件是线性方程 $LN=0$、$LAN=0$，可直接线性判定。

**比特复杂度骨架**：
- $K(\lambda,\mu)$ 的每项是 $\omega\times\omega$ 多项式矩阵的行列式，次数 $\le2\omega$；
  无分式消元计算，每个 $\operatorname{poly}(\omega)$ 次算术；
- $K$ 有 $\binom{k}{\omega}\le2^{\kappa}$ 项，$P$ 条目来自 $q$ 行，计算量
  $$f(\kappa_{\rm obs})\operatorname{poly}(q,\mathcal L);$$
- $B^{\mathsf T}B$ 的条目是 $K$ 的系数，规模 $2\omega$；
- 系数在 $\mathbb Q$ 上精确，比特长 $\operatorname{poly}(\mathcal L,f(\kappa))$；
- 实 QE 的标准比特复杂度给最终 FPT（显式常数未写）。

**实例支持**：`c278_gram_certificate.py` 在 244 上精确验证 $e_0\in\operatorname{row}B$、
$B^{\mathsf T}Bx=e_0$、Cauchy–Binet、$e_2(G_H)=55>0$、$e_3(G_S)=0$，以及扰动后 $e_3>0$。

**与 261/262 的关系**：本节修复了 261/262 中 $q$ 不受控的漏洞；261/262 只保留为固定 $(q,c)$ 版本。

## 相关文件

* [attempts/276](276_77_audit_corrections.md)
* [attempts/261](261_fpt_formal.md)
* [77 答复](../../../for_expert/archive/77_routes_abc_reliability-answer.md)

## 状态

* FPT（Gram 版）：**[M2 纸面]**。
* 实现/比特复杂度：**[未做]**。
