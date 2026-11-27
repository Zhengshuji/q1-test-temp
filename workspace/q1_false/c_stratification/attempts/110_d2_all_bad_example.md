# $d=2$ 的首个例子：整层全坏（与 $d=1$ 的混合相反）

> 2026-11-08。做 item 3（$d\ge2$ 的对应族）的第一例：$k=3,q=3,\omega=2$、$d=2$ 的实例
> （seed 138）。结论：可容许轨迹只有两个点，且两点都**整层全坏**；与 $d=1$ 的"混合"相反。
> 状态：**M2（纸面）**；程序化核对 1 实例。

## 目标

对 $d=2$ 的实例（seed 138）：
1. 算出可容许 $\sigma$ 的集合；
2. 对每个可容许点，证明整条纤维全坏（公共 $\lambda_0$）；
3. 与 $d=1$ 的族定理（attempts/109：开层全坏、例外点好）对比。

## 设想与理由

* $d=1$ 时兼容条件只有 $y_1=0$，纤维里还有自由度让例外点变好；$d=2$ 时兼容条件是两条方程，
  纤维的自由度更小，可能没有好点。
* 若 $d=2$ 的每个可容许点都有公共 $\lambda_0$，则整层全坏——这正是 $d\ge2$ 与 $d=1$ 的分水岭。

## 做法

**实例数据**（`make_instance(7,2,1,138*41+2*7+1)`）：$n=7,p=2,r=1$，$k=3,d=2$，
$$U_0=0,\quad V_0=(-1,0,0),\quad
Z_1=\begin{pmatrix}0&0\\0&0\\0&1\end{pmatrix},\quad
Z_2=\begin{pmatrix}0&0\\1&0\\0&1\end{pmatrix}.$$

**可容许 $\sigma$**：$E=0$，$F_0=\langle e_1\rangle$，故 $\sigma\cdot V_0=0\iff\sigma_1=0$。
写 $\sigma=(0,1,t)$ 或 $(0,0,1)$。

* $\sigma=(0,1,t)$：$S=\ker\sigma=\langle e_1,\,-t e_2+e_3\rangle$。取 $B=(e_1,\,-t e_2+e_3)$，
  $$P=B^\top Z_1=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
  Q=B^\top Z_2=\begin{pmatrix}0&0\\-t&1\end{pmatrix}.$$
  $\operatorname{rank}Q=1$；$\operatorname{rank}[P;Q]=2$（$t\ne0$）或 $1$（$t=0$）。
  故 $\dim X_S=2-(2-1)=1$（$t\ne0$）或 $2-(1-1)=2$（$t=0$）。$E=0$，$E+X_S=S$ 需 $\dim X_S=2$，
  所以 $t\ne0$ 时**不可容许**；$t=0$ 可容许。
* $\sigma=(0,0,1)$：$S=\langle e_1,e_2\rangle$；$P=0$，$Q=\begin{pmatrix}0&0\\1&0\end{pmatrix}$，
  $\operatorname{rank}Q=1$，$\operatorname{rank}[P;Q]=1$，$\dim X_S=2$，可容许。

故可容许轨迹 $=\{(0,1,0),(0,0,1)\}$（两个点，不是 $\mathbb P^1$）。

**$\sigma=(0,1,0)$：整层全坏（$\lambda_0=-1$）。** $S=\langle e_1,e_3\rangle$，$V_0=-e_1$，
$P=Q=\begin{pmatrix}0&0\\0&1\end{pmatrix}$。兼容条件 $b_2=-a_2$；于是
$$x=a_1e_1+a_2e_3,\qquad y=b_1e_1-a_2e_3 .$$
在 $\lambda=-1$ 处，$P(-1)$ 的行：
$$-V_0=e_1,\qquad -x_i-y_i=-(a_{i1}+b_{i1})e_1 .$$
全在 $\langle e_1\rangle$ 里，秩 $\le1<2$。✓

**$\sigma=(0,0,1)$：整层全坏（$\lambda_0=0$）。** $S=\langle e_1,e_2\rangle$，$P=0$，
$Q=\begin{pmatrix}0&0\\1&0\end{pmatrix}$。兼容条件 $bQ=0\Rightarrow b_2=0$；于是
$$x=a_1e_1+a_2e_2,\qquad y=b_1e_1 .$$
$P(\lambda)$ 的行：$e_1$、$(\lambda a_{i1}-b_{i1})e_1+\lambda a_{i2}e_2$。全部 $2$-子式都含因子 $\lambda$：
$$\det(e_1,\lambda x_i-y_i)=\lambda a_{i2},\qquad
\det(\lambda x_i-y_i,\lambda x_j-y_j)=\lambda^2(a_{i1}a_{j2}-a_{i2}a_{j1}).$$
故 $\lambda=0$ 是公共根，秩 $\le1$。✓

