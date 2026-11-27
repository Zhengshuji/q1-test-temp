# DEC / OPT / FIND 在参数 $\ell=\operatorname{rank}(AN)$ 下的 FPT 性：完整纸面证明

> 目标：给出**完整、可逐行检查**的纸面证明，不依赖 Lean。Lean 只作为骨架佐证，列在 §9。
> 记号与论文一致；$k=\dim\ker[C;CA]$、$N$ 是 $K_0$ 的基、$M=[N\ AN]$、$T=\operatorname{row}M$、
> $d=\dim T$、$W_0=\operatorname{row}(L_0M)$、$s_0=\dim W_0$、$\ell=\operatorname{rank}(AN)$、
> $S=\operatorname{row}(AN)\subseteq\mathbb R^k$（$S$ 是**第二个分量**里的子空间）。
> $\mathcal L$ 是输入的二进制长度，$k\le n\le\mathcal L$。

---

## 0. 主定理

**定理.** 设 $A\in\mathbb Q^{n\times n}$、$C\in\mathbb Q^{p\times n}$、$L_0\in\mathbb Q^{r_0\times n}$、
$q\ge r_0$ 为整数，$r=q-r_0$，自由行 $R\in\mathbb R^{r\times n}$ 任意（允许冗余行与零行）。
记 $\ell=\operatorname{rank}(AN)\le k$。则

1. $\mathrm{DEC}(q)$ 可在 $\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L)$ 位运算内判定；
2. 若可行，可在同阶时间内给出**精确的实代数数**见证 $R$（$\mathrm{FIND}$）；
3. 最小可行行槽数 $q_{\min}=r_0+t_{\min}$ 可在同阶时间内求出（$\mathrm{OPT}$），
   其中 $t_{\min}\le2\ell$；若无可行 $W$，约定 $q_{\min}=+\infty$。

**适用范围（必须随定理一起陈述）**：这是**行槽模型**（row-slot）：$L=[L_0;R]$ 的行数就是 $q$，
允许冗余行、零行，条件只有论文的 $(5a)(5b)$。控制论文献中按 $\operatorname{rank}[C;L]-\operatorname{rank}C$
定义的**约化阶**是另一个问题：零填充不增加约化阶，所以本文的单调性与 $q_{\min}$ 公式不能搬过去。

**行槽模型本身为什么有意义**：观测器中“可用的行槽”（传感器通道数、设计槽位数）常常本身就是资源，
与某一行是否冗余无关；允许冗余行、按行计费，是把“设计成本 = 用了多少行”直接写进问题里的自然模型。
约化阶模型把冗余行免费化，适合“最小实现”的语境；两者是不同的优化目标，不是同一问题的粗细版本。

---

## 0.1 输入与输出模型（专家 90 号 §14 要求显式）

- **输入**：$A,C,L_0$ 的有理元素以二进制给出，总位长 $\mathcal L$；$q$ 以一元给出。
- **DEC 的输出**：一个比特。
- **OPT 的输出**：$q_{\min}$（一元）或 $+\infty$ 的标记。
- **FIND 的输出**：$R$ 的**精确实代数数**表示（一元表示 + 隔离区间），位长 $\le L_{\rm out}$（引理 9）。
  不承诺有理见证：非空实代数集未必含有点。

---

---

## 1. 归约：可行性只依赖压缩行对子空间 $W$

**定义.** $B=LM=[H\ H_A]\in\mathbb R^{q\times2k}$，$W=\operatorname{row}B\subseteq\mathbb R^{2k}$。
$\pi_1(h,g)=h$、$\pi_2(h,g)=g$、$\pi_\lambda(h,g)=\lambda h-g$，都从 $\mathbb R^{2k}=\mathbb R^k\times\mathbb R^k$ 出发。

**引理 1（压缩）.** 记 $J=[CA;C]$，则对任意 $Q\in\mathbb R^{m\times n}$，
$$\operatorname{rank}\begin{bmatrix}J\\Q\end{bmatrix}=\operatorname{rank}J+\operatorname{rank}(QN).$$

*证明.* $N$ 的列是 $\ker J$ 的基。对行空间作分解（或对线性映射 $Q$ 限制到 $\ker J$，再用秩-零化度），
$\operatorname{row}[J;Q]/\operatorname{row}J\cong\operatorname{row}(QN)$，取维数即得。∎

**引理 2（两个条件）.** $(5a)\iff\pi_2(W)\subseteq\pi_1(W)$；$(5b)\iff\dim\pi_\lambda(W)=\dim\pi_1(W)$ 对所有 $\lambda\in\mathbb C$。

*证明.* 在引理 1 中取 $Q=[LA;L]$：$\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}J+\operatorname{rank}([H_A;H])$；
而 $(5a)$ 的右边是 $\operatorname{rank}[L;CA;C]=\operatorname{rank}J+\operatorname{rank}H$。两者相等
$\iff\operatorname{rank}[H_A;H]=\operatorname{rank}H\iff\operatorname{row}H_A\subseteq\operatorname{row}H
\iff\pi_2(W)\subseteq\pi_1(W)$。
取 $Q=\lambda L-LA$：$\operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}J+\operatorname{rank}(\lambda H-H_A)$，
右边为 $\operatorname{rank}J+\operatorname{rank}H$；相等 $\iff\operatorname{rank}(\lambda H-H_A)=\operatorname{rank}H$。

