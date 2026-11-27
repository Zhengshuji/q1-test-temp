# 路线 4：$\rho_{ci}$ 的闭式

## 目标
给出"最小可行 $\rho$"的闭式：$\rho_{ci}=\min\{\operatorname{rank}(\mathcal V N):\ \mathcal V\ \text{满足}\ (5a)\}$。

## 设想与理由
$(5a)$ 只依赖 $\mathcal V$ 的"ci 结构"。若最小 ci 子空间（按维数）唯一，则 $\rho_{ci}$ 就是它的 $\operatorname{rank}(\mathcal V N)$ —— 一个 $O(n^3)$ 的闭式。

## 做法
- 早期：`c125_rho1_criterion.py`、`c154_verify_rho_min_formula.py`、`c155_dimension_law.py`（在 `archive/old_scripts/core/`）；
- 本会话：`c190_invariant_family.py`、`c191_pbh.py`、`c192_reduced_search.py`（`tools/certificates/`、`tools/layer_search/`）。

## 进展
1. 早期闭式 $A^{\mathsf T}Z\subseteq Z+K$ 形式：**5/25 不符**（自行作废）。
2. "最小 ci 子空间唯一"：**假**。$\mathbb F_5$ 上出现 25/125/5 个互不包含的极小元；$\mathbb Q$ 上出现两个极小元在同一个 $\dim$ 层但 $\rho$ 不同（$(0,2)$ 与 $(1,1)$）。
3. 推论：$\rho$ 在极小 ci 元上**不恒定** ⟹ 不存在"取一个极小元再算 $\rho$"的闭式。

## 最终结论
**推翻**。

## 放弃原因
具体卡在：ci 族对**和**封闭、对**交**不封闭（半边格），最小元不唯一；而 $\rho$ 与"包含极小"不一致。

## 残留价值
- **$\rho_{ci}=P(T,B,U_0)$**：把"最小 ci 子空间"换成"最小**维数** $(A,B)$-不变子空间"后，问题变成 $P$ —— 现在**已多项式**（[proof/p_is_polynomial/](../../../proof/p_is_polynomial/README.md)）。
  $$\text{这是本路线最重要的遗产：}\rho_{ci}\ \text{可算。}$$

## 相关文件
- [q1_false/attempts/archive_attack_log/03_D10-D16_layers.md](archive_attack_log/03_D10-D16_layers.md)
- `tools/certificates/c190_invariant_family.py`、`tools/layer_search/c192_reduced_search.py`