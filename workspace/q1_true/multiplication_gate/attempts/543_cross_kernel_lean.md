# 543 叉积核向量的 Lean 核验

> 2026-11-27。542 的非线性接口依赖“$\ker[u;v]=\operatorname{span}\{u\times v\}$”。
> 本文件用 Lean 核验三重积恒等式（叉积与 $u,v$ 正交），编译通过。
> 状态：**[Lean]**。

## Lean 声明

文件：[543_lean_cross_kernel.lean](543_lean_cross_kernel.lean)（`namespace Q1Gadget542`，`lake env lean` 退出码 0）：

| 声明 | 内容 |
|---|---|
| `dot_u_cross` | $u\cdot(u\times v)=0$ |
| `dot_v_cross` | $v\cdot(u\times v)=0$ |
| `e1_dot_cross` | $e_1\cdot(u\times v)=u_2v_3-u_3v_2=\det[e_1;u;v]$ |

（仅有未使用变量 warning，无 error。）

## 用途

- 若 $h_1\in\operatorname{span}\{u,v\}$（即 $\det[h_1;u;v]=0$），则 $u\times v$ 同时正交于 $h_1,u,v$，
  故 $\ker H=\operatorname{span}\{u\times v\}$；
- $(5a)$ 的条件 $H_A(u\times v)=0$ 因此是三个**三次**方程（$H_A$ 行线性 × 叉积二次）。

## 下一步

$h_1=e_1$、$H_A$ 取小整数矩阵：写出
$$\det[e_1;u;v]=0,\qquad H_A(u\times v)=0\ (3\ \text{条})$$
并搜索使这组条件等价于 $u_3=u_1u_2$（或某个二次关系）的 $H_A$；再用 $(5b)$ 排除其余分支。

## 状态

- 叉积核：**[Lean]**（3 条声明）；
- 三次方程组：**[未做]**。
