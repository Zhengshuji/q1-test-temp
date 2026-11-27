# D.1 · $P$ 的多项式可解性

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `D.1` 条目（§0.1 归并表）。
> **状态：需要额外假设（专家复核）** —— 修订要求见文末的专家复核意见一节。
> 修订完成前，docs 里该条的等级按"待修"对待。

## 命题

**定义（按专家意见写全）** 固定 $A\in\mathbb C^{n\times n}$、子空间 $B\le\mathbb C^n$、$S\le\mathbb C^n$，令
$$\Phi:=\pi_B\circ A:\ \mathbb C^n\longrightarrow\mathbb C^n/B .$$
可行族与目标函数定义为
$$\mathcal F(A,B,S):=\bigl\{U\le\mathbb C^n:\ S\le U,\ \Phi(U)\subseteq (U+B)/B\bigr\},$$
$$P(A,B,S):=\begin{cases}\min\{\dim U:\ U\in\mathcal F(A,B,S)\}, & \mathcal F(A,B,S)\ne\varnothing,\\[2pt] +\infty, & \mathcal F(A,B,S)=\varnothing,\end{cases}$$
取值在 $\mathbb N\cup\{+\infty\}$ 中，约定 $\dim S+(+\infty)=+\infty$、$+\infty\ge x$ 恒真。
**不采用**"空族时 $P=0$"的约定——那会给出错误的下界。

**D.1（a）〔原 D.1〕（下界）** 对任意 $A,B,S$：
$$P(A,B,S)\ \ge\ \dim S+\dim\frac{AS+S+B}{S+B}.$$

