# 精确提升完成定理：$q-\omega\le d_C$（专家 57 号 §1）

> 2026-11-08。专家 57 号给出的关键观察：压缩子空间 $V=\ker H$ 只记录 $L$ 的行在 $K_0$ 上的限制，
> 不记录它们在 $K_0^\perp$ 方向的分量；后者正是满足 $\operatorname{rank}[C;L]=p+q$ 的自由度。
> 本文件写出精确的提升完成定理，解决前几轮卡住的算法。状态：**M2（纸面）**。

## 目标

给定压缩行 $H=LN_K$（$q\times k$，秩 $\omega$），$L_0$ 固定、$H_0=L_0N_K$，$H_1$ 为底部压缩行。
证明存在 $R$ 使 $RN_K=H_1$ 且
$$\operatorname{rank}\begin{bmatrix}C\\L\end{bmatrix}=p+q\qquad(L=[L_0;R])$$
的充要条件，并给出构造。

## 设想与理由

限制映射 $\rho:\mathcal X^*/\operatorname{row}C\to K_0^*$、$[\ell]\mapsto\ell|_{K_0}$ 的核是
$$E_C=\frac{\operatorname{row}[C;CA]}{\operatorname{row}C},\qquad d_C=\dim E_C=\operatorname{rank}[C;CA]-\operatorname{rank}C.$$
$K_0^*$ 记录压缩行，$E_C$ 记录“提升一行而不改其在 $K_0$ 上限制”的自由度——这正是 $N_K^+$ 构造漏掉的部分。

## 做法

**正合列**：
$$0\longrightarrow E_C\longrightarrow\mathcal X^*/\operatorname{row}C\overset{\rho}{\longrightarrow}K_0^*\longrightarrow0.$$

**命题（完成判据）**：设 $\operatorname{rank}[C;L_0]=p+r$。则存在 $R$ 使 $RN_K=H_1$ 且
$\operatorname{rank}[C;L]=p+q$，当且仅当
$$\boxed{q-\omega\le d_C.}$$

*证明*：取 $q$ 个压缩行到 $\mathcal X^*/\operatorname{row}C$ 的任意提升，得 $\widetilde H:\mathbb C^q\to\mathcal X^*/\operatorname{row}C$。
行类模 $C$ 独立 $\iff\widetilde H$ 单射。若 $a\in\ker\overline H^*$，则对应行组合在 $K_0$ 上为零，
故落在 $E_C$；于是有良定义的
$$\ker\overline H^*\longrightarrow E_C,\qquad a\longmapsto\widetilde H(a).$$
提升行独立 $\iff$ 此映射单射。在 $\mathcal N_0=\{(a,0):a^{\mathsf T}H_0=0\}$ 上映射由 $L_0$ 固定；
$\operatorname{rank}[C;L_0]=p+r$ 保证其已单射。底部行可在 $E_C$ 中自由调整，故可把已单射的映射
从 $\mathcal N_0$ 扩张到整个 $\ker\overline H^*$ $\iff$ $\dim\ker\overline H^*=q-\omega\le d_C$。$\square$

**构造**（专家 §1.6）：取特解 $L^{(0)}N=H$，取 $E_C$ 的基 $G$，令
$$L=L^{(0)}+\begin{bmatrix}0\\XG\end{bmatrix},$$
选 $X$ 使完成映射单射。$q=\omega+1$ 时 $\ker\overline H^*$ 一维，只需让该依赖方向的提升在 $E_C$ 中非零。

## 更正：看不见方向未必保持 $H_A$（2026-11-08，数值核实）

专家 57 号 §1.5 说“加 $\operatorname{row}[C;CA]$ 的行不改变 $H_A$”。**这不对**：若
$g=aC+bCA\in\operatorname{row}[C;CA]$，则 $gN=0$，但
$$gAN=aCAN+bCA^2N=b\,CA^2N,$$
因为 $CAN=0$（$N$ 的列在 $K_0=\ker[C;CA]$ 中），而 $CA^2N$ 一般非零。
在 seeds 10/16/21 上数值核实：$d_C=\operatorname{rank}[C;CA]-\operatorname{rank}C=3$，
映射 $g\mapsto gAN$ 在看不见空间上的秩为 **1**，故保持 $H_A$ 的自由度只有
$$d'_C=d_C-\operatorname{rank}(g\mapsto gAN)=2.$$

因此有两个判据：
* **只做秩完成**（允许改 $H_A$）：$q-\omega\le d_C$；完成后必须重新检验 $(5b)$；
* **保持压缩对**（推荐，谱性质不变）：$q-\omega\le d'_C$，其中
$$E'_C=\{g\in\operatorname{row}[C;CA]:\ gN=0,\ gAN=0\}/\operatorname{row}C.$$

