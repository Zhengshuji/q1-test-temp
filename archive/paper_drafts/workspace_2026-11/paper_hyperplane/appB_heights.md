# 附录 B 高度与算术界

本附录给第 5 节各引理的**可核对细节**：每一步的比特长如何被 $\mathrm{poly}(n,\tau)$ 控制。记号与第 2、5 节一致：$A\in\mathbb R^{n\times n}$、$C\in\mathbb R^{p\times n}$、$L_0\in\mathbb R^{r_0\times n}$、$\mathcal L=[L_0;R]$（$q$ 行、行满秩）、$K_0=\ker[C;CA]$、$k=\dim K_0$、$\rho=\operatorname{rank}[C;CA]=n-k$、$N\in\mathbb R^{n\times k}$ 为 $K_0$ 的基、$M=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$、$\omega=\operatorname{rank}H$（$H=\mathcal L N$）、$s=q-k+1$、$\delta=\dim V_0-\dim(V_0\cap K_0)$。$\tau$ 为输入 $(A,C,L_0)$ 与 $q$ 的二进制编码长度，即所有整数分子与分母的最大比特长。

**约定.** 对整数或分数 $x$，记 $\beta(x)$ 为其分子与分母比特长的最大值，即 $\beta(x)=\lceil\log_2|x|\rceil+1$（整数情形即通常的比特长）。对矩阵 $X$ 记 $\beta(X)=\max_{i,j}\beta(X_{ij})$，$\|X\|_\infty=\max_{i,j}|X_{ij}|$。所有对数以 2 为底。本附录的界**不追求最优常数**，只要求形状为 $\mathrm{poly}(n,\tau)$。

**为什么需要这份附录.** 第 5 节的证明依赖"所有中间量都不大"。这种话在三条路径上都可能失效，本附录逐一封住：

1. **分母**：清分母之后矩阵是整数，但清分母本身可能引入巨大的公共因子（B.1 处理）；
2. **子式**：核基、特征向量、伴随矩阵的元素都是子式之比，子式可以比原矩阵大得多（Hadamard 界，B.1–B.2 处理）；
3. **求逆与 gcd**：$(N^{\mathsf T}N)^{-1}$ 与 $K(X)[\lambda]$ 上的 gcd 都可能让分子分母爆炸（B.2 用 $\det\ge1$ 处理前者，第 5.6 节用子结式处理后者，B.5.2 补充结式的情形）。

三者都有界之后，第 5 节定理的"$\mathrm{poly}(n,\tau)$"才是一个可核对的断言，而不是一句估计。

---

## B.1 压缩基的规范化

第 2.1 节引用了"$K_0$ 的一个基 $N$"，这里把取法定死，并给出它的比特长。共四步。

**第 1 步：清分母.** 把 $[C;CA]\in\mathbb R^{2p\times n}$ 的每个元素写成既约分数。设其分母的最小公倍数为 $D_0$，令
$$\widehat W:=D_0\begin{bmatrix}C\\ CA\end{bmatrix}\in\mathbb Z^{2p\times n}.$$
$[C;CA]$ 共有 $2pn$ 个元素，每个分母的比特长 $\le\tau$，故
$$\beta(D_0)\le 2pn\tau,\qquad \beta(\widehat W)\le \tau+2pn\tau=:\beta_W .$$
（用乘积而非最小公倍数代替 $D_0$ 得到同样的量级，本附录不追求 $D_0$ 的最优。）

**第 2 步：无分数消元求核.** 对 $\widehat W$ 作 Bareiss（无分数）消元。Bareiss 的关键性质是：所有中间量都是 $\widehat W$ 的**子式**，不产生分数。于是中间量的比特长受子式界控制。对任意 $j\times j$ 子矩阵，Hadamard 界给出
$$|\det|\le\prod_{i=1}^{j}\|\text{row}_i\|_2\le\bigl(\sqrt{j}\,\|\widehat W\|_\infty\bigr)^{j},$$
故
$$\log_2|\det|\le \tfrac{j}{2}\log_2 j+j\,\beta_W\le \tfrac{\rho}{2}\log_2\rho+\rho\,\beta_W ,$$
其中 $j\le\rho$（$[C;CA]$ 的秩）。这一步的算术次数是 $O(p\,n\,\min(p,n))$，每个运算作用在 $\mathrm{poly}(n,\tau)$ 位的整数上，故位时间为 $\mathrm{poly}(n,\tau)$。

