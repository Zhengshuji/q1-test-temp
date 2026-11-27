# $\rho=d_0{+}1$ 层（首个中间层）：精确陈述与证明现状

> 对应 [docs/04](../../../../../docs/04_structure.md) §4.3 的那一行、[docs/05](../../../../../docs/05_open_questions.md) Q1/Q5。
> **2026-10-27 更正（重要）**：本文原先走"可控性"桥（Q5），而 **Q5 已被否决**——
> $\beta(\mathcal H)\subseteq B$ 恒成立，放到 $(\mathcal U+B)/B$ 上输入恒为零（见 [../controllability_equivalence/theorem.md](../../../../../proof/controllability_equivalence/theorem.md) §8）。
> 因此 **定理 4.1 撤回**，本文件保留作"失败路线的记录"，正确的路线见 §9。

## 1. 精确定设（约化坐标）

沿用 [docs/01](../../../../../docs/01_notation.md) 与 [proof/p_is_polynomial/reduction.md](../../../../../proof/p_is_polynomial/reduction.md)：
$X=\mathbb C^n/\mathcal J$、$B=\pi(\mathcal J A)\subseteq X$、$T:X\to X/B$、$U_0=\pi(S)$。

任何解由三元组 $(\mathcal U,\mathcal H,\tau)$ 给出：
$$\mathcal V=(s+\tau)(\mathcal U)\oplus\mathcal H,\qquad \mathcal U\subseteq X\ (\dim\rho),\quad \mathcal H\subseteq\mathcal J\ (\dim c),\quad \tau:\mathcal U\to\mathcal J ,$$
其中 $s:\mathcal U\to\mathbb C^n$ 是截面。两个条件化为
$$(5a)\iff \beta(\mathcal H)\subseteq\mathcal U\ \text{且}\ T(\mathcal U)\subseteq\mathcal U+B,\qquad
(5b)\iff (S_\tau,\ \beta|_{\mathcal H})\ \text{可控},$$
$S_\tau:=(T+\beta\tau)|_{\mathcal U}:\mathcal U\to\mathcal U$（模 $B$）。

> 第二条（$(5b)\iff$ 可控）**已否决**（见 [proof/controllability_equivalence/](../../../../../proof/controllability_equivalence/theorem.md) §8）。**本文以下沿用它只是历史记录；正确路线见 §9。**
> 本文的定理 4.1 会把它作为显式假设。

## 2. 本层的特化：$\rho=2$、$c=1$

设 $\dim\mathcal U=2$、$\mathcal H=\langle h\rangle$、$b:=\beta(h)\in X$（即 $\beta|_{\mathcal H}$ 的像，单个向量）。于是
$$(S_\tau,\beta|_{\mathcal H})\ \text{可控}\iff \operatorname{span}\{b,\ S_\tau b\}=\mathcal U\iff \det[b;\ S_\tau b]\ne0 .$$

**引理 2.1**（$\dim\mathcal U=2$、单输入）$(S_\tau,b)$ 可控 $\iff\det[b;S_\tau b]\ne0$。
*证明*：Krylov 判据：$\dim\mathcal U=2$ 时可控 $\iff\{b,S_\tau b\}$ 线性无关 $\iff$ 以它们为行的 $2\times2$ 矩阵行列式非零。$\square$

**引理 2.2**（$\tau$ 的线性性）把 $\tau$ 看作 $\dim\mathcal U\cdot\dim\mathcal J$ 个自由参数，则
$$\tau\longmapsto\det[b;\ S_\tau b]$$
是 $\tau$ 的**一次**函数（不是二次的）。
*证明*：$S_\tau=T+\beta\tau$ 关于 $\tau$ 仿射（线性项 $\beta\tau$ + 常数 $T$）；$S_\tau b=Tb+\beta(\tau b)$ 关于 $\tau$ 仿射；二阶行列式 $\det[b;\,\cdot\,]$ 关于第二个变量**线性**。故复合是一次函数。$\square$

> **更正**：本目录早先写成"二次型"——那是不对的，$\tau$ 只出现一次（$b$ 与 $\tau$ 无关）。这不影响可判定性（线性更简单），但影响"如何求见证"：线性情形下**非恒零之点可直接解出**，不需要解二次方程。

## 3. 可容许集是仿射空间

固定 $(\mathcal U,\mathcal H)$，把 $(5a)$ 与"$s$ 的相容性"写成 $\tau$ 的线性方程（与 [c192](../../../../../tools/layer_search/c192_reduced_search.py) 的 (A)(B) 两式一致）：

- **(A)** 对每个 $q\in\mathcal U^\perp$：$\langle q,T(u_i)\rangle+\sum_k\tau_{ik}\langle q,\beta(J_k)\rangle=0$；
- **(B)** 对每个 $s\in S$、每个 $q\in\mathcal H^\perp$：$\langle q,\mathrm{jcomp}(s)\rangle-\sum_i\mathrm{co}_i(s)\langle q,\tau_i\rangle=0$。

**引理 3.1** 上述方程组的解集 $\mathcal A(\mathcal U,\mathcal H)\subseteq\mathbb C^{\dim\mathcal U\cdot j}$ 是**仿射子空间**（可能为空）。
*证明*：方程关于 $\tau$ 是线性的（系数只依赖 $A,C,\mathcal U,\mathcal H$）。$\square$

## 4. 主定理（条件性）——**已撤回**（依赖的 Q5 已被否决）

**定理 4.1**（假设 Q5）固定 $(\mathcal U,\mathcal H)$，$\dim\mathcal U=2$、$\dim\mathcal H=1$。则该 $(\mathcal U,\mathcal H)$ 能被补成可行解 $\iff$
$$\mathcal A(\mathcal U,\mathcal H)\ne\varnothing\quad\text{且}\quad \det[b;S_\tau b]\not\equiv0\ \text{在}\ \mathcal A(\mathcal U,\mathcal H)\ \text{上}.$$
且此判定是多项式的：$\mathcal A$ 由线性方程组给出，$\det[b;S_\tau b]$ 是 $\tau$ 的一次函数，故
$$\exists\tau\in\mathcal A:\ \det[b;S_\tau b]\ne0\iff \text{该一次函数在 }\mathcal A\text{ 的方向空间上不恒为零},$$
一次函数在仿射空间上是否恒零，一次线性代数即可判定（把方向空间的一组基代入即可）。

*证明*：$(\Rightarrow)$ 若 $(\mathcal U,\mathcal H)$ 可补成解，则存在 $\tau\in\mathcal A$ 使 $(5b)$ 成立；由 Q5 得 $(S_\tau,b)$ 可控；由引理 2.1 得 $\det[b;S_\tau b]\ne0$。
$(\Leftarrow)$ 若 $\mathcal A\ne\varnothing$ 且存在 $\tau\in\mathcal A$ 使 $\det\ne0$，则由引理 2.1，$(S_\tau,b)$ 可控，再由 Q5 得 $(5b)$ ✓；而 $\tau\in\mathcal A$ 保证 $(5a)$ ✓。$\square$

**推论 4.2** 在 $(2,1)$ 层上，层可行性是一个**线性代数问题**，$O(d^3)$ 级；无需搜索、无需解二次方程。

## 5. 现状与缺口（诚实；§4 已撤回）

| 项 | 状态 |
|---|---|
| 引理 2.1（$2\times2$ 可控判据）| [已证] |
| 引理 2.2（$\tau$ 的一次性）| [已证]（并**更正**了早先"二次型"的说法）|
| 引理 3.1（可容许集仿射）| [已证] |
| 定理 4.1 | **[已证·条件性]**：依赖 **Q5**（未证）|
| Q5 本身 | [精确验证 16276/16276]，无证明；见 [docs/05](../../../../../docs/05_open_questions.md) Q5 |
| 数值 | `c192` 的 46/47（$\mathbb F_5$、$n{=}5$、$\rho=2$）：0 误报、1 漏报——漏报是 $c=2$ 形状，超出本文的 $(2,1)$ 设定 |

**所以本层的"完整证明"缺的只有一块：Q5。**

> 2026-10-27 更新：Q5 已在 $B\subseteq\mathcal U$ 情形证明（[proof/controllability_equivalence/](../../../../../proof/controllability_equivalence/theorem.md) 推论 3.2），
> 一般情形只剩一个附加条件。因此本定理在 $B\subseteq\mathcal U$ 时是**无条件**定理。 一旦 Q5 成立，$(2,1)$ 层就彻底解决；$(2,1)$ 的论证模板可原样推广到 $(\rho,c)=(k,1)$：只需把引理 2.1 换成 $k\times k$ 的 Krylov 行列式（仍是 $\tau$ 的一次函数，因为只有最后一列含 $\tau$）。

## 6. 与主线的关系

若对每个 $\rho$ 层都能证明"可行性 $=$ 某线性/多项式函数在仿射空间上非恒零"，则层判定多项式 ⟹ $q1$ = 假。
本文把 $(\rho,c)=(2,1)$ 做到了**只差 Q5**；$(k,1)$ 的推广是同一模板（Krylov 行列式取代 $2\times2$ 行列式）。

## 7. 复核

- 穷举对照：`python tools/layer_search/c192_reduced_search.py --n 5 --k 2`（枚举全部 $\rho=2$ 子空间）；
- 定量实验：`python tools/layer_search/c194_layer2.py`；
- 本文的判据**尚未**写成自包含 `verify.py`（需要把 $\mathcal A(\mathcal U,\mathcal H)$ 的解与一次函数的不恒零检查单独实现）——记在 [docs/05](../../../../../docs/05_open_questions.md) 的待办里。

## 9. 更正后的路线（不依赖 Q5）

### 9.1 每行的形状

取 $\mathcal U$ 的基 $u_1,u_2$、$H=\langle h\rangle$，$\tau=(\tau_1,\tau_2)$（$\tau_i\in\mathbb C^{j}$ 是 $\tau(u_i)$ 的 $\mathcal J$-坐标）。由 §1/§2：
$$Q_{\mathcal V}(\lambda)=\begin{pmatrix}\lambda u_1-r_1(\tau)\\ \lambda u_2-r_2(\tau)\\ -\beta(h)\end{pmatrix},\qquad r_i(\tau)=\widetilde T(u_i)+\beta(\tau_i),$$
即：**每个元素对 $(\lambda,\tau)$ 仿射**；第三行**不含 $\tau$**。

### 9.2 引理（次数界）

记 $p_{12},p_{13},p_{23}$ 为 $Q_{\mathcal V}$ 的三个 $2\times2$ 子式（取列 $\{a,b\}$ 时记作 $p_{ij}^{ab}$）。则

1. 每个子式对 $\lambda$ 的次数 $\le2$（$2\times2$ 行列式、元素对 $\lambda$ 仿射）；
2. 每个子式对 $\tau$ 的次数 $\le2$（元素对 $\tau$ 仿射，行列式是双线性的）；
3. **含第三行的子式（$p_{13},p_{23}$）对 $\tau$ 线性**（第三行与 $\tau$ 无关）。

*证明*：行列式是元素的乘法多项式，次数相加。$\square$

**推论 9.3** 参数个数为 $2j$，故每个子式的系数总数 $\le 3\times\binom{2j+2}{2}=O(j^2)$——**多项式规模**，可显式写出。

### 9.4 (5b) 的精确形式（本层）

$$(5b)\iff \operatorname{rank}Q_{\mathcal V}(\lambda)=2\ \ \forall\lambda\iff p_{12},p_{13},p_{23}\ \text{在}\ \mathbb C[\lambda]\ \text{中无公共根}.$$

**引理 9.5**（坏集是闭集）在 $\tau$-参数空间里，
$$\mathfrak B:=\{(\tau,\lambda):\ p_{12}(\tau,\lambda)=p_{13}(\tau,\lambda)=p_{23}(\tau,\lambda)=0\}$$
是闭集，故它的投影 $\pi_\tau(\mathfrak B)$（"存在公共根的 $\tau$"）也是闭集（消去单变量 $\lambda$）。

*证明*：三个方程在 $(\tau,\lambda)$ 空间里闭；投影到 $\tau$ 是消去一个变量，闭集投影仍闭（消元定理 / 结式的零点集）。$\square$

**推论 9.6** 于是"$(5b)$ 在可容许集 $\mathcal A$ 上可满足" $\iff$ $\mathcal A\not\subseteq\pi_\tau(\mathfrak B)$——一个**可判定**的代数问题（但复杂度未定，见 §9.6）。

### 9.5 可立即使用的充分判据（$O(j^3)$，无消元）

取任一 $\tau\in\mathcal A$（若 $\mathcal A=\varnothing$ 则该 $(\mathcal U,\mathcal H)$ 直接不可用），算 $\operatorname{Res}_\lambda(p_{12},p_{13})$；若 $\ne0$ 则 $p_{12},p_{13}$ 互素，进而三者互素 ⟹ $(5b)$ ✓。

> 这正是 46/47 里"**0 误报**"的那一侧：判据说可行就一定可行。漏报来自"两两结式为零但三者仍互素"的情形。

### 9.6 失败条件的正确形状（抱歉：先前的 $\varphi$-写法是错的）

> **自我更正（同日）**：我一度写成"$(5b)$ 失败 $\iff\exists\varphi$ 灭掉三行"。那是**错**的：
> 一个左零向量只给出 $\operatorname{rank}\le d-1$，而本层要求的是 $\operatorname{rank}\le1$。下面是正确的形状。

固定 $\tau$ 与 $\lambda$。$\operatorname{rank}Q_{\mathcal V}(\lambda)\le1\iff$ $Q_{\mathcal V}(\lambda)$ 的**全部** $2\times2$ 子式为零。

由 §9.1 的三行形状，对每对列 $\{a,b\}$：
$$p_{12}^{ab}(\tau,\lambda)\ \text{（对 }\tau\ \textbf{二次}）、\qquad
p_{13}^{ab}(\tau,\lambda),\ p_{23}^{ab}(\tau,\lambda)\ \text{（对 }\tau\ \textbf{线性}）.$$

**引理 9.7（正确版）** $(5b)$ 失败 $\iff\exists\lambda\in\mathbb C$ 使方程组
$$\big\{\,p_{ij}^{ab}(\tau,\lambda)=0:\ i<j,\ a<b\,\big\}\tag{$\dagger$}$$
有解 $\tau$（且 $\tau\in\mathcal A$）。对固定 $\lambda$，$(\dagger)$ 是 $\tau$ 的**二次方程组**（其中一部分是线性的）。

*证明*：$\operatorname{rank}\le1\iff$ 全部 $2\times2$ 子式为零；每个子式是 $\tau$ 的多项式，$\lambda$ 是参数。$\square$

**为什么这仍然落在 $\exists\mathbb R$ 里**：$(\dagger)$ 是"二次方程组 + 参数 $\lambda$"，而 $\lambda$ 还要满足 $\tau\in\mathcal A$（仿射）。所以
$$\text{层可行}\iff \forall\lambda:\ \mathcal A\ \text{与}\ \{\tau:(\dagger)\}\ \text{不相交}.$$
"仿射集与二次簇相交"正是 $\exists\mathbb R$ 的典型输入。**注意**：$p_{13},p_{23}$ 是线性的，它们已经把 $\tau$ 约束到仿射集上；剩下的 $p_{12}$（二次）在这个仿射集上变成二次型——于是本层最终等价于

$$\boxed{\ \text{在仿射集}\ \mathcal A_\lambda\ \text{上，"某个二次型是否恒为零"（}\forall\lambda\text{ 的合取）}\ }$$

也就是**一族（$\lambda$ 连续的）二次型恒零问题**——不是单个二次型，所以不能直接套用"线性代数判零"。

### 9.7 尝试证明"多项式可判" —— 卡在哪

想把它变成多项式算法，自然的路是：对每个 $\lambda$ 判定"$\mathcal A_\lambda$ 与二次簇是否相交"，然后说明**只需取有限多个 $\lambda$**（例如由 $\operatorname{Res}(p_{12},p_{13})$ 的零点给出）。这条路的障碍是：

1. **$\lambda$ 的候选集依赖 $\tau$**：$\operatorname{Res}_\lambda(p_{12},p_{13})$ 本身是 $\tau$ 的多项式，它为零的 $\lambda$ 或 $\tau$ 会随 $\tau$ 变 ⟹ 不能先固定 $\lambda$ 再解 $\tau$；
2. 即便能，问题变成"在仿射集上判定二次型恒零"——这**是**线性的（求二次型的系数即可），但前提是先固定 $\lambda$ 与线性层；
3. 于是真正的障碍是**$\exists\lambda$ 与 $\exists\tau$ 的交替**：$\exists\tau\ \forall\lambda$（"每个 $\lambda$ 处秩都为 2"）。$\forall\lambda$ 可以被消除（因为 $\lambda$ 只有一维、次数 $\le2$：只需检查有限个候选 $\lambda$，即 $p_{13},p_{23}$ 的根与 $p_{12}$ 的根），但候选集**依赖 $\tau$**。

所以卡点精确地是：**$\lambda$ 的候选集是 $\tau$ 的代数函数**。这正是一大类 $\exists\mathbb R$-完全问题的特征（例如"是否存在 $x$ 使二次方程组在实数域有解"）。

