# 321 专家 93 号裁决落实：$d_{\min}=\nu-1$ 成为定理

> 送审件 [93](../../../for_expert/archive/93_left_inverse_degree_and_directions.md)（已归档），
> 答复 [93-reply](../../../for_expert/archive/93_left_inverse_degree_and_directions-reply.md)。
> 本文件落实裁决，并记录由此得到的一个**新定理**（把 320 的猜想闭合）。

## 目标

1. 逐条落实 93 号裁决。
2. 按 93 号的提示（Hautus 形式 + 可观测性指标）解决 Q5：把 $\deg S\le\omega-1$ 从猜想变成定理，并给出构造。
3. 修正 320 号里专家指出的过度表述（Q3）。

## 设想与理由

93 号给出两条关键提示：

- 规范形 $X=[I_\omega;0]$、$G=[G_1;G_2]$ 后
  $$Q(\lambda)=\begin{bmatrix}\lambda I-G_1\\-G_2\end{bmatrix},$$
  "对每个 $\lambda$ 满列秩"就是 $\operatorname{rank}[\lambda I-G_1;G_2]=\omega\ \forall\lambda$，
  即 **Hautus/PBH 意义下 $(G_1,G_2)$ 可观测**。
- 因此应找 $d_{\min}$ 的**内蕴刻画**（可观测性指标），而不只是一个更紧的界。

把这两条合起来，用"按 $\lambda$ 的幂比较系数"就能同时得到上下界——不需要 Bézout 或伴随。

## 做法

### 1. 定理与证明（8 行）

设 $A\in\mathbb R^{\omega\times\omega}$、$C\in\mathbb R^{p\times\omega}$，$Q(\lambda)=\begin{bmatrix}\lambda I-A\\-C\end{bmatrix}$。

> **定理 1.** 设 $\omega\ge1$，$A\in\mathbb R^{\omega\times\omega}$、$C\in\mathbb R^{p\times\omega}$，
> $Q(\lambda)=\begin{bmatrix}\lambda I-A\\-C\end{bmatrix}$。则存在次数 $\le d$ 的多项式矩阵
> $X(\lambda)\in\mathbb R[\lambda]^{\omega\times\omega}$、$Y(\lambda)\in\mathbb R[\lambda]^{\omega\times p}$ 使
> $$X(\lambda)(\lambda I-A)+Y(\lambda)C=I_\omega$$
> 当且仅当 $\operatorname{rank}[C;CA;\dots;CA^d]=\omega$。
> （$\omega=0$ 时 $Q$ 是空矩阵，左逆平凡；该分支在 312 的引理链里直接处理。）

*证明.* 把 $\lambda$ 的幂逐项比较（$X=\sum_{k\le d}X_k\lambda^k$、$Y=\sum_{k\le d}Y_k\lambda^k$）：

- $\lambda^{d+1}$ 的系数：$X_d=0$；
- $\lambda^k$（$1\le k\le d$）：$X_{k-1}-X_kA+Y_kC=0$；
- $\lambda^0$：$-X_0A+Y_0C=I_\omega$。

（$\Leftarrow$）若 $\operatorname{rank}[C;\dots;CA^d]=\omega$，则 $Y\mapsto YM$（$M=[C;\dots;CA^d]$ 为 $p(d+1)\times\omega$，秩 $\omega$）是满射，取常数 $Y_0,\dots,Y_d$ 使
$$\sum_{k=0}^{d}Y_kCA^k=I_\omega .$$
令 $X_d=0$、$X_{k-1}=X_kA-Y_kC$，则三条系数方程全成立，故 $S=(X,Y)$ 是次数 $\le d$ 的左逆。

（$\Rightarrow$）若恒等式成立，$\lambda^{d+1}$ 的系数给 $X_d=0$；回推得 $X_{k-1}=X_kA-Y_kC$，故
$$X_0=-\sum_{k=1}^{d}Y_kCA^{k-1}.$$
代入 $\lambda^0$ 的方程：$-X_0A+Y_0C=\sum_{k=0}^{d}Y_kCA^k=I_\omega$，于是 $M$ 的秩为 $\omega$。$\square$

> **推论 1.** 令 $\nu$ 为 $(A,C)$ 的可观测性指标（最小的 $k$ 使 $\operatorname{rank}[C;\dots;CA^{k-1}]=\omega$）。则
> $$\boxed{\,d_{\min}(Q)=\nu-1\,}.$$
> 特别地 $d_{\min}\le\omega-1$（经典事实：可观测 $\omega$ 维系统的可观测性指标 $\nu\le\omega$）。

