> **314 补（82 号）**：用 $G=FX$ 替代 $F$：$H_A=GB$、$P=(\lambda X-G)B$；变量数从 $q^2+q\omega$ 降到 $2q\omega$，方程次数从 2 降到 1。c314 验证。

# 固定 $q$ 的多项式算法：$H=XB$ + 秩一致性的完整证明骨架

> 2026-11-10。81 号给出固定 $q$ 的路线；本文件把它写成可检查的引理链。
> 结论：对每个固定 $q$，
> $$q1\in\mathrm{P},$$
> 粗界 $\\mathcal L^{O(q^2)}$（XP 型）。
> 状态：**M2（纸面骨架；秩一致性有 c311 精确验证）**。

## 目标

证明：固定 $q$ 时，$q1$ 可在多项式时间判定（指数依赖 $q$，不依赖 $n$）。

## 设想与理由

$H$ 是 $q\\times k$，秩 $\\omega\\le q$。把 $H$ 分解为 $H=XB$，$X$ 是 $q\\times\\omega$、$B$ 是 $\\omega\\times k$，
自由度集中在 $X$（$q\\omega$）与 $F$（$q^2$）；$B$ 的高维部分用**线性系统一致性**消去。
$(5b)$ 只依赖 $F,X$，用 $2\\omega$ 维 Gram–Bezout 证书。

## 做法：引理链

### 引理 1（秩分解与枢轴规范化）

设 $\\operatorname{rank}H=\\omega>0$。存在枢轴列 $J\\subseteq[k]$，$|J|=\\omega$，使
$$X=H_{:,J}\\in\\mathbb R^{q\\times\\omega}$$
满列秩，且存在 $B\\in\\mathbb R^{\\omega\\times k}$ 使
$$H=XB,\\qquad B_{:,J}=I_\\omega.$$
反之，若 $X$ 满列秩、$B_{:,J}=I_\\omega$，则 $\\operatorname{rank}(XB)=\\omega$。

*证明*：$H$ 的列空间由任意 $\\omega$ 个独立列张成；取 $J$ 为这些列，$B=X^+H$（$X^+$ 左逆），
则 $B_{:,J}=X^+X=I$。反之 $B$ 的 $J$ 列是单位阵，行满秩，故 $XB$ 秩 $\\omega$。$\\square$

### 引理 2（$(5a)$ 的 $F$ 参数化）

若 $\\operatorname{row}H_A\\subseteq\\operatorname{row}H$，则存在 $F\\in\\mathbb R^{q\\times q}$ 使
$$H_A=FH=FXB.$$
反之显然。

*证明*：$H$ 的行空间是 $\\operatorname{im}H^{\\mathsf T}$；每个 $H_A$ 的行是 $H$ 的行的线性组合，
把这些系数排成 $F$ 的行即可。$\\square$

### 引理 3（自由行的线性约束）

令
$$\\mathcal T=\\operatorname{row}[N\\ AN]\\subseteq\\mathbb R^{2k}.$$
对每个自由行 $i$，
$$(H_i,(H_A)_i)\\in\\mathcal T.$$
取 $D$ 使 $\\ker D=\\mathcal T$。则自由行条件等价于
$$D\\begin{bmatrix}(X_iB)^{\\mathsf T}\\\\((FX)_iB)^{\\mathsf T}\\end{bmatrix}=0.$$
固定行 $i\\le r_0$ 满足
$$X_iB=h_i^0,\\qquad (FX)_iB=g_i^0.$$

*证明*：$H_i=r_iN$、$(H_A)_i=r_iAN$，故对是 $r_i[N\\ AN]$，属于 $\\mathcal T$；
反之 $\\mathcal T$ 中每个对都有原像 $r_i$（$[N\\ AN]$ 的行空间定义）。$\\square$

### 引理 4（对 $B$ 的线性化）

固定 $F,X$ 与枢轴 $J$，把 $B$ 的未知条目记为 $b$（$B_{:,J}=I_\\omega$ 代入）。
引理 3 的所有方程对 $b$ 是**线性**的：
$$M(F,X)b=c(F,X),$$
其中 $M,c$ 的条目是 $F,X$ 的多项式，次数 $\\le2$。

*证明*：$X_iB$ 与 $(FX)_iB$ 对 $B$ 线性；$D$ 是常数矩阵；固定行的右端是常数。$\\square$

### 引理 5（参数化线性一致性）