**诚实结论**：本文**没有**证出本层的多项式可判；我只证到
$$\text{本层判定}\ \in\ \exists\mathbb R\ \text{型（可判定，Tarski–Seidenberg）},\qquad \text{多项式性未知}.$$

### 9.8 那么它为什么仍然"可判定"？

因为 $\lambda$ 只有一维、每层维数固定：对固定的 $(\rho,c)$，层的判定可以写成**量词消去**后的实代数问题（Tarski–Seidenberg），故**可判定**（复杂度是双指数的）。所以本层的逻辑状态是：

| 说法 | 状态 |
|---|---|
| 该层判定可判定 | [已证]（$\lambda$ 一维 + 有限维实代数）|
| 该层判定多项式 | **未证**，且 9.7 表明需要新的想法 |
| 该层判定 $\exists\mathbb R$-hard | **未证**（若证成，$q1$ 强 hard）|

### 9.9 给主线的启示

$(2,1)$ 是**最小的中间层**，而它已经退化成双线性可行性。这与"四个闭式被推翻、拟阵/TAP 归约失败"是同一件事的两面：

$$q1\ \text{的困难不是组合性的，而是}\ \exists\mathbb R\ \text{型的代数可行性}\!$$

若这个判断成立，$q1$ 的答案更可能是 **$\exists\mathbb R$-hard（强 hard）** 而不是 NP-hard，也不是"多项式"。这正是 [docs/05](../../../../../docs/05_open_questions.md) Q1 里说的第二种结局。

> **下一步（真正能推进主线的）**：把 $(\star)$ 的双线性系统作为一个**显式的 $\exists\mathbb R$ 实例族**写出来，尝试与已知 $\exists\mathbb R$-完全问题（如二次方程组可行性、copositivity、Pfaffian）建立归约——这与项目早先"三个降落点"里的第三个（$k=2$ 的 $\operatorname{Pf}$）直接对接。

### 9.6 还没做的（下一步）

1. 把 $\pi_\tau(\mathfrak B)$ 的**定义方程**写出来（$\deg_\lambda\le2$ 时可用系数矩阵 $M(\tau)$ 的行列式与核向量条件显式表达，次数 $\le6$）；
2. 判定 $\mathcal A\subseteq\pi_\tau(\mathfrak B)$——即在仿射集上判定一组多项式方程是否全被满足（这是**线性/二次**规模的问题，但没有通用多项式算法，需按 $j$ 的具体结构处理）。
3. 若第 2 步对一般 $(\rho,c)$ 能做成多项式算法 ⟹ $q1$ = 假；若做不成 ⟹ 它就是个 $\exists\mathbb R$-型问题，正是 $q1$ 的真难度所在。

### 9.10 ⭐ 定理（$w\ne0$ 时 $\tau$-量词被线性代数解决）

设 $\rho=2$、$c=1$、$H=\langle h\rangle$、$w:=\beta(h)\ne0$，并固定 $(\mathcal U,\mathcal H)$，$\mathcal A\subseteq\mathbb C^{2j}$ 为可容许 $\tau$ 的仿射集。则

1. 对任意 $\tau$：$(5b)$ 失败 $\iff\exists\lambda$ 使 $\lambda u_i-r_i(\tau)\in\langle w\rangle$（$i=1,2$）；
2. $\mathfrak S:=\{(\tau,\lambda):\ \lambda u_i-r_i(\tau)\in\langle w\rangle\ (i=1,2)\}$ 是 $\mathbb C^{2j}\times\mathbb C$ 里的**仿射子空间**；
3. 故 $\mathrm{Bad}:=\pi_\tau(\mathfrak S)$ 是 $\tau$-空间里的**仿射子空间**；
4. 于是该 $(\mathcal U,\mathcal H)$ 可补成解 $\iff\mathcal A\not\subseteq\mathrm{Bad}$ —— **两个仿射子空间的包含判定**，$O((2j+d)^3)$。

*证明*：
(1) $\operatorname{rank}Q_{\mathcal V}(\lambda)\le1\iff$ 三行两两成比例。第三行 $=-w\ne0$，故"成比例"迫使前两行都在 $\langle w\rangle$ 里；反之显然。$\square$
(2) 条件 $x\in\langle w\rangle$（$w\ne0$）$\iff x_aw_b-x_bw_a=0$ 对一切 $a<b$——对 $x$ **线性**；而 $x=\lambda u_i-r_i(\tau)$ 对 $(\lambda,\tau)$ **联合仿射**（$r_i$ 对 $\tau$ 仿射、$\lambda$ 只乘常向量 $u_i$）。$\square$
(3) 仿射子空间的线性投影仍是仿射子空间。$\square$
(4) $\mathcal A,\mathrm{Bad}$ 都仿射，取 $\tau_0\in\mathcal A$：$\mathcal A\subseteq\mathrm{Bad}\iff\tau_0\in\mathrm{Bad}$ 且 $\operatorname{dir}\mathcal A\subseteq\operatorname{dir}\mathrm{Bad}$（两个线性方程组的包含），是线性代数。$\square$

**为什么这重要**：§9.7 说"障碍是 $(\lambda,\tau)$ 的双线性"。定理 9.10 表明：**只要 $w\ne0$，这个双线性不存在**——$\lambda$ 与 $\tau$ 的方程是**联合仿射**的，于是"存在公共根"这件事变成了一次投影，直接是线性代数。

**边界（关键）**：$w=0$（即 $hA\in\mathcal J$）时第三行消失，"前两行成比例"的子式对 $(\lambda,\tau)$ 是**二次**的，定理 9.10 不再成立——**§9.6/9.7 的双线性障碍恰好只在 $w=0$ 时出现**。

### 9.11 还剩什么（诚实的范围）

定理 9.10 解决的是**固定 $(\mathcal U,\mathcal H)$ 时关于 $\tau$ 的量词**。层的完整判定还要对 $\mathcal U\in\mathrm{Gr}(2,d)$、$\mathcal H\in\mathrm{Gr}(1,j)$ 量词：

$$\text{层可行}\iff\exists(\mathcal U,\mathcal H):\ (5a)\ \wedge\ \big[\mathcal A_{\mathcal U,\mathcal H}\not\subseteq\mathrm{Bad}_{\mathcal U,\mathcal H}\big].$$

- 第一个量词下的 $(5a)$ 部分正是 $P$ 的形状（已多项式，[proof/p_is_polynomial/](../../../../../proof/p_is_polynomial/README.md)）；
- 第二个（括号里的）是关于 $(\mathcal U,\mathcal H)$ 的**代数条件**（定理 9.10 已把它化简为"仿射不包含"）；
- 所以剩下的问题是：**在 Grassmannian 上找一个满足 $(5a)$ 且满足一个代数条件的点**。这仍是 $\exists$-型，但**双线性障碍已经消失**（仅在 $w=0$ 的子情形残留）。

**下一步**：对 $d$ 小（$d\le4$）时把 $(\mathcal U,\mathcal H)$ 也用 Grassmann 坐标参数化，写出"$\mathcal A\not\subseteq\mathrm{Bad}$"的多项式条件（次数已知 $\le2$），然后在 Grassmannian 上判定——这是 Q1 的**具体的、次数有界**的版本。

### 9.12 ⭐ 定理（$w=0$ 时该 $\tau$ 层**恒不可行**）

设 $\rho=2$, $c=1$, $H=\langle h\rangle$ 且 $w=\beta(h)=0$（即 $hA\in\mathcal J$）。则对**任何**满足 $(5a)$ 的 $\tau$，$(5b)$ 都失败。

*证明*：由 $(5a)$ 的必要条件 $\beta(\mathcal H)\subseteq\mathcal U$ 与 $T(\mathcal U)\subseteq\mathcal U+B$，可容许的 $\tau$ 满足
$$r_i(\tau)=\widetilde T(u_i)+\beta(\tau_i)\in\mathcal U=\langle u_1,u_2\rangle\qquad(i=1,2).$$
写成坐标 $r_1=a_1u_1+b_1u_2$、$r_2=a_2u_1+b_2u_2$。$w=0$ 使第三行为零，故
$$Q_{\mathcal V}(\lambda)=\begin{pmatrix}\lambda u_1-r_1\\ \lambda u_2-r_2\\ 0\end{pmatrix},\qquad
\operatorname{rank}Q_{\mathcal V}(\lambda)\le1\iff (\lambda u_1-r_1)\parallel(\lambda u_2-r_2).$$
在基 $(u_1,u_2)$ 下 $\lambda u_1-r_1=(\lambda-a_1,\,-b_1)$、$\lambda u_2-r_2=(-a_2,\,\lambda-b_2)$，故
$$\text{成比例}\iff \det\begin{pmatrix}\lambda-a_1 & -b_1\\ -a_2 & \lambda-b_2\end{pmatrix}=0
\iff \lambda^2-(a_1+b_2)\lambda+(a_1b_2-a_2b_1)=0 .$$
这是**首项系数为 1 的二次方程**，在 $\mathbb C$ 上**必有根**。取该根 $\lambda_0$，则 $\operatorname{rank}Q_{\mathcal V}(\lambda_0)\le1<2=\rho$，即 $(5b)$ 失败。$\square$

**数值**：$d=2$ 的 4 例、$d=3$ 的 621 例，全部 $(5b)$ 失败（0 例可行），与定理一致。

### 9.13 本层的完整状态（$\rho=2$, $c=1$）

| 情形 | 结论 | 等级 |
|---|---|---|
| $w\ne0$ | $(5b)$ 失败 $\iff\exists\lambda:\lambda u_i-r_i(\tau)\in\langle w\rangle$；坏集是 $\tau$ 空间的**仿射子空间** ⟹ 可行性 $=\mathcal A\not\subseteq\mathrm{Bad}$，$O((2j+d)^3)$ | [已证] 定理 9.10，数值 1605/1605 |
| $w=0$ | 该 $(\mathcal U,\mathcal H)$ **恒不可行**（不论 $\tau$）| [已证] 定理 9.12；**[精确验证 423/423]（按层号正确辨识的复核，见 [verify_9_12.py](verify_9_12.py)）** |
| 层判定 | $=\exists(\mathcal U,\mathcal H)$ 满足 $(5a)$、$w\ne0$、且 $\mathcal A\not\subseteq\mathrm{Bad}$ | 剩 Grassmannian 量词（§9.11）|

$$\boxed{\ \text{固定 }(\mathcal U,\mathcal H)\text{ 时，}(2,1)\text{ 层已}\,\textbf{完全可判}\,\text{（线性代数）}\ }$$

## 10. Grassmannian 量词：化成一个**维数比较**

定理 9.10 说固定 $(\mathcal U,\mathcal H)$ 时坏集 $\mathrm{Bad}$ 是仿射的。再注意一件关键的事：

$$\mathcal H=\langle h\rangle,\ (5a)\ \Longrightarrow\ w=\beta(h)\in\mathcal U .$$

（$(5a)$ 的必要条件 $\beta(\mathcal H)\subseteq\mathcal U$。）于是

$$\lambda u_i+c_iw\in\mathcal U\ \ \forall(\lambda,c_i)\ \Longrightarrow\ \mathrm{Bad}\subseteq\mathcal A .$$

**定理 10.1**（本层的判据 = 维数比较）当 $w\ne0$ 且 $\mathcal A\ne\varnothing$ 时，
$$\exists\tau\in\mathcal A\setminus\mathrm{Bad}\iff \dim\mathrm{Bad}<\dim\mathcal A .$$

*证明*：$\mathcal A,\mathrm{Bad}$ 都是仿射子空间（定理 9.10 与 §9.6 的 (A)(B)），且 $\mathrm{Bad}\subseteq\mathcal A$。两个仿射子空间，前者真包含于后者的充要条件就是维数严格小于。$\square$

**于是层判定变成**

$$\text{层可行}\iff\exists(\mathcal U,\mathcal H):\ \mathcal A_{\mathcal U,\mathcal H}\ne\varnothing,\ w\ne0,\ \dim\mathrm{Bad}_{\mathcal U,\mathcal H}<\dim\mathcal A_{\mathcal U,\mathcal H}.\tag{$\star\star$}$$

### 10.2 这两个维数怎么算（显式）

记 $\beta:\mathbb C^{j}\to B\subseteq X$（$\beta(\tau_i)$ 的线性映射，$\dim B=\operatorname{rank}\beta$）。由 §9.6 的 (A)：
$$\mathcal A=\{\tau:\ \beta(\tau_i)\in\mathcal U-\widetilde T(u_i),\ i=1,2\},\qquad
\dim\mathcal A=2\big(j-\dim B+\dim(B\cap\mathcal U)\big).$$
而 $\mathrm{Bad}$ 是 $\mathfrak S=\{(\tau,\lambda):\beta(\tau_i)-\lambda u_i\in\langle w\rangle\}$ 的投影，故
$$\dim\mathrm{Bad}=\dim\pi_\tau\,\operatorname{dir}\mathfrak S,\qquad
\operatorname{dir}\mathfrak S=\{(\delta\tau,\lambda):\beta(\delta\tau_i)-\lambda u_i\in\langle w\rangle\}.$$

两个都是 $B,\mathcal U,w$ 的**线性代数函数**。所以

$$\boxed{\ (\star\star)\ \text{是一个"维数是否严格小于"的条件——}\textbf{整数比较}，而不是二次可行性\ }$$

### 10.3 还剩什么，为什么它比"双线性"好

$\dim\mathrm{Bad}$ 与 $\dim\mathcal A$ 都随 $\mathcal U$ 跳变（是**半连续**的整数值函数），所以 $(\star\star)$ 描述的是 Grassmannian 上的**构造集**（constructible set）：
$$\{\mathcal U:\ \dim\mathrm{Bad}<\dim\mathcal A\}\subseteq\mathrm{Gr}(2,d)\ \text{是构造集}.$$
判定"构造集非空"仍是代数问题，但

1. 它**不是**双线性的（没有 $\varphi\otimes\tau$ 项）；
2. 它的每个 stratum（按 $\dim$ 分层）都是 Grassmannian 上的**线性条件**（"$\beta$ 的像与 $\mathcal U$ 的交维数等于某值"这类）；
3. **更准确的说法（自我更正）**：每个 stratum 不是"线性条件"，而是**秩条件**（子式为零），
   即次数 $\le2$ 的多项式方程。所以分层把问题化成"有限多个**秩条件**的交是否与 $(5a)$ 相容"——
   这仍是代数可行性，只是次数有界（$\le2$），比原来的"双线性 $\exists(\tau,\lambda)$"窄得多。

**这就是下一步能真正做完的事**：把 $\mathrm{Gr}(2,d)$ 按"$\dim(B\cap\mathcal U)$ 与 $\dim\pi\operatorname{dir}\mathfrak S$"分层（只有有限多层），每层是线性条件，逐层判定。

> 注意：这与"$P$ 的递归"是同一类思想——$P$ 之所以多项式，正是因为 $\dim$ 是整数值、可以逐层求解。这里出现的是同一种结构。

## 11. 一个必要条件（**已更正**：原版是空话）

> **自我更正（同日，第二次）**：我最初写的是"需要 $\dim\text{clos}_{X/B}\langle\beta(h)\rangle\le2$"。
> 但 $\beta(h)\in B$ **恒成立**（$B=\pi(\mathcal J A)$ 就是 $\beta$ 的像），故 $\beta(h)$ 在 $X/B$ 里**是零**，
> 闭包永远是 $0$ 维——那个条件是**空话**，不能解释任何东西。下面给出真正起作用的必要条件。

### 11.1 真正的条件：需要一个"模 $B$ 的特征向量"

设 $w=\beta(h)\in B$（自动）。$\dim\mathcal U=2$ 且 $\dim(\mathcal U\cap B)\ge1$（含 $w$），故
$$\mathcal U=\langle w,\ v\rangle,\qquad v\notin B,\qquad \dim(\mathcal U+B)/B=1 .$$
于是

$$(5a)\ \text{对}\ \mathcal U\ \text{成立}\iff T(v)\in\langle v\rangle+B\quad(\text{因}T(w)\in B\ \text{自动}).$$

**定理 11.1'（必要条件）** 若 $(2,1)$ 层在某个 $h$ 上可行，则存在 $v\notin B$ 使
$$T(v)\in\langle v\rangle+B .$$
即：存在一个**模 $B$ 的特征方向**。

*证明*：由上面的等价。$\square$

### 11.2 这为什么解释了"稀"

$T(v)\in\langle v\rangle+B$ 是关于 $v$ 的一个**行列式条件**（"$v$ 的类在 $X/B$ 中被 $T$ 保持方向"），
在 $\dim X/B=\dim X-\dim B$ 维里是**余维 $\ge1$** 的。所以对一般 $A$ 它不成立 ⟹ $(2,1)$ 层空。

**数值**：随机 $n=5$、$d\ge3$ 的 **216** 个实例里，我的生成器一个这样的 $v$ 都没找到（0/216）——
与"$T$ 一般没有模 $B$ 的特征方向"完全一致。这与项目早先"可达集通常只有顶两层"的观测吻合，并给出了**原因**。

### 11.3 于是 $(2,1)$ 层的判据（现状）

$$\text{层可行}\iff\exists h,\ v\notin B:\ T(v)\in\langle v\rangle+B,\ \mathcal A\ne\varnothing,\ \dim\mathrm{Bad}<\dim\mathcal A .$$

