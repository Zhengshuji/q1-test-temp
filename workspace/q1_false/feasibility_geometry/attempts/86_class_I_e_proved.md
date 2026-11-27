# Class I 的 $d=1$ 收束：第 3 条已证（次数论证）+ Lean 内核

## 目标

证明 B.18e 第 3 条：$z\in K$、$z_2\ne0$ $\Rightarrow$ $z\in\operatorname{im}\psi$。这是 Class I 的 $d=1$ 分类最后一块。

## 设想与理由

由 B.18d，$z\notin\operatorname{im}\psi$ $\iff$ $P_z$ 是**非零常数**。所以要证"有根"，只需数次数：
递归 $x_3=-z_2$、$x_{k+1}=\lambda x_k-z_k$；因 $z_2\ne0$，归纳可得 $x_k$ 的次数**恰为** $k-3$、首项系数 $-z_2\ne0$。
于是 $P_z=\lambda x_n+(\deg\le n-3)$ 的次数**恰为** $n-2\ge1$ ⟹ 代数闭 ⟹ 必有根 ⟹ $z\in\operatorname{im}\psi$。

## 做法

1. 纸面证明（归纳 + 代数基本定理）；
2. 精确验证：$w_2\ne0$ 时 $\deg P_w=n-2$（伴矩阵实例 $n=4..7$）；
3. **Lean 内核**：三条引理
   * `recX_natDegree_and_ne`：$c\ne0$ 时递归多项式非零且次数 $=k$；
   * `natDegree_X_mul_add_of_lt`：加低次项不改最高次数；
   * `exists_root_of_natDegree_eq_two`：$\mathbb C$ 上次数 $n-2$（$n\ge3$）必有根。

## 进展

| 项 | 结果 |
|---|---|
| 纸面证明 | 完成（归纳 + FTA）|
| 精确验证 | **412/412**：$w_2\ne0$ 时 $\deg P_w=n-2$ |
| Lean | `PsiImage.lean` **编译 exit=0，0 error 0 warning**（3 条声明）|
| 结论 | **B.18e 三条全部已证** ⟹ $d=1$ 阶整族不可行 ⟹ 配合 B.18b：$q_{\min}=n-1$（$d\le1$ 各阶 + 终阶）|

## 最终结论

1. **B.18e 已完成**（三条皆已证），Class I 的 $d=1$ 分类闭合；
2. $q_{\min}=n-1$ 现在对 $d\in\{0,1\}$ 的两阶成立（$d=0$ 必然可行、$d=1$ 必然不可行）；
   $d\ge2$ 仍待处理，因此"$q_{\min}=n-1$ 对**所有** $q\le n-2$"尚未完成；
3. Lean 覆盖了次数论证与 FTA 收尾（内核），差在 $P_w$ 的显式组装——已按 §4 写明差异。

## 放弃原因

不适用。

## 残留价值

* **B.18e 完整证明**（三条）；
* **Lean 内核** `PsiImage.lean`（3 条声明，exit=0），已登记 STATEMENT_MAP；
* 412/412 的精确验证。

## 相关文件

- `docs/02` B.18b–B.18e、B.18d
- `tools/lean/MyProof/PsiImage.lean`、`tools/lean/STATEMENT_MAP.md`、`proof/lean_coverage.md`
- `tools/verification/psi_image_canonical.py`
