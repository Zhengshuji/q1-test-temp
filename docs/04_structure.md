# 04 · 结构定理（严谨部分）

> 只写**已证**的结构。经验性/统计性的图景**不在**本文件（在 `workspace/q1_false/notes_data_shapes.md`）。
> 凡与此矛盾的旧公式都已在 [proof/refuted/](../proof/refuted/README.md)。

---

## 4.1 主分解（定义性）

对任何解 $\mathcal L$，令 $\mathcal V=\operatorname{row}\mathcal L$、$\rho=\dim\pi(\mathcal V)$、$c=\dim(\mathcal V\cap\mathcal J)$。由 A.1（[docs/02](02_theorems_proven.md)）：
$$q=\rho+c .$$
于是
$$q_{\min}=\min_{(\rho,c)\in\mathcal R}(\rho+c),\qquad
\mathcal R:=\{(\rho(\mathcal V),\,c(\mathcal V)):\ \mathcal V\supseteq S,\ (5a)\wedge(5b)\}.$$

这是**定义性**的分解：它没有断言 $\mathcal R$ 有闭式（事实上有四个候选闭式被推翻，见 `proof/refuted/`）。

---

## 4.2 $\rho$ 一侧 = $P$（已解决）

**引理 4.2.1** $(5a)\iff U:=\pi(\mathcal V)$ 满足 $T(U)\subseteq U+B$ 且 $U\supseteq U_0$，其中 $T$ 是 $A$ 在 $\mathbb C^n/\mathcal J$ 上的诱导作用、$B=\pi(\mathcal J A)$、$U_0=\pi(S)$。
*证明*：$(5a)$ 即 $\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}(\mathcal L)+\mathcal J$；对 $\mathcal J$ 取商得 $\pi(\mathcal LA)\subseteq\pi(\mathcal V)=U$，而 $\pi(\mathcal LA)$ 与 $T(U)$ 相差 $\pi(\mathcal J A)=B$。$\square$

**推论 4.2.2** $\rho_{ci}:=P(T,B,U_0)=\min\{\dim U:\ U\supseteq U_0,\ T(U)\subseteq U+B\}$ 只由 $(5a)$ 决定，且**可算**：由 [proof/p_is_polynomial/](../proof/p_is_polynomial/README.md) 的递归定理，$O(n^4)$。

$$\boxed{\ \text{算术侧}:\ \rho\ \text{在}\ (5a)\ \text{下的最小可行值}=\rho_{ci}=P(T,B,U_0)\ \text{已多项式}\ }$$

---

## 4.3 $c$ 一侧与可达性（开放）

由 A.2：$c\ge\max(c_0,1)$，但 $c$ 可以严格更大（[proof/refuted/](../proof/refuted/README.md) R4：$c_0=1$、真值 $c=2$）。所以 $\mathcal R$ 不能由 $c_0$ 决定。

**已证的层结论**

| 层 | 结论 | 等级 |
|---|---|---|
| $\rho=0$ | $\mathcal V\subseteq\mathcal J$；$(5a)\iff S\subseteq\mathcal J,\ SA\subseteq\mathcal J$；$(5b)$ 自动；$q_{\min}=r$ | [已证]（B.3）|
| $\rho=d$（顶层）| $(5b)\iff(D_W^{\mathsf T},T_W)$ 可观测 | [已证]（B.2）|
| $\mathcal V=\mathbb C^n$ | 可行 $\iff$ $A^{\mathsf T}$ 无特征向量落在 $K$ | [已证]（B.4）|

**未证**：$0<\rho<d$ 的一般层没有已证判据。这正是 [docs/05](05_open_questions.md) Q1。

