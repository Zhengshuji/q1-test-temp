import Mathlib

/-! # 576 575 中的系数比较（Lean）

若对所有 $\lambda$ 有 $\lambda\alpha-a=\lambda\beta y-by$，则 $\alpha=\beta y$ 且 $a=by$。
-/

namespace Q1Gadget576

theorem coeff_compare (al be y a b : ℚ)
    (h : ∀ lam : ℚ, lam * al - a = lam * be * y - b * y) :
    al = be * y ∧ a = b * y := by
  have h0 : -a = -b * y := by simpa using h 0
  have h1 : al - a = be * y - b * y := by simpa using h 1
  constructor
  · linarith
  · linarith

end Q1Gadget576
