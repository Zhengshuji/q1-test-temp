# Theorem A 的位复杂度审计：DEC 是否真的在 $k$ 下 FPT

> 只做分析，不动论文。目标是回答一个问题：$f(k)\operatorname{poly}(\mathcal L)$ 里的 $f$ 是否**只依赖 $k$**
> （而不是偷偷含 $n$ 或 $r$）。所有量都给出显式上界。

## 0. 记号与输入模型

输入：$A\in\mathbb Q^{n\times n}$、$C\in\mathbb Q^{p\times n}$、$L_0\in\mathbb Q^{r_0\times n}$、整数 $q$（一元）。
$\mathcal L$ 为输入的总二进制长度。以下恒有 $k\le n\le\mathcal L$。

$$K_0=\ker[C;CA],\quad N\in\mathbb R^{n\times k}\ (K_0\text{ 的基}),\quad d=\operatorname{rank}[N\ AN]\le\min(2k,n),$$
$$M=[N\ AN]\in\mathbb R^{n\times 2k},\quad T=\operatorname{row}M,\quad W_0=\operatorname{row}(L_0M),\quad s=\dim W_0,\quad m=d-s\le2k.$$

**前提 P（多项式时间预处理）**：$N$、$M$、$T$ 的基、$W_0$ 的基、$W_0$ 在 $T$ 中的补 $V$（$\dim V=m$）
都可由有理数上的高斯消元在 $\operatorname{poly}(n,\mathcal L)$ 位运算内算出，且所有元素的位长
$\operatorname{poly}(n,\mathcal L)$。这是标准的（Cramer 公式 + Hadamard 界），论文的系数位长引理已覆盖同一论证。

## 1. 归约（已由实验与部分 Lean 验证）

$\mathrm{DEC}(q)$ 成立 $\iff$ 存在 $W$ 满足
$$W_0\subseteq W\subseteq T,\qquad \dim(W/W_0)\le r=q-r_0,\qquad W\text{ 满足两个投影条件}.$$

写 $W=W_0\oplus U$、$U\subseteq V$、$t=\dim U$、$\omega=\dim\pi_1(W)$。由结构界（$\omega>0$）：
$$\omega+1\le \dim W=s+t\le2\omega,\qquad\text{即}\qquad \max(0,\omega+1-s)\le t\le\min(r,m,2\omega-s).$$

于是**枚举空间**为：$(t,\omega)$ 对，加上 $\mathrm{Gr}(t,m)$ 的坐标图。

## 2. 每张图、每个 $(t,\omega)$ 的约束系统

变量（实数）：
$$Y\in\mathbb R^{t\times(m-t)}\quad(\text{图坐标}),\qquad x\in\mathbb R^{2\omega}\quad(\text{证书向量}).$$
$$N_{\rm var}=t(m-t)+2\omega\;\le\;\frac{m^2}{4}+2k\;\le\;k^2+2k.$$

多项式：$e_\omega(G_H)>0$、$e_{\omega+1}(G_S)=0$（各一个），以及 $Z^{\mathsf T}Zx=e_0$（$2\omega$ 个）。
$$s=p\cdot2\omega+O(1)=O(\omega)\le O(k).$$

次数：$G_H,G_S$ 的元素是 $Y$ 的二次型使 $e_j$ 为 $2j$ 次；$Z^{\mathsf T}Z$ 的元素是 $Y$ 的 $2\omega$ 次多项式，
乘 $x$ 后为 $2\omega+1$ 次。
$$D\le2\omega+2\le2k+2.$$

系数位长：$\widehat H,\widehat H_A$ 的元素来自 $E_0,E$（有理，位长 $\operatorname{poly}(n,\mathcal L)$）；
$Z^{\mathsf T}Z$ 的系数是 $\binom{k}{\omega}\le2^k$ 项之和，每项是 $2\omega$ 个系数之积，
$$B\le\operatorname{poly}(n,\mathcal L)+O(k\log k+\log 2^k)=\operatorname{poly}(\mathcal L)\cdot 2^{O(k\log k)}.$$
（清分母后仍为同阶；$k\le\mathcal L$。）

