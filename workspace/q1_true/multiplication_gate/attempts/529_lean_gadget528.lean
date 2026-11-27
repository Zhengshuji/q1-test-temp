import Mathlib

/-! # 528 无坏集 gadget：Lean 核验

门上 $d_{23}=\lambda^2$、$d_{12}=2(\lambda(x-1)+2)$。
若两者同时为零，则 $\lambda=0$（由 $\lambda^2=0$）且 $d_{12}=4$，矛盾。
因此 $\gcd(d_{12},d_{23})=1$ 对所有 $x$ 成立，无坏参数。
-/

namespace Q1Gadget528

/-- 两个子式同时为零不可能（$\mathbb Q$ 上）。 -/
theorem no_common_root (x lam : ℚ) (h23 : lam ^ 2 = 0)
    (h12 : 2 * (lam * (x - 1) + 2) = 0) : False := by
  have hlam : lam = 0 := by nlinarith [h23]
  rw [hlam] at h12
  norm_num at h12

/-- 等价形式：不存在公共根。 -/
theorem gcd_one (x lam : ℚ) :
    ¬ (lam ^ 2 = 0 ∧ 2 * (lam * (x - 1) + 2) = 0) := by
  rintro ⟨h23, h12⟩
  exact no_common_root x lam h23 h12

end Q1Gadget528
