# 中间层：结构限制（A(V∩Z) ⊆ Z）+ 一个"铅笔不满秩但可行"的显式反例

## 目标

B.16 只给了中间层（$0<s<\dim V$）的**核判据**。本轮回答两个问题：
(1) 中间层的可容许增广受什么结构限制？(2) 中间层上"铅笔不满列秩"是否等于失败？

## 设想与理由

由 $(5a)$ 可写 $\mathcal LA=T[\mathcal L;CA;C]$。若 $x\in S=V\cap\mathcal Z$，则 $\mathcal Lx=0,Cx=CAx=0$，
故 $(\mathcal LA)x=0$，即 $\mathcal L(Ax)=0$；又 $C(Ax)=CAx=0$，于是 $Ax\in\ker[C;\mathcal L]=\mathcal Z$。
⟹ **$A(S)\subseteq\mathcal Z$ 是必要条件**（不强于 $(5a)$，但很有约束力）。

## 做法

1. 证明上述必要条件（三行）；
2. 在 $n=6,p=r=2$（$\dim V=\dim K=2$）、$d=2$（$\mathcal Z=K$ 唯一、$s=1$）的随机实例里**定向搜索**：
   要求 $\dim(V\cap K)=1$ 且 $A(V\cap K)\subseteq K$，再看 $(5a)$ 是否成立；
3. 对找到的实例核验 $(5a)$、$(5b)$（B.12）与铅笔 $N_{\mathcal Z}(\lambda)$ 的秩。

## 进展

**（1）必要条件已证**：$(5a)\Rightarrow A(V\cap\mathcal Z)\subseteq\mathcal Z$。
推论：若还有 $A(S)\subseteq S$ 且 $S\ne0$，则 $S$ 是 $\ker C$ 内的 $A$-不变子空间，与 $(C,A)$ 可观测矛盾。

**（2）定向搜索（20000 次随机）**：

| 阶段 | 计数 |
|---|---|
| $\dim(V\cap K)\ne0$ | 53 |
| 其中 $A(V\cap K)\subseteq K$ | **1** |
| 且 $(5a)$ 成立（该 $\mathcal Z=K$ 可容许）| **1** |

即中间层的可容许实例**确实存在，但极稀有**（$52/53$ 被必要条件一票否决）。

**（3）找到的实例（$s=1$）**：

* $(5a)$ 成立；$\operatorname{rank}\mathcal L=2=q$；
* $(5b)$ 经 B.12 核验**成立**（$\operatorname{rank}\mathcal O=2=q$）；
* 而铅笔 $N_{\mathcal Z}(\lambda)$ 在 $\lambda=0,\pm1,\pm2,3$ 处秩**恒为 1** $<2=\dim V$。

$$\boxed{\text{"压缩不满列秩"}\ne\text{谱失败}}$$

这正是专家 2026-11-04 §1.4 的告诫，现在有了显式实例；也说明中间层**必须**用 B.16(c) 的核判据。

## 最终结论

1. **B.16b**：$(5a)\Rightarrow A(V\cap\mathcal Z)\subseteq\mathcal Z$（已证）；
2. 中间层可容许实例存在但极稀有（1/20000 随机；52/53 因必要条件不满足被排除）；
3. 中间层上"铅笔秩跌破"**不等于**失败——已给出显式反例（$s=1$、铅笔秩恒 1、$(5b)$ 成立）；
4. 因此 B.16 的三层判据中，(b) 只在 $s=0$ 有效，(c) 是通用的。

## 放弃原因

不适用。

## 残留价值

* 一条**结构限制**（$A(S)\subseteq\mathcal Z$），可用来快速排除大量候选（实验中 52/53）；
* 一个**显式反例**，把"秩跌破 ≠ 失败"从口头提醒变成可复现事实；
* 明确了中间层的判据只能用核形式，避免今后误用"满列秩"作为充要条件。

## 相关文件

- `docs/02` B.16、B.16b、B.13c、B.14
- tools/verification/middle_strata.py（分层采样：$s>0$ 的可容许样本 0/12540）
