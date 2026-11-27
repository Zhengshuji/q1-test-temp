# 证书索引

> 每个 JSON 都是一个**精确实例**：矩阵数字 + 期望值。用 `tools/verification/c164_trusted_baseline.py`（有理数精确判据）或对应脚本复核。

## 反例（用于推翻公式）

| 文件 | 推翻什么 | 关键数字 |
|---|---|---|
| `counterexample_refute_dimV1.json` | $q_{\min}=\dim V+1$ | $n{=}5$，$q{=}1<\dim V+1=2$ |
| `counterexample_candidate.json` | $d+\max(c_0,1)$ | 见文件 |
| `counterexample_d4.json` | $d+\max(c_0,1)$ | $n{=}6,p{=}1,d{=}4$，$q_{\min}=3$ |
| `counterexample_p2.json` | $d+\max(c_0,1)$ | 见文件 |
| `counterexample_max_r_eps_rho_star_plus1_n5_2026-10-26.json` | $\max(r+\varepsilon,\rho^*+1)$ | $S=\mathcal J$ 族，$q_{\min}=n$ |
| `counterexample_max_r_eps_rho_star_plus1_n6_2026-10-26.json` | 同上 | $n{=}6$ |
| `counterexample_refute_layer_formula_2026-10-25.json` | 层公式 | 见文件 |
| `refute_formula_2026-10-25.json` | 同上（第二份） | 见文件 |
| `counterexample_f3_n4_2026-10-27.json` | $F_3$ | $n{=}4,d{=}2,r{=}2,c_0{=}1,\varepsilon{=}1$，$q_{\min}=4$ vs $F_3=3$ |

## 正面证书（用于推翻"夹逼"）

| 文件 | 说明 |
|---|---|
| `certificate_middle_layer.json` | 中间层存在：$q_{\min}=2$，$d{=}2$，$c_0{=}1$，$\varepsilon{=}1$ |
| `certificate_rho0_lt_dimV.json` | $\rho^*=0<\dim V$ 的解 |
| `certificate_rhostar_lt_dimV.json` | $\rho^*<\dim V$ |
| `certificate_wide_bracket.json` | 夹逼可以很宽 |

## 复核

```bash
python tools/verification/c164_trusted_baseline.py          # 基线：cond5a / cond5b（有理数精确）
python tools/p_algorithm/c196_f3_counterexample.py           # F_3 反例（会重写 JSON 并打印判定）
```