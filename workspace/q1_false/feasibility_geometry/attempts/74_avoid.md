# Q3 的定型：AVOID —— 带约束的"正则子铅笔"问题

## 目标

专家 2026-11-04 §Q3/§7 把"认清确切的秩可行性问题"列为第一优先，并指出：单-$\lambda$ 证书是多项式时间的
（两向量比例检验），真正的瓶颈是"存在子空间 $\mathcal Z$ 避开全部广义特征向量"。本轮把这个对象定型，
并核对文献里的对应概念。

## 设想与理由

由 B.13c：$(5b)$ 在 $\mathcal Z$ 处失败 $\iff\exists x\in V\setminus\mathcal Z,\lambda:(\lambda I-A)x\in\mathcal Z$。
取 $B_V$ 为 $V$ 的基、$\Pi$ 为满行秩且 $\ker\Pi=\mathcal Z$ 的矩阵（"杀掉 $\mathcal Z$"的投影），则

$$\text{失败}\iff\exists\lambda:\ \Pi(\lambda I-A)B_V\ \text{列降秩}.$$

于是

$$\textbf{AVOID}:\quad \exists\,\mathcal Z\le K,\ \dim\mathcal Z=d\ \text{使铅笔}\ \Pi_{\mathcal Z}(\lambda I-A)B_V
\ \text{对一切}\ \lambda\ \text{满列秩}.$$

这就是一个**带约束的子铅笔（subpencil）正则性**问题：要求在铅笔 $\lambda I-A$ 中挑一个
"行空间 $=V$、列方向的核 $\subseteq K$"的 $(\dim X-d)\times\dim V$ 压缩，且它在 $\mathbb C[\lambda]$ 上满列秩
（即**没有有限零点**）。等价的三种说法：

1. （B.13c）没有 $(x,\lambda)$ 满足 $x\in V\setminus\mathcal Z$、$(\lambda I-A)x\in\mathcal Z$；
2. （B.12）$(E,\Lambda)$ 可观测（$E$ 零化 $\mathcal LV$）；
3. （铅笔）$\Pi_{\mathcal Z}(\lambda I-A)B_V$ 的极大子式 gcd 为非零常数。

## 做法

1. 把 AVOID 写成上述三种等价形式，并核对它们共享的"约束"是什么；
2. 检索文献里"regular subpencil / 子铅笔正则性 / 压缩"的对应概念。

## 进展

**（1）定型**：AVOID 的约束有两条，且都是**实例给定**的：行空间必须是 $V=\ker[C;CA]$（不是任意子空间），
列方向的核必须落在 $K=\ker[C;L_0]$ 内（不是任意 $\mathcal Z$）。两条合起来使问题成为
"**受约束的 deflation/compression**"。

**（2）文献对应**（检索记录见 literature/SEARCH_LOG.md）：

* 经典概念是 **regular subpencil / 子铅笔的正则性**：把一个（可能正则的）铅笔压缩到给定的行列子空间上，
  问压缩是否正则；Kronecker 标准形给出**无约束**版本的完整答案（[Embedding a regular subpencil into a
  general linear pencil, LAA](https://www.sciencedirect.com/science/article/pii/S002437959900049X)、
  以及 Van Dooren 的 staircase/deflation 理论）；
* 无约束版本对 $\lambda I-A$（$E=I$ 可逆）是**容易的**：压缩的有限零点由 Kronecker 形直接读出；
* 我们的版本多两条约束（$V$ 固定、$\ker\subseteq K$），这两条**不是**坐标约束，因而是经典 Kronecker
  理论不直接覆盖的部分。

**（3）由此得到的判据式猜想（可检验）**：AVOID 的困难（若有）**完全来自约束**；若把 $V$ 换成任意子空间、
把 $K$ 换成整个空间，问题退化为经典子铅笔问题（Kronecker，多项式可解）。这与我们已知的两点一致：
(i) 单-$\lambda$ 证书（更弱的充分条件）是多项式判定的；(ii) (T*) 类（B.14）也是多项式判定的。

## 最终结论

1. **AVOID 的正式陈述**：$\exists\mathcal Z\le K$（$\dim d$）使压缩 $\Pi_{\mathcal Z}(\lambda I-A)B_V$ 在
   $\mathbb C[\lambda]$ 上满列秩；等价形式见上；
2. **文献名**：这是"**带约束的 regular subpencil**（子铅笔正则性 / deflation）问题"；无约束版是经典
   Kronecker 理论（多项式可解），所以**硬度（若有）只能来自 $V$ 与 $K$ 的约束**；
3. 这把 Q3 变成了一个**干净的可攻击问题**：要么证明受约束版本仍可多项式判定（那么 $q1$ 就不是这个原因难），
   要么把它归约到已知难问题（则 $q1$ 继承硬度）；
4. 已排除的"伪硬度来源"：单-$\lambda$ 条件、$(T^*)$ 类、固定尺寸版本（后者由定变量数量词消去多项式可解）。

## 放弃原因

不适用（定型完成；下一步是判定受约束版本）。

## 残留价值

* 一个**可攻击的干净问题**（AVOID）与三种等价形式；
* 文献定位（regular subpencil / deflation），并把"无约束易、受约束才可能难"这一直觉写成可检验的判据式；
* 明确了下一步的技术入口：**受约束 deflation** 的复杂度。

## 相关文件

- `docs/02` B.13c（失败判据）、B.12（可观性归约）、B.14（(T*) 可解类）
- literature/SEARCH_LOG.md（本轮检索记录）
- 专家答复：`workspace/for_expert/archive/13_spectral_structure-answer.md` §Q3/§7
