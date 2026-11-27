# 路线 5：图 / 超图归约（CYCLIC-COVER）

## 目标
把 MIN-ROWS 在坐标层化为**图论**问题，再把已知 NP-hard 的图问题（Tree Augmentation / 最小 2-边连通生成子图）归约进来。

## 设想与理由
坐标层（$A$ 对角、$\mathcal V$ 坐标）时 $(5b)$ 有拟阵刻画，而图拟阵是最自然的拟阵族。若图拟阵可实现，TAP 的 NP-hardness 直接传递。

## 做法
- `archive/old_scripts/q1_true_routes/c171_cyclic_cover.py`：把 CYCLIC-COVER 写成"最小并环集"；
- 与 TAP 的关系：图拟阵特化 + $S_0$ = 生成树 ⟹ 最小 2-边连通生成子图（Nagamochi 2003；公认 NP-hard）；
- `c169_family_scan.py`：检查旧记录的公式在实现实例上的表现。

## 进展
1. CYCLIC-COVER 的图拟阵特化**确实**是 TAP ⟹ 坐标层含 NP-hard 子问题；
2. 但 MIN-ROWS 允许**非坐标** $\mathcal V$，坐标层只是**松弛** ⟹ 硬度不能直接传；
3. 要传需要 $(T)$：坐标解不劣于非坐标解 —— **被 §7.9 的 $n{=}6$ 反例推翻**；
4. 即使 $(T)$ 成立，还需圈空间**可实现**为 $\operatorname{row}[C;CA]$ —— **也不成立**（Krylov 补丁）。

## 最终结论
**死**（与 [01_matroid_tap.md](01_matroid_tap.md) 同源，此处保留最初的图论表述）。

## 残留价值
- CYCLIC-COVER 的精确陈述（最小并环集）；
- 拟阵视角本身（见 01）。

## 相关文件
- `archive/old_scripts/q1_true_routes/c171_cyclic_cover.py`、`c169_family_scan.py`
- [01_matroid_tap.md](01_matroid_tap.md)