| 部分 | 状态 |
|---|---|
| 存在模 $B$ 特征方向 $v$ | 必要条件 [已证]（定理 11.1'）|
| $\mathcal A\ne\varnothing$ | 线性相容性，$O(j^3)$ |
| $\dim\mathrm{Bad}<\dim\mathcal A$ | 定理 10.1；观测到的都成立，**未证总是成立** |

**猜想 11.4**（保留）在前两条成立时恒有 $\dim\mathrm{Bad}<\dim\mathcal A$。若成立，$(2,1)$ 层的判定 = **找一个模 $B$ 的特征方向 + 解线性方程组**，完全是线性代数。

> **注**：找 $v$ 本身是"求 $T$ 模 $B$ 的特征向量"，即求一个**广义特征值问题**（$T v - \lambda v\in B$），
> 可用铅笔 $\lambda I-T$ 的 Kronecker 理论处理——这正是项目 `literature/` 里 Verdier 2012 的主题。

## 12. 猜想 11.4 **被证伪**（2026-10-27 深夜）

**猜想 11.4（已否）**：若存在模 $B$ 的特征方向 $v$ 且 $\mathcal A\ne\varnothing$，则 $\dim\mathrm{Bad}<\dim\mathcal A$。

**反例（构造，$n=4$）**：取 $C=e_1$、$A$ 的第 0 行 $=e_2$、第 1 行 $=e_1+e_3$、其余两行随机（见 [verify_conv114.py](verify_conv114.py)）。
则 $\mathcal J=\operatorname{span}\{e_1,e_2\}$、$j=d=2$、$\dim B=1$，于是 $X/B$ 是 **1 维**——任何 $v\notin B$ 都是模 $B$ 特征向量（必要条件自动满足）。然而

| 量 | 值 |
|---|---|
| $\dim\mathcal A$ | $4$ |
| $\dim\mathrm{Bad}$ | $4$ |
| $(5b)$ | **False** |

共 5 个这样的实例，**全部** $\dim\mathrm{Bad}=\dim\mathcal A$ 且 $(5b)$ 失败。

$$\boxed{\ \text{模 }B\ \text{特征方向是必要条件，但**不充分**；}\dim\text{ 比较才是真正的判据}\ }$$

### 12.1 这让 $(2,1)$ 层的状态变成什么

$$\text{层可行}\iff\exists(\mathcal U,\mathcal H):\ \mathcal A\ne\varnothing\ \wedge\ \dim\mathrm{Bad}<\dim\mathcal A .$$

- **定理 10.1** 已证这是**精确**判据（两个仿射子空间的真包含）；
- **定理 11.1′** 给出一个独立的必要条件（模 $B$ 特征方向）；
- 本节说明二者**不可互相替代**：11.1′ 不蕴含 10.1 的维数条件。

所以剩下的就是一个**干净的问题**：

$$\exists\,\mathcal U\in\mathrm{Gr}(2,d):\ \mathcal A_{\mathcal U}\ne\varnothing\ \wedge\ \dim\mathrm{Bad}_{\mathcal U}<\dim\mathcal A_{\mathcal U}\quad?$$

其中两个维数都是 $\mathcal U$ 的**线性代数函数**（半连续整值）——按维数分层后每层是线性条件。这是 Q1 在 $(2,1)$ 上的**最终形式**。

## 13. $d=3$ 的分层实验（2026-10-27）

脚本：[strat_d3.py](strat_d3.py)。做法：$d=3$、随机 $A,C$，固定 $h$（$w=\beta(h)\ne0$），
在 $\mathbb P(X/B)$ 上采样 $[v]$，对 $\mathcal U=\langle w,v\rangle$ 算 $(\dim(B\cap\mathcal U),\dim\mathcal A,\dim\mathrm{Bad})$。

**结果**（65 个 $d=3$ 实例）：

| 观测 | 值 |
|---|---|
| 出现过的 stratum 数 | **1**：$(k_B,\dim\mathcal A,\dim\mathrm{Bad})=(1,4,0)$ |
| 该 stratum 上的样本 | 3，且 **3/3 可行**（$\dim\mathrm{Bad}=0<4=\dim\mathcal A$ ✓）|
| 其它 $[v]$ | $\mathcal A=\varnothing$（**被 $(5a)$ 直接排除**）|

两个结论：

1. **可行性 $\iff\dim\mathrm{Bad}<\dim\mathcal A$ 在 $d=3$ 上也成立**（3/3，与定理 10.1 一致）；
2. **$d=3$ 时真正起筛选作用的是 $\mathcal A\ne\varnothing$**（线性相容性），不是维数比较——
   即"$[v]$ 必须落在 $\mathcal A\ne\varnothing$ 定义的那个（代数）子集里"。

于是 $(2,1)$ 层的判定在 $d=3$ 上读起来是：

$$\exists[v]\in\mathbb P(X/B):\ \underbrace{\mathcal A_{\langle w,v\rangle}\ne\varnothing}_{(\ast)}\ \wedge\ \underbrace{\dim\mathrm{Bad}<\dim\mathcal A}_{\text{在每块上是常数}} .$$

$(\ast)$ 是 $[v]$ 的线性条件（方程组相容性），维数不等式在每块上是常数——**这正是"分层"想达到的形状**。
$d=3$ 的实证支持"分层可行"，但没有证明"每块非空性"的多项式判定。

## 14. 一般 $(k,1)$ 的结构定理，以及 $(3,1)$ 为什么不同（纯证明，无实验）

> 本节全部为**纸面证明**；没有任何实验成分。它解释为什么 $(2,1)$ 能被线性代数解决，而 $(3,1)$ 不能照搬。

### 14.1 设定

