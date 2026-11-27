# 阶差能否由**纯算术量**预测？——73/74 命中，且"有阶差"方向无假阳性

> **2026-11-04 更正（专家 §10.1 指出后复核）**：本文把判据等价改写成
> "$\dim(\operatorname{row}L_0\cap W)\le p$" 是**错的**。正确形式是
> $$\operatorname{row}L_0\cap W\subseteq\operatorname{row}C\quad\bigl(\iff s_0=r_1+r\iff\dim(\operatorname{row}[C;L_0]\cap W)=p\bigr).$$
> 用 89 个实例复核（`tools/verification/gap_criterion_check.py`）：
> 旧形式 19 命中 / **55 假阳性**（几乎无信息）；新形式 **18 命中 / 0 假阳性 / 1 漏 / 55 真阴性**。
> 原因：$s_0=(p+r)+r_1-\dim(\operatorname{row}[C;L_0]\cap W)$，而 $\operatorname{row}C\subseteq
> \operatorname{row}[C;L_0]\cap W$，故 $s_0-r_1-r=p-\dim(\operatorname{row}[C;L_0]\cap W)$ 恒 $\le0$，
> 等号成立当且仅当该交恰为 $\operatorname{row}C$——这与"$\dim(\operatorname{row}L_0\cap W)\le p$"不是一回事。
> 下文保留原记录（含被推翻的等价式），结论以本框为准。

## 目标

把 [attempts/56](56_witness_scan.md) 的经验规律"$r=2$ 几乎没有阶差"变成可陈述的判据并检验。

## 设想与理由

由 [docs/02](../../../../docs/02_theorems_proven.md) B.9：$(5b)\Rightarrow h<q+r_1$，故 **Type I（$h\ge q+r_1$）⟹ 该阶不可行**。
由整族一致（$V'\cap S=0$ 时 $h=s_0+q-r$）得
$$\text{Type I}\iff s_0\ge r_1+r.$$
而 $s_0=\dim(\operatorname{row}[C;L_0]+W)$，且
$$s_0-(r_1+r)=p-\dim(\operatorname{row}L_0\cap W).$$

**预测**：$q_0$ 阶的全部可容许 $Z$ 都是 Type I $\iff s_0\ge r_1+r\iff\dim(\operatorname{row}L_0\cap W)\le p$
$\Longrightarrow$ $q_0$ 阶不可行 $\Longrightarrow$ 有阶差（$q_{\\min}>q_0$）。

## 做法

[gap_arithmetic.py](../../../../tools/verification/gap_arithmetic.py)：对 [qmin_upper.tsv](../data/qmin_upper.tsv)
的每个实例算 $s_0,r_1,\dim(\operatorname{row}L_0\cap W)$，与实测阶差对照。

## 进展

**混淆矩阵（74 个有见证的实例）**

| | 实测有阶差 | 实测无阶差 |
|---|---|---|
| **预测有阶差**（$s_0\ge r_1+r$）| 18 | **0** |
| **预测无阶差** | **1** | 55 |

* 命中 **73/74**；
* **"预测有阶差"方向没有假阳性**（18/18）——与 B.9+整族一致一致，这一方向是**有理论支撑**的；
* 唯一反例：$n=7,p=2,r=1$ seed 3001（$q_0=3$，$s_0=4=r_1$，$\dim(\operatorname{row}L_0\cap W)=1\le p=2$，
  预测无阶差，实测 $q_{\\min}=4$）。对该例补搜：80 个候选 $\\theta$ 仍无见证；且在 $q_0$ 阶随机采样**找不到**
  代数可容许的 $Z$（12 次采样 0 命中）——说明该阶的可容许集是薄集，见证可能在代数点，或
  整族一致的假设 $V'\\cap S=0$ 在此不成立。

## 最终结论

1. **"有阶差"的充分条件**：$s_0\ge r_1+r$（等价 $\dim(\operatorname{row}L_0\cap W)\le p$）⟹ $q_{\\min}>q_0$。
   这是 B.9 + 整族一致的推论（前提 $V'\cap S=0$），在 18 个实例上无假阳性 ✓；
2. **反向**（"无阶差"）在 55/56 上成立，但**无证明**——需要"$q_0$ 阶存在 Type II 且谱可行的 $Z$"，
   这不是我们的定理能给的；
3. 因此之前"阶差与 $r$ 强相关"的经验规律，**有一个更精确的算术形式**：
   $$\dim(\operatorname{row}L_0\cap W)\le p\ \Longrightarrow\ q_{\\min}>q_0.$$
   $r$ 只是间接相关（$r$ 越大，$\dim(\operatorname{row}L_0\cap W)$ 越容易 $>p$）。

## 放弃原因

不适用（判据与检验完成）。**未做**：反向的证明；唯一反例的定性（代数见证 / 假设失效）。

## 残留价值

* 一个**可陈述、有理论支撑的充分条件**（$\dim(\operatorname{row}L_0\cap W)\le p\Rightarrow$ 有阶差），18/18 无假阳性；
* 把经验规律"$r=2$ 无阶差"升级为更精确的算术形式；
* 明确指出反向缺什么证明。

## 相关文件

- [tools/verification/gap_arithmetic.py](../../../../tools/verification/gap_arithmetic.py)
- [workspace/q1_false/feasibility_geometry/data/qmin_upper.tsv](../data/qmin_upper.tsv)
- [workspace/q1_false/feasibility_geometry/attempts/56_witness_scan.md](56_witness_scan.md)
- [docs/02_theorems_proven.md](../../../../docs/02_theorems_proven.md)（B.9、整族一致）
