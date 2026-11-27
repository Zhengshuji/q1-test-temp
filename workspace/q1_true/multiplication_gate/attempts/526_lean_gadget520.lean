import Mathlib

/-!
# Q1 gadget 520：代数核心的 Lean 核验（修正版）

1. (5a) 的两个 3×3 行列式：det = 2(z-xy)、det = -4(z-xy)（只差非零常数）；
2. 门上两个 2×2 子式 M₁ = λ²+12、M₂ = xλ²+4xλ+2λ+4x-4；
3. 关键恒等式 M₂ - x·M₁ = 2(2x+1)(λ-2)，
   故 x=-1/2 且 λ²=-12 时 M₁=M₂=0 —— 公共根，`(5b)` 在 x=-1/2 失败。
-/

namespace Q1Gadget520

/-- 3×3 行列式（按第一行展开）。 -/
def det3 (a b c d e f g h i : ℚ) : ℚ :=
  a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

/-- (5a) 的第一个行列式：det[h1; h2; a1] = 2(z - x y)。 -/
theorem det_D1 (x y z : ℚ) :
    det3 z x 0 y 1 0 (-2 * (x + 1) * y) (-2 * (x + 1)) 2 = 2 * (z - x * y) := by
  unfold det3
  ring

/-- (5a) 的第二个行列式：det[h1; h2; a2] = -4(z - x y)。 -/
theorem det_D2 (x y z : ℚ) :
    det3 z x 0 y 1 0 (2 * y) 2 (-4) = -4 * (z - x * y) := by
  unfold det3
  ring

/-- 第二个 2×2 子式。 -/
def M2 (x lam : ℚ) : ℚ := x * lam ^ 2 + 4 * x * lam + 2 * lam + 4 * x - 4

/-- 第一个 2×2 子式。 -/
def M1 (lam : ℚ) : ℚ := lam ^ 2 + 12

/-- 关键恒等式：M₂ - x·M₁ = 2(2x+1)(λ-2)。 -/
theorem M2_sub (x lam : ℚ) : M2 x lam - x * M1 lam = 2 * (2 * x + 1) * (lam - 2) := by
  unfold M2 M1
  ring

/-- 退化点：x = -1/2 且 M₁ = 0 时 M₂ = 0（公共根）。 -/
theorem common_root (x lam : ℚ) (hx : 2 * x + 1 = 0) (h1 : M1 lam = 0) :
    M2 x lam = 0 := by
  have h := M2_sub x lam
  unfold M1 at h1
  have hx' : 2 * x + 1 = 0 := hx
  nlinarith [h, h1, hx']

end Q1Gadget520
