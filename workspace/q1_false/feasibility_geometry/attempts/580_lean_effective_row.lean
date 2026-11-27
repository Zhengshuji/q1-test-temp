import Mathlib

/-! # 580 有效自由行例子（$k=4$）的 Lean 核验

门上子式：
$m_{12}=(\lambda-2)(\lambda-1)$、$m_{13}=-r_2(\beta-\lambda)(\lambda-1)$、$m_{23}=r_1(\alpha-\lambda)(\lambda-2)$。
若 $r_1(\alpha-1)\ne0$ 且 $r_2(\beta-2)\ne0$，则无公共根。
-/

namespace Q1Gadget580

theorem no_common_root (r1 r2 al be lam : ℚ)
    (h1 : r1 * (al - 1) ≠ 0) (h2 : r2 * (be - 2) ≠ 0)
    (m12 : (lam - 2) * (lam - 1) = 0)
    (m13 : -r2 * (be - lam) * (lam - 1) = 0)
    (m23 : r1 * (al - lam) * (lam - 2) = 0) : False := by
  have h12 : (lam - 2 = 0) ∨ (lam - 1 = 0) := mul_eq_zero.mp m12
  rcases h12 with h | h
  · have hl : lam = 2 := by linarith
    rw [hl] at m13
    have : r2 * (be - 2) = 0 := by linarith
    exact h2 this
  · have hl : lam = 1 := by linarith
    rw [hl] at m23
    have : r1 * (al - 1) = 0 := by linarith
    exact h1 this

end Q1Gadget580
