# $r=1$ 的固定阶判定：显式代数系统与一个结构实验

## 目标

按专家 2026-11-03 §3.1/§3.2 的中间目标，把 $r=1$、固定阶 $q$ 的判定问题写成**显式的多项式系统**
（变量 = 图卡参数 + Bézout 系数），并检验一个结构性猜想：可行集是否（仿射）线性。

## 设想与理由

专家给的路线：$(5a)$ 是图卡参数里的多项式秩约束；谱条件用**极大子式 gcd 为常数**表达，而
"gcd 为 1" 可用 **Bézout 恒等式** 写成多项式方程（系数次数有界）。若这套系统对 $r=1$ 退化成线性/双线性，
固定阶判定就可能是多项式的；否则它就是一个真正的 $\exists\mathbb R$ 实例，说明难在哪里。

## 做法

### (A) 显式系统

设 $r=1$、固定 $q$，$d=n-p-q$、$K=\ker[C;L_0]$（$\dim k$）。用第一个图卡参数化
$$\mathcal Z=K\cdot W(\Theta),\qquad W=\begin{pmatrix}I_d&\Theta\end{pmatrix},\ \Theta\in\mathbb C^{d\times(k-d)} .$$
记 $P_{\mathcal Z}(\lambda)=[(\lambda I-A)V\ \ Z(\Theta)]$，其中 $V$ 是 $\ker[C;CA]$ 的固定列基、$Z(\Theta)$ 是
$\mathcal Z$ 的列基（$P$ 对 $\Theta$ **线性**）。令 $s=\operatorname{rank}[V\ Z]=\dim V+d$，$m_i(\lambda;\Theta)$
为 $P_{\mathcal Z}$ 的全部 $s\times s$ 极大子式（$\deg_\lambda m_i\le\dim V$）。于是

$$\text{DEC}(q)\ \text{在}\ r=1\ \text{时}\iff \exists\Theta\ \exists\{u_i\}:\quad
\underbrace{\textstyle\sum_i u_i(\lambda)\,m_i(\lambda;\Theta)=1}_{\text{Bézout}},\quad
\deg u_i\le \dim V,\quad \Theta\ \text{满足}\ (5a)\ \text{的秩条件}.$$

因为每个 $m_i$ 对 $\Theta$ 的次数 $\le s$、对 $\lambda$ 的次数 $\le\dim V$，把 $u_i$ 的系数当变量后，
$\sum_i u_i m_i=1$ 是**对 $u$ 线性、对 $\Theta$ 次数 $\le s$** 的方程组；$(5a)$ 的秩条件用"某组固定子式非零"表达
（非零约束）。变量数 $O(d(k-d)+s\dim V\cdot\#i)$，度数 $\le s$ ⟹ 落在 $\exists\mathbb R$ 框架内（专家 §3.1）。

**关键结构问题**：这套系统对 $\Theta$ 的次数是 $s$（一般 $\ge2$），不是线性——除非 $r=1$ 让 $s$ 或
$\Theta$-依赖退化。下面的实验测这一点。

### (B) 结构实验（中点封闭性）

[r1_structure.py](../../../../tools/verification/r1_structure.py)：对 $r=1$、$q=q_0$ 的实例（$d(k-d)\le4$），
在图卡上网格扫描，收集可行集 $\mathcal A$ 与好集 $\mathcal G$（$(5a)$ 且 $(5b)$），
检验 $\Theta_1,\Theta_2\in\mathcal A\Rightarrow(\Theta_1+\Theta_2)/2\in\mathcal A$。

## 进展

| 实例 | $d$ | $k$ | $|\mathcal A|$ | $|\mathcal G|$ | 中点仍可行 |
|---|---|---|---|---|---|
| $n=5,p=1$ seed 3000, $q=2$ | 2 | 3 | 7 | **0** | 20/21 |
| seed 3006, $q=3$ | 1 | 3 | 44 | **0** | 36/40 |
| seed 3021, $q=2$ | 2 | 3 | 7 | **0** | 21/21 |
| seed 3025, $q=2$ | 2 | 3 | 1 | **1** | （无可测配对）|
| seed 3028, $q=2$ | 2 | 3 | 6 | **0** | 12/15 |
| seed 3041, $q=2$ | 2 | 3 | 7 | **0** | 21/21 |

两条观察：

1. **可行集接近仿射但不等同**：多数配对的中点仍可行（20/21、21/21、21/21），但也有明显失败
   （12/15、36/40）⟹ $(5a)$ 的解集是**真正的代数子簇**，不是仿射集；
2. **好集极薄**：网格上通常 $|\mathcal G|=0$ 或 $1$ ⟹ 谱可行集是余维 $\ge1$ 的子集，
   这与"$q_0$ 阶抽样命中率低"的现象一致。

## 最终结论

1. **显式代数系统已写出**：$\exists\Theta\exists u$ 的 Bézout 形式，变量数与度数均多项式，
   与专家 §3.1 的描述一致——这是 $\mathrm{DEC}(q)$ 的规范代数表述；
2. **结构性猜想被否定（至少在这批实例上）**：$(5a)$ 解集不是仿射集（中点失败 12/15、36/40），
   因此"$r=1$ 时退化为线性 ⟹ 多项式算法"这条捷径**不成立**；
3. **好集是薄的**（$|\mathcal G|\le1$ 常见），所以"随机/网格找可行点"在 $r=1$ 上也不可靠——
   必须解系统；
4. 于是 $r=1$ 的复杂度问题仍**开放**：现在的规范表述是一个 $\exists\mathbb R$ 问题，
   既没有多项式算法，也没有归约靶子。

## 放弃原因

不适用（结构与表述完成）。**未做**：$r=1$ 的多项式算法或归约——需要新的结构想法
（例如利用 $r=1$ 时 $P_{\mathcal Z}$ 的特殊分块，或好集的余维结构）。

## 残留价值

* $\mathrm{DEC}(q)$ 在 $r=1$ 时的**显式 $\exists\mathbb R$ 表述**（变量、方程、度数都写清）；
* 一条**否定的结构结论**：$(5a)$ 解集非仿射，堵死了"线性退化 ⟹ 多项式"的捷径；
* 好集薄性的定量观察（网格上 0–1 个点），解释了此前所有"低命中率"现象。

## 相关文件

- [tools/verification/r1_structure.py](../../../../tools/verification/r1_structure.py)
- [workspace/for_expert/06_state_corrections_and_assessment-answer.md](../../../for_expert/archive/06_state_corrections_and_assessment-answer.md)（§3.1–§3.2）
- [workspace/q1_false/feasibility_geometry/attempts/34_q1_closed.md](34_q1_closed.md)（零空间铅笔判据）
- [proof/dec_q_existsR/bitsize.md](../../../../proof/dec_q_existsR/bitsize.md)（编码规模）