**为什么这比 320 的猜想更强**：320 只猜 $d_{\min}\le\omega-1$；推论 1 给出**等式**，并解释了数据里的分布——
$(6,4)$ 的 $\{1,2,3\}$ 正是 $\nu\in\{2,3,4\}$，$q=\omega+1$ 的单桶正是 $\nu=\omega$（单输出）。

### 2. 与项目命题的连接

$r=0$ 时 $H=XB$、$H_A=GB$，压成 $Q(\lambda)=\lambda X-G$（$X$ 满列秩）。行变换取 $X=[I_\omega;0]$、
$G=[G_1;G_2]$，则

$$Q(\lambda)\ \text{对每个}\ \lambda\ \text{满列秩}\iff (G_1,G_2)\ \text{可观测},\qquad d_{\min}=\nu-1 .$$

**对 $r=0$ 系统的直接后果**：317 号用统一界 $d=2\omega-2$（未知量 $(2\omega-1)q\omega$）；现在可取

$$d=\nu-1\ (\le\omega-1),\qquad \text{未知量}\ \nu\,q\,\omega .$$

$\nu$ 由 $[G_2;G_2G_1;\dots]$ 的秩多项式时间算出。$\omega=2,\nu=1$ 时从 $6q$ 降到 $2q$；
$\nu=\omega$ 时从 $(2\omega-1)\omega q$ 降到 $\omega^2q$（约一半）。

### 3. 精确验证（c331）

| 检查 | 结果 |
|---|---|
| $d_{\min}=\nu-1$ | **255/255**；联合直方图全在对角线 $\{(1,0),(2,1),(3,2)\}$ |
| 构造方向：显式造 $S$ 并 sympy 逐项验证恒等式 | **8/8** 成功 |
| $d=\nu-2$ 处构造按预期失败（可观测性块秩不足） | 8/8 按预期 |

脚本：[c331](../../../../tools/verification/c331_observability_index.py)。有限精确检验，不是证明；
**证明是上面的定理 1**。

## 进展

1. **320 的猜想闭合**：$[猜想]\to[已证-纸面]$（定理 1 + 推论 1）+ $[精确验证 255/255]$。
2. **修正 Q3 的过度表述**（专家指出）：320 写"FPT($q$) 若要成立必须来自非量词消去的论证"——
   应为"**本类编码 + 量词消去路线内**不可能；一般 FPT($q$) 未被排除"。93 号明确：
   $\Theta(q^2)$ 变量是当前编码的限制，不是任何算法的下界。
3. **优先级按 93 号重排**：Q5（本轮已完成）→ Q1（超平面确定化，最高优先的几何题）
   → Q4（全局翻译引理，平行）→ Q2（型控制，长期）→ Q3（缓，等 Q4）。
   专家建议投入 60%（代数/几何算法）/ 40%（全局硬度）。
4. **93 号要求的审计项**（未做，登记）：
   - 7.1：FPT 的多项式因子指数必须**与 $\ell$ 无关**，否则位级 FPT 会退化为 XP；FIND 的位模型缺口要在把算法结果当定论前关掉。
   - 7.2：不得使用暗示 $\exists\mathbb R$-complete 的措辞。
   - 7.3：DEC / OPT / FIND 三者分开，判定算法不自动给最小阶构造。
5. **Q1 的具体路线**（93 号给的，取代我原来的"两选项"）：用**齐次化极大子式** $Q(s,t)=sX-tG$
   （二元齐次形式，含无穷远点）而不是仿射次数；用 subresultant / 系数矩阵秩条件表达
   $Y_d=\{y:\deg\gcd(f_1(y),\dots)\ge d\}$；再对例外轨迹做**递归 generic-gcd 分解**。
   警告：次数界本身不等于多项式算法，还要控分量数、表示复杂度、分解位复杂度、递归深度。

## 最终结论

- **定理（新，8 行证明）**：$d_{\min}=\nu-1$，故 $d_{\min}\le\omega-1$。320 的猜想为真，且被锐化为等式。
- **直接收益**：$r=0$ 系统与 $\exists\mathbb R$ 左逆证书的规模由 $\nu$（而不是 $2\omega-1$）控制。
- 本轮**不**升级为 `proof/` 卷宗：登记要走 `docs/02` 编号与别名表，属独立一轮的整理工作；
  这条已在此标记为**待升级**，不得在没有卷宗的情况下当作"已归档定理"引用。

## 放弃原因

- 定理的 `proof/` 卷宗与 `docs/02` 登记未做（见上）。
- 未核 Fabiano–Struppa 的具体界：定理 1 已自足，不再需要外部界。
- Q1/Q2/Q4 未动（Q1 需要齐次化 + 递归分解，是一个完整回合）。

## 残留价值