## 专家 52 号的更强命题（$U_0=0$ 的一般 $d=2$ 全坏）

> **命题**：设 $k=3,\omega=2,q=3,d=2$、$U_0=0$。则每个可容许压缩点都坏。

*证明骨架*（专家 52 号）：
1. $\ker T\to$ 第二坐标的投影单射，故 $\operatorname{rank}Z_2=2$；取 $0\ne\ell$ 使 $\ell Z_2=0$（左核 1 维）。
2. $V_0Z_2=-U_0Z_1=0$，故 $V_0\in\ker(\cdot Z_2)=\operatorname{span}\{\ell\}$。
3. 若 $V_0=0$：$H=[0;X]$、$H_A=[0;Y]$，$X$ 满秩 2；方阵 pencil $\lambda X-Y$ 的行列式次数 2，有根；
   根处 $3\times3$ pencil 秩 $\le1$。
4. 若 $V_0\ne0$：$V_0=\alpha\ell$，$\ell\in S$；选 $\bar A$ 使 $\bar A Z_2=-Z_1$；兼容
   $y-x\bar A\in\operatorname{span}\{\ell\}$；因 $\ell\in S$，兼容 $y\in S\iff x\bar A\in S$；
   可容许 $\Rightarrow S\bar A\subseteq S$；$S/\operatorname{span}\{\ell\}$（1 维）上的诱导算子有特征值 $\mu$；
   则 $\mu x_i-y_i\in\operatorname{span}\{\ell\}$，顶行 $-V_0\in\operatorname{span}\{\ell\}$，
   故 $\operatorname{rank}(\mu H-H_A)\le1$。

*限定*：不能去掉 $U_0=0$；$U_0\ne0$ 时 $V_0Z_2=0$ 未必成立。

## 进展

* 可容许轨迹与两个点的整层全坏都已证。
* 程序化核对（`workspace/_exchange/d2_seed138.py`）：两个可容许点各 3 维纤维采样，verdict 均为 bad。
* 与 $d=1$（attempts/109）对比：$d=1$ 是 $\mathbb P^1$ 混合；$d=2$ 是两点全坏。

## 最终结论

* $d=2$ 的第一例是**整层全坏**：可容许轨迹两个点，分别有公共 $\lambda_0=-1$ 和 $0$。
* **专家 52 号的命题**把它提升为：$k=3,\omega=2,q=3,d=2,U_0=0$ 时**每个**可容许压缩点都坏；
  本文件的枚举是透明插图。$U_0\ne0$ 不在命题范围内。
* 这说明 $d$ 的大小改变现象：$d=1$ 有例外好点，$d=2$ 没有（至少此例）。
* **不是阶结论**：只是 $q=3,\omega=2$ 的层；$q=2$ 的 $\omega=1$ 层仍可能可行。

## 放弃原因

* 一般 $U_0\ne0$ 的 $d=2$ 情形未处理；专家命题不覆盖 $U_0\ne0$。
* 没有检查 $q=2$ / $\omega=1$，不能声称 $q_{\min}$。
* 没有把"两点全坏"写成 Lean。

## 残留价值

* $d=2$ 的第一个完整分析：可容许轨迹 + 两个公共 $\lambda_0$。
* 与 $d=1$ 的混合形成对照，说明分层/纤维维数确实随 $d$ 改变。
* 给 107 的投影定理提供第二个模型（全坏型）。

## 相关文件

* [attempts/109](109_family_theorem_p1_mixed.md)（$d=1$ 的混合族）
* [attempts/104](104_p2_constrained_locus.md)（$d=1$ 单例）
* [tools/verification/p2_stratification_check.py](../../../../tools/verification/p2_stratification_check.py)
* `workspace/_exchange/d2_seed138.py`（本文件的枚举脚本）

## 状态

* 实例分析：**[已证-纸面]**（两个点全坏，公共 $\lambda_0$）。
* **专家命题**（$U_0=0$ 的一般 $d=2$ 全坏）：**[已证-纸面，专家 52 号]**；$U_0\ne0$ 不覆盖。
* 程序化核对：**[精确验证 1 实例]**（两点的纤维采样均 bad）。
* 未做：$U_0\ne0$、Lean、实点。
