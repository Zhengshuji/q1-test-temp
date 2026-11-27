# $k=\omega$ 的 RP 上界（有理输入）

> 2026-11-08。落实专家 49 号答复 §7 的 Priority A。工具：`tools/verification/rp_k_omega_check.py`。
> 状态：**M2**（纸面证明 + 机器核验判据；矩形 Hermite 引用已核对（SL95 Las Vegas，RP 吸收）；待专家复核升 M3）。

## 目标

$$\textbf{定理（目标）}.\quad \text{有理输入下，}k=\omega\text{ 的判定问题 } \mathrm{DEC}_{k=\omega}(q)\in\mathbf{RP}.$$

"有理输入"指 $A,C,L_0$ 的元素为二进制有理数，$q$ 用一元编码；$R$ 在 $\mathbb Q^{(q-r)\times n}$ 中取。
存在性仍在 $\mathbb C$ 上问（与项目约定一致）。

## 设想与理由

1. $k=\omega$ 时 $\operatorname{rank}H=k\Rightarrow\ker H=0\Rightarrow(5a)$ **自动成立**；
2. 可容许域 $D=\{\operatorname{rank}H=k,\ \operatorname{rank}L=q\}$ 是仿射空间中的**开集**（两个秩条件都是"某个子式非零"），
   故 $D$ 非空时**不可约**；
3. 坏集 $\mathcal B$ 在 $D$ 中 **Zariski 闭**（闭性定理，B.24 专家已核）；
4. 于是：**$D\subseteq\mathcal B$（全坏）或 $D\setminus\mathcal B$ 非空开稠密（好点为一般点）**；
5. 所以"存在好点"$\iff$"一般点好"——这正是随机特殊化能用于**存在性**问题的原因；
6. 取一个有理点、精确算行列式因子：若为常数则接受；否则拒绝。**单侧错误**（不可行时永不接受）$\Rightarrow$ RP。

## 做法

**参数空间**：$V=\mathbb Q^{m}$，$m=(q-r)n$，$R\mapsto(H(R),H_A(R))$ 仿射线性。

**算法**（$T$ 次重复，$N$ 为网格大小）：

```
for t = 1..T:
    sample R0 uniformly from {1,...,N}^m
    if rank H(R0) != k or rank L(R0) != q: continue
    Delta <- k-th determinantal divisor of lambda*H(R0) - H_A(R0) over Q[lambda]   (Smith form)
    if deg(Delta) == 0: return YES
return NO
```

**引理 1（开性与不可约）**：$H$ 有 $k$ 列、$L$ 有 $q\le n$ 行，故 $\operatorname{rank}H=k$、$\operatorname{rank}L=q$
分别是"某个 $k\times k$ / $q\times q$ 子式非零"，为开条件；$D$ 是仿射空间的开子集，非空时不可约。

**引理 2（坏集闭）**：$\mathcal B=\pi(\mathcal I)$，$\mathcal I=\{(R,\lambda):\text{全部 }k\text{-子式}=0\}\subseteq V\times\mathbb A^1$；
齐次化到 $\mathbb P^1$ 后投影真（$[1:0]$ 处由 $\operatorname{rank}H=k$ 排除），故 $\mathcal B$ 闭（B.24 闭性定理）。

**引理 3（逐分量二分）**：$D$ 不可约 + $\mathcal B$ 闭 $\Rightarrow$ $D\subseteq\mathcal B$ 或 $D\setminus\mathcal B$ 非空开稠密（B.24 定理 A）。

**引理 4（两个常系数组合，gcd 为 1）**：设 $m_1,\dots,m_N\in\mathbb Q(R)[\lambda]$ 的 gcd 为 1。
令 $V_0=\operatorname{span}_{\mathbb Q}\{m_i\}$。则存在常系数有理组合 $f,g\in V_0$ 使 $\gcd(f,g)=1$。

*证明*（按专家 50 号答复 §1.2 修复；原版对**所有**不可约 $p$ 取并集，而 $p$ 有无限多个，
不能直接用"有限并集不能覆盖"）：取任一非零 $f\in V_0$。若 $f$ 是非零常数，取 $g=1$ 即可。
否则 $f$ 在 $\mathbb Q(R)[\lambda]$ 中只有**有限**个不可约因子 $p_1,\dots,p_s$。对每个 $p_j$，
$V_{p_j}=\{h\in V_0:p_j\mid h\}$ 是**真**子空间（因 gcd 为 1，某个 $m_i$ 不被 $p_j$ 整除）。
$\mathbb Q$ 无限，有限个真子空间不能覆盖 $V_0$；取 $g\in V_0\setminus\bigcup_j V_{p_j}$，
则 $f$ 的任何不可约因子都不整除 $g$，故 $\gcd(f,g)=1$。$\square$