**复数化（专家 90 号 §1.2 要求，严格性所必需）**：$W$ 是实子空间，而 $\lambda$ 取复值，
所以 $(5b)$ 里的 $\pi_\lambda$ 必须在复化空间上理解：
$$W_{\mathbb C}=W\otimes_{\mathbb R}\mathbb C\subseteq\mathbb C^{2k},\qquad
\pi_\lambda:W_{\mathbb C}\to\mathbb C^k .$$
因实矩阵在 $\mathbb R$ 与 $\mathbb C$ 上秩相同，$\operatorname{rank}_{\mathbb C}(\lambda H-H_A)$ 对实 $\lambda$
等于实秩；对复 $\lambda$ 则只有复数化后才良定义。以下凡写 $\pi_\lambda(W)$ 均指 $\pi_\lambda(W_{\mathbb C})$，
其维数在 $\mathbb C$ 上计。∎

**引理 3（沙包与可实现性）.** 对 $L=[L_0;R]$：$W_0\subseteq W\subseteq T$ 且 $\dim(W/W_0)\le r$。
反之，任一满足这三条的子空间 $W$ 都可由某个 $R$ 用恰好 $t=\dim(W/W_0)$ 个自由行实现。

*证明.* 前半：$W=\operatorname{row}(L_0M)+\operatorname{row}(RM)$，故 $W\supseteq W_0$ 且 $W\subseteq T$；
$\dim(W/W_0)\le\operatorname{rank}(RM)\le r$。
后半：$u\mapsto uM$ 是 $\mathbb R^n\to T$ 的满射；取 $W/W_0$ 的一组基 $w_1,\dots,w_t$，
选原像 $u_i$ 使 $u_iM=w_i$，令 $R$ 的前 $t$ 行为 $u_i$、其余为零。则 $\operatorname{row}(RM)$ 模 $W_0$ 张成 $W/W_0$，
故 $W_0+\operatorname{row}(RM)=W$。∎

---

## 2. 结构界

**引理 4.** 若 $W$ 可行且 $\omega=\dim\pi_1(W)>0$，则
$$\omega+1\le\dim W\le2\omega.$$

*证明.* 上界：由引理 2，$\pi_2(W)\subseteq\pi_1(W)$；$(5b)$ 在 $\lambda=0$ 处给出
$\dim\pi_0(W)=\dim\pi_1(W)=\omega$，而 $\pi_0(W)=\pi_2(W)$（差一个符号，维数不变）。
于是 $\pi_2(W)=\pi_1(W)=:U$，$W\subseteq U\times U$，故 $\dim W\le2\dim U=2\omega$。
下界：若 $\dim W=\omega$，则 $\pi_1|_W$ 与 $\pi_2|_W$ 都是同构，$W$ 是某 $F:U\to U$ 的图，$g=Fh$。
$\mathbb C$ 上 $F$ 有特征值 $\lambda_0$；在 $\lambda_0$ 处 $\pi_{\lambda_0}(W)=(\lambda_0 I-F)U$ 的维数 $<\omega$，
与 $(5b)$ 矛盾。$\omega=0$ 时由 $\pi_2(W)\subseteq\pi_1(W)=0$ 得 $W=0$。∎

**推论.** $s_0+t=\dim W\in\{\omega+1,\dots,2\omega\}\cup\{0\}$，故
$$\max(0,\omega+1-s_0)\le t\le\min(r,\ 2\omega-s_0).$$

---

## 3. 最小阶与单调性

**引理 5（单调与饱和）.** $\mathrm{DEC}(q)\Rightarrow\mathrm{DEC}(q+1)$；且当 $r\ge d-s_0$ 时
$\mathrm{DEC}(r_0+r)=\mathrm{DEC}(r_0+d-s_0)$。

*证明.* 补零行：$H'=[H;0]$、$H_A'=[H_A;0]$，秩与铅笔的秩全不变。饱和：$\dim(W/W_0)\le\dim(T/W_0)=d-s_0$。∎

**引理 6.** $q_{\min}=r_0+t_{\min}$，其中 $t_{\min}=\min\{\dim(W/W_0):W\text{ 可行}\}$，且 $t_{\min}\le2\ell$。

*证明.* 引理 3 说明可行性 $\iff$ 存在可行 $W$ 且 $\dim(W/W_0)\le r$；单调性说明最小的 $r$ 就是 $t_{\min}$，
故 $q_{\min}=r_0+t_{\min}$。上界：可行 $W$ 满足 $W\subseteq U\times U$，$U\subseteq S$，
$\dim U=\omega\le\ell$，故 $\dim W\le2\omega\le2\ell$，于是
$$t_{\min}=\dim(W/W_0)=\dim W-s_0\le2\ell .$$
（更紧的界是 $t_{\min}\le2\omega-s_0$。）∎

> 注意：$t_{\min}\le2\ell$ 而不是 $\le\ell$。可行 $W$ 的维数可以到 $2\omega$（是两个 $\omega$ 维空间的关系），
> 只减去 $s_0$ 得到的是 $t$。二分区间因此取 $[0,2\ell]$。

---

## 4. 坐标变换到 $S$（关键的一步，之前漏了）

