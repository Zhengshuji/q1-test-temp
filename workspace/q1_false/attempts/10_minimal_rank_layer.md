# 最小秩层（$\rho=\rho_{ci}$）的判定：能否化为多项式恒等测试

> 方向：$q1$ = 假（多项式算法）。优先级：**专家 2026-11-01 指定的第一目标**。
> 相关：专家复核 §6（Q5.1）、[docs/05](../../../docs/05_open_questions.md) Q1。

## 目标

证明或推翻下面这条**候选定理**（专家 2026-11-01 §6.4 的表述）：

> **Minimal-rank-layer reduction.** 设 $\mathcal A_{\min}$ 是 $\rho=\rho_{ci}$ 层上"代数可容许"实现的仿射参数空间。
> 若谱条件可表示为一个多项式 $F$ 使
> $$\mathrm{DEC}_{\rho_{ci}}(q)\iff\exists x\in\mathcal A_{\min}:F(x)\ne0,$$
> 则 $\mathrm{DEC}_{\rho_{ci}}(q)\iff F|_{\mathcal A_{\min}}\not\equiv0$。

若成立且 $F$ 可显式写出，"该层判定"就归到**多项式恒等测试（PIT）**；再若 $F$ 的结构允许确定性多项式时间测试，则 $q1$ = 假（至少该层）。

## 设想与理由

- 该层 $\rho_{ci}=P(T,B,U_0)$ 已可算（$O(n^4)$，D.1–D.3、E.1）；
- 层内"代数可容许"部分是**线性/仿射**约束（$T_S\subseteq U$、$U\subseteq\ldots$），只有谱条件是"非零"型；
- 非零型条件在无限域上有标准事实：**$\exists x\in\mathcal A:F(x)\ne0\iff F|_{\mathcal A}\not\equiv0$**（只要 $\mathcal A$ 非空；若 $\mathcal A$ 是仿射空间或其**非空 Zariski 开子集**，后者稠密，结论同样成立）；
- 专家指出：$\rho_{ci}$ 可算**不**推出该层可判——缺的正是"可行集是仿射/开稠密集"与"$F$ 显式构造"两件。

## 做法（三步，按专家 Stage A/B/C）

1. **写出 $\mathcal A_{\min}$**：在 $\rho=\rho_{ci}$ 层，把 $\mathcal V$ 参数化（$U$ 的 Grassmann 坐标 $\times$ 基），
   把 $(5a)$、$T_S\subseteq U$、"$U\cap(G/S)=0$" 化成对参数的**线性等式 + 线性不等式**；
   记录哪些是开条件（后者给 Zariski 开）。
2. **写出 $F$**：谱条件 = "极大子式 $f_1(x,\lambda),\dots,f_s(x,\lambda)$ 无公根"。
   用 resultant/subresultant 把"无公根"变成一个关于 $x$ 的多项式非零条件：
   例如取两个 $x$-多项式的组合 $g_x,h_x$，令 $F(x):=\operatorname{Res}_\lambda(g_x,h_x)$。
   **注意**：不能随手取一个极大子式（非零多项式必有复根），组合必须由 $\gcd=1$ 的判定构造给出。
3. **测试**：$F|_{\mathcal A_{\min}}\not\equiv0$ 的判定；先做**精确小实例**（$\mathbb Q$ 上、$n\le6$）验证
   $F$ 的构造是否真的等价，再谈复杂度。

## 进展

- [x] 确认该层 $\rho_{ci}=P$ 可算（D.1–D.3、E.1，已有 Lean/纸面）
- [x] 确认"非零条件 + 仿射/开集 ⟹ 非恒零"这条逻辑（专家 §6.1）
- [x] 读完 Liu(2026)、Löfberg(2026)：确认**方阵情形**（$q=t$）下 $(5b)\iff\det[U\mid P]\in\mathbb C^\times$
      即"全部非首项系数为零 + 常数项非零"，与 Liu 的"残差进系数"同形（[docs/07 §9](../../../docs/07_literature_review.md)）
