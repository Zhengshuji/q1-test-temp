# 猜想 T 的证明尝试：因子化路线的中间结果与瓶颈

> **2026-11-03 更正**：T 已被推翻（见 [C4](../../../../proof/refuted/C4_type3_counterexample.md)），
> 本文档的证明尝试因此**作废为历史**；但其中 $(*)$ 的结构性改写仍然成立且有用。

## 目标

证明**猜想 T**：在 $q=q_0$ 处，
$$(5b)\iff h<q_0+r_1 .$$

## 设想与理由

用 $(5a)$ 的因子化（P1 §V / 本项目 `5a_archive`）：存在 $\Lambda,G_0,G_1$ 使
$$\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA,\qquad Q_{\mathcal L}(\lambda)=D(\lambda)H,$$
$$D(\lambda)=\begin{pmatrix}\lambda I-\Lambda&-G_1&-G_0\\0&I&0\\0&0&I\end{pmatrix},\qquad H=[\mathcal L;CA;C].$$

于是（秩-零化度，**严格恒等式**）
$$\operatorname{rank}Q_{\mathcal L}(\lambda)=h-\dim\bigl(\operatorname{im}H\cap\ker D(\lambda)\bigr),$$
所以
$$\boxed{(5b)\iff \operatorname{im}H\cap J\ker(\lambda I-\Lambda)=\{0\}\quad\forall\lambda ,}\tag{$\star$}$$
其中 $Jv=(v,0,0)$。注意 $\ker D(\lambda)=\{Jv:(\lambda I-\Lambda)v=0\}$（专家 2026-11-03 §Q2 的收紧），
所以准确的说法是"**嵌入的特征空间** $J\ker(\lambda I-\Lambda)$ 不能落在 $\operatorname{im}H$ 里"，
而不是"$\Lambda$ 的谱避开 $\operatorname{im}H$"。

这是 $(5b)$ 的一个等价改写，把"秩不降"变成"$H$ 的像与 $D$ 的核不交"。
$\ker D(\lambda)$ 在 $\lambda\notin\sigma(\Lambda)$ 时是 $2p$ 维的；当 $\lambda\in\sigma(\Lambda)$ 时多出
$\ker(\lambda I-\Lambda)$，**谱障碍正是从这些特征方向漏进来的**。

## 做法

1. 写出 $(\star)$ 并核对它与既有判据等价（代数上直接由秩-零化度得到）；
2. 分析 $(\star)$ 在 $q=q_0$ 处为什么该蕴含 $h<q_0+r_1$。

## 进展

$(\star)$ 成立。要进一步证 T，需要下面这一步：

> **待证子命题（已按专家 2026-11-03 的意见收紧为条件形式）**：设 $\mathcal L$ 是 $q_0$ 阶、
> 满足 $(5a)$ 且 $h<q_0+r_1$ 的增广。若 $(5b)$ 失败，则存在维数 $<q_0$ 的 $(5a)$-可行增广
> （与 $q_0$ 的最小性矛盾）。

**为什么必须收紧**：无条件的"$(5b)$ 失败 ⟹ 更小增广"是**错的**——公开两阶差例子在 $q_0=3$ 处
就有失败的增广，而 $q_0$ 已是代数最小阶（专家 2026-11-03 §Q3）。$h\ge q_0+r_1$ 的情形本来就允许失败，
不该期望更小的增广。

这一步**本轮没有做出来**。难点在：$\operatorname{im}H\cap\ker D(\lambda)\ne0$ 只给出一个
"谱方向" $z\in\operatorname{im}H$ 被 $D(\lambda)$ 杀掉，但**不直接给出**一个更小的可行行空间——
它给出的是"$\Lambda$ 的某个特征方向与 $\operatorname{row}\mathcal L$ 的关系"，
而 $(5a)$ 的可行性约束在 $\operatorname{row}\mathcal L$ 上，不在 $\Lambda$ 上。

另一条可能的路线：把 $(\star)$ 与"$\Lambda$ 的特征向量在 $H$ 的像里"等价化，再用
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ 与 $h<q_0+r_1$（即 $q_0+r_1-h\ge1$，
非零左指标存在）比较维数——但这只给出维数不等式，**没有**给出矛盾。

## 最终结论

* 得到 $(5b)$ 的一个**结构性等价改写** $(\star)$：$\operatorname{im}H\cap\ker D(\lambda)=0\ \forall\lambda$；
* 把 T 化归为一个清晰的子命题（"有谱方向被 $D$ 杀掉 ⟹ 存在更小的可行增广"），但**未证**；
* 本轮**没有**证明 T，也没有找到反例（前一轮 175 个 $h<q_0+r_1$ 样本无反例）。

## 放弃原因

子命题需要把"$\Lambda$ 的特征方向"翻译回"更小的可行行空间"，这一步没有进展：
$(5a)$ 的约束在行空间上，谱条件在 $\Lambda$ 上，两者的联系只通过 $H$ 与 $D$ 的乘积——
目前只能得到等价改写，不能得到"更小可行空间"的构造。

## 残留价值

* $(\star)$ 可以直接当作**判据的实现方式**（比 Smith 形更结构化：只需检查 $H$ 的像与 $D(\lambda)$ 的核）；
* 一个明确的子命题作为后续目标（若证出，T 成立，$q_0$ 阶判定即多项式）；
* 记录了"为什么这一步难"：$(5a)$ 与谱条件的接口是 $H$ 与 $D$ 的乘积，而不是共享的行空间。

## 相关文件

- [workspace/q1_false/feasibility_geometry/attempts/08_failure_types.md](08_failure_types.md)（T 的数据）
- [tools/verification/type3_search.py](../../../../tools/verification/type3_search.py)（反例搜索）
- [proof/left_index_count/](../../../../proof/left_index_count/README.md)（B.9）
- [proof/5a_archive/](../../../../proof/5a_archive/README.md)（因子化 $LA=\Lambda L+G_0C+G_1CA$）