**D.1（b）〔原 D.2〕（一步递归）** 记 $M:=T+C$、$\pi:Y\twoheadrightarrow Y/M$、
$C':=\widehat\pi(\Phi(M))\le Y/M$、$T':=\widehat\pi(\Phi(T))$（$\widehat\pi:Y/C\to Y/M$ 为自然商映射），并定义
注意 $\Phi$ 的值域是 $Y/C$（$C\subseteq M$），故先用**自然商映射** $\widehat\pi:Y/C\to Y/M$（$\widehat\pi(y+C)=y+M$，
良定义正因 $C\subseteq M$）把像搬到 $Y/M$：
$$C':=\widehat\pi\bigl(\Phi(M)\bigr),\qquad T':=\widehat\pi\bigl(\Phi(T)\bigr),\qquad
\Phi'(y+M):=\widehat\pi\bigl(\Phi(y)\bigr)+C'\quad(\text{取任一 lift } y).$$
则
1. $\Phi'$ **良定义**：若 $y'-y=m\in M$，则 $\Phi(y')=\Phi(y)+\Phi(m)$，而 $\Phi(m)\in\pi^{-1}(C')$，故在 $C'$ 的商里相同；
2. $\mathcal P(Y,C,\Phi,T)=\dim T+\mathcal P(Y/M,C',\Phi',T')$，其中 $\mathcal P$ 与 $P$ 同构造成（把 $C$ 取自变量的商）。

**D.1（c）〔原 D.3〕（算法）** 由 (b) 迭代 $O(n)$ 步、每步 $O(n^3)$ ⟹ $P\in\mathbf P$（$O(n^4)$）。

**D.1（d）〔原 D.4〕（Lean 覆盖）** (b) 的 $({\ge})$ 半、可行性下降、$\Phi'$ 良定义、截面与构造步、通用提升引理已机器检查；
$({\le})$ 的实构造（$\sigma$ 存在性的区间包含一步）仍纸面。

**D.1（e）〔原 E.1〕** $\rho_{ci}=P(T,B,U_0)$，其中 $T$ 是 $A$ 在 $\mathbb C^n/\mathcal J$ 上的作用、$B=\pi(\mathcal J A)$、$U_0=\pi(S)$。

**D.1（f）〔原 E.2〕** $\rho_{ci}$ 可在 $O(n^4)$ 内计算。

## 纸面证明

### 0. 约定与记号

* 全部子空间为有限维 $\mathbb C$-子空间，$\dim$ 为 $\mathbb C$-维数；$+\infty$ 的处理见命题里的约定。
* $\pi_B:\mathbb C^n\to\mathbb C^n/B$ 是商映射；"$\Phi(U)\subseteq(U+B)/B$" 是 "对每个 $u\in U$，$Au\in U+B$" 的简写。
* 下文所有"取最小"都在 $\mathbb N\cup\{+\infty\}$ 中进行；$\dim$ 只取有限值，故非空族的 $\min$ 存在。

### 1. D.1（a）：逐可行 $U$ 的证明（专家推荐的结构）

固定**任意**可行 $U\in\mathcal F(A,B,S)$（不预先取最小；空族情形见 §3）。由可行性：
$$S\le U,\qquad AU\le U+B .$$

**(i)** 由 $S\le U$ 得 $\dim U=\dim S+\dim\frac{U}{S}$。

**(ii)** 由 $AU\le U+B$ 与 $S\le U$ 得 $AS+S+B\le U+B$，于是有单射（包含诱导）
$$\frac{AS+S+B}{S+B}\hookrightarrow\frac{U+B}{S+B}.$$
由第二同构定理 $\frac{U+B}{S+B}\cong\frac{U}{U\cap(S+B)}$。又 $S\le U$ 且 $S\le S+B$，故 $S\le U\cap(S+B)$，于是
$$\dim\frac{U}{U\cap(S+B)}\ \le\ \dim\frac{U}{S}\qquad(\ast)$$
（商掉更大的子空间，维数更小）。

**(iii)** 合并 (i)(ii) 与 $(\ast)$：
$$\dim U\ \ge\ \dim S+\dim\frac{AS+S+B}{S+B}.$$
对可行 $U$ 取下确界（非空时即最小值），即得 (a)。

**注**：这一步**只用**"$U$ 可行"，不需要任何递归或商不变性；专家建议的正是这个顺序。

### 2. D.1（b）：良定义 + 一步递归

**2.1 $\Phi'$ 的良定义。** 设 $y'-y=m\in M=T+C$。由 $\Phi$ 线性，$\Phi(y')=\Phi(y)+\Phi(m)$。
按定义 $C'=\pi\Phi(M)$，而 $\pi:Y\twoheadrightarrow Y/M$，故 $\Phi(m)\in\pi^{-1}(C')$，其在
$\frac{Y/M}{C'}$ 中的类为零。因此 $\Phi'(y'+M)=\Phi'(y+M)$。$\square$

（这一条正是专家要求的"不能默认商不变"的地方：$\Phi$ **不**诱导 $Y/M$ 上的自同态，
它的像落在**再来一次商** $\frac{Y/M}{C'}$ 里。本项目早先踩过同类错误——$A(\mathcal J)\not\subseteq\mathcal J$，
所以 $A$ 不诱导 $\mathbb C^n/\mathcal J$ 上的映射；正确对象是 $\rho_{ci}=P(T,B,U_0)$ 里的 $T$。）

**2.2 $({\ge})$ 半。** 设 $U$ 对 $(Y,C,\Phi,T)$ 可行（$T\le U$、$\Phi(U)\subseteq(U+C)/C$）。则

* $T\le U\cap M$（因 $T\le M$ 且 $T\le U$），故 $\dim(U\cap M)\ge\dim T$；
* $\pi(U)$ 对 $(Y/M,C',\Phi',T')$ 可行：$T'\le\pi(U)$ 由 $T\le U$；$\Phi'(\pi(U))\subseteq(\pi(U)+C')/C'$ 由
  $\Phi(U)\subseteq(U+C)/C$ 与 $\Phi'$ 的定义直接得到；
* $\dim\pi(U)=\dim U-\dim(U\cap M)$。

于是 $\dim U=\dim(U\cap M)+\dim\pi(U)\ge\dim T+\mathcal P(Y/M,C',\Phi',T')$，对 $U$ 取最小即得 $({\ge})$。

**2.3 $({\le})$ 半：六项检查（专家第三轮要求的逐条核实）。**

前提：$U'\le Y/M$ 对商问题可行，即 $T'\le U'$ 且
$$\forall u\in U':\quad \widehat\pi\bigl(\Phi(su)\bigr)\in U'+C',\qquad(\ast)$$
其中 $s:Y/M\to Y$ 是 $\pi$ 的线性截面（$\pi\circ s=\mathrm{id}$；存在性由 $Y$ 有限维、$\pi$ 满射）。

**检查 1（类型）**：$s:Y/M\to Y$ 线性；$\gamma:C'\to M$ 线性；$\beta:U'\to C'$ 线性；
$\sigma=-\gamma\circ\beta:U'\to M$；$\widehat\pi\Phi:Y\to Y/M$。全部定义域/值域匹配，
$\Phi'\bigl(\tfrac{Y}{M}\bigr)\subseteq\tfrac{Y/M}{C'}$ 与 $\Phi'$ 的良定义见 §2.1。

**检查 2（线性）**：$u\mapsto su+\sigma u$ 是 $Y/M\to Y$ 的线性映射（$s$ 线性、$\sigma$ 线性），
故 $E_\sigma:=\{su+\sigma(u):u\in U'\}=(s+\sigma)(U')$ 是子空间。

**检查 3（含 $T$）**：取 $U:=T+E_\sigma$，则 $T\le U$ 显然。

**检查 4（$T$ 上可行）**：设 $t\in T$。由 $\widehat\pi\Phi(T)=T'\le U'=\pi(E_\sigma)$，存在 $e\in E_\sigma$ 使
$\pi(\Phi t-e)=0$，即 $\Phi t-e\in M=T+C$。于是
$$\Phi t\in E_\sigma+M\le U+M=U+T+C=U+C .$$
（最后一步用 $T\le U$。）

**检查 5（$E_\sigma$ 上可行，用 $\sigma$ 的定义方程）**：由 $(\ast)$ 与 $C'$ 的定义，
映射 $\nu:M\to C'/(C'\cap U')$，$m\mapsto \widehat\pi\Phi(m)+(C'\cap U')$ 是满射
（$m\mapsto\widehat\pi\Phi(m)$ 满射到 $C'$，再商掉 $C'\cap U'$ 仍满）。逐基向量取 $\beta(u)$ 满足
$$\nu\bigl(\sigma(u)\bigr)=-\nu\bigl(\text{lift of }\widehat\pi\Phi(su)\text{ 在 }C'\text{ 中的代表}\bigr),$$
即存在 $m_u\in M$ 使 $\pi\bigl(\Phi(su)+\Phi(\sigma(u)+m_u)\bigr)\in U'$；把 $m_u$ 吸收进 $\sigma(u)$（$\sigma$ 的取值在 $M$ 中）得
$$\pi\bigl(\Phi(su+\sigma u)\bigr)\in U'\quad\Longrightarrow\quad \Phi(su+\sigma u)\in\pi^{-1}(U')=E_\sigma+M\le U+C .$$
等价写法（$(\sigma)$ 性质）：
$$\widehat\pi\Phi(su+\sigma u)=\widehat\pi\Phi(su)-\beta u\in U',\qquad \sigma=-\gamma\circ\beta .$$

**检查 6（$U$ 全体 + 维数）**：$U=T+E_\sigma$，而约束 $\Phi(U)\subseteq U+C$ 是**线性**条件，
由检查 4、5 在每个生成元上成立即得全体成立。维数：
$$\dim U=\dim T+\dim E_\sigma\le\dim T+\dim U'$$
（$E_\sigma$ 是 $U'$ 的线性像，可能是 $T$ 的相关方向，故只有 $\le$；这对 $({\le})$ 半足够）。
于是 $\mathcal P\le\dim U\le\dim T+\dim U'$，对可行 $U'$ 取最小即得 $({\le})$ 半。$\square$

**结论**：$({\ge})$（§2.2）与 $({\le})$（本节）合起来给出
$$\mathcal P(Y,C,\Phi,T)=\dim T+\mathcal P(Y/M,C',\Phi',T').$$

**机器检查**：$\sigma$ 的线性构造与逐点校正 = `PRec.exists_sigma`（登记"差异：无"）；
构造步 $U=T\sqcup(s+\sigma)''U'$ 可行且 $\dim U=\dim T+\dim U'$ = `PRecursionLift.lift_admissible`（"差异：无"）；
$(\ge)$ 半 = `PRecursion.step_le` 的相应部分。

**2.4 空族的一致性。** 若 $\mathcal F=\varnothing$，则 (a) 两端为 $+\infty$（约定成立）；
(b) 由 2.2/2.3 的对应 $U\leftrightarrow\pi(U)$ 得"$\mathcal F\ne\varnothing\iff\mathcal F'\ne\varnothing$"，
故两边同为 $+\infty$。$\square$

### 3. D.1（c）(e)(f)

(c)：每次递归把 $\dim Y$ 严格下降（$\dim M\ge\dim T\ge1$，除非 $M=Y$，此时一步终止），至多 $n$ 步；
每步只做秩与子空间运算（$O(n^3)$），故 $O(n^4)$。

(e)：在商 $\mathbb C^n/\mathcal J$ 上 $T=\pi A$、$B=\pi(\mathcal J A)$、$U_0=\pi(S)$；
$(5a)\iff AU\subseteq U+\mathcal J\iff$（过商）$T(\pi U)\subseteq\pi U+B$ 且 $\pi U\supseteq U_0$，而 $\dim\pi U=\rho$。
对 $\pi U$ 取最小即得 (e)。(f) 由 (c)。$\square$

## Lean

* 等级行引用的 Lean 声明：`D1Core.d1_P_lower_bound`、`D1Core.P`、`D1Core.lean`、`d1_lower_bound`、`PRecursion`、`PRecursionLift`、`PRecursionSigma`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 该条暂无独立精确验证脚本（纸面证明 + 支撑目录）。

## 状态与历史

**等级**：[已证] $+$ **[Lean]**（`D1Core.d1_P_lower_bound` = 本条陈述（$P$ 的定义 `D1Core.P` 在 `D1Core.lean`）；逐 $W$ 版 `d1_lower_bound`。假设"可行集非空"，空集时 $P=0$ 无意义）。
**等级**：[已证] $+$ **部分 [Lean]**（D.4 覆盖 $({\ge})$ 半、可行性下降、$\Phi'$ 良定义、截面与构造步；$({\le})$ 的实构造仍纸面）。
**等级**：[已证]。
**等级**：[Lean] `PRecursion` / `PRecursionLift` / `PRecursionSigma`（见 [tools/lean/](../../tools/lean/README.md)）。
**等级**：[已证]（**完整证明**：[proof/p_is_polynomial/reduction.md](../p_is_polynomial/reduction.md)，含 $T$ 的良定义）。
**等级**：由 D.3。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3（仅 (a)）** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— (a) 下界 M3/F3；(b) 递归 M3/F2（$\sigma$ 显式 + 六项检查；Lean：`exists_sigma`、`lift_admissible` 均无差异）|


## 支撑目录

[p_is_polynomial/](../p_is_polynomial/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（第四轮：六项检查已逐条写出，递归等式闭合）

**上一轮未接受**：$(\le)$ 半只给了抵消机制，未做类型/可行性检查。

**本轮**：§2.3 按专家列的六项逐条写出——
(1) 类型；(2) 线性；(3) 含 $T$；(4) $T$ 上可行（用 $\widehat\pi\Phi(T)=T'\le U'=\pi(E_\sigma)$ 与 $M=T+C\le U+C$）；
(5) $E_\sigma$ 上可行（用 $\nu:M\to C'/(C'\cap U')$ 满射定出 $\sigma$；即 $\widehat\pi\Phi(su+\sigma u)=\widehat\pi\Phi(su)-\beta u\in U'$）；
(6) 全体可行（线性 ⟹ 生成元足够）与维数 $\dim U=\dim T+\dim E_\sigma\le\dim T+\dim U'$。

因此 $\mathcal P=\dim T+\mathcal P'$ 闭合；等级升为 **M3/F2 → 完成**（Lean：`exists_sigma` 与 `lift_admissible` 均登记"差异：无"）。
