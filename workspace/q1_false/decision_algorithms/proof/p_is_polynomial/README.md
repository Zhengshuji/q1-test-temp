# 命题：$P(A,B,S)$ 是多项式可算的

> **对应 docs 条目**：D.1（见 [docs/02](../../../../../docs/02_theorems_proven.md) §0.1 归并表）

$$P(A,B,S)=\min\{\dim W:\ W\supseteq S,\ AW\subseteq W+B\}$$

## 状态

| 部分 | 等级 |
|---|---|
| 下界 $P\ge\dim S+\dim\frac{AS+S+B}{S+B}$ | **[已证]** |
| 一步递归 $\mathcal P(Y,C,\Phi,T)=\dim T+\mathcal P(Y',C',\Phi')$（两方向）| **[已证]** + 部分 **[Lean]** |
| $O(n^4)$ 算法（递归 + 终止性）| **[已证]**；[精确验证 29/29] 对穷举 |
| 见证构造（每个 $P$ 配一个可行 $W$）| [精确验证 36/36]（$n=4,5,6$）|
| $\sigma$ 存在性（$({\le})$ 的关键一步）| **[已证]**（纸面）；Lean：通用提升引理 ✓ + **区间包含的一般形式 ✓（2026-10-28 新增，`PRecursionSigmaRange.lean`）**；仅"实例化到具体数据"未形式化 |

**结论**：$P\in\mathbf P$（$O(n^4)$）。这是"算术侧"的全部内容（[docs/04](../../../../../docs/04_structure.md) §4.2）。

## 文件

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | 命题、下界、递归定理（含 $({\ge})/({\le})$ 完整证明）|
| [algorithm.md](algorithm.md) | 算法、终止性、复杂度 |
| [verification.md](verification.md) | Lean 清单、数值对拍、诚实清单、复现命令 |

**代码**（在 `tools/`）：
- `tools/p_algorithm/c195_P_q.py`（$\mathbb Q$ 精确值）、`c197_P_witness.py`（值 + 见证）、`c196_f3_counterexample.py`（$F_3$）、`c198_graphic_matroid.py`（图拟阵实验）
- `tools/lean/`（Lean 备份，WSL 工程 `~/WorkSpace/lean4/MyProof`）

## 复现

```bash
python tools/p_algorithm/c195_P_q.py
python tools/p_algorithm/c197_P_witness.py --n 5
wsl -e bash -lc 'cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH" && lake build MyProof.PRecursion'
```

## 风险

- 文献：**Emre–Hautus (1980) 已读**（[REFERENCES](../../../../../literature/REFERENCES.md) #20）：它只给 **supremal**（最大）$(A,B)$-不变子空间的多项式刻画与构造，**不涉及最小维数** ⟹ 本命题（最小维数 $P$）**不被抢占** ✓。
  但它的 Thm 3.1 参数化了所有 $(A,B)$-不变子空间，是 $P$ 的**另一条**可能算法路线（未做）。
- Lean：$\sigma$ 存在性的**一般形式已形式化**（区间包含，2026-10-28）；只有"实例化到具体递归数据"这一步还在纸面。