**引理 5（结式次数界）**：$k$ 阶子式在 $\lambda$ 与 $R$ 中的总次数都 $\le k$，故 $f,g$ 作为 $\lambda$ 的多项式，
系数是 $R$ 的 $\le k$ 次多项式；$\operatorname{Res}_\lambda(f,g)$ 是 $\le2k$ 阶行列式，总次数 $\le 2k^2$。
且 $R_0\in\mathcal B\Rightarrow f(R_0,\cdot),g(R_0,\cdot)$ 有公根 $\Rightarrow \operatorname{Res}(R_0)=0$。

**引理 6（秩条件的见证）**：$D\ne\varnothing$ 时，存在非零 $k\times k$ 子式 $h$ 与 $q\times q$ 子式 $\ell$，
次数 $\le k$、$\le q$。令 $P=\operatorname{Res}\cdot h\cdot\ell$，则
$$E:=\mathcal B\cup\{\operatorname{rank}H<k\}\cup\{\operatorname{rank}L<q\}\subseteq\{P=0\},\qquad \deg P\le 2k^2+k+q.$$

**引理 7（抽样）**：取 $N=2(2k^2+k+q)$，每个 $R$ 元素独立均匀取自 $\{1,\dots,N\}$，则
$$\Pr[R_0\in E]\le \frac{\deg P}{N}\le \frac12 .$$

**引理 8（矩形行列式因子，精确陈述）**：在 $R_0$ 处，$P_0(\lambda)=\lambda H(R_0)-H_A(R_0)$ 是 $q\times k$、元素次数 $\le1$ 的
$\mathbb Q[\lambda]$ 矩阵；其 $k$ 阶行列式因子 $\Delta_k$ 等于全部 $k$ 阶子式的 gcd，且
$$\deg\Delta_k=0\iff \operatorname{rank}P_0(\lambda)=k\ \ \forall\lambda\in\mathbb C.$$

**引理 8 的引用（已核对）**：由 attempts/106 的桥接引理，$\Delta_k(P)=\det D$（$UP=[D;0]$，$U$ 幺模）；
矩形 Hermite 形由 Storjohann–Labahn（ISSAC 1995, pp. 119–125；Zbl 0914.65044）的 **Las Vegas** 算法给出：
$m\times n$（$m>n$）归约到 $(n+1)\times n$，主代价同无分数高斯消元。
RP 吸收 Las Vegas（RP + Las Vegas = RP），故引理 8 不再依赖 KKS 的方阵定理。

**引用分工（更新）**：KKS 1987 的显式定理是**方阵非奇异**，不再作为矩形引理的主引用；
主引用改为 SL95（Las Vegas 矩形 Hermite）+ 桥接引理。SL 1997 的 Smith 算法仍是方阵非奇异/$\mathbb Z[x]$，
只作备选。$\deg\Delta_k\le k$。

**矩形的桥接（attempts/106）**：若 $UP=[D;0]$（$U$ 幺模、$D$ 为 $k\times k$ 三角块），则
$\Delta_k(P)=\det D$（差一个非零常数）——证明只用 Cauchy–Binet + $k$-子式理想的不变性。
于是"矩形行列式因子"归约到**矩形 Hermite 形**，不必把 KKS 的方阵定理硬套到矩形情形。
矩形 Hermite 的引用已核对：Storjohann–Labahn（ISSAC 1995, pp. 119–125；Zbl 0914.65044）是
**Las Vegas**，把 $m\times n$（$m>n$）归约到 $(n+1)\times n$，主代价同无分数高斯消元；
RP 吸收 Las Vegas，故这一步在 RP 意义下闭合。

**定理的证明**：

*（无假阳性）* 若答案为 NO，则 $D=\varnothing$ 或 $D\subseteq\mathcal B$。前者每次抽样秩检验失败；后者每个可容许样本都坏，
$\deg\Delta_k>0$。两种情形都不会返回 YES。✓

*（假阴性 $\le2^{-T}$）* 若答案为 YES，则 $D\setminus\mathcal B$ 非空开。由引理 7，一次抽样落入
$D\setminus\mathcal B$ 的概率 $\ge1/2$；$T$ 次独立重复后失败概率 $\le2^{-T}$。✓

故 $\mathrm{DEC}_{k=\omega}(q)\in\mathbf{RP}$。$\square$

**关于 $\mathbb Q$ 与 $\mathbb C$**：$D\setminus\mathcal B$ 是 $\mathbb Q$-Zariski 开集；非空开集的有理点稠密
（其补是 $\mathbb Q$ 上真闭集，不能包含全部 $\mathbb Q$-点）。故"$\mathbb C$ 上存在好点"$\iff$"有理好点存在"，
抽样在有理点上不损失完备性。$\deg\Delta_k>0$ 在 $\mathbb Q[\lambda]$ 上 $\iff$ 有复根 $\iff$ 在 $\mathbb C$ 上坏。

