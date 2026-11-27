# tests/ — 复现脚本（q1_false 方向）

> 按主题分组的一次性脚本。**都不能当证据**，只用于复现某条路线的实验。

| 目录 | 主题 | 代表脚本 |
|---|---|---|
| [rho1/](rho1/) | $\rho=1$ 层 | `rho1_characterization.py`、`rho1_solver.py`、`hunt_r1_nontight.py`、`exact_r1_q3.py` |
| [rho2_middle/](rho2_middle/) | 中间层 / $\rho=2$ | `coupled_scan.py`、`find_middle_k2.py`、`k2_pinned.py`、`exact_k2_layer.py`、`verify_t20.py` |
| [sigma/](sigma/) | $\sigma$ 与引理 4.3 | `exact_sigma.py`、`lemma43_positive.py` |
| [zform/](zform/) | Z 形式 | `zform_check.py` |
| [scans/](scans/) | 参数扫描 | `param_scan.py`、`pencil_diag.py`、`q4_scan.py`、`rho_k_structure.py`、`symbolic_t.py`、`rank_drop_analysis.py` |
| [verify/](verify/) | 证书复核 | `verify_candidate.py`、`verify_refute_formula.py`、`combined_check.py`、`cp_check.py`、`descent_algorithm.py` |
| [results/](results/) | JSON 结果 | `candidate_r1_nontight.json`、`middle_k2_pinned.json`、`scan_certificate_middle_layer_194320.json` |

## 注记

- 这些脚本多数依赖 `tools/exact_linalg/audit_independent.py`；运行前确认 `sys.path` 指向正确（多数脚本内部已 `insert`）。
- 与 `proof/` 下的证书相比，这里的 JSON 是**中间结果**，正式证书在 [proof/refuted/certificates/](../../../proof/refuted/certificates)。