- [ ] 显式写出 $\mathcal A_{\min}$（第一步）
- [ ] 构造 $F$ 并在小实例上核验等价（第二步/第三步）

## 最终结论

待定。

## 放弃原因

（暂不适用）

## 残留价值

即使本路线失败，两个副产品独立有用：
1. $\mathcal A_{\min}$ 的显式参数化（可复用于任何层的枚举）；
2. "方阵情形 $\iff$ 系数方程"这条桥（与 Liu 的构造同形），是**硬度归约**（Workstream C）的入口。

## 相关文件

- [docs/05](../../../docs/05_open_questions.md) Q1（含专家四条补充）
- [archive/expert_correspondence/expert_review_2026-11-01/README.md](../../../archive/expert_correspondence/expert_review_2026-11-01/README.md) §6
- [proof/p_is_polynomial/](../../../proof/p_is_polynomial/)（$P$ 的递归与下界）
- [literature/notes/LIU_2026_SOF_EXISTS_R.md](../../../literature/notes/LIU_2026_SOF_EXISTS_R.md)

---

## 6. 第一步的推导：$\mathcal A_{\min}$ 到底是什么（2026-11-02）

### 6.1 设与记号

商空间 $X=\mathbb C^n/\mathcal J$（$\dim X=d=n-j$），$T$ 是 $A$ 在 $X$ 上的作用，$B=\pi(\mathcal J A)\subseteq X$，
$U_0=\pi(\operatorname{row}L_0)$。层的条件只经由 $U:=\pi(\mathcal V)\subseteq X$：

$$\dim U=\rho,\qquad U\supseteq U_0,\qquad (5a)\iff TU\subseteq U+B .$$

（$\mathcal V$ 的其余部分落在 $\mathcal J$ 里，由 $c$ 记账。）

### 6.2 图卡参数化（Grassmann 坐标）

取 $U=\operatorname{im}G$，$G\in\mathbb C^{d\times\rho}$ 满列秩；图卡 $I\subseteq\{1,\dots,d\}$（$|I|=\rho$）使 $G_I$ 可逆，
归一化 $G_I=I_\rho$，则

$$G=\begin{pmatrix}I_\rho\\ \Theta\end{pmatrix}\quad(\Theta\in\mathbb C^{(d-\rho)\times\rho}),$$

即**一个图卡内 $U$ 由仿射参数 $\Theta$ 参数化**（这正是 P2 的"图卡 $Z_I(\Theta)$"）。

### 6.3 两条约束在 $\Theta$ 下的形状

1. **$U_0\subseteq U$**：$U_0=\operatorname{im}G_0$（$G_0$ 的列张成 $U_0$），条件
   $\operatorname{rank}[G,\ G_0]=\rho$，即全部 $(\rho+1)$-子式为零。
   由于 $G$ 的条目**仿射**于 $\Theta$，这些子式是 $\Theta$ 的**仿射**函数 ⟹ **线性方程组** ✓

2. **$TU\subseteq U+B$**：等价于
   $$\operatorname{rank}[G,\ B,\ TG]=\operatorname{rank}[G,\ B]\quad(\text{记 } b=\dim B),$$
   即全部 $(\rho+b+1)$-子式为零。$TG$ 的条目也**仿射**于 $\Theta$，故这些子式是 $\Theta$ 的
   **次数 $\le\rho+b+1$ 的多项式** ⟹ **非线性（行列式型）方程组**。

### 6.4 结论（重要，且与专家的假设不同）

> **$\mathcal A_{\min}$（单图卡内）是一个"线性方程组 + 行列式簇"的代数集，一般不是仿射空间。**

所以专家 §6.1 的"可行集是仿射空间或非空 Zariski 开子集"这一条**不能直接假设**；
若要用"非零条件在稠密集上"的论证，必须先把**行列式型条件解掉**（例如：
在 $\rho=\rho_{ci}$ 的极小性下，$TU\subseteq U+B$ 是否自动成立？或是否可等价地写成 $\Theta$ 的**线性**条件？）。