## 进展

* 定理与证明（引理 1–8）已写出；引理 8 现由**桥接引理 + 矩形 Hermite（SL95 Las Vegas）**给出，剩 $D$ 的位长细节。
* 机器核验（`rp_k_omega_check.py`，精确 `Fraction`）：
  * 可行实例（$n=6,p=2,q=3,k=2$，$K\cap AK=0$）：19 个可容许样本中 **15 好 / 4 坏**（坏样本正是例外集；
    说明单次抽样会以正概率失败，符合 RP 的单侧性）；
  * 不可行实例（$n=4,p=1,q=3,k=2$，$K=AK$，$A|_K$ 为 swap）：20 个样本 **全部坏**（算法永不接受）；
  * Smith 路径与"枚举子式 + gcd"路径 **39/39 一致**。

## 最终结论

* 目标定理成立（引理 8 已闭合到 RP + Las Vegas）：**$\mathrm{DEC}_{k=\omega}(q)\in\mathbf{RP}$**。
* **不是 ZPP**：重复抽样直到命中在 NO 实例上不终止；单侧错误不自动给出互补算法。
* fixed-$(q,\omega)$ 的"多项式"陈述**更强地保留**（有界次数消元），RP 是变量维数下的上界。
* 与专家 49/50 号答复一致：四项要求已落实；第 4 项（Smith）按 50 号建议单列成引理；引理 4 已修复。

## 放弃原因

* 定理停在 **M2**：引理 8 已改为桥接引理 + 矩形 Hermite（SL95 Las Vegas）；剩 $D$ 的位长细节与专家复核。
* 未给出 **去随机化**（P 版本）：需要确定性的例外集避开或代数算法，本轮不做。

## 残留价值

* 一条可发表的复杂度命题：$k=\omega$ 的 RP 上界，且与 fixed-$(q,\omega)$ 的 P 陈述分离清楚；
* 引理 4（两个常系数组合）与引理 5（$2k^2$ 次数界）是**可复用**的，也回答了专家"如何给次数界"的问题；
* 机器核验给出"可行实例的坏样本比例"与"不可行实例 0 假阳性"的直接证据；
* 下一步（Priority B）：自由区 $q=3,\omega=2$ 的充要判据；本定理的抽样框架可直接复用。

## 相关文件

* [tools/verification/rp_k_omega_check.py](../../../../tools/verification/rp_k_omega_check.py)
* [tools/verification/poly_smith.py](../../../../tools/verification/poly_smith.py)（Smith 形/行列式因子实现）
* [proof/B.24/README.md](../../../../proof/B.24/README.md)（闭性定理、定理 A、专家第二十二/二十三论）
* [workspace/for_expert/archive/49_same_S_and_q_omega_plus_1-answer.md](../../../for_expert/archive/49_same_S_and_q_omega_plus_1-answer.md)（专家 §1/§7）

## 专家复核（50 号答复，§1）

* **结构论证成立**：$D$ 开、$\mathcal B$ 闭、二分、有理采样、Schwartz–Zippel 都被确认；不是 ZPP。
* **引理 4 原证明有 gap**（对无限多个不可约 $p$ 取并集），已按专家给的"先取 $f$、只用它的有限个因子"修复（见上）。
* **结式次数界**：$\le2k^2$ 有效，但要用 $f,g$ 的**实际** $\lambda$-次数（不是子式的上界）。
* **矩形行列式因子**：KKS 1987 的显式定理是方阵非奇异；SL 1997 也是方阵非奇异/$\mathbb Z[x]$。
  已改用**桥接引理**（attempts/106：$UP=[D;0]\Rightarrow\Delta_k=\det D$）+ **SL95 的 Las Vegas 矩形 Hermite**
  （ISSAC 1995, pp. 119–125；Zbl 0914.65044）；RP 吸收 Las Vegas。
* **位长记账**：还要算 $N_K$、$H(R_0),H_A(R_0)$、采样整数（$\le N$）与行列式因子的系数位长；$q$ 一元编码保证维数多项式有界。
* 结论：补上 Smith 引理后 RP 可无条件；fixed-$(q,\omega)$ 的 P 陈述保留。

## 状态

* 定理：**[已证-纸面，M2]**；引理 4 已按专家 §1.2 修复；引理 8 已由桥接引理 + SL95（Las Vegas）闭合；待专家复核升 M3。
* 机器核验：判据实现与单侧性 **39/39 一致**；不构成定理的机器证明。
* 与 49/50 号答复的对应：RP 路线被确认"structurally sound"；剩余是 Smith 引理与位长记账。
