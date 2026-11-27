# Majumdar (2026), *Affine Rank Minimization is ER Complete* — 阅读笔记

> arXiv:2602.14037v1（2026-02-15），45 页，cs.CC。
> 作者：Angshul Majumdar（Indraprastha Institute of Information Technology, Delhi）。
> 读取日期：2026-11-09。全文：`literature/papers/2602.14037.{pdf,txt}`。

---

## 1. 问题与结果

**ARM(k)**：给定有理 $A_\ell\in\mathbb Q^{m\times n}$、$b_\ell\in\mathbb Q$，问是否存在实 $X$ 使
$$\langle A_\ell,X\rangle=b_\ell\ (\ell=1,\dots,q),\qquad \operatorname{rank}X\le k.$$

- **Thm 2.8（成员）**：固定 $k\ge1$，ARM(k) ∈ ∃R（因子见证 $X=UV$，常数大小）。
- **∃R-硬度**：从 ETR 多项式时间多一归约；**ARM(3) 已 ∃R-完全**。
- 输出实例保持多项式维数与比特长；约束只有**仿射等式 + 单一全局秩约束**。

## 2. 归约结构（对观测器最相关）

1. ETR 公式 → 算术电路，**gate-equality normal form**；
2. 每个门量放进 $X$ 的指定条目；常数/复制/加法/取负由**线性约束**实现；
3. 乘法由**常数大小 rank-forcing gadget** 实现：
   - 违反 $z=xy$ 会迫使某个 $4\times4$ 子矩阵满秩，与 $\operatorname{rank}X\le3$ 矛盾；
   - 满足时给出显式 rank-3 完成；
4. **gauge block**：固定一个满秩 $3\times3$ 子矩阵，消除 rank-3 分解的基变换歧义；
   保证所有可行 rank-3 实现解码出的 carrier 值一致；
5. **composition lemma**：gadget 嵌入无隐藏耦合，全局 sound + complete。

## 3. 与本项目的关系

- 这是**最接近的代数源**：仿射约束 + 单一全局秩约束；
- 观测器侧的差别：$H=LN$、$H_A=LAN$ **同源耦合**，且还有谱条件；ARM 的 $X$ 完全自由；
- 可借鉴的三件技术：**违反 ⇒ 满秩子式**、**gauge block 去歧义**、**composition lemma**；
- 若能把观测器的压缩对模拟成 ARM 的“带 gauge 的 $X$”，硬度路线可大大缩短；
  但目前没有这个模拟（$H,H_A$ 不能独立选择）。
