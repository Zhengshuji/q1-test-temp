# 563 第二参数族核心矛盾的 Lean 核验

> 2026-11-27。把 562 的核心方向（条件成立 ⇒ 无公共根）写成 Lean 定理并编译通过。
> 状态：**[Lean]**。

## 声明

文件：[563_lean_second_family.lean](563_lean_second_family.lean)（`namespace Q1Gadget563`，退出码 0）：

```
theorem no_common_root (a b u v lam : ℚ)
  (hab : a ≠ b) (ha1 : a ≠ 1) (hb1 : b ≠ 1)
  (hu : u ≠ 0) (hv : v ≠ 0)
  (h12 : (lam - a) * (lam - b) = 0)
  (h13 : (lam - a) * (lam - 1) * v = 0)
  (h23 : -((lam - b) * (lam - 1) * u) = 0) : False
```

## 证明结构

1. $m_{12}=0$ ⇒ $\lambda=a$ 或 $\lambda=b$；
2. $\lambda=a$：$m_{23}=-(a-b)(a-1)u=0$ ⇒ $a=b$、$a=1$、$u=0$，均矛盾；
3. $\lambda=b$：$m_{13}=(b-a)(b-1)v=0$ ⇒ $b=a$、$b=1$、$v=0$，均矛盾。

## 两个参数族的 Lean 覆盖

| 族 | Lean 声明 | 文件 |
|---|---|---|
| 560（$rAN=(v,0,w)$） | `Q1Gadget561.no_common_root` | `561_lean_param_family.lean` |
| 562（$rAN=r$） | `Q1Gadget563.no_common_root` | `563_lean_second_family.lean` |

两族都验证了“条件成立 ⇒ 无公共根”，加上纸面的显式根（条件不成立 ⇒ 有公共根），
完整覆盖了“可行 $\iff$ 等式 + 非零条件”的核心。

## 状态

- Lean：**[Lean]**（2 条声明，退出码 0）；
- 反向：**[已证-纸面]**（560/562 的显式根）。
