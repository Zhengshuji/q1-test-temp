# $P$ 的验证

## 5. 验证

### 5.1 Lean 4（机器验证，`lake build MyProof.PRecursion` → 9054 jobs, 0 error）

文件：WSL `~/WorkSpace/lean4/MyProof/MyProof/PRecursion.lean`；Windows 备份 `tools/lean/PRecursion.lean`（逐字节一致）。

| 定理 | 内容 |
|---|---|
| `comapSubtypeEquiv` | `comap U.subtype M ≃ U ⊓ M` |
| `finrank_map_mkQ_add` | $\dim(\pi U)+\dim M=\dim(U\sqcup M)$ |
| `dim_lower_quotient` | **$({\ge})$ 一半**：$\dim T+\dim(\pi U)\le\dim U$ |
| `bot_admissible` | 递归基 |
| `induced` | \(\Phi'\) 良定义 |
| `admissible_image` | 可行性下降到商实例 |
| `exists_section` | 商的线性截面存在 |
| `section_image` | $s''U'$ 映满 $U'$ 且与 $M$ 交零 |
| **`lift_admissible`**（`PRecursionLift.lean`）| **$({\le})$ 的构造步**：给定 $\sigma$，$U=T\sqcup(s+\sigma)''U'$ 可行且 $\dim U=\dim T+\dim U'$ |
| **`exists_lift_of_range_le`**（`PRecursionSigma.lean`）| **$\sigma$ 存在性的可复用核心**：$\operatorname{range}g\le\operatorname{range}\psi\Rightarrow$ $g$ 沿 $\psi$ 提升 |

**已做（2026-10-28）**：区间包含的一般形式 $\operatorname{range}\varphi\le\operatorname{range}\psi$ 已在 `PRecursionSigmaRange.lean` 中机器验证（3 条，`lean` 退出码 0）。
~~未做~~：解包 level-1 可行性），以及递归迭代本身。

### 5.2 数值

| 对拍 | 结果 |
|---|---|
| $\mathbb F_5$ 穷举（$n=4,5,6$） | $29/29$ |
| $\mathbb Q$ 精确实现 `c195_P_q.py` vs $\mathbb F_p$ 穷举（$p=5,7,11$） | 无一个 $P_{\mathbb F_p}>P_{\mathbb Q}$（单向不等式全部成立）|
| $\mathbb Q$ 网格穷举 vs 算法 | $11/12$；1 例解释为可行集无 $\mathbb Q$-点（算法给的是 $\mathbb C$ 上的值，正是 $q1$ 所需）|
| **见证构造** `c197_P_witness.py`（$n=4,5,6$）| **$36/36$**：每个 $P$ 值都附一个 $W$，精确满足 $\dim W=P$、$AW\subseteq W+B$、$W\supseteq S$ |

---

## 7. 诚实清单

| 断言 | 等级 |
|---|---|
| 定理 1（下界）| 已证 |
| 定理 2（递归等式）| 已证（两方向）|
| 算法 $O(n^4)$ | 已证（由定理 2 + 终止性）|
| $\rho_{ci}=P(T,B,U_0)$ 可算 | 已证（由定理 2）|
| Lean 9 条（`PRecursion` + `PRecursionLift`）| 机器验证 |
| `exists_lift_of_range_le`（`PRecursionSigma`）| 机器验证（$\sigma$ 存在性的通用核心）|
| $({\le})$ 的构造（给定 $\sigma$）| 机器验证（`lift_admissible`）|
| $({\le})$ 的 $\sigma$ 存在性：**区间包含（一般形式）** | **机器验证**（`PRecursionSigmaRange.lean`，2026-10-28）|
| $({\le})$ 的 $\sigma$ 存在性：**实例化到具体数据（线性版）** | **机器验证**（`PRecursionLin.lean` 的 `exists_sigma`，2026-10-29）|
| 数值对拍 | 精确验证（非证明）|
| $q1$ 的复杂度 | **开放** |

---

## 8. 复现

```bash
# Lean（WSL）
wsl -e bash -lc 'cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH" && lake build MyProof.PRecursion'

# 有理精确算法 + 对拍
python tools/p_algorithm/c195_P_q.py
python tools/p_algorithm/c195_P_q.py --n 5
```
| `inducedQuotient` / `inducedQuotient_mkQ` / `inducedQuotient_map_T_le`（`PRecursionInduced.lean`）| **机器验证**：level-1 映射 $\Phi'$ 的良定义 + 定义性质 + $T'\subseteq C'$ |
| `exists_correction_pointwise`（`PRecursionSigmaPoint.lean`）| **机器验证**：$\sigma$ 的逐点校正（线性化未做）|
| `step_le`（`PRecursionStep.lean`）| **机器验证**：一步递归 $({\le})$ 半（无 $\sigma$）|

> **注（2026-10-29）**：$({\ge})$ 半（level-0 可行 => level-1 可行 + 维数不等式）**早已机器验证**：
> `admissible_image`（结构性）+ `dim_lower_quotient`（维数）。所以 Lean 里"一步递归"的两半都齐了；
> 剩下的是把两半**组装成关于 $\mathcal P$ 的等式**（需要先形式化 $\mathcal P$ 的定义与最小性）。