## 3. 图的数量

$$\#\text{charts}=\sum_{t=0}^{m}\binom{m}{t}=2^m\le2^{2k}=4^k,\qquad \#(t,\omega)\le(2k+1)(k+1)=O(k^2).$$
合计至多 $4^k\cdot O(k^2)$ 个子问题。

## 4. 每个子问题的代价

用 Renegar 的 Part II 界（论文引用的是 $B(\log B)(\log\log B)(sD)^{O(N_{\rm var})}$）：
$$(sD)^{O(N_{\rm var})}=\bigl(O(k^2)\bigr)^{O(k^2)}=\exp\bigl(O(k^2\log k)\bigr),$$
$$B(\log B)(\log\log B)=\operatorname{poly}(\mathcal L)\cdot 2^{O(k\log k)}\quad(\text{被上式吸收}).$$

构造约束系统本身：$\binom{k}{\omega}$ 个极大子式的 Cauchy–Binet 求和，$2^k\cdot\operatorname{poly}(k,\mathcal L)$；
稠密展开成单项式系数为 $\binom{N_{\rm var}+D}{D}=\exp(O(k^2\log k))$。

## 5. 合计

$$T_{\mathrm{DEC}}\;\le\;\underbrace{4^k\cdot O(k^2)}_{\text{子问题数}}\cdot
\underbrace{\exp\bigl(O(k^2\log k)\bigr)\operatorname{poly}(\mathcal L)}_{\text{单个子问题}}
\;=\;f(k)\operatorname{poly}(\mathcal L),$$
$$\boxed{f(k)=\exp\bigl(O(k^2\log k)\bigr)}.$$

**结论**：$f$ 只依赖 $k$，与 $n$、$r$ 无关。Theorem A 的位复杂度账**是平的**，前提是三个标准事实可用：

1. 有理矩阵消元的位长界（预处理）；
2. Renegar Part II 界对"$s$ 个多项式、次数 $D$、$N$ 个变量、系数位长 $B$"的形式（论文已引用）；
3. Cauchy–Binet 求和把 $\binom{k}{\omega}$ 项压成 $2\omega\times2\omega$ 的 Gram 矩阵（论文已证，实验 c317 复核）。

## 6. OPT 与 FIND

**OPT**：$q_{\min}=r_0+t_{\min}$，$t_{\min}\le m\le2k$。对 $t=0,1,\dots,m$ 依次判定（每个 $t$ 内再枚举 $\omega$ 与图），
首次成功的 $t$ 即 $t_{\min}$。共 $\le2k+1$ 轮，故
$$T_{\mathrm{OPT}}\le(2k+1)\,T_{\mathrm{DEC}}=f(k)\operatorname{poly}(\mathcal L).$$

**FIND**：拿到可行子问题的见证后，
1. 由 $Y^*$ 构造 $U$ 的基、再构造 $W$ 的基（$\operatorname{poly}(k)$ 次算术）；
2. 对每个基向量解 $uM=w$（$M$ 的右逆，预处理一次，$\operatorname{poly}(n,\mathcal L)$）；
3. 组装 $R$ 并精确复核 $(5a)(5b)$（多项式时间）。

见证的类型：实代数数，用最小多项式 + 隔离区间表示；其位长由 Renegar 的界控制（$f(k)\operatorname{poly}(\mathcal L)$）。
**不承诺有理见证**——非空的实代数集不一定含有理点。

## 7. 仍未闭合的地方（必须写明）

1. **见证抽取**：Renegar 的判定算法给出"是否可行"；要拿到点需要带输出的版本（标准做法是常数因子代价，
   但要把引用写清楚）。若不使用带输出的算法，FIND 只能做到"判定 + 用 $\varepsilon$-网近似"，这不再是精确算法。
