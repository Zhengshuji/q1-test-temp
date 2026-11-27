# 按专家 2026-11-03 答复推进：T 被推翻、坏 λ 定位、三项技术更正

## 目标

落实专家 2026-11-03 答复中的：

* **§Q6 最高优先**：定向寻找 Type III 反例（证伪 T）；
* **§技术注 1–4**：数 vs 和、行满秩显式化、"证明 T ⟹ 多项式"的软化、三层区分；
* **§Q2**：把 $(\star)$ 写成嵌入形式 $\operatorname{im}H\cap J\ker(\lambda I-\Lambda)=0$；
* **§Q3**：把 II.7 的无条件蕴含改成条件形式。

## 设想与理由

专家指出：先前的"175 个样本无 Type III"不足以支持 T，且**实例族太窄**（无重复特征值/Jordan 块、$p\le2$）。
他建议按结构化 $A$（对角互异/重复、Jordan 块）、$p\ge3$、正维数族来定向搜索。

## 做法

1. [type3_structured.py](../../../../tools/verification/type3_structured.py)：三族结构化 $A$
   （对角互异、对角重复、Jordan 块）× $p\in\{2,3\}$ × $r\in\{1,2\}$；Z-参数化在 $q_0$ 阶抽样；
   $d_{\\rm fin}$ 用 Toeplitz 零度快速算；**确定性种子**（可复现）；
2. [verify_C4_type3.py](../../../../proof/refuted/verify_C4_type3.py)：反例的三重核验（Toeplitz/Smith、零空间判据、逐条 assert）；
3. [type3_bad_lambda.py](../../../../tools/verification/type3_bad_lambda.py)：坏 $\lambda$ 的直接定位（扫有理 $\lambda$）。

## 进展

**反例（T 被推翻）**：$n=6$、$A$ 为三个 $2\times2$ Jordan 块（特征值 $1,2,1$）、$p=r=2$、$r_1=4$、$q_0=3$，
$$L=\begin{pmatrix}0&0&8&20&1&4\\1&3&0&0&0&0\\0&0&1/4&1&0&0\end{pmatrix}$$
满足 $(5a)$、含 $L_0$、$\operatorname{rank}L=3$，且 $h=6<7=q_0+r_1$、$k=1\le s=3$、$\varepsilon=[1]$、$d_{\\rm fin}=2>0$。

* Toeplitz/Smith：`five_b=False`、`d_fin=2`；
* 零空间判据：极大子式 gcd 次数 $=2$；
* 坏 $\lambda$：$5/3$ 与 $3$（另一候选为 $\lambda=1$ 重根）。

**统计**：22 个结构化实例、212 个 $q_0$ 阶样本、45 个 $h<q_0+r_1$，其中 **17 个 Type III**。

## 最终结论

* **T 是错的**：零指标障碍不是最小阶的唯一障碍；
* 先前的 175 个"无反例"样本是**实例族太窄**的结果——专家的结构化建议立刻命中；
* 坏 $\lambda$ 可精确到有理数，$(\star)$ 的嵌入形式提供了正确的机制语言；
* 已按 §技术注 1–4 更正文档（数/和分开、行满秩显式、软化多项式结论、三层区分）。

## 放弃原因

不适用（目标达成）。**未做**：专家 §B/§C 两项（符号证明公开例子在 $q_0+1$ 阶的 $h=q+r_1$ 全族性质；
$q_0$ 阶完备族的图卡方程）——都需要符号消元，当前环境无 CAS。

## 残留价值

* 一个**已证伪的猜想 + 精确反例 + 坏 $\lambda$ 定位**，把"最小阶判定"从"整数条件"拉回真正的谱分析；
* 结构化实例生成器与定向搜索框架（可复现，确定性种子）；
* 机制语言 $(\star)$ 与"坏 $\lambda$"的连接，可用于后续的 Type III 分类。

## 相关文件

- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)
- [tools/verification/type3_structured.py](../../../../tools/verification/type3_structured.py)
- [tools/verification/type3_bad_lambda.py](../../../../tools/verification/type3_bad_lambda.py)
- [proof/refuted/verify_C4_type3.py](../../../../proof/refuted/verify_C4_type3.py)
- [workspace/q1_false/feasibility_geometry/attempts/09_T_proof_attempt.md](09_T_proof_attempt.md)（$(\star)$ 的来源）
