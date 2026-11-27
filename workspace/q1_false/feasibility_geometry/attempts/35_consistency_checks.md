# 七条一致性检查落地（专家 2026-11-03 §8.6），并明确系数域与谱域

## 目标

按专家 §8.6，把"每个候选必须通过的七条检查"做成**可复用模块**并接入验证流程；
同时落实 §8.2（候选的系数域）与 §8.4（谱域含 $\\lambda=0$）的表述要求。

## 设想与理由

专家指出：**增加随机样本量**不如**七条精确一致性检查**有价值，因为历史错误的共同模式是
"约束写漏、结论看起来对"。七条是：

1. $\\operatorname{rank}[C;\\mathcal L]=p+q$；
2. $\\dim\\ker[C;\\mathcal L]=n-p-q$；
3. 零空间基 $Z$ 满足 $CZ=0$、$\\mathcal LZ=0$；
4. $(5a)$ 与零空间秩判据（$\\operatorname{row}(\\mathcal LA)\\subseteq\\operatorname{row}\\mathcal L+W$）一致；
5. 铅笔的**目标秩** $h$，且一般 $\\lambda$ 处的秩恰为 $h$（法秩 $=h$）；
6. 极大子式 gcd 与 Toeplitz 零度判据结论一致；
7. 所有条目是有理数（`Fraction`）——从而候选是**实**矩阵（§8.2）。

## 做法

[consistency_checks.py](../../../../tools/verification/consistency_checks.py)：
`check_candidate(A, C, L0, L, tag)` 逐条 `assert`，返回 `{cond, h, five_b, d, r1}`；
驱动脚本对 C4 的两个候选、专家给的 $\\mathcal L_*$、公开例子在 $q_0$ 的显式解、三个随机实例运行。

## 进展

六个候选**全部通过**：

| 候选 | $\\operatorname{rank}[C;\\mathcal L]$ | $\\dim\\ker$ | $CZ=\\mathcal LZ=0$ | $(5a)$ | $h=$ 法秩 | gcd/Toeplitz | 域 |
|---|---|---|---|---|---|---|---|
| C4 #0、#1 | 5 | 1 | ✓ | 成立 | $6$ ✓ | 一致（失败）| 有理 |
| $\\mathcal L_*$（专家）| 5 | 2 | ✓ | 成立 | $5$ ✓ | 一致（成立）| 有理 |
| 公开例子 $q_0$ 显式解 | 5 | 3 | ✓ | 成立 | $7$ ✓ | 一致（失败）| 有理 |
| rand 6/2/1、7/2/2 | 3、4 | 3、3 | ✓ | 成立 | 相符 | 一致 | 有理 |

## 最终结论

1. 七条检查已模块化，并在 6 个基准候选上全通过；
2. **系数域**（§8.2）：本项目的所有候选都由有理数构成 ⟹ 是**实**矩阵；检查 7 用 `isinstance(v, Fraction)`
   把这个要求变成断言；
3. **谱域**（§8.4）：$(5b)$ 要求对所有 $\\lambda\\in\\mathbb C$（含 $0$）成立；我们用的 gcd 判据是
   **恒等式检验**（与具体 $\\lambda$ 无关），因此自动覆盖 $\\lambda=0$；只有在"抽样 $\\lambda$"的快速预筛里
   才需要显式包含 $\\lambda=0$，且该预筛不得用于结论（见 [attempts/34](34_q1_closed.md) 的误报教训）。

## 放弃原因

不适用（落地完成）。**未做**：把该模块接入**所有**既有脚本（目前只在独立驱动里运行；
下一步应作为每个 `verify_*.py` 的强制前置）。

## 残留价值

* 一个可直接复用的七条检查模块，把"证书脚本必须先断言基本不变量"（CLAUDE §7 规则 21）具体化；
* 把"系数域 = 有理（⟹ 实）"和"谱域 = 全 $\\mathbb C$（含 0）"两条表述要求变成代码断言；
* 六个基准候选（含两个反例与两个可行见证）成为回归集。

## 相关文件

- [tools/verification/consistency_checks.py](../../../../tools/verification/consistency_checks.py)
- [workspace/for_expert/06_state_corrections_and_assessment-answer.md](../../../for_expert/archive/06_state_corrections_and_assessment-answer.md)（§8.2、§8.4、§8.6）
- [workspace/q1_false/feasibility_geometry/attempts/34_q1_closed.md](34_q1_closed.md)
- [CLAUDE.md](../../../../CLAUDE.md) §7 规则 21