- 一个可独立成节的小定理（证明 8 行），把 $r=0$ 的规模从 $2\omega-1$ 降到 $\nu$；
- 专家裁决的逐条落实表（下）；
- Q1 的可执行路线（齐次化 + subresultant + 递归分解）与它的四个未控量；
- 一条方法论：**先问"这个量有没有内蕴刻画"，再问"界紧不紧"**——93 号的提示正是这样把猜想变成等式的。

## 专家复核意见（裁决）

| 问题 | 93 号裁决 | 落实 |
|---|---|---|
| Q1 超平面确定化 | 最高优先的几何题；改用齐次化极大子式 + subresultant + 递归例外轨迹分解；警告次数界≠算法 | 记入 §进展 5，作为下一轮 Q1 的路线 |
| Q2 型控制 | 用 Kronecker 箭图语言；**但箭图是 tame 而非有限表示型**，必须区分离散剖面 / 连续模 / 嵌入数据；拆成三条陈述；从 $c=2$ 起 | 记入，待做 |
| Q3 FPT($q$) | 仍然可能；$\Theta(q^2)$ 只是 QE 路线的限制，不是下界；暂不做 W[1]-hard | 修正 320 的表述 |
| Q4 硬度 | 先证**全局秩解码翻译引理**（双向）；放弃局部乘法门；no-go 只作内部技术结果；不要假设固定秩 3 自动传递 | 作为平行线 |
| Q5 次数界 | 提到"可观测性指标"并找内蕴刻画 | **已解决**：定理 1 + 推论 1（255/255 验证） |
| Q6 任务规划 | Q5 → Q1 → Q4（平行）→ Q2（长期）→ Q3（缓）；60/40 投入；避免碎片化 | 采纳，写入优先级 |

## 重要性评估与新颖性（自我校准）

**一句话**：这是引理级的**锐化**，不是突破；很可能不是新结果；影响局限在 $r=0$ 与证书规模。

- **新颖性：待核，倾向不新。** 把铅笔认作 Hautus 形式之后，"$[\lambda I-A;C]$ 的多项式左逆次数
  $=$ 可观测性指标 $-1$"属于经典多项式矩阵 / 观测器文献的常见对象（93 号的提示本身即指向它）。
  检索（记入 [`literature/SEARCH_LOG.md`](../../../../literature/SEARCH_LOG.md)）**未命中**该等式的明文陈述；
  最接近的是标量 Diophantine/Bézout 的次数界、以及"最小次数多项式基 + 观测性指标"这条线，
  加上 Fabiano–Struppa 的一般界。**在文献逐条核对之前按"重新发现"记账**，
  不得在对外文档中当作新定理主张。
- **买到什么**：$r=0$ 的系统从 $(2\omega-1)q\omega$ 个未知量降到 $\nu q\omega$（常数因子 2–3）；
  $\exists\mathbb R$ 左逆证书同量级下降；从账本上删掉一个猜想。
- **买不到什么**：不触及 $q1$（没有硬度、没有一般 $r$ 的算法、没有新的层几何）；不改变任何复杂度类
  （$r=0$ 本来就是多项式，只是多项式更小）；不影响固定 $q$ 的 XP 与固定 $\ell$ 的 FPT 的指数结构；
  只覆盖**一次**铅笔（一般次数 $d$ 的 $2d\omega-d-1$ 未动）。
- **所以**：值得记、值得用、**不值得宣传**。论文里最合适的位置是零自由行那一节的一句更紧的界，
  不单独成节、不作里程碑；`proof/` 卷宗与 `docs/02` 登记**暂缓**（若日后要对外引用这条再补）。

本轮真正重要的两件事不是这条定理，而是：93 号对优先级的重排（Q5→Q1→Q4$\parallel$→Q2→缓 Q3），
以及它纠正了我们的一个**假下界**——"$\Theta(q^2)$ 个变量"只限制量词消去路线，不是任何算法的下界。

## 相关文件

- 送审件：[93](../../../for_expert/archive/93_left_inverse_degree_and_directions.md)
- 答复：[93-reply](../../../for_expert/archive/93_left_inverse_degree_and_directions-reply.md)
- [c331](../../../../tools/verification/c331_observability_index.py)（本轮新增）
- [c330](../../../../tools/verification/c330_certificate_degree.py)（320 的搜索）
- [attempts/320](320_left_inverse_degree.md)（猜想原文，已被本轮锐化）
- [attempts/317](317_85_verdict_r0.md)（$r=0$ 的 $2\omega-2$ 界与系统规模）

## 状态

- 定理 1 / 推论 1：**[已证-纸面]** + **[精确验证 255/255 + 构造 8/8]**；`proof/` 卷宗**待建**。
- Q3 修正：**[已落实]**（文字级）。
- Q1/Q2/Q4：**[未开始]**，路线已记录。
