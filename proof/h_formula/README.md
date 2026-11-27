# $h=\\dim(\\mathcal Z^{\\perp}+W)$：正规秩的几何公式与它给出的必要条件

> **对应 docs 条目**：B.9（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

**状态**：**[已证-纸面]**（本文件）+ **[精确验证 240/240]**（[verify.py](verify.py)）。

## 记号

$\\mathcal L$ 行满秩，$\\operatorname{row}L_0\\subseteq\\operatorname{row}\\mathcal L$，
$\\mathcal Z=\\ker[C;\\mathcal L]$（$\\dim d=n-p-q$），故 $\\operatorname{row}[C;\\mathcal L]=\\mathcal Z^{\\perp}$
（$\\dim p+q$）。令
$$W=\\operatorname{row}[C;CA]\\quad(\\dim r_1),\\qquad
H=[\\mathcal L;CA;C],\\qquad h=\\operatorname{rank}H .$$

## 定理

$$\\boxed{\\ h=\\dim\\bigl(\\mathcal Z^{\\perp}+W\\bigr)\\ }$$

*证明*：$h=\\operatorname{rank}[\\mathcal L;CA;C]=\\dim(\\operatorname{row}\\mathcal L+W)$。
一方面 $\\operatorname{row}\\mathcal L\\subseteq\\mathcal Z^{\\perp}$ 给出 $\\operatorname{row}\\mathcal L+W\\subseteq\\mathcal Z^{\\perp}+W$；
另一方面 $\\mathcal Z^{\\perp}=\\operatorname{row}[C;\\mathcal L]=\\operatorname{row}C+\\operatorname{row}\\mathcal L\\subseteq W+\\operatorname{row}\\mathcal L$
（因为 $\\operatorname{row}C\\subseteq W$），故 $\\mathcal Z^{\\perp}+W\\subseteq\\operatorname{row}\\mathcal L+W$。
两边相等。$\\square$

**重要推论**：$h$ **只依赖** $\\mathcal Z$（与 $\\mathcal L$ 在 $\\mathcal Z^{\\perp}$ 里的具体补无关）——这与实验观察一致
（同一 $\\mathcal Z$ 换 200 种补，$h$ 恒为 8）。

## 推论 1（B.9 的几何形式）

记 $\\delta:=\\dim(\\mathcal Z^{\\perp}\\cap W)-p\\ \\ge0$（$\\operatorname{row}C\\subseteq\\mathcal Z^{\\perp}\\cap W$）。
由维数公式
$$h=\\dim(\\mathcal Z^{\\perp}+W)=r_1+q-\\delta,$$
于是
$$(5b)\\ \\Longrightarrow\\ \\delta\\ge1\\iff \\mathcal Z^{\\perp}\\cap W\\supsetneq\\operatorname{row}C
\\iff \\mathcal Z^{\\perp}+W\\subsetneq\\mathbb C^{n}\\ (\\text{当 }q+r_1\\le n).$$

## 推论 2（"见证"形式）

$\\delta\\ge1$ 等价于存在 $w\\in W\\setminus\\operatorname{row}C$ 使 $w\\perp\\mathcal Z$（即 $w^{\\mathsf T}z=0,\\ \\forall z\\in\\mathcal Z$）。于是

$$\\boxed{\\ (5b)\\ \\Longrightarrow\\ \\exists\\,w\\in W\\setminus\\operatorname{row}C,\\quad \\mathcal Z\\subseteq\\ker(w^{\\mathsf T})\\ }$$

即"可行 $\\mathcal Z$ 必须被 $W$ 里某个**额外**元素整块消灭"。

## 推论 3（自动满足的情形）

若 $q+r_1>n$，则 $h=\\dim(\\mathcal Z^{\\perp}+W)\\le n<q+r_1$，B.9 自动不构成障碍。
所以**整数障碍只可能在 $q\\le n-r_1$ 时触发**，且需要 $\\mathcal Z$ 处于"非一般位置"。

## 验证（[verify.py](verify.py)）

在公开例子（$n=8,p=r=2,r_1=4$）的 $q=3,4,5,6$ 上抽 240 个 $\\mathcal Z$（其中 160 个 $(5a)$ 可行）：
$h=\\dim(\\mathcal Z^{\\perp}+W)$ **240/240** 成立。

