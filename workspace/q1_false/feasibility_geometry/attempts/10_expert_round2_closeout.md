# 上一轮专家建议的收尾：§10.5（几何与谱退化簇）与 Q1（零空间判据）

## 目标

清点上一轮专家建议（§10、§12）的完成情况，并补齐两项：

* **§10.5**：公开两阶差例子中，"谱退化簇是否包含 $q_0$ 与 $q_0+1$ 的**整个**代数可行族"？
  若成立，指出**负责的代数关系**。
* **Q1**：把零空间判据 (12) 与 Toeplitz 判据交叉核对，作为独立验证。

## 设想与理由

* §10.5 可以直接检验：若在 $q_0+1$ 阶所有代数可行增广都有 $h\ge q+r_1$，则 B.9 就解释了该阶的**全部**失败，
  而不必逐图卡算谱——"负责的代数关系"就是"可行族被限制在超曲面 $h=q+r_1$ 上"。
* Q1 的判据 (12) 与 Toeplitz 判据是两条独立路线；交叉核对能同时验证实现与理论。

## 做法

* 用 Z-参数化（[z_generator.py](../../../../tools/verification/z_generator.py)）在 $q=4$、$q=5$ 各抽 40 个代数可行增广，
  记录 $h$ 与 $(5b)$；
* 用 [nullspace_vs_toeplitz.py](../../../../tools/verification/nullspace_vs_toeplitz.py) 比较
  `spectral_gcd_Z`（$P(\lambda)=[(\lambda I-A)V\mid Z]$ 的极大子式 gcd）与 Toeplitz 判据的结论。

## 进展

**清点**：

| 专家建议 | 状态 |
|---|---|
| §10.1 用 $\mathrm{cl}\le q_{\min}\le n_0-p$ 取代经验猜想 | ✅（C3 + docs/05）|
| §10.2 加强的 B.9 区间 | ✅（proof/left_index_count，698 例）|
| §10.3 以 $q_0$ 为最小维数的权威 | ✅（attempts/07）|
| §10.4 复现公开两阶差例子 | ✅（proof/fernando_2gap）|
| §10.5 谱退化簇 + 代数关系 | **本轮补齐 $q_0+1$ 阶** |
| §12.3 B.9 强化成结构判据 | 部分（attempts/09）|
| Q1 零空间判据 | **本轮交叉核对 30/30** |

**§10.5 的结果**（$r_1=4$、$q_0=3$）：

| 阶 $q$ | 抽样 | $h$ 的取值 | $q+r_1$ | $(5b)$ 成立 |
|---|---|---|---|---|
| 4 | 40 个代数可行 | $\{8\}$ | $8$ | **0** |
| 5 | 40 个代数可行 | $\{8\}$ | $9$ | **40** |

**Q1**：30 个样本全部一致（4 个因 $d=0$ 跳过）。

## 最终结论

* $q_0+1=4$ 阶的失败**完全由 B.9 解释**：可行族被限制在 $h=q+r_1=8$ 上；
* $q=5$ 时族离开该超曲面（$h=8<9$），$(5b)$ 成立；
* 这与**猜想 T** 一致；
* $q_0=3$ 阶仍不能直接检验（$(A)$ 是薄集：0/240、0/500），需要代数消元。

## 放弃原因

不适用（$q_0$ 阶的完整检验不在本轮范围：需要符号消元，当前环境无 CAS）。

## 残留价值

* 把 §10.5 的"负责关系"具体化为 **$h=q+r_1$**——一个可检验的整数关系；
* 零空间判据与 Toeplitz 的双路线交叉核对（30/30），可作后续的独立复核手段；
* 明确了唯一剩余缺口：$q_0$ 阶的代数消元。

## 相关文件

- [proof/fernando_2gap/](../../../../proof/fernando_2gap/README.md)
- [tools/verification/nullspace_vs_toeplitz.py](../../../../tools/verification/nullspace_vs_toeplitz.py)
- [tools/verification/spectral_gcd.py](../../../../tools/verification/spectral_gcd.py)
- [workspace/q1_false/feasibility_geometry/attempts/08_failure_types.md](08_failure_types.md)（猜想 T）
- [workspace/q1_false/feasibility_geometry/attempts/09_T_proof_attempt.md](09_T_proof_attempt.md)
