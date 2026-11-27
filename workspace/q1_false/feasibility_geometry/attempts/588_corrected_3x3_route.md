# 588 修正后 3×3 路线的试算：$\det P$ 不为零，构造失败

> 2026-11-27。按 587 的修正，尝试让 $\det P\equiv0$ 的某个系数等于 $r_1r_2-z$。
> **结果：手算漏了一项，实际 $\det P=-r_1\lambda(\lambda-1)\ne0$，构造失败。**
> 状态：**[已证-纸面]** + **[精确验证]**。

## 构造

$q=3$、$a_1=a_2=e_1$、$a_3=e_2$；
$$h_1=(1,0,0),\quad h_2=(1,r_1,1),\quad h_3=(0,z,r_2).$$

## 实际行列式

$$P(\lambda)=\begin{bmatrix}\lambda-1&0&0\\\lambda-1&\lambda r_1&\lambda\\0&\lambda z&\lambda r_2-1\end{bmatrix},$$
$$\det P=(\lambda-1)\big[\lambda r_1(\lambda r_2-1)-\lambda^2 z\big]
=\lambda(\lambda-1)\big[r_1(\lambda r_2-1)-\lambda z\big].$$
门上 $z=r_1r_2$：
$$r_1(\lambda r_2-1)-\lambda r_1r_2=-r_1 ,$$
所以
$$\det P=-r_1\,\lambda(\lambda-1)\ne0 .$$

**构造失败**：$\det P$ 不恒为零，$(5b)$ 在 $\lambda=0,1$ 处掉秩。

## 手算的错误

原稿把 $\det P$ 写成 $(r_1r_2-z)(\lambda^3-\lambda^2)$，漏了 $p_3$ 的 $\lambda r_2-1$ 与 $p_2$ 的 $\lambda$ 的交叉项；
精确计算给出上式。

## 教训

- 3×3 的 $\det$ 手算容易漏交叉项；**必须用 sympy 复核**；
- 即使 $\det H=r_1r_2-z$，$\det P$ 的其它项不会自动抵消；
- 下一步应先用 sympy 验证 $\det P\equiv0$，再谈 $(5b)$。

## 状态

- 构造失败：**[已证-纸面]** + **[精确验证]**（sympy：$\det=-r_1\lambda(\lambda-1)$）；
- 下一步：用 sympy 搜索使 $\det P\equiv0$ 且 $2\times2$ 子式 gcd=1 的组合。