**第 3 步：核基与清分母.** 消元后读出 $K_0$ 的基：每个坐标是一个 $\rho\times\rho$ 子式与一个非零 $\rho\times\rho$ 主子式之比，故

$$\beta(\text{坐标})\le 2\Bigl(\tfrac{\rho}{2}\log_2\rho+\rho\,\beta_W\Bigr)=:2\beta_K .$$

把每列乘以各分母的最小公倍数，得到**整数**列。

**第 4 步：本原化.** 对整数列的每个列向量，除以它所有分量的最大公约数 $g$。因为 $g\ge1$ 是整数，除以它只会**减小**每个分量的绝对值，故比特长不增加：$\beta(N)\le 2\beta_K$。

**引理 B.1（压缩基）.**
$$\beta(N)\le 2\beta_K=2\Bigl(\tfrac{\rho}{2}\log_2\rho+\rho\,\beta_W\Bigr),\qquad \beta_W=\tau+2pn\tau .$$
基 $N$ 可在 $\mathrm{poly}(n,\tau)$ 位时间内算出。

*说明.* 四步的算术次数都是 $n$ 的多项式；每步的每个运算作用在 $\mathrm{poly}(n,\tau)$ 位的整数上；位时间等于"算术次数 × 单位运算的位代价"，故为 $\mathrm{poly}(n,\tau)$。$\square$

**为什么本原化是必要的一步.** 若不清分母、不除公约数，$N$ 的列可能带有公共的有理因子，使 $N^{\mathsf T}N$ 的行列式变成极小的分数，进而让 $M$ 的分子分母同时膨胀。本原化把 $\det(N^{\mathsf T}N)$ 拉回整数（见 B.2），这是后文所有界的基础。

**B.1.1 为什么 Bareiss 的中间量是子式.** 无分数消元在第 $t$ 步把元素更新为
$$a^{(t+1)}_{ij}=\frac{a^{(t)}_{tt}a^{(t)}_{ij}-a^{(t)}_{it}a^{(t)}_{tj}}{a^{(t-1)}_{t-1,t-1}},$$
分母恰是上一步的枢轴。归纳可见：$a^{(t)}_{ij}$ 等于"由前 $t$ 行与第 $i$ 行、前 $t$ 列与第 $j$ 列组成的 $(t+1)$ 阶子式"除以"前 $t-1$ 步的枢轴乘积"。因此**每个中间量都是子式（至多差一个已知的整数因子）**，其比特长由 Hadamard 界统一控制，而不需要逐步估计增长。这正是用 Bareiss 而不用带分数的高斯消元的原因。

**B.1.2 算术次数.** 消元是 $O(\rho^{2}n)$ 次域运算；读核基、清分母、求每列最大公约数各是 $O(nk)$ 次整数运算；最大公约数用欧几里得算法，代价是操作数比特长的多项式。总计 $\mathrm{poly}(n)$ 次算术。

---

## B.2 压缩矩阵的高度

**引理 B.2（压缩矩阵）.**
$$\beta(N^{\mathsf T}N)\le 2\beta(N)+\log_2 n,\qquad \beta(N^{\mathsf T}AN)\le 2\beta(N)+\tau+2\log_2 n,$$
且 $M$ 的元素满足
$$\beta(M)\le (k-1)\Bigl(\tfrac12\log_2 k+\beta(N^{\mathsf T}N)\Bigr)+\beta(N^{\mathsf T}AN)+\beta\bigl(\det(N^{\mathsf T}N)\bigr),$$
右端是 $\mathrm{poly}(n,\tau)$。

*证明.* (i) $N^{\mathsf T}N$ 的元素是 $\sum_{l=1}^{n}N_{li}N_{lj}$，共 $n$ 项，每项 $\le 2^{2\beta(N)}$，故比特长 $\le 2\beta(N)+\log_2 n$。

(ii) $N^{\mathsf T}AN$ 的元素是 $\sum_{l,m}N_{li}A_{lm}N_{mj}$，共 $n^{2}$ 项，每项 $\le 2^{2\beta(N)+\tau}$，故比特长 $\le 2\beta(N)+\tau+2\log_2 n$。

