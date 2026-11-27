# C1 —— $q_{\min}=\mathrm{cl}+1$ 被推翻（2026-11-02）

## 被推翻的陈述

**C1**（2026-11-02 下午提出，**已推翻**）：对功能可观测的 $(A,C,L_0)$，
$$q_{\min}=\operatorname{cl}(A,C,L_0)+1,$$
其中 $\operatorname{cl}=\min\{\dim V:\operatorname{row}L_0\subseteq V,\ VA\subseteq V+\operatorname{row}[C;CA]\}$。

**证据基础（当时）**：8 个实例（$n=5,p=r=1$；$L_0$ 取可观性矩阵行的**随机组合**），偏移全为 $+1$。

## 反例

$n=5$、$p=r=1$、seed 3001（实例生成见 [tools/verification/qmin_scan_pr.py](../../tools/verification/qmin_scan_pr.py) 的 `make_instance`）：

* $\operatorname{cl}=1$，即 $(5a)$ 下最小行数是 $1$；
* 该唯一候选（$1\times 5$ 的 $L$）**本身**满足 $(5b)$（Toeplitz 判据 $\nu_s=(s+1)m-s$ 精确通过）；

⟹ $q_{\min}=1=\operatorname{cl}$，**不是** $\operatorname{cl}+1$。

同类反例在 56 个可观测实例中有 **40 个**（$n=5,6$；$p,r\in\{1,2\}$；10 个 seed），
偏移分布：

$$\{\,+0:\ 40,\quad +1:\ 14\,\}\qquad(\text{另 }2\text{ 个未找到见证，见下}).$$

## 为什么当时误判

旧实例的 $L_0$ 是**可观性矩阵行的随机组合**（稠密），使得 $\operatorname{cl}=3$ 且闭包处 $(5b)$ 必失败；
新实例的 $L_0$ 直接取 $[C;CA;CA^2]$ 的**单行**（稀疏），闭包常常只有 1–2 维，且这些极小候选往往已经满足 $(5b)$。
**实例类不同，结论就不同**——这正是"采样只能筛假、不能定真"的又一例。

## 幸存的较弱陈述（未证，有数据）

$$\boxed{q_{\min}\in\{\operatorname{cl},\ \operatorname{cl}+1\}}$$

* 54/56 个实例落在 $\{\operatorname{cl},\operatorname{cl}+1\}$（40 个取 $\operatorname{cl}$、14 个取 $\operatorname{cl}+1$）；
* 其中 $\operatorname{cl}$ 情形是**精确结论**（$q=\operatorname{cl}$ 时唯一候选，直接判定）；$\operatorname{cl}+1$ 情形有显式见证；
* 2 个实例（$n=6,p=r=1$，seed 3005/3008）在 $\operatorname{cl}+1$ 处 12 条链式样本都没找到见证——**未定**。

**注意**：这不是"$\delta\le1$ 恒成立"的证明；只说明**已测的 54 个实例里最多差 1 行**。

## 意义

* 若 $\delta\le1$ 普遍成立，$q_{\min}$ 的判定就归结为"闭包处一次 $(5b)$ 检验 + 闭包 $+1$ 处的存在性"；
  后者仍非平凡（不是单点判定），所以**不直接推得多项式算法**；
* 真正的结构问题变成：**闭包处 $(5b)$ 何时成立**（40/56 成立——什么样的结构使它成立？）；
* 这也给了专家 §3"generic 可行性"路线一个具体对象。

## 证书

```bash
python -u tools/verification/qmin_scan_pr.py     # 56 个可观测实例；输出偏移分布
```

脚本对每个 $q$ 逐点 `assert`：行满秩、$\operatorname{row}L_0\subseteq\operatorname{row}L$、$(5a)$；
$(5b)$ 用 [Toeplitz 判据](../toeplitz_criterion/README.md)（与 Smith 路径交叉验证过 66/66）。

## 相关

- [workspace/q1_false/feasibility_geometry/attempts/03_functional_observability.md](../../workspace/q1_false/feasibility_geometry/attempts/03_functional_observability.md)（提出 C1 的那一轮，含更正）
- [proof/refuted/README.md](README.md)（R/C 系列索引）