这是一个**可检验的问题**：在小实例上枚举该层的可行 $U$，看解集是否线性（例如：

- 解集的仿射包维数是否等于解集维数？
- 是否每个解都是某个线性系统的解？分别对"只保留线性方程"与"全部方程"求解并比较。

若两者相同 ⟹ 行列式条件冗余 ⟹ $\mathcal A_{\min}$ 是仿射的 ⟹ 专家的第一目标可行。
若不同 ⟹ 需要在行列式簇上做非零论证（更接近 $\exists\mathbb R$ 的一般情形）。

### 6.5 下一步（具体）

1. 写 `tools/verification/layer_min_affine.py`：对小 $n$（$\le6$）、$\rho=\rho_{ci}$ 的实例，
   在图卡内精确枚举/求解 $\Theta$ 的可行集，比较"线性方程解集"与"全部方程解集"；
2. 若发现解集非仿射，记录**最小反例**（这也回答"为什么这一层不平凡"）。

---

## 7. 第一次计算实验（2026-11-02）：闭包算法与 P 的交叉核对

**脚本**：[tools/verification/min_layer_closure.py](../../../tools/verification/min_layer_closure.py)（精确有理算术）。

做的事情：
1. 把实例搬到商空间 $X=\mathbb C^n/\mathcal J$（$\mathcal J=\operatorname{row}[C;CA]$），算出 $T$、$B=\pi(\mathcal J A)$、$U_0=\pi(\operatorname{row}L_0)$；
2. 用**闭包迭代** $U\leftarrow U+TU+B$ 求"含 $U_0$ 的 $T$-不变模 $B$ 最小子空间" $U^*$；
3. 断言 $U_0\subseteq U^*$ 且 $TU^*\subseteq U^*+B$；
4. 与 [tools/p_algorithm/c195_P_q.py](../../../tools/p_algorithm/c195_P_q.py) 的递归 `P_alg` 交叉核对。

**结果**（四个实例）：

| 实例 | $n$ | $d$ | $\dim B$ | $\dim U_0$ | closure | `P_alg` | 一致 |
|---|---|---|---|---|---|---|---|
| R17-like | 5 | 3 | 0 | 1 | 1 | 1 | ✓ |
| second | 6 | 4 | 0 | 1 | 1 | 1 | ✓ |
| chain | 4 | 2 | 0 | 1 | 2 | 2 | ✓ |
| B=0（n=4）| 4 | 2 | 0 | 0 | 0 | 0 | ✓ |

**一个真实的发现（约定差异）**：第一次运行出现 `chain: closure=2, P_alg=1` 的"不一致"。
手算确认 $P=2$（$U_0=\operatorname{span}\{(0,1)\}$，$T(0,1)=(1,0)$，故必须取全空间）。
原因是 **`c195_P_q.P_alg` 用行约定**（$x\mapsto xA$），而新脚本的 $T$ 是列约定；转置后
`P_alg(T^T)=2` ✓。**已在脚本里加注释并转置**。

### 7.1 更正（2026-11-02，专家复核 §1.3）

> 上面把"闭包维数"当成 $P=\rho_{ci}$ 的说法**是错的**。$P$ 的定义是
> $$P=\min\{\dim U:\ U_0\subseteq U,\ TU\subseteq U+B\},$$
> 而闭包迭代给的是"**含 $U_0$ 与 $B$ 的最小 $T$-不变子空间**"——两者一般**不等**。
>
> **专家的反例**：$T=0$、$U_0=0$、$B\ne0$。闭包 $=B$（维数 $>0$），但 $U=0$ 已经可行（维数 $0$）。
>
> 已把该反例加入 [min_layer_closure.py](../../../tools/verification/min_layer_closure.py) 作**回归测试**
> （脚本现在会断言"闭包 $\ne P$"）：`闭包维数 = 1, P_alg = 0 ⟹ 反例成立: True`。
> 四个真实实例上两者相等只是**巧合**（那些实例里 $U_0$ 已经把闭包撑满），不能推广。