(iii) $\det(N^{\mathsf T}N)$ 是**正整数**：$N$ 是实矩阵且列满秩，$N^{\mathsf T}N$ 正定；又 $N$ 是整数矩阵，故 $N^{\mathsf T}N$ 是整数矩阵、行列式为正整数，于是
$$\det(N^{\mathsf T}N)\ge 1 .$$
这条下界是关键的：它说明 $(N^{\mathsf T}N)^{-1}=\operatorname{adj}(N^{\mathsf T}N)/\det(N^{\mathsf T}N)$ 的分母不会把分子"挤小"，分子只需由伴随矩阵的界控制。

(iv) $M=\operatorname{adj}(N^{\mathsf T}N)\,N^{\mathsf T}AN/\det(N^{\mathsf T}N)$。伴随矩阵的元素是 $k-1$ 阶子式，由 Hadamard 界
$$\beta\bigl(\operatorname{adj}(N^{\mathsf T}N)\bigr)\le (k-1)\Bigl(\tfrac12\log_2 k+\beta(N^{\mathsf T}N)\Bigr).$$
乘上 $N^{\mathsf T}AN$、再以 $\det(N^{\mathsf T}N)$ 为分母，比特长是三者之和，即所述。$\square$

**推论 B.2.1.** $M$ 的元素的比特长是 $\mathrm{poly}(n,\tau)$；特别地，存在常数 $c_1$ 使
$$\beta(M)\le c_1\bigl(n^{3}\tau+n^{2}\log_2 n\bigr).$$
（本附录不优化 $c_1$；重要的是它是 $n$ 与 $\tau$ 的多项式。）

---

## B.3 特征多项式与根高度

**引理 B.3（特征多项式）.**
$$\beta(\chi_M)\le k\bigl(\beta(M)+\tfrac12\log_2 k\bigr)+\beta(M)+k=\mathrm{poly}(n,\tau),$$
其中 $\beta(\chi_M)$ 指清分母并取本原部分后系数的比特长。

*证明.* $\chi_M(t)=t^{k}+\sum_{i=1}^{k}(-1)^{i}\sigma_i(M)\,t^{k-i}$，$\sigma_i$ 是 $i$ 阶主子式之和。每个 $i$ 阶子式由 Hadamard 界控制在 $(\sqrt{i}\|M\|_\infty)^{i}$ 以内；求和至多 $\binom{k}{i}$ 项，只增加 $\log_2\binom{k}{i}\le k$ 位。清分母引入 $M$ 各元素分母的乘积，其对数同样是 $\mathrm{poly}(n,\tau)$。计算可用 Faddeev–LeVerrier 或插值法，算术次数 $\mathrm{poly}(n)$。$\square$

**引理 B.4（根的高度与次数）.** 设 $\mu$ 是 $\chi_M$ 的任一复根。则
$$[\mathbb Q(\mu):\mathbb Q]\le k\le n,\qquad h(\mu)\le \beta(\chi_M)+\tfrac12\log_2(k+1)+\log_2 2,$$
其中 $h$ 是对数绝对高度
$$h(\mu)=\frac{1}{[\mathbb Q(\mu):\mathbb Q]}\sum_{\sigma}\log^{+}|\sigma(\mu)|,\qquad \log^{+}x=\max\{0,\log x\},$$
求和跑遍 $\mu$ 的全部共轭。

*证明.* 次数不超过 $\deg\chi_M=k$。高度：$\mu$ 是整系数多项式 $\chi_M$ 的根，系数比特长 $\beta(\chi_M)$；Cauchy 界给出
$$|\mu|\le 1+\max_{i}\frac{|a_i|}{|a_k|}\le 1+2^{\beta(\chi_M)}\le 2^{\beta(\chi_M)+1},$$
于是每个共轭的 $\log^{+}|\sigma(\mu)|\le\beta(\chi_M)+1$；再除以次数，得所述界。$\square$

**推论 B.4.1.** $h(\mu)=\mathrm{poly}(n,\tau)$；实根可用精确实根隔离在 $\mathrm{poly}(n,\tau)$ 位时间内分离为互不相交的有理区间。

**注 B.3.1.** 引理 B.4 的界对**有理**根同样成立（此时 $h(\mu)=\log\max\{1,|\mu|\}$），故下文对有理与无理特征值用同一套估计，不需要分支。

**B.3.2 这些界是不是空的.** 取最坏但常见的量级：$\tau=1$（$0/1$ 输入）、$n=8$、$\rho=4$、$p=2$。则

$$\beta_W\le 1+2\cdot2\cdot8\cdot1=33,\qquad \beta_K\le \tfrac{4}{2}\log_2 4+4\cdot33=4+132=136,\qquad \beta(N)\le 272 .$$

