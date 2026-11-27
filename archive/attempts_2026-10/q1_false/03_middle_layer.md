# 路线 3：中间层

## 目标
搞清楚 $0<\rho<\dim V$ 的层（"中间层"）是否存在、能否放大、对 $q_{\min}$ 的影响。

## 设想与理由
顶层（$\rho=d$）和底层（$\rho=0$）都有判据；如果中间层不存在或可忽略，$q_{\min}$ 就只剩两端 —— 那就多项式了。

## 做法
- `q1_false/tests/rho2_middle/`（`coupled_scan.py`、`find_middle_k2.py`、`k2_pinned.py`、`exact_k2_layer.py`、`verify_t20.py`）
- 证书 `proof/refuted/certificates/certificate_middle_layer.json`
- `archive/process_logs/LAYER_AUDIT_2026-10-24.md`

## 进展
1. **存在**：给出精确证书（$n{=}6$，$d{=}2$，$q_{\min}=2$，$\rho^*=1<\dim V$）。
2. **不可非平凡放大**：块扩展（D38/D40）会破坏它；只有"不可见块 padding"能放大，而那是平凡放大（不增难度）。
3. **两个解互不包含**（D45）：中间层的两个解没有包含关系 ⟹ 不能用"取并"合并。

## 最终结论
**存在、稀有、不可放大**。所以"忽略中间层"的路线**不成立**（它真的会影响 $q_{\min}$），但它的稀有性解释了为什么多数实例只有顶两层。

## 残留价值
- 中间层证书（可用于测试任何未来算法）。
- "不可放大"的证明思路（块扩展的分析）。

## 相关文件
- [03_D10-D16_layers.md](archive_attack_log/03_D10-D16_layers.md)、[04_D17-D26_structure.md](archive_attack_log/04_D17-D26_structure.md)
- 证书：`proof/refuted/certificates/certificate_middle_layer.json`