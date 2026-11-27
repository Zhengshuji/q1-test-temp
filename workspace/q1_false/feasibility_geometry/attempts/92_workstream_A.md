# Workstream A 完成：B.25（矩形铅笔 $D-\lambda U$ 判据）+ WorkA.lean（秩公式，exit=0）

## 目标

按专家 2026-11-05 §8 的 Workstream A：
1. 把 B.24' 提为主定理（已在上一轮完成）；
2. **写出坐标形式**：矩形铅笔 $D-\lambda U$；
3. **接到 Smith/gcd 工具**；
4. 形式化优先级 1–3 中的前两项（秩公式、块因子化）。

## 设想与理由

$W=\mathcal LV$ 取基 $U$（$q\times k$，$k=h-r_1$），$\Phi$ 在这组基上的像给出 $D$。则
$$\Phi(Ua)=Da,\qquad (5b)\ \text{失败}\iff\exists\lambda:\operatorname{rank}(D-\lambda U)<k,$$
这正是**矩形广义特征值问题**，其判据是"$k$ 阶极大子式 gcd 有正次数"——与 B.8a 的 Smith 判据同一件事。
于是谱条件与既有的多项式矩阵工具（gcd/不变因子）**直接接上**。

## 做法

1. 写 B.25（判据 + gcd 形式 + 次数界 + 与 Smith 的连接）；
2. 新增 `WorkA.lean`：秩公式 $\dim\operatorname{range}(PH)+\dim(\ker P\cap\operatorname{range}H)=\dim\operatorname{range}H$
   （专家优先级 1），用显式线性同构 $\ker(P|_S)\simeq S\cap\ker P$；
3. 登记 STATEMENT_MAP / 覆盖率表 / docs 等级行。

## 进展

| 项 | 结果 |
|---|---|
| **B.25（已证）** | $(5b)$ 失败 $\iff\exists\lambda:\operatorname{rank}(D-\lambda U)<k$ $\iff$ 极大子式 gcd 正次数 $\iff$ Smith 形有非常数不变因子 |
| 次数界 | 极大子式次数 $\le k$ ⟹ 判据是"有限个次数 $\le k$ 的多项式有公根" |
| 精确验证 | 3453/3453（gcd 有正次数 $\iff$ B.12 判据失败）|
| **WorkA.lean** | **exit=0、0 error 0 warning**：`WorkA.kerRestrictEquiv`、`WorkA.finrank_range_comp`（**秩公式**，专家优先级 1）|
| 登记 | STATEMENT_MAP **180 声明 / 170 条目 / 0 问题**；B.23 覆盖行与等级行升级为 ✓ [Lean-conditional] |

## 最终结论

1. **Workstream A 的数学部分完成**：谱条件 = 矩形铅笔 $D-\lambda U$ 的广义特征值问题 = gcd/Smith 判据；
2. **形式化优先级 1 完成**（秩公式）；优先级 2（块因子化的矩阵实例化）仍需 $\lambda$-依赖的矩阵运算层；
3. $\Phi$ 的良定义与"$K_1|_W$ 唯一"是纸面（专家 §2.1），未形式化。

## 放弃原因

不适用（A 的数学部分已完成；矩阵层形式化留待后续）。

## 残留价值

* **B.25**：把谱条件与多项式矩阵工具接上的桥；
* **WorkA.lean**：秩公式（可复用）；
* 一份明确的"剩余形式化清单"（块因子化实例化、$\lambda$-矩阵运算、$\Phi$ 良定义）。

## 相关文件

- `docs/02` B.25、B.23（等级升级）
- `tools/lean/MyProof/WorkA.lean`、`tools/lean/STATEMENT_MAP.md`、`proof/lean_coverage.md`
- `tools/verification/partial_operator.py`
- 专家答复：`workspace/for_expert/archive/19_spectral_pair_and_class_I-answer.md` §8