设 $M(z)\\in\\mathbb R^{m\\times n}$、$c(z)\\in\\mathbb R^m$ 是固定参数 $z$ 的多项式矩阵/向量。
则
$$\\exists b:\\ M(z)b=c(z)$$
等价于
$$\\operatorname{rank}(MM^{\\mathsf T})=\\operatorname{rank}(MM^{\\mathsf T}+cc^{\\mathsf T}).$$
进一步，秩相等可写成有限析取
$$\\bigvee_{t=0}^{d_1}\\left[e_t(\\Gamma)>0\\wedge e_{t+1}(\\Gamma)=0\\wedge e_{t+1}(\\Gamma')=0\\right],$$
$$\\Gamma=MM^{\\mathsf T},\\quad \\Gamma'=MM^{\\mathsf T}+cc^{\\mathsf T},\\quad
d_1=\\min(m,n).$$

*证明*：$\\operatorname{im}\\Gamma=\\operatorname{im}M$，$\\operatorname{im}\\Gamma'=\\operatorname{im}[M\\ c]$；
$Mb=c$ 有解 $\\iff c\\in\\operatorname{im}M\\iff\\operatorname{rank}\\Gamma=\\operatorname{rank}\\Gamma'$。
对半正定 $\\Gamma$，$e_t>0,e_{t+1}=0\\iff\\operatorname{rank}\\Gamma=t$；
$\\Gamma'\\succeq\\Gamma$ 保证 rank 不会更小，故最后一个条件给 $\\operatorname{rank}\\Gamma'\\le t$。
$\\square$

`c311` 在 200 个随机系统上验证了秩一致性恒等式。

### 引理 6（$(5b)$ 只依赖 $F,X$）

$$P(\\lambda)=(\\lambda I-F)XB.$$
$B$ 行满秩（$B_{:,J}=I_\\omega$），取右逆 $B^+$，则
$$\\operatorname{rank}P(\\lambda)=\\operatorname{rank}((\\lambda I-F)X).$$
所以
$$(5b)\\iff\\operatorname{rank}((\\lambda I-F)X)=\\omega\\quad\\forall\\lambda.$$

### 引理 7（谱证书）

设 $Q(\\lambda)=(\\lambda I-F)X$，$Q$ 是 $q\\times\\omega$，各 $\\omega\\times\\omega$ 子式 $m_I(\\lambda)$ 次数 $\\le\\omega$。
则
$$(5b)\\iff\\gcd_I m_I=1.$$
若 $\\omega>0$，存在 $2\\omega$ 维 Gram–Bezout 证书：
$$\\exists x\\in\\mathbb R^{2\\omega}:\\ B^{\\mathsf T}Bx=e_0,$$
其中 $B$ 由 $m_I$ 与 $\\lambda^j m_I$（$j<\\omega$）的系数向量组成；
且 $X$ 满列秩由 $e_\\omega(X^{\\mathsf T}X)>0$ 保证。

*证明*：与 277 的 Gram 证书相同；$m_I$ 无公根 ⇔ 存在 $g_I$，$\\sum g_I m_I=1$，$\\deg g_I<\\omega$；
把系数向量排成 $B$，$e_0\\in\\operatorname{row}B\\iff\\exists x:B^{\\mathsf T}Bx=e_0$。$\\square$

### 定理（固定 $q$）

对每个固定 $q$，$q1$ 可在
$$\\mathcal L^{O(q^2)}$$
时间判定（XP 型；指数依赖 $q$）。

*证明路线*：
1. 枚举 $\\omega=0,\\dots,q$；$\\omega=0$ 直接判 $H_0=H_{A,0}=0$；
2. 枚举枢轴 $J$，$\\binom{k}{\\omega}\\le k^q$；
3. 量化 $F\\in\\mathbb R^{q\\times q}$、$X\\in\\mathbb R^{q\\times\\omega}$ 与谱证书 $x\\in\\mathbb R^{2\\omega}$；
4. 写引理 5 的秩一致性公式（消去 $B$）；
5. 加 $e_\\omega(X^{\\mathsf T}X)>0$、引理 7 的谱证书；
6. 变量数 $q^2+q\\omega+2\\omega=O(q^2)$；固定 $q$ 时是常数维实代数，
   用单指数实可行性算法得 $\\mathcal L^{O(q^2)}$。

**两个方向**：
- 若 $L$ 可行，取 $X,B,F$，引理 1–6 给公式成立；
- 若公式成立，取 $B$（引理 5 保证存在），令 $H=XB$、$H_A=FXB$；
  固定行由引理 3 的方程匹配；自由行对在 $\\mathcal T$ 中，可由 $r_i$ 实现；
  $(5a)$ 由 $H_A=FXB$；$(5b)$ 由引理 7。$\\square$

## 进展

* 固定 $q$ 的完整引理链；
* 秩一致性消去 $B$（c311 精确验证）；
* 谱证书只依赖 $F,X$；
* 变量数 $O(q^2)$。

## 最终结论

* 固定 $q$ 有可检查的多项式路线，粗界 $\\mathcal L^{O(q^2)}$；
* 这是 XP，不是 FPT；与固定 $\\kappa_{\\rm obs}$ 的 FPT 互补；
* 仍需补：枢轴枚举的重复/覆盖、$\\omega=0$、比特复杂度、$D$ 的构造。

## 放弃原因

* 未写完整比特复杂度；
* 未实现；
* 未处理 $B$ 参数化的所有退化。

## 残留价值

* 一个完整的证明骨架；
* 秩一致性引理的精确陈述；
* 与 81 号路线一致。

## 相关文件

* [attempts/311](../../../q1_true/multiplication_gate/attempts/311_81_verdict_routes.md)
* [attempts/277](277_gram_fpt.md)
* `tools/verification/c311_rank_consistency.py`

## 状态

* 骨架：**[M2 纸面]**。
* 形式化/实现：**[未做]**。
