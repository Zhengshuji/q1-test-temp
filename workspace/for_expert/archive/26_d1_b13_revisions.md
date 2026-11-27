# 送审材料：D.1 与 B.13 的修订，以及 B.4 的约定澄清

本份回应你上轮的三条裁决（B.4 有缺口、D.1 需额外假设、B.13 有缺口），并附上你要求的完整修订。
记号沿用前几份报告；$(5a)/(5b)$ 与 $\mathcal V,\mathcal Z,S,K,W$ 的定义不变。

---

# Part I. B.4：约定的澄清（你的更正成立，附机器核验）

你的裁决：使铅笔降秩的是 $A$ 的**右**特征向量，不是 $A^{\mathsf T}$ 的。我们据此做了核验。

**核验方式**：在 $\mathcal V=\mathbb C^n$ 的实例上（$n=3$，随机整数，共 3962 个），逐条比较

* **(P)** $\exists\,0\ne x:\ Cx=CAx=0$ 且 $(\lambda I-A)x=0$（右特征向量）；
* **(D)** $\exists\,0\ne\varphi:\ \varphi C=\varphi CA=0$ 且 $\varphi(\lambda I-A)=0$（$A^{\mathsf T}$ 的左特征向量）；
* （R）铅笔 $[\lambda\mathcal L-\mathcal LA;CA;C]$ 在 $\lambda$ 处列满秩失效。

**结果**：

| 判据 | 与 (R) 一致 | 反例 |
|---|---|---|
| (P) | **3962 / 3962** | 0 |
| (D) | 3845 / 3962 | **117** |

所以你的更正是对的：**(P) 才是 B.4 的正确形式**。

**但要记录一处内部不一致**：项目原先的 Lean 内核（`b4_iff_no_eigenvector`）证的其实是 (D)——
它给出 $\dim(M\top+\mathcal J)=n\iff\ker M^{\mathsf T}\cap\mathcal J^{\perp}=0$。这在数学上是对的
（零化子恒等式），但它对应的不是本项目的行空间约定下的铅笔秩降。因此：
该条**不再算作 B.4 的 Lean 覆盖**；按 (P) 重述的内核列为待办。
我们在条目里显式写了"行约定"与"(P)/(D) 二者的区别"。

---

# Part II. D.1：按你的要求补全（定义、空族约定、良定义、逐 $U$ 证明）

## II.1 定义与约定

$$P(A,B,S):=\begin{cases}\min\{\dim U:\ S\le U,\ \Phi(U)\subseteq(U+B)/B\}, & \text{可行族非空},\\ +\infty, & \text{否则},\end{cases}\qquad \Phi:=\pi_B\circ A .$$

取值在 $\mathbb N\cup\{+\infty\}$，约定 $\dim S+(+\infty)=+\infty$。明确**弃用**空族时 $P=0$ 的约定。

## II.2 下界：逐可行 $U$（你推荐的结构）

固定任意可行 $U$。由 $S\le U$、$AU\le U+B$：

$$\frac{AS+S+B}{S+B}\hookrightarrow\frac{U+B}{S+B}\cong\frac{U}{U\cap(S+B)},\qquad
\dim\frac{U}{U\cap(S+B)}\le\dim\frac{U}{S}\quad(\text{因 }S\le U\cap(S+B)).$$

于是 $\dim U=\dim S+\dim\frac US\ \ge\ \dim S+\dim\frac{AS+S+B}{S+B}$，对 $U$ 取最小即得下界。
这一步不使用任何递归或商不变性。

## II.3 递归：$\Phi'$ 的良定义与两半

记 $M=T+C$、$\pi:Y\twoheadrightarrow Y/M$、$C'=\pi\Phi(M)$、$T'=\pi\Phi(T)$，并令
$$\Phi':\frac{Y}{M}\longrightarrow\frac{Y/M}{C'},\qquad \Phi'(y+M)=\Phi(y)+C' .$$

