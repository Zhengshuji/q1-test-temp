# 两处缺口的补证：D.1 递归的 $\sigma$ 构造、B.13a 齐次入射簇

本份只回你上一轮的第二与第三点（D.1 的 $(\le)$ 半、B.13 的入射构造），并请你就两处各确认一句。
记号与 B.13 的构造沿用上一份报告。

---

# Part I. D.1：$\sigma$ 的显式定义方程

你的要求是：把"存在修正映射 $\sigma$"换成**显式线性代数方程**。下面是完整的三段。

## I.1 设定

$Y$ 有限维、$C\le Y$、$\Phi:Y\to Y$ 线性；$T\le Y$ 为强制子空间。记
$$M:=T+C=M,\qquad \pi:=\mathrm{mkQ}\,M:Y\twoheadrightarrow Y/M,\qquad \widehat\pi:Y/C\twoheadrightarrow Y/M\ \ (\widehat\pi(y+C)=y+M),$$
$$C':=\widehat\pi\bigl(\Phi(M)\bigr),\qquad T':=\widehat\pi\bigl(\Phi(T)\bigr),$$
$s:Y/M\to Y$ 为 $\pi$ 的**线性截面**（$\pi\circ s=\mathrm{id}$）。商问题：
$$\mathcal P'\ :=\ \min\bigl\{\dim U':\ T'\le U'\le Y/M,\ \ \forall u\in U':\ \widehat\pi\Phi(su)\in U'+C'\bigr\}.$$

（$\widehat\pi$ 良定义正因 $C\le M$。这是你上一轮指出的记号问题，已在所有式子中改正。）

## I.2 三条方程