## 与既有结果的关系

* B.9（$h<q+r_1$ 必要）是本定理的直接推论——但本定理给出 $h$ 的**精确表达式**，
  并把它化为 $\\mathcal Z$ 的几何；
* 公开例子在 $q=4$ 处 $q+r_1=8=n$，故 $\\dim(\\mathcal Z^{\\perp}+W)\\le8$，而 $\\ge8$（因为 $\\ge q+r_1-\\)…），
  实际 $=8$ ⟹ $\\delta=0$ ⟹ B.9 必然触发（**这就是 §B 的结构解释**）；
* C4 的反例说明 Type III 存在：它满足 $\\delta\\ge1$ 但仍有有限初等因子。

## 补充（2026-11-03，专家 §Q2/§Q4）：限制映射形式与 Schubert 余维

令 $K=\ker C$、$U=W/\operatorname{row}C\subset K^*$（$\dim U=a=r_1-p$）、
$T=\mathcal Z^{\perp}\cap K^*$（$\dim T=q$）。限制映射
$$\rho_{\mathcal Z}:U\to\mathcal Z^*,\qquad [w]\mapsto w|_{\mathcal Z}$$
的核恰是"被 $\mathcal Z$ 消灭的 $W$ 的类"，于是
$$\delta=\dim\ker\rho_{\mathcal Z}=\dim(U\cap T),\qquad h=q+r_1-\delta .$$
从而
$$\delta\ge1\iff T\cap U\ne\{0\},$$
即"$\delta\ge1$"是 Grassmannian $\operatorname{Gr}(q,N)$（$N=n-p$）上"与固定 $a$ 维子空间 $U$ 非平凡相交"的
**Schubert 簇**；当 $q+a\le N$ 时其余维为
$$N-q-a+1=n-q-r_1+1=d-a+1 .$$
特别地 $q+r_1=n$ 时它是**除子**（余维 1），所以 $\delta=0$ 是"一般位置"，
**不能**从 $q+r_1=n$ 推出 $\delta=0$（此前 B.11 的推论 3 需按此更正）。

## 更正（2026-11-03）

* 推论 3 原文"$q+r_1=n\Rightarrow\delta=0$"**错**：由 $h\le n$ 只能得 $\delta\ge0$；
  正确说法是"$q+r_1=n$ 时 $\delta\ge1$ 是 Schubert 除子，$\delta=0$ 为一般位置"；
  "公开例子 $q=4$ 处全族 $\delta=0$"是**抽样证据**（1999/1999），符号证明仍开放。
* $(5a)$ 的精确形式是 $\operatorname{rank}\varphi=0$（$\varphi:\mathcal Z^{\perp}\to\mathbb C^n/(\mathcal Z^{\perp}+W)$），
  见 [attempts/21](../../workspace/q1_false/feasibility_geometry/attempts/21_expert_corrections.md)；
  样本核验 974/974。

## 推论（2026-11-03）：失败类型由整数决定

设 $K=\ker[C;L_0]$、$S=\operatorname{row}[C;L_0]+W$、$s_0=\dim S$。任何 $(5a)$-可行增广有
$\mathcal Z^{\perp}=K^{\perp}+V$（$V=\operatorname{span}(v_1,\dots,v_t)$、$t=q-r$），故
$$h=\dim(S+V)=s_0+\dim\pi(V),\qquad \pi:\mathbb C^n\to\mathbb C^n/S .$$
于是
$$\text{Type I}\ (h\ge q+r_1)\iff \dim\pi(V)\ge q+r_1-s_0 .$$
若 $V\cap S=0$（$\dim\pi(V)=t=q-r$），则 Type I $\iff s_0\ge r_1+r$，**与增广的选取无关**。
公开例子（$s_0=6,r_1=4,r=2,n=8$）：$q=3$ ⟹ $h=7=q+r_1$、$q=4$ ⟹ $h=8=q+r_1$（都是 Type I）、
$q=5$ ⟹ $\dim\pi(V)\le2$ ⟹ $h\le8<9$ ⟹ 整数障碍消失。验证见
[workspace/q1_false/feasibility_geometry/attempts/23_type_is_integer.md](../../workspace/q1_false/feasibility_geometry/attempts/23_type_is_integer.md)。