2. **系数位长 $B$ 的显式常数**：上面写的是 $\operatorname{poly}(\mathcal L)\cdot2^{O(k\log k)}$；
   要把它变成"$\operatorname{poly}(\mathcal L)\cdot f(k)$"没有问题，但 $f$ 的指数里多一个 $k\log k$ 因子，
   与 §5 的估计一致，不改变 FPT 结论。
3. **稠密展开**：$\binom{N_{\rm var}+D}{D}$ 是构造代价而非求解代价；若求解器接受稀疏表示，可省去，
   但上界不变（仍 $\exp(O(k^2\log k))$）。
4. **$\omega=0$ 分支**：$W=0$，单独判定（$H=H_A=0$ 的充要条件），不进入上面的系统。

## 9. 见证抽取：FIND 的前提——**已核实**

**引用**：Basu–Pollack–Roy, *Algorithms in Real Algebraic Geometry*, 2nd ed., Springer 2006,
**Theorem 13.12**（配合 **Algorithm 13.1 / 13.2 Sampling**）：

> 给定 $s$ 个次数 $\le d$ 的多项式（$k$ 个变量），存在算法计算所有可实现的符号条件
> $\mathrm{SIGN}(\mathcal P)$ **并给出样本点**，复杂度
> $$\sum_{j\le k}4^j\binom{s}{j}d^{O(k)}=s^{k+1}d^{O(k)}\quad(\text{在系数环 }D\text{ 上的算术运算});$$
> 输出的 univariate representation 次数 $\le O(d)^k$，整系数时系数位长 $\le\tau\,d^{O(k)}$。

（第 13.3 节 Theorem 13.22 是代数集上的版本，复杂度按代数集的维数计，我们不需要。）

**代入本文参数**（$N_{\rm var}\le k^2+2k$、$s=O(k)$、$d=O(k)$、$\tau=\operatorname{poly}(\mathcal L)2^{O(k\log k)}$）：

- 算术代价：$(s d)^{O(N_{\rm var})}=(k^2)^{O(k^2)}=\exp(O(k^2\log k))$；
- 输出位长：$\tau\,d^{O(N_{\rm var})}=\operatorname{poly}(\mathcal L)\cdot\exp(O(k^2\log k))$。

所以
$$T_{\rm FIND}\le f(k)\operatorname{poly}(\mathcal L),\qquad f(k)=\exp(O(k^2\log k)),$$
与 DEC 同阶。**FIND 的 FPT 性不再依赖未核实的假设**；唯一的前提是"可行 $\iff$ 某个可实现符号条件与公式相容"
（这是符号条件的定义，逐项检查即可）。

**残余注意**：Theorem 13.12 的复杂度是**算术**代价；乘上位长得到**位**代价时，BPR 只给了输出位长界，
没有给中间计算的位长界。若要用位模型，需要引用 BPR 的位复杂度章节（第 8 章）或 Renegar 的位界
把中间计算也算上。这一条要在论文里写清楚，不能只写 $(sd)^{O(k)}$。

## 11. 专家（89 号回复）的修正——必须采纳

以下五条是专家指出的**实质性修正**，已核对原回复（`for_expert/archive/89_subspace_reduction_and_fpt-reply.md`）：

**(1) 系数位高与公式总长必须分开。**
- 单个系数的位高（Renegar 界里那个 $B$）：$\tau_{\rm cert}\le\operatorname{poly}(\mathcal L)+O(k\log(k+2))$，
  即基本就是 $\operatorname{poly}(\mathcal L)$；
- **展开后公式的总长度**：$L_{\rm formula}\le2^{O(k\log(k+2))}\operatorname{poly}(\mathcal L)$。
本文 §2 把两者写成一个 $B$ 是错的。Renegar 界用的是 $\tau_{\rm cert}$；指数里的 $2^{O(k\log k)}$ 属于 $L_{\rm formula}$。

