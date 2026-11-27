# 带证书的逐阶判定 + 谱域参数化（专家 §8.1、§8.4、§8.6 的落地）

## 目标

落实专家反复强调的一条：**网格/抽样不能证明"无解"，只有证书才能**。

## 设想与理由

他 §8.1 的原话是"a finite rational-grid sample is a complete scan of a Grassmannian"之否定——
理由：图卡覆盖 Grassmannian，但**有理网格不覆盖图卡**；容许子空间的坐标可能落在代数扩张上，
或构成正维族。因此：

* 网格可以**发现见证**、**测试猜想**、**做回归**；
* 但**不能**用来断言"某阶无解"或"恰好 18 个可容许零空间"。

于是把"结论"改成**带类型的证书**，没有证书就输出 `UNKNOWN`。

## 做法

### (1) 带证书的判定 [decide_with_certificate.py](../../../../tools/verification/decide_with_certificate.py)

对每个阶给出四种结论之一：

| 结论 | 证书 |
|---|---|
| `FEASIBLE` | 显式 $\\mathcal L$，且通过**七条一致性检查**（含 $(5b)$ 的 gcd）|
| `INFEASIBLE_INTEGER` | 整数障碍（$h\\ge q+r_1$；$V'\\cap S=0$ 时 $h=s_0+q-r$ 恒定）或单点且 $h\\ge q+r_1$ |
| `INFEASIBLE_SPECTRAL` | 单点且 $h<q+r_1$（该点谱失败）|
| `INFEASIBLE_OCCLUSION` | $h=n$ 且 $\\dim\\overline{\\Phi(\\mathbb P(V))}\\ge q-r$（射影维数定理）|
| `UNKNOWN` | 上述都没有：**抽样未见见证不构成否证** |

### (2) 谱域做成显式参数 [spectral_domain.py](../../../../tools/verification/spectral_domain.py)

`DOMAIN_C`（全 $\\mathbb C$，含 $0$）/ `DOMAIN_SPEC_A` / `DOMAIN_SPEC_LAMBDA`；
`sample_lambdas` 对 `DOMAIN_C` **显式加入 $0$**；`decide` 返回**精确**结论 + 诊断字段
`samples_would_miss`（该域上的抽样是否会漏掉真实掉秩点）。

### (3) 七条检查接线

`consistency_checks.check_candidate` 已接入 [regression_Lstar.py](../../../../tools/verification/regression_Lstar.py)：
两个基准候选（$\\mathcal L_*$ 与 $L_0$）在回归测试里同时跑七条检查。

## 进展

**带证书判定**（实例 $n=7,p=r=2$、seed 4004，阶区间 $[2,3]$）：

```
q=2: INFEASIBLE_SPECTRAL —— 单点（q=r）：h=5，q+r1=6，(5b)=False
q=3: FEASIBLE —— 见证（80 次抽样内找到）
     行：[-1,0,0,0,-1,0,0] / [1,0,0,0,0,0,1] / [0,0,0,1,0,1,0]
```

**谱域诊断**（C4 的两个候选）：

| 候选 | 域 | 精确 $(5b)$ | 该域抽样会漏掉掉秩 |
|---|---|---|---|
| C4#0 | $\\mathbb C$ | 失败 | **是**（掉秩点在非有理处）|
| C4#0 | $\\operatorname{spec}(A)$ | 失败 | **是** |
| C4#1 | $\\mathbb C$ | 失败 | 否（掉秩在 $\\lambda=3$）|
| C4#1 | $\\operatorname{spec}(A)$ | 失败 | **是** |

⟹ "在特征值上抽样"同样会漏——这解释了此前那次误报的根源，也说明**必须用 gcd 恒等式**。

## 最终结论

1. **§8.1 的纪律层已落地**：任何"无解"结论现在必须带证书（整数/遮蔽/单点），否则只能是 `UNKNOWN`；
2. **§8.4 已落地**：谱域是显式参数，且给出"该域抽样是否会漏"的可计算诊断；
3. **§8.6 已接线**：回归测试里两个基准候选都跑七条检查；
4. **仍缺（诚实）**：**真正精确的图卡分析**（对 $\\dim\\operatorname{Gr}\\ge2$ 用消元替代网格）没有实现——
   需要 Gröbner/三角分解，本仓库无 CAS。现阶段的做法是"没有证书就标 `UNKNOWN`"，
   并**撤回**此前由网格得出的"0 命中 ⟹ 无解"式表述（见 [09_work_inventory](../../../../workspace/support/project_management/09_work_inventory.md) F 组）。

## 放弃原因

不适用（纪律层完成）。**未做**：精确消元（$\\dim\\operatorname{Gr}\\ge2$）。

## 残留价值

* 一个**不会说谎**的逐阶判定入口：结论带类型、见证带一致性检查；
* 谱域参数化 + "抽样会漏"诊断，直接对应此前两次误报的成因；
* 明确了"哪些历史结论只是网格证据"（`docs/09` F 组）。

## 相关文件

- [tools/verification/decide_with_certificate.py](../../../../tools/verification/decide_with_certificate.py)
- [tools/verification/spectral_domain.py](../../../../tools/verification/spectral_domain.py)
- [tools/verification/consistency_checks.py](../../../../tools/verification/consistency_checks.py)
- [tools/verification/regression_Lstar.py](../../../../tools/verification/regression_Lstar.py)
- [workspace/for_expert/06_state_corrections_and_assessment-answer.md](../../../for_expert/archive/06_state_corrections_and_assessment-answer.md)（§8.1、§8.4、§8.6）
