# 依赖引理：有效 Bezout 界与实 QE 复杂度

> 2026-11-09。261 的 FPT 定理依赖两个标准事实。本文件把它们写成可引用的引理，
> 并说明本项目只需要“界存在且只依赖尺寸”，不需要最优常数。
> 状态：**M2（纸面；标准代数/实代数几何）**。

## 目标

把 261 的两个外部依赖写成明确引理，避免“次数界未证”的漏洞。

## 设想与理由

261 需要：
1. $(5b)$ 的 Bezout 证书 $\\sum g_i f_i=1$ 中 $g_i$ 的次数有只依赖 $q,k,\\omega$ 的界；
2. 固定维数实量词消去的复杂度对变量数/方程数/次数是 $f(m,s,d)\\operatorname{poly}(\\mathcal L)$。

两者都是标准结果；本项目只需存在性界，不需要显式最优值。

## 做法

### 引理 B1（有效 Bezout 界）

设 $f_1,\\dots,f_s\\in K[x]$（$K$ 为域），$\\deg f_i\\le d$，且 $\\gcd(f_1,\\dots,f_s)=1$。
则存在 $g_1,\\dots,g_s\\in K[x]$ ，使
$$\\sum_i g_i f_i=1,\\qquad \\boxed{\\deg g_i\\le (s-1)d.}$$

*证明*：对 $s$ 归纳。
- $s=1$：$f_1$ 是单位，取 $g_1=1/f_1$，次数 0。
- $s=2$：扩展 Euclid 给 $g_1f_1+g_2f_2=1$，$\deg g_1<\deg f_2\le d$、$\deg g_2<\deg f_1\le d$。
- $s>2$：令 $h=\gcd(f_1,\dots,f_{s-1})$。对 $f_i'=f_i/h$（$i<s$）用归纳假设，
  得 $\sum_{i<s}a_i f_i'=1$，$\deg a_i\le(s-2)d$；故 $\sum a_i f_i=h$。
  又 $\gcd(h,f_s)=1$，扩展 Euclid 给 $u h+v f_s=1$，$\deg u<\deg f_s\le d$、$\deg v<\deg h\le d$。
  取 $g_i=u a_i$（$i<s$）、$g_s=v$，则
  $$\sum_{i<s}(u a_i)f_i+v f_s=u h+v f_s=1,$$
  且 $\deg g_i\le d+(s-2)d=(s-1)d$、$\deg g_s\le d\le(s-1)d$。$\square$

**注**：$s\\le2^k$、$d=\\omega$，故 $D=(s-1)\\omega\\le\\kappa_{\\rm obs}2^{\\kappa_{\\rm obs}}$，只依赖 $\\kappa_{\\rm obs}$。

### 引理 QE1（固定维数实 QE）

设 $\\varphi$ 是 $\\mathbb R$ 上由 $s$ 个多项式（次数 $\\le d$、变量数 $\\le m$、整系数比特长 $\\mathcal L$）组成的公式。
则判定 $\\varphi$ 的复杂度为
$$(s d)^{O(m)}\\operatorname{poly}(\\mathcal L).$$
（Basu–Pollack–Roy 的实代数几何算法；这是标准界。）

### 推论

261 的系统中 $m,s,d\\le f(\\kappa_{\\rm obs})$，故
$$(s d)^{O(m)}\\operatorname{poly}(\\mathcal L)=f(\\kappa_{\\rm obs})\\operatorname{poly}(\\mathcal L),$$
即 FPT。

## 进展

* 把 261 的两个依赖写成引理；
* 明确只需存在性界，$D(\\kappa)$ 可以很大；
* FPT 结论不依赖最优 Bezout 常数。

## 最终结论

* 固定 $\\kappa_{\\rm obs}$ 的 FPT 定理在标准 Bezout + QE 界下成立；
* 若要写进论文，需引用 BPR 书与有效 Bezout 的标准陈述；
* 常数是理论级的，实际不可用。

## 放弃原因

* $D(s,d)=(s-1)d$ 已给显式形式；
* 未复述 BPR 证明；
* 未处理实点/复点编码细节。

## 残留价值

* 两个可引用的依赖引理；
* 明确的“只需存在性”论证；
* 与 261 对齐。

## 相关文件

* [attempts/261](261_fpt_formal.md)
* [attempts/260](260_fpt_kappa.md)
* [docs/05 Q10](../../../../docs/05_open_questions.md)

## 状态

* 依赖引理：**[M2 纸面]**。
* 显式常数：**[未做]**。