设 $W$ 可行。由引理 4 的证明，$\pi_1(W)=\pi_2(W)=U\subseteq S$，$W\subseteq U\times U\subseteq S\times S$。
因此在 $S$ 的基下写坐标，$W$ 变成 $\mathbb R^\ell\times\mathbb R^\ell$ 的子空间，
所有对象（$H$、$H_A$ 的行）都落在这个 $\ell$ 维空间里。

**引理 7.** 存在有理可逆矩阵 $Y_S$（把 $S$ 的基写到标准基），使得
$H Y_S$ 与 $H_A Y_S$ 的**秩、行空间包含关系、行空间相等关系**与原来一致，且它们落在 $\mathbb R^\ell$ 中；
坐标变换是显式的、位长 $\operatorname{poly}(\mathcal L)$。

*证明.* $S$ 由 $[N\ AN]$ 的后半部分张成，是有理子空间。取 $S$ 的一组有理基、补全为 $\mathbb R^k$ 的基，
得 $Y_S\in\mathbb Q^{k\times k}$ 可逆。**注意**（专家 90 号回复 §3.2 的更正）：
右乘可逆阵**不保持行空间本身**，$\operatorname{row}(XY_S)\ne\operatorname{row}(X)$；
保持的是秩、以及两个行空间之间的 $\subseteq$ 与 $=$ 关系。故下文只使用这些关系，不使用行空间的相等。∎

于是：**所有计数都用 $\ell$，不用 $k$**。

## 5. 编码

