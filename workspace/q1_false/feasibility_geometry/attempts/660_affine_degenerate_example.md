# 660 仿射铅笔的退化例子：$B$ 被约束出零列 ⇒ 必败

> 2026-11-27。检验 659 的“仿射铅笔问题”：给一个 $V=I$、$d=2$、$S=e_1$ 的小例，定理 2 的约束把 $B$ 的第二列逼成零，
> 于是任何 $B\in\mathcal B$ 都使铅笔在 $\lambda=0$ 掉秩。
> 状态：**[已证-纸面]** + **[精确验证]**。

## 设定

$k=2$、$q=3$、$d=2$、$Z'=\begin{bmatrix}0&0\\1&0\end{bmatrix}$、$S=\operatorname{span}\{e_1\}$。
$K=S^\perp=\operatorname{span}\{e_2\}$。
取 $V=I_2$、$U=\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}$（$H=UV=U$，$\operatorname{im}H=\operatorname{span}\{e_1,e_2\}$）。

## 定理 2 的约束

$\ker(V|_K)=0$（$V$ 在 $K$ 上单射）⇒ 约束唯一确定 $B$ 在 $V(K)=\operatorname{span}\{e_2\}$ 上的值：
$$B e_2=U\,(VZ'e_2)=U\cdot0=0 .$$
所以 $B$ 的第二列为零：$B=\begin{bmatrix}b_1&0\\b_2&0\\b_3&0\end{bmatrix}$。

## 铅笔必败

$$P(\lambda)=\lambda U-B=\begin{bmatrix}\lambda-b_1&0\\-b_2&\lambda\\-b_3&0\end{bmatrix}.$$
非零 2×2 子式：
$$-\lambda(\lambda-b_1),\qquad b_3\lambda .$$
无论 $b_1,b_2,b_3$ 取何值，
$$\gcd=\lambda\quad(\text{非平凡})\ \Rightarrow\ (5b)\ \text{失败}.$$

（sympy：子式 $[-\lambda(b_1-\lambda),0,b_3\lambda]$，gcd $=\lambda$。）

## 意义

- 定理 2 的仿射空间 $\mathcal B$ 可以**退化**到使铅笔必败（这里 $B$ 的整列被钉为零）；
- 所以“$\mathcal B\ne\varnothing$”远不等于可行；
- 该例也说明 $V=I$ 的分解方式可能不是好的选择（$H$ 的核为零，$d=q$？这里 $q=3>d=2$）。

## 注意

- 这只是**固定 $H$**（固定 $U,V$）的失败，不是实例级不可行；
- 该数据对应 657 的实例（$r_0=0$ 时取 $L=0$ 可行）；实例层面要排除所有 $H$ 才行。

## 下一步

1. 对同一数据，换 $V$（不同分解 $H=UV$）看是否存在可行的 $\mathcal B$；
2. 找出“任何 $V$ 都失败”的判据——这才是实例级不可行的证明路径；
3. 与 ChatGPT 核对这个退化机制。

## 状态

- 退化例子：**[已证-纸面]** + **[精确验证]**；
- 实例级判据：**[开放]**。