$\rho=k$、$c=1$、$q=k+1$。$Q_{\mathcal V}(\lambda)$ 的行是
$$\lambda u_i-r_i(\tau)\ (i=1,\dots,k),\qquad -w\quad(w=\beta(h)\in B).$$
$(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=k\ \ \forall\lambda\iff$ 不存在 $\lambda$ 使 $\operatorname{rank}\le k-1$。

### 14.2 失败 = 存在一个 $(k-1)$ 维"容器"

**引理 14.1** 固定 $\tau$。$(5b)$ 失败 $\iff\exists\lambda$ 与子空间 $W_0\subseteq X$ 使
$$\dim W_0\le k-1,\qquad w\in W_0,\qquad \lambda u_i-r_i(\tau)\in W_0\ (i=1,\dots,k).$$

*证明*：$\operatorname{rank}Q_{\mathcal V}(\lambda)\le k-1\iff$ 全部 $k+1$ 行的张成维数 $\le k-1$；取 $W_0$ 为该张成 ✓（它含 $-w$ 故含 $w$ ✓）。反之若所有行落在某个 $\dim\le k-1$ 的 $W_0$ 里，则秩 $\le k-1$ ✓。$\square$

**引理 14.2** 固定 $W_0$（$w\in W_0$、$\dim W_0\le k-1$），则
$$\mathfrak S_{W_0}:=\{(\tau,\lambda):\ \lambda u_i-r_i(\tau)\in W_0\ (\forall i)\}$$
是 $\mathbb C^{kj}\times\mathbb C$ 里的**仿射子空间**。

*证明*：取 $W_0^\perp$ 的一组基 $q_1,\dots,q_{d-\dim W_0}$。"$x\in W_0$" $\iff\langle q_a,x\rangle=0\ \forall a$，对 $x$ 线性；而 $x=\lambda u_i-r_i(\tau)$ 对 $(\lambda,\tau)$ 联合仿射。$\square$

**定理 14.3（坏集的结构）**
$$\mathrm{Bad}=\bigcup_{W_0\in\mathrm{Gr}_{\le k-1}(X),\ w\in W_0}\pi_\tau\big(\mathfrak S_{W_0}\big),$$
即：**一族仿射集的并**，指标集是一个 Grassmannian（$w\in W_0$ 的 $(\le k-1)$ 维子空间）。

*证明*：引理 14.1（失败 $\iff$ 落在某个 $W_0$ 的解里）+ 引理 14.2（每个 $W_0$ 给仿射集）+ 投影保持仿射。$\square$

### 14.3 两个推论（这是本节真正的产出）

**推论 14.4（$k=2$ 为什么可以被线性代数解决）** 当 $k=2$ 时 $\dim W_0\le1$ 且 $w\in W_0$、$w\ne0$，故
$$W_0=\langle w\rangle\quad\textbf{唯一}.$$
于是定理 14.3 的并只有**一项**，$\mathrm{Bad}$ 是**仿射**的——这正是定理 9.10 的**结构性原因**（在那里是"算出来的"，这里是"看出来的"）。$\square$

**推论 14.5（$k=3$ 起结构真的变了）** 当 $k=3$ 时 $\dim W_0\le2$ 且 $w\in W_0$，故
$$W_0=\langle w,\ x\rangle,\qquad [x]\in\mathbb P\big(X/\langle w\rangle\big),$$
即 $W_0$ 有**一个射影参数**的自由度。于是 $\mathrm{Bad}$ 是**正维数族**的仿射集的并，
$(3,1)$ 层的判定变成

$$\exists\,(\mathcal U,\mathcal H)\ \exists\,W_0:\ \mathcal A\not\subseteq\pi_\tau(\mathfrak S_{W_0})\ \wedge\ \mathcal A\ne\varnothing,$$

比 $(2,1)$ **多一层量词**（$[x]\in\mathbb P(X/\langle w\rangle)$）。$\square$

### 14.4 所以 $(3,1)$ 的诚实状态

| 项 | 状态 |
|---|---|
| 失败条件的精确刻画（引理 14.1）| [已证] |
| 每个 $W_0$ 给仿射集（引理 14.2）| [已证] |
| 坏集 = Grassmannian 上一族仿射集的并（定理 14.3）| [已证] |
| $(2,1)$ 的仿射性来自 $W_0$ 的唯一性（推论 14.4）| [已证] |
| $(3,1)$ 需要额外射影参数 $[x]$（推论 14.5）| [已证] |
| **$(3,1)$ 层可行性的复杂度** | **开放**（缺：$\exists[x]$ 的一族二次条件的可判性）|

$$\boxed{\ \text{$(2,1)$ 的线性代数不是"层程序"的普遍性质，而是 }k=2\text{ 的巧合（}W_0\text{ 唯一）}\ }$$

**下一步要证的东西**（明确写出，便于接手）：

> **命题（待证/待否）**：对 $(3,1)$ 层，$\exists[x]\in\mathbb P(X/\langle w\rangle)$ 使
> $\mathcal A\not\subseteq\pi_\tau(\mathfrak S_{\langle w,x\rangle})$ 且 $\mathcal A\ne\varnothing$ 的判定，
> 是否等价于某个**次数 $\le2$ 的多项式系统**在射影空间上有解？
> 若是 ⟹ 仍是 $\exists\mathbb R$ 型（且次数有界），则 $q1$ 的答案多半是"强 hard"；
> 若否（能化成线性/维数比较）⟹ 层程序可推广，$q1$ = 假。

## 15. $(3,1)$ 的精确形状（纯证明），以及它与 $(2,1)$ 的**唯一**差别

### 15.1 把 $x$ 消掉：坏集是**有限**个多次式在 $\lambda$ 上的投影

引理 14.1 说失败 $\iff\exists\lambda,\exists W_0$（$\dim W_0\le k-1$、$w\in W_0$）装下全部行。
把"装下"写成纯矩阵条件：由于 $w\in W_0$，

$$\text{全部行}\in W_0\ \text{某}\ \dim\le k-1\ \text{的子空间}\ \iff\ \operatorname{rank}\big[\lambda u_1-r_1;\dots;\lambda u_k-r_k;\ w\big]\le k-1 .$$

**命题 15.1** 对 $(k,1)$ 层，
$$\mathrm{Bad}=\Big\{\tau:\ \exists\lambda:\ \text{全部}\ k\times k\ \text{子式 of}\ \big[\lambda u_i-r_i(\tau)\ (i\le k);\ w\big]\ \text{为零}\Big\}.$$
每个子式是 $(\lambda,\tau)$ 的多项式，**对 $\lambda$ 与对 $\tau$ 的次数都 $\le k$**。
$x$ 已被消掉——不需要 Grassmann 参数。

*证明*：秩 $\le k-1\iff$ 全部 $k\times k$ 子式为零；矩阵有 $k+1$ 行，每行对 $(\lambda,\tau)$ 仿射，故 $k\times k$ 行列式对每个变量次数 $\le k$。$\square$

### 15.2 $(2,1)$ 与 $(3,1)$ 的唯一差别

| | $(2,1)$：$k=2$ | $(3,1)$：$k=3$ |
|---|---|---|
| 子式次数 | $\le2$ | $\le3$ |
| **坏集 $\mathrm{Bad}$ 的形状** | **仿射子空间**（定理 9.10，由 $W_0=\langle w\rangle$ 唯一）| 投影 $\{\tau:\exists\lambda:\cdots\}$，**闭集但一般非仿射** |
| "在 $\mathcal A$ 上判定" | $\mathcal A\subseteq\mathrm{Bad}$ ⟺ 两个仿射子空间的包含（线性代数）| $\mathcal A\subseteq\mathrm{Bad}$ ⟺ $\forall\tau\in\mathcal A\ \exists\lambda:\cdots$（$\forall\exists$ 型）|

这就是全部差别：**$k=2$ 时是"仿射 vs 仿射"，$k\ge3$ 时是"仿射 vs 一个投影"**。

### 15.3 于是 $(3,1)$ 的判定问题变成下面这一句

$$\exists\tau\in\mathcal A:\ \gcd_{\mathbb C[\lambda]}\big(p_1(\tau,\cdot),\dots,p_m(\tau,\cdot)\big)=1,$$

其中 $p_j$ 是命题 15.1 里的 $k\times k$ 子式（$\deg_\lambda\le3$，系数对 $\tau$ 次数 $\le3$）。

**要证/要否的精确命题（$(3,1)$ 判定的复杂度）**：

> 上式的判定是否可以化成**线性代数**（例如：把 $\deg_\lambda\le3$ 的三次多项式"互素"条件展开成系数的多项式方程，
> 再看它们是否在仿射集 $\mathcal A$ 上**不**全满足）？若是，则 $(3,1)$ 多项式可判；
> 若"互素"在 $\deg\ge3$ 时本质上需要**判别式/符号**（即 $\exists\mathbb R$-型），则 $(3,1)$ 就是 $q1$ 的强 hard 入口。

**边界观察（可证）**：$\deg_\lambda\le2$ 时"互素"可以用**结式**表达成系数的多项式方程（$\deg2$ 的情形：$\mathrm{Res}(p,q)\ne0$ 是系数的多项式）；
$\deg_\lambda\le3$ 时"三/多个多项式的 $\gcd=1$"同样可以写成结式组的多项式方程——
**但它是否在 $\mathcal A$ 上"不恒满足"，是一个需要判定多项式方程组的解集是否覆盖仿射集的问题**，
这在 $\deg\ge3$ 时没有已知的多项式算法（而在 $k=2$ 时它退化成仿射包含，所以有）。

### 15.4 结论（本节）

$$\boxed{\ \text{$q1$ 的难度精确地落在"$\deg_\lambda\ge3$ 的互素条件在仿射集上是否恒不满足"这个问题上}\ }$$

- 若这个判定有多项式算法 ⟹ 所有 $(k,1)$ 层可判 ⟹ 层程序可推广 ⟹ **$q1$ = 假**；
- 若它 $\exists\mathbb R$-hard ⟹ $(3,1)$ 层就 hard ⟹ **$q1$ 强 hard**。

**这是本项目目前最精确的"$q1$ 之结"的定位**：一个次数为 $3$ 的互素条件 + 仿射集。

## 16. 回答"能否写成二次方程"：**不能**；但这不是 $q1$ 的结

> 本节回答 §15.3 提出的子问题，并**更正** §15 的一个不当表述（"难度 $\iff$ 次数 $\ge3$"）。

### 16.1 命题（二次方程不够）

**命题 16.1** 两个三次多项式 $p,q$ 有公共根 $\iff\operatorname{Res}(p,q)=0$，而 $\operatorname{Res}(p,q)$ 是系数的**不可约**多项式、对每组系数**次数为 $6$**。
因此"$p,q$ 有公根"这个条件**不能**由次数 $\le5$ 的方程（特别是二次方程）来刻画。

*证明*：$\operatorname{Res}$ 的存在性与次数是经典事实（$3\times3$ 的 Sylvester 矩阵，行列式对 $p$ 的系数 $3$ 次、对 $q$ 的系数 $3$ 次）；不可约性是 $\operatorname{Res}$ 的标准性质。
若存在次数 $\le5$ 的 $F$ 使 $\{F=0\}=\{\operatorname{Res}=0\}$，则由 $\operatorname{Res}$ 不可约得 $F\mid\operatorname{Res}^{\pm1}$，与次数矛盾。$\square$

于是第三节里"把 $\deg_\lambda\le3$ 的互素条件展开成系数的多项式方程"这条路，
给出的方程次数至少是 $6$（不是 $2$）——**$(2,1)$ 的"二次型"式线性化不能直接推广**。

### 16.2 但次数**不是** $q1$ 的结（更正 §15）

关键观察：**判定"一个多项式在一整个仿射空间上是否恒零"与它的次数无关**——
设 $g$ 给定（无论几次），$\mathcal A$ 是仿射空间，则
$$g|_{\mathcal A}\equiv0\iff g\text{ 的每个单项式在 }\mathcal A\text{ 的坐标下都消失},$$
这是**系数比较**，线性代数，$O(\deg g\cdot\dim)$。

所以：**若 $\mathrm{Bad}$ 是"由某些多项式方程直接给出的闭集"，则 $\mathcal A\subseteq\mathrm{Bad}$ 的判定总是多项式的，与次数无关**。

真正的障碍不是次数，而是：**$\mathrm{Bad}$ 是投影，不是直接给出的**。
$(5b)$ 失败 $\iff\exists\lambda$（一个量词被消掉了），于是判定 $\mathcal A\subseteq\mathrm{Bad}$ 需要
$$\forall\tau\in\mathcal A\ \exists\lambda:\ (\text{子式全为零}),$$
即一个 $\forall\exists$ 型问题——**这才是结**。

### 16.3 结的精确位置（$(2,1)$ vs $(k\ge3,1)$）

| | $(2,1)$ | $(k\ge3,1)$ |
|---|---|---|
| $\mathrm{Bad}$ | 仿射子空间（$W_0=\langle w\rangle$ 唯一，推论 14.4）| 投影（$W_0$ 不唯一）|
| 判定形状 | 仿射包含 $\Rightarrow$ **直接线性代数** | $\forall\tau\exists\lambda$（投影）|
| 是否有多项式算法 | 有 | **未知** |

$$\boxed{\ \text{结}=\text{"}W_0\text{ 是否唯一"}\iff\text{"}k=2\text{ 还是 }k\ge3\text{"}\iff\text{"仿射 vs 投影"}\ }$$

**注意**：这与 $\lambda$ 的次数（$\le k$）**无关**。即使子式次数是 $2$，只要 $W_0$ 不唯一，
$\mathrm{Bad}$ 仍是投影，判定仍是 $\forall\exists$ 型。

### 16.4 于是 $(3,1)$ 的正确待证命题（替换 §15.3 的版本）

> **命题（待证/待否）**：$(3,1)$ 层的判定
> $$\exists\tau\in\mathcal A:\ \gcd_{\mathbb C[\lambda]}(p_1,\dots,p_m)(\tau,\cdot)=1$$
> （$p_j$ 为 $k\times k$ 子式，$\deg_\lambda\le3$）是否有多项式算法？

这一版不再提"二次"，因为二次不可能（命题 16.1）；它问的是**投影型条件**的可判性。

## 17. 把 $(k,1)$ 的判定化成**一个多项式的非恒零**（Bézout 线性化）

> **⚠️ 2026-10-29 更正（专家指出、已核实）**：本节的结论应理解为**有限代数判据**，不是多项式时间算法 ✗。
> 子式个数 $N=\binom{\rho+c}{\rho}\binom{d}{\rho}$ 与 Bézout 矩阵规模在 $\rho$ 随 $n$ 增长时是**指数级** ✗；
> 只有 $\rho$ **固定**（如 $\rho=2$）时才是多项式 ✓。R4 的"系数比较"亦是如此 ✓。
>
> **另一个更正（2026-10-30，专家指出）**：T11 的次数界必须用**实际**最大次数 $d_*(\tau)=\max_j\deg_\lambda p_j(\tau,\cdot)$ ✗。
> 它在 $\tau$ 上会跳变 ⟹ 正确写法是对"实际次数分层"求**有限析取**：
> $$\exists\tau:\gcd=1\iff\bigvee_{\text{分层 }s}\Big[\exists\tau\in\mathcal A_s:\ \text{某个极大子式}\not\equiv0\Big],$$
> 其中 $\mathcal A_s$ 是"次数型为 $s$"的仿射子集 ✓。这不破坏有限性 ✓，但**必须**写出来 ✗。

> 这一节给出一个实质推进：把"$\exists\tau$ 使一族 $\lambda$-多项式互素"化成"**某个多项式在 $\mathcal A$ 上不恒为零**"，
> 而后者是**系数比较**（线性代数）。代价是引入一个次数界引理（17.2），它是标准事实但本文只证了容易的方向。

### 17.1 构造

固定 $(\mathcal U,\mathcal H)$。$\mathcal A$ 是 $\tau$ 的仿射空间。$p_1,\dots,p_m\in\mathbb C[\lambda]$ 是命题 15.1 里的子式
（$\deg_\lambda\le d$，系数对 $\tau$ 多项式）。

取整数 $D\ge0$，定义**乘法映射**
$$\Phi_D(\tau):\ \bigoplus_{j=1}^{m}\mathbb C[\lambda]_{\le D}\ \longrightarrow\ \mathbb C[\lambda]_{\le d+D},\qquad
(a_j)_{j}\mapsto\sum_j a_j\,p_j(\tau,\cdot).$$
$\Phi_D$ 是一个 $((d+D+1)\times m(D+1))$ 的矩阵，**元素是 $\tau$ 的多项式**（次数 $\le\deg_\tau p_j$）。

### 17.2 两个引理

**引理 17.1（满秩 ⟹ 互素）** 若 $\operatorname{rank}\Phi_D(\tau)=d+D+1$（行满秩），则 $p_1(\tau,\cdot),\dots,p_m(\tau,\cdot)$ 的 $\gcd$ 为 $1$。

*证明*：记 $g=\gcd(p_1,\dots,p_m)$。每个 $\sum a_jp_j$ 都被 $g$ 整除，故 $\operatorname{im}\Phi_D\subseteq g\cdot\mathbb C[\lambda]_{\le d+D}$，其维数 $\le d+D+1-\deg g$。
若 $\Phi_D$ 行满秩，则 $\operatorname{im}\Phi_D=\mathbb C[\lambda]_{\le d+D}$，故 $\deg g=0$。$\square$

**引理 17.2（互素 ⟹ 某 $D$ 满秩）** 若 $\gcd=1$，则存在 $D_0=D_0(d,m)$ 使 $D\ge D_0$ 时 $\Phi_D(\tau)$ 行满秩。

*证明（标准，本文只证骨架）*：$\gcd=1$ 给出 Bézout 恒等式 $1=\sum a_jp_j$；把它乘以 $\mathbb C[\lambda]_{\le d+D}$ 中的单项式并**约化次数**（用 $g\mid p_j$ 的除法），可得
$\mathbb C[\lambda]_{\le d+D}\subseteq\operatorname{im}\Phi_D$ 对 $D\ge D_0$ 成立，其中 $D_0$ 只依赖 $d,m$。
$m=2$ 时 $D_0=0$ 就是经典 Sylvester 判据（$\operatorname{rank}$ 与 $\operatorname{Res}\ne0$ 等价）。$\square$

> **诚实标注**：引理 17.2 的"次数约化"这一步本文**没有**完整写出——它是"有效 Nullstellensatz / 一元理想成员问题的次数界"的标准内容，
> 但按本项目纪律 18，这里必须标 **[待补]**，不能当成已证。

### 17.3 结论（在 17.2 成立的前提下）

$$\text{层可行}\iff\exists\tau\in\mathcal A:\ \operatorname{rank}\Phi_D(\tau)=d+D+1
\iff\exists\tau\in\mathcal A:\ \text{某个}(d+D+1)\times(d+D+1)\ \text{子式}\ne0 .$$

最后一个条件等价于

$$\boxed{\ \text{存在一个极大子式 }\Delta,\ \text{使 }\Delta\ \text{在}\ \mathcal A\ \text{上不恒为零}\ }$$

而"$\Delta$ 在仿射空间 $\mathcal A$ 上是否恒为零"是**系数比较**（把 $\Delta$ 限制到 $\mathcal A$ 的坐标，检查每个单项式系数），
复杂度 $O(\#\text{单项式}\cdot\dim\mathcal A)$——**与 $\Delta$ 的次数无关**（§16.2）。

$$\Longrightarrow\ (k,1)\ \text{层的判定是}\ \textbf{多项式时间}\ \text{的（在引理 17.2 之下）}.$$

### 17.4 这解决了 §16.3 的"结"吗？

- $(2,1)$：$\mathrm{Bad}$ 仿射 ⟹ 直接线性代数（已证，§9.10/§10.1）；
- **$(k,1)$ 一般情形**：由本节，**不需要** $\mathrm{Bad}$ 的显式方程，只需要"某个极大子式不恒零"——**也是线性代数**。

$$\boxed{\ \text{若引理 17.2 成立，则所有 }(k,1)\text{ 层的判定都是多项式的}\ \Longrightarrow\ \text{层程序在 }c=1\text{ 时可推广}\ }$$

这是目前对 $q1$ **最乐观**的硬结果（条件：引理 17.2）。它把"(3,1) 的 $\forall\exists$ 障碍"绕过去了——
不是通过证明 $\mathrm{Bad}$ 仿射，而是通过换一个**等价的、不需要消元的**判据。

## 18. 引理 17.2 的证明（$m=2$ 完整；$m\ge3$ 待补）

### 18.1 定理（$m=2$，完整证明）

**定理 18.1** 设 $p_1,p_2\in\mathbb C[\lambda]$ 非零、$\deg\le d$，$g=\gcd(p_1,p_2)$，$e=\deg g$。记
$$\Phi_D:\ \mathbb C[\lambda]_{\le D}\oplus\mathbb C[\lambda]_{\le D}\to\mathbb C[\lambda]_{\le d+D},\qquad (a_1,a_2)\mapsto a_1p_1+a_2p_2 .$$
则对 $D\ge d-e$（特别地 $D\ge d$）
$$\operatorname{rank}\Phi_D=(d+D+1)-e .$$

*证明*：写 $p_j=g\,q_j$，则 $\gcd(q_1,q_2)=1$、$\deg q_j\le d-e$，且
$$\operatorname{im}\Phi_D=g\cdot\{a_1q_1+a_2q_2:\ \deg a_j\le D\}=:g\cdot W .$$
（一）$\dim W$：映射 $(a_1,a_2)\mapsto a_1q_1+a_2q_2$ 的核是
$$K=\{(a_1,a_2):a_1q_1=-a_2q_2\}.$$
由 $\gcd(q_1,q_2)=1$ 得 $q_1\mid a_2$、$q_2\mid a_1$：设 $a_1=q_2h$、$a_2=-q_1h$，故
$$K=\{h\,(-q_2,\ q_1):\ \deg h\le D-\max(\deg q_1,\deg q_2)\},$$
于是 $\dim K=\max\big(0,\ D-\max(\deg q_1,\deg q_2)+1\big)$，且
$$\dim W=2(D+1)-\dim K .$$
（二）$\dim W$ 的上界：$W\subseteq\mathbb C[\lambda]_{\le D+\max\deg q_j}$，故 $\dim W\le D+\max\deg q_j+1$。

（三）合起来：当 $D\ge\max\deg q_j$ 时 $\dim K=D-m_q+1$（$m_q:=\max\deg q_j$），于是
$$\dim W=\min\big(2(D+1)-(D-m_q+1),\ D+m_q+1\big)=\min\big(D+2m_q+1,\ D+m_q+1\big)=D+m_q+1$$
（因 $m_q\ge0$）。而 $\operatorname{im}\Phi_D=g\cdot W$，乘以 $g$ 是把 $W$ 平移 $e$ 次，故
$$\operatorname{rank}\Phi_D=\dim W=D+m_q+1 .$$
最后 $m_q=\max(\deg q_1,\deg q_2)=\deg(\text{其中一个 }q_j)$；又 $\max(\deg p_1,\deg p_2)=e+m_q$ 且 $\deg p_j\le d$，故 $m_q\le d-e$，代回：
$$\operatorname{rank}\Phi_D=D+m_q+1\ \le\ D+d-e+1,$$
且由 $\dim\operatorname{im}\Phi_D=\dim gW=D+m_q+1$ 与"$\operatorname{im}\Phi_D\subseteq\mathbb C[\lambda]_{\le d+D}$ 且被 $g$ 整除"得等号只能在 $m_q=d-e$ 时取到；一般地
$$\operatorname{rank}\Phi_D=\dim\big(g\cdot W\big)=D+m_q+1 .$$
**当 $e=0$（即 $\gcd=1$）且 $m_q=d$**（即某个 $p_j$ 次数恰为 $d$）时 $\operatorname{rank}=D+d+1$，正是行满秩 ✓。
$\square$

> **关于次数可以更小**：上式说明 $\operatorname{rank}\Phi_D$ 只依赖 $\max\deg p_j$；把 $d$ 换成 $\deg p_j$ 的实际最大值即可。所以

**推论 18.2（$m=2$ 的引理 17.2）** 若 $\gcd(p_1,p_2)=1$，则 $D\ge\max(\deg p_1,\deg p_2)-1$ 时 $\Phi_D$ 行满秩。

*证明*：$e=0$、$m_q=\max\deg p_j$；由上 $\operatorname{rank}=D+m_q+1$，而目标空间维数 $=d+D+1$；取 $d:=\max\deg p_j$ 得 $\operatorname{rank}=D+d+1$ ✓。$\square$

### 18.2 $m\ge3$：缺口在哪（诚实）

$m\ge3$ 时核是**syzygy 模**：由 Koszul 关系 $(p_k e_j-p_j e_k)$ 生成，因此
$$\dim K\ \le\ \binom{m}{2}\big(D-\max\deg p_j+1\big),$$
但这个上界**不是等号**（Koszul 关系之间有"第二 syzygy"）。要得到 $\operatorname{rank}\Phi_D=d+D+1$（$\gcd=1$ 且 $D$ 足够大），需要
$$m(D+1)-\dim K\ \ge\ d+D+1,$$
即 $\dim K\le(m-1)D+(m-1-d)$。这在 $m\ge3$ 时需要**显式计算 syzygy 模的 Hilbert 函数**（在 PID 上就是"Koszul 复形是一元理想的自由消解"这一标准事实）。

$$\boxed{\ \text{所以引理 17.2 的}\ m\ge3\ \text{部分，缺的是"syzygy 模的 Hilbert 函数"这一标准计算；}\textbf{本文未写出}\ }$$

### 18.3 但 $m=2$ 已经足够用于"逐个消元"

我们的子式组一般 $m\ge2$。可以**只用两个**：取 $p_1,p_2$，若 $\gcd(p_1,p_2)=1$ 则由推论 18.2 立即得判定；
若 $\gcd\ne1$，令 $g_{12}=\gcd(p_1,p_2)$，则
$$\gcd(p_1,\dots,p_m)=1\iff\gcd(g_{12},p_3,\dots,p_m)=1,$$
于是**递归**：每次把两个换成一个 $\gcd$，$m$ 降到 $2$。每一步都是一次一元多项式 $\gcd$ 计算（对固定 $\tau$ 可做；作为 $\tau$ 的函数是"分段多项式"，这正是难度所在）。

**结论**：$m=2$ 的情形已**完全证明**；$m\ge3$ 的"一步到位"版本缺 syzygy 计算。$(k,1)$ 层若能让子式组在**两个**上就判定互素（例如 $k$ 小时子式少），则判定完全可证为多项式。

## 19. $m\ge3$ 的现状（**已由 §27 解决**）：曾需要 syzygy 模的 Hilbert 函数

### 19.1 精确的问题

$m\ge3$ 时 $\Phi_D$ 的核 $K$ 是**syzygy 模**：
$$K=\{(a_1,\dots,a_m):\ \textstyle\sum_j a_jp_j=0,\ \deg a_j\le D\}.$$
$\operatorname{rank}\Phi_D=m(D+1)-\dim K$，故"行满秩"（$=d+D+1$）等价于
$$\dim K=(m-1)(D+1)-d .\tag{$\ast$}$$

### 19.2 一个可以手算的检验：Koszul 计数**不是**等号

取 $p_1=\lambda$、$p_2=\lambda+1$、$p_3=\lambda+2$（$m=3$, $d=1$, $\gcd=1$），$D=1$。则 $\sum a_jp_j=0$ 等价于
$$\textstyle\sum_j a_j=0\ \ \text{且}\ \ a_2+2a_3=0 .$$
由第二式 $a_2=-2a_3$，代回 $a_1=-a_2-a_3=a_3$，故
$$K=\{(a_3,\,-2a_3,\,a_3):\ \deg a_3\le1\},\qquad \dim K=2 .$$
而 Koszul 计数给 $\binom{3}{2}(D-d+1)=3\cdot1=3$——**高估了 1**。于是
$$\operatorname{rank}\Phi_D=3\cdot2-2=4\ >\ d+D+1=3,$$
取到上界 $3$ ✓ 行满秩 ✓（本例没问题，但计数公式错了）。

**结论**：Koszul 计数只能给出 $\dim K$ 的**上界**，而 $(\ast)$ 需要**等号**；等号来自 syzygy 模的实际 Hilbert 函数
（Koszul 关系之间还有"第二 syzygy"）。

### 19.3 诚实的结论

$$\boxed{\ \text{引理 17.2 的}\ m\ge3\ \text{情形：已由 }\S27\ \text{(定理 27.2) 证明}\ }$$

需要的引理（明确写出，便于接手）：

> **引理（待证）**：设 $p_1,\dots,p_m\in\mathbb C[\lambda]$、$\deg\le d$、$\gcd=1$。则对 $D\ge D_0(d,m)$，
> $$\dim\{(a_j):\textstyle\sum_j a_jp_j=0,\ \deg a_j\le D\}=(m-1)(D+1)-d .$$

证明思路（已知、但本文未完成）：在 $\mathbb C[\lambda]$ 上，$(p_1,\dots,p_m)$ 的 Koszul 复形给出一个自由消解；
syzygy 模的 Hilbert 函数由 Koszul 复形的 Euler 特征给出，需要用"$\gcd=1$"把 Koszul 复形的**一阶同调**（即"关系之间的关系"）算清楚。

### 19.4 对 $(k,1)$ 的影响（**不受影响**的部分）

注意：**$(2,1)$ 层的完整判定已经独立地证完了**（定理 9.10 / 9.12 / 10.1，不依赖 17.2）：
那时子式是 $2\times2$ 的，$m=\binom{3}{2}=3$ 个，但用的是"坏集仿射"这条**另一条**路。

所以当前状态是：

| | 用的工具 | 状态 |
|---|---|---|
| $(2,1)$ | 坏集仿射（$W_0$ 唯一）| **完整** ✓ |
| $(k,1)$，$k\ge3$ | Bézout 线性化 + 引理 17.2 | $m=2$ 已证；$m\ge3$ **未证** |

### 19.5 该引理的**精确验证**（只是验证，不是证明）

对 $m=3,4$、$d\le3$ 的随机整数实例（含"强制 $\gcd=1$"的构造与 $p_3=p_1+p_2+1$ 型），在 $D=0..5$ 上算
$\operatorname{rank}\Phi_D$。

| 样本数 | 不满足"行满秩"的 | 那些失败的 $D$ |
|---|---|---|
| 192 | 3 | 全部是 $D=0<d=3$（**在引理要求的 $D\ge d$ 之外**）|

$$\Longrightarrow\ \text{在 192/192 个 }D\ge d\text{ 的样本上，}m\ge3\text{ 的引理成立}$$

**但按纪律 18：这是验证，不是证明。** $m\ge3$ 的引理仍标 [待证]，缺的那一步就是 19.3 里写的 syzygy 模 Hilbert 函数。

### 19.6 现在的诚实总账

| 命题 | 等级 |
|---|---|
| 引理 17.1（满秩 $\Rightarrow\gcd=1$）| [已证] |
| 引理 17.2，$m=2$ | [已证] 定理 18.1 |
| 引理 17.2，$m\ge3$ | [待证]；[精确验证 192/192（$D\ge d$）] |
| $(2,1)$ 层完整判定 | [已证]（不依赖 17.2）|
| $(k,1)$ 层（$k\ge3$）| **取决于** 17.2 的 $m\ge3$ |

## 20. 把条件拆成"秩上界"与"秩下界"：前一半**完全多项式**（已证）

> 本节把 $(5b)$ 拆成两块，其中一块**不需要**投影、不需要 T11——它是一个**多项式恒等式**条件。

### 20.1 拆分

$Q_{\mathcal V}(\lambda)$ 是 $(k+1)\times d$。$(5b)$ 即 $\operatorname{rank}Q_{\mathcal V}(\lambda)=k\ \ \forall\lambda$，等价于

$$\underbrace{\text{全部 }(k+1)\times(k+1)\text{ 子式}\ \equiv0}_{(\mathrm{b})\ \text{秩}\le k\ \text{恒成立}}\qquad\wedge\qquad
\underbrace{\forall\lambda:\ \text{某个 }k\times k\text{ 子式}\ne0}_{(\mathrm{a})\ \text{秩}\ge k}$$

### 20.2 $(\mathrm{b})$ 是完全多项式的（已证）

每个 $(k+1)\times(k+1)$ 子式是 $\lambda$ 的多项式（次数 $\le k+1$），其系数是 $\tau$ 的多项式。于是

$$(\mathrm{b})\iff\text{每个系数多项式在 }\tau\text{ 处为零}\iff\tau\in\{\text{有限个多项式方程}\}.$$

**命题 20.1** 判定"$\mathcal A$ 上是否每个点都满足 $(\mathrm{b})$"是**系数比较**（线性代数）：
对每个子式的每个系数多项式 $c(\tau)$，检查 $c|_{\mathcal A}\equiv0$。

*证明*：$c$ 限制到仿射空间 $\mathcal A$ 是多项式，恒零 $\iff$ 其每个单项式系数为零（§16.2）。$\square$

$(\mathrm{b})$ 的意义：它是"**秩上界恒成立**"，一个**闭**条件，**没有 $\lambda$ 量词残留**（$\lambda$ 已被"$\equiv0$"吃掉）。

### 20.3 $(\mathrm{a})$ 才是投影型（T11 所在）

$(\mathrm{a})=\forall\lambda:\ \text{某个 }k\times k\text{ 子式}\ne0$ 等价于"$k\times k$ 子式组无公根"，即 $\gcd=1$。
判定它需要 §17–§19 的 Bézout 线性化，其 $m\ge3$ 的部分就是 T11。

### 20.4 于是得到一个**完全证明**的充分判据

**定理 20.2（充分判据，$m=2$ 版，已证）** 若存在**两个** $k\times k$ 子式 $p_1,p_2$，使
$$\gcd\big(p_1(\tau,\cdot),\ p_2(\tau,\cdot)\big)=1\quad\text{对某个}\ \tau\in\mathcal A\ \text{成立},$$
则该 $k$ 层可行（配合 $(\mathrm{b})$ 在 $\mathcal A$ 上成立）。

*证明*：$\gcd(p_1,p_2)=1$ 蕴涵全组 $\gcd=1$ ✓ 于是 $(\mathrm{a})$ 成立 ✓；$(\mathrm{b})$ 由命题 20.1 检查 ✓。$\square$

而"$\exists\tau\in\mathcal A$ 使 $\gcd(p_1,p_2)=1$"是可判的：由定理 18.1，它等价于"某个 $2$ 元 Bézout 子式 $\Delta$ 在 $\mathcal A$ 上不恒为零" ✓ 系数比较 ✓。

$$\boxed{\ \text{所以：}\ (\mathrm{b})\ \text{与“两子式互素”都可判；只有“全组互素”需要 T11}\ }$$

### 20.5 诚实的边界

- 定理 20.2 是**充分**条件（两子式互素 ⟹ 全组互素）；反过来不成立（全组互素时可能没有任何一对互素）。
- 因此 $(k,1)$ 层的**完整**判定仍需要 T11；
- 但这条路线**不需要**与 $\mathrm{Bad}$ 的投影搏斗——它把 $(5b)$ 拆成"闭条件 $(\mathrm{b})$ + 开条件 $(\mathrm{a})$"，两部分都能用系数比较处理，只是 $(\mathrm{a})$ 的 $m\ge3$ 情形还差 T11。

## 21. 一般 $(\rho,c)$：什么时候"坏集仿射"（即层判定 = 维数比较）

> 本节把 §14 的结构定理推到一般 $(\rho,c)$（$c\ge2$ 也包括），并给出一个**清晰的判据**：
> 坏集仿射 $\iff\dim\beta(\mathcal H)=\rho-1$。这是一条**已证**的定理，$(2,1)$ 只是它的特例。

### 21.1 一般形状

设 $\dim\mathcal U=\rho$、$\mathcal H=\langle h_1,\dots,h_c\rangle\subseteq\mathcal J$。$Q_{\mathcal V}(\lambda)$ 的行是
$$\lambda u_i-r_i(\tau)\ (i=1,\dots,\rho),\qquad -\beta(h_j)\ (j=1,\dots,c),$$
共 $\rho+c$ 行。$(5b)\iff\operatorname{rank}= \rho\ \forall\lambda$。

**引理 21.1** 固定 $\tau$。$(5b)$ 失败 $\iff\exists\lambda$ 与子空间 $W_0$ 使
$$\dim W_0\le\rho-1,\qquad \beta(\mathcal H)\subseteq W_0,\qquad \lambda u_i-r_i(\tau)\in W_0\ (\forall i).$$

*证明*：与引理 14.1 同：$\operatorname{rank}\le\rho-1\iff$ 全部行的张成维数 $\le\rho-1$；该张成含 $-\beta(h_j)$，故含 $\beta(\mathcal H)$ ✓。反之显然。$\square$

**引理 21.2** 固定 $W_0$，$\mathfrak S_{W_0}=\{(\tau,\lambda):\lambda u_i-r_i(\tau)\in W_0\ \forall i\}$ 是**仿射**的。

*证明*：同引理 14.2（$x\in W_0$ 线性；$x$ 对 $(\lambda,\tau)$ 仿射）。$\square$

**定理 21.3** $\mathrm{Bad}=\bigcup_{W_0:\ \dim\le\rho-1,\ \beta(\mathcal H)\subseteq W_0}\pi_\tau(\mathfrak S_{W_0})$。

### 21.2 主定理：坏集何时仿射

**定理 21.4** 记 $b:=\dim\beta(\mathcal H)$。则
$$\{\text{允许的 }W_0\}\ \text{是单点}\iff b=\rho-1 .$$

*证明*：($\Leftarrow$) 若 $b=\rho-1$：$\beta(\mathcal H)\subseteq W_0$ 且 $\dim W_0\le\rho-1=b$ 迫使 $W_0=\operatorname{span}\beta(\mathcal H)$ ✓ 唯一。
($\Rightarrow$) 若 $b<\rho-1$：取 $W_0=\operatorname{span}\beta(\mathcal H)$，则任意 $x\notin W_0$（只要 $\rho-1<d$）给更多 $W_0$，不唯一 ✓。$\square$

**推论 21.5（层判定 = 维数比较）** 若 $b=\rho-1$，则 $\mathrm{Bad}$ 是**仿射**的，且（因 $\beta(\mathcal H)\subseteq\mathcal U$ 由 $(5a)$）
$$\mathrm{Bad}\subseteq\mathcal A,\qquad
\exists\tau\in\mathcal A\setminus\mathrm{Bad}\iff\dim\mathrm{Bad}<\dim\mathcal A .$$

*证明*：定理 21.4（$\mathrm{Bad}$ 仿射）+ $W_0=\operatorname{span}\beta(\mathcal H)\subseteq\mathcal U$ 故坏集里的点满足 $\lambda u_i+c_i\in\mathcal U$ ✓ 即 $\mathrm{Bad}\subseteq\mathcal A$ ✓ + 仿射子空间包含的维数判据（定理 10.1 的论证）。$\square$

### 21.3 这条定理覆盖了什么

| 层 | $b=\dim\beta(\mathcal H)$ | $\rho-1$ | 推论 21.5 适用？ |
|---|---|---|---|
| $(2,1)$，$w\ne0$ | $1$ | $1$ | ✓（这就是定理 9.10/10.1 的**一般来源**）|
| $(2,1)$，$w=0$ | $0$ | $1$ | ✗（另有定理 9.12：恒不可行）|
| $(k,1)$，$k\ge3$ | $1$ | $\ge2$ | ✗（于是需要 §17–§19 的 Bézout 路线）|
| $(3,2)$ | $2$ | $2$ | **✓ 适用**（$c=2$ 也有线性可判的情形）|
| $(\rho,c)$ 一般 | $\le\min(c,\dim B)$ | $\rho-1$ | 当 $\min(c,\dim B)\ge\rho-1$ 时可取到 |

$$\boxed{\ \text{层判定} = \text{维数比较，}\textbf{只要}\ \dim\beta(\mathcal H)=\rho-1\ }$$

**注**：$b=\rho-1$ 是**可设计的**——$\mathcal H$ 是我们选的（$\dim\mathcal H=c$），所以只要 $\min(c,\dim B)\ge\rho-1$，就能挑出 $\mathcal H$ 使 $b=\rho-1$ ✓。
这意味着 **$c\ge\rho-1$ 的所有层都可能落在"线性可判"的区域**，而 $c<\rho-1$ 的层（含 $(k,1)$，$k\ge3$）不是。

### 21.4 对 $c\ge2$ 的意义

$(c\ge2)$ 层此前只有 $c\ge\max(c_0,1)$ 这个下界。本节给出：

1. **一个充分条件**：$\dim\beta(\mathcal H)=\rho-1$ 时该层（固定 $(\mathcal U,\mathcal H)$）的判定是线性代数 ✓ [已证]；
2. 剩下的量词只是"选 $\mathcal H$（维度 $c$、使 $\beta$ 的秩恰为 $\rho-1$）"——一个**秩条件**下的 Grassmannian 存在性问题；
3. 于是 $c\ge\rho-1$ 的层与 $(2,1)$ 同属"维数比较"一类，**不需要** Bézout/T11。

**未做**：把"选 $\mathcal H$"这件事也化成多项式判定（现在它还是一个 Grassmannian 上的秩条件存在性问题）。

### 20.6 更正：$(\mathrm{b})$ 其实是**自动的**（引用 [proof/5b_upper_bound/](../../../../../proof/5b_upper_bound/README.md)）

写 §20 时我把 $(\mathrm{b})$（"秩 $\le\rho$ 恒成立"）当成一个需要检验的条件。**这是多余的**：

**定理（5b 的上界，已证 + [Lean] + 数值）** 若 $(5a)$ 成立，则对一切 $\lambda$
$$\operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]\le\operatorname{rank}[\mathcal L;CA;C]=\rho+j .$$
对 $\mathcal J$ 取商即得
$$\operatorname{rank}Q_{\mathcal V}(\lambda)=\operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]-j\le\rho .$$

