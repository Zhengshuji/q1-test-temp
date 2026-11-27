# $c=1$ 层的特征线：显式计算（16/21）

> 2026-11-08。182 的非特征线引理把 $q=4,\omega=3$ 的 `none` 升级到“除特征线外不可行”。
> 本文件把特征线算出来：seed 21 有**两条有理特征线**，seed 16 有**两条复共轭特征线**。
> 状态：**M2（计算）**；逐线精确检验待做。

## 目标

解 $\det[v,Av]=0$（$v=a w_0+b w_1$）的齐次二次方程，列出特征线，供逐线检验。

## 设想与理由

182 的引理只剩特征线；特征线由齐次二次方程给出，至多两条。把二次方程显式解出来，
就能把“连续族”降成“4 条固定线”，方便逐线精确检验。

## 做法

取 $v(a,b)=a w_0+b w_1$（作为 $K_0$ 坐标，再嵌入 $\mathbb C^n$ 为 $Nv$），
$Av=aAw_0+bAw_1$。对坐标对 $(i,j)$ 算 $2\times2$ 子式：
$$\Delta_{ij}(a,b)=(a w_{0,i}+b w_{1,i})(a Aw_{0,j}+b Aw_{1,j})-(i\leftrightarrow j),$$
取一个非零的 $\Delta_{ij}$，写成
$$\alpha a^2+\beta ab+\gamma b^2=0.$$

## 结果

### seed 21

$$\alpha=1,\quad\beta=-1,\quad\gamma=0:\qquad a(a-b)=0.$$
两条**有理**特征线：
$$L_1=\mathbb Cw_1\ (a=0),\qquad L_2=\mathbb C(w_0+w_1)\ (a=b).$$
两者都在 180 工具的 grid 枚举中（$t=\infty$ 与 $t=1$），均返回 `none`；但当时没有“逐线完整”的证明。

### seed 16

$$\alpha=2,\quad\beta=-2,\quad\gamma=1:\qquad 2a^2-2ab+b^2=0,\qquad \Delta=-4.$$
两条**复共轭**特征线：
$$\frac{b}{a}=1\pm i.$$
即 $L_\pm=\mathbb C(w_0+(1\pm i)w_1)$，不是有理线；有理算术工具无法直接枚举。

## seed 21 的特征线检验（2026-11-08）

在 $L_1=\mathbb Cw_1$ 与 $L_2=\mathbb C(w_0+w_1)$ 上，精确计算可容许解空间投影到 $(b,c)$ 的最大秩：
```
w1       max (b,c) rank = 1
w0+w1    max (b,c) rank = 1
```
需要 $\operatorname{rank}=2$ 才能有 $\operatorname{rank}H=3$；两条线都只有 1，故 **$\operatorname{rank}H\le2<3$**，
$L_1,L_2$ 不可行。结合 182 的非特征线引理：**seed 21 的 $q=4,\omega=3$ 完全不可行**。

## seed 16 的复特征线（已完成）

在 $\mathbb Q(i)$ 上重做（复数用有理数对表示，精确 Gaussian 消元）：
- $v=w_0+(1+i)w_1$；
- $Av$ 的 $K_0$ 坐标 $w$ 由 $Nw=Av$ 解出；
- $\operatorname{Ann}(L)$ 的基 $h_0,u_1,u_2$；
- $\varphi_j=u_j\cdot w$，计算得 $\varphi=(1,0)\ne0$。

于是可容许条件 $b\cdot\varphi=0$ 给 $b$ 一个**真超平面**（复 1 维），三个底部行的 $(b,c)$ 最大秩为 **1** $<2$，
故 $\operatorname{rank}H\le2<3$，该复特征线**不可行**；共轭线同理。

## seed 16 / 21 的结论

- 非特征线：182 引理，不可行；
- 21 的两条有理特征线：秩 1，不可行；
- 16 的两条复特征线：秩 1，不可行。

所以 **$q=4,\omega=3$ 对两个 seed 都完全不可行**。结合 $q=4,\omega=2$ 也不可行，
$q=4$ 的 $\omega=2,3$ 两层都被排除；**但 $q=4$ 还有 $\omega=1$（$c=3$）与 $\omega=4$（$c=0$）两层未查**，
所以尚不能断言 $q=4$ 全部排除。

## 进展

* 特征线从“≤2 条”变成**显式**：21 两条有理线，16 两条复共轭线；
* 非特征线由 182 的引理覆盖；
* 剩余：在 $L_1,L_2$（21）与 $L_\pm$（16）上逐线检验 $\operatorname{rank}H=3$ 与铅笔好性。

## 最终结论

* 21 的特征线是有理的，可精确检验；
* 16 的特征线是复的，需要 $\mathbb Q(i)$（或 $\mathbb Q(\sqrt{-1})$）上的精确算术；
* `none` → 证明的最后一步是这四条线（各 1 条 $L$）上的有限检验。

## 放弃原因

* 未在 $L_1,L_2,L_\pm$ 上完成“rank3 + 好铅笔”的精确判定；
* 未把二次方程的一般解写成 $W_L$ 不 $\subseteq D$ 的情形；
* 未 Lean 化。

## 残留价值

* 特征线的显式表达；
* 明确了最后一步是 4 条固定线（不是连续族）。

## 相关文件

* [attempts/182](182_c1_infeasibility_lemma.md)（非特征线引理）
* [attempts/180](180_uniform_stratum_solver.md)（工具）
* [attempts/179](../../decision_algorithms/attempts/179_c2_scope.md)（范围）

## 状态

* 特征线计算：**[M2，精确有理]**。
* 逐线判定：**[未做]**。
