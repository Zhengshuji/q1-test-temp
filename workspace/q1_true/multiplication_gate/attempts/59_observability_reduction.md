# 核验专家的**可观性归约**：固定候选的谱检验降为 $q$ 维可观性秩计算

## 目标

专家 2026-11-04 §3 提出一个归约：$(5b)$ 等价于某个 $q$ 维**可观测性**条件。若能对上我们的定义，
固定候选的谱检验就从"极大子式 gcd / Smith 形 / 对所有 $\lambda$"变成一个**普通矩阵秩计算**。
本轮把它核验、写成命题、并对照既有三条判据。

## 设想与理由

由 $(5a)$ 取 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$，则 $Q_{\mathcal L}(\lambda)=D(\lambda)H$，其中
$H=[\mathcal L;CA;C]$、$D(\lambda)=\begin{pmatrix}\lambda I-\Lambda&-G_1&-G_0\\0&I&0\\0&0&I\end{pmatrix}$。
用 $\operatorname{rank}(DH)=\operatorname{rank}H\iff\ker D\cap\operatorname{im}H=0$：

* $\ker D(\lambda)=\{(u,0,0):(\lambda I-\Lambda)u=0\}$；
* $\operatorname{im}H=\{(\mathcal Lx,CAx,Cx):x\in\mathbb C^n\}$。

于是掉秩 $\iff\exists x\in V=\ker[C;CA]$ 使 $\mathcal Lx\ne0$ 且 $\Lambda\mathcal Lx=\lambda\mathcal Lx$，
即
$$(5b)\iff U:=\mathcal L(V)\ \text{不含}\ \Lambda\ \text{的非零特征向量}
\iff(E,\Lambda)\ \text{可观测}\ (\ker E=U)\iff\operatorname{rank}\mathcal O(E,\Lambda)=q .$$

## 做法

[observability_test.py](../../../../tools/verification/observability_test.py)：精确有理算术实现——
求因子化得 $\Lambda$、$M=\mathcal LV_0$、取 $\ker E=\operatorname{im}M$ 的零化子、算
$\mathcal O=[E;E\Lambda;\dots;E\Lambda^{q-1}]$ 的秩，与 Toeplitz 判据逐例对照。

## 进展

* **44/44 一致**（44 个 $(5a)$-可行候选，含 $V\cap\mathcal Z\ne0$ 的掉秩样本）。
* 实现中踩过一个错：解 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ 时**未知数编号与解包转置不一致**
  （首版 41/44，3 例把可行判为不可行）；修正后 44/44。这正是"证书脚本要先打印不变量"的又一次实例。
* 已写成 **B.12**（含逐步证明与"边界"说明）并记入 `docs/08` §2 的 2.6 行；
  同时按专家要求补上 C4 的 $q=4$ 显式见证（见 `proof/refuted/C4_type3_counterexample.md`）。

## 最终结论

1. 归约**正确**且与本项目定义对得上；固定候选的谱检验 = $q$ 维可观性秩检验（多项式时间）；
2. 它给 $\exists\mathbb R$ 编码一个更紧凑的证书（观测性矩阵左逆），且 $s=\operatorname{rank}\mathcal L(V)$
   只有 $q+1$ 种取值 ⟹ 层析取是多项式的（这是专家 §7 的建议）；
3. **但**：这是"给定 $\mathcal L$"的多项式时间检验；**不**给出选择 $\mathcal L$ 的多项式算法，
   也不改变 $q1$ 的开放状态（专家 §8 也这样强调）。
4. 专家的提醒："$r_1=p+r$"不是必然（支配性只给 $r_1\le p+r$），正确提法是 incidence variety 的维数界——
   已记入 `docs/08` §4.11.0。

## 放弃原因

不适用（核验完成）。

## 残留价值

* 一个**可替代 gcd/Smith 的谱判据**（更简单、更快、更容易做成证书）；
* 明确的边界（候选级 vs 选择级），避免把"固定候选可判"误读成"问题可判"；
* 实现陷阱的记录（转置编号不一致），可作为"证书脚本先打印不变量"的范例。

## 相关文件

- [tools/verification/observability_test.py](../../../../tools/verification/observability_test.py)
- [docs/02_theorems_proven.md](../../../../docs/02_theorems_proven.md) B.12
- [docs/08_results.md](../../../../docs/08_results.md) §2 的 2.6 行、§4.11.0
- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)（$q=4$ 见证）
- [workspace/for_expert/archive/10_status_and_direction-answer.md](../../../for_expert/archive/10_status_and_direction-answer.md)（专家 §3/§7/§8）