**谨慎声明**：
1. 这四个实例只说明"闭包维数 = 递归 P"在这几个点上成立，**不是定理**；
2. 闭包给的是"含 $S$ 与 $B$ 的最小 $T$-不变子空间"，它等于 $P$（$\min\dim$ 版本）**未证**；
   注意 $\{U:S\subseteq U,TU\subseteq U+B\}$ 对交**不封闭**（$(U_1+B)\cap(U_2+B)\nsubseteq(U_1\cap U_2)+B$），
   所以"最小元"的存在性本身需要单独论证；
3. 本实验**没有**回答 §6 的问题（$\mathcal A_{\min}$ 是否仿射）；那需要按 §6.5 的比较实验。

---

## 8. 第二次计算实验（2026-11-02）：线性条件**不**蕴含行列式条件

**脚本**：[tools/verification/layer_min_affine.py](../../../tools/verification/layer_min_affine.py)（精确有理算术）。

**设置**：在图卡 $I$（$|I|=\rho$）内把 $U$ 参数化为 $G(\Theta)=[I_\rho;\Theta]$，比较两个解集：

- $A_{\rm lin}=\{\Theta:U_0\subseteq\operatorname{im}G(\Theta)\}$（**线性**方程）；
- $A_{\rm full}=A_{\rm lin}\cap\{\Theta:TU\subseteq U+B\}$（再加**行列式**条件）。

### 8.1 三个真实实例：线性解集是 0 维

| 实例 | $d$ | $\rho_{ci}$ | $\dim U_0$ | 线性解集维数 |
|---|---|---|---|---|
| R17-like | 3 | 1 | 1 | 0 |
| second | 4 | 1 | 1 | 0 |
| chain | 2 | 2 | 1 | 0 |

即：这些实例上图卡内 $U$ 被"$U_0\subseteq U$"钉死，问题**退化**——比较实验没有信息量。

### 8.2 合成数据：给出**精确反例**（这是本节的结论）

取 $d=4$、$\rho=3$、$B=0$、$U_0=\operatorname{span}\{e_0\}$、$T:e_0\mapsto e_1\mapsto e_2\mapsto0$，$e_3\mapsto0$
（此时闭包维数 $=3=\rho_{ci}$）。线性解集维数 $=(d-\rho)(\rho-1)=2$，**正维**。

结果（脚本原样输出）：

| 图卡 $I$ | 线性解集维数 | 特解处 det 条件 | 采样点 |
|---|---|---|---|
| $(0,1,2)$ | 2 | 成立 | **s=0 处违反** |
| $(0,1,3)$ | 2 | **不成立（反例 $\Theta=0$）** | s=0 处违反 |
| $(0,2,3)$ | 2 | **不成立（反例 $\Theta=0$）** | s=0 处违反 |
| $(1,2,3)$ | — | 线性条件不相容 | — |

**结论（谨慎表述）**：

> 存在**精确有理反例点** $\Theta$ 满足线性条件 $U_0\subseteq U$ 但违反 $TU\subseteq U+B$。
> 因此在**这个合成数据**上 $A_{\rm lin}\supsetneq A_{\rm full}$——"$\mathcal A_{\min}$ 是线性/仿射集"**不成立**。

**边界（必须写明）**：
1. 合成数据**未必**来自某个 $(A,C,L_0)$ 实例；所以结论是对**参数化逻辑**的，不是对某个真实实例的；
2. 三个真实实例上线性解集是 0 维，问题退化，**没有**给出真实实例上的反例；
3. 若要真实实例上的反例，需要一个 $\rho_{ci}>\dim U_0+1$ 的实例（让 $(d-\rho)(\rho-1)>0$）。

### 8.3 下一步

