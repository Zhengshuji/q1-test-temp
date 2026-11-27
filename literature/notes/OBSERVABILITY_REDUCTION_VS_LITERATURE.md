# 可观性归约 vs 文献（2026-11-04，应专家 §Q5 要求）

## 三种表述的对照

| 表述 | 谱条件的形状 | 出处 |
|---|---|---|
| 原始观测器形式 | 对**每个** $\lambda$ 的秩条件 | 文献（P1/P2 的 (14b)）|
| 零空间铅笔 | $\operatorname{rank}\big((\lambda I-A)V\mid Z\big)=\operatorname{rank}(V\mid Z)$ | 文献（P2 Thm 4）——**本项目只引用，不声称新** |
| 本项目（B.12）| $(E,\Lambda)$ 可观测，$\ker E=\mathcal L(V)$；等价于 $\operatorname{rank}[E;E\Lambda;\dots]=q$ | 专家给出、本项目核验（L1 + 44/44）|

## 可以声称的增量（专家 §Q5 的措辞）

> We derive an equivalent finite-dimensional observability test for the spectral condition of a fixed
> algebraically admissible augmentation.

即：**不得**声称 PBH 或"零空间/铅笔刻画"是新的；可能新的是
(a) 从增广方程导出具体这对 $(E,\Lambda)$，(b) 由此得到的紧凑 $\exists\mathbb R$ 证书（G.2）。

## 待办

* 把 Darouach & Fernando (Automatica 2025) 与 P2 的谱条件小节逐条对照，写进论文的 related-work 一节；
* 论文引言用上面的三行表说明关系与增量。