> $(2,1)$ 层（$\rho=2,c=1$）：刻画是"铅笔的三个 $2\times2$ 子式无公根"（[已证]）；子式对 $(\lambda,\tau)$ 的次数都 $\le2$（[已证]），"存在公根"的 $\tau$ 集是闭集（[已证]）⟹ 该层判定**可判定**；且当 $w=\beta(h)\ne0$ 时，$\tau$ 量词被**线性代数**解决（坏集是仿射子空间，[proof/rho1_layer/theorem.md](../proof/rho1_layer/theorem.md) 定理 9.10）；剩的是对 $(\mathcal U,\mathcal H)$ 的量词；$w=0$ 时该 $(\mathcal U,\mathcal H)$ **恒不可行**（定理 9.12）；且需要 一个模 $B$ 的特征方向（定理 11.1-更正版；随机 216 例 0 命中 ⟹ 该层稀有）。但该条件**不充分**（猜想 11.4 已否，§12）。
> 早先试图经"可控性"判定的路线**已否决**（[docs/05](05_open_questions.md) Q5）：$\beta(\mathcal H)\subseteq B$ 恒成立，输入算子为零。

---

## 4.4 与 $q1$ 的关系

$$q1\ \text{的复杂度}=\text{"判定 }(\rho,c)\in\mathcal R\ \text{是否成立"的复杂度}$$

- 若该判定多项式 ⟹ $q_{\min}$ 多项式 ⟹ **$q1$ = 假**；
- 若该判定 $\exists\mathbb R$-hard ⟹ **$q1$ 强 hard**。

$q_{\min}$ 是整数且 $0\le q_{\min}\le n$，所以"计算 $q_{\min}$"与"判定 $q_{\min}\le k$"等价。

> **$(k,1)$ 的结构**（[proof/rho1_layer/theorem.md](../proof/rho1_layer/theorem.md) §14，纯证明）：
> $(5b)$ 失败 $\iff\exists$ 一个 $\dim\le k-1$、含 $w$ 的子空间 $W_0$ 装下所有行。
> $k=2$ 时 $W_0=\langle w\rangle$ **唯一** ⟹ 坏集仿射（这就是 $(2,1)$ 能用线性代数的原因）；
> $k\ge3$ 时 $W_0=\langle w,x\rangle$ 多一个射影参数 ⟹ 坏集是一族仿射集的并，判定多一层量词。

> **一般 $(\rho,c)$ 的判据**（[proof/rho1_layer/theorem.md](../proof/rho1_layer/theorem.md) §21，纯证明）：
> 允许的容器 $W_0$ 唯一 $\iff\dim\beta(\mathcal H)=\rho-1$；此时坏集仿射、包含于 $\mathcal A$，
> 层判定 = **维数比较**。所以 $(2,1)$ 与 $(3,2)$ 这类层是**线性可判**的（$\mathcal H$ 可选）。

## 4.5 退化与边界情形（论文"Degenerate and boundary cases"一节的底稿）
|---|---|
| $K=\ker[C;CA]=0$ | $\operatorname{rank}[C;CA]=n$，故 $Q_{\mathcal L}(\lambda)$ 含秩 $n$ 的行块 ⟹ $\operatorname{rank}Q_{\mathcal L}(\lambda)=n$ 对一切 $\lambda$ ⟹ **$(5b)$ 自动成立** | 单列命题；并注意 $\mathbb P(K)=\varnothing$，B.13 的覆盖判据空洞 |
| $V=0$ | 则 $\mathcal L=0$、$C=0$，$Q_{\mathcal L}\equiv0$、$h=0$；$(5a)$ 与 $(5b)$ 都成立 | 单列平凡情形（涉及 $\mathbb P(V)$、$\mathbb P(W)$ 的语句需先排除）|
| $\operatorname{rank}\mathcal L<q$ | $\mathcal L$ 有冗余行；结构公式必须用 $\operatorname{rank}\mathcal L$ 而非 $q$ | 保留在一般定理里；特别注意 $d_\infty=h-\operatorname{rank}\mathcal L$（**不是** $h-q$）|
| $L_0=0$ | B.9 的严格不等式在 $L_0\ne0$ 下证；固定行约束消失，可能允许更简单的增广 | 单列特殊族，不套用一般下界 |

