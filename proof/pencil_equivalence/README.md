# 命题：$(5b)$ 的商铅笔形式

> **对应 docs 条目**：B.1（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

$$(5b)\iff \operatorname{rank}Q_{\mathcal V}(\lambda)=\rho\quad\forall\lambda,\qquad
Q_{\mathcal V}(\lambda)=\lambda\,\pi(\mathcal L)-\pi(\mathcal LA)\in\mathbb C^{q\times d},\ \ \rho=\dim\pi(\mathcal V).$$

## 证明

$[\lambda\mathcal L-\mathcal LA;CA;C]$ 的行空间 = $\operatorname{row}(\lambda\mathcal L-\mathcal LA)+\mathcal J$；
对 $\mathcal J$ 取商，秩条件即 $\operatorname{rank}(\lambda\pi(\mathcal L)-\pi(\mathcal LA))=\dim\pi(\mathcal V)$。$\square$

## 等级与验证

| 项 | 值 |
|---|---|
| 等级 | [已证] |
| 验证 | `python proof/pencil_equivalence/verify.py` → **15/15** |
| 覆盖 | 8 个随机可行解（可观测堆叠）+ 7 个证书解；$\lambda\in\{0,\pm1,2\}$ |
| 等价判定 | 对每个解比较 `cond5b`（原始子式 gcd 判据）与"所有 $\lambda$ 处秩 $=\rho$"，两者一致 |

## 用途

- 顶层（$\rho=d$）时退化为可观测性判据（[proof/top_layer_observability/](../top_layer_observability/README.md)）；
- $q1$ 的"层判定"全部以它为出发点（[docs/05](../../docs/05_open_questions.md) Q1）。

## 附：E3（交维数形式）的复核

docs/00 §0.3 的 **E3**（$F_\lambda=\{v:\ v(\lambda I-A)\in\mathcal J\}$，
$(5b)\iff\dim(\mathcal V\cap F_\lambda)=\dim(\mathcal V\cap\mathcal J)\ \forall\lambda$）的纸面证明在
`archive/expert_correspondence/Q1_FOR_EXPERT_7.md` 定理 1，**本项目从未复核** ✗。

本目录新增 [verify_E3.py](verify_E3.py)：在有限实例上**逐 λ** 比较两边：

```bash
python proof/pencil_equivalence/verify_E3.py --trials 200     # 1128/1128 一致 ✓
```

**等级**：E3 因此是 **[精确验证 1128/1128]**（不是 [已证]——证明仍未复核）。验证 ≠ 证明（CLAUDE §4）。
