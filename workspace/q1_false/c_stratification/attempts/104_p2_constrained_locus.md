# $k=3,\omega=2,q=3$ 的 $\mathbb P^2$ 约束轨迹：首个正维混合例子

> 2026-11-08。落实专家 51 号答复的"具体实验"：$k=3,\omega=2,q=3$ 的精确分量分析。
> 实例来自随机生成器（`qmin_scan_pr.make_instance(7,2,1,179)`）；工具在 `workspace/_exchange/`（未入 git）。

## 目标

专家 51 号答复建议：**先做 $k=3,\omega=2,q=3$ 的 $\mathbb P^2$ 精确分量分析**——admissibility、
compatibility 矩阵的秩分层、$E+X_S=S$、逐分量 generic determinant divisor；再写
$k=\omega+1$ 的投影约束定理。本文件记录第一个正维例子。

## 设想与理由

* 专家 51 号答复：先做 $k=3,\omega=2,q=3$ 的 $\mathbb P^2$ 分量分析；不要先分类全部分量，
  先在 incidence 空间上按兼容秩分层。
* 找"正维"可容许轨迹：若 $U_0=0$（$E=0$）且 $Z_1=0$，兼容条件退化为对 $y$ 的一个线性方程；
  $F_0$ 只给 $\sigma$ 一个线性条件，轨迹可能是 $\mathbb P^1$。
* 若 $V_0$ 本身落在兼容核方向里，则 $\lambda_0=0$ 处整族掉秩——这是最便宜的"公共 $\lambda_0$"结构。

## 做法

* 用 `qmin_scan_pr.make_instance(7,2,1,179)` 生成实例；算 $N_K,U_0,V_0,Z_1,Z_2$（$K$-坐标）。
* 枚举 $\sigma=(a,-4b,b)$（即 $\sigma\cdot V_0=0$），对每个 $S=\ker\sigma$ 取基 $B$；
  兼容条件 $y_1=0$，构造 $H=[0;x_1;x_2]$、$H_A=[V_0;y_1;y_2]$，检验 $\operatorname{rank}$ 与 $2$-子式 gcd。
* 一般点用 $\lambda_0=0$ 的秩论证；例外点用纤维搜索。

## 实例

$n=7$、$p=2$、$r=1$、$q=3$；由 `make_instance(7,2,1,179)` 生成。计算得

$$k=3,\qquad d=\dim\ker T=1,\qquad
U_0=L_0N_K=(0,0,0),\qquad V_0=L_0AN_K=(0,-1,-4),$$
$$Z_1=0,\qquad Z_2=e_1=(1,0,0)\quad(\text{K-坐标}).$$

（$E=0$、$F_0=\langle V_0\rangle$；$V_0$ 的第一坐标为 $0$，这是关键。）

## 进展

**1. 可容许轨迹是 $\mathbb P^1$。** $E=0$，故只需 $F_0\subseteq S$，即 $\sigma\cdot V_0=0$：
$$\sigma=(\sigma_1,\sigma_2,\sigma_3),\qquad -\sigma_2-4\sigma_3=0
\iff \sigma\propto(a,-4b,b),$$
即 $\mathbb P^2$ 中的一条**射影直线**（不是有限个点）。

**2. 兼容对与 $X_S$。** $Z_1=0$、$Z_2=e_1$，故兼容条件为 $y_1=0$；对任意 $x\in S$ 都可取
$y\in S\cap\{y_1=0\}$，所以 $X_S=S$，$E+X_S=S$ 自动。于是**整条 $\mathbb P^1$ 都可容许**。

**3. 一般层（$\sigma\ne(1,0,0)$）全坏（证明）。** 设 $S\ne\{y_1=0\}$。则
$S\cap\{y_1=0\}$ 是 $S$ 中的一条线；又 $V_0\in S$ 且 $(V_0)_1=0$，故
$$S\cap\{y_1=0\}=\langle V_0\rangle.$$
于是每个兼容的 $y_i$ 都是 $V_0$ 的倍数。在 $\lambda_0=0$ 处，铅笔
$$\lambda H-H_A=\begin{pmatrix}-V_0\\-y_1\\-y_2\end{pmatrix}$$
的三行全在 $\langle V_0\rangle$ 里，秩 $\le1<2=\omega$。**故一般层全坏**（公共 $\lambda_0=0$）。

**4. 例外点 $\sigma=(1,0,0)$：是好的（显式）。** 此时 $S=\{y_1=0\}$，$S\cap\{y_1=0\}=S$（2 维），
$\lambda_0=0$ 的论证失效。在 $S$-坐标 $(e_2,e_3)$ 里取
$$H=\begin{pmatrix}0&0\\1&0\\0&1\end{pmatrix},\qquad
H_A=\begin{pmatrix}-1&-4\\0&1\\1&0\end{pmatrix},$$
则 $\operatorname{rank}H=2$、$\operatorname{rank}\binom{H}{H_A}=2$（可容许），且三个 $2$-子式为
$$-1-4\lambda,\qquad 4+\lambda,\qquad \lambda^2-1,$$
gcd $=1$。**故该点是好的**——与"整条 $\mathbb P^1$ 全坏"相反。

**5. 采样为什么漏了它。** 之前的脚本在 $q_v=p=0$ 时把 $y$ 固定为 $0$，而例外点的兼容 $y$ 是
2 维自由的；所以"16 个 $\sigma$ 全坏"是**采样漏点**，不是事实。修正后：$\mathbb P^1$ 是**混合**的。