#### 4.5.45.2 需要补充的（专家第五轮 §5.2）

| 情形 | 后果 | 处理 |
|---|---|---|
| $V_0=V\cap K=0$ | $W_K=\mathcal LV_0=0$ ⟹ 无部分特征向量 ⟹ **$(5b)$ 成立** | 推论（比 $W_K=0$ 更易验证）|
| $W_K=\mathcal LK=0$ | 同上：无 $0\ne w\in W_K$ ⟹ **$(5b)$ 成立** | 推论（由 B.24 的判据直接得到）|
| $S=V\cap\ker\mathcal L=0$ | $\mathcal L|_V$ 单射 ⟹ $\dim W_0=\dim V_0$；**不**由此推出 $W=W_0$（需 $V_0=V$）| 单列"最干净"情形；不要混同 $W$ 与 $W_0$ |
| $\rho=0$ | 零商层（B.3）：$\mathcal V\subseteq\mathcal J$，$(5b)$ 自动 | 单列层；注意 $\rho$ 与 $\dim W_K$ 是**两个不同的量**，建议用 $\rho_W$ 与 $\omega:=\dim W_K$ 两个符号 |
| $q=0$ | 空增广（仅当 $r=0$ 时可能）| 边界情形，定义要覆盖空矩阵 |
| $h=0$ | 零铅笔；法秩与"零阶子式的 gcd"约定要显式给出 | 直接处理，不套用正秩的行列式因子定理 |
| $\mathbb P(K)$ 或 $\mathbb P(V)$ 为空 | B.13 的维数论证不适用 | 先设正维假设，再补空空间情形 |
| 无穷谱参数 | $(5b)$ 只对**有限** $\lambda$ 量化，**不**要求无穷远处满秩 | 必须区分"有限秩降的避免"与"含无穷远的射影秩保持"——后者是更强的条件，$(5b)$ 不要求它 |

#### 4.5.45.3 两条可以立刻写成推论的

**推论 1（$K=0$）** 若 $\ker[C;CA]=0$，则 $(5b)$ 自动成立（对任意 $\mathcal L$）。
*证明*：$\operatorname{rank}[C;CA]=n$ ⟹ $Q_{\mathcal L}(\lambda)$ 的 $CA,C$ 行块已秩 $n$（列数 $n$）⟹ 满列秩。

**推论 2（$W_K=0$）** 若 $\mathcal L\ker[C;CA]=0$，则 $(5b)$ 成立。
*证明*：由 B.24 的判据 $(5b)$ 失败 $\iff\exists0\ne w\in W_K:\Phi_K(w)\in\mathbb Cw$；$W_K=0$ 时不存在这样的 $w$。$\square$
（注意：$W_K=0$ **不**等价于 $V_0=0$；$V_0=S$ 时也成立。）

### 4.5.4 写论文时的顺序建议

1. 先给**一般情形**（$K\ne0$、$V\ne0$、$\operatorname{rank}\mathcal L$ 任意、$L_0\ne0$、$h>0$），
   并全程用 $\operatorname{rank}\mathcal L$ 与 $\dim W_K$；
2. 再给上面两条推论；
3. 最后列"空射影空间 / $q=0$ / $h=0$ / 无穷远"四条**约定性**处理；
4. 明确写出：$(5b)$ 不要求无穷远处满秩（B.6 会给出无穷初等因子）。

### 4.5.5 与项目内已有结果的对齐

* B.6 的 $d_\infty=h-\operatorname{rank}\mathcal L$、右最小指标全零——这些**只在 $(5a)$ 下**成立，写进一般情形；
* B.9 的严格不等式需要 $L_0\ne0$——写进"$L_0=0$ 的情形"；
* B.13 的覆盖判据需要 $\mathbb P(K)\ne\varnothing$ 与 $\mathcal B=\varnothing$——写进其自身条目，不在一般定理里。