接着 $\beta(N^{\mathsf T}N)\le 2\cdot272+\log_2 8=547$，$\beta(M)$ 是 §B.2 的三项之和，量级在 $4\times10^{3}$ 比特以内。也就是说：对 $n=8$ 的实例，所有中间量都在几千比特的量级，完全可算。这些界的作用不是给出可行规模，而是证明"不随输入规模指数爆炸"。

---

## B.4 特征向量与纤维基

**引理 B.5（$K$ 上的基）.** 设 $\mu$ 是 $\chi_M$ 的实根、$K=\mathbb Q(\mu)$、$d=[K:\mathbb Q]\le n$。则：

1. $E_\mu=\ker(M-\mu I)$ 在 $K$ 上有一个本原向量 $a$，其坐标（$K$ 元素的坐标表示）的比特长 $\le \beta_K':=2\bigl(\tfrac{k}{2}\log_2 k+k(\beta(M)+\beta(\mu))\bigr)$；
2. $E_\mu^0$、$U_v^\perp$、$D_v=K_0\cap U_v^\perp$、$\mathcal Q_v/\overline V_{0,v}$ 的基都可在 $K$ 上算出，比特长同为 $\mathrm{poly}(n,\tau)$；
3. 全部计算的位时间为 $\mathrm{poly}(n,\tau)\cdot\mathrm{poly}(d,\beta_K')=\mathrm{poly}(n,\tau)$。

*证明.* (1) $a$ 是 $(M-\mu I)\in K^{k\times k}$ 的核，用 Cramer 法则：其坐标是 $(k-1)$ 阶子式（在 $K$ 上）与非零 $(k-1)$ 阶主子式之比。$K$ 元素的算术代价是 $\mathrm{poly}(d,\beta(\mu))$ 位（标准事实 (S3)），子式的界由 Hadamard 与 $\beta(M)$、$\beta(\mu)$ 给出，故坐标为 $K$ 元素、其坐标表示的比特长为所述。清分母、除公约数后得到本原向量。

(2) 四者分别是 $K$ 上矩阵的核、像、和与商：$E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN)$ 是两个线性条件的交；$U_v^\perp=\{x:\langle x,v\rangle=\langle x,Av\rangle=0\}$；$D_v$ 是 $K_0$ 上两条泛函的公共核；$\mathcal Q_v/\overline V_{0,v}$ 是商空间的一组补基。四者的矩阵规模都 $\le n$，用同一套无分数消元，中间量是子式，故比特长同上。

(3) $K$ 上每次算术 $\mathrm{poly}(d,\beta)$ 位，消元的算术次数是 $n$ 的多项式，$d\le n$。$\square$

**注 B.4.1（必须在 $K$ 上算）.** 当 $\mu\notin\mathbb Q$ 时，$E_\mu$ 是 $K$ 上的一条直线，而不是 $\mathbb Q$ 上的一维空间：它在 $\mathbb Q$ 上的"迹"是 $d$ 个共轭直线的直和，维数 $d$。若在 $\mathbb Q$ 上算核，会把一条方向错误地拆成 $d$ 条共轭方向，随后的纤维构造与铅笔都会变。因此方向枚举与纤维构造必须与 $\mu$ 落在同一个 $K$ 里。

**注 B.4.2（标量积与范数）.** 上述空间都在 $\mathbb R^n$ 里，正交补与投影按标准欧氏内积取；$v$ 是 $K$ 上的向量，但 $\langle\cdot,\cdot\rangle$ 的值落在 $K$ 里（因为 $A$、$C$、$L_0$ 都取有理数，$\mu$ 是 $\chi_M$ 的根）。故 $D_v$、$U_v^\perp$ 的方程系数在 $K$ 里，无需扩域。

**B.4.3 $K$ 上算术的代价，具体写出来.** 设 $K=\mathbb Q[\mu]/(f)$，$f$ 是 $\mu$ 的极小多项式，次数 $d\le n$、系数比特长 $\beta(f)\le\beta(\chi_M)$。元素用坐标 $(c_0,\dots,c_{d-1})$ 表示，$c_i$ 是比特长 $\le\beta_K'$ 的有理数。则：

