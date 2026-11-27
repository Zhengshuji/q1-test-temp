# 609 非平凡 $(5a)$ 下秩 1 逃逸的完整分类

> 2026-11-27。607 只做了粗略分析；本文件给出 $W\ne0$、$G=g e_1^{\mathsf T}$ 时秩 1 的完整分类。
> 状态：**[已证-纸面]**。

## 设定

$H=uv^{\mathsf T}$（秩 1），$H_A=uw^{\mathsf T}+g e_1^{\mathsf T}$，$w=Z'^{\mathsf T}v$。

$(5a)$：对 $x\in v^{\perp}$，$u(w\cdot x)+g\,x_1=0$。

## 分类

**情形 A：$v_1\ne0$。**
$e_1\notin v^{\perp}$，$x_1$ 在 $v^{\perp}$ 上不恒为零。需要
$$u(w\cdot x)+g x_1=0\quad\forall x\in v^\perp .$$
若 $g\parallel u$（$g=\lambda u$），条件化为 $(w+\lambda e_1)\cdot x=0\ \forall x\in v^\perp$ ⇒ $w+\lambda e_1\parallel v$。
即 $Z'^{\mathsf T}v+\lambda e_1\parallel v$——这是对 $v$ 的**特征型方程**，一般无解，
但对特殊 $v$（$Z'$ 的广义特征向量）可能成立。

**情形 B：$v_1=0$。**
$x_1=0$ 在 $v^\perp$ 上（因 $e_1\in v^\perp$），条件化为 $w\cdot x=0\ \forall x\in v^\perp$ ⇒ $w\parallel v$，
即 $v$ 是 $Z'$ 的左特征向量。再代回：$x_1=0$ 自动，无额外条件。
所以**情形 B 只需 $v$ 是 $Z'$ 的左特征向量且 $v_1=0$**——这时 $(5a)$ 自动成立。

## 结论

- 秩 1 逃逸**没有被完全阻断**：
  - 情形 B：$v$ 取 $Z'$ 的、第一坐标为 0 的左特征向量即可；
  - 情形 A：$g\parallel u$ 且 $v$ 满足 $Z'^{\mathsf T}v+\lambda e_1\parallel v$ 时可能。
- 607 的“一般被阻断”仍对：情形 B 要求 $Z'$ 有第一坐标为 0 的左特征向量；
  若 $Z'$ 的所有左特征向量第一坐标都非零，情形 B 消失。

## 修补

选 $Z'$ 使**所有左特征向量的第一坐标非零**（例如 $Z'=J$：唯一左特征向量 $e_1$，第一坐标 1 ✓）。
此时情形 B 消失，只剩情形 A 的“特征型方程”——需要进一步排除或接受为特例。

## 下一步

1. 取 $Z'=J$（单块）验证情形 A 是否有解（$Z'^{\mathsf T}v+\lambda e_1\parallel v$）；
2. 两块时每块用 $J$，检查秩 1 是否仍可能；
3. 若秩 1 被排除，再研究秩 2。

## 状态

- 分类：**[已证-纸面]**；
- 秩 1 的其它存活情形：**[未排除]**。