1. 构造（或找出）$\rho_{ci}$ 较大、$\dim U_0$ 较小的**真实实例**，重跑本脚本；
2. 若真实实例上也出现 $A_{\rm lin}\supsetneq A_{\rm full}$，则专家的"仿射/Zariski 开"假设在该层**确定不成立**，
   需要改为"在行列式簇上做非零论证"（更接近一般 $\exists\mathbb R$）；
3. 若真实实例上 $A_{\rm lin}=A_{\rm full}$（即行列式条件被蕴含），则反而支持专家的路线。

---

## 9. 第三次实验（2026-11-02）：在**真实实例**上找到正维线性解集与反例

**脚本**：[tools/verification/find_layer_instance.py](../../../tools/verification/find_layer_instance.py)（确定性伪随机搜索 + 比较实验）。

### 9.1 搜索

$n=6$、$p=1$、$C=e_0^{\mathsf T}$、$L_0=e_1^{\mathsf T}$，扫 400 个整数 $A$（密度 0.3，条目 $\in\{-1,0,1,2\}$）。
筛选条件 $(d-\rho_{ci})(\rho_{ci}-1)>0$（即 $2\le\rho_{ci}\le d-1$，线性解集才可能正维）。

**命中 227/400** —— 这类实例**很常见**（不是稀有构造）。

### 9.2 两个实例的反例（精确有理点）

| 实例 | $d$ | $\rho_{ci}$ | $\dim B$ | 图卡 | 线性解集维数 | 特解 $\Theta$ | det 条件 |
|---|---|---|---|---|---|---|---|
| seed=1002 | 5 | 4 | 1 | $(0,1,2,3)$ | 3 | $\Theta=0$ | **违反**（反例）|
| seed=1002 | 5 | 4 | 1 | $(0,1,2,4)$ | 3 | $\Theta=0$ | **违反**（反例）|
| seed=1003 | 4 | 2 | 2 | $(0,1)$ | 2 | $\Theta=0$ | **违反**（反例）|

（$\Theta=0$ 即 $U=\operatorname{span}\{e_i:i\in I\}$，是图卡里的"坐标子空间"。）

### 9.3 结论（谨慎表述）

> 在**真实** $(A,C,L_0)$ 实例上，**行列式条件不被线性条件蕴含**：
> 存在精确有理点满足 $U_0\subseteq U$ 却违反 $TU\subseteq U+B$。

因此：
1. "在图卡坐标下 $\mathcal A_{\min}$ 是仿射集"——**不成立**（它是线性集与行列式簇的交，且交是真子集）；
2. 这不**推翻**专家的候选定理（它把"$\mathrm{DEC}\iff\exists x\in\mathcal A_{\min}:F(x)\ne0$"当**假设**），
   但推翻了"$\mathcal A_{\min}$ 自然是仿射的、因而非零论证自动成立"这一**希望**；
3. 要救回"非零 ⟹ 不恒零"，需要：
   (i) 另一种参数化（让行列式条件变成恒等式），或
   (ii) 在行列式簇上直接做非零论证（Gram 行列式/结式等），这更接近一般 $\exists\mathbb R$。

### 9.4 下一步

- 试**另一种参数化**：直接参数化"满足 $TU\subseteq U+B$ 的 $U$"（例如先取 $T$-不变子空间格中的可容许块），
  看新坐标下行列式条件是否变成线性/恒真；
- 若不行，转 Workstream B（Kronecker 结构）——专家认为中间层更值得投入。

---

## 10. 第四次实验（2026-11-02）：最小层的可行 $U$ **不唯一**（正维族）

在 seed=1002（$d=5$、$\rho_{ci}=4$、$\dim B=1$、$\dim U_0=1$）上，于两个图卡内枚举
$\Theta$ 的小整数组合（$\{-1,0,1\}^{\dim\rm null}$），检查 $TU\subseteq U+B$：

| 图卡 | 线性解集维数 | 满足 det 的**不同**有理点数（枚举到） | 三个解（只差最后一列）|
|---|---|---|---|
| $(0,1,3,4)$ | 3 | **3** | $\Theta_{2}=(0,-1,-1,c)$，$c\in\{-1,0,1\}$ |
| $(0,2,3,4)$ | 3 | **3** | $\Theta_{1}=(0,-1,-1,c)$ |

