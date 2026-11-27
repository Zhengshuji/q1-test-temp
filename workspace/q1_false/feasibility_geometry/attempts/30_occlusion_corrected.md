# 遮蔽判据的修正：需要 $h=n$，且用像的维数而非满射

## 目标

落实专家 2026-11-03 §4 对"坏点像遮蔽"论证（[attempts/27](27_bad_locus_blocking.md)、[attempts/26](26_c4_proof.md)）的两条更正，
给出可以直接使用的充分条件。

## 设想与理由

原文论证：$z(x)=(\\lambda(x)I-A)x\\in\\mathcal Z$ 时 $Q_{\\mathcal L}(\\lambda(x))x=0$，$x\\ne0$，于是"掉秩"。
专家指出：**这个推理只在 $h=n$ 时成立**——$Q_{\\mathcal L}$ 有 $n$ 列、参考秩 $h$；$h<n$ 时非零核向量**不**蕴含
$\\operatorname{rank}<h$。因此定理必须显式假设"该阶的每个可行候选都满足 $h=n$"。

第二条：满射不是必要条件。令 $Y=\\overline{\\Phi(\\mathbb P(V))}\\subseteq\\mathbb P(K)$、$m=\\dim Y$、$k=\\dim K$；
每个 $\\mathcal Z$ 是 $K$ 的 $d$ 维子空间，$\\mathbb P(\\mathcal Z)$ 是 $\\mathbb P^{k-1}$ 中的 $(d-1)$ 维射影平面。
射影维数定理给出：若
$$m+(d-1)\\ \\ge\\ k-1\\iff \\boxed{\\,m\\ge k-d=q-r\\,},$$
则 $Y$ 与**每个**这样的平面相交。于是"遮蔽"的充分条件从"$\\Phi$ 满射"放宽为"$\\dim Y\\ge q-r$"。

第三条：有理映射的延拓只在曲线情形成立（$\\mathbb P^1$）；高维时**不能**假设延拓为态射，须用"像的闭包"。

## 做法

1. 对 C4 实例（[attempts/26](26_c4_proof.md)）复核：$h=s_0+t=6=n$ ✓、$\\dim V=\\dim K=2$（$\\mathbb P^1\\to\\mathbb P^1$）⟹
   专家的修正不影响该证明，且曲线情形延拓成立 ✓；
2. 在本次实验里检索"$h<n$ 但构造出非零核向量"的情形，确认原文若不加 $h=n$ 会过强。

## 进展

**修正后的定理（可直接引用）**：

> 设阶 $q$ 的每个可行增广都满足 $h=n$（等价地 $\\mathcal Z^{\\perp}+W=\\mathbb C^n$，从而 $(5a)$ 自动成立）。
> 令 $Y$ 为坏点映射 $\\Phi$ 的像的射影闭包。若 $\\dim Y\\ge q-r$，则该阶无解。

**C4 的复核**：$n=6$、$h=6=n$ ✓；$q=r+1$ ⟹ $q-r=1$；$\\dim Y=\\dim\\mathbb P^1=1\\ge1$ ✓，条件满足 ⟹ 无解 ✓
（与原文结论一致，但依据换成了正确的像维数条件）。

**$h<n$ 的注意点**：在 $h<n$ 的阶上，$Q_{\\mathcal L}(\\lambda)x=0$ 还需 $x$ 落在"掉秩子空间"里才推出失败；
本项目的实测（[type_criterion.py](../../../../tools/verification/type_criterion.py)）显示这类阶上 $h$ 是常数，
但"非零核向量 ⟹ 失败"**不能**直接使用。

## 最终结论

1. **遮蔽定理的假设**：$h=n$（每候选）；结论：$\\dim Y\\ge q-r\\Rightarrow$ 该阶无解；
2. **不再用"满射"**，改用像的闭包维数（更弱、更易满足；$\\mathbb P^1\\to\\mathbb P^1$ 时两者等价）；
3. **有理映射延拓**只在曲线情形引用；高维用像的闭包；
4. C4 的整族不可行证明**不受影响**（它恰满足 $h=n$ 与 $q-r=1$）。

## 放弃原因

不适用（更正完成）。**未做**：$\\dim Y$ 的一般计算方法（需要消元/像的闭包维数）。

## 残留价值

* 一个**正确的**充分条件（可直接用于排除整个阶）；
* 明确指出原论证的隐含假设（$h=n$），避免在 $h<n$ 的阶上误用；
* 与 C4 的既有证明兼容，且给出了它满足条件的具体数值（$h=n=6$、$q-r=1$、$\\dim Y=1$）。

## 相关文件

- [workspace/for_expert/05_integer_obstruction_occlusion_anomaly-answer.md](../../../for_expert/archive/05_integer_obstruction_occlusion_anomaly-answer.md)（专家 2026-11-03 答复 §4）
- [workspace/q1_false/feasibility_geometry/attempts/26_c4_proof.md](26_c4_proof.md)
- [workspace/q1_false/feasibility_geometry/attempts/27_bad_locus_blocking.md](27_bad_locus_blocking.md)
- [tools/verification/regression_Lstar.py](../../../../tools/verification/regression_Lstar.py)
