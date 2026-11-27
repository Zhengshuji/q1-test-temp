# B.31 · 可行性的必要条件：$\delta$ 落在中间层

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.31` 条目（§0.1 归并表）。

## 命题

**B.31（可行性的必要条件：$\delta$ 必须落在中间层）** 设 $(p,r)$ 任意、$\mathcal L$ 可容许、$q+p<n$（即低于终阶）。则
$$\boxed{(5b)\ \text{成立}\ \Longrightarrow\ 1\le\delta(\mathcal V)<r_1-p ,}$$
其中 $\delta(\mathcal V)=\dim\bigl(\operatorname{row}(CA)/(\operatorname{row}(CA)\cap\mathcal V)\bigr)$、$\mathcal V=\mathcal Z^\perp$。

## 纸面证明

*证明*：设 $(5b)$ 成立且 $q+p<n$。
* 若 $\delta=r_1-p$，则 $\operatorname{row}(CA)\cap\mathcal V=0$，由 B.28(2) 得 $h=q+r_1$，于是 **B.22** 断言 $(5b)$ 失败——矛盾；
* 若 $\delta=0$，则 $\operatorname{row}(CA)\subseteq\mathcal V$，由 B.28(1) 的 $(5a)\iff\mathcal VA\subseteq\mathcal V+W_0$ 得 $\mathcal VA\subseteq\mathcal V$，
  归纳得 $\operatorname{row}(CA^k)\subseteq\mathcal V$（因 $\operatorname{row}C\subseteq\mathcal V$）；$(C,A)$ 可观测时
  $\operatorname{span}\{\operatorname{row}(CA^k)\}=\mathbb C^{1\times n}$，故 $\mathcal V=\mathbb C^{1\times n}$，$n\le\dim\mathcal V=q+p$——矛盾。
故 $1\le\delta<r_1-p$。$\square$

*推论（统一 B.27/B.29）*：$p=1$ 时 $r_1\le 2p=2$ ⟹ $r_1-p\le1$ ⟹ 中间层为空 ⟹ 低于终阶无可行候选 ⟹ $q_{\min}=n-1$ ✓
（这给出了 B.29 的**一行动机**：不是两情形的巧合，而是"中间层不存在"）。
*锐利性（中间层非空且可行）*：$n=6$、$p=r=2$、$q=3$（$q_0=2$）、$r_1=4$、$\delta=1$ 的显式证书（$(5a)$ ✓、$\operatorname{rank}[C;\mathcal L]=5$ ✓、
$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$ ✓、$(5b)$ ✓）——见 `proof/delta1_feasible/README.md` 与
`tools/verification/certificate_delta1.py`。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`B31.logic` / `B31.necessary` 的逻辑骨架（两极端层不可行 ⟹ 可行时 $1\le\delta<\rho$））（必要条件）+ **[精确验证]**（锐利性证书）。

## Lean

* `B31_32_33.lean` —— `B31.logic`（两个极端层都不可行 ⟹ 可行时 $1\le\delta<\rho$）、`B31.necessary`（同上，谓词形式）
* 差异：$\delta=0$ 与 $\delta=\rho$ 两层的"不可行"作为假设；它们的数学内容在 B.28（不变子空间排除）与 B.22（等号障碍）里

## 精确验证

* `tools/verification/two_stage.py`：3400 个可容许候选，几何筛选后 1905，**0 个被筛掉却可行**（等价于本命题无反例）
* `tools/verification/delta_fixed.py`：按修正后的 $\delta=h-(q+p)$ 分层重扫



## WSL 侧内核（同步前仅机器可复核）

下面这些内核已在 WSL 的 Lean 工程里编译通过（`lake build MyProof` exit=0），
但**尚未同步到 Windows 侧、也未登记进 `STATEMENT_MAP`**，因此 docs 的等级行暂未把它们计入：

* `B31_32_33.lean`（已在 Windows 侧登记）



## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 状态与历史

经专家复核（2026-11-05）：正确；$q+p<n$ 在 $\delta=0$ 支是本质的。
