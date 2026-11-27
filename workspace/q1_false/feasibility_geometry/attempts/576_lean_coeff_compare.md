# 576 575 中系数比较的 Lean 核验

> 2026-11-27。575 的退化情形用到一步系数比较；本文件把它写成 Lean 定理并编译通过。
> 状态：**[Lean]**。

## 声明

文件：[576_lean_coeff_compare.lean](576_lean_coeff_compare.lean)（`namespace Q1Gadget576`，退出码 0）：

```
theorem coeff_compare (al be y a b : ℚ)
    (h : ∀ lam : ℚ, lam * al - a = lam * be * y - b * y) :
    al = be * y ∧ a = b * y
```

## 证明

- 取 $\lambda=0$：$-a=-by$ ⇒ $a=by$；
- 取 $\lambda=1$：$\alpha-a=\beta y-by$ ⇒ $\alpha=\beta y$（用上一步）。

## 在 575 中的作用

575 比较 $x$ 分量：$\lambda\alpha-a=\lambda y(\beta-b/\lambda)=\lambda\beta y-by$，
由 `coeff_compare` 得 $\alpha=\beta y$、$a=by$。
再由 $z$ 分量的 $1/\lambda$ 项得 $b=0$，于是 $a=0$，结论 $rN=\beta h_2+\gamma h_3$、$rAN\in\operatorname{span}\{a_2\}$。

## 状态

- Lean：**[Lean]**（1 条声明，退出码 0）；
- 575 的其余步骤：**[已证-纸面]**。