- 加法：$d$ 次基域加法，代价 $O(d\beta_K')$；
- 乘法：先做 $d^{2}$ 次基域乘法（代价 $O(d^{2}\beta_K'^{2})$），再把 $2d-2$ 次的结果模 $f$ 约化（$d$ 次多项式除法，代价 $O(d^{2}\beta_K'^{2})$）；
- 求逆：扩展欧几里得，代价 $O(d^{2}\beta_K'^{2})$。

三者都是 $\mathrm{poly}(d,\beta_K')$ 位，与引理 B.5 (3) 一致。**关键点**：这些代价里没有"随 $\mu$ 与有理数距离"增长的量——$K$ 的算术是精确的代数运算，不需要把 $\mu$ 数值化。

---

## B.5 图卡的规模

固定一个实特征值 $\mu$、一条方向 $[v]\in\mathbb P(E_\mu^0)$ 与纤维
$$\operatorname{Gr}\bigl(m,\ \mathcal Q_v/\overline V_{0,v}\bigr),\qquad m=s-\delta .$$
记商丛的秩 $\widetilde r:=r(v)-\delta$，其中 $r(v)=\rho$（特征方向）或 $\rho-1$（非特征方向），$\delta=\dim V_0-\dim(V_0\cap K_0)$。

**引理 B.6（图卡规模）.**

1. **参数个数.** $d_{\mathrm{chart}}=m(\widetilde r-m)\le \widetilde r^{2}/4\le p^{2}$。
2. **次数.** 图卡行 $\mathrm{comp}_i+\sum_{j}X_{ij}\mathrm{comp}_{m+j}$ 对 $X$ 仿射；铅笔 $\lambda H-H_A$ 对 $\lambda$ 线性；故 $\omega\times\omega$ 极大子式对 $X$ 与 $\lambda$ 的次数都 $\le\omega$。
3. **子式个数.** $\binom{q}{\omega}\binom{k}{\omega}=k\binom{q}{s}$，且
$$k\binom{q}{s}\le n\sum_{j=0}^{2p+1}\binom{n}{j}=n^{O(p)} .$$
4. **图卡数.** $\mathrm{Gr}(m,\widetilde r)$ 的标准图卡数为 $\binom{\widetilde r}{m}\le 2^{\widetilde r}\le 2^{2p}$。
5. **块数.** 实特征值至多 $k\le n$ 个，每个至多一条方向（几何单谱），故总图卡数 $\le n\cdot 2^{2p}$。
6. **稠密规模.** 每个子式是"$\lambda$ 次数 $\le\omega$、$X$ 次数 $\le\omega$、$d_{\mathrm{chart}}$ 个变量"的多项式，其稠密规模为
$$D=\omega\binom{d_{\mathrm{chart}}+\omega}{d_{\mathrm{chart}}}\le n\binom{n+p^{2}}{p^{2}}=n^{O(p^{2})}.$$

*证明.* (1) $\widetilde r\le r(v)\le\rho\le 2p$；$x\mapsto x(\widetilde r-x)$ 在 $x=\widetilde r/2$ 取最大，故 $d_{\mathrm{chart}}\le\widetilde r^{2}/4\le p^{2}$。

(3) $\omega=k-1$，故 $\binom{k}{\omega}=k$；非空条件 $s\le r(v)\le\rho\le2p$，故 $\binom{q}{s}\le\sum_{j\le2p}\binom{n}{j}$；乘以 $k\le n$ 得所述。

(4) $\binom{\widetilde r}{m}\le\sum_{j}\binom{\widetilde r}{j}=2^{\widetilde r}$。

(6) 把 $D$ 展开：$\binom{d+\omega}{d}\le (e(d+\omega)/d)^{d}$，其中 $d\le p^{2}$ 是常数（$p$ 固定），$\omega\le n$，故 $D\le n\cdot(\text{常数})^{p^{2}}\cdot n^{p^{2}}=n^{O(p^{2})}$。$\square$

**注 B.5.1（$p$ 固定时 $D$ 是多项式）.** $D=n^{O(p^{2})}$ 的指数含 $p^{2}$，但 $p$ 固定，故 $D$ 是 $n$ 的多项式。这正是本文"固定 $p$"的含义；若 $p$ 随 $n$ 增长，$D$ 不再是多项式。

**B.5.2 结式的比特长（供第 4 节的充分判据使用）.** 第 4 节的"结式判据"用一对 $\omega$ 次 $\lambda$-多项式的结式作为"生成好"的**充分**条件。它的比特长也是 $\mathrm{poly}(n,\tau)$：结式是 $2\omega$ 阶 Sylvester 矩阵的行列式，元素是 $X$ 的多项式（次数 $\le\omega$、系数高度 $\le H$）；由 Hadamard 界，
$$\beta(\operatorname{Res})\le 2\omega\bigl(\tfrac12\log_2(2\omega)+\beta_{\min}\bigr),$$
其中 $\beta_{\min}$ 是 Sylvester 元素（作为 $X$ 的多项式系数）的比特长。于是"某个结式不恒为零"这个判据的验证代价与 B.5 (6) 同量级。**注意**：结式判据只是充分的；它的否定不构成"全坏"的证书（见第 4 节的反例）。

---

## B.6 汇总与依赖

| 条目 | 量 | 界 | 依据 |
|---|---|---|---|
| B.1 | $\beta(N)$ | $2\bigl(\tfrac{\rho}{2}\log_2\rho+\rho\beta_W\bigr)$ | Bareiss + Hadamard |
| B.2 | $\beta(M)$ | $\mathrm{poly}(n,\tau)$（推论 B.2.1） | 伴随矩阵 + $\det\ge1$ |
| B.3 | $\beta(\chi_M)$ | $\mathrm{poly}(n,\tau)$ | 主子式之和 |
| B.4 | $h(\mu)$、$[K:\mathbb Q]$ | $\le\beta(\chi_M)+O(\log k)$、$\le n$ | Cauchy 界 |
| B.5 | $\beta(\text{特征向量与基})$ | $\mathrm{poly}(n,\tau)$ | Cramer + (S3) |
| B.6 | $d_{\mathrm{chart}}$、子式数、图卡数、$D$ | $\le p^{2}$、$n^{O(p)}$、$\le2^{2p}$、$n^{O(p^{2})}$ | 组合计数 |

**标准事实（引用，不在本文证明）：**

- **(S1)** 整系数多项式分解（LLL 型），$\mathrm{poly}(N,\beta)$ 位。
- **(S2)** 实根隔离，$\mathrm{poly}(N,\beta)$ 位。
- **(S3)** 代数数域 $K=\mathbb Q[\mu]/(f)$ 的算术：加减乘求逆是 $\mathrm{poly}(d,h)$ 位，零判定精确。
- **(S4)** 子结式：给出分式域上 gcd 的本原部分，中间量是 Sylvester 子矩阵的行列式，比特长受输入次数与高度的多项式控制。

**本附录自己算的：**

- 清分母与 Bareiss 的具体比特长（B.1）；
- $\det(N^{\mathsf T}N)\ge1$ 及其对逆矩阵分子分母的控制（B.2）；
- $\chi_M$ 系数与根高度的显式界（B.3）；
- 特征向量与纤维基在 $K$ 上的比特长（B.4）；
- 图卡规模与稠密规模 $D$ 的计数（B.5）。

**未声称的：** 本附录不给最优常数，也不给"$K$ 上算术"的最优位复杂度；这两者都不影响第 5 节定理的形状。

**B.6.1 与第 5 节的对应表.**

| 第 5 节 | 用到的本附录条目 |
|---|---|
| 引理 5.1（压缩高度） | 引理 B.1、引理 B.2、推论 B.2.1 |
| 引理 5.2（特征多项式高度） | 引理 B.3 |
| 引理 5.3（根高度与次数） | 引理 B.4、推论 B.4.1、注 B.4.2 |
| 引理 5.4（特征向量与纤维基） | 引理 B.5、注 B.4.1、注 B.4.2、B.4.3 |
| 引理 5.5（图卡规模） | 引理 B.6、注 B.5.1 |
| 引理 5.6、5.7（子结式与多多项式 gcd） | 第 5.6 节（标准事实 (S4)）；本附录 B.5.1 补结式的比特长 |
| 定理 5.1 | 以上全部 |

**B.6.2 界之间的关系.** 文中的界按如下顺序逐层建立，后一层用前一层：

$$\beta(\widehat W)\ \longrightarrow\ \beta(N)\ \longrightarrow\ \beta(N^{\mathsf T}N),\ \beta(N^{\mathsf T}AN)\ \longrightarrow\ \beta(M)\ \longrightarrow\ \beta(\chi_M)\ \longrightarrow\ h(\mu),\ [K:\mathbb Q]\ \longrightarrow\ \beta(\text{特征向量与基}).$$

每一层的界都只依赖前一层与输入参数 $(n,p,\tau)$，没有循环。这是本附录可以独立核对的原因。
