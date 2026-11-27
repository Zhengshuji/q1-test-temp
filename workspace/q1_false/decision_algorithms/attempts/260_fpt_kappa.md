# 固定 $\\kappa_{\\rm obs}$ 的 FPT 定理（模标准 QE 界）

> 2026-11-09。255 修正后，固定 $\\kappa_{\\rm obs}$ 控制 $k,r,q$。本文件给出 FPT 证明路线：
> 不需要 249 的 $Q,R$ 次数界；直接用**极大子式的 Bezout 恒等式** + 实量词消去。
> 状态：**M2（纸面；依赖标准 QE 复杂度界）**。

## 目标

证明：固定 $\\kappa_{\\rm obs}$ 时，$q1$ 有 $f(\\kappa_{\\rm obs})\\operatorname{poly}(\\mathcal L)$ 算法（FPT）。

## 设想与理由

255：$\\kappa_{\\rm obs}=r\\operatorname{rank}[N,AN]\\ge rk$ ⇒ $k\\le\\kappa_{\\rm obs}$、$r\\le\\kappa_{\\rm obs}$。
所以压缩数据 $H,H_A$、极大子式个数、Bezout 系数都只依赖 $\\kappa_{\\rm obs}$。
把 $(5a)(5b)$ 写成有限个多项式方程，用实量词消去；变量数与次数都是 $f(\\kappa_{\\rm obs})$，
QE 对固定维数是多项式（Basu–Pollack–Roy）。

## 做法

### 1. 参数化

$N$ 有理基；$T(\\Delta R)=(\\Delta RN,\\Delta RAN)$ 的像维数 $\\kappa_{\\rm obs}$。
取像的一组基，用 $t\\in\\mathbb C^{\\kappa_{\\rm obs}}$ 参数化 $(H,H_A)=(H_0,H_{A,0})+T(R)$。
（实数据时把 $\\mathbb C$ 系数拆成实/虚部。）

### 2. $(5a)$

$\\operatorname{rank}[H_A;H]=\\operatorname{rank}H$ 等价于所有 $(\\omega+1)$-子式为零。
$[H_A;H]$ 是 $2q\\times k$，$q,k\\le f(\\kappa)$，子式个数
$$\\binom{2q}{\\omega+1}\\le2^{2q}\\le f(\\kappa),$$
每个次数 $\\le\\omega+1\\le f(\\kappa)$。

### 3. $(5b)$：Bezout 证书

设 $f_1,\\dots,f_s$ 是 $P(\\lambda)=\\lambda H-H_A$ 的全部 $\\omega$-子式（$s=\\binom{k}{\\omega}\\le2^k$）。
$$(5b)\\iff\\gcd(f_1,\\dots,f_s)=1
\\iff\\exists g_1,\\dots,g_s\\in\\mathbb C[\\lambda]:\\ \\sum_i g_i f_i=1.$$
$P$ 次数 1 ⇒ $\\deg f_i\\le\\omega$。
标准 Bezout 界：若 $\\gcd=1$，可取 $\\deg g_i\\le\\max_j\\deg f_j\\le\\omega$。
所以 $g_i$ 的系数个数 $\\le s(\\omega+1)\\le f(\\kappa)$。

### 4. 实代数系统

未知量：$t$（实/虚部）+ $g_i$ 的系数；方程：$(5a)$ 的子式、$(5b)$ 的 Bezout 系数方程。
变量数、方程数、次数都 $\\le f(\\kappa)$。
实量词消去（固定维数）：
$$\\operatorname{poly}(\\mathcal L)\\cdot(sd)^{O(m)}=f(\\kappa)\\operatorname{poly}(\\mathcal L).$$
所以是 FPT（常数巨大，理论结果）。

### 5. 与 249 的关系

249 的 $QPR=I$ 也可用，但需要 $Q,R$ 的次数界；Bezout 路线绕开了它：
不需要构造 $Q,R$，只需极大子式的 Bezout 系数。

## 进展

* 固定 $\\kappa_{\\rm obs}$ 的 FPT 证明路线；
* 绕开 249 的 $Q,R$ 次数界；
* 明确依赖：标准 Bezout 界 + 实 QE 复杂度。

## 最终结论

* 固定 $\\kappa_{\\rm obs}$ 时 $q1\\in\\mathrm{FPT}$（模标准 QE 界）；
* 固定 $(q,c)$ 是特例；
* 变 $\\kappa_{\\rm obs}$ 仍开放（可能 $\\exists\\mathbb R$-hard）。

## 放弃原因

* 未写出完整 QE 复杂度常数；
* 未实现算法；
* 未处理实点/复点与比特长的所有细节。

## 残留价值

* 一个清晰的 FPT 定理骨架；
* 参数化层级：固定 $\\kappa_{\\rm obs}$ ⇒ FPT；变 $\\kappa_{\\rm obs}$ 开放；
* 与 247/249/255 一致。

## 相关文件

* [attempts/255](../../../q1_true/multiplication_gate/attempts/255_kappa_correction.md)
* [attempts/249](../../../q1_true/multiplication_gate/attempts/249_compact_certificate.md)
* [docs/05 Q10](../../../../docs/05_open_questions.md)

## 状态

* FPT 骨架：**[M2 纸面]**。
* 实现/常数：**[未做]**。