**结论（精确）**：最小层（$\dim U=\rho_{ci}$、$U_0\subseteq U$、$TU\subseteq U+B$）上存在
**至少三个不同的**可行 $U$——因此

1. 最小层的 $\exists$ **不是**"单点"，**不能**把该层判定的 $\exists$ 直接消掉；
2. $\mathcal A_{\min}$ 是**正维行列式簇**（不是仿射集、也不是单点）；
3. 专家的候选定理里"$\exists x\in\mathcal A_{\min}:F(x)\ne0$"是一个**真正的**半代数问题，
   不能靠"$\mathcal A_{\min}$ 是仿射的"简化。

**谨慎边界**：上面三个点只是"枚举到"的三个（$\Theta$ 的最后一列取 $-1,0,1$）；这不说明解集恰好是这三条，
也不说明维数恰好是 1——只说明**非唯一**且**正维**。

## 11. 由 8–10 得到的状态总结

| 问题 | 答案 |
|---|---|
| 图卡内"线性条件 ⟹ 行列式条件"？ | **否**（真实实例反例，§9） |
| 最小层可行 $U$ 唯一？ | **否**（至少三个，§10） |
| 最小层 $\mathcal A_{\min}$ 是仿射集？ | **否**（§8 合成 + §9 真实） |
| 最小层判定可化为 PIT？ | **仍开放**：需在正维行列式簇上做非零论证 |

**下一步建议**（见 §9.4）：换参数化（$T$-不变子空间格里的可容许块），或转 Workstream B（Kronecker）。

---

## 12. 第五次实验（2026-11-02）：秩分层——$\mathcal A_{\min}$ 是**可构造集**，未必闭

专家（2026-11-02 §1.2）指出：$TU\subseteq U+B$ 写成
$\operatorname{rank}[TG\ G\ B]=\operatorname{rank}[G\ B]$，**右边随 $\Theta$ 变**，
所以不是一个闭行列式条件；可行集可能是**开的**。他给了反例，已在本轮**复现**。

### 12.1 复现（脚本 [layer_min_affine.py](../../../tools/verification/layer_min_affine.py) 的 `expert_counterexample`）

$d=2$、$B=\operatorname{span}\{e_1\}$、$T:e_1\mapsto e_2$、$U_t=\operatorname{span}\{e_1+t e_2\}$（图卡 $(0)$，$\Theta=t$）：

| $t$ | $\operatorname{rank}[G,B]$ | $TU\subseteq U+B$ |
|---|---|---|
| $0$ | 1 | **False** |
| $1$ | 2 | True |
| $-2$ | 2 | True |
| $3/2$ | 2 | True |

（脚本里是**断言**这两个模式，不是硬编码结论——第二次我一开始把 $T$ 的方向写反了，断言立刻抓住。）

**结论**：可行集 $=\{t\ne0\}$ 在仿射直线里是**开集**（补一点）。

### 12.2 正确的描述

$$\mathcal A_{\min}=\bigcup_{k}\underbrace{\{\Theta:\operatorname{rank}[G(\Theta),B]=k\}}_{\text{局部闭}}\cap\underbrace{\{\operatorname{rank}[TG,G,B]=k\}}_{\text{闭}} .$$

即**有限个局部闭块的并**（constructible set），不是单个闭簇——除非有额外假设使 $\operatorname{rank}[G,B]$ 恒定。

**对"非零条件"论证的影响**：专家 §4（Q4.3）的泛型可行性定理要求 $X$ **不可约**；
对可构造集必须先取**不可约分支/秩层**，再逐块论证。这正是专家 §4 的"Obstacle 2"。

### 12.3 还缺什么

- 在**真实实例**上统计：可行集落在哪个秩层？是否只有一层承载可行点（若是，问题退化回闭情形）；
- 若可行点分布在多个秩层，则"泛型可行性"要逐层陈述。
