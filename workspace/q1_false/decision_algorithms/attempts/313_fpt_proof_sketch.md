> **314 补（82 号）**：$r=0$ 需单独处理（$\kappa_{\rm obs}=0$ 但 $q,k,\omega$ 可任意大）：直接判 $(5a)$，再用 $Q(\lambda)=\lambda X-G$ 的 polynomial left inverse 判 $(5b)$；$k=0$、$\omega=0$ 同样直接判。

# 固定 $\\kappa_{\\rm obs}$ 的 FPT：完整引理链

> 2026-11-10。81 号把 Gram 证书定为最强算法主线。本文件把它写成与 312 平行的引理链：
> $$\\text{固定 }\\kappa_{\\rm obs}\\Rightarrow q1\\in\\mathrm{FPT}.$$
> 变量数 $\\kappa_{\\rm obs}+2\\omega+1$，$q$ 只进多项式时间的系数计算。
> 状态：**M2（纸面骨架；索引与实例有 c278/c313 精确验证）**。

## 目标

给出固定 $\\kappa_{\\rm obs}$ 的 FPT 证明骨架，补齐 277 的索引/边界/比特复杂度。

## 设想与理由

自由行对 $(H_i,H_{A,i})=(r_iN,r_iAN)$ 落在
$$\\mathcal T=\\operatorname{row}[N\\ AN],\\qquad d_0=\\dim\\mathcal T=\\operatorname{rank}[N\\ AN].$$
每行 $d_0$ 个坐标，$r$ 行共 $\\kappa_{\\rm obs}=r d_0$ 个有效变量。
$(5a)$ 用 Gram 矩阵的初等对称多项式；$(5b)$ 用 $2\\omega$ 维 Gram–Bezout 证书；
$B^{\\mathsf T}B$ 用 Cauchy–Binet 压缩，避免枚举 $\\binom{q}{\\omega}$ 行子集。

## 做法：引理链

### 引理 1（压缩参数化）

设 $r\\ge1$。映射
$$r_i\\longmapsto(r_iN,r_iAN)=r_i[N\\ AN]$$
的像是 $\\mathcal T$，维数 $d_0$。取 $\\mathcal T$ 的有理基，每行用 $d_0$ 个坐标 $t_i$ 表示；
所有自由行共 $\\kappa_{\\rm obs}=r d_0$ 个实变量 $t$。$H,H_A$ 是 $t$ 的仿射线性函数。
且
$$k\\le d_0\\le\\kappa_{\\rm obs}.$$

*证明*：$N$ 满列秩，$N$ 的列在 $[N\\ AN]$ 中，故 $k\\le d_0$；每行 $d_0$ 个坐标，$r$ 行。$\\square$

### 引理 2（$(5a)$ 的 Gram 形式）

$$G_H=H^{\\mathsf T}H,\\qquad G_S=H^{\\mathsf T}H+H_A^{\\mathsf T}H_A.$$
则
$$\\operatorname{rank}G_H=\\operatorname{rank}H,\\qquad
\\operatorname{rank}G_S=\\operatorname{rank}\\begin{bmatrix}H\\\\H_A\\end{bmatrix}.$$
对半正定 $G$，$e_j(G)>0\\iff\\operatorname{rank}G\\ge j$。所以在 rank-$\\omega$ 层上
$$(5a)\\iff e_\\omega(G_H)>0\\ \\wedge\\ e_{\\omega+1}(G_S)=0.$$

### 引理 3（Bezout 次数界）

设实多项式 $f_1,\\dots,f_s$ 次数 $\\le\\omega$，无公复根。则存在实多项式 $g_i$，$\\deg g_i<\\omega$，使
$$\\sum_i g_i f_i=1.$$

*证明*：取非零实线性组合 $g=\\sum a_i f_i$；其复根有限。对每个根 $\\alpha$，条件 $h(\\alpha)=0$
（$h=\\sum b_i f_i$）是系数 $b$ 的真实线性子空间；有限个真子空间不能覆盖，故选 $h$ 使 $\\gcd(g,h)=1$。
Euclid 给 $ug+vh=1$，$\\deg u,\\deg v<\\omega$；展开即得。$\\square$

### 引理 4（$2\\omega$ 维 Gram 证书与索引）

设 $f_i$ 是 $P(\\lambda)=\\lambda H-H_A$ 的全部 $\\omega$-子式。令
$$B_{(i,j),t}=c_{i,t-j},\\qquad 0\\le j<\\omega,\\ 0\\le t<2\\omega,$$
其中 $c_{i,a}$ 是 $f_i$ 的 $\\lambda^a$ 系数（越界取 0）。则
$$\\operatorname{row}B=\\left\\{\\text{系数向量 of }\\sum_i g_i f_i:\\deg g_i<\\omega\\right\\},$$
$$(5b)\\iff e_0\\in\\operatorname{row}B\\iff\\exists x\\in\\mathbb R^{2\\omega}:\\ B^{\\mathsf T}Bx=e_0.$$

