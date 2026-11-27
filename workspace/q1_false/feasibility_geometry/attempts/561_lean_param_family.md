# 561 参数族核心矛盾的 Lean 核验

> 2026-11-27。把 560 的 $a\ne b$、$a,b\ne0$ 情形写成 Lean 定理并编译通过。
> 状态：**[Lean]**。

## 声明

文件：[561_lean_param_family.lean](561_lean_param_family.lean)（`namespace Q1Gadget561`，`lake env lean` 退出码 0）：

```
theorem no_common_root (a b u v lam : ℚ)
  (hab : a ≠ b) (ha : a ≠ 0) (hb : b ≠ 0)
  (hauv : a * u ≠ v) (hv : v ≠ 0)
  (h12 : (lam - a) * (lam - b) = 0)
  (h13 : lam * v * (lam - a) = 0)
  (h23 : -((lam - b) * (lam * u - v)) = 0) : False
```

（`ha : a ≠ 0` 未被用到——$a\ne b$ 与 $au\ne v$ 已足够；warning 仅为 linter。）

## 证明结构

1. $m_{12}=0$ ⇒ $\lambda=a$ 或 $\lambda=b$；
2. $\lambda=a$：$m_{23}=-(a-b)(au-v)=0$ ⇒ $a=b$ 或 $au=v$，均矛盾；
3. $\lambda=b$：$m_{13}=bv(b-a)=0$ ⇒ $b=0$ 或 $v=0$ 或 $b=a$，均矛盾。

## 与 560 的关系

这机器验证了 560 表格第一行“$a\ne b$、$a,b\ne0$ 时 $\gcd=1\iff au\ne v\wedge v\ne0$”的核心方向
（条件成立 ⇒ 无公共根）；另一方向（条件不成立 ⇒ 有公共根）由 560 的构造直接给出。

## 状态

- Lean：**[Lean]**（1 条声明，退出码 0）；
- 反向（有公共根）：**[已证-纸面]**（560 的显式根）。