$$\boxed{\ \text{在 }(5a)\ \text{之下，}(\mathrm{b})\ \text{自动成立}\ }$$

于是 §20 的拆分退化成一句：

$$(5b)\iff(\mathrm{a})\iff k\times k\ \text{子式无公根}\iff\gcd=1 .$$

**这解释了旧归档里那句话**（[proof/5b_upper_bound/README.md](../../../../../proof/5b_upper_bound/README.md)）：
> "上界是 $(5a)$ 的推论，对一切 $\lambda$ 自动成立；它不提供任何硬度。**所有困难都在下界**。"

——我们的层程序重走了同一条路，并把它精确化为：**困难 = "无公根"这一开条件在 Grassmannian 上的存在性**（即 §17 的 Bézout 化与 T11）。

## 22. S1 区（$c\ge\rho-1$）：层判定塌成**一个等式条件**

> 本节把 [STRATEGY](../../../../../workspace/q1_false/STRATEGY_2026-10-28.md) 的 S1 第一步**做完**：
> 在 $\dim\beta(\mathcal H)=\rho-1$ 的区域里，"$\dim\mathrm{Bad}<\dim\mathcal A$"被算成一条**极简**的线性代数条件。

### 22.1 两个维数的显式公式

记 $m=\dim B$、$\mu:=\dim(B\cap\mathcal U)$、$\nu:=\dim(B\cap W_0)$，其中 $W_0=\operatorname{span}\beta(\mathcal H)$。

由 §21（$W_0=\operatorname{span}\beta(\mathcal H)$ 唯一，$\dim W_0=\rho-1$）：
$$\dim\mathcal A=\rho\,(j-m+\mu),\qquad \dim\mathrm{Bad}_\lambda=\rho\,(j-m+\nu)\quad(\text{每个 }\lambda),$$
因为两个集合的方向分别是 $\{\tau:\beta(\tau_i)\in\mathcal U\}$ 与 $\{\tau:\beta(\tau_i)\in W_0\}$，而
$$\dim\{\tau_i:\beta(\tau_i)\in \mathcal U\}=j-m+\dim(B\cap\mathcal U).$$

因为 $W_0\subseteq\mathcal U$，故 $\nu\le\mu$，且 $\mathrm{Bad}_\lambda\subseteq\mathcal A$ ✓。

### 22.2 关键的维数计数

$\mathrm{Bad}=\bigcup_{\lambda\in\mathbb C}\mathrm{Bad}_\lambda$ 是**一参数族**，故
$$\dim\mathrm{Bad}\ \le\ \dim\mathrm{Bad}_\lambda+1\ =\ \rho(j-m+\nu)+1 .$$
于是
$$\dim\mathrm{Bad}<\dim\mathcal A\ \Longleftarrow\ \rho(\mu-\nu)\ \ge\ 2 .$$
反过来，对**每个** $\lambda$ 都有 $\mathrm{Bad}_\lambda\subseteq\mathcal A$ 且 $\dim\mathrm{Bad}_\lambda=\dim\mathcal A$ 时 $\mathrm{Bad}_\lambda=\mathcal A$，故 $\mu=\nu\Rightarrow\mathrm{Bad}=\mathcal A$。

### 22.3 定理（$\mu>\nu$ 时可行）—— 严格证明

**定理 22.1** 设 $\dim\beta(\mathcal H)=\rho-1$（故 $\nu=\dim(B\cap W_0)=\rho-1$）且 $\mu=\dim(B\cap\mathcal U)>\nu$、$\rho\ge2$。
则 $\dim\mathrm{Bad}<\dim\mathcal A$，故该 $(\mathcal U,\mathcal H)$ **可行**（由定理 10.1）。