固定 $t$、$\omega\ge1$、以及 $\operatorname{Gr}(t,m')$ 的一张图，其中
$$m'=\dim\bigl(T\cap(S\times S)\bigr)-s_0\le2\ell-s_0,\qquad
\text{图数}=\binom{m'}{t},\quad \sum_t\binom{m'}{t}=2^{m'}\le4^\ell.$$

变量：$Y\in\mathbb R^{t\times(m'-t)}$（图坐标）与 $x\in\mathbb R^{2\omega}$（证书），
$$N_{\rm var}=t(m'-t)+2\omega\le\frac{m'^2}{4}+2\omega\le\ell^2+2\ell.$$

**记号（专家 90 号 §4.2 要求）**：$\sigma_j(X)$ 表示实对称矩阵 $X$ 的第 $j$ 个初等对称多项式
（即 $X$ 的全部 $j$ 阶主子式之和；对半正定阵，$\sigma_j(XX^{\mathsf T})>0\iff\operatorname{rank}X\ge j$，
$\sigma_j=0\iff\operatorname{rank}X<j$）。约定 $j$ 超过矩阵阶数时 $\sigma_j=0$。
$\mathbf e_1=(1,0,\dots,0)^{\mathsf T}\in\mathbb R^{2\omega}$ 是第一个标准基向量。

**$\omega=0$ 分支（必须在进入下面的编码之前单独处理）**：由引理 4 的证明，$\omega=0$ 时 $W=0$；
而 $W\supseteq W_0$，故**当且仅当 $W_0=0$ 时**可行，且此时无需任何自由行。
若 $W_0\ne0$ 则直接判不可行（对一切阶数）。因此下面只处理 $\omega\ge1$。

多项式（固定 $W=W_0\oplus U$ 的基矩阵 $Z(Y)=[H(Y)\ G(Y)]$，$\nu=s_0+t\le2\omega$ 由剪枝保证）：
$$\sigma_\omega(HH^{\mathsf T})>0,\qquad
\sigma_{\omega+1}\!\left(\begin{bmatrix}H\\G\end{bmatrix}\begin{bmatrix}H\\G\end{bmatrix}^{\mathsf T}\right)=0,\qquad
B(Y)^{\mathsf T}B(Y)\,x=\mathbf e_1 .$$

**$B$ 的方向与尺寸（专家 90 号 §4.4）**：$P_Y(\lambda)=\lambda H(Y)-G(Y)$ 是 $\nu\times\ell$ 铅笔；
对每个 $\omega$ 阶子式 $f_{I,J}(\lambda;Y)=\det P_Y(\lambda)_{I,J}$（$|I|=|J|=\omega$）取
$\lambda^j f_{I,J}$，$0\le j<\omega$，每个是次数 $\le2\omega-1$ 的 $\lambda$ 多项式，其系数向量长 $2\omega$。
把这些向量作为**行**排成
$$B(Y)\in\mathbb R^{\,\omega\binom{\nu}{\omega}\binom{\ell}{\omega}\times 2\omega},$$
**列数恰为 $2\omega$**，与子式个数无关。$B^{\mathsf T}Bx=\mathbf e_1$ 等价于 $\mathbf e_1\in\operatorname{row}B(Y)$，
即诸 $f_{I,J}$ 有次数 $<\omega$ 的 Bézout 恒等式，即无公共复零点。

- 多项式个数 $S_{\rm poly}=2+2\omega\le2\omega+2$；
- 次数 $D\le2\omega+2$；
- 单个系数的位高 $\tau_{\rm cert}\le\operatorname{poly}(\mathcal L)$（引理 8）；
- **展开后公式的总长** $L_{\rm formula}\le2^{O(\omega\log(\omega+2))}\operatorname{poly}(\mathcal L)$。

**为什么剪枝必须写在构造之前**：$\sigma_j$ 是 $j$ 阶主子式之和，所以
- $\sigma_\omega(HH^{\mathsf T})$ 有 $\binom{\nu}{\omega}$ 项；
- $\sigma_{\omega+1}(\cdot)$ 有 $\binom{\nu}{\omega+1}$ 项（**不是 $\binom{\nu}{\omega}$**，专家 92 号 §7 的更正）。

只有 $\nu\le2\omega$ 时才有 $\binom{\nu}{\omega+1}\le2^\nu\le4^\omega$ 与 $\binom{\nu}{\omega}\le4^\omega$，
与 $r_0$ 无关；否则 $\binom{s_0+t}{\omega+1}$ 没有 $\ell$ 的上界。

**分支枚举（专家 92 号 §7.2 要求显式）**：对每对 $(t,\omega)$ 只保留
$$0\le t\le\min(r,m'),\qquad 1\le\omega\le\ell,\qquad \omega\le\nu=s_0+t\le2\omega .$$
（$\omega>\ell$ 或 $\omega>\nu$ 的秩选择不可能；$\nu\le2\omega$ 是结构界给出的必要条件。）
**先剪枝，再构造多项式系统。**

**换坐标后的尺寸（专家 92 号 §3.1 的更正）**：在 $\mathbb Q^{2k}$ 上用分块变换 $\operatorname{diag}(P,P)$，
再利用 $V\subseteq S\times S$ 删去最后 $2(k-\ell)$ 个零坐标，于是
$$Z(Y)\in\mathbb R^{\nu\times2\ell},\qquad H(Y),G(Y)\in\mathbb R^{\nu\times\ell},\qquad
P_Y(\lambda)\in\mathbb R^{\nu\times\ell}.$$
下文所有 $\binom{\ell}{\omega}$ 与 $\nu\times\ell$ 都指这个 $2\ell$ 维坐标下的矩阵。
（原先写 $\nu\times2k$ 却用 $\binom{\ell}{\omega}$，是坐标不一致，已改。）

**Cauchy–Binet 压缩**：$B^{\mathsf T}B$ 的元素由
$$\sum_{|J|=\omega}\det\!\bigl(P_{:,J}(\lambda)^{\mathsf T}P_{:,J}(\mu)\bigr)=\sum_{I,J}f_{I,J}(\lambda)f_{I,J}(\mu)$$
的系数矩阵给出。**换坐标之后 $P$ 只有 $\ell$ 列**，所以列子集只有 $\binom{\ell}{\omega}\le2^\ell$ 个；
行子集 $I$ 由 Cauchy–Binet 消掉，不需要枚举。**这里必须用 $\ell$ 而不是 $k$**：
若写成 $\binom{k}{\omega}\le2^k$，指数就含有 $k$，而 $k$ 可以远大于 $\ell$，定理就不再是 FPT in $\ell$。
（专家 90 号回复第 5 节指出的正是这一处，已改正。）

---

## 5.1 商空间里的图参数化（专家 90 号 §4.1 要求）

写在 $V=T\cap(S\times S)$ 的**商空间**里，不是 $V$ 的任意 $t$ 维子空间——否则会允许不含 $W_0$ 的候选。

构造顺序（固定，每一步都有理）：

1. 取 $W_0$ 的一组**有理基**，记其矩阵为 $E_0$（$s_0$ 行）；
2. 取 $W_0$ 在 $V$ 中的一组**有理补**，记其矩阵为 $E_Q$（$m'=\dim V-s_0$ 行）；
3. 在 $\mathbb R^{m'}$ 里取 $\mathrm{Gr}(t,m')$ 的标准图：$[I_t\ |\ Y]$（$t\times m'$），$Y\in\mathbb R^{t\times(m'-t)}$；
4. 提升回 $V$：$U(Y)=[I_t\mid Y]\,E_Q$；
5. 与固定基合并：$Z(Y)=\begin{bmatrix}E_0\\ U(Y)\end{bmatrix}$，共 $\nu=s_0+t$ 行，元素是 $Y$ 的**仿射**函数。

于是每个图给的候选都**自动含 $W_0$**，且 $Y$ 的图覆盖 $\mathrm{Gr}(t,m')$ 的全部点。
图数 $\binom{m'}{t}$，合计 $2^{m'}\le4^\ell$。

## 5.2 系数位高引理（专家 90 号 §5.2 要求，显式导出）

**引理 8（系数位高）.** 在 §5.1 的构造下，若输入为有理数、位长 $\mathcal L$，则
$$\tau_{\rm cert}\le\operatorname{poly}(\mathcal L)+O\bigl(\omega\log(\omega+2))+\ell .$$
由于 $\ell\le n\le\mathcal L$ 且 $\omega\le\ell$，即 $\tau_{\rm cert}\le\operatorname{poly}(\mathcal L)$。

*证明.* 分四项。

**(a) 有理预处理.** $N$、$S$ 的基、$E_0$、$E_Q$、补空间基：都是 $n\times n$ 有理矩阵的高斯消元结果。
按 Hadamard 界，$j$ 阶子式位长 $\le O(j(\tau_{\rm in}+\log j))$，其中 $\tau_{\rm in}$ 是输入系数位长；
消元不放大超过多项式因子，故四项基矩阵的元素位长 $\le\tau_0:=\operatorname{poly}(\mathcal L)$。

**(b) 图矩阵.** $Z(Y)$ 的元素是 $Y$ 的仿射函数，系数来自 $E_0,E_Q$，位长 $\le\tau_0$。

**(c) $\omega$ 阶子式.** $P_Y(\lambda)_{I,J}$ 的每个元素是 $(\lambda,Y)$ 的仿射函数，位高 $\le\tau_0+1$。
行列式展开为至多 $\omega!$ 项、每项至多 $\omega$ 个因子之积，故 $f_{I,J}$ 作为 $(\lambda,Y)$ 的多项式，
其系数位高
$$\le \omega\,\tau_0+\log(\omega!)+O(\omega\log(\omega+2))=O\bigl(\omega\,\tau_0+\omega\log(\omega+2)\bigr).$$

**(d) Cauchy–Binet 求和.** $K(\lambda,\mu)=\sum_{|J|=\omega}\det\bigl(P_{:,J}(\lambda)^{\mathsf T}P_{:,J}(\mu)\bigr)$
的每一项是 $\omega\times\omega$ 行列式，元素是 $(\lambda,\mu,Y)$ 的双线性函数，系数位高同 (c)；
求和项数 $\binom{\ell}{\omega}\le2^\ell$，只增加 $\ell$ 位。于是 $B^{\mathsf T}B$ 的系数位高
$$\le O\bigl(\omega\,\tau_0+\omega\log(\omega+2)\bigr)+\ell .$$
$\sigma_\omega$ 是 $\binom{\nu}{\omega}$ 个 $\omega$ 阶主子式之和，$\sigma_{\omega+1}$ 是
$\binom{\nu}{\omega+1}$ 个 $(\omega+1)$ 阶主子式之和；由剪枝 $\nu\le2\omega$，两者项数都 $\le4^\omega$，
只增加 $2\omega$ 位。合并即得
$$\tau_{\rm cert}\le O\bigl(\omega\tau_0+\omega\log(\omega+2)\bigr)+\ell+2\omega=\operatorname{poly}(\mathcal L).$$

**共同的清分母**：所有多项式同时乘以它们的有理系数的公分母。公分母是若干位长 $\le\tau_0$ 的行的
乘积，位长 $\le O(\ell\tau_0)=\operatorname{poly}(\mathcal L)$；清分母不改变零点集，只把位高再抬这一项。∎

**说明**：这条引理把专家指出的四项（有理基、图坐标、子式、$B^{\mathsf T}B$ 求和）各自界了一次；
其中 (c) 的 $O(\omega\log(\omega+2))$ 现在有推导支撑。代回 $\omega\le\ell\le\mathcal L$ 即
$\tau_{\rm cert}\le\operatorname{poly}(\mathcal L)$。

## 5.3 预处理代价引理（专家 90 号 §6.1 要求）

**引理 10（预处理）.** 给定有理输入，下列数据可在
$$\exp\bigl(O(\ell\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L)$$
位运算内构造：$N$ 与 $K_0$ 的基、$M=[N\ AN]$、$T$ 与 $S=\operatorname{row}(AN)$ 的基、
$W_0=\operatorname{row}(L_0M)$ 的基、$V=T\cap(S\times S)$ 的基、$W_0$ 在 $V$ 中的补 $E_Q$、
以及每张图的仿射矩阵 $Z(Y)$ 的系数数据。

*证明.* 前三项是 $n\times n$ 有理矩阵的零空间与行空间计算，高斯消元 $O(n^3)$ 次域运算，
每次位长 $\operatorname{poly}(\mathcal L)$（Hadamard + Cramer）。$V$ 是两个子空间的交，用
$\dim(V_1\cap V_2)=\dim V_1+\dim V_2-\operatorname{rank}[B_1;B_2]$ 的等价算法（对 $[B_1;B_2]$ 消元）求得；
补空间 $E_Q$ 同样由消元给出。$Z(Y)$ 的系数就是 $E_0,E_Q$ 的元素，无需额外计算。
图的个数是 $\binom{m'}{t}\le2^\ell$，每张图只需写出 $O(\nu\cdot2\omega)$ 个系数，故总和
$2^\ell\cdot O(\ell^2)$. 与消元的 $\operatorname{poly}(n,\mathcal L)$ 合并即得。∎

## 6. 判定界（Renegar）

对每张图、每个 $(t,\omega)$，用 Renegar 的 Part II 判定界
$$T\le B(\log B)(\log\log B)(S_{\rm poly}D)^{O(N_{\rm var})}$$
（$B$ = 单个系数的位高 = $\tau_{\rm cert}$）。代入：
$$(S_{\rm poly}D)^{O(N_{\rm var})}=(O(\omega^2))^{O(\ell^2)}=\exp\bigl(O(\ell^2\log(\ell+2))\bigr),$$
$$B\log B\log\log B=\operatorname{poly}(\mathcal L)\cdot2^{O(\ell\log(\ell+2))}\quad(\text{被吸收}).$$
乘上图数与 $(t,\omega)$ 的对数：
$$T_{\rm DEC}\le\underbrace{4^\ell}_{\text{图}}\cdot\underbrace{O(\ell^2)}_{(t,\omega)}\cdot
\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L)
=\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L).$$

---

## 7. OPT

由引理 5 单调，$t\mapsto\mathrm{DEC}(r_0+t)$ 单调不减。$t_{\min}\le m'\le2\ell$，故在 $[0,m']$ 上二分：
$$T_{\rm OPT}\le\bigl(\lceil\log_2(m'+1)\rceil+1\bigr)T_{\rm DEC}
=\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L).$$
若 $t=m'$ 仍不可行，则无可行 $W$，$q_{\min}=+\infty$（由引理 5 的饱和性，更大的 $t$ 也不必再试）。

---

## 8. FIND（见证抽取）

**定理（BPR 1997）.** 设 $P\subset\mathbb R[X_1,\dots,X_N]$ 有 $S_{\rm poly}$ 个多项式、次数 $\le D$。
存在算法计算所有**可实现符号条件**及其样本点，算术代价 $S_{\rm poly}^{N+1}D^{O(N)}$；
样本点取遍每个非空符号条件连通分支（因此**开集、非闭、非有界**都覆盖），
输出为精确实代数数（一元表示 + 隔离区间），系数位长 $\le\tau D^{O(N)}$。

**应用.** 我们的公式是符号条件的布尔组合；非空 $\iff$ 某个可实现符号条件与公式相容。
故对每张图调用一次 BPR，取满足公式的样本点 $Y^*$（若该分支 $x$ 分量存在则整点存在）。

**重建 $R$.** 预计算有理线性截面 $\sigma:T\to\mathbb Q^{1\times n}$，$\sigma(w)M=w$
（$M$ 的右逆，$\operatorname{poly}(n,\mathcal L)$ 位）。由 $Y^*$ 得 $U$ 的基、$W$ 的基 $w_i$，
令 $r_i=\sigma(w_i)$，$R$ 的前 $t$ 行为 $r_i$（代数数），其余为零。

**代价.** 算术 $S_{\rm poly}^{N+1}D^{O(N)}=\exp(O(\ell^2\log(\ell+2)))$。

**引理 9（见证的表示位长；BPR 2006, Theorem 13.11）.** 设 $P$ 是 $k$ 个变量、$s$ 个多项式、
次数 $\le d$、整系数位高 $\le\tau$ 的族。存在算法输出一组点，**每个非空符号条件的每个连通分支一个**，
其**一元表示**（$P_i(\theta)=0$、$Y_j=Q_j(\theta)/Q_{0}(\theta)$，外加根指定）满足
$$\deg\le O(d)^k,\qquad \text{系数位高}\le\tau\,d^{O(k)},\qquad \#\text{点}\le\sum_j4^j\binom{s}{j}O(d)^k=s^{O(k)}d^{O(k)},$$
算术代价 $s^{O(k)}d^{O(k)}$（在系数环 $D$ 上）。

**引用核实（专家 92 号 §8 提出的疑问）**：我们的 PDF 是 **Second Edition**（ISBN 978-3-540-33098-1），
目录为 Ch.11 *Cylindrical Decomposition Algorithm*、**Ch.13 *Existential Theory of the Reals***、
Ch.14 *Quantifier Elimination*、Ch.15 *Computing Roadmaps…*；§13.1 的标题正是
*Finding Realizable Sign Conditions*（第 515 页），Theorem 13.11 就在该节内。
所以"§13.1, Theorem 13.11"这个引用**是对的**，专家所指的"Ch.13 是 CAD、Ch.15 是 ∃R"应是记混了版次。

**代入我们的参数**：变量数 $k\leftarrow N_{\rm var}\le\ell^2+2\ell$、次数 $d\leftarrow D\le2\omega+2\le2\ell+2$、
多项式数 $s\leftarrow S_{\rm poly}\le2\omega+2$、位高 $\tau\leftarrow\tau_{\rm cert}\le\operatorname{poly}(\mathcal L)$（引理 8）。
先清分母把有理系数变成整系数：公分母位长 $\operatorname{poly}(\mathcal L)$，不改变零点集，只把 $\tau$ 再抬 $\operatorname{poly}(\mathcal L)$。于是
$$\deg\le(2\ell+2)^{O(\ell^2)}=\exp\bigl(O(\ell^2\log(\ell+2))\bigr),$$
$$\text{系数位高}\le\operatorname{poly}(\mathcal L)\,(2\ell+2)^{O(\ell^2)}
=\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L).$$
一元表示含 $N_{\rm var}+1$ 个多项式（$P,Q_0,\dots,Q_{N_{\rm var}}$），每个次数 $\le\deg$、系数位高如上，故
$$L_{\rm out}\le(N_{\rm var}+1)(\deg+1)(\text{位高}+1)
=\exp\bigl(O(\ell^2\log(\ell+2))\bigr)\operatorname{poly}(\mathcal L).$$

**算术代价换算成位代价——这一步原先不成立（专家 92 号 §12 的更正）**：
"每个算术运算作用在位高 $\le B$ 的系数上、代价 $\operatorname{poly}(B)$"**不能**从输入系数的位高推出，
因为中间量（子结式、结式、代数数运算）的位长可以远大于输入。BPR 自己就在第 8 章写道：

> "These bitsize estimates do not follow in general from an analysis [of the arithmetic complexity]."

**已核实**：BPR §13.1 给的是**系数环 $D$ 上的算术复杂度**加上**输出的位长界**，
**没有**给出采样点算法的位复杂度；第 8 章只做基本算法（Horner 等）的位长记账。
所以 BPR 不能直接提供 FIND 的位复杂度。

**文献检索结果**（2026-11）：没有找到适用于**一般符号条件**的位复杂度采样点定理。
现有最接近的是 Berthomieu–Gillot–Safey El Din（arXiv:2605.18110, 2026），
但那是**单个不等式**定义的连通分支，且算法是概率性的，不能直接套到我们的公式上。

**因此 FIND 的位复杂度只能标为待补**，需要的精确命题是：

> **（需要的定理）** 对 $s$ 个多项式、次数 $\le D$、$N$ 个变量、整系数位高 $\le\tau$ 的族，
> 构造每个非空符号条件的样本点（含根指定）可在 $(sD)^{O(N)}\operatorname{poly}(\tau)$ **位**运算内完成。

若这条成立，代入本文参数即得 $T_{\rm FIND}=\exp(O(\ell^2\log(\ell+2)))\operatorname{poly}(\mathcal L)$。

- **定理 A（算术构造）**：见证可在 $\exp(O(\ell^2\log(\ell+2)))$ 次算术运算内构造。
  出处：BPR 2006 Theorem 13.11 的算术复杂度（在系数环 $D$ 上）。
- **定理 B（位复杂度构造）**：**未证明**，依赖上面那条缺失的定理。

**从一元表示恢复 $R$（专家 92 号 §11 的更正）**：不需要乘乘法表。因为
$Z(Y)$ 对 $Y$ 仿射、$\sigma$ 有理线性、基恢复是有理矩阵运算，所以每个 $R$ 元素是 $Y$ 的**有理仿射线性组合**，
故可写成
$$R_{ab}=\frac{\widetilde Q_{ab}(\theta)}{Q_0(\theta)},$$
$\deg\widetilde Q_{ab}\le\deg$，只需把有理系数组合起来，**次数不增、位高只增加预处理数据的位长与
加法项数的对数**。这比乘法表的论证更干净，也给出了输出大小的界。

**结论（诚实版）**：
$$\boxed{\text{FIND 的算术复杂度}=\exp\bigl(O(\ell^2\log(\ell+2))\bigr),\qquad
\text{位复杂度}=\text{待补（需位模型的采样点定理，见上）}}$$
见证是精确实代数数（一元表示 + 隔离区间/Thom 编码作为根指定，专家 92 号 §10 要求）。

**不承诺有理见证**：非空实代数集不一定含有点；输出是实代数数，符合模型（$R$ 允许实数）。

---

## 9. 哪些有 Lean、哪些没有

| 内容 | Lean | 位置 |
|---|---|---|
| 行空间 = 行映射像、可实现性、沙包 | ✅ | `Q1Subspace.lean` |
| 压缩恒等式（抽象） | ✅ | `Q1Compression.lean` |
| 秩可加 $\iff$ 行包含 | ✅ | `Q1RankInclusion.lean` |
| 铅笔秩恒定接口、$z=0$ 处 $\operatorname{rank}H_A=\operatorname{rank}H$ | ✅ | `Q1Pencil.lean` |
| $\pi_1=\pi_2$（投影层 + 矩阵层） | ✅ | `Q1Projection.lean`、`Q1Step3.lean` |
| $\dim W\le2\omega$ | ❌ | 缺 `Submodule.finrank_prod` |
| $\omega+1\le\dim W$ | ❌ | 需要图与特征值 |
| $q_{\min}=r_0+t_{\min}$ | ❌ | 纸面 3 行 |
| 编码、Renegar、BPR、位算术 | ❌（本质不可形式化） | 本文 §5–§8 |

全图构建：`lake build MyProof` = 9116 jobs，公理仅 `propext, Classical.choice, Quot.sound`。

**§9.1 一处保真修正（可靠性核查中发现）.** Lean 接口原先写铅笔为 $zH-HA$，隐含
$K_0=\ker[C;CA]$ 在 $A$ 下不变；但 $x\in K_0$ 只给 $Cx=CAx=0$，推不出 $CA^2x=0$，
所以 $H_A=LAN$ **一般不等于** $HA$。纸面证明从未使用该等式（始终把 $H$ 与 $H_A$ 当独立块），
但 Lean 的陈述弱于命题。已改为 `z • H - H_A`，$H,H_A$ 独立；重建 9116 jobs 通过、公理不变。
这条正是项目规范"陈述保真"要防的错误。

## 9.2 可靠性核查表

| 断言 | 核查方式 | 状态 |
|---|---|---|
| 引理 1 压缩恒等式 | Lean `finrank_range_prod` + 论文 §V | ✅ 双覆盖 |
| 引理 2 两条件只依赖 $W$ | 纸面（引理 1 代入） | ✅ |
| 引理 3 沙包 / 可实现性 | Lean `rowSpan_fromRows_left`、`mem_rowSpan_iff_exists_vecMul`；实验 `c320` 往返 36/36 | ✅ |
| 引理 4 结构界上界 | 纸面；$\pi_1=\pi_2$ 由 Lean `rowSpace_eq` 覆盖矩阵形式 | ✅ |
| 引理 4 结构界下界（特征值） | 纸面；**未形式化** | ⚠️ 纸面可信，Lean 缺 |
| 引理 5 单调 / 饱和 | 纸面；实验 `c320` 单调检查 | ✅ |
| 引理 6 $q_{\min}=r_0+t_{\min}$ | 纸面；实验 `c322`（36/36 压缩） | ⚠️ 纸面 + 实验，未形式化 |
| 引理 7 坐标变换 | 纸面（专家已指出原措辞错误并更正） | ✅ |
| 引理 8 系数位高 | 纸面推导（四项）；**未逐项数值核对** | ⚠️ 待核 |
| §5 编码与剪枝 | 纸面；$\sigma_j/\mathbf e_1$ 记号、$ 尺寸、$\omega=0$ 分支已补 | ✅ |
| §6 Renegar 代入 | 算术核对（$S_{\rm poly}D=O(\ell^2)$，$N=\ell^2+2\ell$） | ✅ |
| §7 二分 | 纸面（单调 + 区间 $2\ell$） | ✅ |
| §8 BPR 算术界 | 引用定理 | ✅ |
| §8 BPR 位界 | 引理 9 给**输出位长**；位复杂度仍需位模型的采样点定理（BPR 只给算术复杂度，第 8 章明说位长估计不能由算术分析推出） | ❌ |

**结论**：纸面证明的"归约 + 结构 + 计数"部分是可靠的；**两处仍是纸面依赖**：
特征值论证（未形式化）与系数位高的逐项核对（未数值验证）。**一处仍是缺口**：$L_{\rm out}$。

---

## 10. 专家 90 号回复要求补的点（按重要性）

**A. 已在本文件改正的**
1. ~~$2^k$~~ → $2^\ell$：换坐标后 Cauchy–Binet 只对 $\ell$ 列求和（§5）。
2. “右乘可逆阵保持行空间”是**错的**，只保持秩与 $\subseteq$、$=$ 关系（§4 引理 7）。
3. FIND 的算术界与位界分开陈述（§8）。
4. 行槽模型在定理处显式声明（§0）。

**B. 仍缺、必须补的**

5. ~~系数位高引理~~ —— **已在 §5.2 补全**（引理 8）。
6. ~~图参数化在商空间~~ —— **已在 §5.1 补全**。
7. ~~$B$ 的方向与尺寸~~ —— **已在 §5 补全**（行 $=\omega\binom{\nu}{\omega}\binom{\ell}{\omega}$，列 $=2\omega$）。
8. ~~$e_j$ 记号冲突~~ —— **已改为 $\sigma_j$ 与 $\mathbf e_1$**，并约定 $\sigma_j=0$ 当 $j$ 超界。
9. ~~$\omega=0$ 分支~~ —— **已并入 §5 开头**（先判 $W_0=0$）。
10. ~~复数化~~ —— **已在引理 2 补全**（$W_{\mathbb C}=W\otimes_{\mathbb R}\mathbb C$）。
11. ~~预处理代价引理~~ —— **已补为引理 10（§5.3）**。
12. ~~行槽模型的独立意义~~ —— **已在 §0 补一段**，并新增 §0.1 输入输出模型。

**C. 专家建议的论文主定理形式**（他给的 consolidated 版本，可直接采用）：

> 在行槽模型下，$\mathrm{DEC}$、$\mathrm{OPT}$、$\mathrm{FIND}$ 都以
> $f(\ell)=\exp(O(\ell^2\log(\ell+2)))$ 为参数依赖，$\ell=\operatorname{rank}(AN)$；
> 判定与优化的界为 $f(\ell)\operatorname{poly}(\mathcal L)$，构造给出输出敏感的界。

他的结论：**架构成立、不主张约化阶、不承诺有理见证；补齐 A/B 两组后可投。**

**C′. 与并行会话的编号冲突**：`workspace/for_expert/` 下同时存在
`90_lean_blockers.md`（另一路，已归档回复）与本文件的 `90_minimum_order_and_construction_fpt.md`。
两者主题不同、文件名不同，但前缀重复；如需并表，建议把本组改为 92。

## 11. 尚未完全闭合的点（如实列出）

1. **$\tau_{\rm cert}$ 的逐项核对**：引理 8 已给出四项推导，但 $(c)(d)$ 的常数未数值验证；
   引理 8 用的是 $\binom{\ell}{\omega}\le2^\ell$（已按专家更正为 $\ell$）。
2. ~~$L_{\rm out}$ 的界~~ —— **已由引理 9 闭合**（BPR Theorem 13.11 的次数 $O(d)^k$ 与位高 $\tau d^{O(k)}$，代入 $N_{\rm var},D,S_{\rm poly},\tau$）。
3. **坐标变换到 $S$**：引理 7 只写了论证要点，未给出 $Y_S$ 的显式构造与位长。
4. **$\omega=0$ 分支**：单独处理（$W=0$，可行 $\iff W_0=0$），未并入 §5 的编码。
5. **行槽 vs 约化阶**：已在定理中声明适用范围，但若审稿人要求约化阶版本，需要另证。
6. **特征值论证**（引理 4 下界）：纸面完整，**未形式化**；且需在 $W_{\mathbb C}$ 上陈述（见引理 2 的复数化段）。