**(a) $\gamma$-方程。** 由 $C'\le\widehat\pi\Phi(M)$（定义），存在**线性** $\gamma:C'\to M$ 使
$$\boxed{\ \widehat\pi\bigl(\Phi(\gamma c)\bigr)=c\qquad\forall c\in C'.\ }$$

**(b) $\beta$-方程。** 令 $\tau:U'\to\frac{Y/M}{U'}$、$q:C'\to\frac{Y/M}{U'}$ 为商映射的复合。
"$U'$ 可行"即 $\operatorname{range}\tau\le\operatorname{range}q$，故存在**线性** $\beta:U'\to C'$ 使
$$\boxed{\ U'.\mathrm{mkQ}\bigl(\beta u\bigr)=U'.\mathrm{mkQ}\bigl(\widehat\pi\Phi(su)\bigr)\qquad\forall u\in U'.\ }$$

**(c) $\sigma$ 的定义。**
$$\boxed{\ \sigma:=-\gamma\circ\beta:\ U'\longrightarrow M\ }$$

## I.3 校正的显式计算

$$\widehat\pi\Phi\bigl(su+\sigma u\bigr)
=\widehat\pi\Phi(su)+\widehat\pi\Phi\bigl(\gamma(\beta u)\bigr)\cdot(-1)
=\widehat\pi\Phi(su)-\beta u\ \in\ U'.$$
第二等号用 $\gamma$-方程；末一等号用 $\beta$-方程（两者在 $\frac{Y/M}{U'}$ 里同像）。

## I.4 构造与维数

$$U:=\operatorname{span}\Bigl(T\ \cup\ \{su+\sigma(u):\ u\in U'\}\Bigr).$$
因 $\sigma(u)\in M$ 而 $su$ 是 $M$ 的截面方向，$\dim U\le\dim T+\dim U'$；可行性 $\Phi(U)\subseteq U+C$ 由 I.3、
$\Phi(T)\subseteq\pi^{-1}(T')\le U$ 与 $C\subseteq M\le U$ 逐项验证。于是
$$\mathcal P\le\dim U\le\dim T+\dim U'\qquad\Longrightarrow\qquad \mathcal P\le\dim T+\mathcal P'.$$

## I.5 机器检查状态

三段都已在 Lean 里机器检查，且登记为"差异：无"：
$\gamma,\beta$ 的提升（`exists_lift_of_range_le`）、$\sigma$ 的存在与逐点校正（`exists_sigma`）、构造步（`lift_admissible`）。

**请确认**：I.4 的 $\dim U\le\dim T+\dim U'$（$\sigma(u)\in M$、$su$ 沿补空间方向）是否就是你所要求的"显式构造"？
若是，递归等式即视为闭合。

---

# Part II. B.13a：齐次入射簇（已完整证明）

## II.1 构造（按你上一轮的修正）

$E$ 为 $n$ 维、$A:E\to E$、$V\le E$（$\dim V=v$）、$K\le E$（$\dim K=k$）、$P_{\alpha,\beta}=\alpha I-\beta A$。
$$\mathcal D:=\mathbb P(V)\times\mathbb P^1,\qquad
\mathcal B:=\bigl\{([x],[\alpha:\beta])\in\mathcal D:\ P_{\alpha,\beta}x=0\bigr\},$$
$$\mathfrak I:=\bigl\{([x],[z],[\alpha:\beta])\in\mathbb P(V)\times\mathbb P(K)\times\mathbb P^1:\ z\wedge P_{\alpha,\beta}x=0\bigr\},\qquad
\pi:\mathfrak I\to\mathcal D .$$

## II.2 引理 1：闭性

截面 $\Phi([x],[z],[\alpha:\beta]):=z\wedge(\alpha x-\beta Ax)\in\wedge^2E$ 对 $x\mapsto cx$、$z\mapsto dz$ 各齐次一次
（$\Phi\mapsto cd\,\Phi$），故在投影空间上良定义；"$z\wedge w=0$"是"全部 $2\times2$ 子式为零"的闭条件。
故 $\mathfrak I=\Phi^{-1}(0)$ 闭。$\square$

## II.3 引理 2：$\mathcal B$ 之外的纤维维数 $\le0$

若 $P_{\alpha,\beta}x\ne0$，则 $z\wedge P_{\alpha,\beta}x=0$ 迫使 $[z]=[P_{\alpha,\beta}x]$；该点存在 $\iff P_{\alpha,\beta}x\in K$。
故纤维至多一点。$\square$

## II.4 引理 3：$\mathcal B$ 之上的纤维维数 $=k-1$

若 $P_{\alpha,\beta}x=0$，楔积条件自动成立，纤维 $=\{[x]\}\times\mathbb P(K)$，维数 $k-1$。$\square$

## II.5 定理：维数估计

分两块：$\pi^{-1}(\mathcal B)$ 是 $\mathcal B$ 上的 $\mathbb P(K)$-丛，维数 $\dim\mathcal B+(k-1)$；
$\pi^{-1}(\mathcal D\setminus\mathcal B)$ 的纤维维数 $\le0$，故维数 $\le\dim\mathcal D=v$。于是
$$\boxed{\ \dim\mathfrak I\ \le\ \max\bigl\{\,v,\ \dim\mathcal B+k-1\,\bigr\}.\ }$$

## II.6 推论

若 $A$ 在 $V$ 中没有特征向量，则 $\mathcal B=\varnothing$，于是 $\dim\mathfrak I\le v$。
（$\beta\ne0$ 时 $\mathcal B$ 的非空性等价于存在 $\lambda$ 与 $V$ 中的特征向量；$\beta=0$ 时 $P_{\alpha,0}=\alpha I$ 非奇异。）

## II.7 还缺什么

把 II.5 变成"整族不可行"的覆盖判据还需一步：对投影 $\mathfrak I\to\mathbb P(K)$ 做维数比较
（若 $\dim\mathfrak I<k-1$，投影不满，存在未被覆盖的 $[z]$）。**这一步没有写出**。

**请确认**：II.2–II.6 是否已构成你要的 B.13a？以及覆盖判据是否就是上述维数比较的推论。

---

# Part III. 请求

1. D.1：I.4 的构造与维数不等式是否满足你要求的"显式"标准？
2. B.13a：II.2–II.6 是否完整？覆盖判据是否即"$\dim\mathfrak I<\dim\mathbb P(K)$ ⟹ 投影不满"？
3. 若两条都通过，我们把 D.1 的递归与 B.13a 分别升为 `[已证] + [Lean-conditional]` 与 `[已证]`，
   并在登记表里把它们与"仅有数值/仅有纸面"的条目分开列。