*证明*：$B$ 的行是 $\\lambda^j f_i$ 的系数向量，张成所有 $\\deg g_i<\\omega$ 的组合；引理 3 给 $1$ 的表示。
$\\operatorname{row}B=\\operatorname{im}(B^{\\mathsf T}B)$（实矩阵），故等价。$\\square$

### 引理 5（Cauchy–Binet 压缩）

定义
$$K(\\lambda,\\mu)=\\sum_{|J|=\\omega}\\det\\big(P(\\lambda)_{:,J}^{\\mathsf T}P(\\mu)_{:,J}\\big).$$
则
$$K(\\lambda,\\mu)=\\sum_i f_i(\\lambda)f_i(\\mu).$$
令 $S_{a,b}$ 是 $K$ 的 $\\lambda^a\\mu^b$ 系数，则
$$(B^{\\mathsf T}B)_{t,t'}=\\sum_{j=0}^{\\omega-1}S_{t-j,t'-j}.$$
$K$ 只有 $\\binom{k}{\\omega}\\le2^{\\kappa_{\\rm obs}}$ 项，每项 $\\omega\\times\\omega$ 行列式，
$P$ 的次数 1，故 $B^{\\mathsf T}B$ 可在 $f(\\kappa_{\\rm obs})\\operatorname{poly}(q,\\mathcal L)$ 时间算出。

*证明*：Cauchy–Binet 给第一式；$B$ 的索引给第二式（c313 精确验证）。$\\square$

### 定理（固定 $\\kappa_{\\rm obs}$ 的 FPT）

固定 $\\kappa_{\\rm obs}$ 时，$q1$ 可在
$$f(\\kappa_{\\rm obs})\\operatorname{poly}(\\mathcal L)$$
时间判定（$\\mathcal L$ 是输入比特长度）。

*证明路线*：
1. 处理 $r=0$（无自由行，直接检查 $L_0$）与 $k=0$（压缩问题 vacuous）；
2. 对 $\\omega=0$：$(5a)$ 迫使 $H=H_A=0$，直接判固定行是否为零；
3. 对 $\\omega=1,\\dots,\\min(q,k)$，用引理 1 的参数 $t\\in\\mathbb R^{\\kappa_{\\rm obs}}$；
4. 加 $z$ 把 $e_\\omega(G_H)>0$ 写成 $z\\,e_\\omega(G_H)=1$；加 $x\\in\\mathbb R^{2\\omega}$ 与 $B^{\\mathsf T}Bx=e_0$；
5. 变量数 $\\kappa_{\\rm obs}+2\\omega+1=f(\\kappa_{\\rm obs})$；
6. 方程个数/次数只依赖 $\\kappa_{\\rm obs}$；系数由引理 5 在 $f(\\kappa)\\operatorname{poly}(q,\\mathcal L)$ 时间算出；
7. 单指数实可行性算法给 $f(\\kappa)\\operatorname{poly}(\\mathcal L)$。

**方向**：可行 $L$ ⇒ 取 $t$ 坐标、$x$ 证书，公式成立；公式成立 ⇒ 由 $t$ 还原自由行（引理 1），
$H,H_A$ 满足 $(5a)$（引理 2）与 $(5b)$（引理 4）。$\\square$

## 验证

- `c313`：244 铅笔上验证索引公式 $(B^{\\mathsf T}B)_{t,t'}=\\sum_j S_{t-j,t'-j}$ 与 $e_0\\in\\operatorname{row}B$，PASS；
- `c278`：244 上验证 $B^{\\mathsf T}Bx=e_0$、Cauchy–Binet、$e_2(G_H)=55$、$e_3(G_S)=0$，PASS。

## 进展

* 完整 FPT 引理链；
* 索引修正（$c_{i,t-j}$）；
* $\\omega=0$、$r=0$、$k=0$ 的边界；
* $q$ 只进多项式系数计算。

## 最终结论

* 固定 $\\kappa_{\\rm obs}$ 的 FPT 有可检查骨架；
* 仍需把比特复杂度写成显式引理（Gaussian elimination、行列式、QE 界）；
* 这是当前最成熟的算法主线。

## 放弃原因

* 未写显式比特复杂度常数；
* 未实现；
* 未 Lean 化。

## 残留价值

* 与 312 平行的完整骨架；
* 两个精确验证脚本；
* 论文算法部分的基础。

## 相关文件

* [attempts/277](277_gram_fpt.md)
* [attempts/278](278_gram_certificate_instance.md)
* [attempts/312](312_fixed_q_proof_sketch.md)
* `tools/verification/c313_gram_indexing.py`

## 状态

* 骨架：**[M2 纸面]**。
* 形式化/实现：**[未做]**。
