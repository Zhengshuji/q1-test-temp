# 路线 2：层公式（$q(\rho)$ 表）

## 目标
证明 $q_{\min}=\min_{\rho}q(\rho)$ 有一条**闭式**，其中 $q(\rho)$ 是固定 $\rho=\operatorname{rank}(\mathcal LN)$ 层的最优 $q$。

## 设想与理由
单个闭式被反例打死后，改为"分层 + 每层一个公式"，希望每层的公式简单（如 $\rho+1$、$\rho+c_0$ 等）。

## 做法
`archive/process_logs/LAYER_AUDIT_2026-10-24.md` + `q1_false/attempts/archive_attack_log/03_D10-D16_layers.md`、`05_D27-D35_formulas.md`；
工具 `tools/verification/c166_layer_audit.py`、`c167_probe_tightness.py`。

## 进展
| 候选 | 结果 |
|---|---|
| $q(\rho)=\rho+1$（每层）| 70 对 $(\text{实例},\rho)$ 中 **69 紧、1 例外** |
| 例外 | `refute_dimV1` 的 $\rho{=}1$ 层需 $q{=}3$ 而非 2；**已证**：这正是"$L_0$ 本身是解"的退化层，与公式无关 |
| $q_{\min}=\max(r,\rho^*+1)$ | 被 $S=\mathcal J$ 族推翻（$q_{\min}=n$）|
| $q_{\min}=\max(r+\varepsilon,\rho^*+1)$ | 同上（$\varepsilon$ 项）|
| $F_3=\max(r+\varepsilon,\rho^*+\max(c_0,1))$ | 被 $n{=}4$ 反例推翻（$c$ 可被顶到 2）|

## 最终结论
**分层结构正确，但"每层有简单闭式"是错的**。层内 $c$ 的取值不由 $c_0$ 决定。

## 残留价值
- $q_{\min}=\min_\rho q(\rho)$ 与 $q=\rho+c$ 的分解 —— 现已升格为 [docs/04](../../../docs/04_structure.md) 的主分解。
- 紧性审计工具（`c166`/`c167`）与 70 对数据。

## 相关文件
- [05_D27-D35_formulas.md](archive_attack_log/05_D27-D35_formulas.md)
- [q1_false/attempts/03_middle_layer.md](03_middle_layer.md)