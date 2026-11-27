# B.25 · 矩形铅笔与 gcd 判据

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.25` 条目（§0.1 归并表）。

## 命题

**B.25（Workstream A：矩形铅笔 $D-\lambda U$ 与 gcd 判据）** 设 $\mathcal L$ 可容许、$W=\mathcal LV\subseteq\mathbb C^q$、$\Phi$ 如 B.24。
取 $U\in\mathbb C^{q\times k}$ 列满秩、$\operatorname{col}U=W$（$k=\dim W=h-r_1$），并令 $D\in\mathbb C^{q\times k}$ 的第 $i$ 列为 $\Phi(u_i)$
（$u_i$ 为 $U$ 的第 $i$ 列），则 $\Phi(Ua)=Da$。于是

1. **矩形广义特征值判据**：
$$(5b)\ \text{失败}\iff\exists\lambda\in\mathbb C:\ \operatorname{rank}(D-\lambda U)<k ;$$
2. **gcd 判据**：$\iff$ 矩形铅笔 $D-\lambda U$（$q\times k$，法秩 $k$）的 $k$ 阶极大子式的 gcd 是**正次数**多项式
   （等价地：它在 $\mathbb C[\lambda]$ 上的 Smith 形有非常数不变因子，即 B.8a 的 $d_{\rm fin}>0$）；
3. **次数界**：极大子式是次数 $\le k$ 的多项式，故失败判据是"有限个次数 $\le k$ 的多项式有公根"。

## 纸面证明

*证明*：1 由 $\operatorname{rank}(D-\lambda U)<k\iff\exists a\ne0:Da=\lambda Ua\iff\exists0\ne u=Ua:\Phi(u)=\lambda u$（B.24 第 3 条）。
2 由"多项式矩阵在某个 $\lambda$ 掉秩 $\iff$ 极大子式 gcd 有根 $\iff$ 正次数"（B.8a 的行列式因子论证）。3 直接。$\square$

*意义*：
* 这是把谱条件写成**一个矩形广义特征值问题**——正是我们先前定位的"约束子铅笔/AVOID"在 Class I 的具体形式；
* $U$ 由 $\mathcal L$（经 $W=\mathcal LV$）决定、$D$ 由 $\Phi=\mathcal L A|_V$ 决定，两者**同源**，耦合显式化；
* 与 Smith/gcd 工具直接相连：判定只需在 $\mathbb C[\lambda]$ 上算 $D-\lambda U$ 的不变因子。

## Lean（2026-11-06 已同步登记）

**[Lean-conditional]** —— 内核只覆盖代数/维数骨架，矩阵实例化与其余分部为纸面。

* 内核：`B25_Family.gcd_eval_eq_zero_of_common_root`、`gcd_is_const_of_no_common_root`、`no_common_root_iff_gcd_const`
* 均在 `tools/lean/MyProof/` 下，已登记进 `tools/lean/STATEMENT_MAP.md`；WSL 侧 `lake build MyProof` exit=0。
* 差异：矩阵实例化/行空间翻译与其余分部仍为纸面（详见 `## 状态与历史` 的等级行）。

## 精确验证

* `tools/verification/partial_operator.py`

## 状态与历史

*等级*：**[已证-纸面]** $+$ **[精确验证 3453/3453]**（`tools/verification/partial_operator.py`：gcd 有正次数 $\iff$ B.12 判据失败）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。




## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F3 |
| 导出等级 | **L4** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（字面） |


## 支撑目录

无（证据全部在本卷宗内）。