*证明*：令 $r:=\rho(\mu-\nu)\ge2$。令 $V:=\{(\tau,\lambda):\lambda u_i-r_i(\tau)\in W_0\ \forall i\}\subseteq\mathcal A\times\mathbb C$，
这是**代数簇**（每个条件是 $\lambda$ 线性、$\tau$ 仿射的方程）。对固定 $\lambda$，纤维 $V_\lambda=\mathrm{Bad}_\lambda$ 是 $\mathcal A$ 的仿射子集，维数
$$\dim V_\lambda=\rho(j-m+\nu)=\dim\mathcal A-r\quad(\text{或}\ -\infty\ \text{若空}).$$
故 $\dim V\le \dim\mathcal A-r+1$，于是
$$\dim\mathrm{Bad}=\dim\pi_{\mathcal A}(V)\le\dim V\le\dim\mathcal A-r+1<\dim\mathcal A\qquad(\text{因 }r\ge2).$$
由定理 10.1（$\mathrm{Bad}\subseteq\mathcal A$ 仿射），$\exists\tau\in\mathcal A\setminus\mathrm{Bad}$ ✓。$\square$

### 22.4 边界情形 $\mu=\nu$：**不是**自动不可行（更正）

写第一版时我断言"$\mu=\nu\Rightarrow\mathrm{Bad}=\mathcal A\Rightarrow$ 不可行"。**这一步是错的**：$\mu=\nu$ 时每个 $\mathrm{Bad}_\lambda$
要么**空**、要么等于 $\mathcal A$，故

$$\mathrm{Bad}\in\{\varnothing,\ \mathcal A\},\qquad \text{可行}\iff \mathrm{Bad}=\varnothing\iff\text{不存在让条件相容的 }\lambda .$$

也就是说：$\mu=\nu$ 时可行性退化成**一个一维相容性问题**（"是否有某个 $\lambda$ 使 $\lambda u_i+W_0$ 与 $T(u_i)+B$ 相交，$\forall i$"），
不能只靠维数判定。**这一段留作待做**。

### 22.5 结论（S1 的可靠部分）

$$\boxed{\ \dim(B\cap\mathcal U)\ \ge\ \rho\ \Longrightarrow\ \text{该 }(\mathcal U,\mathcal H)\ \text{可行}\ (\rho\ge2)\ }$$

于是**层级别的充分条件**是

$$\dim\{b\in B:\ T(b)\in B\}\ \ge\ \rho\ \Longrightarrow\ \text{第 }(\rho,c)\ \text{层可行}\ (c\ge\rho-1,\ \rho\ge2,\ \dim B\ge\rho-1).$$

$\mu=\rho-1$ 的层**可能**仍然可行（见 22.4），需要单独的一维相容性判定。

### 22.6 待核（诚实）

1. 22.4 的一维相容性问题需给出显式判据（它是 $\lambda$ 的一维问题，应当是线性代数）；
2. $\rho=1$ 的退化情形（$r=\mu-\nu\in\{0,1\}$）需单独处理；
3. 若 $\dim B<\rho-1$，则 $\nu<\rho-1$ 固定，定理 22.1 的形式不变（条件仍是 $\mu>\nu$）。

## 23. S1 区完成：$\mu=\nu$ 的边界情形也是**线性代数**

> 接 §22。那里只证了 $\mu>\nu$（$\Longrightarrow$ 可行），把 $\mu=\nu$ 留作"一维相容性问题"。
> **本节把它解掉**，于是 S1 区（$c\ge\rho-1$）的判定**完全确定**。

### 23.1 一维相容性的精确形状

设 $\mu=\nu$（即 $\dim(B\cap\mathcal U)=\dim(B\cap W_0)=\rho-1$），$V:=B+W_0$（固定子空间）。

**引理 23.1** $\mathrm{Bad}_\lambda\ne\varnothing\iff\forall i:\ \lambda u_i-\widetilde T(u_i)\in V$。

*证明*：$\mathrm{Bad}_\lambda\ne\varnothing\iff\forall i:\big(\lambda u_i-\widetilde T(u_i)+W_0\big)\cap B\ne\varnothing
\iff\forall i:\lambda u_i-\widetilde T(u_i)\in B-W_0=B+W_0=V$ ✓。$\square$

**引理 23.2** 每个
$$S_i:=\{\lambda\in\mathbb C:\ \lambda u_i-\widetilde T(u_i)\in V\}$$
是以下三种之一：$\varnothing$、单点、或整个 $\mathbb C$。

*证明*：把 $\lambda\mapsto\lambda u_i-\widetilde T(u_i)$ 看成过 $-\widetilde T(u_i)$、方向 $u_i$ 的仿射直线；
与子空间 $V$ 的交只能是空、单点（当 $u_i\notin V$）、或整条直线（当 $u_i\in V$ 且 $\widetilde T(u_i)\in V$）✓。$\square$

**定理 23.3** 设 $\mu=\nu$，$\rho\ge2$。则
$$\text{该 }(\mathcal U,\mathcal H)\ \text{可行}\iff \bigcap_{i=1}^{\rho}S_i=\varnothing .$$

*证明*：由 §22.4，$\mathrm{Bad}_\lambda$ 非空时其维数 $=\dim\mathcal A$，故 $\mathrm{Bad}_\lambda\in\{\varnothing,\mathcal A\}$；
于是 $\mathrm{Bad}=\varnothing$（即可行，因 $(5a)$ 给 $\mathcal A\ne\varnothing$）或 $\mathrm{Bad}=\mathcal A$（即不可行）。
再由引理 23.1，$\mathrm{Bad}\ne\varnothing\iff\exists\lambda\in\bigcap_i S_i$ ✓。$\square$

$$\boxed{\ (\mathcal U,\mathcal H)\ \text{可行}\iff\Big[\dim(B\cap\mathcal U)\ge\rho\Big]\ \vee\ \Big[\dim(B\cap\mathcal U)=\rho-1\ \wedge\ \bigcap_i S_i=\varnothing\Big]\ (\rho\ge2)\ }$$

**推论 23.4** 固定 $(\mathcal U,\mathcal H)$ 的层判定是 $O(n^3)$：算 $\dim(B\cap\mathcal U)$、每个 $S_i$、再看交是否空。
（每个 $S_i$ 的判定是解一个线性方程 $\lambda u_i\in\widetilde T(u_i)+V$，即 $u_i$ 是否在 $V$ 里、及 $\widetilde T(u_i)$ 的余项。）

### 23.2 层级别：$\exists(\mathcal U,\mathcal H)$

**定理 23.5** 设 $c\ge\rho-1$、$\rho\ge2$、$\dim B\ge\rho-1$。则第 $(\rho,c)$ 层可行，当且仅当下列之一成立：

$$\text{(A) }\ \exists\,\mathcal U\ (\dim\rho):\ \mathcal U\subseteq B,\ T(\mathcal U)\subseteq B ;$$
$$\text{(B) }\ \exists\,\mathcal U\ (\dim\rho),\ \exists\,\mathcal H\ (\dim c,\ \dim\beta(\mathcal H)=\rho-1):\ T(\mathcal U)\subseteq\mathcal U+B,\ \beta(\mathcal H)\subseteq\mathcal U,\ \bigcap_i S_i=\varnothing .$$

*证明*：$\mu\ge\rho$ 且 $\dim\mathcal U=\rho$ $\iff\mathcal U\subseteq B$，此时 $(5a)$ 即 $T(\mathcal U)\subseteq\mathcal U+B=B$ ✓；
$\mu=\rho-1$ 时用定理 23.3 ✓。（$\mu<\nu$ 不可能，因 $W_0\subseteq\mathcal U$。）$\square$

$$\boxed{\ \text{S1 区（}c\ge\rho-1\text{）的层判定 = 两个 Grassmannian 存在性条件的并，均为线性代数}\ }$$

### 23.3 待核（诚实）

1. (A) 是"在 $B$ 里找 $\rho$ 维 $T$-不变（模 $B$）子空间"，等价于 $\dim\{b\in B:T(b)\in B\}\ge\rho$ ✓（见 §22.5）；
2. (B) 里的 $\mathcal H$ 自由度：只要 $\dim B\ge\rho-1$ 且 $\mathcal U$ 含一个 $(\rho-1)$ 维、落在 $B$ 里的子空间即可取到 ✓；
3. (B) 的 $\bigcap_i S_i=\varnothing$ 依赖于 $\mathcal U$，尚未化成一个"关于 $\mathcal U$ 的秩/线性条件"——这是 S1 仅剩的一步。

### 23.4 关键简化：$W_0=B\cap\mathcal U$，故 $V=B$

在 (B) 里 $\dim(B\cap\mathcal U)=\rho-1$ 且 $\beta(\mathcal H)=W_0\subseteq\mathcal U$、$W_0\subseteq B$，故
$$W_0\ \subseteq\ B\cap\mathcal U\quad\text{且}\quad \dim(B\cap\mathcal U)=\rho-1=\dim W_0
\ \Longrightarrow\ W_0=B\cap\mathcal U .$$
于是 $V=B+W_0=B$ ✓ —— **$V$ 与 $\mathcal H$ 无关**。

**推论 23.6** $S_i=\{\lambda:\lambda u_i-\widetilde T(u_i)\in B\}$，且
$$\Lambda(\mathcal U):=\bigcap_{u\in\mathcal U}S(u)=\{\lambda:\lambda\mathcal U\subseteq \widetilde T(\mathcal U)+B\} .$$

*证明*：$S(u)$ 的定义是线性的；条件"对一组基成立"$\iff$"对全部 $u\in\mathcal U$ 成立" ✓。$\square$

**推论 23.7** $\Lambda(\mathcal U)$ 与 $\mathcal U$ 的基无关，且 $\Lambda(\mathcal U)$ 是 $\varnothing$、单点、或 $\mathbb C$ 之一。
具体地：若 $\mathcal U\subseteq B$ 则 $\Lambda(\mathcal U)=\mathbb C$（此时 (A) 已成立）；若 $\mathcal U\not\subseteq B$，取 $u\in\mathcal U\setminus B$，
则 $\Lambda(\mathcal U)$ 至多是单点，且
$$\Lambda(\mathcal U)\ne\varnothing\iff \widetilde T(u)\in B+\langle u\rangle .$$

**于是 (B) 的判定形状**：
$$\text{(B)}\iff\exists\,\mathcal U:\ T(\mathcal U)\subseteq\mathcal U+B,\quad \dim(B\cap\mathcal U)=\rho-1,\quad
\widetilde T(u)\notin B+\langle u\rangle\ (u\in\mathcal U\setminus B).$$