**良定义**：若 $y'-y=m\in M$，则 $\Phi(y')=\Phi(y)+\Phi(m)$，而 $\Phi(m)\in\pi^{-1}(C')$，故在 $C'$ 的商里相同。$\square$

这里正是你指出的要点：$\Phi$ **不**诱导 $Y/M$ 上的自同态，它的像落在**再来一次商** $\frac{Y/M}{C'}$。
同一个陷阱在本项目里出现过一次：$A(\mathcal J)\not\subseteq\mathcal J$，所以 $A$ 不诱导 $\mathbb C^n/\mathcal J$ 上的映射；
正确的对象是 $\rho_{ci}=P(T,B,U_0)$ 里的 $T$（$A$ 在 $\mathbb C^n/\mathcal J$ 上**由 $(5a)$ 保证**的诱导作用）。

**$(\ge)$ 半**：对可行 $U$，$\pi(U)$ 对商问题可行，且 $\dim(U\cap M)\ge\dim T$，故
$\dim U\ge\dim T+\mathcal P(Y/M,C',\Phi',T')$。

**$(\le)$ 半**：对商问题的可行 $U'$，取 $U=\pi^{-1}(U')$；需要区间包含引理 + $M\to C'$ 的满射性给出修正映射 $\sigma$，
使 $\Phi(\sigma u')\in\pi^{-1}(U')+C$。这一步仍是纸面（算法与构造在支撑材料里），也是唯一尚未形式化的部分。

**空族一致性**：由 $U\leftrightarrow\pi(U)$ 的对应得"可行族非空 $\iff$ 商问题可行族非空"，故两边同为 $+\infty$。

---

# Part III. B.13：射影化的修订（接受"有缺口"，给出修正构造与待证三引理）

## III.1 修正后的构造

参数取 $[\alpha:\beta]\in\mathbb P^1$，关系齐次化：
$$\mathfrak I:=\bigl\{([x],[z],[\alpha:\beta])\in\mathbb P^{n-1}\times\mathbb P^{n-1}\times\mathbb P^1:\ z\wedge(\alpha I-\beta A)x=0,\ z\ne0\bigr\}.$$
在 $\beta\ne0$ 的仿射图（$\lambda=\alpha/\beta$）上退化为原 $\lambda$-族；在 $\beta=0$ 上给出无穷远纤维 $[z]=[Ax]$。
这样在整条 $\mathbb P^1$ 上有定义——原写法在无穷远点无意义，这是你指出的第一处缺口。

## III.2 三段式分解（按你的建议）

| 引理 | 待证内容 |
|---|---|
| 入射引理 | $\mathfrak I$ 在 $\mathbb P^{n-1}\times\mathbb P^{n-1}\times\mathbb P^1$ 中闭，且维数上界可按 $\dim\mathcal V$、$\dim K$ 算出 |
| 纤维引理 | 投影 $\mathfrak I\to\mathbb P(\mathcal V)\times\mathbb P^1$ 的纤维至多一点（对固定 $([x],[\alpha:\beta])$，$[z]$ 被决定）|
| 覆盖引理 | 在**可构造像**上做维数估计（不用"闭投影仍闭"），得"整族不可行"的充分条件 |

## III.3 与 B.13e 分开

单-$\lambda$ 证书（$\dim V=\dim K$、$(\lambda_0I-A)V=K$、$V\cap K=0$）自成一条，不并入一般入射定理。

## III.4 剩余缺口（明确记录）

三引理的**证明**尚未完成：需要在齐次版上重做维数计数，并处理 $z\ne0$、$x\in\mathcal V$ 这两个开条件。
我们不再把它当作已完成定理；条目状态标为"有缺口（方向已定，证明待补）"。

---

# Part IV. 其余修订（你列出的 12 条资格）

已逐条写进对应条目：A.1 拆分商等价与下界可达性；G.1 补次数界依据、realification、bit-size 界；
F.1 只作必要条件；H.1 保留 $A(S)\subseteq Z$ 为显式假设并注明 $[U\mid P]$ 不必方阵；
B.3 去掉 $L_0\ne0$；B.8 改用正规秩 $h$ 的 $\Delta_h$；B.9 改用 $q\ge1$；
B.11 声明 Type I 只是数值分类；B.16 用 $\exists\lambda:\ker N_Z(\lambda)\not\subseteq S$；
B.21 不要求 $q\ge1$；B.23 声明不需要 $K_1$ 可对角化；B.24 声明不需要 $L$ 行满秩。

另外按你的建议做了两项结构合并：

1. **B.16 + B.17 + B.21 → 一条**（统一商铅笔定理）：三段分别是分层判据、永久核与精确失败判据、右零空间与指标；
   理由是三者都是同一个 $\overline N_{\mathcal Z}(\lambda):V/S\to X/\mathcal Z$ 的不同侧面。
2. **B.23 + B.24 → 内蕴谱刻画**：由 $\Phi=K_1|_W$ 得
   $$(5b)\ \text{失败}\iff\exists\,0\ne w\in W:\ \Phi(w)=K_1w\in\mathbb C w ,$$
   与"$\overline N_{\mathcal Z}(\lambda)$ 逐点单射"是同一障碍的两种写法。这一形式不需要人为选择整空间扩张 $\Lambda$。

---

# Part V. 请求

1. **D.1**：请只看 §II.3 的 $(\le)$ 半——$\sigma$ 的区间包含一步是否成立、条件是否够；其余部分是否可接受为定稿？
2. **B.13**：三段式分解是否是正确的拆法？若你同意，我们先只写"入射引理"（齐次、闭、维数），
   纤维与覆盖两步留到下一轮。
3. **B.4**：按 (P) 重述的 Lean 内核我们随后补；在此之前 B.4 的等级是"纸面 + 精确验证（3962/3962）"。
4. 合并后的 B.17 与内蕴谱刻画是否就是你设想的"统一商铅笔定理 + 内蕴谱刻画"？