**(2) 分支剪枝 $s_0+t\le2\omega$ 是复杂度证明的必需项，不是优化。**
没有它，行子式个数 $\binom{s_0+t}{\omega}$ 没有参数上界；有了它
$\binom{\nu}{\omega}\le\binom{2\omega}{\omega}\le4^\omega$，配合列子式 $\binom{k}{\omega}\le2^k$，总数才是 $2^{O(k)}$。
所以**构造多项式之前**就要用结构界剪枝。

**(3) 行槽阶 vs 约化阶：必须分开陈述。**
本文的模型允许冗余行与零行，于是
$$\mathrm{DEC}_{\rm slot}(q)\Rightarrow\mathrm{DEC}_{\rm slot}(q+1),\qquad q_{\min}=r_0+t_{\min}$$
都是**行槽**意义下的结论。控制论文献里的"约化阶"按 $\operatorname{rank}[C;L]-\operatorname{rank}C$ 计，零填充不增加阶，
所以单调性与 $q_{\min}$ 公式**不能**直接搬到 $\mathrm{DEC}_{\rm red}$。论文与本文档都必须写明是行槽模型。

**(4) FIND 改用符号条件采样点定理（BPR 1997）。**
> S. Basu, R. Pollack, M.-F. Roy, *On computing a set of points meeting every cell defined by a
> family of polynomials on a variety*, J. Complexity 13(1):28–37, 1997.

算术代价 $s^{N+1}D^{O(N)}$；返回每个**非空符号条件**连通分支中的一个点，因此**开集、非有界、非闭**都覆盖
（严格不等式 $>0$ 就是 $+1$ 符号条件）；输出是精确实代数数（不是有理数）。
位代价要写 $(sD)^{O(N)}\operatorname{poly}(\tau)+(L_{\rm out})$，不能只引算术代价。

**(5) OPT 可以二分。**
由单调性：先测 $q=r_0+m$，失败则无可行阶；成功则在 $[r_0,r_0+m]$ 上二分，
$$T_{\rm OPT}=O(\log(k+2))\,T_{\rm DEC}+T_{\rm FIND}.$$

另外两条**改进**（比 $k$ 更小的参数）：

- $\ell=\operatorname{rank}(AN)\le k$：可行 $W$ 满足 $\pi_1(W)=\pi_2(W)\subseteq\operatorname{row}(AN)=S$，故
  $W\subseteq T\cap(S\times S)$，其维数 $\le2\ell$；把坐标换到 $S$ 的基上，变量数 $\le\ell^2+2\ell$、图数 $\le4^\ell$。
- 迭代公共投影核 $S_*$：$S_0=\mathbb R^k$、$T_j=T\cap(S_j\times S_j)$、$S_{j+1}=\pi_1(T_j)\cap\pi_2(T_j)$，
  序列递减并在 $\le k$ 步稳定；每个可行 $W\subseteq T\cap(S_*\times S_*)$。
  **实验（`c323`）**：12 个随机实例上 $\dim S_*=\operatorname{rank}(AN)$（一般位置上不缩小），
  但"可行 $W$ 落在核内"与 $\dim S_*\le\ell$ **全部成立，0 failure**。

**记号**：本文档里 $s$ 同时表示 $\dim W_0$ 与多项式个数，必须改：$s_0=\dim W_0$、$S_{\rm poly}$、$\tau$。

## 12. 结论

- $\mathrm{DEC}\in\mathrm{FPT}(k)$，$f(k)=\exp(O(k^2\log k))$，**与 $r$ 无关**；
- $\mathrm{OPT}\in\mathrm{FPT}(k)$（$\le2k+1$ 次判定）；
- $\mathrm{FIND}\in\mathrm{FPT}(k)$（判定 + 线性求解 + 代数数见证），前提是见证抽取可用。

**这些都不解决 q1**：$k$ 本身可随 $n$ 增长，所以"$k$ 固定时 FPT"与"一般输入多项式时间"是两件事。