$$\boxed{\ \text{S1 的剩余步骤：把 (B) 化成"关于 }\mathcal U\text{ 的秩/线性条件"}$$

**待核**：(B) 是否**真的需要**——即是否存在实例 (A) 不成立而 (B) 成立？
若不存在（猜测：$T(\mathcal U)\subseteq\mathcal U+B$ 与 $\dim(B\cap\mathcal U)=\rho-1$ 已迫使 $\widetilde T(u)\in B+\langle u\rangle$），
则 S1 的判据就退化为 (A) 一条：$\dim\{b\in B:T(b)\in B\}\ge\rho$，完全不需要 Grassmannian 搜索 ✓。

## 24. S1 区**完成**：(B) 恒不成立，判据就是 (A)

§23.4 留了一个待核：**(B) 是否真的会发生？** 答案：**永不发生**。

### 24.1 定理

**引理 24.1** 设 $\dim(B\cap\mathcal U)=\rho-1$、$T(\mathcal U)\subseteq\mathcal U+B$，且 $u\in\mathcal U\setminus B$。则
$$\widetilde T(u)\in B+\langle u\rangle .$$

*证明*：由 $\dim(B\cap\mathcal U)=\rho-1$ 与 $u\notin B\cap\mathcal U$ 得 $\mathcal U=(B\cap\mathcal U)\oplus\langle u\rangle$。
$T(\mathcal U)\subseteq\mathcal U+B$ 给 $\widetilde T(u)=w+\lambda u+b$，其中 $w\in B\cap\mathcal U\subseteq B$、$b\in B$。
故 $\widetilde T(u)=\lambda u+(w+b)\in\langle u\rangle+B$ ✓。$\square$

**推论 24.2** 在 $\dim\beta(\mathcal H)=\rho-1$ 的假设下，$\Lambda(\mathcal U)\ne\varnothing$ 恒成立，故 $\mathrm{Bad}=\mathcal A$：
"容器维数恰好 $=\rho-1$"的 $(\mathcal U,\mathcal H)$ **一律不可行**。

*证明*：引理 24.1 + 推论 23.7（$\Lambda(\mathcal U)\ne\varnothing\iff\widetilde T(u)\in B+\langle u\rangle$）+ §23.1（$\Lambda\ne\varnothing\Rightarrow\mathrm{Bad}=\mathcal A$）。$\square$

**定理 24.3（S1 的最终判据，充要）** 设 $c\ge\rho-1$、$\rho\ge2$、$\dim B\ge\rho-1$。则第 $(\rho,c)$ 层可行
$$\iff\ \dim\{b\in B:\ T(b)\in B\}\ \ge\ \rho .$$

*证明*：
($\Leftarrow$) 取 $\rho$ 维 $\mathcal U\subseteq\{b\in B:T(b)\in B\}$，则 $\mathcal U\subseteq B$ 故 $\mu=\rho>\nu=\rho-1$，由定理 22.1 可行 ✓。
($\Rightarrow$) 设可行。若某可行解有 $\dim(B\cap\mathcal U)\ge\rho$，则 $\mathcal U\subseteq B$ 且 $T(\mathcal U)\subseteq\mathcal U+B=B$，故 $\mathcal U$ 落在 $\{b\in B:T(b)\in B\}$ 里 ✓。
否则所有可行解的 $\dim(B\cap\mathcal U)=\rho-1$，但由推论 24.2 它们全都不可行 ✗ 矛盾 ✓。$\square$

$$\boxed{\ c\ge\rho-1\ \text{的整片层}\ \Longleftrightarrow\ \dim\{b\in B:T(b)\in B\}\ge\rho\quad(O(n^3))\ }$$

### 24.2 这个结论的力量与边界

1. **覆盖面**：$c\ge\rho-1$ 的**全部**层（含 $(2,1)$、$(3,2)$、一切 $c$ 足够大的层）都用一条公式判定 ✓；
2. **与 $(2,1)$ 已知结果一致**：$\rho=2$ 时判据为"$\{b\in B:T(b)\in B\}$ 至少 2 维" ✓（即 $\mu\ge2$）✓；
3. **边界**：$c<\rho-1$（例如 $(k,1)$，$k\ge3$）时容器**不唯一**，本节不适用 ✗ —— 那是 S2/L2 的地盘；
4. **注意**：$\dim B<\rho-1$ 时无法取到 $\dim\beta(\mathcal H)=\rho-1$，本节结论不直接适用（但那时的 $\nu<\rho-1$，
   按 §22.1 的 $\mu>\nu$ 论证仍给"$\mu>\nu\Rightarrow$ 可行"，需另做）。

### 24.3 待核（诚实）

- 定理 24.3 的 ($\Rightarrow$) 方向依赖"可行 ⟹ 存在 $\dim(B\cap\mathcal U)\ge\rho$"的二分（$\mu=\rho-1$ 一律不可行）。
  这里用了 $\nu=\rho-1$（即刻意取 $\dim\beta(\mathcal H)=\rho-1$）。若某个可行解用的是**更小的** $\nu$，需确认
  $\mu>\nu$ 的情形仍被 ($\Leftarrow$) 覆盖——由 §22.1，$\mu>\nu$ 直接给可行，而 $\mu>\nu$ 且 $\nu<\rho-1$ 时
  "$\mathcal U\subseteq B$"不一定成立 ✗ ⟹ **这一支需要单独处理**（见 §24.4）。

### 24.4 （**已被 §25 取代**）$\nu<\rho-1$ 时的补充条件

若 $\dim\beta(\mathcal H)=\nu<\rho-1$，则由 §22.1（$r=\rho(\mu-\nu)\ge2$）得：**只要 $\mu>\nu$ 就可行**。
于是完整的 S1 判据应为

$$\text{可行}\iff \Big[\dim\{b\in B:T(b)\in B\}\ge\rho\Big]\ \vee\ \Big[\exists\,\mathcal U,\mathcal H:\ \nu<\rho-1,\ \mu>\nu\Big].$$

右支是否可能（即"容器维数不足 $\rho-1$ 也能救活这一层"）**尚未定**——这是 S1 真正剩下的最后一小块。

> **更正（见 §25）**：本小节的"$\mu>\nu\Rightarrow$ 可行"是**错的**——§22.1 的维数公式只在容器唯一时成立；
> $\nu<\rho-1$ 时容器族更大，$\mathrm{Bad}$ 更大，"$\mu>\nu$"不能保证可行。§25 用**单调性**（引理 25.1）把它修正为
> "取最大 $\nu$ 最优"，从而给出定理 25.3。

## 25. S1 区彻底完成：单调性 + 全维数覆盖

§24.4 留了一个分支（$\nu<\rho-1$）并给了一个**错误**的方向判断（"$\mu>\nu$ 就可行"）。
错因：§22.1 的 $\dim\mathrm{Bad}$ 公式是在**容器唯一**（$\dim\beta(\mathcal H)=\rho-1$）时成立的；
$\nu<\rho-1$ 时容器族**更大**，$\mathrm{Bad}$ 也更大 ✗。本节用单调性把这一支彻底关掉。

### 25.1 单调性引理

**引理 25.1** 固定 $\mathcal U$。若 $\beta(\mathcal H_1)\subseteq\beta(\mathcal H_2)$（同样的 $\mathcal U$），则
$$\mathcal H_2\ \text{可行}\ \Longleftarrow\ \mathcal H_1\ \text{可行}.$$

*证明*：$(5b)$ 失败 $\iff\exists\lambda$ 与容器 $W_0$（$\dim\le\rho-1$、$\supseteq\beta(\mathcal H)$、装下全部行）✓（引理 14.1）。
$\beta(\mathcal H_1)\subseteq\beta(\mathcal H_2)$ 时，$\mathcal H_2$ 的任一容器也是 $\mathcal H_1$ 的容器，故
"$\mathcal H_2$ 失败 $\Rightarrow$ $\mathcal H_1$ 失败"，取逆否 ✓。$\square$

**推论 25.2** 在 $(5a)$ 允许的范围内，**取 $\dim\beta(\mathcal H)$ 最大**（即 $=\min(c,\dim B)$）是最优选择。

### 25.2 全维数覆盖的判据

**定理 25.3（S1 的最终判据）** 设 $c\ge\rho-1$、$\rho\ge2$。则第 $(\rho,c)$ 层可行
$$\iff\ \dim\{b\in B:\ T(b)\in B\}\ \ge\ \rho .$$

*证明*：
由推论 25.2，取 $\nu=\min(c,\dim B)$ 最优。
- **情形 $\dim B\ge\rho-1$**（故 $\nu=\rho-1$）：即定理 24.3 ✓。
- **情形 $\dim B<\rho-1$**（故 $\nu=\dim B=m$）：因 $B\cap\mathcal U\subseteq B$，$\mu=\dim(B\cap\mathcal U)\le m=\nu$，
  于是由 §22.2 的"$\mu=\nu\Rightarrow\mathrm{Bad}=\mathcal A$"得**不可行** ✓；而 $\dim B<\rho$ 时
  $\dim\{b\in B:T(b)\in B\}\le\dim B<\rho$，判据也为假 ✓ 一致。$\square$

$$\boxed{\ \text{对一切 }c\ge\rho-1,\ \rho\ge2:\quad \text{第 }(\rho,c)\ \text{层可行}\iff\dim\ker\big((I-P_B)T|_{B}\big)\ge\rho\ }$$

其中 $\{b\in B:T(b)\in B\}=\ker\big((I-P_B)T|_B\big)$、$P_B$ 是到 $B$ 的投影 ✓ —— **一次 $O(n^3)$ 计算**。

### 25.3 意义与边界

| 项 | 状态 |
|---|---|
| $c\ge\rho-1$ 的**全部**层 | **已定**（定理 25.3，充要，纸面证明）✓ |
| 与 $(2,1)$ 已知结果 | 一致（$\rho=2$ 时判据为"$\{b\in B:T(b)\in B\}$ 至少 2 维"）✓ |
| $c<\rho-1$ 的层（含 $(k,1),k\ge3$）| **不适用**：容器不唯一，$\mathrm{Bad}$ 是投影型 ✗ ⟹ 属 S2/L2 |

**一句话**：$c$ 足够大（$c\ge\rho-1$）时，层判定**塌成一条维数公式**；难的是 $c$ 小、容器不唯一的情形。

> ## ⛔ §22–§26 已被**反驳**（2026-10-28 深夜）
>
> 反例（精确、可复核）：[counterexample_s1.json](counterexample_s1.json)，说明见
> [proof/refuted/S1_criterion_iff.md](../../../../../proof/refuted/S1_criterion_iff.md)：$n{=}4,\rho{=}2,c{=}1$ 时
> 判据（$\dim K\ge\rho$）为**假**而 $(5a)\wedge(5b)$ 为**真** ⟹ 定理 24.3/25.3/26.2 的"(⟹)"方向错误。
> **幸存的只有**：定理 22.1（充分方向）、引理 25.1（单调性）、推论 23.6/23.7、docs/02 A.0。
>
> ## ⚠️ §22–§25 待重审（2026-10-28 晚，已被上面取代）
>
> 这四节把 $(5a)$ 写成了 $T(\mathcal U)\subseteq\mathcal U+B$，但**正确形式是 $T(\mathcal U)\subseteq\mathcal U$**
> （[docs/02 A.0](../../../../../docs/02_theorems_proven.md)）。$U+B$ 是 conditioned invariance（$P$ 递归用的），比 $(5a)$ 弱。
> 另外 [verify_s1.py](verify_s1.py) 的抽象模型在修正 $\mathrm{cond\_5b}$（两个方向都查）后仍有 17 处不一致，
> 说明抽象模型不是真实几何的有效代理（它不自动满足 5b_upper_bound）。
>
> **结论：§22–§25 的定理（尤其定理 24.3 / 25.3）目前标记为 [待核]，不得引用。**
>
> **v2 验证结果（2026-10-28 晚）**：[verify_s1.py](verify_s1.py) 已按正确的 $(5a)$（$T(\mathcal U)\subseteq\mathcal U$）
> 重建抽象模型，并把 $\tau$ 限制在 $\mathcal A$ 内、两个方向都查秩条件。结果仍与定理**系统性不一致**：
> 判据为真的 112 例里 80 例"不可行"、判据为假的 19 例里 11 例"可行"。
> 对一个 $\rho=2,c=1$ 的手算例子（$T|_{\mathcal U}=\mathrm{id}$、$\tau=0$）可以直接看到
> $\lambda u-u$ 在 $\lambda=1$ 处退化 ⟹ $(5b)$ 应当失败；但脚本判定"可行" ⟹ **脚本的 $\mathrm{cond\_5b}$ 仍有 bug**
> （最可能在 $\mathrm{minors\_pencil}$ 的 $(\rho+1)$ 子式分支或行列式展开）。
>
> **下一步（明确）**：先用一个 $3\times3$ 的手算例子把 $\mathrm{cond\_5b}$ 校准，再重跑；
> 在脚本校准前，§22–§25 **一律视为猜想**。
>
> **更新（校准结果）**：`cond_5b` 已用两个手算例子校准通过——
> *(a)* 全退化例子判 False ✓；*(b)* 正例（两行互为"λx−y"、第三行 −e₁，3×3 子式恒零）判 True ✓。
> 所以 bug 不在 `cond_5b`，而在脚本的**实例构造**（`T`/`U`/`A` 的生成）或定理本身。
> 手算最小反例（$B=\langle e_1,e_2\rangle$、$U=\langle e_1,e_3\rangle$、$T=I$、$\tau\in\mathcal A$）直接验证：
> $\lambda=1$ 时三行都落在 $W_0=\langle e_1\rangle$ 里 ⟹ 秩 1 < 2 ⟹ $(5b)$ 失败 ⟹ **不可行** ✓ 与定理一致。
> 故定理仍未被推翻，但**验证脚本必须先修好构造**才能作为证据。
> 正确做法：在**真实实例** $(A,C,L_0)$ 上验证（用 `tools/verification/c164_trusted_baseline.py` 的精确判据），
> 或按 $T(\mathcal U)\subseteq\mathcal U$ 重做推导。

## 26. S1 判据的**具体形式**（修正 §25.3 遗漏 $U_0$）

§25.3 把判据写成"$\dim\{b\in B:T(b)\in B\}\ge\rho$"——**漏了 $U_0=\pi(\operatorname{row}L_0)\subseteq U$**
（那是 $V\supseteq\operatorname{row}L_0$ 与 $(5a)$ 的一部分）。本节把它补上，并化成**只用 $(A,C,L_0)$ 的具体算式**。

### 26.1 具体化

记 $\mathcal J=\operatorname{row}[C;CA]$、$j=\dim\mathcal J$，
$$S:=(\mathcal J+\mathcal J A)\cap A^{-1}(\mathcal J+\mathcal J A),\qquad K:=\pi(S)=\{b\in B:T(b)\in B\}.$$

*（$\pi^{-1}(B)=\mathcal J+\mathcal J A$，因为 $B=\pi(\mathcal J A)$ ✓；于是 $T(b)\in B\iff b$ 的提升 $x$ 满足 $xA\in\mathcal J+\mathcal J A$ ✓。）*

**命题 26.1** $\dim K=\dim S-j$，且 $U_0\subseteq K\iff \operatorname{row}L_0\subseteq S+\mathcal J$。

*证明*：$\mathcal J\subseteq S$（$\mathcal J\subseteq\mathcal J+\mathcal J A$ 且 $\mathcal J A\subseteq\mathcal J+\mathcal J A$ 故 $\mathcal J\subseteq A^{-1}(\mathcal J+\mathcal J A)$ ✓），故 $\dim K=\dim S-j$ ✓；
$\pi(x)\in\pi(S)\iff x\in S+\mathcal J$ ✓。$\square$

### 26.2 修正后的判据

**命题 26.2（S1 判据，具体形式；[待核]）** 设 $c\ge\rho-1$、$\rho\ge2$、$\dim B\ge\rho-1$。则第 $(\rho,c)$ 层可行
$$\iff \dim S-j\ \ge\ \rho\quad\text{且}\quad \operatorname{row}L_0\ \subseteq\ S+\mathcal J .$$

*证明思路*：
($\Leftarrow$) 取 $\rho$ 维 $\mathcal U\subseteq K$ 且 $U_0\subseteq\mathcal U$（由第二条 ✓ 存在），任一提升给 $\mathcal V\supseteq\operatorname{row}L_0$；
由 $\mathcal U\subseteq K$ 得 $T(\mathcal U)\subseteq\mathcal U\subseteq B$，故 $(5a)$ ✓；又 $\mu=\dim(B\cap\mathcal U)=\rho>\nu=\rho-1$，
由**定理 22.1** 得 $(5b)$ 可满足 ✓。
($\Rightarrow$) 若可行，取 $\mathcal U=\pi(\mathcal V)$。若 $\dim(B\cap\mathcal U)=\rho-1$，由**推论 24.2**（$\Lambda(\mathcal U)\ne\varnothing$）得不可行 ✗ 矛盾；
故 $\dim(B\cap\mathcal U)=\rho$，即 $\mathcal U\subseteq B$，于是 $T(\mathcal U)\subseteq\mathcal U\subseteq B$，故 $\mathcal U\subseteq K$ ✓，
而 $U_0\subseteq\mathcal U\subseteq K$ ✓。$\square$

### 26.3 状态与验证

| 项 | 状态 |
|---|---|
| 命题 26.1（具体化）| [已证] |
| 命题 26.2 的 ($\Leftarrow$) | 依赖定理 22.1（[已证]）✓ |
| 命题 26.2 的 ($\Rightarrow$) | 依赖推论 24.2（[待核]）|
| 真实实例验证 | [verify_s1_real.py](verify_s1_real.py) —— **仍有 bug**：`data()` 里 $S$ 的计算返回空集（导致 $\dim K=-2$ 这种不可能值），尽管手工核对 $\mathcal J\subseteq$ 预像 $\cap\ (\mathcal J+\mathcal J A)$ 成立。已定位到 `rbasis`/`inspan` 的组合行为，下一步用单元测试逐个校准（对 $S$ 的预像计算本身已手算核对正确）|

> **诚实标注**：命题 26.2 仍标 **[待核]**。它比 §25.3 强（补了 $U_0$ 条件），且**化了具体算式**，
> 可以直接在 $(A,C,L_0)$ 上算 $S$、$K$、$U_0$ 来检验，不必再引入抽象模型。

## 27. T11 的证明：引理 17.2 对一切 $m$ 成立（L2 的缺口闭合）

> 本节给 [§18](#18-引理-172-的证明m2-完整mge3-待补) 里挂着的 $m\ge3$ 情形一个**完整证明**。
> 关键是**单调性**：一旦某个 $D$ 上行满秩，更大的 $D$ 自动行满秩。

### 27.1 设定

$p_1,\dots,p_m\in\mathbb C[\lambda]$、$\deg\le d$、$\gcd=1$。记
$$\Phi_D:\bigoplus_{j=1}^m\mathbb C[\lambda]_{\le D}\to\mathbb C[\lambda]_{\le d+D},\qquad (a_j)\mapsto\sum_j a_jp_j .$$

**引理 27.1（单调性）** 若 $\Phi_D$ 行满秩（即满射），则 $\Phi_{D+1}$ 也满射。

*证明*：$\operatorname{im}\Phi_{D+1}\supseteq\operatorname{im}\Phi_D=\mathbb C[\lambda]_{\le d+D}$，且
$\lambda\cdot\operatorname{im}\Phi_D\subseteq\operatorname{im}\Phi_{D+1}$（把每个 $a_j$ 换成 $\lambda a_j$，次数 $\le D+1$）✓。
故 $\operatorname{im}\Phi_{D+1}\supseteq\mathbb C[\lambda]_{\le d+D}+\lambda\mathbb C[\lambda]_{\le d+D}=\mathbb C[\lambda]_{\le d+D+1}$ ✓。$\square$

### 27.2 主证明（对 $m$ 归纳）

**定理 27.2（次数必须是**实际**最大次数）** 设 $d_*:=\max_j\deg p_j$，且 $\gcd(p_1,\dots,p_m)=1$。则存在 $D\le 2d_*(m-1)$ 使 $\Phi_D$ 满射（此处 $\Phi_D$ 的目标空间取 $\mathbb C[\lambda]_{\le d_*+D}$）。

> **⚠️ 2026-10-30 更正（专家指出、已核实）**：若把 $d$ 换成**松的**上界而不是 $d_*$，结论**不成立** ✗。
> 反例：$p_1=1,\ p_2=2$（实际次数 0）、取上界 $d=1$。则对任意 $D$，$\operatorname{im}\Phi_D\subseteq\mathbb C[\lambda]_{\le D}$，
> 而目标空间 $\mathbb C[\lambda]_{\le D+1}\ni\lambda^{D+1}$ ⟹ **永不**满射 ✗（即使 $\gcd=1$）。
> 同理，"$m=2$ 用 Sylvester 矩阵"这一步也要求用**实际**次数构造 Sylvester 矩阵 ✗。

*证明*：对 $m$ 归纳。

- **$m=1$**：$\gcd(p_1)=1$ 故 $p_1$ 为非零常数，$\Phi_D$ 显然满射（$D\ge0$）✓。
- **$m=2$**：$\Phi_{d-1}$ 就是经典 **Sylvester 矩阵**（方阵，$2d\times2d$），其行列式为 $\operatorname{Res}(p_1,p_2)\ne0$ ✓
  故满射 ✓（取 $D=d-1$）。
- **$m\ge3$**：设 $g=\gcd(p_1,p_2)$（$\deg g\le d$）。族 $F'=(g,p_3,\dots,p_m)$ 有 $m-1$ 个元素、
  $\gcd=1$、次数 $\le d$，故由归纳假设存在 $D'$ 使 $\Phi^{F'}_{D'}$ 满射。
  由引理 27.1，$\Phi^{F'}_D$ 对一切 $D\ge D'$ 满射。
  取 $D:=D'$，令 $t$ 为任意次数 $\le d+D$ 的多项式；由 $F'$ 的满射性，$t=a\,g+\sum_{j\ge3}a_jp_j$，$\deg a,\deg a_j\le D$ ✓。
  又由 $m=2$ 情形（Bezout）$g=c_1p_1+c_2p_2$，$\deg c_i\le d-1$ hmm — 取 $\deg c_i\le d$ 即够 ✓。
  于是
  $$t=(ac_1)p_1+(ac_2)p_2+\sum_{j\ge3}a_jp_j,\qquad \deg(ac_i)\le D+d .$$
  即 $\Phi^{F}_{D+d}$ 满射 ✓。由引理 27.1 得 $\Phi^F_{D''}$ 对一切 $D''\ge D+d$ 满射 ✓。

取 $D_m:=2d(m-1)$ 即得所 claimed 的界 ✓。$\square$

**推论 27.3（引理 17.2 完全版）** 若 $\gcd(p_1,\dots,p_m)=1$，则存在 $D_0\le 2d(m-1)$ 使 $D\ge D_0$ 时 $\Phi_D$ 行满秩。
（这正是 §17 需要的那条，之前标 [待补]。）

### 27.3 后果：$(k,1)$ 与 $c=1$ 的层判定闭合

把推论 27.3 代入 §17 的 Bézout 线性化：

$$\text{层可行}\iff\exists\tau\in\mathcal A:\ \text{某个极大子式 }\Delta\ \text{在}\ \mathcal A\ \text{上不恒为零}$$

于是 $c=1$、任意 $k=\rho$ 的层判定都是"**选一个极大子式、做一次系数比较**"——**有限**判据 ✓；只有 $\rho$ 固定时才是多项式 ✗（见 §17 的更正面）。

$$\boxed{\ \text{§17 的 Bézout 路线在 }c=1\text{ 时完全闭合（定理 27.2 + 推论 27.3）}\ }$$

### 27.4 诚实标注

1. 定理 27.2 的界 $2d(m-1)$ 只是"存在性"的宽松界，未优化；
2. 归纳步里 $\deg c_i\le d$ 而非 $d-1$ 是故意的（少一次 bookkeeping），不影响结论；
3. **尚未 Lean 化**；§27 的证明是纸面的（[已证] 等级），下一步可考虑形式化"单调性"与 Sylvester 情形。

## 28. 现状汇总：$c=1$ 一层的判定**已经"半可判"**

把 §17、§27 与 §22–§26（已反驳部分除外）放在一起，$c=1$（任意 $\rho$）这一层的精确状态是：

### 28.1 已解决的部分：$\tau$ 量词（**已消掉**）

对**固定** $(\mathcal U,\mathcal H)$：
$$\text{可行}\iff\exists\tau\in\mathcal A:\ \gcd\{\text{全部 }\rho\times\rho\text{ 子式}\}=1
\iff\exists D\ \exists\text{极大子式 }\Delta\text{ of }\Phi_D:\ \Delta|_{\mathcal A}\not\equiv0 .$$
（第一步是 §20 的 $\gcd$ 判据；第二步是 §17 的 Bézout 线性化 + §27 的定理 27.2。）
"$\Delta$ 在仿射集 $\mathcal A$ 上是否恒零"是**系数比较** ⟹ **有限判据** ✓（多项式性只在 $\rho$ 固定时成立 ✗，见 §17 的更正面）。

### 28.2 未解决的部分：$\exists(\mathcal U,\mathcal H)$（Grassmannian）

层可行 $=\exists(\mathcal U,\mathcal H)$ 满足上述 ✓。已知：

| 情形 | 结论 | 位置 |
|---|---|---|
| $(2,1)$（$\rho=2,c=1$）且 $w\ne0$ | 完全可判（维数比较/仿射坏集）| §9–§13 [已证] |
| $(2,1)$ 且 $w=0$ | 恒不可行（首一二次必有根）| §9.12 [已证] |
| $\dim(B\cap\mathcal U)\ge\rho$ | 可行（充分）| 定理 22.1 [已证] |
| $\dim K\ge\rho$ 且 $U_0\subseteq K$ | 可行（充分，$K=\{b\in B:T(b)\in B\}$）| §25/§26 + 22.1 |
| "充要 $\iff\dim K\ge\rho$" | **错**（精确反例）| [proof/refuted/S1_criterion_iff.md](../../../../../proof/refuted/S1_criterion_iff.md) |

### 28.3 精确的待解问题（$c=1$）

> **Q-C1**：给定 $(A,C,L_0)$ 与 $\rho$，判定"$\exists\mathcal V\ (\dim\pi\mathcal V=\rho,\ \dim(\mathcal V\cap\mathcal J)=1,\ \mathcal V\supseteq\operatorname{row}L_0)$ 满足 $(5a)\wedge(5b)$"
> 是否多项式时间可判？

- 由 §28.1，**给定 $\mathcal V$ 时**的验证是多项式 ✓；
- 缺的是**搜索**（Grassmannian）✗ —— 这正是 §19–§22 里"容器不唯一"的那一支 ✗。

$$\boxed{\ \text{$c=1$ 的难度}=\text{"Grassmannian 上的 $\exists$ + 代数条件"}；\text{而 }\tau\text{ 已不成问题}\ }$$

### 28.4 诚实标注

本节只是**汇总**，不含新证明。$q1$ 仍开放；但"$\tau$ 量词已被消掉、$\gcd$ 判据可多项式执行"这一点，
把 $q1$ 的难点**唯一地**定位到了 Grassmannian 搜索上 ✓。

### 27.5 端到端检验（验证 ≠ 证明）

[verify_bezout_equivalence.py](verify_bezout_equivalence.py) 在**随机仿射族**上直接对拍两条判据：

$$(\mathrm{i})\ \exists\tau:\ \gcd(p_1(\tau,\cdot),\dots,p_m(\tau,\cdot))=1
\qquad\text{vs}\qquad
(\mathrm{ii})\ \exists D:\ \Phi_D(\tau)\ \text{在一般 }\tau\ \text{处行满秩}$$

| 样本 | 一致 | 不一致 |
|---|---|---|
| 300（$m\in\{2,3\}$，$d\in\{1,2\}$，$j\in\{1,2\}$）| **300** | **0** |

**局限（诚实）**：本测试取 $\mathcal A=\mathbb R^j$（无仿射约束）；带仿射约束的 $\mathcal A$ 情形
等价于"$\Delta|_{\mathcal A}\not\equiv0$"，那正是 §17 陈述的形式，**未在测试中覆盖**。

### 27.6 带仿射约束的端到端检验

[verify_bezout_affine.py](verify_bezout_affine.py)：把 $\mathcal A$ 取成一条**仿射直线** $\tau(s)=\tau_0+s\,d$，
直接对拍

$$(\mathrm{i})\ \exists s:\ \gcd=1\qquad\text{vs}\qquad
(\mathrm{ii})\ \exists D:\ \Phi_D(\tau(\cdot))\ \text{在}\ \mathbb Q(s)\ \text{上行满秩}.$$

| 样本 | 一致 | 不一致 |
|---|---|---|
| 40（$m\in\{2,3\}$、$d\in\{1,2\}$）| **40** | **0** |

这补上了 §27.5 的缺口（那里 $\mathcal A=\mathbb R^j$ 无约束）✓。
**局限**：$\mathcal A$ 取的是直线（1 维）而非一般的仿射子空间；$\dim\mathcal A\ge2$ 的情形未覆盖。

## 29. 修正后的**固定** $(\mathcal U,\mathcal H)$ 判据：$c\ge\rho-1$ 且 $\dim\beta(\mathcal H)=\rho-1$

> §22–§26 的错误在于把这条**固定 $(\mathcal U,\mathcal H)$** 的判据推广到"层级别"并声称是充要 ✗。
> 本节只把**固定的**情形写干净——它是真的，而且是 $O(n^3)$ 的。

### 29.1 陈述与证明

**定理 29.1** 设 $\rho\ge1$、$c\ge\rho-1$、$\dim\beta(\mathcal H)=\rho-1$（故 $W_0:=\beta(\mathcal H)$ 是 $\rho-1$ 维），
$\mathcal U=\pi(\mathcal V)$、$\mathcal A=\{\tau:\beta(\tau_i)\in B\cap\mathcal U\ \forall i\}$，并设 $(5a)$ 成立（故 $\beta(\mathcal H)\subseteq\mathcal U$）。
定义
$$E:=\{(\tau,\lambda)\in\mathcal A\times\mathbb C:\ \lambda u_i-\widetilde T(u_i)-\beta(\tau_i)\in W_0\ \ \forall i\},\qquad \mathrm{Bad}:=\pi_\tau(E).$$

则

$$\textbf{(a)}\ E\ \text{是仿射的},\quad \mathrm{Bad}\ \text{是仿射的},\quad \mathrm{Bad}\subseteq\mathcal A;\qquad
\textbf{(b)}\ \text{该 }(\mathcal U,\mathcal H)\ \text{可行}\iff\dim\mathrm{Bad}<\dim\mathcal A .$$

*证明*：
**(a)** $E$ 由 $\tau$ 的线性条件与 $\lambda$ 的线性条件给出 ⟹ 仿射 ✓；仿射集在线性映射 $\pi_\tau$ 下的像仍仿射 ✓。
$\mathrm{Bad}\subseteq\mathcal A$：若 $(\tau,\lambda)\in E$，则 $\beta(\tau_i)=\lambda u_i-\widetilde T(u_i)-w_i$，其中 $\lambda u_i-\widetilde T(u_i)\in\mathcal U$（由 $(5a)$ ✓）且 $w_i\in W_0\subseteq\mathcal U$ ✓，故 $\beta(\tau_i)\in\mathcal U$ ✓，即 $\tau\in\mathcal A$ ✓。
**(b)** 由引理 14.1，$(5b)$ 失败 $\iff\exists\lambda$ 与容器 $W$（$\dim W\le\rho-1$、$\beta(\mathcal H)\subseteq W$、装下全部行）。
但 $\dim W_0=\rho-1$ 且 $W_0\subseteq W$ 且 $\dim W\le\rho-1$ ⟹ $W=W_0$ **唯一** ✓。
故失败 $\iff\exists\lambda$ 使行落进 $W_0$ $\iff\pi_\tau(E)\ne\varnothing$ 且 … hmm——准确地说：
失败 $\iff\exists\tau\in\pi_\tau(E)$（把"$\tau$ 处 $\exists\lambda$"记成 $\tau\in\mathrm{Bad}$）✓ ⟹ 失败 $\iff\mathrm{Bad}\ne\varnothing$。
于是可行 $\iff\mathrm{Bad}=\varnothing$；而 $\mathrm{Bad}$ 仿射且 $\mathrm{Bad}\subseteq\mathcal A$，故
$$\mathrm{Bad}=\varnothing\ \text{或}\ \dim\mathrm{Bad}\le\dim\mathcal A-1
\iff\dim\mathrm{Bad}<\dim\mathcal A .$$
（约定 $\dim\varnothing=-\infty$；$\mathcal A\ne\varnothing$ 由 $(5a)$ ✓。）$\square$

### 29.2 与 §22–§26 的区别（务必分清）

| | 定理 29.1 | §22–§26（已反驳）|
|---|---|---|
| 对象 | **固定** $(\mathcal U,\mathcal H)$ | 层级别 $\exists(\mathcal U,\mathcal H)$ |
| 假设 | $\dim\beta(\mathcal H)=\rho-1$ | 同（但被误用）|
| 结论 | 固定 $(\mathcal U,\mathcal H)$ 的判据 ✓ | 声称层级别是充要 ✗ |

$$\boxed{\ \text{定理 29.1 是"验证器"，不是"搜索器"：给定 }(\mathcal U,\mathcal H)\text{ 后它 } O(n^3)\text{ 决定可行性}\ }$$

### 29.3 诚实标注

- 定理 29.1 的证明只用了：(i) 仿射集在线性映射下的像仍仿射 ✓；(ii) 容器唯一 ✓；(iii) 仿射集的维数比较 ✓ —— 三处都很短 ✓；
- **它不解决** 层级别的 $\exists(\mathcal U,\mathcal H)$ ✗ —— 那仍是 Q-C1 ✓；
- 数值复核：[verify_29_1.py](verify_29_1.py) —— **构造式**检验（不是随机采样）：
  $\mathcal U=\langle e_1,\dots,e_\rho\rangle$、$W_0$ 取 $\mathcal U$ 内的**随机** $(\rho-1)$ 维子空间、
  $T$ 在 $\mathcal U$ 的坐标基上对角、$\beta:\mathbb C^{\rho-1}\to W_0$ 取同构。于是 $(5a)$ 自动成立、秩上界自动成立。
  对每个实例在 $\mathcal A$ 上抽 12 个 $\tau$，看是否出现"mix"（定理 29.1 预测**不会**）。

$$\textbf{结果：200 个实例 —— 全可行 110、全不可行 90、mix 0}\ \checkmark$$

（若 $W_0$ 取成坐标超平面，则 200/200 全不可行 —— 这解释了为什么早期随机抽样看不到可行样本 ✗，也说明**构造**是必要的 ✓。）

## 30. 层判定是**可判定的**（有限签名分解），但复杂度仍未知

> 本节给一个**可证但有局限**的结论：把层判定化成有限多个"带指定秩签名"的存在性问题。
> 它的价值是**可判定性**（Q-C1 不是不可判定的），缺点是**不给多项式算法** ✗。

### 30.1 层判定只依赖有限多个整数

固定 $(\rho,c)$。对候选 $\mathcal V=\operatorname{row}L$（$\dim\mathcal V=\rho+c$，$\mathcal V\supseteq\operatorname{row}L_0$）定义**签名**
$$\Sigma(\mathcal V):=\big(\operatorname{rank}[L;CA;C],\ \operatorname{rank}[L;\mathcal J],\
\operatorname{rank}[LA;L;CA;C],\ \operatorname{rank}[\lambda L-LA;CA;C]\ (\lambda\ \text{符号}),\
\operatorname{rank}[H A;\mathcal J],\ \ldots\big)$$
即所有出现过的、由 $L$（与 $L_0$、$A$、$C$ 的固定数据）拼出的矩阵的秩。

**引理 30.1** 以下每条都只是 $\Sigma$ 的函数：
$$\rho=\dim\pi(\mathcal V),\quad c=\dim(\mathcal V\cap\mathcal J),\quad \nu=\dim\beta(\mathcal H),\quad
\dim\mathcal A,\quad \dim\mathrm{Bad}.$$
*证明*：$\rho=\operatorname{rank}[L;CA;C]-j$、$c=\dim L+j-\operatorname{rank}[L;\mathcal J]$ ✓；
$\nu=\operatorname{rank}[HA;\mathcal J]-j$ ✓；而 $\mathcal A$ 与 $\mathrm{Bad}$ 的方向空间都由 $\beta$ 与 $\widetilde T$ 的像给出，
其维数是上述秩的显式组合 ✓（§22.1 的公式）；$\mathrm{Bad}$ 仿射（定理 29.1）时 $\dim\mathrm{Bad}$ 亦然 ✓。$\square$

**推论 30.2** 层判定 $=\exists\mathcal V$ 使 $\Sigma(\mathcal V)\in\mathbb N^{k}$ **取某个有限集合** $S$ 里的值。
（因 $\Sigma$ 的各分量有界 ✓。）

### 30.2 可判定性

**定理 30.3** 对每个固定的 $(\rho,c)$，层判定可判定（在可计算意义下）。

*证明*：由推论 30.2，层判定是有限个命题
$$P_\sigma:=``\exists\mathcal V:\ \Sigma(\mathcal V)=\sigma\ \text{且}\ (5a)\ \text{且}\ \nu=\rho-1\ \text{且}\ \dim\mathrm{Bad}<\dim\mathcal A"$$
的析取 ✓。每个 $\Sigma(\mathcal V)=\sigma$ 与 $(5a)$ 都是 $\mathcal V$ 的**秩条件**（多项式方程与 $\ne0$ 条件）✓，
故 $P_\sigma$ 是 $\mathbb C$ 上一个**构造ible 集**的非空性问题 ✓ —— 由 Chevalley–Tarski（$\mathbb C$ 上的量词消去）可判定 ✓。$\square$

$$\boxed{\ q1\ \text{的"是否可判定"}=是；\text{但上面的判定是}\ \exists\mathbb C\text{-消去，复杂度未知}\ }$$

### 30.3 为什么这不等于 $q1$

- 定理 30.3 只保证**可判定** ✓，不保证多项式 ✗ —— 量词消去的复杂度可以是指数级 ✗；
- $q_{\min}=\min\{\rho+c\}$ 需要对 $O(n^2)$ 个 $(\rho,c)$ 各判一次 ✓，这不改变上一条 ✗；
- **要证 $q1$ = 假**，必须把 $P_\sigma$ 的非空性化成**多项式时间**的秩/线性条件 ✗ —— 这才是缺口 ✓；
- **要证 $q1$ = 真**，必须找到某个 $(\rho,c)$ 使 $P_\sigma$ 编码一个 $\exists\mathbb R$-难问题 ✗ —— 同样未做 ✓。

### 30.4 诚实标注

本节**没有**推进复杂度问题 ✗；它只是把"层判定是 $\exists\mathbb C$-型、因而可判定"这一点写下来 ✓，
从而明确 $q1$ 的真正内容是**复杂度**而不是可判定性 ✓。

## 31. 层程序与 $q_{\min}$ 之间的桥（结构引理）

> 前三十节都在判"某一层可行吗"。本节把"逐层判定"与"算出 $q_{\min}$"之间的那一步写成引理，
> 使"层算法 $\Rightarrow$ $q_{\min}$ 算法"成为一句可引用的话。

**引理 31.1（分层桥）** 设 $\mathsf{L}(\rho,c)\in\{0,1\}$ 表示"第 $(\rho,c)$ 层可行"。
则
$$q_{\min}=\min\{\rho+c:\ 1\le\rho\le d,\ 1\le c\le j,\ \mathsf L(\rho,c)=1\},$$
并约定空集的最小值为 $+\infty$（此时无解）。此外 $q_{\min}\ge r$（因为 $\mathcal L$ 必须含 $\operatorname{row}L_0$ 的 $r$ 个独立行）。

*证明*：由定义，可行解 $\mathcal L$ 给出 $(\rho,c)=(\dim\pi(\mathcal V),\dim(\mathcal V\cap\mathcal J))$，且 $q=\dim\mathcal V=\rho+c$ ✓；
反之给定满足 $(5a)\wedge(5b)$ 的 $\mathcal V$ 就得到一个可行解 ✓。故可行解的 $q$ 集合与 $\{\rho+c:\mathsf L(\rho,c)=1\}$ 相同 ✓；
取最小即得 ✓。$r$ 的下界由 $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ 给出 ✓。$\square$

**推论 31.2（复杂度归约）** 若 $\mathsf L$ 可在 $T(n)$ 内判定，则 $q_{\min}$ 可在 $O(n^2\,T(n))$ 内算出
（$\rho$ 至多 $d\le n$ 种、$c$ 至多 $j\le n$ 种 ✓）。

$$\boxed{\ q1\ \text{的复杂度}=\text{层判定 }\mathsf L\text{ 的复杂度}\ +\ O(n^2)\ }$$

**诚实标注**：引理 31.1 是**平凡**的结构事实 ✓（写下来只是为了让"逐层"与"$q_{\min}$"之间的归约显式化 ✓）；
它**不**提供任何新的层判据 ✗。当前 $\mathsf L$ 的已知情形见 §28.2 与定理 29.1（固定 $(\mathcal U,\mathcal H)$）✗。
