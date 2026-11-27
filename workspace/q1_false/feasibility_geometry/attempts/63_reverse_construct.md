# 反向构造：整族 Type III **不是孤例**（第二个实例，且 gap=2）

## 目标

专家 2026-11-04 §Step 2 让我们"按构造"而不是"筛选"去找第二个整族 Type III 实例。
本轮按 $U_1=\alpha U_0$（等价 $(A-\alpha I)V\subseteq\ker L_0$）反向构造，成功。

## 设想与理由

筛选失败的原因是 $\varepsilon=0$ 在随机族里几乎不出现（$n=6,p=2,r=2$ 的 6000 次随机中 0 个）。
反过来：**先定 $V$、再让 $A$ 把 $V$ 打进 $\ker C$、最后选 $L_0$ 与 $V$ 上的 $\alpha$**，则 $\varepsilon=0$ 自动成立。
构造步骤（全部 $\mathbb Q$ 上精确）：

1. $V=\langle e_1,\dots,e_{d_V}\rangle$；
2. $C$：前 $d_V$ 列为 $0$，其余随机，$\operatorname{rank}C=p$；
3. $A$：前 $d_V$ 列落在 $\ker C$ 里（于是 $CA|_V=0$），其余随机；要求 $\dim\ker[C;CA]=d_V$ 恰好、$(C,A)$ 可观测；
4. 取 $\alpha$，$K=(A-\alpha I)V$；取 $L_0=S\,\mathcal O(C,A)$ 使 $L_0K=0$、$\operatorname{rank}L_0=r$、$(L_0,A)$ 可观测；
5. 要求 $V\not\subseteq\ker(A-\alpha I)$（否则 $V$ 含特征向量，$q_{\min}=\infty$）。

## 做法

[reverse_construct.py](../../../../tools/verification/reverse_construct.py)：400 次尝试，86 个成功构造；
对每个实例在 $q_0$ 与 $q_0+1$ 阶枚举图卡与 $\theta$，把候选分成 可行 / Type I / Type III。

## 进展

### （1）构造成功率高，且整族 Type III 是**常态**

| 阶段 | 计数 |
|---|---|
| 尝试 | 400 |
| 构造成功 | **86** |
| 在 $q_0+1$ 阶（$d<k$，有真正参数）整族 Type III | **86 / 86** |
| 在 $q_0$ 阶（$d=k$，$Z$ 被强制）整族 Type III | 22（其余 64 是 Type I）|

即：**构造出来的实例，在 $q_0+1$ 阶全部是整族 Type III**——与"筛选式搜索一个也找不到"形成鲜明对照。
（$q_0$ 阶的 22 例是"$Z$ 被强制"的平凡整族，不算 C4 型现象。）

### （2）一个详细核验的实例（$n=6,p=r=2$，$\alpha=-2$）

$$A=\begin{pmatrix}
2&1&2&-1&2&-1\\
2&-2&1&-2&1&1\\
12&-8&-1&0&1&-1\\
6&-4&-2&2&2&-1\\
-2&1&0&2&1&2\\
1&-1&0&1&0&-1\end{pmatrix},\quad
C=\begin{pmatrix}0&0&0&1&2&-2\\0&0&-1&1&-2&2\end{pmatrix},\quad
L_0=\begin{pmatrix}-6&9&8&-11&-2&-28\\7&-8&-4&11&25&20\end{pmatrix}$$

$q_0=2$、$n_0=6$、$r_1=4$、$\dim V=2$、阶区间 $[2,4]$。逐阶结果：

| 阶 | $d$ | $k$ | 图卡 | 测试候选 | 可行 | $h$ | $q+r_1$ | 符号 gcd 次数 | 结论 |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 2 | 1 | 22 | 0 | 6 | 6 | 2 | **Type I**（$h=q+r_1$）|
| 3 | 1 | 2 | 2 | 各 22 | 0 | 6 | 7 | **1**（两张卡）| **整族 Type III** |
| 4 | 0 | 2 | — | — | 有见证 | 6 | 8 | — | **可行** |

$q=4$ 的显式见证（$[L_0;R]$，$R$ 为后两行，七条检查全过）：

$$R=\begin{pmatrix}0&1&4&-4&3&-1\\-4&-2&-3&1&3&-1\end{pmatrix}$$

⟹ 该实例 $q_{\min}=4$，**阶差 2**，中间那一阶是**真正的**整族 Type III（$d=1<k=2$，参数空间正维）。
两点都优于 C4：有**两种失败类型相继出现**（Type I 然后 Type III），且阶差是 2。

### （3）跌落 locus 已证为空（2026-11-04 补）

用 B.13c 的形式：失败 $\iff\exists x\in V\setminus\mathcal Z,\lambda:(\lambda I-A)x\in\mathcal Z$。
因 $\dim(V\cap K)=0$，任何 $x\in V\setminus0$ 自动满足 $x\notin\mathcal Z$。令
$M(\theta,\lambda)=(I-P_z)(\lambda I-A)V$（$6\times2$），失败 $\iff\operatorname{rank}M\le1$。
把 15 个 $2\times2$ 子式看成 $\mathbb Q(\theta)[\lambda]$ 的元素：

| 图卡 | 非零子式 | $\gcd$ 次数 | 共同根 | 全部子式在根处恒零 | 首项系数 |
|---|---|---|---|---|---|
| $(0)$ | 14 | 1 | $\lambda=-2$ | **是** | 1 |
| $(1)$ | 14 | 1 | $\lambda=-2$ | **是** | 1 |

$\gcd=\lambda+2$ 首一、与 $\theta$ 无关且整除全部子式 ⟹ **对每个** $\theta$ 都有 $\operatorname{rank}M(\theta,-2)\le1$
⟹ **跌落 locus 为空**。加上 $\theta=-8..8$ 的 34 个精确核验（无一可行），该阶的整族失败成为**定理**。
证书写在 [proof/type3_second_example/README.md](../../../../proof/type3_second_example/README.md)。

## 最终结论

1. **整族 Type III 不是孤例**：反向构造在 86/86 个实例上于 $q_0+1$ 阶产生整族 Type III；
   其中一例已做成**完整证书**（跌落 locus 为空，见第 (3) 条与 `proof/type3_second_example/`）；
2. **$\varepsilon=0$ 在随机数据里罕见（0/6000），但可系统构造**——这解释了"筛选找不到、构造一造就有"；
3. 详细核验的实例：$q_0=2$ 为 Type I、$q_0+1=3$ 为整族 Type III、$q=4$ 可行 ⟹ $q_{\min}=4$，**阶差 2**；
4. 待补：该实例的跌落 locus（subresultant 分析）；若能证空，则得到一个与 C4 **结构不同**的整族反例。

## 放弃原因

不适用（构造与核验成功；跌落 locus 留待下一步）。

## 残留价值

* 一个**可复现的构造**（`reverse_construct.py`），能批量产出整族 Type III 实例；
* 一个**阶差 2** 的显式实例（比 C4 更能说明"计数与谱是两种机制"）；
* 定量结论：$\varepsilon=0$ 随机罕见、可构造 ⟹ 搜索策略必须"按构造"而非"按筛选"。

## 相关文件

- `tools/verification/reverse_construct.py`
- `docs/02` B.13d（$\varepsilon=0$ 的秩判据，构造的依据）
- `attempts/62_structured_search.md`（筛选式搜索的负结果，与本条互补）
- 专家答复：`workspace/for_expert/archive/12_research_direction-answer.md` §Step 2
