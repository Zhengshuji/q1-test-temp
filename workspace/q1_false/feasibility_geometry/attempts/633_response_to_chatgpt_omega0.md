# 633 回应 ChatGPT：$\omega=0$ 的强结论不成立，但 $\omega\le s$ 有支持

> 2026-11-27。ChatGPT 提出更强的“可行 $\Rightarrow\omega=0$”（商空间上 $\lambda I-T-K$ 必有特征值）。
> 本文件指出该论证漏掉了 $Z$ 是 $q\times q$、而限制在 $V=\operatorname{im}H$ 上的映射不是 $\lambda I-T$；
> 631 给出 $\omega>0$ 的反例；同时一个 $\omega>s$ 的数值例子支持 $\omega\le s$。
> 状态：**[已证-纸面]**（631 反例）+ **[精确验证]**（例子）。

## 631 的反例

$W$ 满行秩（$s=k$）、$q>r_0$、$q-1\le k$：可取 $H$ 秩 $q-1$、$Z$ 的特征向量避开 $V=\operatorname{im}H$，
得可行解，$\omega=q-1>0$。所以“可行 $\Rightarrow\omega=0$”不成立。

**原因**：$Z$ 是 $q\times q$，$(\lambda I-Z)|_V$ 是 $V\to\mathbb C^q$ 的映射，没有“$\omega\times\omega$ 行列式”；
只有当 $\omega=q$（$V=\mathbb C^q$）时才退化为方阵、必有特征值。

## $\omega>s$ 的数值例子（$s=1$）

$k=q=3$、$Z'=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}$（循环）、$S=\operatorname{row}(W)=\operatorname{span}\{e_1\}$（$s=1$）、
$H=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}$（$\omega=2>s$）。

约束 $ZH=HZ'+G$（$G$ 行在 $S$ 内）逐行求解：
- $H_1Z'=(0,1,0)\in\operatorname{row}H$ ⇒ $G_1=0$；
- $H_2Z'=(0,0,1)\in\operatorname{row}H$ ⇒ $G_2=0$；
- 于是 $Z=\begin{bmatrix}a&0&1\\b&0&1\\c&0&0\end{bmatrix}$（自由参数 $a,b,c$）。

$V=\operatorname{im}H=\operatorname{span}\{e_1,e_2\}$；对 $v=\beta e_2\in V$ 有 $Zv=0$ ⇒ $e_2$ 是 $Z$ 的特征向量（$\lambda=0$），
与 $a,b,c$ 无关。故 $(\lambda I-Z)$ 在 $V$ 上总有核 ⇒ $(5b)$ 失败 ⇒ **该 $H$ 不可行**。

## 现状

- $\omega=0$ 的强结论：**被 631 推翻**；
- $\omega\le s$：本例支持（$\omega=2>s=1$ 不可行），但仍需一般证明或反例；
- 直觉：$G$ 的行被限制在 $S$ 内，$\omega>s$ 时约束会把 $Z|_V$ 的某个特征方向“钉”在 $V$ 里。

## 下一步

1. 对更多 $(Z',S,H)$ 组合做符号检验，寻找 $\omega>s$ 的可行反例；
2. 若找不到，尝试证明“$\omega>s$ ⇒ 存在 $v\in V$ 与 $\lambda$ 使 $Zv=\lambda v$”；
3. 与 629/631 合并为分情形定理。

## 状态

- $\omega=0$ 强结论：**推翻**（631）；
- $\omega\le s$：**[M2 猜想]**（有支持）。