构造仍为 $L=L^{(0)}+[0;XG]$，但 $G$ 应取 $E'_C$ 的基（若要保持 $H_A$）；
$q=\omega+1$ 时只需 $d'_C\ge1$。

**算法含义**：$t=2$（$V$ 不变）时 $\ker H\subseteq\ker H_A$ 自动成立；$t<2$ 时必须用提升的
off-$K_0$ 分量额外满足 $\ker H\subseteq\ker H_A$，不能只靠 $N_K^+$。

## 专家 00 号复核（2026-11-08）：确认 d'_C，并给出更一般的 T_V 版本

复核结论：$gAN=b\,CA^2N$ 的计算正确，$d'_C=d_C-\operatorname{rank}\Gamma$ 正确，
$q-\omega\le d'_C$ 是**保持压缩对**的完成判据。三个补充：

1. **固定 $L_0$ 必须显式进入定理**：用
   $$\overline{\mathcal L}_0=\operatorname{span}\{[l]:l\ \text{是}\ L_0\ \text{的行}\}\subseteq\mathcal X^*/\operatorname{row}C,$$
   把 $\overline{\mathcal L}_0$ 扩张为 $q$ 维子空间，使其在 $K_0$ 上的限制为指定像；避免把已可用的
   看不见方向重复计数。
2. **更一般的“只在 $V$ 上兼容”版本**：令 $\mathcal T_V(G)=GAN_K|_V$，$d'_C(V)=\dim\ker\mathcal T_V$。
   则 $d'_C(V)\ge d'_C$；判据 $q-\omega\le d'_C(V)$ 对应“构造一个兼容提升、再检验谱铅笔”，
   不要求保持整个压缩对。两个版本都应写出：
   * 全局保持对的完成（$E'_C$，$d'_C$）；
   * 只在 $V$ 上兼容的完成（$\mathcal T_V$，$d'_C(V)$）。
3. **“保持一个可容许对” $\ne$ “把任意对变成可容许”**：若参考提升 $L^{(0)}$ 已不满足
   $\ker H\subseteq\ker H_A$，加 $E'_C$ 的元素**不能**修复；第 4 步（$GAN_K|_V=-L^{(0)}AN_K|_V$）
   是关于 $G$ 的仿射线性方程，解集非空才是可容许提升存在的条件。

**算法含义**：正确管线是
1. 选 $H$（$\ker H=V$）；2. 取参考提升 $L^{(0)}$；3. 解仿射方程 $GAN_K|_V=-L^{(0)}AN_K|_V$；
4. 在解空间中满足 $\operatorname{rank}[C;L]=p+q$；5. 构造铅笔、检验 $(5b)$。
若第 3 步无解，该 $V$ 不可提升；若第 4 步不能同时满足，则用 $d'_C(V)$ 判定。

## 进展

* 正合列、完成判据、构造已写出（按专家 57 号 §1.2–1.6）。
* 判据把“提升 + 两个秩条件”化为**一个维数不等式** $q-\omega\le d_C$；$q=\omega+1$ 时为 $d_C\ge1$。
* 与 $(5a)$ 的关系：$(5a)\iff\ker H\subseteq\ker H_A$，只依赖压缩对，故 $E_C$ 方向的提升不破坏 $(5a)$。

## 最终结论

* 完成判据：$\operatorname{rank}[C;L_0]=p+r$ 且 $q-\omega\le d_C$；
* $q=\omega+1$：只需 $\operatorname{rank}[C;CA]-\operatorname{rank}C\ge1$；
* 这解决了前几轮“由 $V$ 构造 $L$ 失败”的卡点：失败原因是只用了 $N_K^+$，没有用 $E_C$ 的自由度。

## 放弃原因

* 未处理 $C$ 非满行秩（专家：把 $p$ 换成 $\operatorname{rank}C$）；
* 未实现/未精确验证；未 Lean 化。

## 残留价值

* $c=2$ 算法缺失的“提升层”；
* 可直接写进论文的 lifting 一节，并接 $q=\omega+1$ 的简单判据。

## 相关文件

* [attempts/114](../../c_stratification/attempts/114_lifting_lemma.md)（旧 lifting 引理，只处理 $\operatorname{rank}[L_0;R]$）
* [attempts/143](../../c_stratification/attempts/143_c2_rigorous_parameterization.md)（失败记录）
* [attempts/150](150_universal_pencil_descent.md)（统一块判据）

## 状态

* 完成定理：**[已证-纸面，M2]**（按专家 57 号的证明）。
* 实现/验证/Lean：**[未做]**。
