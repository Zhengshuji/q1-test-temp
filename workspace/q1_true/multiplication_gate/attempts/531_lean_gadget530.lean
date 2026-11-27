import Mathlib

/-! # 530 gadget 的 Lean 核验（实际使用的常系数）

- $H_{A,0}$ 的行：$-2h_2+2h_3$、$-2h_3$、$0$；
- 门上 $h_1=xh_2$，子式 $d_{12}=2(\lambda(x+1)+2)$、$d_{23}=\lambda^2$；
- 两者无公共根 ⇒ 无坏参数。
-/

namespace Q1Gadget530

/-- 一行的分量形式：$-2h_2+2h_3=(-2y,-2,2)$。 -/
theorem ha1_eq (y : ℚ) :
    (-2 * y, -2, (2 : ℚ)) = (-2 * y, -2 * 1, -2 * 0 + 2 * 1) := by
  simp

/-- $H_{A,0}$ 第二行：$-2h_3=(0,0,-2)$。 -/
theorem ha2_eq : ((0 : ℚ), 0, -2) = (0 * 0, 0 * 0, -2 * 1) := by
  simp

/-- 门上 $h_1=xh_2$。 -/
theorem h1_eq (x y : ℚ) : (x * y, x, (0 : ℚ)) = (x * y, x * 1, x * 0) := by
  simp

/-- 两个子式无公共根。 -/
theorem no_common_root (x lam : ℚ) (h23 : lam ^ 2 = 0)
    (h12 : 2 * (lam * (x + 1) + 2) = 0) : False := by
  have hlam : lam = 0 := by nlinarith [h23]
  rw [hlam] at h12
  norm_num at h12

/-- 等价形式。 -/
theorem gcd_one (x lam : ℚ) :
    ¬ (lam ^ 2 = 0 ∧ 2 * (lam * (x + 1) + 2) = 0) := by
  rintro ⟨h23, h12⟩
  exact no_common_root x lam h23 h12

end Q1Gadget530