**6. 例外点的完见证（回代 $R$）。** 把上面的 $(H,H_A)$ 回代成显式的 $R$（$2\times7$）：
$$R=\begin{pmatrix}0&0&0&0&0&1&0\\0&0&-\tfrac75&1&0&0&-\tfrac45\end{pmatrix},\qquad
L=\binom{L_0}{R}.$$
`consistency_checks.check_candidate` 七条全过：
$\operatorname{rank}[C;L]=5$、$\dim\ker=2$、$CZ=LZ=0$、$(5a)$ 成立、$h=6=$ 法秩、
gcd/Toeplitz 一致（$(5b)$ 成立）、域 $=\mathbb Q$。故这个好点是**完见证**（不只是抽象 $(H,H_A)$）。

**7. 开层的 generic gcd（符号证书）。** 在开层取 $\sigma=(1,t,-t/4)$（$t\ne0$），$S=\ker\sigma$ 的基为
$b_1=(-t,1,0)$、$b_2=(t/4,0,1)$；$V_0=(0,-1,-4)$，兼容方向 $n_q=(t/4,t)$。令
$x_i=a_iB$、$y_i=s_i\,n_qB$，在 $\mathbb Q(t,a_1,a_2,s_1,s_2)[\lambda]$ 上算三个 $2$-子式的 gcd：
$$\gcd\{2\text{-子式}\}=\lambda\,t .$$
$t\ne0$ 时这是 $\lambda$（差单位），即**公共根恰为 $\lambda=0$**，没有其它公共根。
这把"公共 $\lambda_0=0$"从逐点论证升级为**整层的 gcd 证书**：开层每一点都坏，且坏根就是 $0$。
（计算：`workspace/_exchange/p2_generic_gcd.py`，sympy 符号 gcd；另用 8 组随机有理参数复核，gcd 均为 $\lambda$。）

**8. 同参数的两个额外实例（粗扫，不作结论）。** 同 $(n,p,r)=(7,2,1)$ 的 seed 589、794 也给出
$k=3,d=1$ 与 $\mathbb P^1$ 可容许轨迹；各 8 个 $\sigma$ 的纤维粗扫全坏。但第一例的教训是粗扫会漏好点
（例外点被漏过），所以这两例只是**待查**，需逐例符号 gcd 才能下结论。

## 最终结论

* 这个 $k=3,\omega=2,q=3$ 实例的 $\mathbb P^1$ 可容许轨迹是**混合**的：
  * 开层（$\sigma\ne(1,0,0)$）：**整层 gcd $=\lambda$**（符号证书；$t\ne0$ 时 $\lambda t$ 即 $\lambda$），全坏；
  * 例外点（$\sigma=(1,0,0)$）：显式好点（gcd $=1$），并回代出显式 $R$（七条检查全过）。
* **纤维维数在例外点跳变**：一般点 $y$ 被限制在 $\langle V_0\rangle$（1 维），例外点 $y$ 在 $S$ 中 2 维自由。
  这正是专家 51 号答复强调的"**按 compatibility 秩分层**"：Grassmannian 参数 $\sigma$ 本身不足以决定好坏，
  必须把纤维维数/兼容秩一起放进分层。
* R-空间的逐分量定理仍然成立：好点所在的 R-分量上，好集是开稠密；但**从 $\mathbb P^1$ 直接读结论会错**。

> **注（322）**：这里的"$\mathbb P^1$ 混合"是**底空间**层面的说法。全空间其实分成两支：
> $\{b=0\}$（$\sigma=(1,0,0)$，$y$ 二维自由，一般点**好**）与 $\{y\propto V_0\}$（底空间是整个 $\mathbb P^1$，
> $\gcd=\lambda$ 全**坏**）；乘积式 $b\,(-4y_2+y_3)=0$ 给出分解。逐分量看没有"混合"。
> 验证见 [c332](../../../../tools/verification/c332_104_component_split.py)、[attempts/322](322_hyperplane_determinism_components.md)。
* **不是阶结论**：这只是 $q=3,\omega=2$ 的层；$\omega=1$ 层与 $q=2$ 仍可能可行（n=5 的教训）。

## 放弃原因

* 开层上的 **generic determinant divisor**（在 $\mathbb C(t)[\lambda]$ 上）还没算；目前开层是逐点/结构证明
  （公共 $\lambda_0=0$），不是整层的一个 gcd 证书。
* 例外点的好点还没有回代出 $R$（Grassmann 判据的充分性保证可回代，但未显式做）。
* 没有检查 $\omega=1$ / $q=2$，所以不能声称 $q_{\min}$。

## 残留价值

* 一个**同一 $\mathbb P^1$ 上好坏并存**的约束例子：开层全坏、例外点好；直接说明"必须按秩分层"。
* "公共 $\lambda_0$" 结构：若 $V_0$ 落在兼容核方向的交里，则 $\lambda_0$ 处整层掉秩——这是
  $k=\omega+1$ 投影定理的一个可证明特例。
* 实例数据（$U_0,V_0,Z_1,Z_2$）与脚本可直接复用；例外点的显式 $H,H_A$ 可作证书。

## 相关文件

* `workspace/_exchange/scan_k3_d1.py`（找实例）
* `workspace/_exchange/p2_seed4.py`（P^2 枚举与纤维搜索；未入 git）
* [workspace/ROADMAP.md](../../../ROADMAP.md) §5（专家 51 号答复的优先级）
* [proof/B.24/README.md](../../../../proof/B.24/README.md)（块判据、$q=\omega+1$ 判据）

## 状态

* 开层：**[已证-纸面 + 符号 gcd 证书]**（gcd $=\lambda t$；$t\ne0$ 时即 $\lambda$）。
* 例外点：**[已证-纸面 + 精确验证 + 完见证]**（显式 $H,H_A$，gcd $=1$；显式 $R$ 过七条检查）。
* 层结论：$\mathbb P^1$ 是**混合**的；**不是阶结论**。
